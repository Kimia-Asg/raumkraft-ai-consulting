# MVP Documentation — RaumKraft AI Assistant

## Overview

The RaumKraft AI Assistant is a Streamlit web application that provides two AI-powered tools for RaumKraft Immobilien & Design:

1. **UC1 — Property Listing Generator:** Generates polished German sales listings from structured property data.
2. **UC2 — Client Enquiry Triage:** Classifies incoming enquiries by type and urgency, then drafts a response for agent review.

Both tools keep a human in the loop — AI generates drafts, agents review and approve before any action. All AI interactions are traced in LangSmith for full transparency and cost tracking.

## Tech Stack

| Component | Technology | Why |
|---|---|---|
| Frontend | Streamlit | Fast prototyping, Python-only, no frontend code needed |
| LLM | OpenAI GPT-4o-mini (via LangChain) | Low cost per request, fast response, sufficient quality for text generation |
| LLM Framework | LangChain (`langchain-openai`) | Automatic token counting and cost tracking in LangSmith |
| Monitoring | LangSmith | Full trace of every AI call — input, output, duration, cost |
| Language | Python 3.10+ | Industry standard, compatible with all dependencies |

## Data Source

- **Round 1:** Synthetic data (500 properties, 1,200 enquiries) generated via Python scripts.
- **Round 2:** Real-world data from Kaggle — [Germany Housing - Rent and Price](https://www.kaggle.com/phanindraparashar/germany-housing-rent-and-price-data-set-apr-20), originally sourced from ImmobilienScout24. Sale listings filtered and used for UC1 property input.

## Repo Structure

```
mvp/
├── app.py               # Main Streamlit application (UC1 + UC2)
├── requirements.txt     # Python dependencies
├── .env.example         # Template for API keys (copy to .env)
├── .env                 # Actual API keys (NOT in git)
└── mvp_documentation.md # This file
```

## How to Run

### Prerequisites
- Python 3.10 or higher
- OpenAI API key
- LangSmith API key (free tier works)

### Setup

```bash
# 1. Navigate to the MVP folder
cd mvp

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create your .env file from the template
cp .env.example .env
# Edit .env and add your actual API keys

# 4. Run the app
streamlit run app.py
```

The app opens in your browser at `http://localhost:8501`.

### Environment Variables

| Variable | Description | Where to get it |
|---|---|---|
| `OPENAI_API_KEY` | OpenAI API key | https://platform.openai.com/api-keys |
| `LANGSMITH_API_KEY` | LangSmith API key | https://smith.langchain.com/settings |

These are set automatically via the `.env` file. LangSmith tracing is enabled by default — every AI call is logged to the `raumkraft-mvp` project.

### UC3 — Design Brief Generator (+ Image Prompt Generation)

**Input:**
- Meeting notes / consultation transcript (pasted text)
- Brief language (German or English)

**Output:**
- Structured design brief: Room(s), Style Preference, Budget, Timeline, Constraints, Additional Notes
- Editable text area for designer review
- Optional: a ready-to-use image-generation prompt (via a second button), built from the extracted brief

**MVP scope note:** The mood board concept itself (an actual generated image) is **not implemented** in this MVP — GPT-4o-mini is a text model and does not generate images. What the MVP delivers instead is a **professional, ready-to-use text prompt** that a designer can pair with a photo of the client's room inside an external image generator (e.g. Google Gemini / Nano Banana) to produce the visual concept. Photo upload is not required by the MVP — it happens downstream, in the image generator itself, once the prompt is copied over. This keeps the MVP scoped to what GPT-4o-mini can actually do, while still proving the full UC3 concept end-to-end (notes → brief → image-ready prompt).

**System prompt constraints:**
- Extraction: uses ONLY information present in the notes; missing fields marked "Not specified," never guessed
- Image prompt: single, ready-to-use paragraph (80–120 words), respects budget tier and constraints, instructs the image generator to preserve room architecture

## Features

### UC1 — Property Listing Generator

**Input fields:**
- Property type (apartment, house, office, penthouse, loft)
- District / neighbourhood
- Size (m²), rooms, floor
- Energy class (A+ to H)
- Asking price (€)
- Features (comma-separated, e.g. Balkon, Einbauküche)
- Target audience (general, young professionals, families, seniors, investors)
- Neighbourhood notes (optional)

**Output:**
- AI-generated German sales listing (150–200 words)
- Editable text area for agent review
- "Approve & Copy" button for final text

**System prompt constraints:**
- Uses ONLY provided data — never fabricates amenities or neighbourhood details
- Structured format: headline, lifestyle paragraph, key facts, neighbourhood note, CTA
- Mentions energy class naturally
- Professional but warm tone

### UC2 — Client Enquiry Triage

**Input:**
- Customer enquiry text (paste from email or contact form)
- Response language (German or English)

**Output:**
- Classification: Viewing Request / Pricing Question / General Information / Complaint / Interior Design Enquiry / Other
- Urgency: High / Medium / Low
- Draft response (80–120 words) for agent review

**System prompt constraints:**
- Never commits to anything — always frames as "we will get back to you"
- Professional but warm tone matching RaumKraft brand
- Agent finalises before sending

## LangSmith Monitoring

Every AI call is automatically traced to LangSmith with:
- Full input prompt
- Full output text
- Response duration
- Token count (input + output)
- API cost per request

This is the transparency layer for CEO Chleo — proof that AI is not a black box. Traces are viewable at https://smith.langchain.com under the `raumkraft-mvp` project.

## Limitations vs Production

| Aspect | MVP | Production |
|---|---|---|
| Data input | Manual form entry | CRM/database integration |
| Enquiry source | Copy-paste text | Email/API webhook auto-ingestion |
| Publishing | Copy text manually | Direct CMS/portal integration |
| Authentication | None | Role-based access (agent, manager, admin) |
| Storage | No history saved | Database for all generated listings and triage decisions |
| Multi-language | German only (UC1), German/English (UC2) | Full multi-language support |
| Batch processing | One at a time | Bulk listing generation |
| Error handling | Basic (missing field warnings) | Comprehensive error handling, retry logic, fallback models |
| Scalability | Single user, local | Cloud-deployed, multi-user, load-balanced |

## Cost per Request

Using GPT-4o-mini pricing:
- UC1 listing generation: ~€0.001–0.002 per listing (short input, ~200 word output)
- UC2 enquiry triage: ~€0.001 per enquiry (short input, ~120 word output)

At 200 listings/month + 1,200 enquiries/month = estimated **€1.40–2.60/month** in API costs.
