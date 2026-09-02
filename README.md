# 🏠 RaumKraft AI Assistant — AI Consulting Capstone

**AI Consulting & Integration Bootcamp — Ironhack (2026)**
**Consultant:** Kimia Asgari

## Project Overview

RaumKraft Immobilien & Design is a fictional ~150-employee Hamburg-based firm combining real estate brokerage with in-house interior design. This project delivers an AI consulting engagement across two rounds — from research and POC to a working MVP with full compliance documentation.

**CEO Chleo's concern:** *"AI is not transparent."*
**Our answer:** Every AI interaction is traced in LangSmith. No black box.

### 🔗 Live MVP: [raumkraft-ai-consulting.onrender.com](https://raumkraft-ai-consulting.onrender.com)

## Three AI Use Cases

| # | Use Case | Type | Status |
|---|---|---|---|
| UC1 | **Property Listing Generator** — structured data → AI draft → agent reviews → publish | Primary | ✅ Working MVP |
| UC2 | **Client Enquiry Triage** — auto-classify + draft response → agent approves → send | Secondary | ✅ Working MVP |
| UC3 | **Design Brief Generator** — meeting notes → structured brief → per-room prompts → Gemini room analysis → design concept | Future | ✅ Working MVP |

## Tech Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| LLM (UC1, UC2, UC3 brief) | OpenAI GPT-4o-mini via LangChain |
| Vision AI (UC3 design concept) | Google Gemini 3.6 Flash |
| Monitoring | LangSmith (traces + cost tracking) |
| Deployment | Render (free tier) |
| Data | Kaggle — Germany Housing Rent & Price (ImmobilienScout24) |

## Repo Structure

```
raumkraft-ai-consulting/
├── README.md                          ← You are here
├── feedback/
│   └── round1_decision.md             ← Round 1 presentation feedback + KEEP decision
├── research/                          ← Round 1: sector research, opportunities/risks, use cases
├── data/                              ← Kaggle real data (Germany Housing) + synthetic data
├── dashboard/                         ← Round 1: Tableau dashboards + screenshots
├── n8n/                               ← Round 1: n8n POC workflow + screenshots
├── langsmith/                         ← Round 1: LangSmith traces + screenshots
├── cost_estimation/                   ← Round 1: cost and timeline estimates
├── presentation/                      ← Presentation slides
├── poc/
│   ├── poc_documentation.md           ← POC documentation (Round 1 → Round 2 evolution)
│   └── poc_workflow.json              ← n8n workflow export
├── MVP/
│   ├── app.py                         ← Streamlit app (UC1 + UC2 + UC3)
│   ├── requirements.txt               ← Python dependencies
│   ├── .env.example                   ← Template for API keys
│   └── mvp_documentation.md           ← MVP documentation
├── compliance/
│   ├── eu_ai_act_compliance.md        ← EU AI Act risk classification + conformity assessment
│   └── gdpr_documentation.md          ← GDPR data flows, DPIA, data subject rights
├── use_case_definition.md             ← Use case definition (Round 1 → Round 2 evolution)
├── roi_risk_assessment.md             ← ROI (275% at 12 months) + 9-risk matrix
├── strategic_plan.md                  ← POC → Pilot → Full Deployment → Scale
└── run_langsmith_demo.py              ← Round 1: LangSmith trace demo script
```

## How to Run the MVP Locally

```bash
cd MVP
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys (OpenAI, LangSmith, Gemini)
streamlit run app.py
```

See `MVP/mvp_documentation.md` for full setup instructions.

## Key Numbers

| Metric | Value |
|---|---|
| Upfront cost | €15,000 |
| Monthly running cost | ~€400 |
| Annual value | €74,256 |
| 12-month ROI | 275% |
| 36-month ROI | 658% |
| Break-even | Month 3 |
| EU AI Act classification | Limited Risk |

## Round 1 → Round 2 Evolution

| Aspect | Round 1 | Round 2 |
|---|---|---|
| Use cases | UC1 only (POC) | UC1 + UC2 + UC3 (working MVP) |
| Interface | n8n webhook (no UI) | Streamlit web app (deployed on Render) |
| Data | Synthetic | Real (Kaggle - ImmobilienScout24) |
| Monitoring | LangSmith traces (no cost) | LangSmith with per-request cost tracking |
| Documentation | Research pack + cost estimation | Full consulting package (ROI, compliance, strategy) |

## License

This is a student capstone project for educational purposes.
