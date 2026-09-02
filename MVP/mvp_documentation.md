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
| LLM (UC1, UC2, UC3 brief) | OpenAI GPT-4o-mini (via LangChain) | Low cost per request, fast response, sufficient quality for text generation |
| Vision AI (UC3 design concept) | Google Gemini 3.6 Flash | Free tier, vision capability (analyzes room photos), generates design concepts |
| LLM Framework | LangChain (`langchain-openai`) | Automatic token counting and cost tracking in LangSmith |
| Monitoring | LangSmith | Full trace of every AI call — input, output, duration, cost |
| Deployment | Render (free tier) | Cloud hosting with auto-deploy from GitHub |
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

### UC3 — Design Brief Generator + Mood Board Concept

**Workflow:**
1. Designer pastes meeting notes from client consultation
2. AI extracts a structured design brief (rooms, style, budget, timeline, constraints)
3. AI detects which rooms need redesigning and generates a **per-room image-generation prompt**
4. Designer uploads a photo of each room
5. **Google Gemini** analyzes the room photo + brief and produces a **professional text-based design concept** (color palette, furniture, materials, layout recommendations)
6. The generated prompt + design concept serve as the foundation for the designer to create the mood board and prepare the design document

**Output per room:**
- Tailored image-generation prompt (ready to copy into Nano Banana or similar tool)
- AI-generated design concept based on actual room photo analysis (color palette, furniture recommendations, materials, constraints addressed)

**Obstacles encountered during development:**

1. **Google Gemini image generation is not available in Germany via API.** Gemini's image generation feature is geo-restricted and does not support Germany at this time. As a result, the MVP uses Gemini's **vision + text** capability instead — Gemini sees the room photo, analyzes it, and produces a detailed text-based design concept. In production, image generation could be enabled via a server in a supported region, or by using an alternative provider.

2. **OpenAI DALL-E is too expensive for this use case.** OpenAI charges ~$0.04–0.08 per image, which at scale (multiple rooms per client, multiple clients per month) would significantly impact running costs. This does not align with RaumKraft's cost-conscious approach.

3. **Chosen approach:** Instead of generating images directly, the MVP produces professional, ready-to-use prompts that designers can copy into **Nano Banana** or any external image generator. Combined with Gemini's text-based design concept (which analyzes the actual room photo), the designer has everything needed to create the mood board and prepare the design document. This is a practical, cost-effective solution that keeps the designer in creative control.

**Tech stack for UC3:**
- GPT-4o-mini: brief extraction + prompt generation
- Google Gemini 3.6 Flash: room photo analysis + design concept generation

**System prompt constraints:**
- Extraction: uses ONLY information present in the notes; missing fields marked "Not specified," never guessed
- Per-room prompts: tailored to each room's specific requirements from the brief
- Design concept: references what Gemini actually sees in the uploaded photo

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
| Multi-language | German only (UC1), German/English (UC2, UC3) | Full multi-language support |
| Batch processing | One at a time | Bulk listing generation |
| Image generation (UC3) | Text-based design concept + prompt for external tool (Gemini image gen unavailable in Germany; DALL-E too expensive) | Dedicated image generation via Nano Banana API or Gemini from supported region |
| Error handling | Basic (missing field warnings) | Comprehensive error handling, retry logic, fallback models |
| Scalability | Single user, local + Render deployment | Cloud-deployed, multi-user, load-balanced |

## Cost per Request

Using GPT-4o-mini pricing:
- UC1 listing generation: ~€0.001–0.002 per listing (short input, ~200 word output)
- UC2 enquiry triage: ~€0.001 per enquiry (short input, ~120 word output)
- UC3 brief extraction + prompt generation: ~€0.002–0.004 per session (two GPT calls: brief + per-room prompts)
- UC3 design concept (Gemini): Free tier — Google Gemini 3.6 Flash (15 req/min free)

At 200 listings/month + 1,200 enquiries/month + 23 design projects/month = estimated **€2–4/month** in API costs.
