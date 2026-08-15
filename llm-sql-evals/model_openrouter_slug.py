"""
The 5 models under test, as OpenRouter slugs.
Kept as a list of (display_name, slug) so output tables show friendly names.
"""
MODELS = [
    ("Grok 4.5",        "x-ai/grok-4.5"),
    ("Claude Sonnet 5", "anthropic/claude-sonnet-5"),
    ("MiniMax M3",      "minimax/minimax-m3"),
]

if __name__ == "__main__":
    print(f"{len(MODELS)} models under test:")
    for name, slug in MODELS:
        print(f"  {name:18s} -> {slug}")