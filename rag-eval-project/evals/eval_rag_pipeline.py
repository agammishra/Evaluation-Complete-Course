import os
# 1. THIS MUST BE AT THE VERY TOP (Before importing deepeval)
os.environ["DEEPEVAL_TELEMETRY_OPT_OUT"] = "YES"

import json
import time
from dotenv import load_dotenv

# 2. NOW we can import deepeval safely
from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import (
    FaithfulnessMetric,
    AnswerRelevancyMetric,
    ContextualRelevancyMetric,
)

from src.rag_pipeline import RagPipeline

load_dotenv()

GOLDEN_PATH = "goldens/faithfulness_dataset.json"
JUDGE_MODEL = "gpt-4o-mini"
THRESHOLD = 0.7

# 3. LOAD queries
with open(GOLDEN_PATH) as f:
    goldens = json.load(f)

# 4. RUN THE FULL PIPELINE 
rag = RagPipeline()
test_cases = []
print("Generating pipeline responses...")

for g in goldens:
    result = rag.invoke(g["query"])
    test_cases.append(
        LLMTestCase(
            input=g["query"],
            actual_output=result["answer"],
            retrieval_context=result["context"],
        )
    )
    time.sleep(0.5)

# 5. THE THREE TRIAD METRICS
metrics = [
    ContextualRelevancyMetric(threshold=THRESHOLD, model=JUDGE_MODEL, include_reason=True, async_mode=False),
    FaithfulnessMetric(threshold=THRESHOLD, model=JUDGE_MODEL, include_reason=True, async_mode=False),
    AnswerRelevancyMetric(threshold=THRESHOLD, model=JUDGE_MODEL, include_reason=True, async_mode=False),
]

# 6. EVALUATE - MANUAL CHUNKING FIX
print("Starting evaluation in small batches...")

# Evaluate 2 test cases at a time to prevent network crashes
batch_size = 2
for i in range(0, len(test_cases), batch_size):
    batch = test_cases[i : i + batch_size]
    print(f"\n--- Evaluating batch {i//batch_size + 1} (Test cases {i} to {i + len(batch) - 1}) ---")
    
    evaluate(
        test_cases=batch, 
        metrics=metrics
    )
    
    time.sleep(2) # Give the network a break before the next batch