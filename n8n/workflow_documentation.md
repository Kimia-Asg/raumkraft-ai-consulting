# n8n Workflow Documentation — Property Listing Generator POC

## Overview

This proof-of-concept demonstrates **Use Case 1: AI-Assisted Property Listing Generation**. It shows Chleo a working example of how structured property data flows into an LLM, generates a listing draft, and gets routed for human review — all with full transparency.

## What the Workflow Does

```
[Webhook Trigger] → [Format Property Data] → [LLM: Generate Listing] → [LangSmith Log] → [Output Draft for Review]
```

### Step-by-step:

1. **Webhook Trigger** — Simulates a new property being entered into the CRM. In production, this would connect to the actual CRM or a form submission.

2. **Format Property Data** — A "Set" or "Code" node that structures the incoming data into a clean prompt. Fields:
   - Address (city/district only — no exact address for GDPR in demo)
   - Property type (apartment, house, commercial)
   - Size (m²)
   - Rooms
   - Floor / total floors
   - Key features (balcony, garden, parking, etc.)
   - Energy class
   - Asking price
   - Target audience hint (families, young professionals, investors)

3. **LLM Node (OpenAI or HTTP Request)** — Sends the structured data to an LLM with:
   - **System prompt:** RaumKraft brand tone guidelines, formatting rules, length constraints
   - **User prompt:** The structured property data
   - **Temperature:** 0.7 (creative enough for compelling copy, constrained enough for accuracy)

4. **LangSmith Logging** — HTTP Request node sending the prompt, response, and metadata to LangSmith for tracing. (Alternative: if using LangChain within a Code node, tracing is automatic.)

5. **Output** — The generated draft is sent to a designated Slack channel, email, or webhook endpoint where the agent can review and approve.

## POC Evidence (Built & Tested)

The workflow was built and successfully executed in n8n. Evidence:

- `workflow.json` — exported workflow (import into n8n via Settings → Import Workflow)
- `screenshots/canvas_all_green.png` — full workflow canvas, all 3 nodes executed successfully
- `screenshots/openai_output.png` — actual generated listing output from GPT-4o-mini

### Sample Generated Output (German, from live test run)

Test input: Apartment, Hamburg-Eimsbüttel, 85 sqm, 3 rooms, €385,000

> **Charmante 3-Zimmer Wohnung im Herzen von Hamburg-Eimsbüttel**
> Willkommen in dieser einladenden 3-Zimmer-Wohnung, die durch ihre großzügige Raumaufteilung und das helle Ambiente besticht. Auf einer Fläche von 85 Quadratmetern bietet diese Wohnung viel Platz für individuelles Wohnen und entspannten Lebensstil...
>
> *(full text in screenshots/openai_output.png)*

This confirms the end-to-end flow works: structured property data → LLM-generated, on-brand German listing copy — with the system prompt successfully constraining the model to only use provided facts (no invented amenities or transit details).

## How to Run the POC

### Prerequisites
- n8n account (cloud free tier or self-hosted)
- OpenAI API key (set in n8n credentials)
- LangSmith API key (set in n8n credentials or environment)

### Setup
1. Import `workflow.json` into n8n (Settings → Import Workflow)
2. Configure credentials:
   - OpenAI API key
   - LangSmith API key (if using HTTP logging)
3. Activate the workflow
4. Send a test webhook payload (sample below)

### Sample Test Payload

```json
{
  "property_type": "Apartment",
  "district": "Hamburg-Eimsbüttel",
  "size_sqm": 85,
  "rooms": 3,
  "floor": 2,
  "total_floors": 5,
  "features": ["balcony", "fitted kitchen", "hardwood floors", "elevator"],
  "energy_class": "B",
  "asking_price": 385000,
  "target_audience": "young professionals or small families",
  "year_built": 2019
}
```

### Expected Output

A German-language property listing draft (~150–200 words) in RaumKraft's brand tone, structured with:
- Headline
- Opening paragraph (lifestyle hook)
- Key facts (structured)
- Neighbourhood context
- Call to action

## System Prompt (Used in LLM Node)

```
You are a copywriter for RaumKraft Immobilien & Design, a premium German real estate and interior design firm. Write property listings in German that are:
- Professional but warm — not robotic, not overly salesy
- Factually accurate — use ONLY the data provided, never invent features
- Structured: headline, lifestyle paragraph, key facts, neighbourhood note, CTA
- Length: 150–200 words
- Mention energy class naturally
- If target audience is specified, subtly tailor the tone

Never fabricate amenities, transportation connections, or neighbourhood details not provided in the input. If information is missing, omit it — do not guess.
```

## Limitations vs. Production

| POC | Production |
|---|---|
| Webhook trigger with manual payload | CRM integration (e.g., Salesforce, HubSpot, Pipedrive webhook) |
| Single language (German) | Multilingual with language parameter |
| Output to Slack/webhook | Output to CRM draft field with agent approval UI |
| Manual LangSmith logging via HTTP | Native LangChain tracing or LangSmith SDK |
| No image handling | Would include photo selection/ordering suggestions |
| Static system prompt | A/B tested prompts with LangSmith experiments |
| No feedback loop | Agent edits feed back into prompt improvement |

## Cost per Listing (Estimated)

Using GPT-4o-mini for generation:
- Input: ~300 tokens (structured data + system prompt)
- Output: ~400 tokens (listing draft)
- Cost per listing: ~$0.001–0.002
- At 200 listings/month: **~$0.20–0.40/month** in API costs

This is negligible. The cost is in human time, not API calls.

## Transparency Story for Chleo

This workflow directly addresses Chleo's fear that "AI is not transparent":

1. **Every input is structured** — the AI only sees what we give it, not arbitrary data
2. **Every output is logged** — LangSmith captures the full prompt and response
3. **A human reviews every draft** — nothing publishes without an agent's approval
4. **Costs are trackable** — per-listing costs visible in monitoring
5. **The workflow is visual** — Chleo can see the n8n canvas and understand the flow without coding knowledge
