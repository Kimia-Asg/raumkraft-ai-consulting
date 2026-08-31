# Capstone Round 1 — AI Consulting Pitch for RaumKraft Immobilien & Design

## Author: Kimia Asgari

## Scenario

**Client:** Chleo, CEO of **RaumKraft Immobilien & Design**
**Sector:** Real Estate / Interior Design
**Company Size:** Medium (≈150 employees across 4 regional offices in Germany)

RaumKraft is a mid-sized German company combining real estate brokerage with in-house interior design services. They handle residential sales, commercial leasing, and turnkey interior design for new-build apartments and office renovations. Chleo is skeptical about AI — concerned it lacks transparency and won't integrate with their existing workflows.

## What This Repository Contains

| Folder | Contents |
|---|---|
| `research/` | Sector analysis, opportunity/risk mapping, 3 use case proposals |
| `dashboard/` | Tableau dashboard file (.twbx) + documentation with screenshots |
| `n8n/` | Proof-of-concept automation workflow + docs |
| `langsmith/` | Monitoring setup, dataset, and transparency evidence |
| `cost_estimation/` | Cost analysis and implementation timeline |
| `feedback/` | Round 1 decision (stop / continue / pivot) |
| `presentation/` | Slide deck used for class presentation |
| `data/` | Public/synthetic datasets used across deliverables |

## How to Navigate

1. **Start with the research pack** (`research/`) to understand the sector context and proposed use cases
2. **View the dashboard** — open `dashboard/dashboard.twbx` in Tableau Desktop or Tableau Public (see `dashboard_documentation.md` for screenshots and metric rationale)
3. **Explore the POC** — import `n8n/workflow.json` into n8n (see `n8n/workflow_documentation.md` for setup)
4. **Check monitoring** — see `langsmith/` for observability evidence
5. **Review costs** — `cost_estimation/` contains the financial and timeline estimates

## Setup

```bash
# If using any Python data-prep scripts
pip install -r requirements.txt

# Copy and fill environment variables
cp .env.example .env
```

## Tech Stack

- **Tableau Public / Desktop** — stakeholder dashboard
- **n8n** (cloud) — automation proof of concept
- **LangSmith** — LLM observability and monitoring
- **Python + pandas** — data preparation
- **OpenAI API** — LLM integration in POC


