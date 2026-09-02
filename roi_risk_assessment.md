# ROI & Risk Assessment — RaumKraft AI Assistant

## 1. Cost Overview

### Upfront Costs (POC + Pilot Phase)

| Item | Cost | Notes |
|---|---|---|
| AI Consulting (discovery + POC) | €10,000 | 11-week engagement |
| Streamlit MVP development | €3,000 | UC1 + UC2 build, testing, deployment |
| LangSmith setup + monitoring | €500 | Configuration, dashboards, team training |
| CRM integration scoping | €1,500 | Technical assessment for production integration |
| **Total upfront** | **€15,000** | |

### Ongoing Monthly Costs (Production)

| Item | Monthly cost | Notes |
|---|---|---|
| OpenAI API (GPT-4o-mini) | €50–80 | ~200 listings + ~1,200 enquiry triages/month |
| LangSmith monitoring | €39 | Plus plan for team access |
| Cloud hosting (Streamlit Cloud or equivalent) | €50–100 | Dedicated instance for RaumKraft |
| Maintenance & support | €200 | Bug fixes, prompt tuning, updates |
| **Total monthly** | **€339–419** | Rounded: ~€400/month |

### Ongoing Annual Cost

| | Low estimate | High estimate |
|---|---|---|
| Annual running cost | €4,068 | €5,028 |
| Rounded | **~€4,100/year** | **~€5,000/year** |

## 2. Quantified Business Value

### UC1 — Listing Generation

| Metric | Current | With AI | Savings |
|---|---|---|---|
| Time per listing | 30–45 min | 5–10 min (review + edit) | ~25–35 min/listing |
| Listings per month | 200 | 200 | — |
| Hours saved per month | — | — | **83–117 hrs/month** |
| Hours saved per year | — | — | **~1,000–1,400 hrs/year** |
| Time to publish | 11 days avg | 3–5 days (estimated) | 6–8 days faster |

**Value calculation (UC1):**
- Average agent salary: ~€50,000/year → ~€26/hour (incl. overhead)
- Hours saved: ~1,200 hrs/year (midpoint)
- **Annual value UC1: ~€31,200/year**

### UC2 — Enquiry Triage

| Metric | Current | With AI | Savings |
|---|---|---|---|
| Response time | 5–7 hours avg | Under 2 hours (target) | 3–5 hrs faster |
| Routine enquiries (auto-draftable) | 69% of 1,200/month = 828 | AI drafts, agent approves | — |
| Time per enquiry (manual) | 10–15 min | 2–3 min (review draft) | ~10 min/enquiry |
| Hours saved per month | — | — | **~138 hrs/month** |
| Hours saved per year | — | — | **~1,656 hrs/year** |

**Value calculation (UC2):**
- Hours saved: ~1,656 hrs/year
- At €26/hour
- **Annual value UC2: ~€43,056/year**

### Combined Business Value

| | Annual |
|---|---|
| UC1 — Listing generation | €31,200 |
| UC2 — Enquiry triage | €43,056 |
| **Total direct value** | **€74,256/year** |

### Indirect Value (not quantified but expected)

- Faster response times → higher conversion rates on enquiries
- Consistent listing quality → stronger brand perception
- Agent satisfaction → reduced turnover (agents focus on high-value tasks instead of repetitive writing)
- Faster time-to-publish → properties sell faster, less inventory carrying cost

## 3. ROI Calculation

**Formula:** `ROI = (Net Benefit / Total Cost) × 100`

### 12-Month ROI

| Item | Amount |
|---|---|
| Total value (12 months) | €74,256 |
| Upfront cost | €15,000 |
| Running cost (12 months) | €4,800 (€400 × 12) |
| **Total cost** | **€19,800** |
| **Net benefit** | **€54,456** |
| **ROI (12 months)** | **275%** |

### 36-Month ROI

| Item | Amount |
|---|---|
| Total value (36 months) | €222,768 |
| Upfront cost | €15,000 |
| Running cost (36 months) | €14,400 (€400 × 36) |
| **Total cost** | **€29,400** |
| **Net benefit** | **€193,368** |
| **ROI (36 months)** | **658%** |

### Break-Even

- Monthly net benefit: €74,256 / 12 = €6,188
- Monthly running cost: €400
- Monthly net gain: €5,788
- Months to recover upfront cost: €15,000 / €5,788 = **~2.6 months**
- **Break-even: Month 3 of production deployment**

## 4. Assumptions

| # | Assumption | Basis |
|---|---|---|
| 1 | 200 listings/month remains stable | Based on RaumKraft's current output and 2-year revenue trend |
| 2 | 1,200 enquiries/month remains stable | Based on current intake across all channels |
| 3 | 69% of enquiries are routine and auto-draftable | Based on dashboard analysis of enquiry categories |
| 4 | Agent salary ~€50,000/year fully loaded | German market benchmark for mid-level real estate agents |
| 5 | AI reduces listing time by 25–35 min per listing | Based on MVP testing — generation takes <30 seconds, agent review ~5–10 min |
| 6 | AI reduces enquiry handling by ~10 min per routine enquiry | Based on MVP testing — classification + draft in <10 seconds, agent review ~2–3 min |
| 7 | GPT-4o-mini pricing remains stable | Based on current OpenAI pricing; historically AI costs decrease over time |
| 8 | Agent adoption reaches 70%+ within pilot | Mitigated by volunteer-first pilot and training programme |

**Note:** These estimates are based on MVP testing and industry benchmarks. Actual ROI would be validated during the pilot phase with real RaumKraft data and agent feedback.

## 5. Risk Matrix

| # | Risk | Category | Likelihood (1–5) | Impact (1–5) | Risk Score | Mitigation |
|---|---|---|---|---|---|---|
| 1 | **AI hallucination** — model invents property features, amenities, or neighbourhood details not in input | Technical | 2 | 5 | 10 | System prompt explicitly forbids fabrication; structured input limits the model; agent review catches errors before publishing; LangSmith traces flag anomalies |
| 2 | **GDPR non-compliance** — personal data in enquiries processed without proper legal basis or safeguards | Regulatory | 3 | 5 | 15 | EU-based API endpoints; data processing agreement with OpenAI; no personal data stored beyond session; DPIA completed (see `gdpr_documentation.md`) |
| 3 | **Staff resistance** — agents refuse to adopt AI tool, undermining ROI | Operational | 3 | 4 | 12 | Pilot with volunteer agents first; frame AI as assistant not replacement; training programme; gather feedback and iterate; demonstrate time savings with real metrics |
| 4 | **API cost escalation** — OpenAI raises prices or usage exceeds projections | Technical | 2 | 3 | 6 | Monthly cost cap in API settings; per-request cost tracking in LangSmith; model fallback strategy (switch to cheaper model if costs rise); current cost is <€80/month — large margin before concern |
| 5 | **EU AI Act misclassification** — system classified as minimal risk but regulator determines otherwise | Regulatory | 2 | 4 | 8 | Conservative classification approach; human-in-the-loop on all outputs; no automated decision-making; documentation prepared for Limited Risk obligations as precaution (see `eu_ai_act_compliance.md`) |
| 6 | **Output quality degradation** — model updates from OpenAI change output quality without notice | Technical | 3 | 3 | 9 | Pin model version (gpt-4o-mini); LangSmith evaluation dataset to benchmark quality after updates; prompt regression tests; human review catches quality drops |
| 7 | **Vendor lock-in** — dependency on OpenAI as sole LLM provider | Operational | 2 | 3 | 6 | LangChain abstraction layer allows model swapping; evaluate alternatives quarterly (Anthropic Claude, Google Gemini, open-source models); no proprietary fine-tuning in MVP phase |
| 8 | **Data leakage** — sensitive property or client data exposed through API calls | Ethical | 2 | 5 | 10 | OpenAI data processing terms (no training on API data); EU endpoints; no personally identifiable data in UC1 prompts; UC2 anonymisation layer before API call in production |

### Risk Heat Map Summary

| | Low Impact (1–2) | Medium Impact (3) | High Impact (4–5) |
|---|---|---|---|
| **High Likelihood (4–5)** | — | — | — |
| **Medium Likelihood (3)** | — | Output quality degradation (9) | GDPR non-compliance (15), Staff resistance (12) |
| **Low Likelihood (1–2)** | — | API cost escalation (6), Vendor lock-in (6) | AI hallucination (10), EU AI Act misclassification (8), Data leakage (10) |

**Overall risk posture:** Manageable. The two highest risks (GDPR and staff resistance) both have clear, actionable mitigations. No risks are in the high-likelihood / high-impact quadrant.
