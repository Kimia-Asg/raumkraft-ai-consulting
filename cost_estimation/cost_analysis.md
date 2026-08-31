# Cost Analysis — AI Implementation for RaumKraft

## Assumptions

| Assumption | Value | Basis |
|---|---|---|
| Company size | ~150 employees | Scenario definition |
| Active agents | ~50 | Estimated from company size |
| Listings per month | ~200 | ~4 per agent per month |
| Enquiries per week | ~200 | Mid-range for regional firm |
| Interior design projects per month | ~8–12 | Based on team size (~20 designers) |
| LLM model for POC | GPT-4o-mini | Cost-efficient for structured generation |
| LLM model for production | GPT-4o or Claude Sonnet | Higher quality for client-facing text |
| n8n hosting | Cloud (free/starter tier for POC; Team tier for production) | Standard SaaS pricing |
| LangSmith | Free tier for POC; Plus for production | Standard SaaS pricing |
| Consultant rate | €1,200/day | Market rate for junior AI consultant in Germany |

## Upfront Costs (POC Phase — Month 1–2)

| Item | Cost | Notes |
|---|---|---|
| **Consulting time** (setup, research, configuration) | €12,000–15,000 | 10–12 days of consulting |
| **n8n Cloud** (Starter) | €0–20/month | Free tier covers POC volume |
| **LLM API costs** (POC testing) | €5–20 | Minimal during development |
| **LangSmith** (free tier) | €0 | Sufficient for POC |
| **Tableau Public** (free) or Desktop licence | €0 | Free tier sufficient for POC dashboards |
| **Total POC phase** | **~€12,000–15,000** | Primarily consulting time |

## Production Costs (Monthly, Post-Pilot)

### Use Case 1: Listing Generation

| Item | Monthly cost | Calculation |
|---|---|---|
| LLM API (GPT-4o-mini) | €5–10 | 200 listings × ~700 tokens × $0.15/1M input + $0.60/1M output |
| LLM API (GPT-4o, if upgraded) | €20–40 | Same volume, higher per-token cost |
| n8n Cloud (Team) | €50–100 | Depending on execution volume |
| **Subtotal UC1** | **€55–150/month** | |

### Use Case 2: Communication Triage

| Item | Monthly cost | Calculation |
|---|---|---|
| LLM API (classification + drafting) | €15–30 | ~800 enquiries/month × ~500 tokens avg |
| Additional n8n executions | Included in Team tier | |
| **Subtotal UC2** | **€15–30/month** | |

### Use Case 3: Design Brief Generator (if implemented)

| Item | Monthly cost | Calculation |
|---|---|---|
| LLM API (longer context — meeting notes to brief) | €10–25 | ~10 projects × ~2,000 tokens avg |
| **Subtotal UC3** | **€10–25/month** | |

### Monitoring and Infrastructure

| Item | Monthly cost |
|---|---|
| LangSmith Plus | €39/month |
| n8n Team tier | €50–100/month |
| Tableau (Public: free / Creator: €70/user/month) | €0–140/month |
| **Subtotal infra** | **€89–279/month** |

### Total Monthly Production Cost

| Scenario | Monthly cost |
|---|---|
| UC1 only | ~€160–310 |
| UC1 + UC2 | ~€175–340 |
| UC1 + UC2 + UC3 | ~€185–365 |

## Value Estimation (Conservative)

| Value driver | Estimated monthly value | Basis |
|---|---|---|
| Agent time saved on listings (200 listings × 30 min saved) | ~€8,000–12,000 | 100 hours saved × €80–120/hr fully loaded agent cost |
| Faster response time → improved lead conversion | ~€5,000–15,000 | Even a 5% improvement on conversion from faster responses |
| Designer time saved on briefs | ~€2,000–4,000 | 10 projects × 2 hrs saved × €100–200/hr designer cost |
| **Conservative total monthly value** | **€15,000–31,000** | |

## ROI Summary (Simplified)

| Metric | Value |
|---|---|
| Upfront investment | ~€12,000–15,000 |
| Monthly cost | ~€175–365 |
| Monthly value (conservative) | ~€15,000–31,000 |
| Payback period | **~1 month** after go-live |
| 12-month ROI | **~50x–100x** on running costs |

**Caveat:** These are estimates for a consulting-conversation level pitch. A real engagement would validate time-savings assumptions with actual RaumKraft workflow data during the pilot phase. The ROI is deliberately framed conservatively — I would rather under-promise.

## Cost Risks

| Risk | Mitigation |
|---|---|
| API cost spikes from unexpected volume | Set hard monthly budget caps; use cheaper models for classification tasks |
| n8n pricing changes | Evaluate self-hosted option as backup |
| LLM quality degrades after model update | LangSmith monitoring detects drift; versioned prompts allow rollback |
| Scope creep during implementation | Fixed-scope phases with decision gates (mirrors our POC → Pilot → Deploy plan) |
