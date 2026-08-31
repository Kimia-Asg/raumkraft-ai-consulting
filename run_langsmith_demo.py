"""
RaumKraft LangSmith Monitoring Demo
------------------------------------
This script:
1. Uploads the evaluation dataset (data/langsmith_eval_dataset.json) to LangSmith
2. Runs each example through the OpenAI listing-generation prompt
3. Traces every call automatically to LangSmith (so you can see full observability)

HOW TO USE:
1. Fill in your two API keys below (OPENAI_API_KEY and LANGSMITH_API_KEY)
2. Run: python run_langsmith_demo.py
3. Go to https://smith.langchain.com and check your project + dataset
"""

import os
import json

# ============================================================
# STEP 1: PASTE YOUR API KEYS HERE
# ============================================================
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")

# ============================================================
# Setup — do not edit below this line
# ============================================================
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["LANGSMITH_API_KEY"] = LANGSMITH_API_KEY
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_PROJECT"] = "raumkraft-listing-poc"

from langsmith import Client, traceable
from openai import OpenAI

client = Client()
openai_client = OpenAI()

SYSTEM_PROMPT = """You are a copywriter for RaumKraft Immobilien & Design, a premium German real estate and interior design firm. Write property listings in German that are:
- Professional but warm — not robotic, not overly salesy
- Factually accurate — use ONLY the data provided, never invent features
- Structured: headline, lifestyle paragraph, key facts, neighbourhood note, CTA
- Length: 150–200 words
- Mention energy class naturally
- If target audience is specified, subtly tailor the tone

Never fabricate amenities, transportation connections, or neighbourhood details not provided in the input. If information is missing, omit it — do not guess."""


@traceable(name="generate_listing")
def generate_listing(property_data: dict) -> str:
    """Generates a property listing draft — this call is auto-traced to LangSmith."""
    user_content = f"""Property type: {property_data.get('property_type')}
District: {property_data.get('district')}
Size: {property_data.get('size_sqm')} sqm
Rooms: {property_data.get('rooms')}
Floor: {property_data.get('floor')} of {property_data.get('total_floors')}
Features: {', '.join(property_data.get('features', []))}
Energy class: {property_data.get('energy_class')}
Asking price: €{property_data.get('asking_price')}
Target audience: {property_data.get('target_audience', 'general')}"""

    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_content},
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content


def main():
    # Load the eval dataset
    data_path = os.path.join(
        os.path.dirname(__file__), "data", "langsmith_eval_dataset.json"
    )
    with open(data_path, "r", encoding="utf-8") as f:
        examples = json.load(f)

    print(f"Loaded {len(examples)} examples from langsmith_eval_dataset.json")

    # 1. Create (or reuse) the dataset in LangSmith
    dataset_name = "raumkraft-listings-eval"
    try:
        dataset = client.create_dataset(dataset_name)
        print(f"Created new dataset: {dataset_name}")
    except Exception:
        dataset = client.read_dataset(dataset_name=dataset_name)
        print(f"Using existing dataset: {dataset_name}")

    # 2. Upload each example as a dataset example
    for i, ex in enumerate(examples):
        client.create_example(
            inputs=ex["input"],
            outputs=None,  # we don't have "correct" outputs, this is generative
            dataset_id=dataset.id,
        )
    print(f"Uploaded {len(examples)} examples to dataset '{dataset_name}'")

    # 3. Run each example through the real LLM call — this creates traces in LangSmith
    print("\nRunning generation for each example (this will take a minute)...\n")
    for i, ex in enumerate(examples):
        result = generate_listing(ex["input"])
        print(f"--- Example {i+1}: {ex['input'].get('property_type')} in {ex['input'].get('district')} ---")
        print(result[:200] + "...\n")

    print("\nDone! Go to https://smith.langchain.com")
    print(f"-> Project: raumkraft-listing-poc (shows all traces)")
    print(f"-> Dataset: {dataset_name} (shows all uploaded examples)")


if __name__ == "__main__":
    main()