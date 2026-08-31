# Opportunities and Risks — AI for RaumKraft Immobilien & Design

## Opportunity Map

### High-Impact Opportunities

| # | Opportunity | Business value | Effort | Priority |
|---|---|---|---|---|
| 1 | **Automated property listing drafts** | Saves agent time (est. 30–45 min per listing); consistent quality and tone; multilingual output for international clients | Low–Medium | ⭐ High |
| 2 | **Client communication triage and follow-up** | Reduces response time; prevents leads from going cold; frees agents from repetitive email/WhatsApp replies | Low | ⭐ High |
| 3 | **Interior design brief generator** | Converts initial client conversations into structured design briefs; reduces designer onboarding time per project | Medium | ⭐ High |
| 4 | **Property market micro-analytics** | Dashboard-level insights on pricing trends, time-on-market, comparable properties for agents and clients | Medium | Medium |
| 5 | **Energy efficiency data extraction** | Auto-parse energy certificates to enrich listings and compliance reporting | Medium | Medium |
| 6 | **Design style matching** | Match client aesthetic preferences to past RaumKraft projects or material catalogues | High | Lower (Round 2 / MVP stretch) |

### Why These Fit a Medium-Sized Firm

- **Budget-conscious:** Use cases 1–3 require API calls + no-code automation, not custom ML infrastructure
- **Team-sized impact:** 150 employees means even small per-person time savings scale meaningfully
- **Low technical barrier:** n8n + LLM API is deployable without hiring ML engineers
- **Incremental adoption:** Each use case is standalone; Chleo doesn't have to commit to "full AI transformation"

## Risk Assessment

### Risk Matrix

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **Hallucinated property details** (wrong sq. meters, incorrect price, fabricated features) | Medium–High | High (legal liability, client trust) | Human-in-the-loop review before publishing; structured prompts with explicit data fields; LangSmith monitoring for output validation |
| **GDPR violation** (client data sent to US-based LLM providers without proper DPA) | Medium | High (fines up to 4% of annual turnover) | Use EU-hosted API endpoints where available; data processing agreements; anonymise/pseudonymise client data before LLM processing |
| **Staff resistance** ("AI is replacing us") | High | Medium (adoption failure) | Frame AI as assistant, not replacement; involve team in pilot; show time-saved metrics, not headcount-reduction language |
| **Over-reliance / de-skilling** | Medium | Medium | Maintain human review for all client-facing outputs; training on when to override AI suggestions |
| **Vendor lock-in** to a single LLM provider | Medium | Medium | Abstract LLM calls behind a simple API layer; monitor costs per provider; test alternatives periodically |
| **Cost overrun** if API usage scales unexpectedly | Low–Medium | Medium | Set usage caps and alerts; estimate per-listing and per-communication costs upfront; monitor via LangSmith |
| **Low-quality outputs for design briefs** (AI doesn't understand spatial/aesthetic nuance) | Medium | Low–Medium | Use structured templates + human designer review; AI drafts the brief, designer refines |
| **EU AI Act classification uncertainty** | Low | Medium | Most use cases here are likely minimal/limited risk; document classification reasoning early; reassess if use case scope changes |

### Risks Specific to Chleo's Concern (Transparency)

Chleo's core fear is that AI is a "black box." The risks above map directly to this concern:

1. **"What did the AI actually write?"** → LangSmith traces show every prompt and response
2. **"Can we trust the output?"** → Human-in-the-loop + structured validation
3. **"Where does our data go?"** → Data flow documentation + GDPR compliance path
4. **"How much will this cost us?"** → Token-level cost monitoring via LangSmith + upfront estimates
5. **"What if it breaks?"** → Monitoring dashboards with alerts; no AI system runs autonomously without review

## Summary: Risk-Adjusted Priority

For the Round 1 pitch, the recommended lead use case is **Use Case 1 (Automated Listing Drafts)** supported by **Use Case 2 (Client Communication Triage)**. These have the best ratio of business value to risk, and they directly address Chleo's transparency concerns because:
- Outputs are text (easy to review)
- The workflow is linear (easy to monitor in LangSmith)
- They touch the core revenue activity (brokerage) so impact is immediately visible
- They don't require access to sensitive personal data beyond what's already in the CRM

Use Case 3 (Design Brief Generator) is the differentiator for Round 2 / a deeper engagement.
