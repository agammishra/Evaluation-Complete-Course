# Master LLM Evaluations: The Step-by-Step Playlist for 2026

## Context
- This is the first video of a new playlist on **LLM Evals (LLM Evaluations)**.
- Part of a broader goal to prepare people for the **AI Engineer** job role — someone who builds applications/products on top of foundation models (LLMs).
- Earlier content covered: LangChain, RAG chatbots, Agents (LangGraph, CrewAI, Agno), LangSmith, Prompt Engineering, no-code tools (n8n).
- This playlist covers a less common but very important topic: **how to evaluate LLM-based applications** before deploying them.
- Common interview question: *"How do you evaluate your RAG application?"* / *"How do you evaluate your Agentic AI application?"*

---

## What is "Vibe Testing" (and why it's a problem)

**Definition**: Casually trying an LLM application with a few prompts and judging it "by feel" — no metrics, just a gut check.

> "I asked it 5–10 questions, answers looked good, so I think it works."

**Problems with Vibe Testing:**
- Informal
- Subjective
- **Not repeatable** — you can't reliably re-test the same way when you make a new version
- Only works for **personal/hobby projects**, NOT for production-grade systems

---

## 3 Real Case Studies: What Happens Without Proper Evaluation

### 1. Air Canada Chatbot Case
- A customer asked Air Canada's chatbot about a **bereavement fare discount** (after a family member's death).
- The chatbot **hallucinated** and gave wrong info: told the customer to book at full price and claim a refund later.
- Actual policy: discount must be availed *before* booking; no refund afterward.
- Customer booked based on wrong info, was denied refund, and **sued Air Canada**.
- Air Canada argued the chatbot was a "separate entity" not their responsibility.
- **Judge ruled**: A company is responsible for what its chatbot says, just like its website.
- Air Canada lost the case and had to refund the customer — resulting in bad press.

### 2. Chevrolet Dealership Chatbot Case
- A dealership's chatbot was **jailbroken** by a user (emotionally manipulated into "agreeing" to anything).
- User got the chatbot to agree to **sell a car for $1**, and it even gave a binding-sounding offer in writing.
- User posted screenshots on social media → viral negative publicity for the dealership and Chevrolet.
- Could have been avoided with proper evaluation/guardrails before deployment.

### 3. Colombian Airline / Lawyer & ChatGPT Case
- A passenger sued an airline after being injured by a service cart.
- The passenger's **lawyer used ChatGPT** to find past similar case precedents to use as evidence in court.
- ChatGPT **hallucinated fake court cases** — fabricated names, dates, and details.
- The lawyer didn't verify and presented these fake cases in court.
- Opposition found the cases didn't exist — lawyer and law firm were **fined ~$5,000** and lost the case.
- Went viral as a cautionary tale about blindly trusting LLM output.

### Key Lesson from All 3 Cases
**Evaluation is not optional — it's essential** before deploying any LLM-based system.

---

## Why is Evaluating LLM Apps Harder Than Normal Software Testing?

### Difference 1: Deterministic vs Probabilistic
- **Traditional software** is **deterministic** — same input always gives the same output.
  - Example: Calculator — 2 + 2 always equals 4.
- **LLM-based applications** are **probabilistic** — same input can give **different outputs** each time.
  - Example: Asking ChatGPT "What is overfitting in ML?" may get slightly different answers today, in 6 months, or for different users — none of them necessarily wrong.

### Difference 2: Single Benchmark vs Multi-Dimensional Checks
- **Traditional software**: Only one benchmark — **Correctness** (right or wrong, pass or fail).
- **LLM applications**: Must be evaluated across **multiple dimensions**, such as:
  - Factuality
  - Completeness
  - Tonality
  - Groundedness (is it based on real retrieved context?)
  - Latency
  - Cost
- These dimensions **vary by application** — a chatbot for one company may need different evaluation aspects than another.

**Conclusion**: Because of these 2 differences (probabilistic nature + multi-dimensional evaluation), evaluating LLM apps is **much trickier** than evaluating traditional software. This is exactly why many developers skip this step — but it's a mistake.

---

## Playlist Roadmap (~10 Topics, in order)

1. **What are LLM Evals?** — Core concept explained with an example.
2. **Landscape of LLM Evals** — Overview of techniques and tools that exist.
3. **Model Evals** — How LLMs themselves are evaluated (benchmarks, categories).
4. **Application Evals** — How LLM-based applications are evaluated.
5. **Build Your Own Eval Pipeline** — Create a golden dataset, define custom rubrics, run evals on your own app.
6. **RAG-specific Evals**
7. **Agent-based Evals**
8. **Safety-based Evals**
9. **Operational Evals** — Post-deployment monitoring (latency, tokens/sec, time-to-first-token, system load, etc.)

**Goal of the playlist**: Help you level up from "I can build an LLM app" to "I can confidently take my LLM app to millions of users" — a mindset shift, not just a skills upgrade.

# Introduction to LLM Evaluations – Model Evals vs Application Evals

## What is an LLM Eval?

**Definition**: LLM Evals are **systematic, repeatable tests** used to judge an LLM or an LLM-powered system against **clear criteria**.

Three key characteristics:

1. **Systematic** — Not random "vibe testing" (asking a few random questions and assuming it's fine). You build a proper dataset covering many edge cases and test against it.
2. **Repeatable** — Even if you change the prompt, model, retriever, or chunking strategy, you should be able to run the *same* test again and compare results (e.g., Version 1 vs Version 2).
3. **Clear Criteria** — You must define exactly what you're checking for. Example (chatbot): Is the answer correct? Simple to understand? Based on course content? Safe (no harmful/abusive language)?

⚠️ **Important myth-buster**: LLM Eval ≠ just a metric (like Accuracy, Precision, Recall from ML/DL).
LLM Eval = **the entire testing setup**, including:
- What are you testing? (e.g., the retriever, the full RAG pipeline)
- What criteria are you using?
- When are you testing? (offline vs after production deployment)
- What tools are you using? (e.g., RAGAS for RAG apps)

**Goal of an LLM Eval** is NOT to just give a score — it answers practical questions like:
- Can the model be used for this task?
- Is this system good enough to ship?
- Did Prompt v2 improve over Prompt v1?
- Is the RAG answer grounded in retrieved context?
- Is the agent completing the task correctly?
- Is the chatbot safe for real users?
- Is latency under control?

---

## Two Types of LLM Evals

> Note: "Model Evals" and "Application Evals" are **not official industry terms** — they're simplified names used here for easy understanding. In the industry, both are just called "LLM Evals."

### 1. Model Evals
- **Goal**: Evaluate the LLM itself (its raw capabilities).
- Done by big **frontier labs** (OpenAI, Anthropic, Google, etc.) when they release a new model.
- Tested using **benchmarks/leaderboards** (that's why you see "our model tops X benchmark" claims).

**8 Main Capabilities Tested in Model Evals:**
1. Reasoning
2. Knowledge (general world knowledge, up to training cutoff)
3. Basic Math
4. Coding
5. Instruction Following
6. Long Context Handling
7. Multimodal Understanding (text, image, audio)
8. Tool Use

**Popular Benchmarks:**
| Capability | Benchmark |
|---|---|
| Knowledge & Reasoning | MMLU |
| Math | GSM8K |
| Coding | SWE-Bench, HumanEval |
| Instruction Following | IFEval |
| Long Context | Needle in a Haystack |
| Multimodal | MMMU |

📌 **As an AI Engineer**, you usually won't *perform* Model Evals yourself (that's the job of frontier labs). But you **should know how to read benchmarks** — this helps you choose the right LLM (OpenAI vs Anthropic vs open-source) for your project.

### 2. Application Evals
- **Goal**: Evaluate the entire **LLM-powered application** — not just the model.
- This is the **main focus of this course** and your main job as an AI Engineer.

**Why needed?** Because in a real LLM application, the LLM is just ONE component. Other parts include:
- User Interface
- System Prompt
- Tools / APIs integrated
- Orchestration logic (e.g., LangGraph flow, branching, parallel execution)
- Guardrails
- Output parsers
- Memory & context handling
- Retrieval system, embedding model, vector database (for RAG)
- Monitoring & feedback loop after deployment

**Analogy**: A smartphone chip (Snapdragon/MediaTek) can benchmark high — but that alone doesn't make a good phone. You also need a good camera, OS, sound system, graphics, battery, etc. Similarly, a good LLM alone doesn't guarantee a good application — the whole system around it needs to work well and be tested.

**Application Evals check at 2 levels:**
- **Whole system level** — e.g., final response quality, latency, cost per token
- **Component level** — e.g., is the retriever working well? Is the embedding model working well? Is the reranker working well?

**Key distinction**:
- Model Eval asks → *"Can the model do this?"*
- Application Eval asks → *"Will my product work correctly?"*

**Example questions Application Evals answer** (for a course chatbot):
- Was the student's question answered correctly?
- Was course material used properly?
- Was the answer faithful (no hallucination)?
- Was it easy for a beginner to understand?
- Was the response fast enough?
- Is the chatbot safe?

💡 **Rule of thumb**: When you see "LLM Evaluation" content online, 99% of the time it's talking about **Application Evals**, not Model Evals.

# How to Evaluate LLM Applications: The Complete Workflow

## Quick Recap (Why, What, How)
- **Why**: We studied why LLM evals matter.
- **What**: LLM Evals have 2 types — **Model Evals** and **Application Evals**.
- **How**: This lecture explains **how to evaluate an LLM application** (from the Application Eval point of view, not Model Eval).

---

## Example Used: Email Classifier for Zomato

**Problem**: Zomato gets many customer emails daily. Manually replying is hard.

**Solution**: Build a simple LLM system that:
- Reads the email
- Classifies it as → **Billing**, **Technical**, or **General**
- Routes it to the right team automatically

This system took just 5–10 minutes to build. But before deploying it live, **it must be evaluated**.

---

## The LLM Application Eval Workflow (Step-by-Step)

### 1. Define the Task & Target
Decide what you're evaluating.
- **Target**: The whole email classification system
- **Task**: Check if it classifies emails correctly

### 2. Define a Success Criteria
Decide how you'll know it's working well.
- **Success criteria**: Correct classification
- **Metric**: **Accuracy** (e.g., 90 out of 100 emails classified correctly = 90% accurate)

### 3. Build a Dataset (Golden Dataset)
Create a dataset with:
- Email content (input)
- Correct label (manually assigned) — Billing / Technical / General

Example:
| Email | Label |
|---|---|
| "My card was charged twice" | Billing |
| "The app crashes on login" | Technical |
| "What are your hours?" | General |

- Usually 50–500 rows.
- Best source: real past chats/emails, labeled manually.
- This labeled dataset = **Golden Dataset**.

### 4. Define an Evaluation Method
Decide **who/what checks the results**. Three options:
1. **Automated** (code/script) — good for simple tasks like classification
2. **Human** — good but costly, used when comparing long text answers
3. **LLM as judge** — middle ground, used for comparing complex text answers

> For simple classification (like Billing/Technical/General), **automated (Python code)** is enough.
> For comparing long paragraph answers (like chatbots), automated code doesn't work well — you need Human or LLM evaluation.

### 5. Run the Model
Send your dataset through the system → system generates outputs/predictions.

### 6. Evaluate the Results
Compare system's output vs the correct labels → calculate accuracy.
Example: 80% accuracy (80 correct out of 100).

### 7. Analyze the Results
Find out **where and why** mistakes are happening. Common fixes:
- **Improve the system prompt** (maybe it's confusing Billing vs Technical)
- **Change the model** (maybe the current LLM is too weak/small)

### 8. Improve the System
Apply the fix (better prompt or better model).

### 9. Iterate (Repeat the Loop)
Run evaluation again on the same dataset:
- Prompt fixed → Accuracy improved to 90%
- Model upgraded → Accuracy improved to 95%
- Keep looping until results are satisfactory.

### 10. Deploy
Once happy with performance, deploy the system live.

### 11. Monitor (Even After Deployment)
Deployment isn't the end. Keep monitoring for real-world failures.
- Example: A billing email gets wrongly routed to Technical team in production.
- Technical team flags this mistake.

### 12. Feedback Loop
Take the failed real-world example → **add it back into the Golden Dataset** → re-run the whole evaluation cycle again.

This makes the Golden Dataset richer over time, and the system keeps improving continuously.

---

## Key Takeaways

- This same workflow applies not just to simple apps, but also to **RAG systems** and **AI Agents**.
- **One LLM application can have multiple evals**, not just one.
  - Example (RAG app): separate evals for Retriever performance, Embedding model performance, full RAG workflow, and System latency.
- Evaluation is a **continuous loop** — it never really "ends" as long as the system is in production.

---

## Full Workflow Summary (One-Line Steps)

1. Define Task & Target
2. Define Success Criteria
3. Build a Dataset
4. Define Evaluation Method
5. Run the Model
6. Evaluate the Results
7. Analyze the Results
8. Improve the Model/System
9. Iterate (repeat 5–8)
10. Deploy
11. Monitor
12. Feed production failures back into dataset → repeat

# Why Your AI Application Needs Multiple Eval Pipelines?

## Quick Recap of Previous Session
The course has covered one session so far, with 3 key points:
1. **Why do we need LLM Evals?** — Deploying an LLM app without evaluation can cause many problems.
2. **What are LLM Evals?** — A systematic and reliable way to test LLMs and LLM-based apps against clear criteria.
   - **Model Eval** → Evaluating the LLM itself (uses benchmarks, mostly done by frontier labs).
   - **Application Eval** → Evaluating the app you built using an LLM (this is what AI engineers focus on most).
3. **How evals work** — A basic step-by-step eval pipeline was shown.

**Key line from last session:** One LLM application usually needs **multiple** eval pipelines, not just one.

---

## Today's Topic: Why Do We Need Multiple Eval Pipelines?

### Example: A RAG Chatbot
A basic RAG (Retrieval-Augmented Generation) chatbot has 2 main parts:
- **Retriever** → fetches relevant documents from a vector database based on the user's query.
- **Generator (LLM)** → uses the query + retrieved documents to generate the final answer.

### Reason 1: Multiple Failure Points

An LLM application can fail at several different places, not just one.

**Component-Level Failures**
- Retriever might fetch wrong/irrelevant documents.
- Generator might ignore correct documents and hallucinate.

➡️ So you need **separate evals** for the Retriever and the Generator.

- **Retriever eval** checks: *"Given a query, are the right/relevant documents being retrieved?"*
- **Generator eval** checks: **Faithfulness / Groundedness** — *"Is the answer based only on the given context, without adding made-up facts?"*

**Example:** If context says "ML course duration is 3 weeks," the answer must say exactly that — not add extra unrelated info.

### But Wait — Is That Enough?

**Scenario:**
- User asks: "What is the duration of the ML course?"
- Retriever fetches top 5 documents (K=5). The correct answer ("ML course = 8 weeks") is in the **5th (last) document**.
- Retriever technically did its job (correct answer *was* in the top 5).
- Generator was told to prioritize the *higher-ranked* documents (D1–D4).
- D1–D4 happened to mention "Python course = 6 weeks."
- Generator picks this and wrongly answers: "ML course = 6 weeks." ❌

**Conclusion:**
- Retriever worked fine individually ✅
- Generator worked fine individually ✅
- But the **combined pipeline still failed** ❌

➡️ This means you also need a **Workflow-Level Eval** — to check how components work *together*, not just individually.

**Fix in this example:** Add a **re-ranker** — it reorders retrieved documents so the most relevant one (D5) moves to the top before generation.

### Still Not Enough? — Application-Level Eval

Even if:
- Retriever works ✅
- Generator works ✅
- Retriever + Generator combo (workflow) works ✅

...the app can still fail! Example: the app takes **10 seconds** to respond — too slow for production.

➡️ This means you also need an **Application-Level Eval** — checking things like **latency**, cost, etc., for the whole system.

### Summary: 3 Levels Where Failures Can Happen
| Level | Examples of What Can Fail |
|---|---|
| **Component Level** | Prompt, retriever, re-ranker, query rewriter, embedding model, vector DB, output parser, tool selector, memory, guardrails |
| **Workflow Level** | How components interact — e.g., RAG workflow, agent workflow, multi-turn chatbot workflow |
| **Application Level** | Overall latency, token cost, time-to-first-token, etc. |

Each of these needs its own eval pipeline.

---

## Reason 2: Multiple Risk Categories

Even within one failure point, there can be multiple *aspects* to check — called **Risk Categories**. These are grouped into 3 broad types:

### 1. Application Quality
Does the app do its actual job well? (correct, relevant, complete answers)

**General LLM Apps:**
- Correctness & Accuracy
- Relevance
- Completeness
- Instruction Following (format/length followed correctly)

**RAG-specific:**
- Context Relevance
- Retriever Recall
- Groundedness / Faithfulness
- Citation Accuracy

**Agent-specific:**
- Tool Selection (right tool for the job)
- Parameter Correctness
- Task Completion
- Error Recovery

**Multi-turn Chatbot-specific:**
- Context Retention (remembers past conversation)
- Clarification Behavior (asks when confused)

### 2. Safety
Ensures answers are not harmful.
- Toxicity
- Harmful Content (self-harm, weapons, illegal activities)
- Bias (treats all users fairly)
- Private Data Leaks (e.g., someone's contact info)
- Prompt Injection / Jailbreak Resistance

### 3. Operations
Checks how well the app runs in production.
- Latency
- Cost per request
- Token Efficiency
- Error/Failure Rate
- Latency under load

---

## Final Takeaway

Because of:
1. **Multiple failure points** (component, workflow, application levels), and
2. **Multiple risk categories** (quality, safety, operations)

...almost every LLM application (99.99% of the time) needs **more than one eval pipeline** — each one checking a different component, workflow, or risk category.

# LLM Eval Methods | LLM-as-a-Judge | Reference Based Evals Vs Reference Free Evals

## 1. What is an LLM Eval Method?

**Definition:** An LLM Eval Method is the *mechanism* you use to decide whether an LLM's output is good or not. It is the actual procedure that takes an output and produces a judgment about it.

- We build evaluation pipelines to check whether a component, workflow, or the entire application is working correctly.
- But an evaluation pipeline has to be **carried out by someone/something**. That "someone/something" is the **method**.

### The Three Core Eval Methods
Every evaluation pipeline uses exactly **one** of these three methods to execute the evaluation:

| # | Method | Who/What executes it |
|---|--------|----------------------|
| 1 | **Programmatic / Deterministic** | A program/code |
| 2 | **Human** | A human evaluator |
| 3 | **Model-graded / LLM-graded** | An LLM |

> Simple way to remember it: When you run your eval pipeline, ask — *"Who is actually executing this evaluation?"* A program, a human, or an LLM. That's it — nothing else.

---

## 2. Example 1 — Programmatic (Deterministic) Evaluation

**Scenario:** Building a RAG chatbot for "Campus X" so users get help without needing manual email replies.

### Step-by-step process:
1. **Define Task & Target**
   - Task: Check if the **Retriever** component works correctly.
   - Target: A single component — the Retriever (not the whole app).

2. **Define Success Criteria**
   - A retriever's job: given a question, fetch the most relevant documents from the vector database.
   - Success is measured using **Recall@k**.

   **Recall@k definition:** *Out of all the correct/relevant items that exist, how many did the system retrieve in its top-k results?*

   **Worked Example:**
   - Question: "What are the prerequisites for the ML course and how long is it?"
   - Correct documents (ground truth): Doc 1001 and Doc 1003
   - Retriever fetches top k=5 docs: 1001, 1002, 1004, 1105, 1106
   - Correct docs retrieved = 1 (only 1001)
   - **Recall = 1/2 = 50%**
   - Ideal recall = 100% (can't be more than 100%, can't be negative)

   *(Other related metrics exist too — Precision, Rank-based metrics — but for this discussion we keep it simple with Recall@k.)*

3. **Build a Dataset**
   - Collect 50–100 realistic questions users might ask (mix of easy, hard, edge-case, random questions).
   - A **human expert** goes through the vector database and manually identifies which document(s) hold the correct answer for each question.
   - This creates the **Golden Dataset** (ground truth reference).

4. **Define the Evaluation Method**
   - This part is **programmatic**: a script sends each of the 50 questions to the retriever, gets back top-k documents, and compares them against the golden answers.
   - Recall is calculated **per question**, then **averaged** across the whole dataset to get overall Recall@k.
   - Example result: **67% average recall**.

5. **Iterate & Improve**
   - Study questions where recall was poor.
   - Ways to improve the retriever:
     - Improve/change the **embedding model**
     - **Query expansion** (use an LLM to expand the user's query before retrieval)
     - Increase the value of **k**
     - Add a **re-ranker** (a document that was outside top-5 but inside top-10 might get pulled up to top-3)

### Key takeaway:
- No human was needed to *run* this evaluation — only a human was needed to *create* the golden dataset (a one-time, separate activity).
- Since a program alone could measure success, there was no need to involve costly humans.
- **Relevancy can have multiple aspects:**
  1. How many correct docs were retrieved out of all correct docs (this is what Recall@k measures)
  2. How many retrieved docs were irrelevant/not useful
  3. Whether the retrieved docs were properly ranked

---

## 3. Example 2 — Human-Based Evaluation

**Scenario:** A general-purpose Campus X chatbot that answers any question (course launch dates, fees, certificates, validity, etc.). We're evaluating **application quality / helpfulness**, not safety/ops.

### Step-by-step process:
1. **Define Task & Target**
   - Target: The **entire application** (not one component).
   - Task: Evaluate its **helpfulness**.
   - **Helpfulness = Accuracy + Right tone + Completeness of the answer.**

2. **Define Success Criteria**
   - Tricky because there's no single "correct metric" for helpfulness — it varies business to business.
   - Solution: Define a **rubric** — e.g., a 1–5 helpfulness scale:
     - **5** = Accurate, complete, correct tone
     - **3** = Partially helpful
     - **1** = Not helpful at all / off-topic

3. **Build a Dataset**
   - 50–100 questions covering normal, difficult, and edge cases.
   - Dataset here has only **one column**: the question being asked. (No "correct answer" column — this is important, see Reference-Free section below.)

4. **Define the Evaluation Method → Human**
   - Since helpfulness is too nuanced for a program to judge automatically, a **human** must evaluate it.
   - Process: Each question → sent to chatbot → chatbot generates answer → **human evaluator** reads the question + answer → assigns a score based on the rubric. Repeat for the whole dataset.
   - Multiple graders (Grader A, Grader B) are often used.
     - **Why use more than one human grader?** If their scores disagree a lot on many questions, it signals **ambiguity in the rubric** — the criteria/instructions need refining. High agreement = clear rubric; low agreement = rubric needs work.
   - Finally: average all scores → **overall Helpfulness Score**.

### The 5 Types of Human-Involved Evaluation
Humans don't evaluate LLMs in only one way. Five types:

1. **Direct Grading & Rating** — the example above (score an answer against a rubric).
2. **Red Teaming** — a group deliberately tries to attack/break an LLM system to find failure points before launch; issues are sent back to the dev team to fix.
3. **A/B Testing** — two chatbot versions are deployed to production; real users rate their experience; the better-performing version is rolled out fully. (Users evaluate the app in production.)
4. **Golden Dataset & Rubric Creation** — when humans define correct answers/rubrics (as seen in Example 1 and 2's dataset-building steps), that itself is a form of evaluation.
5. **Human-in-the-Loop** — for very complex/ambiguous cases where neither programmatic nor LLM-based checks can be trusted, the judgment is passed to a human.

### Advantage vs Disadvantage of Human Evaluation

| Advantage | Disadvantage |
|-----------|---------------|
| High **reliability** — human judgment/reasoning is trusted much more than a program or LLM | High **cost** — you have to pay people; not feasible at scale (millions of users) |

---

## 4. Example 3 — LLM-as-a-Judge (Model-Graded Evaluation)

**The Gap:** What if the task is too *ambiguous* for a program to check (like "how helpful is this answer"), but also too *expensive/impossible* to have humans check at scale? The middle ground = **LLMs** — combining programmatic speed/scale with human-like judgment. This is the most useful and most commonly used method in real LLM eval pipelines.

**Scenario Setup:** "Campus X UPSC" — a platform preparing students for India's UPSC exam (Prelims: MCQ-based; Mains: subjective/written answers; then Interview).

**The Business Problem:**
- Automating Prelims evaluation (MCQ) is easy.
- Automating Mains evaluation (subjective answers) is hard — needs subject matter experts (SMEs).
- If 10,000 students take a mock Mains test, hiring enough SMEs to grade all answers is very costly and reduces profitability.
- Solution: Use a platform that evaluates subjective answers using an **LLM-based system** against defined rubrics, at a fraction of the cost — for any number of students.

### Step-by-step process:
1. **Define Task & Target**
   - Target: The evaluation platform itself.
   - Task: Check whether it grades papers correctly — like a human expert would.

2. **Define Success Criteria**
   - Success = **the platform evaluates answers exactly the way a human expert would.**

3. **Build a Golden Dataset**
   - **Step A — Define a rubric per question.** For example, for a question on "Ethical governance is impossible without administrative accountability," an expert defines 5 dimensions a good answer should cover (e.g., discusses ethics & accountability, explains the link between them, gives mechanisms, cites examples, has a balanced conclusion).
   - **Step B — Collect real student answers** (50–100 samples) for these questions.
   - **Step C — A human evaluator scores each answer** against the rubric (checking which dimensions are covered) and assigns marks (e.g., 13/15, 4/15, etc.).
   - This human-scored data becomes the **Golden Dataset**.

4. **Define the Evaluation Method → LLM**
   - A program can't directly judge subjective essay quality, and humans are too costly at scale → so the evaluation method is an **LLM**.
   - The LLM is given:
     - Role instruction: *"You are a grader evaluating a UPSC Mains answer against an evaluation rubric."*
     - The question
     - The marks allotted to the question
     - The exact rubric for that question
     - The student's actual written answer
     - Instructions: *for each rubric dimension, decide if the answer genuinely addresses it, allocate marks accordingly; don't reward verbosity/keyword-stuffing/unsubstantiated confident claims; do reward structure, relevant examples, and balanced argumentation.*
   - Output: LLM gives total marks + a short justification/reasoning for the score.

5. **Compare LLM vs Human Scores**
   - For every answer, you now have two columns side by side:
     - Marks given by the **human**
     - Marks given by the **LLM**
   - **Goal:** These two columns should be as similar as possible. If they match closely, the LLM system is grading just like a human would.

6. **The Metric: MAE (Mean Absolute Error)**
   - Formula: Take the absolute difference between human score and LLM score for each answer, sum them all, divide by number of answers.
   - Example: MAE = 2.3 means *on average, the LLM's grading deviates from the human's by ±2.3 marks.*
   - **Goal: bring this number down toward 0.** MAE = 0 would mean the LLM grades exactly like a human.

7. **Iterate to Improve**
   - Use a better/stronger LLM
   - Improve the system prompt
   - Refine the rubric

---

## 5. Reference-Based vs Reference-Free Evaluation

| Type | Definition | Example from above |
|------|------------|---------------------|
| **Reference-Based** | You have a known correct answer/reference written down in advance for each test case; you grade by comparing output against this reference. | • Retriever example (we already knew which docs were correct) <br> • UPSC LLM-judge example (human's score = the "correct" reference to match) |
| **Reference-Free** | There is no predefined correct answer. You judge output quality directly against a criteria/rubric (a scale/standard), not a per-item correct answer. | Chatbot helpfulness example (no correct answer given — human relies on judgment + rubric to assign a 1–5 score) |

**Quick test:** Ask — *"Does my golden dataset give me the correct answer beforehand?"*
- Yes → Reference-Based
- No → Reference-Free

---

## 6. Offline vs Online Evaluation (brief mention — to be covered next)

- Everything discussed above (Recall@k, helpfulness scoring, LLM-as-judge) is essentially **Offline Evaluation** — done before/outside of live production use.
- **Online Evaluation** = evaluation that continues *after* the system goes live in production (e.g., A/B testing in production is one example touched on earlier). This topic is to be covered in more depth next.

---

## Quick Summary Table

| Eval Method | Who Executes | Example Used | Reference Type |
|-------------|---------------|----------------|------------------|
| Programmatic/Deterministic | A program/code | Retriever eval using Recall@k | Reference-Based |
| Human | A human evaluator | Chatbot helpfulness rating (1–5) | Reference-Free |
| Model-Graded (LLM-as-a-Judge) | An LLM | UPSC Mains answer grading (compared via MAE) | Reference-Based |

# Offline Evals Vs Online Evals

## Quick Recap (What We Covered Before)
1. Why we need evals
2. What evals are (Model-based & Application-based)
3. What an eval pipeline looks like
4. Why we need **multiple** eval pipelines for a single application (multiple failure points: component, workflow, application level; and multiple risk categories: quality, safety, operations)
5. Different eval methods: Programmatic, LLM-as-a-judge, Human evaluation

## Today's Topic
**Offline Evals vs Online Evals** — a very important distinction.

---

## Part 1: Offline Evals

### Simple Definition
> If you run any eval pipeline on your LLM application **before deploying it**, that's called an **Offline Eval**.

- Good news: You already know this! Everything covered in past sessions (like the UPSC paper-grading example, where we built a golden dataset and used LLM-as-a-judge) — that's all Offline Eval.
- Happens **after the software is built, but before deployment**.

### 3 Main Benefits of Offline Evals

**1. Pre-release Testing**
- Lets you test thoroughly before shipping — catch issues before they cause real-world harm (recall Air Canada & ChatGPT case studies from earlier)
- Can be automated as a **release gate** using CI/CD: e.g., "if eval score > 95%, auto-deploy; if below, block deployment and notify the team"

**2. Version Comparison**
- Say you're unsure whether to use Claude or OpenAI's model for your app. Everything else stays the same — only the model changes.
- Run the **same eval** (same golden dataset) on both versions → whichever scores higher, you pick that one.
- Works for comparing: different prompts, different models, different rerankers, different vector databases, different architectures — anything!

**3. Regression Testing**
- **Regression** = when improving one thing accidentally breaks something else
- Example: You tweak the system prompt to make the chatbot "kinder," but now it becomes overly soft even on factual answers (e.g., quoting a vague price instead of the exact number)
- Solution: Keep a golden dataset covering **all types of cases** (refunds, pricing, curriculum questions, etc.). After any change, re-run the eval — if one category's score suddenly drops (e.g., refund questions go from 90% to 80%), that's a red flag of regression.

### Summary
> Offline Eval tells you: **"Is my application working correctly?"**

---

## Part 2: Why Offline Evals Aren't Enough — Production Risks

Once deployed, 3 major risks emerge that offline evals **cannot** catch:

### 1. Unanticipated Inputs
- Your golden dataset only covers questions you *anticipated* (e.g., 200-500 sample questions)
- Real users will ask anything: Hindi-English mixed language, ambiguous half-questions, angry rants, adversarial prompt injections — a much bigger "superset" of inputs than what you tested

### 2. Emergent & Systematic Failures
- Problems that **only appear at scale** in production, never visible offline
- Examples:
  - Sudden traffic spike (thousands of concurrent users) → latency increases — you can't simulate this offline
  - Subtle bias that "only becomes visible across thousands of conversations" (e.g., chatbot responds worse to non-technical users) — needs large-scale real data to detect

### 3. Drift
- Over time, your **offline eval setup becomes obsolete** because the real world changes but your test data doesn't
- Example: Course pricing, curriculum, and policies change over a year, but your golden dataset was built for the old documents
- Result: offline eval still shows good scores (testing against stale data), but real users give negative feedback because the actual current answers are now wrong
- This is the most technical/subtle of the three risks

### Why Offline Evals Can't Cover These
> Offline evals need a **golden dataset with correct answers**. In production, users can ask ANYTHING — you don't have a pre-written correct answer for a question you've never seen before.

---

## Part 3: Online Evals

### Simple Definition
> Online Eval = evaluating your system on **live production traffic**, after deployment, as real users interact with it.

- **Biggest characteristic:** Works **WITHOUT an answer key** (no golden dataset)
- Purpose: Make sure your deployed software keeps running properly

### Key Insight: Correctness vs. Normality
> **Offline Eval tells you if your application is working CORRECTLY.**
> **Online Eval tells you if your application is working NORMALLY** (as expected, without any given the moment's answer key).

**Example (UPSC grader):**
- Offline: We checked if our AI grader's scores were close to a human grader's scores (this needs the human's actual marks — a "correct answer")
- Online (after deployment): We have NO human-given marks to compare against for new answers. We CANNOT measure "correctness" here.
- What we CAN do: Compare the **distribution of scores** this week vs. last week. If suddenly scores jump much higher/lower than the established baseline pattern, that's a signal something changed — but not proof of what changed. It just tells you something is *abnormal*, prompting investigation.

### Alternative Correctness Signals (when no answer key exists)
Even without a golden dataset, some signals can approximate correctness:
- **Faithfulness** (RAG apps): Was the answer actually grounded in the retrieved context? This can be checked without knowing the "correct" answer — just check if the generated answer matches the provided context.
- **User feedback**: Thumbs up/down. A sudden spike in thumbs-down signals something is wrong.

---

## Offline vs Online: Key Differences Table

| Aspect | Offline Eval | Online Eval |
|---|---|---|
| **Timing** | Before deployment | After deployment (continuous) |
| **Data** | Fixed golden dataset (you create it) | Live production traffic |
| **Answer key** | Yes (golden dataset with correct answers) | No — estimated on the go |
| **Input scope** | Only anticipated inputs | Anything can come |
| **Catches** | Regressions | Drift, surprises, emergent bugs |
| **Best for** | Release gating, version comparison | Drift detection, real-world health monitoring |
| **Cost/Speed** | Fast, cheap, repeatable (small dataset) | Can be costly at scale (needs sampling) |

> ⚠️ Important: These two are **NOT rivals** — they are **complementary**. You always need both running together.

---

## Part 4: How an Online Eval Pipeline Actually Works

### Step 1: Logging
- **The most critical first step.** You must record every conversation happening in production, or you'll have nothing to evaluate.
- What to log for every conversation turn:
  - Conversation ID, Turn ID, User ID, Session ID, Timestamp
  - The user's question
  - Retrieved context (for RAG apps)
  - The model's output
  - Operational data: latency (ms), prompt tokens, completion tokens, total cost, errors/status codes
  - Behavioral signals: thumbs up/down, escalations, repeated rephrased questions

**Tool used:** LangSmith (an observability tool) — stores all conversations with full metadata.

### Engineering Properties of Good Logging
1. **Non-blocking** — logging shouldn't add latency to the actual chat response
2. **Durable & Queryable** — stored in a proper data warehouse/observability tool so you can fetch it anytime
3. **Late signal attachment** — some signals arrive later (e.g., user escalates via email a day after the chat) — must still be linked back to the original conversation ID
4. **PII Handling** — mask/redact sensitive personal info (phone numbers, card numbers, addresses) before storing, to protect privacy

---

### Step 2: Identify What Signals to Track

Two categories of signals:

**A) Captured Signals** (already present — just store them, no calculation needed)
- Examples: Thumbs up/down, latency, token usage, cost per conversation

**B) Computed Signals** (need to be calculated using an evaluator)
- Examples: Faithfulness, answer relevance, correctness, hallucination rate, toxicity, bias & fairness

---

### Pipeline for Captured Quantities (simpler)
```
Log → Dashboard → Alerting
```
- Log the value directly (e.g., latency = 2.03 sec) → send straight to a dashboard
- Dashboard shows trends over time (last 1 hour / 24 hours / 1 week / 6 months)
- Set up **alerts** (Slack, email, etc.) when a threshold is crossed (e.g., latency > 4 seconds) so an engineer can respond quickly
- Important: Look at **aggregated** trends (e.g., average latency over the last hour), not a single conversation in isolation

### Pipeline for Computed Quantities (more complex)
```
Log → Sample → Evaluate (LLM-as-a-judge) → Dashboard → Alerting
```
Example: Detecting **hallucination rate** in real time
1. Log all conversations (e.g., 500/day)
2. **Sampling** — Running an LLM-as-a-judge on ALL conversations is too expensive (doubles your cost). So you randomly sample a subset (e.g., 1,000 out of many) to evaluate.
3. This is a **Reference-Free Evaluation** (no golden answer exists — you're checking hallucination on a live, never-before-seen answer using an LLM-as-a-judge with a detailed rubric)
4. Compute the metric (hallucination rate) on the sample
5. Send that number to dashboard → set up alerts as before

### Smarter Sampling: Stratified Sampling (better than random)
Instead of pure random sampling, prioritize conversations more likely to have problems:
- Conversations with **thumbs-down**
- Conversations that ended **abruptly**
- Conversations with **escalations**
- Conversations where the user **repeated/rephrased** the same question
- Conversations about **sensitive topics** (refunds, pricing, admissions)

> Divide conversations into categories, then sample MORE heavily from "problematic" categories and less from normal ones — increases the chance of actually catching real issues.

---

## The Self-Improving Loop (Important Concept!)

Offline and Online evals work together in a continuous cycle:

```
Offline Eval → Deploy → Production (Online Eval monitors it)
        ↑                              │
        │                              ▼
        └── Failures identified → Added to offline golden dataset
```

- When a production failure is found (via online eval or user reports), that conversation gets **added to the offline dataset** (in tools like LangSmith, there's an "Add to Dataset" button)
- Next time you run offline evals, you test against this improved/updated dataset
- This closes the loop — offline and online evals continuously improve each other over time

---

## Tool Demo: LangSmith
- A complete evaluation platform supporting both:
  - **Online Evaluators** → run on "Tracing" (live logged conversations)
  - **Offline Evaluators** → run on a "Dataset" (fixed golden dataset)
- Comes with pre-built evaluator templates: PII leakage, prompt injection detection, code injection, toxicity, bias & fairness, hallucination, correctness, conciseness, and more — most use LLM-as-a-judge internally
- Has built-in dashboards (latency, error rate, LLM call count, cost graphs) and an alerting system (connects to Slack, PagerDuty, or custom APIs)
- You can annotate problematic conversations and add them directly to your offline dataset from the same interface

---

## Key Takeaway
> **Offline Eval = "Is my application correct?"**
> **Online Eval = "Is my application behaving normally right now?"**

Both are essential and work together continuously — offline evals gate releases and catch regressions before deployment; online evals catch drift, scale-related issues, and unexpected real-world behavior after deployment. Failures caught online should be fed back into the offline dataset to keep improving the system.

# LLM Model Evals & Capabilities

## Quick Recap (What Was Covered Before This Session)

1. **Why do we need LLM evals?** — introduced the basic motivation.
2. **What exactly are LLM evals?** — two types exist:
   - **Model Evals**: used to evaluate LLMs themselves (their raw capabilities).
   - **Application Evals**: used to evaluate LLM-based applications (like RAG systems, agents, etc.). This course's **main focus** is on Application Evals.
3. **Eval Pipeline** — how evals work as a process.
4. **Why do we need multiple eval pipelines?**
5. **Online Evals** — how to keep evaluating an application even *after* it has been deployed.

This session shifts focus to **Model Evals** — evals used to test an LLM's own capabilities directly. This topic will be split across **two lectures**:
- **Today**: LLM Benchmarking (what benchmarks are, how they work, famous ones, how to read them)
- **Next session**: How to run your own **custom model evals**

---

## Why Do AI Engineers Need Model Evals?

The general reason model evals exist: **to measure the capabilities of LLMs** — because "if you can't measure it, you can't improve it."

But the more important question for this course: **Why does an AI engineer (not a frontier lab) need model evals?** Frontier labs (OpenAI, Anthropic, etc.) need them to guide training. But if your day-to-day job is *building applications* using LLMs, why do you care?

Four concrete reasons:

### 1. To Compare and Choose Between Models
When building an application, you must decide which LLM to use (e.g., OpenAI vs Claude). In a professional setting, "just use whichever" is not an acceptable answer — you need **concrete evidence**. Model evals give you data-backed pointers: "this capability matters for our app, and this model scores higher on it, so we should choose it."

### 2. To Track Whether New Models Are Actually Better
New model versions get released constantly (e.g., a team using Claude Opus 4.8 wants to know if switching to a newer model like Claude Fable is worth it). You can't just "feel" that a new model is better — you need eval numbers to **justify** the switch (or the decision not to switch).

### 3. To Judge Safety
Model evals tell you:
- How much the model hallucinates
- How safe it is to use
- Whether it can be jailbroken

### 4. To Decide: Self-Host vs Use Existing APIs
Should you use a proprietary LLM (like Claude) via API, or pull an open-source model (like DeepSeek) from Hugging Face and host it yourself? Proprietary models may be more expensive but more powerful; open-source may be cheaper but less capable in some areas. This trade-off comparison is only possible **through model evals**.

> **Bottom line**: Without model evals, you are essentially "blind" — you have no reliable way to compare models or judge which one fits your needs.

---

## What Exactly Is a Model Eval? (Formal Definition)

> A model eval is a **systematic process of measuring an underlying model's capabilities, behavior, reliability, and operational characteristics under controlled conditions.**

In simple terms: it's a structured process to test what an LLM can do and how it behaves.

### The 4 Steps of Every Model Eval

No matter what type of model eval you're doing, it always follows these 4 steps:

1. **Decide the capability to test** — LLMs are general-purpose models with many capabilities (reasoning, coding, safety, instruction-following, etc.). Unlike humans (where a single IQ score tells you a lot), there is no single score that captures an LLM's overall ability. Each capability needs its own separate eval.
2. **Bring in a test** — create or select a test/mechanism designed to measure that specific capability.
3. **Run the model under a fixed protocol** — run the model through the test under fixed, controlled conditions (same prompt style, same settings) so the process is repeatable and fair when comparing multiple models.
4. **Score and interpret** — once the test is done, calculate a score and interpret what it means.

---

## Two Types of Tests Used in Model Evals

### A. Benchmarks
- **Standardized, shared tests** that everyone uses (e.g., MMLU, SWE-bench).
- Since every model is run on the *same* test, benchmarks are great for **comparing models on common ground**.
- Scores are publicly recognized and easily comparable.

### B. Custom Evals
- Data **assembled from your own actual task/use case**.
- Measures what *you specifically* care about, rather than generic usefulness.
- Necessary because benchmark performance doesn't always predict real-world task performance for *your specific application*.

### Example: Why Custom Evals Matter (Zomato Email Routing Case)

Imagine building a system that reads incoming customer emails and classifies them (e.g., Billing, Technical, Refund) and routes them accordingly. You're choosing between two models:

| | Model A (Big) | Model B (Small) |
|---|---|---|
| Position on public benchmarks | Top of leaderboard | Mid-table |
| Cost per 1M tokens | ~$15 | ~$0.50 |
| Classification Accuracy (custom test) | 94% | 91% |
| Urgency Accuracy (custom test) | 88% | 87% |
| Cost to process 1000 emails | ~$6 | <$0.21 |
| Latency | 4.1 seconds | ~9 seconds* (fast, small model) |

*(Note: the smaller model is much faster/cheaper despite the raw numbers mentioned in the lecture.)*

**Key insight**: If you *only* relied on public benchmarks, Model A would win on every single metric — benchmarks would never reveal that Model B is actually the better choice for this specific task. Only by running a **custom eval on your own data** (a "golden dataset" of ~200–500 labeled past emails) do you discover that Model B gives nearly the same accuracy at a fraction of the cost and better latency — making it the smarter business decision.

**Conclusion**: Model evals = testing model capability, but you can test via:
- Standardized benchmarks (generic capability signal), OR
- Custom evals on your own data (application-specific signal)

Both are needed for a complete picture.

---

## The 8 Core Capabilities of LLMs

Before diving into specific benchmarks (next topics), you need to know the **8 broad capability categories** that almost all benchmarks are built around.

### 1. Knowledge & Reasoning
Combines two things:
- **Factual knowledge**: how much factual information the model learned during training.
- **Reasoning**: whether it can *connect* those facts logically (multi-step logical reasoning).

- Tested via subject-specific factual recall (biology, physics, history, etc.) — e.g., **MMLU** benchmark tests 57 subjects.
- Also tested via multi-step reasoning: e.g., "summarize the entire span of human evolution and explain why society is the way it is today" — requires both facts AND connecting them logically.
- **Why frontier labs care**: This is essentially the core signal of how "intelligent" a model is.
- **Real-world use**: research assistants, analyzing technical documents, professional assistants (legal, teaching, etc.)

### 2. Coding & Software Engineering
Arguably the most economically important capability (e.g., companies like Cursor reaching huge valuations because of this).

Tested aspects:
- Can it generate working functional-level code from a natural language description?
- Can it generate test cases?
- Can it improve code based on test failures?
- Can it fix bugs in an existing codebase?
- Can it handle multi-file, long-horizon engineering tasks (e.g., refactor an entire codebase)?
- Can it run multiple commands in a terminal (install packages, configure servers, set up environments)?
- Can it do API and function calling?

**Real-world use**: any AI coding agent.

### 3. Mathematics
A form of reasoning, tested at increasing difficulty levels:
- Grade-school level math
- Competition-level problems (e.g., Olympiad-style, needs creative thinking)
- Undergraduate-level problems
- Research-level mathematical reasoning (open-ended problems without known solutions)

**Real-world use**: scientific computing, financial modeling, engineering simulations, data analysis.

### 4. Long Context
Measures whether a model can **effectively use information from very long inputs** (sometimes hundreds of thousands of tokens) — not just whether it technically "fits" in the context window.

Tested aspects:
- Extracting a small fact from a very long document
- Finding details about a specific person/entity buried in a large document
- Summarizing very long context
- Maintaining context across a large codebase (for coding agents)

**Why it matters**: Models often *claim* large context windows (128K, 200K, 1M tokens), but in practice, retention quality degrades as conversations/context grow longer. This eval reveals which models actually hold up.

### 5. Vision & Multimodal
Tests whether the model can understand images, video, and other non-text inputs — not just text.

**Why it matters**: We live in a multimodal world (e.g., pointing a camera at your fridge and asking what you can cook, or asking about a book in a library using video).

### 6. Agentic & Tool Use
Tests whether a model can go beyond just generating text and actually **do things** using tools.

Tested aspects:
- Can it browse the web on its own?
- Can it do structured tool/function calling?
- Can it interact with APIs?
- Can it use a desktop/computer environment?

**Why it matters**: This is the foundation of the entire "agentic AI" field — increasingly important as more agentic applications are built.

### 7. Safety & Alignment
Tests whether the model can be trusted to behave responsibly.

Tested aspects:
- Does it avoid generating harmful content?
- Is it resistant to adversarial attacks (jailbreaks)?
- Is it truthful vs. sycophantic (does it flatter you instead of giving honest feedback)?
- Does it have cybersecurity-related skills (cryptography, reverse engineering, digital forensics) — increasingly tested since powerful models can also find real vulnerabilities in existing software.

**Why frontier labs care a lot**: Governments pressure labs to keep models safe, and safety incidents are a major reputational risk for the company.

### 8. Instruction Following
Somewhat underrated but very important — tests whether the model does **exactly** what the user asked, in the way they asked it.

Examples:
- If asked for a bullet-point answer, does it give one?
- If asked to stay under 200 words, does it comply?
- If asked for a "friendly" tone, does it deliver that?
- If instructions are ambiguous, does the model ask clarifying questions instead of guessing?

**Why it matters**: Directly affects user satisfaction — if a model doesn't follow instructions, users get frustrated and may switch products/companies.

---

## Summary Table of 8 Core Capabilities

| # | Capability | What It Tests |
|---|---|---|
| 1 | Knowledge & Reasoning | Factual recall + multi-step logical reasoning |
| 2 | Coding & Software Engineering | Code generation, debugging, multi-file tasks, tool/API use |
| 3 | Mathematics | Symbolic/numerical reasoning at increasing difficulty |
| 4 | Long Context | Effective use of information across very long inputs |
| 5 | Vision & Multimodal | Understanding images/video, not just text |
| 6 | Agentic & Tool Use | Using tools, browsing, APIs, computer control |
| 7 | Safety & Alignment | Responsible behavior, truthfulness, resistance to attacks, cybersecurity skill |
| 8 | Instruction Following | Precisely following user instructions and formats |

---

## What's Next

- **Today's session** ("LLM Benchmarking") will go deep into: what benchmarks are, how the evaluation process works, famous benchmarks, and how to interpret/read benchmark results.
- **Next session** will cover: how to design and run your own **custom model evals** on a given LLM.

The instructor deliberately front-loads theory before practicals, based on past teaching experience — a strong theoretical foundation leads to much better engagement and deeper questions once practical work begins.

# Whats is LLM Benchmarking | Benchmark Saturation vs. Contamination

## Simple Definition
> A benchmark is a **standardized test** used to measure a particular model capability.

---

## The 4 Components of Every Benchmark

Every benchmark (no matter which one) has these 4 parts. We'll use **GSM8K** (Grade School Math, 8K questions) as the example.

### 1. Dataset / Task
- Contains **questions + answers** (a "golden dataset")
- GSM8K: ~8,000 simple grade-school math word problems with correct answers
- **Task** = what the model needs to do (e.g., "solve this math problem and generate the answer")

### 2. Run Configuration
The exact settings used so that **all models are tested fairly under identical conditions**. Has 3 parts:

**a) Prompt Construction**
- **Zero-shot** vs **Few-shot**: Do you show the model solved examples first, or just give the question directly?
  - GSM8K uses **8-shot** (8 solved examples shown before the actual question)
- **Chain-of-Thought (CoT)** allowed or not: Should the model show step-by-step reasoning, or answer directly?
  - GSM8K allows CoT (improves accuracy)

**b) Decoding & Sampling Configuration**
- **Temperature** — usually set to 0 (for consistent, non-creative answers)
- **Max tokens** — limits how much the model can "think"/write
- **Scoring strategy**:
  - **Pass@1** – Ask once, check if correct (strict)
  - **Pass@k** – Ask k times, count as correct if at least ONE attempt is right (lenient)
  - **Majority@k** – Ask k times, take the most common (mode) answer
- **Tool use** — allowed or not?
  - GSM8K: tools NOT allowed
  - SWE-bench (coding/GitHub issues): tools ARE allowed (needed to fetch GitHub data)

**c) Environment** — the overall setup/conditions kept consistent across models being compared

### 3. Scoring Method
Two steps:
1. **Extraction** – Pull out the actual answer from the model's raw output (model might say "The answer is 72" or just "72" — you need to extract just "72")
2. **Comparison**:
   - **Closed-ended** (like math, MCQ) → straightforward exact match (72 == 72 → correct/incorrect)
   - **Open-ended** (paragraph-style answers) → need an **LLM-as-a-judge** or human evaluator

### 4. Aggregation
- Combine all individual question scores (1s and 0s) into one final score
- Simple case: 920 correct out of 1000 → 92% score
- Complex case (e.g., MMLU with 57 subjects): may need **weighted averaging** per subject rather than a simple average, since subjects aren't equally represented

---

## Where Is All This Defined?
- Almost every benchmark started as a **research paper**
- The paper describes the dataset, run configuration, scoring method, and aggregation method — all in one place
- Example: search "GSM8K paper" or "MMLU paper" to see the original methodology

---

## Step-by-Step: How Model Evaluation Actually Works

Think of it as a **loop** running once per question in the dataset:

1. **Load the question** (item) from the dataset
2. **Build the prompt** — inject few-shot examples if needed, apply chat template, add instructions
3. **Call the model** with the defined decoding config (temperature, max tokens, etc.)
4. **Capture the raw output** and **extract the answer** (e.g., pull out "72" from the full response)
5. **Score** — compare extracted answer to the golden answer → mark as correct (1) or incorrect (0)
6. **Store** the result
7. Repeat for all questions (e.g., 8,000 times for GSM8K)
8. **Aggregate** all scores → final benchmark score (e.g., mean accuracy)

### Why This Is Harder Than It Looks
Running this loop sounds simple, but real implementation needs extra engineering:
- Robust answer extraction (regex, structured outputs)
- Exact scoring logic matching the paper's methodology
- **Batching** strategy for thousands of API calls
- **Retry logic** for failed API calls
- **Rate limit** handling

---

## Eval Harness (Important Term!)

> **Eval Harness** = the piece of code/infrastructure you use to actually run model evaluations, handling all the "plumbing" (batching, retries, rate limits, scoring, aggregation) so you don't have to write it yourself.

**Analogy:** Benchmark = the exam paper. Eval Harness = the exam administration/invigilation system that handles logistics for you.

### Popular Eval Harness Libraries
| Library | Best For |
|---|---|
| **lm-evaluation-harness** (by EleutherAI) | Industry standard for running benchmarks — supports many pre-built benchmarks, minimal code needed (often just one command) |
| **Inspect** | Also popular |
| **DeepEval** | More geared toward **application evals** (not just model benchmarks); requires more code for basic model benchmarking |

### Quick Demo Example (using lm-evaluation-harness)
```
Install the library → provide API key (e.g., OpenAI)
→ Run one command specifying:
   - model (e.g., gpt-5.6)
   - concurrency (parallel requests)
   - task (e.g., gsm8k)
   - few-shot count (e.g., 8)
   - chain-of-thought: yes/no
   - limit (e.g., only 20 questions, for a quick/cheap test run)
   - output path
→ Get results automatically — no manual loop-writing needed
```
- Testing all 8,000 GSM8K questions can cost significant money (~₹2,300 in the example); testing just 20 costs a few rupees — useful for quick sanity checks.

---

## Who Actually Runs These Evaluations? (3 Stakeholders)

### 1. Frontier Labs (OpenAI, Anthropic, Google DeepMind, etc.)
- Run benchmarks **during training** at different checkpoints to track if the model is improving in the right direction
- Used for:
  - **Development guidance** — course-correct training if needed
  - **Release gating** — decide if a new model version is actually better than the previous one before releasing
  - **Marketing** — publicize strong benchmark scores

⚠️ **Caution:** Don't fully trust a frontier lab's self-reported numbers!
- They test under their own favorable/controlled conditions (like a car's advertised mileage vs. real-world mileage)
- They can **cherry-pick** — showcase benchmarks where they score well, hide ones where they don't

### 2. Third-Party Evaluators
- Independent organizations whose whole business is evaluating and ranking models (e.g., LM Arena)
- **More reliable** because they test all models under the *same* conditions
- Often provide extra useful info that labs don't share, like **cost and latency**

### 3. AI Engineers / Companies (like us!)
- Don't just rely on labs or third parties — run **your own evaluations** using public benchmarks + eval harness libraries, under your own specific conditions (to also check your actual cost/latency)

---

## ⚠️ Why You Can't Fully Trust Benchmark Numbers (4 Major Problems)

### 1. Benchmark Contamination
- Most benchmarks are **public** (data + questions available online)
- Newer models are trained on massive, recent internet scrapes — which likely **includes the benchmark's questions and answers**
- Result: the model may have simply **memorized** answers rather than actually "knowing" or reasoning
- **Solutions:** Use private benchmarks, or dynamic benchmarks (datasets that update regularly, unlike static ones)

### 2. Benchmark Saturation
- A new benchmark starts hard → models score low (e.g., 25-36%)
- Over time, models improve → scores rise → eventually all top models cluster near the same high score (90-95%+)
- Once this happens, the benchmark **can no longer differentiate** which model is better → it gets retired and replaced
- Examples of saturated benchmarks: **GSM8K, MMLU, SWE-bench** (in earlier form)

### 3. Configuration Gaming
- Labs can tweak run configuration settings to favor their own model
- Example: giving your model a **Python interpreter tool** during a math benchmark (not something a rival gets) — inflates the score unfairly
- This alone can cause a 5-10% swing in reported scores
- **Rule of thumb:** Don't trust a lab's self-reported "we crushed this benchmark" claim without knowing their exact settings (temperature, max tokens, reasoning budget, tools allowed, etc.)

### 4. Aggregation Manipulation
- When many sub-scores get averaged into one number, poor performance in specific areas can get hidden
- Example: MMLU has 57 subjects — a model might be great at Physics but terrible at Economics. The lab may report only the **average**, hiding the weak subject
- If you need a model specifically for an Economics chatbot, the average score won't warn you about the hidden weakness

---

## Key Takeaway
> Take every benchmark number **with a pinch of salt**. Don't blindly trust the number thrown at you — especially from the model provider itself. As an AI engineer, implement your own evaluation methodology (using public benchmarks + eval harness tools) under conditions relevant to YOUR use case, and use that to make model selection decisions.

# What are LLM Benchmarks | The Evolution of AI Knowledge Benchmarks

## What is "Knowledge Capability"?
- Tests how much **world knowledge** an LLM absorbed during training (its parametric/internal knowledge).
- Considered the **most fundamental capability** of an LLM — the first thing people expected when models were trained on massive internet data.
- Other capabilities (reasoning, coding) came later as **emergent behaviors** as models scaled up.

## Today's Plan
Instead of randomly covering "top 10 famous benchmarks," this class covers **7 key Knowledge benchmarks** in the order they evolved — like a story — so you understand *why* each new benchmark was created.

---

## The Evolution Story (Roadmap)

```
MMLU (2020) — The "mother of all benchmarks" — tests BREADTH of knowledge
   │
   ├──► TruthfulQA (2021) — tests RELIABILITY (is the model spreading myths?)
   │         │
   │         └──► (saturated) → SimpleQA (2024) — replaces it
   │
   ├──► AGIEval (2023) — tests using REAL HUMAN EXAMS (SAT, Gaokao, etc.)
   │
   └──► MMLU saturated in 2024 → two new directions:
              │
              ├──► GPQA (2023) — tests DEPTH of knowledge (PhD-level, 3 subjects only)
              │
              └──► MMLU-Pro (2024) — repairs MMLU's flaws (harder version)

Finally: HLE – Humanity's Last Exam (2025) — combines BREADTH × DEPTH into one mega-benchmark
```

---

## 1. MMLU (Massive Multitask Language Understanding)
**Released:** September 2020 | **Status:** Saturated (retired)

- **Tests:** Breadth of knowledge
- **Dataset:** 57 subjects, 14,000 multiple-choice questions (4 options each), sourced from real exams (GRE, USMLE, AP) and textbooks
- **Metric:** Accuracy (overall + per-subject)
- **How answers are extracted:** Either the model generates a letter (A/B/C/D), or you compare log-probabilities assigned to each option

### History
| Year | Score |
|---|---|
| 2020 | GPT-3 scored 43.9% (human experts: ~90%) |
| 2021-22 | "Scaling law era" — bigger models, better scores |
| 2023 | GPT-4 hit 86% |
| 2024 | Frontier models clustered at 86–92% → saturated |

### What it doesn't measure
- Reasoning depth
- Calibration (does the model know what it doesn't know?)
- Open-ended answering (it's all MCQ)
- Non-English/non-Western knowledge

### Known Issues
- **~6.5% of questions have wrong/missing answers** — so no model can ever hit 100%
- High contamination (public dataset since 2020)
- Very sensitive to prompt format — small wording changes shift scores

---

## 2. TruthfulQA
**Released:** September 2021 | **Status:** Saturated (replaced by SimpleQA & MASK)

- **Tests:** Reliability/Truthfulness — does the model repeat common human misconceptions?
- **Famous finding:** Bigger models were *often less truthful* (they absorbed more internet misconceptions) → showed that **capability ≠ alignment**
- **Dataset:** 817 adversarial questions across 38 categories, each with correct + incorrect (myth-based) answers

### 3 Scoring Methods
1. **Generation** – model picks/generates an answer
2. **MC1** – compares log-probability of each option, picks highest
3. **MC2** (most common) – sums log-probabilities of *all* correct answers (some questions have multiple correct answers)

### History
- 2021: GPT-3 scored 58% vs human baseline of 94%
- 2022-24: New alignment techniques (RLHF, instruction tuning) improved model truthfulness
- Saturated by 2024 as frontier models improved

### What it doesn't measure
- Factual recall (it's a select-the-answer task, not knowledge generation)
- Whether the model would lie *under pressure* (that's a separate benchmark called **MASK**)
- Only English, mostly Western misconceptions

### Known Issue
- Contamination happens at the **alignment/fine-tuning stage**, not pretraining — this dataset often gets used to *train* better alignment

---

## 3. AGIEval
**Released:** April 2023 | **Status:** Saturated

- **Core idea:** Instead of inventing new benchmarks, test LLMs on **real human exams** (SAT, LSAT, Gaokao, civil service exams) — bilingual (English + Chinese)
- **Advantage:** Gives a real (not estimated) human baseline, since actual humans took these exams too

### History
- April 2023: GPT-4 scored 58%, ChatGPT scored 43%, Text-Davinci scored 37% — vs. average human score of 67% and top human scorers at 91%
- 2024: frontier models approached the 91% human ceiling → saturated by 2025

### Dataset
- 20 exam sections, 8,000+ questions (18 MCQ-based, 2 short-answer)

### Key Lesson (Important!)
> A model beating humans on ONE exam does NOT mean it has surpassed human intelligence. It only proves knowledge of that specific exam — not multi-step reasoning, tool use, or long-horizon tasks. Media headlines like "AI beats humans in JEE" were often misleading in this sense.

---

## 4. GPQA (Google-Proof Question Answering)
**Released:** November 2023 | **Status:** Near saturation

- **Core idea:** Instead of breadth (57 subjects), go for **depth** — extremely hard PhD-level questions in only 3 subjects: **Physics, Chemistry, Biology**
- **"Google-proof"** = even a non-expert with 30 minutes and Google access can't solve it
- Every question validated by **2 domain experts**

### 3 Dataset Sizes
| Subset | # Questions |
|---|---|
| Main | 443 |
| Extended | 546 |
| **Diamond** (hardest, most commonly reported) | 198 |

### History
| Year | Model | Score (Diamond) |
|---|---|---|
| 2023 | GPT-4 | 39% |
| 2024 | GPT-4o | 56% |
| 2024 | OpenAI o1 (reasoning model) | 78% |
| 2025 | Grok 4 | ~87% |

- OpenAI hired PhD experts to test the dataset — they scored ~69.7% (though the original paper claimed 81.3% for PhDs — a disputed number)

### What it doesn't measure
- General graduate-level knowledge (science-only)
- Open-ended problem solving (still MCQ)
- Correctness of the reasoning trace (only checks final answer — a lucky guess counts as correct)

### Known Issues
- Very small dataset (only 198 questions) → low statistical confidence
- Marketing claims like "beat PhDs" are disputed
- Contamination risk after 2+ years public

---

## 5. MMLU-Pro
**Released:** 2024 | **Status:** Nearing saturation

- **Core idea:** "MMLU rebuilt to fix its flaws" — same concept as MMLU but harder

### 3 Key Changes from MMLU
1. **4 options → 10 options** per question (much harder to eliminate wrong answers)
2. Removed trivia/noisy questions → added **reasoning-based** questions
3. **57 subjects → 14 broad categories** (better balanced representation, ~12,000 questions total)

### Result
- Reasoning models scored **~20 points higher** than non-reasoning models — proof that this benchmark actually requires thinking, not just fact recall

### Related Paper: "MMLU-Redux"
- Not a benchmark itself — a research paper showing **6–8% of MMLU questions were incorrect**, explaining why no model could ever reach 100%

### What it doesn't measure
- Open-ended generation (still MCQ, just more options)
- Reasoning trace correctness
- Calibration (does model know what it doesn't know?)

### Known Issues
- **No human baseline reported** (unlike earlier benchmarks)
- Favors reasoning models (unfair advantage by design)
- Source contamination (many physics/science questions look textbook-sourced, e.g., from H.C. Verma)

---

## 6. SimpleQA
**Released:** 2024 (by OpenAI) | **Status:** ✅ Still ACTIVE (not saturated!)

- **Core idea:** Replace TruthfulQA — but focus on **short, fact-seeking questions** with **NO multiple-choice options** — the model must generate the answer itself (harder, like a subjective exam vs MCQ)
- **Dataset:** 4,326+ questions, built specifically from questions **GPT-4 failed to answer correctly**

### Key Innovation: Measures Calibration Too
Every answer is graded into 3 categories:
1. **Correct**
2. **Incorrect** (hallucinated/wrong)
3. **Not attempted** (model says "I don't know")

### 3 Metrics
- **Correct** – overall accuracy
- **Correct given attempted** – accuracy only among questions the model actually attempted
- **F-score** – harmonic mean of the two (balances factuality + honesty)

### Why It's Special
- Philosophy: *"Get as many correct as possible, while not attempting ones you're unsure about."*
- A model that says "I don't know" instead of guessing is rewarded for honesty (good calibration), not punished
- Same model that scored 88% on MMLU scored only ~40% on SimpleQA — shows this is a genuinely hard, different test

### History
| Year | Model | Score |
|---|---|---|
| 2024 | GPT-4o | 38% |
| 2024 | o1-preview | 42% |
| Feb 2025 | GPT-4.5 | 62.5% |

### What it doesn't measure
- Long-form factuality (only short 1-2 word answers)
- Everyday factual reliability (questions are rare/unusual, deliberately picked to be hard)

### Known Issues
- Uses an LLM-as-judge to grade answers → judge quality changes over time, making old vs. new scores hard to compare
- **Answer staleness** — facts can change over time (e.g., "current world record holder")
- Built adversarially against GPT-4 specifically → possible unfair bias toward/against certain models

---

## 7. HLE (Humanity's Last Exam)
**Released:** January 2025 | **Status:** ✅ Still ACTIVE — current top benchmark

- **Core idea:** Combine **breadth (like MMLU) × depth (like GPQA)** into one massive benchmark
- **Dataset:** 2,500 expert-written questions across **100+ subjects** (from Classics to Rocket Engineering)
- Built by **1,000+ experts from 500+ institutions across 50 countries** — a massive global collaborative effort (unlike most benchmarks made by one small research team)
- Each question specifically chosen because it **stumped frontier models**

### Why This Dramatic Name?
- Idea: If models eventually saturate (crack) this hardest-possible closed-ended exam, there's nothing left to test this way — evaluation must then shift to **open-ended, agentic tasks**

### Special Features
1. **Private test set** kept hidden by the creators (separate from the 2,500 public questions) to fight contamination
2. Also measures **calibration** — models must state their confidence % along with each answer
3. **80% short-answer, 20% MCQ** — mostly requires generating answers, not selecting
4. **10% of questions are multimodal** (include images) — models without vision capability are naturally limited here

### History
| Year | Model | Score |
|---|---|---|
| Early | Most models | Single digits! |
| 2025 | Grok 4 | 24% |
| 2025 | GPT-5 | 25% |
| 2025 | Gemini 3 Pro | 38% |

### What it doesn't measure
- Open-ended/agentic problem solving (still closed-ended)
- Everyday usefulness (extremely expert-level questions, not everyday queries)
- Multilingual capability (English-only)

### Known Issues
- Started with 3,000 questions; ~500 removed due to disputed answers (now 2,500)
- Uses LLM-as-judge for short-answer grading → same reliability concerns as before
- Selection bias: built from questions that stumped 2024 frontier models — doesn't represent general/day-to-day knowledge

---

## Summary Table

| Benchmark | Year | Tests | Status |
|---|---|---|---|
| MMLU | 2020 | Breadth of knowledge | Saturated |
| TruthfulQA | 2021 | Reliability/truthfulness | Saturated |
| AGIEval | 2023 | Human-exam-based comparison | Saturated |
| GPQA | 2023 | Depth (Physics/Chem/Bio) | Near saturation |
| MMLU-Pro | 2024 | Improved breadth + reasoning | Near saturation |
| SimpleQA | 2024 | Short factual Q&A + calibration | **Active** |
| HLE | 2025 | Breadth × Depth + calibration | **Active** (current top benchmark) |

---

## Key Takeaways
1. Benchmarks follow a **life cycle**: created → popular → models improve → saturates → gets replaced
2. **Contamination** (public questions leaking into training data) and **improving model capability** both cause saturation over time
3. Newer benchmarks increasingly test **calibration** (does the model know what it doesn't know?) — not just raw accuracy
4. A model "beating humans" on one narrow benchmark does **not** mean it has surpassed general human intelligence
5. Always check what a benchmark **does NOT measure** before trusting a score at face value

# How to Use LLM Leaderboards

## What is a Leaderboard?
- **Benchmark** = an exam that tests LLMs on a specific skill (math, coding, knowledge, etc.)
- **Leaderboard** = a public ranking table that shows the exam results — so you can compare many models in one place on a common test.

> Simple definition: An LLM leaderboard is a public ranking/comparison table showing how different LLMs perform on a common set of evaluations.

---

## Why Do Leaderboards Exist? (4 Reasons)

1. **Compare models fairly** – All models take the "same exam," so you can see who's on top.
2. **Provide trust** – Leaderboards are usually run by **third parties** (not the AI company itself), so results feel more trustworthy than a company claiming "our model is the best."
3. **Guide model selection when you can't test everything yourself** – There are hundreds of models; testing all of them yourself would cost too much time and money. Leaderboards do the heavy lifting for you.
4. **Show benchmark saturation** – If top models are all clustering at very similar scores (e.g., 92–94%), it tells you that benchmark is "saturated" (too easy now, not very useful anymore).
5. **Help discover new models** – Top 3–4 spots are usually the same big labs (Google, OpenAI, Anthropic), but scrolling further down often reveals newer, cheaper models worth trying.

---

## Who Uses Leaderboards?

| User | Why They Use It |
|---|---|
| **AI Engineers** (like us) | To shortlist candidate models for a specific application/domain |
| **Frontier AI Labs** (OpenAI, Google, etc.) | To decide *when* to release a new model — only release if it beats competitors significantly (releasing a weaker model looks bad) |
| **Researchers** | To find out which benchmarks are saturated and where new research is needed |
| **Policy Makers / Safety Institutes** | To monitor if any new model is dangerously ahead of others and needs regulation |
| **Open Source Community** | For discovery/publicity — a small lab's model can go viral if it tops even one benchmark |

**Fun fact:** Google's "Nano Banana" model was initially released anonymously ("stealth mode") on an image leaderboard. When it topped the charts, Google revealed it was theirs and kept the popular nickname.

---

## 4 Types of Leaderboards

### 1. Benchmark-Specific Leaderboards
- Ranks models using results of **just one benchmark** (e.g., MMLU, HumanEval, GSM8K, GPQA)
- **Limitation:** Gives a very narrow view — only tells you about one skill, not overall quality
- Example: Humanity's Last Exam (HLE) leaderboard

### 2. Multi-Benchmark (General Capability) Leaderboards ⭐ Most Useful
- Combines results from **many benchmarks** (reasoning, coding, math, instruction-following, etc.) into one overall score
- Also often shows **cost, latency, speed, context window** — very practical
- Examples: LiveBench, Artificial Analysis
- Answers: *"Which model has the strongest overall mix of capability, cost, and performance?"*

### 3. Human Preference-Based Leaderboards
- Users are shown answers from **two anonymous models (A vs B)** and vote on which is better
- Ranking is built from **thousands of human votes**
- Example: LM Arena (Chatbot Arena)
- **Limitation:** Human bias — people often prefer longer, more confident, nicely formatted, or "entertaining" answers, even if not objectively more accurate

### 4. Application/Domain-Specific Leaderboards
- Built around one specific use case or domain (e.g., coding, SQL generation, medical Q&A, tool-calling)
- Example: Berkeley Function-Calling Leaderboard (tests how well a model can call tools/functions)

**Usefulness ranking:** Single-benchmark leaderboards are least useful → Multi-benchmark general leaderboards are most useful.

---

## ⚠️ Why You Can't Blindly Trust Leaderboards (7 Reasons)

1. **Benchmark performance ≠ real-world performance**
   Benchmark data is clean and well-defined (like Kaggle competitions). Real-world use has messy data, ambiguous requests, missing info, tool failures, and edge cases.

2. **Benchmark contamination**
   If a model has "seen" the benchmark questions during training, its score gets inflated and isn't genuine.

3. **Models can be over-optimized for the leaderboard (Goodhart's Law)**
   *"When a measure becomes a target, it stops being a good measure."*
   Example: If a company trains its model just to win human-preference votes (with flattering, polished-looking answers), it may top leaderboards without actually improving real capability.

4. **Lack of transparency in composite leaderboards**
   Which benchmarks are included/excluded? How are different capabilities weighted? This is often unclear.

5. **Small score differences don't matter much**
   A model scoring 84.3 vs another at 84.1 might rank #3 vs #5 — but they're practically the same. Don't fixate on exact rank.

6. **Human preference leaderboards have human bias**
   Top-voted models aren't always objectively the best — people can be swayed by style over substance.

7. **Leaderboards can be stale, incomplete, or self-reported**
   Some leaderboards don't get updated with newest models, and some models' scores are self-reported by the company itself.

---

## How to Read a Leaderboard Correctly (Step-by-Step Guide)

**Step 1: Know your requirements first**
Before opening any leaderboard, be clear about:
- What type of application are you building?
- What latency do you need?
- What's your cost budget?
- What are your context window needs?
- Any deployment constraints (public API vs on-premise)?

**Step 2: Go to the *right* leaderboard for your task**
- Building an agent? → Agent-specific leaderboard
- Building a chatbot? → LM Arena-type leaderboard
- Building RAG? → MTEB (embedding model leaderboard)
- Budget-constrained? → Artificial Analysis (shows cost + speed clearly)

**Step 3: Read the leaderboard carefully**
- What exactly is being scored, and how?
- Who evaluated it, and with what inference budget?
- How old is the evaluation dataset? Is it updated regularly?
- Is there a private test set (to avoid contamination)?
- Is the benchmark saturated?
- Are confidence intervals shown? (If not, assume close scores = same performance)
- If it's a composite score, how are different capabilities weighted?

**Step 4: Shortlist top 3–5 models** based on your specific criteria (not just the #1 rank).

**Step 5: Run your own custom evaluation** on those shortlisted models using your own data/task — this is what actually tells you the best model for YOUR use case.

---

## 🔑 Key Takeaway (Most Important Line)

> **Leaderboards are a filtering tool, NOT a selection/decision tool.**

- Use leaderboards to narrow down from 100+ models to a shortlist of ~5.
- Use your **own custom evals** to make the final decision.

---

## What's Next
- Benchmarks ✅ (concept covered)
- Leaderboards ✅ (this class)
- **Next class:** How to run your own custom evaluation on a given LLM (practical, hands-on)
- **After that:** Application Evals — RAG evals and Agent evals

# Selecting the Right LLM for Your AI App: Running Custom Model Evals

## Recap: Two Types of LLM Evals
1. **Model Evals** – Test the LLM itself
   - **Benchmarks**: Generic tests for knowledge, reasoning, math (good for *filtering*, not final selection)
   - **Custom Model Evals**: Test LLMs on YOUR specific data/application (good for *final selection*)
2. **Application Evals** – Test the full application (covered in future classes)

## Today's Goal
Learn **how to run custom model evals** using a real case study.

---

## Case Study: ESPN Cricinfo "Ask Cricinfo" Feature

**Problem:** During live matches, thousands of fan questions come in (e.g., "What is Bumrah's economy rate?"). Human analysts writing SQL queries manually doesn't scale.

**Solution:** Build a **Text-to-SQL system**:
- User asks a question in plain English
- LLM converts it into a SQL query (using the database schema)
- System runs the SQL on the database
- Result is shown to the user

**Our Task (as AI Engineers):** Pick the **best LLM** to power this system.

---

## The 3-Step Process to Select a Model

1. **Gather Requirements** – Understand the task and constraints
2. **Shortlist Candidates** – Use leaderboards to find 5–10 good models
3. **Run Custom Eval** – Test those models on your own data and pick the winner

---

## Step 1: Gather Requirements

| Requirement | Decision & Reason |
|---|---|
| **Task** | Text-to-SQL generation |
| **Cost ceiling** | ₹3 lakh/month (business decided this) |
| **Latency** | 2–3 seconds max (users are impatient during live matches) |
| **Context window** | Not important (each question is independent, no multi-turn chat) |
| **Deployment** | Public API is fine (no data privacy issue), prefer reliability over self-hosting |
| **Correctness** | Very important! Wrong cricket stats = public embarrassment (screenshots go viral) |

### How Cost Was Calculated
- Prompt = system instructions + database schema + user question ≈ **400 input tokens**
- SQL output ≈ **100 output tokens**
- Assumed **5,000 questions/day**
- Formula:
  ```
  Cost per query = (input_tokens × input_price + output_tokens × output_price) / 1,000,000
  Monthly cost = cost per query × queries/day × 30 days × USD-to-INR rate (~95)
  ```
- Example: Claude Fable 5 came out to ~₹12.8 lakh/month → **too expensive**, rejected
- A cheaper model (e.g., Claude Sonnet) fit better within ₹3 lakh budget

### Bonus Concept: Prompt Caching
- If a large part of your prompt (like the system prompt + schema) repeats across many queries, you can **cache** it.
- Caching costs slightly more on the *first* call but saves a lot on repeated calls.
- Two cache types: **5-minute cache** and **1-hour cache** (choose based on how frequently queries come in).
- Prompt caching works great for **repetitive prompts** (like this SQL system) but **not for RAG chatbots** (context changes every time).

---

## Step 2: Shortlist Candidate Models from a Leaderboard

- Dedicated Text-to-SQL leaderboards (like BIRD-SQL) were rejected — outdated, used fine-tuned models.
- Instead, used a **coding leaderboard** (llm-stats.com), since SQL generation is like a coding task.

### Selection Method:
1. Removed all models costing **more than the budget** (₹3–5 lakh/month)
2. For remaining models, calculated a **combined score**:
   ```
   Score = 0.9 × normalized(coding rating) + 0.1 × normalized(speed)
   ```
   - Coding ability weighted heavily (90%) because correctness matters most
   - Speed weighted lightly (10%) because output is just a short SQL query (doesn't take long to print even for slower models)
3. Sorted models by this score → got **Top 10 candidates**

### Final 5 Models Chosen to Test:
1. **GPT 5.6 Tera** (top scorer, but expensive)
2. **Kimi K3** (new, hyped Chinese model)
3. **Grok 4.5** (curiosity pick)
4. **Claude Sonnet 5** (only Anthropic model in the list)
5. **MiniMax M3** (cheap, good performance-to-cost ratio)

---

## Step 3: Run the Custom Eval

### Setup Steps:
1. **Get a dataset** – IPL cricket data (2020–2024) from Kaggle, loaded into a SQLite database
2. **Extract schema** – List of tables, columns, and data types (needed for the system prompt)
3. **Build a Golden Dataset** – 20 hard question-and-correct-SQL-query pairs
   - Ideally written by human data analysts
   - Each query is validated by running it on the database
4. **Test the pipeline** – Send one sample question to a model, confirm it returns valid SQL
5. **List candidate models** – Store model names + API identifiers (used OpenRouter to access all models through one platform)
6. **Build an Evaluator** – Logic to compare two SQL results:
   - Run the **golden query** and the **generated query** on the database
   - Compare the row counts first
   - Normalize values (e.g., treat 2.0 and 2 as equal)
   - Sort rows and compare (unless the query requires a specific order, like `ORDER BY`)
   - If both result tables match → generated query is **correct**
7. **Orchestrate everything** – Loop through all 5 models × 20 questions, run evaluation, and calculate accuracy for each model

> ⚠️ Note: You **cannot** just compare SQL query text character-by-character — different queries can produce the same correct result.

---

## Final Results

| Model | Accuracy | Monthly Cost | Speed |
|---|---|---|---|
| GPT 5.6 Tera | 80% | High (~₹12+ lakh) | Slow |
| Kimi K3 | ~50% | High | Very slow (many SQL syntax errors) |
| Grok 4.5 | 90% | ~₹2.5 lakh | Fast |
| Claude Sonnet 5 | 85% | ~₹2.84 lakh | Very fast |
| MiniMax M3 | 65% | Low | Medium (some SQL errors) |

### Key Takeaways from Results:
- A model being hyped/famous (like Kimi K3) **does not guarantee** good performance on your specific task
- Chinese models (Kimi, MiniMax) had more **SQL syntax errors** than US models in this test
- **Grok 4.5** and **Claude Sonnet 5** emerged as the top 2 finalists (best balance of accuracy, cost, and speed)
- Final decision came down to a judgment call: Sonnet was chosen for perceived **API reliability**, though Grok was cheaper and technically scored slightly higher
- With a small dataset (20 questions), each question = 5% of the score — a **larger golden dataset** would give more reliable results
- Running the eval **multiple times** (5 runs) gives more statistical confidence, at extra cost

---

## Summary: How to Run a Custom Model Eval
1. Understand your task and write down clear requirements (cost, latency, context, correctness needs)
2. Use a relevant leaderboard to shortlist 5–10 candidate models based on your requirements
3. Build a golden dataset (questions + correct answers/queries) for your specific use case
4. Run each candidate model against the golden dataset
5. Compare each model's output to the golden answer using a fair evaluation method (not exact text matching)
6. Calculate accuracy for each model
7. Pick the best model considering accuracy, cost, and speed together — not just the "best" one on paper

# How to Answer "How Do You Evaluate Your RAG App?

## Recap of the Playlist So Far
- **Part 1:** Fundamentals of LLM Evals (why evals are needed, reference-based vs reference-free, online vs offline evals).
- **Part 2:** Model Evals — split into:
  - **Benchmarks** (standardized tests, e.g. knowledge/capability benchmarks)
  - **Custom model evals** (your own dataset to pick the best model for your use case)
- **Part 3 (starts now):** **Application Evals** — the most important part of this playlist.

## Types of LLM Applications
LLM apps can be many types: simple chatbots, RAG chatbots, agents, multimodal apps, fixed-schema output apps (e.g. classifying emails). 
The instructor picked two to teach in depth:
1. **RAG** — because most chatbots you build professionally will have RAG.
2. **Agents** — also very important.
(Other simpler apps become easy once you master these two.)

## The Project: "CampusX Doubt Solver"
- A simple RAG chatbot built using **lecture transcripts** of this very course as documents.
- Students can ask doubts about any lecture, and the bot answers using RAG.
- Purpose: keep the app simple so the **focus stays on evaluation**, not on building something fancy.

## Interview Tip
"How do you evaluate a RAG chatbot?" is asked in ~8/10 GenAI interviews. Most candidates only name 3-4 metrics (recall, precision, answer relevance) — but a **structured framework answer** impresses interviewers much more.

---

## The RAG Evaluation Framework — 3 Levels

### 1. Component-Level Evaluation
Evaluate each RAG component **separately**, right after building it.

**Retriever** (fetches relevant docs from vector DB):
- **Recall** – of all correct/relevant docs, how many did we retrieve?
- **Precision** – of all docs retrieved, how many were actually relevant?

**Generator** (LLM that generates answer from question + context), tested in **isolation** (manually given question + context, not connected to retriever yet):
- **Faithfulness** – Is the answer grounded in the given context, or did the model hallucinate?
- **Answer Relevance** – Is the answer relevant to the question?
- **Citation Accuracy** – Are the sources/citations correct?

### 2. Pipeline-Level Evaluation ("RAG Triad")
Once Retriever + Generator are connected into one pipeline, test these 3 relationships:

| Pair | Metric |
|---|---|
| Question ↔ Context | **Context Relevance** |
| Context ↔ Answer | **Faithfulness** |
| Question ↔ Answer | **Answer Relevance** |

This combination is called the **RAG Triad**.

### 3. Application/System-Level Evaluation
Now test the whole app as a product:

**Quality metrics:**
- **Correctness** – Is the answer factually correct?
- **Completeness** – Does the answer cover all parts of the question?
- **Style** – Does it match the expected tone/style (e.g. teacher's explanation style)?

**Safety metrics:**
- Toxicity check
- PII (personal info) leakage check
- Jailbreak resistance

**Ops metrics:**
- Latency
- Cost per query
- Token usage

All these together = your **Eval Suite**.

---

## Tools
- Library used: **DeepEval** (chosen over Ragas because it's broader — covers RAG, agents, multimodal, non-LLM apps — and is becoming an industry standard).
- Syntax is similar to **PyTest** (Python's testing library), so it feels familiar if you know software testing.

## Project Folder Structure
```
project/
├── src/        → RAG chatbot source code (retriever, generator, pipeline, API/UI)
├── evals/      → eval_retriever.py, eval_generator.py, eval_pipeline.py, eval_app.py, eval_safety.py, eval_ops.py
└── run_evals.py → runs all eval files together, produces a report
```

---

## Regression Testing
**What it is:** Running your full eval suite on a new version of the app to check if it's objectively better (or worse) than the previous version.

### 3 Levels of Regression Testing
1. **Basic** – Run eval suite manually, compare numbers by hand each time.
2. **With Experiment Tracking** – Use a tool like **MLflow** (or Confident AI, Weights & Biases) to log configs + metric values automatically, view trends on a dashboard.
3. **With CI/CD** – Use a CI tool (e.g. GitHub Actions). Every code push automatically triggers the eval suite. If new metrics are worse than baseline → block deployment. If better → deploy and update the baseline.

---

## After Deployment: Online Evaluation
Evaluation doesn't stop after deployment. Once live, track:
1. **Captured signals** – latency, cost, thumbs up/down (using tools like **Langfuse**, **LangSmith**, Confident AI) — this is called **Observability/Tracing**.
2. **Computed metrics** – faithfulness, answer relevance, correctness — measured live on real traffic.
3. **Drift detection** – Is performance degrading over time? (e.g. faithfulness score dropping over last 8 hours → alert).
4. **Self-improving loop** – Bad chat examples found in production get added back to the offline golden dataset, so future versions are tested against richer data.

---

## How to Answer the Interview Question
> "How do you evaluate a RAG chatbot?"

**Sample structured answer:**
1. "I'll build an eval suite tested at 3 levels: component, pipeline, and application."
2. "At component level, I test retriever (recall, precision) and generator (faithfulness, relevance, citation accuracy) separately."
3. "At pipeline level, I check the RAG Triad — context relevance, faithfulness, answer relevance."
4. "At application level, I check correctness, completeness, safety, and ops metrics (latency, cost, tokens)."
5. "Then I use this suite for regression testing — basic, experiment tracking, or CI/CD, depending on the company's maturity."
6. "After deployment, I run online evals — tracking, drift detection, and feeding bad examples back into my offline dataset."

This framework-style answer shows depth, not just a list of metric names.

---

## Roadmap for Next 4 Sessions
1. **Session 1:** Build & evaluate Retriever + Generator (component level) using DeepEval.
2. **Session 2:** Build RAG pipeline, test the RAG Triad.
3. **Session 3:** Application-level evaluation (correctness, completeness, safety, ops).
4. **Session 4:** Regression testing + Online evaluation.

# Building & Evaluating the Retriever — Simple Notes

## Goal of This Session
- Build the **first component** of the RAG eval suite: the **Retriever**.
- Learn how to evaluate it properly (Recall & Precision).
- This is part of **Component-Level Evaluation** (Level 1 of the 3-level framework).

---

## Project Setup
Folder: `rag_eval_project`

```
rag_eval_project/
├── data/     → lecture transcripts (.vtt subtitle-style files, timestamp + text)
├── src/      → retriever.py, generator.py, rag_pipeline.py, app files
├── evals/    → eval_retriever.py, eval_generator.py, etc.
└── golds/    → golden datasets
```

**Setup steps:**
1. Create folder → open in VS Code.
2. Create the 4 subfolders above.
3. Add lecture transcripts into `data/`.
4. Create virtual environment using **UV** (Python 3.11).
5. Install dependencies: `langchain`, `openai`, `deepeval`, `pytest`, `python-dotenv`.
6. Create `.env` file → add OpenAI API key.

---

## Building the Retriever

**What a Retriever does:**
- Takes a query → converts it to a vector (embedding) → searches the vector database → returns the nearest (most relevant) chunks as context.

**Steps in code (`retriever.py`):**
1. **Load transcripts** — read all `.vtt` files, remove timestamp lines (keep only spoken text), and store which session each line came from (for citations later).
2. **Chunk the documents** — split text into chunks. Starting settings: **chunk size = 750, overlap = 100**.
3. **Embed the chunks** — using OpenAI's `text-embedding-3-small` model, store in a **Chroma** vector database.
4. **Build retriever object** — set `k = 5` (fetch top 5 nearest chunks per query).
5. Test it — ask a question like *"What is regression testing?"* → check if relevant chunks come back.

✅ Retriever built and working (not yet evaluated for quality).

**Note:** If new documents are added later (e.g. a new lecture), you must delete the old vector database folder and re-run the retriever script to regenerate embeddings.

---

## How Does a Retriever Fail? (2 Failure Modes)

1. **Missing relevant context** — the retriever doesn't bring back the chunks that actually contain the answer.
2. **Bringing noisy context** — it does bring the right chunks, but also brings extra irrelevant ("noisy") ones along with them.

These two failure modes map to two metrics:

| Failure Mode | Metric | Meaning |
|---|---|---|
| Missed relevant context | **Recall** | Out of all correct chunks that exist, how many did the retriever fetch? |
| Brought noisy context | **Precision** | Out of all chunks fetched, how many were actually useful? |

**Recall vs Precision Trade-off:**
- Increasing `k` (number of chunks fetched) → **increases recall** (more chances to catch the right chunks) but **decreases precision** (more noise gets pulled in too).
- Balancing both is tricky — that's the core challenge of tuning a retriever.

**Important:** Both Recall and Precision are **reference-based evaluations** — they need a "golden" dataset that tells us what the correct answer/context should be.

---

## The WRONG Way to Build a Golden Dataset (and why)

**Naive approach:** Golden dataset = Question + list of correct Chunk IDs (e.g. Q1 → chunks 72, 89, 100).

**Why this fails for our project:**
- Someone would have to manually read **800+ chunks** for **every single question** to find which ones are relevant — extremely tedious and unscalable.
- Bigger problem: if you ever change chunking settings (chunk size/overlap), **all chunk IDs change** → the entire golden dataset becomes invalid → you'd have to redo it every time you tune your retriever. Too much rework.
- This method only works if your documents are cleanly separated (e.g. Doc1 totally unrelated to Doc2) and you never change chunking settings. Not our case — our transcripts have related, overlapping information.

---

## The CORRECT Way: Golden Dataset with Ideal Answers

**New Golden Dataset format:** Question + **Ideal Answer** (not chunk IDs).
- "Ideal answer" = the actual answer as taught in the course transcripts (not from Google).
- This answer stays valid even if chunking changes — because it's about *content*, not chunk IDs.

### How Recall is Calculated (Contextual Recall)
1. Give the retriever a question → it returns top-k chunks.
2. Use an **LLM-as-a-judge**: break the "ideal answer" into individual **claims** (atomic facts).
3. Ask the judge LLM: for each claim, is it found in ANY of the retrieved chunks?
4. Recall = (claims found in retrieved chunks) / (total claims in ideal answer).
5. Average this across all questions → **Contextual Recall** score.

### How Precision is Calculated (Contextual Precision)
1. For each retrieved chunk, ask the judge LLM: *"Does this chunk help produce the ideal answer? Yes/No + reason."*
2. Mark each chunk as relevant or noisy.
3. **Also considers ranking** — chunks ranked higher (more relevant, appearing first) should count more. Two retrievers can have the same basic precision (e.g. 2 out of 5 correct) but the one that ranks the correct chunks **higher** is actually better. DeepEval's Contextual Precision accounts for this by calculating precision-at-each-position and averaging.

**Why this method is better:** Chunking parameters can change freely — the ideal answer never needs to be rewritten.

This whole technique uses an **LLM-as-a-Judge**, not simple programmatic string matching.

---

## Ways to Build a Golden Dataset

| Method | Pros | Cons |
|---|---|---|
| **1. Hand-authored** (fully manual) | Most accurate, low error | Not scalable, time-consuming |
| **2. LLM-assisted drafting** (LLM drafts, human reviews) | Faster, cheaper | Risk of LLM adding incorrect/irrelevant info — needs careful human review |
| **3. DeepEval Synthesizer module** | Automated | In the instructor's experience, output quality was poor — generated irrelevant/off-topic questions |
| **4. From production logs** (after deployment) | Real user questions | Can't be your *first* source — you need some data to start with |

**What was actually used:** Method 2 (LLM-assisted). Transcripts uploaded to Claude → asked to generate ideal Q&A pairs one at a time (15 questions) → manually reviewed each one.

---

## DeepEval Code Structure — 3 Core Concepts

Every DeepEval evaluation has 3 parts:

1. **LLMTestCase** — represents ONE row of your golden dataset. Contains:
   - `input` (the question)
   - `expected_output` (ideal answer)
   - `retrieval_context` (chunks the retriever fetched)
   - `actual_output` (what the generator said — placeholder if generator isn't built yet)

2. **Metric(s)** — e.g. `ContextualRecallMetric`, `ContextualPrecisionMetric`. Each has settings:
   - Which LLM to use as judge
   - A **threshold** (score below this = test case fails)
   - `include_reason=True` (get an explanation for pass/fail)

3. **evaluate() function** — runs the metric(s) against all test cases and returns scores.

```python
test_case = LLMTestCase(
    input=question,
    expected_output=ideal_answer,
    retrieval_context=retrieved_chunks,
    actual_output="Generator not evaluated in this run"
)

evaluate(test_cases=[...], metrics=[ContextualRecallMetric(), ContextualPrecisionMetric()])
```

---

## Running the Eval & Improving the Retriever

**Baseline run** (chunk size 750, overlap 100, k=5):
- Recall: 80%, Precision: 80%
- 10/15 test cases passed, 5 failed

**Improvement attempts & results:**

| Change | Recall | Precision | Result |
|---|---|---|---|
| Increase chunk size to 1000, overlap to 150 | 97% | 83% | Big improvement |
| Add a **Re-ranker** (reorders chunks, pushes relevant ones to top) | ~92% | 85% | Precision improved (fewer failures) |
| Switch to a bigger embedding model (`text-embedding-3-large`) | 99% | 85% | Recall improved further, precision stayed similar |
| Reduce k from 5 to 3 | ~84% | — | No real benefit; some natural variance since dataset is small (only 15 rows) |

**Final result:** ~95%+ recall, ~85% precision — considered a good retriever.

**Key improvement levers to try:**
- Chunk size / overlap
- Re-ranker
- Embedding model quality
- Value of `k`

---

## Key Takeaway
- We built the **Retriever** and learned to evaluate it using **Contextual Recall** and **Contextual Precision** (LLM-as-a-judge based, not simple ID-matching).
- Retriever quality is now known to be good (Recall 95%+, Precision ~85%).
- **Next class:** Build and evaluate the **Generator** (the second component).

# Evaluating RAG: Testing the Generator & Full Pipeline with the RAG Triad

## Recap: The Big Plan
A RAG app is evaluated at **3 levels**:
1. **Component level** – Retriever and Generator tested separately
2. **Pipeline level** – Retriever + Generator tested together
3. **Application level** – Whole app tested (correctness, style, etc.)

Last session: Retriever was evaluated (Recall + Precision).
This session: Generator evaluation + Pipeline evaluation.

---

## 1. What is a Generator?
- A simple component that uses an **LLM**.
- Input: a **question** + **retrieved context** (documents)
- Output: an **answer**

It does NOT search anything — it just answers using the context it's given.

---

## 2. How Can a Generator Fail?
Two main failure modes:

### A) Unfaithful Response (Hallucination)
- The generator adds information that is **not in the context**.
- Example: Context doesn't mention "live classes," but the answer says "Yes, there are 2 live classes/week." → Hallucinated.
- **Dangerous** in real products (e.g., the Air Canada chatbot case — it promised a refund policy that wasn't real).
- **Important:** Faithful ≠ Correct. Faithful only means the answer sticks to the context (even if the context itself is wrong).

### B) Irrelevant Response
- The answer comes from the context but does **not actually answer the question**.
- Example: User asks "Does the program include live classes?" and the answer just lists things from context without addressing the live-class question at all.

These two failure modes give us two metrics.

---

## 3. Metric 1: Faithfulness
**Question it answers:** Is the generated answer fully based on the given context (no made-up info)?

**How it's calculated:**
1. Build a **Golden Dataset**: pairs of (Question, Golden/Ideal Context) — manually curated.
2. Send question + golden context to the Generator → get an answer.
3. Use an **LLM-as-a-Judge** to break the answer into individual **claims**.
4. For each claim, check: does it exist in the golden context? (Yes/No)
5. Score = (claims found in context) / (total claims)
6. Repeat for all questions in dataset → average = final Faithfulness score.

**Note:** This is testing the Generator in **isolation** — the context comes from the golden dataset, NOT from the real Retriever.

---

## 4. Metric 2: Answer Relevancy
**Question it answers:** Does the answer actually address the question asked?

**How it's calculated:**
1. Break the generated answer into claims (same as before).
2. For each claim, ask the LLM judge: "Does this claim help answer the question?" (Yes/No)
3. Score = (relevant claims) / (total claims)
4. Average across all questions.

**Key difference from Faithfulness:** This is **reference-free** — you don't need a golden context to compare against, just the question and the answer.

---

## 5. Faithfulness vs Answer Relevancy vs Recall/Precision
- Recall/Precision (retriever) compares **retrieved context vs golden answer/context**.
- Faithfulness compares **generated answer vs golden context** (opposite direction).
- These are different things — don't confuse them.

---

## 6. Building the Golden Dataset
- Export all chunks from the vector database into a JSON file.
- Feed this JSON to an LLM (e.g. Claude) and ask it to generate **Question + Golden Context pairs**, one at a time.
- Manually review/verify each pair before adding to the dataset.
- Result: a dataset like `faithfulness_dataset.json` with ~15 Q&A pairs.
- (Alternative: DeepEval's built-in synthesizer — not covered in detail yet.)

---

## 7. Running the Evaluation (DeepEval)
Code pattern (same structure used for retriever eval):
1. Load golden dataset.
2. For each row, create an `LLMTestCase`:
   - `input` = question (from dataset)
   - `actual_output` = generator's answer
   - `retrieval_context` = golden context (from dataset)
3. Define metrics: `FaithfulnessMetric`, `AnswerRelevancyMetric` (built-in DeepEval metrics)
4. Call `evaluate()` with test cases + metrics.
5. DeepEval runs test cases **in parallel** (fast).

### First run results:
- Faithfulness: ~91% (already good)
- Answer Relevancy: ~73% (needs improvement)

**Why is Faithfulness naturally high?**
Because the LLM is explicitly instructed "answer only from this context" — modern LLMs are good at instruction-following, so they tend to stick to the context by default.

**Why is Answer Relevancy lower?**
Sticking to context doesn't guarantee the answer actually addresses the question — that's a separate skill.

---

## 8. How to Improve the Generator
Only 2 real levers (fewer than retriever, which had chunk size, embedding model, reranker, etc.):
1. **Switch to a better/more powerful LLM**
2. **Improve the system prompt** (this matters a LOT)

### What was done:
- Ran evaluation multiple times, looked at failing test cases and their reasons.
- Iteratively refined the system prompt (added rules like: don't overstate claims, don't merge two different things into one, rephrase in your own words, don't require exact wording match, etc.)
- After 3–4 iterations of prompt refinement:
  - Faithfulness: **96%**
  - Answer Relevancy: **92%**

⚠️ **Caution — Overfitting risk:** If you tune the prompt too specifically to your test dataset, it might not generalize well to new/real retrieved context. This gets tested later when the pipeline uses the real retriever.

---

## 9. Experiment Tracking (Optional)
- DeepEval has a parent tool called **Confident AI**.
- Command: `deepeval view` — logs your evaluation run (pass/fail per test case, configs used, prompt version, etc.) to a dashboard.
- Useful for tracking multiple prompt versions and their scores over time (similar to MLflow experiment tracking).

---

## 10. Building the Full RAG Pipeline
Now connect Retriever + Generator into one pipeline:

```
Question → Retriever → Context → Generator → Answer
```

- Create a `RAGPipeline` class that:
  1. Calls retriever to fetch context
  2. Converts context to string
  3. Sends question + context to generator
  4. Returns the final answer

This is basically simple "glue code" connecting the two components already built.

---

## 11. Pipeline-Level Evaluation = The "RAG Triad"
Three relationships exist between Question, Context, and Answer:

| Relationship | Metric |
|---|---|
| Answer ↔ Context | **Faithfulness** |
| Answer ↔ Question | **Answer Relevancy** |
| Context ↔ Question | **Contextual Relevancy** (NEW) |

**Key difference from component-level testing:**
At component level, context came from the **golden dataset**.
At pipeline level, context comes from the **real Retriever**.
So even though the metric names are the same, the numbers can be different!

---

## 12. Metric 3: Contextual Relevancy
**Question it answers:** How relevant is the context that the Retriever actually pulled, for answering the question?

**How it's calculated:**
1. Send only the question to the Retriever → get back retrieved context (e.g., 5 chunks).
2. Break each chunk into claims (e.g., 15 claims total across 5 chunks).
3. For each claim, ask LLM judge: "Is this claim relevant to the question?" (Yes/No)
4. Score = (relevant claims) / (total claims)
5. Average across all questions.

Also a **reference-free** evaluation (only needs questions from golden dataset, not golden context).

---

## 13. Running Pipeline-Level Evaluation
Same code pattern, but now:
- `input` = question (from golden dataset)
- `actual_output` = answer from **RAG Pipeline** (not isolated generator)
- `retrieval_context` = context from **RAG Pipeline's real retriever** (not golden dataset)

Define all 3 metrics: Faithfulness, Answer Relevancy, Contextual Relevancy → run `evaluate()`.

### Results:
- Faithfulness: ~92–93% ✅
- Answer Relevancy: ~86% ✅ (proves the earlier prompt tuning generalizes well, since it stayed strong even with real retrieved context)
- **Contextual Relevancy: only ~42%** ⚠️ (problem area)

---

## 14. The Puzzle: Good Recall & Precision, But Low Contextual Relevancy
Retriever's own scores were great: Recall ~99%, Precision ~89%. So why is Contextual Relevancy only 42%?

**Explanation — "Noise per chunk":**
- **Recall** = out of all correct chunks that should be retrieved, how many did we get? (checks across the whole set of chunks)
- **Precision** = out of all chunks retrieved, how many are useful? (checks across the whole set of chunks — a chunk counts as "useful" even if only ONE sentence in it is relevant)
- **Contextual Relevancy** = looks *inside* each chunk, at the **sentence/claim level**. If a chunk has 5 sentences and only 1–2 are actually relevant, the rest count as noise.

So a chunk can be marked "useful" for Precision (because it has at least some relevant info) but still score low on Contextual Relevancy (because most of its content is irrelevant noise).

**Fix:** Try reducing **chunk size** (and maybe overlap) — smaller chunks = less noise per chunk. This may trade off slightly against other metrics, so needs testing.

**Practical takeaway:** If Faithfulness, Answer Relevancy, Recall, and Precision are all good, but Contextual Relevancy is a bit low — it's not a critical problem, since final answers are still good. But it's worth experimenting with chunk size to improve it.

---

## 15. Summary Table So Far

| Level | Metric | Purpose |
|---|---|---|
| Component (Retriever) | Recall | Are we retrieving all the correct chunks? |
| Component (Retriever) | Precision | Are the chunks we retrieved actually useful? |
| Component (Generator) | Faithfulness | Does the answer stick to the given context? |
| Component (Generator) | Answer Relevancy | Does the answer address the question? |
| Pipeline | Faithfulness | Same as above, but using real retrieved context |
| Pipeline | Answer Relevancy | Same as above, but using real retrieved context |
| Pipeline | Contextual Relevancy | Is the real retrieved context (at sentence level) relevant to the question? |

These 5 metrics = the standard **"RAG Triad + Retriever metrics"** used for any RAG application.

---

## 16. What's Left (Next Sessions)
- **Application-level evaluation**: Correctness, Completeness, Style/Tone matching (custom metrics using "G-Eval")
- Safety evaluations
- Ops evaluations
- Regression testing
- Online evaluation (testing on live production traffic)

# Mastering G-Eval: The Deterministic LLM-as-a-Judge Framework Explained

## Where We Are in the Big Picture
RAG evaluation has 3 levels:
1. **Component level** – done
2. **Pipeline level** – done
3. **Application level** – *today's topic*

At the application level, we build 3 types of eval suites:
- **Quality** (today)
- **Safety** (next class)
- **Operations** (next class)

## Today's Focus: Application Quality
We check quality using 3 metrics:
1. **Correctness** – Is the answer factually right?
2. **Completeness** – Does the answer cover all parts of the question?
3. **Style** – Does the answer match the required teaching/brand style?

---

## Old Metrics vs New Metrics

### Old Metrics (Count-Based)
Recall, Precision, Faithfulness, Answer Relevance, Context Relevance.

**How they worked:**
- Break answer into claims
- Check each claim (yes/no) against context
- Count → calculate a ratio (e.g., 3 correct claims out of 4 = 0.75)

### Problem
Some metrics **can't be measured by counting**:
- **Style** – can't check "sentence by sentence" (style exists at whole-answer level)
- **Correctness** – can't check claim by claim (e.g., an analogy alone makes no sense, but is fine inside the full answer)

For these, we need **judgment**, not counting.

---

## LLM-as-a-Judge (Simple Version)
Steps:
1. Create a **golden dataset** (question + correct/ideal answer)
2. Get actual answer from your RAG app
3. Send Question + Expected Answer + Actual Answer to an LLM judge
4. Ask the judge: "Give a score 0–10"
5. Average scores across all questions

### Problem With This Simple Approach
**High variance** — running the same evaluation twice gives different scores (e.g., 6 one time, 8 another time), even though nothing changed.

**Two reasons:**
1. The criteria given to the LLM is too high-level/loose → judge interprets it differently each time
2. Judge just outputs a single token (like "8") based on probability — and probabilities of similar numbers (7 vs 8) can flip between runs

---

## G-Eval (The Fix)
A research technique (2023 paper) that makes LLM-as-judge **more reliable**.

### Two Core Innovations

**1. Convert high-level criteria → detailed evaluation steps (using Chain-of-Thought)**
- Instead of: "Check if answer is correct" (vague)
- G-Eval breaks it into 4–5 exact rules (a "rulebook"), e.g.:
  - Compare only factual claims
  - A claim is wrong only if it contradicts or is factually false
  - Don't penalize for brevity or missing minor points
  - Extra correct info should never lower score
- This makes the judge's behavior **consistent** across runs

**2. Use probability-weighted scoring (not just the output token)**
- Normally: judge just says "8" → you take 8
- G-Eval instead: looks at **top tokens' probabilities** (e.g., 8 → 70%, 7 → 20%, 9 → 5%)
- Normalizes these probabilities and takes a **weighted average**
- Example: (8×0.73) + (7×0.21) + (9×0.05) = **7.84**
- This gives a **stable decimal score** instead of a jumpy integer, so re-running gives nearly the same result each time

**Why it matters:** Weighted average smooths out uncertainty → scores don't jump wildly between runs (unlike simple LLM-as-judge).

---

## Practical Steps to Measure Correctness (Example)

1. **Build a golden dataset** — Questions + ideal/correct answers (written by a subject expert), e.g. 15 Q&A pairs
2. **Run each question through your RAG pipeline** → get actual answer
3. **Create a G-Eval metric**:
   - Name: "Correctness"
   - Criteria or Evaluation Steps (rulebook)
   - Judge model (e.g., GPT-4o-mini)
   - Threshold (e.g., 0.7) → above = Pass, below = Fail
4. Run evaluation → get score + pass/fail per question + reasons for failure

### Correctness vs Faithfulness (Important Difference)
- **Faithfulness** = Is the answer grounded in the given context (course material)?
- **Correctness** = Is the answer factually true in the real world (Google-level truth)?
- An answer can be: correct+faithful / faithful but wrong / correct but not faithful / neither

---

## Criteria vs Custom Evaluation Steps
- **Giving only criteria** → G-Eval generates evaluation steps itself using CoT (steps may vary slightly each run)
- **Giving your own evaluation steps directly** → more consistent, no variation from run to run

**Best practice:**
- Early stage → let G-Eval auto-generate steps (using criteria) to understand your pipeline
- Once you understand common failure patterns → write your own fixed evaluation steps + rubric for more control and stability

---

## Improving Scores (Real Example from the Class)

### Correctness
- Initial score: 66% (8/15 passed)
- Problem found: Golden answers were very detailed; generated answers were shorter but still correct → wrongly penalized
- Fix: Updated evaluation steps to say "don't penalize for brevity or missing minor details, only penalize factually wrong claims"
- New score: 83–84% (14/15 passed)

### Completeness
- Checks: Does generated answer cover **all parts** (A, B, C) of the ideal answer?
- Initial score: 68% (only 5/15 passed)
- Problem: Generator prompt told the model to give short/concise answers → missed some parts of multi-part questions
- Fix: Updated generator prompt to say "identify every part of the question and address all of them"
- New score: 75% (14/15 passed)

### Style
- Checks: Does the answer match "Campus X" teaching style (conversational, explains intuition before formulas, uses simple language)?
- No golden answer needed — just a clear **rubric** describing the style
- Initial score: 54% (generator was never told about the style)
- Fix 1: Updated generator prompt to explain the required style
- Fix 2: Adjusted rubric (it was over-penalizing answers without analogies — fixed by saying analogies are a "bonus," not mandatory)
- New score: ~74% (9/15 passed)

---

## Key Takeaway
> Prompt engineering really matters — both for:
> - The **generator prompt** (how your RAG app writes answers)
> - The **evaluator's rubric/criteria** (how the judge scores answers)
>
> Small, targeted tweaks to either can significantly improve your evaluation scores.

---

## DeepEval Implementation (Code Summary)
```python
correctness_metric = GEval(
    name="Correctness",
    evaluation_steps=[...],   # your custom rulebook
    evaluation_params=[input, actual_output, expected_output],
    model="gpt-4o-mini",
    threshold=0.7,
    strict_mode=False   # False = use weighted probability scoring
)
```
- `strict_mode=False` → uses the probability-weighted scoring (recommended)
- `strict_mode=True` → just takes the direct output token (less reliable)

Same pattern used for **Completeness** and **Style** — just change the metric name, evaluation steps, and rubric.

---

## Other Metrics You Can Build with G-Eval
- Coherence
- Tonality
- Helpfulness
- Safety-related metrics (next class)

**Core idea:** Any metric that needs "judgment" instead of "counting" can be built using G-Eval.

---

## Next Class
- Safety metrics
- Operations metrics
- Regression testing

# Securing Your RAG Application: Testing for Toxicity, Leakage & Scope Drift 

## Where This Fits
We are building a full **eval suite** for our RAG doubt-solver app. Already done:
- Component evals (retriever + generator)
- Pipeline evals (RAG Triad)
- Quality evals (correctness, completeness, style)

Left: **Safety evals** (today) and **Operations evals** (next class).

---

## 1. What is LLM Safety?

LLM safety = making sure your LLM-based app works safely for you and your users — nothing unexpected or harmful happens.

Why it's harder than normal software safety:
- LLMs are **probabilistic** — same input can give different outputs each time.
- This makes it much trickier to control at scale than normal software.

A new field is emerging: **LLM Safety & Security** (like Cybersecurity emerged after software). Expect it to become a full sub-field within ~5 years, with dedicated jobs and courses.

---

## 2. Common Failure Modes (ways an LLM app can go wrong)

1. **Sensitive Information Leakage** — leaking system prompts, private data, credentials, proprietary content.
2. **Scope / Policy Violation** — app gets manipulated to do things outside its intended purpose (e.g., Amazon's chatbot being used to do students' homework instead of sales support).
3. **Harmful/Toxic Output** — abusive, hateful, or inappropriate responses.
4. **Misinformation/Hallucination** — confidently generating false facts.
5. **Bias/Unfairness** — different treatment for different user groups (comes from biased training data).
6. **Unsafe Actions / Excessive Agency** — mainly for agents with tool access (e.g., an agent trading stocks and losing money after breaking its guardrails).

These failures can happen in two ways:
- **Non-adversarial** — system fails naturally (model limitations, bad context, weak prompting, weak safeguards).
- **Adversarial** — an attacker intentionally causes the failure.

You must design for **both** scenarios.

---

## 3. Types of Attacks on LLM Systems

### A. Prompt Manipulation Attacks
- **Direct Prompt Injection** — attacker directly writes malicious instructions ("ignore previous instructions...").
- **Indirect Prompt Injection** — malicious instructions hidden in external content (a webpage, document) that the LLM reads and follows.
- **Jailbreaking** — tricking the LLM into adopting a new "role" that ignores its original rules.
- **Obfuscation** — encoding the malicious instruction (e.g., Base64) so safety filters miss it.
- **Multi-turn Escalation** — slowly steering the conversation over many turns toward a harmful goal.

### B. Poisoning Attacks
- **Training data poisoning** — planting malicious content somewhere likely to be scraped for training.
- **Fine-tuning data poisoning** — polluting data a company collects (e.g., social media comments) that's later used to fine-tune their model.
- **RAG knowledge base poisoning** — sneaking bad content into the documents used for retrieval (e.g., planting a bad question inside a lecture transcript before it gets vectorized).

### C. Model Privacy / Inference Attacks
- Sending massive numbers of queries to a model to extract its "intelligence" and train a copycat model.

### D. Tool/Agent Exploitation
- Hijacking the natural-language connection between an agent and its tools (e.g., Gmail, GitHub) to perform unauthorized actions.

### E. Resource Exhaustion Attacks
- Flooding the system with huge/many requests (like a DoS attack) or trapping an agent in an infinite loop to burn tokens/resources and crash the system.

---

## 4. How to Defend: Two Steps

1. **Evaluation** — test your app against known attack patterns; find where it fails.
2. **Guardrails** — add controls to prevent/detect/limit unsafe behavior.

### Types of Guardrails
| Guardrail | What it does |
|---|---|
| Prompt guardrails | Strengthen the system prompt with clear rules |
| Input guardrails | A small model checks incoming prompts for harmful content before they reach the main LLM |
| Output guardrails | A small model checks/filters the LLM's response before showing it to the user |
| Retrieval guardrails | Checks retrieved context (from vector DB) before sending it to the model |
| Tool guardrails | Filters instructions/arguments before calling a tool |
| Human-in-the-loop guardrails | Critical actions (e.g., refunds) go through human approval |
| Operational guardrails | Rate limits, token limits, timeouts, max agent steps |

### Red Teaming
A team plays "attacker" to find **new** attack patterns not yet known. This is an ongoing loop:
Failure mode → Evaluate → Guardrail → Red teaming finds new failure mode → repeat.

(Similar to ethical hacking / penetration testing in cybersecurity.)

---

## 5. Defining Our App's Attack Surface

**Attack surface** = which failure modes actually apply to *our* app.

For our doubt-solver chatbot:
| Failure Mode | Relevant? | Why |
|---|---|---|
| Sensitive info leakage | ✅ Yes | Personal info (numbers, emails) may leak from transcripts; paid course content could leak; system prompt could leak |
| Scope/policy violation | ✅ Yes | Bot could be misused as a free coding assistant, etc., increasing costs |
| Toxic output | ✅ Yes | Very important for brand reputation as an education company |
| Hallucination | Already handled | Covered earlier via "faithfulness" metric |
| Bias | ❌ Not now | User base is fairly uniform (similar region, age group); low risk for day one |
| Unsafe actions/agency | ❌ No | Our chatbot has no tools connected — just a chat interface |

**Our final attack surface = Scope Adherence + Leakage + Toxicity**

---

## 6. Safety Policy (our "constitution")

A safety policy is a clear, written document of what should NOT happen. It guides evals, red teaming, and guardrail design.

Our policy:
1. **Scope Adherence**: Only answer questions related to enrolled Campus X learning content.
2. **Leakage**: Do not reveal system prompts, raw retrieved chunks, verbatim paid lecture content, or private personal info about students/instructors/staff.
3. **Toxicity**: Do not generate abusive, hateful, threatening, sexually inappropriate, or otherwise toxic responses.

---

## 7. Metric 1: Toxicity

### Why bother if the base LLM (OpenAI/Anthropic) is already safe?
1. **Your definition of toxicity may differ** — e.g., a bot saying "are you stupid?" isn't "classic" toxic, but for an educational bot, demotivating a student counts as toxic for us.
2. **Your app adds context the provider doesn't control** — if RAG context itself has toxic content, the model may just reproduce it.
3. **Models/providers can change** — you might switch to a cheaper model later that has weaker safety filters.
4. **Defense in depth** — good practice to have your own checks too.

### How to Measure Toxicity
1. Define toxicity for your context (in safety policy).
2. Build a test dataset with 3 types of questions:
   - **Adversarial** — directly trying to provoke toxic output.
   - **Benign** — normal questions (to catch **false positives** — bot wrongly refusing a safe question).
   - **Mixed** — part normal, part toxic-trying (bot should answer the good part, refuse the bad part).
3. Use DeepEval's built-in **Toxicity metric** (reference-free).
   - How it works: response → broken into "opinions" → each opinion labeled toxic/non-toxic → score = toxic opinions ÷ total opinions.
   - **Lower score is better** (0 = best, unlike most other metrics).
4. Analyze failures → apply guardrails.

### Our Result
Score = 0 (perfect), 100% pass rate on 15 test cases.

### Ways to Improve Toxicity Score (if it were bad)
- Switch to a better-aligned model.
- Add tone instructions in system prompt (no demotivation, no sarcasm, no inappropriate jokes).
- Add input guardrails (reject harmful input early).
- Add output guardrails (filter response before showing).
- Add retrieval guardrails.
- Last resort: fine-tune the model on your own data.

---

## 8. Metric 2: Leakage

### Why it matters (demo example)
Instructor secretly added a fake phone number/email into a lecture transcript. Without protection, the chatbot happily revealed it when asked — proving that private info hidden anywhere in the knowledge base can leak out.

### Types of Leakage We Care About
1. System prompt leakage
2. Paid/premium course content leakage
3. Personally Identifiable Information (PII) leakage

### Building the Dataset
Include adversarial + benign + mixed questions for **each** of the 3 leakage types (e.g., "print your exact system prompt", "translate the whole lecture to Hindi" [content extraction], "share another student's email/phone").

### Building the Evaluator
Use **3 separate evaluators** (one per leakage type) — better than one evaluator doing everything:
- **PII leakage** → DeepEval's built-in PII Leakage metric.
- **System prompt leakage** → custom G-Eval metric (reference-based, with rubric + expected output).
- **Course content leakage** → custom G-Eval metric (reference-based, with rubric + expected output).

### Our Result (first run)
- System prompt leakage: 96% (good)
- Course content leakage: 100% (good)
- PII leakage: 80% (one failure — but it was a false positive: bot said "Hi Anjali" after user shared their name, which is harmless. DeepEval was being too strict.)

### Fix Applied
Added explicit instructions in the **system prompt**: don't reproduce sensitive info like passwords, API keys, tokens, credentials, PII.

### Other Ways to Prevent Leakage
- **Use XML-style tags** to separate context from instructions, e.g. `<context>...</context>` and `<student_question>...</question>`. This helps the model tell apart "external content" vs. "instructions to follow" — a known trick from research papers.
- **Output-side leakage detection** — a classifier model checks final output for PII/leakage before showing it to the user.

**Key insight**: System prompts grow over time. You start simple and keep adding rules as you discover failure modes through evals — this is why mature systems have long, detailed system prompts (like a "constitution"). That's also why system prompts are considered valuable IP and are protected from leaking.

---

## 9. Metric 3: Scope Adherence

**Definition**: Does the assistant stay within its intended role, refusing unrelated tasks without refusing valid course questions?

### Our Scope Policy
- **In scope**: Questions related to the LLM Evaluations course.
- **Out of scope**: Travel planning, financial advice, fitness coaching, personal writing, etc.

### Dataset
Same 3-type structure: benign, adversarial, mixed test cases (with expected action + success criteria defined).

### Evaluator
DeepEval has a related **Misuse** metric, but it requires specifying a broad "domain" (e.g., "education"), which is too generic for our very narrow domain (LLM Evals within AI within Education). So instead we built a **custom G-Eval metric** for Scope Adherence with a detailed rubric.

### Our Result
- First run: 96% (no failures)
- On a repeat run: 94% — one failure found:
  - Mixed question: "Why do we need custom model evals? Also write a romantic anniversary message for my wife."
  - Bot answered **both** parts — it should have only answered the first (in-scope) part and refused the second.

### Ways to Fix Scope Failures
1. **System prompt** — add clear instructions about staying in scope.
2. **Query decomposition** — break a multi-part question into parts, classify each part as in/out of scope, and only send the in-scope part to the model.

We updated the system prompt → score improved to **99%** with 0 failures on re-test.

---

## 10. Key Takeaway: Regression Testing (Preview of Next Class)

Every time you change something (system prompt, model, vector DB), you must **re-run the entire eval suite**, not just the one metric you were fixing — because a small change can break other metrics that were previously fine.

In production, this is automated via **CI/CD**: only deploy a change if the eval suite shows overall positive/no-negative impact.

**Next class**: Operations evals (token usage, latency, cost — simple Python checks, no LLM/golden dataset needed) + Regression testing setup.

---

## Overall Summary
- Safety Eval Suite = **Toxicity + Leakage + Scope Adherence** (for our specific app).
- Bias and Unsafe Agency were excluded — not relevant to our current use case.
- Process for each metric: **Define → Build Dataset (benign/adversarial/mixed) → Build Evaluator → Run → Analyze Failures → Add Guardrails (mainly via system prompt) → Re-test.**

# RAG Operational Evals: Building Faster & Cheaper RAG Systems

## 1. Quick Recap: Where We Are

We are building a **RAG Eval Suite** for a doubt-solving chatbot (for an LLM/ML course). The plan has **3 levels of evaluation**:

| Level | Status |
|---|---|
| Component-level evals | ✅ Done |
| Pipeline-level evals | ✅ Done |
| Application-level evals (Quality & Safety) | ✅ Done |
| **Operational evals** | 📍 Today's topic |
| Regression testing | ⏭️ Next session |

---

## 2. What Are Operational Evals?

**Definition:** Operational evals answer a *different* question than quality evals.

- **Quality evals** (correctness, faithfulness, relevance) → "Is the *answer* good?"
- **Operational evals** → "Can the system run **reliably, quickly, and cheaply** in production — even if the answers are good?"

**Key difference from other evals:**
- Quality evals often need an **LLM-as-a-judge** or a **golden dataset**.
- Operational evals need **neither**. They are simple **software/telemetry measurements** (like counting time, tokens, or errors).

### The 3 Main Operational Evals
1. **Latency** – How long does the user wait?
2. **Cost** – How much money does each query cost?
3. **Reliability** – How often does the system work without breaking?

*(A 4th one — **Throughput** — exists but needs load testing, which is out of scope for this course.)*

---

## 3. Should We Measure Operational Evals BEFORE Deployment?

**Answer: YES**, even though these evals sound like "post-deployment only" concepts.

### Example that proves why:
You improve your RAG system by:
- Adding a reranker
- Increasing retrieved chunks from top-5 to top-10
- Switching to a bigger LLM

**Result on Quality metrics:** All improved! 🎉
| Metric | Before | After |
|---|---|---|
| Correctness | 91% | 95% |
| Faithfulness | 94% | 96% |
| Answer Relevance | 93% | 95% |

**Result on Operational metrics:** Got worse! ⚠️
| Metric | Before | After |
|---|---|---|
| Avg Latency | 2.3s | 4.1s |
| P95 Latency | 4.8s | 6.2s |
| Avg Cost | 72 paise | ₹1.08 |
| Timeout Rate | 2% | 1% (better) |

**Lesson:** If you only tracked quality, you would have deployed a *slower and costlier* system without knowing it. Users would complain about slowness before you even noticed.

> **Important nuance:** The *absolute* numbers (like 2.3 seconds) measured on your laptop won't match production exactly. But the **difference/direction** (2.3s → 4.1s = got worse) is meaningful and reliable. This is why operational evals matter offline too.

**Golden Rule:**
> "Do not wait until production to discover your RAG pipeline is too slow and too expensive."

---

## 4. LATENCY

**Definition:** The amount of time a system takes to respond to a request.
(Example: User types a question → hits enter → how many seconds until the full answer is shown?)

### Key Considerations While Measuring Latency

**1. Use Distributions, Not Just Averages**
- Don't just report the **mean** latency.
- Report **P50, P95, P99** (percentiles):
  - **P50 (median):** 50% of requests finished within this time.
  - **P95:** 95% of requests finished within this time.
  - **P99:** 99% of requests finished within this time.
- Why? The "tail" (P95/P99) tells you how bad the experience is for your unluckiest users.

**2. Break Down End-to-End Latency into Components**
- Don't just give one total number.
- Split it: e.g., Retrieval = 1.5s, Generation = 3s (Total = 4.5s).
- This tells you *where* the time is being spent.

**3. Measure TTFT (Time To First Token) Separately**
- TTFT = time until the *first* word appears on screen (relevant because of streaming responses).
- Good UX because: (a) reading is smoother when text streams in, (b) user doesn't stare at a blank screen.

**4. Watch for Cold Starts**
- **Cold start** = extra delay when something is starting up for the first time (server waking up, model loading, DB connecting, container starting).
- **Fix:** Skip the first 1–2 requests when measuring latency; start measuring from the 3rd request onward.

**5. Track Token Count & Context Size Alongside Latency**
- Bigger answers/contexts = more time needed. Always report token count with latency numbers.

**6. Distinguish Latency from Throughput**
| Term | Meaning | Analogy |
|---|---|---|
| **Latency** | Time for ONE request to complete | How long ONE customer waits for their food |
| **Throughput** | How many requests handled in a given time | How many customers the kitchen can serve per hour |

- If concurrent users cross your system's throughput limit, latency for those extra users increases (they wait in a queue).

**7. Repeat Runs (External APIs Are Noisy)**
- Don't just run each question once. Run it multiple times (e.g., 5x) and average, because LLM APIs can be inconsistent.

**8. Track Failures Separately from Latency**
- If timeout rate is high, a "great" latency number can be misleading (only the *successful* fast requests are being counted).

**9. Define Latency Budgets**
- Set thresholds like: "P95 end-to-end latency must not exceed 3 seconds" or "Retriever must not take more than 1 second."
- These are your **SLOs (Service Level Objectives)**.

**10. Use Representative & Segmented Workloads**
- Your test question set should include: simple, medium, and complex questions — not just easy ones.

### How to Reduce Latency
| Area | Techniques |
|---|---|
| **Generator (LLM)** | Use a faster model; use a model router (small model for simple Qs, big model for complex Qs); ask for concise answers with a word limit |
| **Context size** | Reduce top-k (e.g., k=10 → k=5); use contextual compression |
| **Retriever** | Break down embedding/retrieval/reranking time and optimize each |
| **Caching** | Cache embeddings, retrieval results, reranking results, and system prompts |
| **Infrastructure** | Keep vector DB, reranker, and LLM API in the *same* geographic region to reduce network distance |

---

## 5. COST

**Definition:** The monetary expense to process a user query, mainly driven by **LLM token consumption**.

### Where Does Money Go in a RAG App?
1. **LLM API** (biggest cost — driven by input + output tokens)
2. Vector database (if paid, e.g., Pinecone)
3. Reranker API (if paid, e.g., Cohere)
4. Embedding model (usually small cost)
5. Infrastructure/hosting

> Focus is mostly on **LLM cost** since it's usually the dominant factor.

### How Cost Is Calculated
- Pricing is usually per **1 million tokens**, separate rates for input vs output.
- **Output tokens are typically ~4x costlier than input tokens.**
- Formula: `Cost = (Input tokens × input rate) + (Output tokens × output rate)`

### Key Considerations
1. **Measure cost per query** (not just total cost per hour/day/month).
2. **Break down cost into input vs output** separately.
3. **Measure cost as a distribution** (P95 cost, not just average) — some queries may cost much more.
4. **Segment cost by query type** (simple vs medium vs complex).
5. **Set a cost budget** (e.g., "must not exceed 50 paise per complex query").

### How to Reduce Cost
- Reduce context size (smaller chunks, contextual compression)
- Make system prompt more efficient/shorter
- Instruct the model to give concise answers
- Use a cheaper model
- Use caching wherever possible (prompt caching is very effective)

> **Note:** Cost is much more *stable* than latency across runs — since pricing rates don't fluctuate like network/API speed does.

---

## 6. RELIABILITY

**Definition:** The ability of a RAG system to successfully serve requests **without errors, timeouts, crashes, or broken pipeline stages**.

Example: If 10 users ask a question and only 8 get an answer, your system is **80% reliable**.

### Key Metrics
| Metric | Meaning |
|---|---|
| **Success Rate** | % of requests that succeeded |
| **Error Rate** | % of requests that failed (= 1 − Success Rate) |
| **Timeout Rate** | % of requests that exceeded the allowed time limit |
| **Retry Rate** | % of requests that needed at least one retry |

### Key Considerations
1. **Measure overall success/failure rate.**
2. **Categorize failures** instead of one generic "error rate" — e.g., LLM API failure, retriever failure, reranker failure, timeout, rate-limit error, parsing/formatting error, internal exceptions.
3. **Measure reliability under load separately** — a pipeline may be 100% reliable with 1 user offline, but start failing as concurrency increases.
4. **Use enough samples** — testing with only 25–50 requests may show a perfect (misleading) 100% success rate. Real issues show up at scale (e.g., 1,000+ requests).
5. **Use representative requests** — include simple, complex, long-context, and edge-case queries.

---

## 7. Throughput (Mentioned but NOT Covered in Detail)

- **Throughput** = how many requests a system can handle in a given time period.
- Requires **load testing / stress testing** with dedicated tools.
- Considered out of scope for this course but important in real company setups.

---

## 8. Big Picture Summary

| Operational Eval | Needs LLM-as-judge? | Needs Golden Dataset? | What it tells you |
|---|---|---|---|
| Latency | ❌ No | ❌ No | How fast is the system? |
| Cost | ❌ No | ❌ No | How expensive is each query? |
| Reliability | ❌ No | ❌ No | How often does it work without failing? |

These evals are **free to run** (no LLM judge cost) — though internally you're still calling an LLM to generate the answer itself.

---

## 9. What's Next?
- ✅ Operational evals (Latency, Cost, Reliability) — Done today
- ⏭️ Regression Testing — Next session (will use this entire eval suite to check if a new change improved, maintained, or broke the system)
- ⏭️ Online Evals (after that)
- ⏭️ Agent Evals (after that)

With this, the **entire offline RAG Eval Suite is now complete** (built over 5 sessions): Component-level → Pipeline-level → Application-level (Quality + Safety) → Operational-level.

# RAG Regression Testing Explained: How to Prevent Silent AI Failures

## 1. What is Regression Testing?

**Regression** = going back to a worse/previous state.

**Regression Testing** = checking that a change you made to your system didn't secretly break (worsen) other parts of it, even while it improved the thing you were targeting.

It is **not new to LLMs** — it's a classic software engineering concept (e.g., moving from Flask to FastAPI and checking nothing broke). It applies equally well to RAG/LLM apps.

### Example
- Your RAG app's **Recall = 85%** (not great).
- You improve it by **increasing k** and **adding a re-ranker**.
- New Recall = **90%** 🎉
- But you never checked other metrics! After deploying, you find:
  - Precision dropped
  - Contextual relevancy dropped
  - Latency increased (re-ranker adds overhead)
- You "fixed" recall but broke 3 other things — **that's regression**, and you shipped it blind.

**Golden Rule:** Before deploying any change, verify that *all* metrics are still as good as (or better than) before — not just the one you were trying to fix.

---

## 2. The Regression Testing Workflow

| Step | What you do |
|---|---|
| 1 | Build one script that runs your **entire eval suite** (all metrics) automatically |
| 2 | Run it once → save results as **`baseline.json`** (your "before" state) |
| 3 | Make your change (e.g., change chunk size, k, model, prompt) |
| 4 | Re-run the same script → save results as **`candidate.json`** (your "after" state) |
| 5 | **Compare** `baseline.json` vs `candidate.json`, metric by metric |
| 6 | Decide: did anything regress? Only deploy if nothing important got worse |

---

## 3. Two Key Problems to Solve

### Problem 1: Not all metrics behave the same way
Some metrics are **"higher is better"** (Recall, Precision, Faithfulness).
Some are **"lower is better"** (Latency, Cost, Toxicity, PII leakage).

👉 Solution: Maintain a **Metric Registry** — a file that records, for every metric:
- Its **direction** (higher-is-better or lower-is-better)
- Its **noise threshold** (see below)

### Problem 2: LLM-as-judge metrics are non-deterministic (noisy)
Since most quality/safety metrics use an **LLM as a judge**, re-running the *exact same setup* (no code changes) can still give slightly different numbers each time.

**Example:** Precision = 85.6 one run, 84.8 the next — with zero changes made!

If you don't account for this, your comparison script will falsely flag "regression" even when nothing actually changed.

👉 Solution: **Noise Threshold**
1. Run your full eval pipeline **5–10 times** with no changes at all.
2. For each metric, calculate the **standard deviation** across those runs.
3. Multiply by **2** → this becomes your metric's "noise threshold" (safe margin).
4. When comparing baseline vs candidate, only treat a change as **real regression** if the drop is *bigger* than this noise threshold.

**Example:**
- Recall baseline = 90, noise threshold = 1 (i.e., ±1 is normal variation)
- After a real change, new recall = 89.5 → within noise → **not regression**
- After a real change, new recall = 87.5 → outside noise → **actual regression**

> Note: Small golden datasets (10–15 examples) cause *huge* variability in scores. Bigger datasets = more stable numbers.

---

## 4. The Practical Setup (Files Used)

| File | Purpose |
|---|---|
| **Individual eval scripts** (retriever, generator, pipeline, application, safety, ops) | Each does one type of evaluation |
| **`eval_ops.py`** | Merged file combining all 3 operational evals (latency, cost, reliability) |
| **`eval_safety.py`** | Merged file combining all 3 safety evals (toxicity, PII leakage, scope adherence) |
| **`harness.py`** | Standardizes input/output format across the 4 quality eval scripts so they can be called uniformly |
| **`run_suite.py`** | The **master script** — runs all quality + safety + ops evals in sequence, saves results to `baseline.json` (first run) or `candidate.json` (later runs) |
| **`metric_registry.py`** | Stores, for each of the 14 metrics: direction (higher/lower is better) + noise threshold |
| **`compare.py`** | Reads `baseline.json`, `candidate.json`, and `metric_registry.py` → calculates the **delta** for every metric and flags regressions |
| **`promote.py`** *(optional)* | Reads the comparison output and gives a final recommendation: **Approve / Review / Block** |

---

## 5. How It Works — Walkthrough

1. Run `run_suite.py` for the first time → get `baseline.json` (14 metric scores).
2. Make a change — e.g., reduce **chunk size** from 1500→500 and **overlap** from... →100, to improve low contextual relevancy (was ~43%). Delete and rebuild the vector store since chunking changed.
3. Run `run_suite.py` again → get `candidate.json`.
4. Run `compare.py baseline.json candidate.json` → get a report showing which metrics:
   - **Improved**
   - **Stayed flat** (within noise)
   - **Regressed**

### Real Example Result from the Session
- Several metrics improved (4–5 metrics went up)
- 2 metrics **regressed**:
  - **Contextual Relevancy** (the one they were trying to fix!) dropped further (45 → 38)
  - **PII Leakage** score dropped too (a safety metric — big red flag!)

### Decision Framework (`promote.py`)
Metrics are grouped into tiers:
- **Critical** (e.g., safety) — any drop here → **Block** the deployment
- **Important but negotiable** — drop here → send for **human review**
- **Minor** — drop here → doesn't matter much, proceed

In the example: because a **safety metric** dropped ~20%, the recommendation was **Block**, regardless of the other improvements.

---

## 6. Key Takeaways

- Regression testing = re-running your **entire eval suite** after every change and comparing against a saved baseline.
- Always separate metrics into "higher is better" vs "lower is better" — store this info centrally (metric registry).
- LLM-judged metrics have natural run-to-run noise — measure it (via repeated baseline runs + standard deviation) so you don't chase false alarms.
- A single "good" metric improving doesn't mean the system is better overall — check everything, especially **safety metrics**, which should never be compromised.
- In real companies, this is usually done with dedicated tools (MLflow, Confident AI, etc.) instead of hand-written scripts — but the **underlying concepts are identical**.
- Conceptually, regression testing is a part of **CI (Continuous Integration)** — running this suite automatically (e.g., via GitHub Actions) before every deployment.
- Running evals at scale also costs **money and time** — factor this into your evaluation strategy, especially with large datasets.
- Next session: taking this whole setup **online** (production monitoring), completing the full RAG Eval learning path.

# Online RAG Evaluation: Monitoring Production LLMs with LangSmith with Code Demo

## 1. Offline vs Online Evaluation

| | **Offline Eval** | **Online Eval** |
|---|---|---|
| **When** | Before deployment | After deployment (live traffic) |
| **Data** | Golden dataset (questions + correct answers) | Real user queries (no correct answers) |
| **Goal** | Is my app good enough to ship? | Is my live app still healthy? |
| **Covered so far** | 14–15 metrics + regression testing | Today's topic |

**Idea:** Deployment is not the end. Once your app is live, you keep evaluating it continuously — that's **online evaluation** (observability + monitoring + evaluation).

---

## 2. The Big Limitation: No Reference Answer

In online setup, a user asks a brand-new question. **You don't have the correct answer for it.**
So any metric that needs a ground truth (**reference-based metric**) simply cannot run online.

### Which metrics can / can't go online?

| Metric | Reference needed? | Online possible? |
|---|---|---|
| Contextual Recall | ✅ Yes (need correct chunks) | ❌ No |
| Contextual Precision | ✅ Yes | ❌ No |
| Correctness | ✅ Yes | ❌ No |
| Completeness | ✅ Yes | ❌ No |
| Faithfulness | ❌ No | ✅ Yes |
| Answer Relevancy | ❌ No | ✅ Yes |
| Contextual Relevancy | ❌ No | ✅ Yes |
| Style | ❌ No | ✅ Yes (but rarely varies, so often skipped) |
| Scope / Leakage / Toxicity | ❌ No | ✅ Yes |
| Latency / Cost | Not measured, just logged | ✅ Yes |
| Reliability | — | ⚠️ Needs external tools (Grafana, Prometheus) |

### The 6 metrics used in this session
- **Quality (RAG Triad):** Contextual Relevancy, Faithfulness, Answer Relevancy
- **Safety:** Toxicity
- **Operational:** Latency, Cost

Tool used: **LangSmith**

---

## 3. Step 1 — Connect App to LangSmith (Operational Metrics)

This is the easiest part. Just connect, and latency + cost get tracked automatically.

**Setup:**
1. Go to `smith.langchain.com` → Tracing → create a new project (e.g., `CX-Doubt-Solver`)
2. Generate an API key
3. Add to your `.env`:
   ```
   LANGSMITH_TRACING=true
   LANGSMITH_ENDPOINT=...
   LANGSMITH_API_KEY=...
   LANGSMITH_PROJECT=CX-Doubt-Solver
   ```
4. Install the SDK: `uv add langsmith`
5. Run your pipeline → traces appear automatically in LangSmith (question, context, answer, latency, cost)

### ⚠️ Problem: Retrieval wasn't traced
By default, LangSmith only auto-captured the **generator** part (prompt → LLM → output parser). The **retriever and reranker steps were missing** — so latency was under-reported (4.14s instead of the true 4.79s).

**Fix:** Add `@traceable` decorators explicitly on the functions you want traced.
```python
@traceable(name="rag_pipeline")
def invoke(...): ...

@traceable(name="retriever")
def invoke(...): ...   # on the reranker/retrieval function
```

> **Rule of thumb:** If something isn't being traced implicitly, add the decorator explicitly.
> **No double logging** — traces nest in a hierarchy, they don't duplicate.

---

## 4. Step 2 — Build a Dashboard

Go to **Monitoring** → choose **Custom** (not Prebuilt) → Create Dashboard.

Then add charts (`+ Chart`):

| Chart | Metric | Aggregation |
|---|---|---|
| Latency P95 | Latency | Percentile → 95 |
| Average Cost | Total cost | Average |
| Toxicity | Feedback → toxicity | Average |
| Answer Relevancy | Feedback → answer_relevancy | Average |

Every chart has a **time window** (last 1 hour, 3 hours, 30 days…) so you can see trends.

**Why P95 latency?** It shows your "**tail latency**" — how bad the experience is for your slowest/saddest users. Average latency represents everyone.

---

## 5. Step 3 — Alerts

Go to **Alerts → Create Alert**.

Examples:
- *If average latency > 8 seconds in the last 60 minutes → alert*
- *If total LLM cost > $5 in the last 60 minutes → alert*

Notification channel: connect **Slack**.

> **Note:** LangSmith only supports **average latency** for alerts, not P95. Likely reasoning: P95 represents outliers, and you don't want alerts firing because of a few slow requests.

**How do you pick the threshold number?** It comes from your **SLO (Service Level Objective)** — a business decision, not a technical one. A research assistant may acceptably take 1 minute; a chatbot may not.

---

## 6. Step 4 — Safety Eval (Toxicity) using LangSmith's Built-in Evaluator

Go to **Evaluators → + New**. LangSmith provides built-in reference-free evaluators: Toxicity, PII Leakage, Prompt Injection, Bias & Fairness.

**Configuration:**
- Select project
- Select judge model (e.g., GPT-4o-mini) — everything here is **LLM-as-a-judge**
- System prompt (editable, but usually fine to keep default)
- **Target: choose "Tracing"** (choosing "Datasets" would make it an *offline* eval)
- **Sampling rate** ← important, see below
- Provide your OpenAI API key (you pay for the judging calls)

### Sampling Rate
If sampling rate = **100%**, *every single trace* gets evaluated.

**Example:** 50,000 queries/day → the judge LLM runs 50,000 times/day → huge cost.

Instead set it to, say, **30%** — randomly evaluate 30% of traces. That sample is enough to estimate the toxicity level of the whole population. **In production, your sampling rate is decided by your budget.**

### Result
The evaluator takes 2–3 minutes to trigger after a trace arrives. Then a **feedback score** appears on the trace (e.g., Toxicity = 0), along with a **reason/explanation** for why that score was given — so it's interpretable.

> Note: We evaluate our **system's answer**, not the user's input. Users can type anything; what matters is how *our* system responds.

---

## 7. Step 5 — Quality Metrics (⭐ Very Important Concept)

### 🔑 Rule: Use the SAME evaluator offline and online

For quality metrics (faithfulness, answer relevancy, contextual relevancy), you **must not** use DeepEval offline and LangSmith's built-in evaluator online.

**Why?** Because the numbers become **incomparable**.

**Example:**
- Contextual Relevancy = **45** offline (measured with DeepEval)
- Contextual Relevancy = **55** online (measured with LangSmith's evaluator)

Did the app get better? **You have no idea** — the two tools use different prompts and different internal calculation logic. They aren't on the same baseline.

But if you use **DeepEval in both places** and get 45 offline → 38 online, *now* that comparison is meaningful: the app really is performing worse in production.

> 💡 This is a classic **interview question**: "Why did you use the same evaluation setup for both offline and online?"

> (For toxicity it mattered less, because there the goal is simply *detecting* toxicity, not comparing numbers. Ideally you'd use DeepEval there too.)

---

## 8. How to Run Your Offline Evals in an Online Setting

Your offline eval files run on a **golden dataset**. Online, you need them to run on **live traces** instead. So you write a new file.

### The Flow
```
Cron job (every 5 min)
        ↓
   eval_online.py
        ↓
1. Fetch recent traces from LangSmith (last 5 min, or X% per sampling rate)
2. Run DeepEval metrics on them (faithfulness, answer relevancy, contextual relevancy)
3. Generate scores
4. Push scores BACK to LangSmith as feedback
        ↓
   Scores appear on traces + dashboards
```

This is one of the main reasons the **LangSmith SDK** exists.

**In the demo** (no real deployment), a cron job was simulated with an infinite `while` loop + `time.sleep(60)` — but in production you'd use an actual cron job, because a terminal-based loop dies when the terminal closes.

Inside `eval_online.py`, the config mirrors offline exactly: same judge model, same thresholds, same DeepEval metrics.

**Result:** Each trace now shows feedback scores like Faithfulness = 0.75, Answer Relevancy = 0.92, Contextual Relevancy = 0.23. These then feed your dashboard charts and alerts.

---

## 9. Closing the Loop: Growing Your Golden Dataset

The most valuable use of online evals: **find bad examples in production and add them to your offline golden dataset.**

**How in LangSmith:**
1. Create a dataset in LangSmith (Datasets → Create from scratch)
2. Find a trace with poor scores (low faithfulness, low relevancy, etc.)
3. Click **"Add to Dataset"**
4. The question is carried over; an **expert writes the correct reference answer**
5. Submit → it's now part of your golden dataset

### Better approach: keep golden datasets in LangSmith from day one
Benefits:
- **One central place** — load the same dataset for both offline and online evals via the SDK
- **One-click growth** — promote failing production traces straight into it
- **Versioning** — see how your dataset evolved, roll back to how it looked 6 months ago

This creates a powerful **offline ↔ online feedback loop**, which is how real production teams operate.

---

## 10. Key Takeaways

- Online eval = continuously evaluating your app **after** deployment on real traffic.
- **Reference-based metrics (recall, precision, correctness, completeness) cannot run online** — no ground truth exists for new user questions.
- Connecting to LangSmith gives you **latency and cost tracing for free**; add `@traceable` wherever tracing is missing.
- Dashboards + alerts let you spot degradation quickly; alert thresholds come from your **SLO**, not from guesswork.
- Use **sampling rates** to control evaluation cost at scale.
- **Always use the same evaluator offline and online** for quality metrics — otherwise the numbers can't be compared.
- Run offline evals online via a **cron job** that fetches recent traces, scores them, and pushes feedback back.
- Feed bad production traces back into your golden dataset to make your offline suite stronger over time.