# POC Documentation — RaumKraft AI Assistant

## Overview

This document covers the Proof of Concept (POC) built in Round 1 and its evolution into the Round 2 MVP. The POC demonstrated that AI-assisted property listing generation is technically feasible, cost-effective, and transparent — addressing CEO Chleo's core concern that "AI is a black box."

## Round 1 POC — n8n Workflow

### Tools Used

| Tool | Purpose |
|---|---|
| n8n Cloud | No-code workflow automation |
| OpenAI API (GPT-4o-mini) | Text generation for property listings |
| LangSmith | Trace monitoring — input, output, duration |
| Webhook (n8n) | Trigger point for incoming property data |

### Workflow Steps

1. **Webhook trigger** — receives structured property data (JSON) via HTTP POST
2. **Edit Fields node** — formats the property data into a clean prompt
3. **OpenAI node** — sends formatted prompt to GPT-4o-mini with the system prompt (German listing copywriter, 150–200 words, structured format, never fabricate)
4. **Response** — returns the generated listing text

### Workflow File

`n8n/workflow.json` — importable into any n8n instance.

### What the POC Proved

- GPT-4o-mini generates quality German property listings from structured input
- Output follows the required structure (headline, lifestyle paragraph, key facts, neighbourhood note, CTA)
- Response time is under 5 seconds per listing
- The model respects the "never fabricate" constraint when prompted correctly
- Cost per listing is a fraction of a cent

### What the POC Did NOT Prove

- No user interface — only testable via webhook/API call
- No enquiry triage capability (UC2)
- No editable output — agent cannot review and modify in-place
- No cost tracking per request
- No batch processing
- Single use case only

### Screenshots

See `n8n/screenshots/` for workflow editor and test output screenshots.

## LangSmith Monitoring (Round 1)

### Setup

- Project: `raumkraft-listing-poc`
- 5 traced runs with real property inputs
- Evaluation dataset: `raumkraft-listings-eval` (5 input/output examples)

### What Was Traced

- Full input prompt (property data)
- Full output text (generated listing)
- Response duration
- Token count

### What Was NOT Traced in Round 1

- API cost per request (added in Round 2 via LangChain integration)

### Screenshots

See `langsmith/screenshots/` for trace and evaluation dataset screenshots.

## Round 1 → Round 2 Evolution

| Aspect | Round 1 POC | Round 2 MVP |
|---|---|---|
| Tool | n8n Cloud (no-code) | Streamlit + Python (low-code) |
| Interface | Webhook only (no UI) | Web app with form inputs and editable output |
| Use cases | UC1 only (listing generation) | UC1 + UC2 (listing + enquiry triage) |
| Data | Synthetic (500 properties) | Real-world Kaggle data (Germany Housing dataset) |
| Output | Raw text response | Editable text area + approve button |
| Monitoring | LangSmith traces (no cost) | LangSmith traces with automatic cost tracking via LangChain |
| Human review | Not possible in workflow | Built into UI — agent edits before approving |
| Reproducibility | Import workflow JSON into n8n | `pip install` + `streamlit run app.py` |

### Why the Upgrade?

The n8n POC validated the AI capability but had three gaps the MVP addresses:

1. **No UI for agents** — the POC was only testable via API calls. The MVP gives agents a real interface they can use daily.
2. **Single use case** — Round 1 feedback confirmed UC1 alone is too simple. The MVP adds UC2 (enquiry triage).
3. **No cost visibility** — switching from raw OpenAI client to LangChain enables automatic cost tracking in LangSmith, which strengthens the transparency story for Chleo.

## How to Reproduce the Round 1 POC

1. Import `n8n/workflow.json` into an n8n instance (cloud or self-hosted)
2. Set the OpenAI API key in the n8n credentials
3. Send a POST request to the webhook URL with property data JSON:

```json
{
  "property_type": "Wohnung",
  "district": "Hamburg-Eppendorf",
  "size_sqm": 75,
  "rooms": 3,
  "energy_class": "B",
  "asking_price": 350000,
  "features": "Balkon, Einbauküche, Fußbodenheizung"
}
```

4. The workflow returns a German property listing

## How to Reproduce the Round 2 MVP

See `mvp/mvp_documentation.md` for full setup instructions.

## Demo Recording

A recorded demo of both the POC and MVP is available in the presentation materials. The demo covers:

1. POC: n8n workflow execution with sample property data
2. MVP: Streamlit app — UC1 listing generation + UC2 enquiry triage
3. LangSmith: Trace view showing input, output, duration, and cost
