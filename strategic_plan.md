# Strategic Deployment & Commercialisation Plan — RaumKraft AI Assistant

## 1. Deployment Phases

### Phase 1: POC (Weeks 1–3) ✅ COMPLETED

**Objective:** Prove that AI can generate quality German property listings from structured data.

| Item | Detail |
|---|---|
| Scope | UC1 only — listing generation |
| Tool | n8n workflow + OpenAI GPT-4o-mini |
| Data | Synthetic property data (500 listings) |
| Monitoring | LangSmith traces (5 runs + evaluation dataset) |
| Team | AI consultant (Kimia) + RaumKraft project sponsor (Chleo) |
| Outcome | AI generates accurate, structured listings in under 5 seconds. No fabrication when prompted correctly. Cost per listing: fraction of a cent |

**Gate decision:** ✅ POC successful → proceed to MVP/Pilot

### Phase 2: MVP + Pilot (Weeks 4–11)

**Objective:** Deploy a working app with UC1 + UC2 to a small group of agents. Validate time savings, quality, and adoption with real workflows.

| Item | Detail |
|---|---|
| Scope | UC1 (listing generation) + UC2 (enquiry triage) |
| Tool | Streamlit app + LangChain + OpenAI GPT-4o-mini + LangSmith |
| Data | Real property data (Kaggle Germany Housing dataset) + live enquiries (pilot group) |
| Duration | 8 weeks (4 weeks build + 4 weeks pilot) |
| Pilot group | 5–8 volunteer agents from one regional office (Hamburg) |
| Monitoring | LangSmith with full cost tracking, weekly quality review |

**Pilot success criteria (must meet ALL to proceed):**

| Metric | Target |
|---|---|
| Listing creation time | Reduced to under 10 minutes (from 30–45 min) |
| Enquiry response time | Under 2 hours for routine enquiries (from 5–7 hours) |
| Agent adoption | ≥70% of pilot agents using the tool daily by week 4 |
| Output quality | ≥85% of listings published with minor or no edits |
| Agent satisfaction | NPS ≥ 30 among pilot agents |
| Error rate | <5% of outputs require major corrections |
| Cost per month | Within projected €400/month budget |

**Gate decision:** Review pilot results with Chleo and management. If criteria met → proceed to full deployment. If partially met → extend pilot 4 more weeks. If not met → reassess approach.

### Phase 3: Full Deployment (Weeks 12–18)

**Objective:** Roll out to all agents across all 4 regional offices. Integrate with existing CRM and email systems.

| Item | Detail |
|---|---|
| Scope | UC1 + UC2 company-wide; UC3 (design brief generator) development begins |
| Users | All ~50 agents across 4 offices |
| Integration | CRM integration for property data auto-fill; email system integration for enquiry auto-ingestion |
| Infrastructure | Cloud deployment (EU-hosted), role-based access control |
| Training | 2-hour training session per office + video tutorial + support channel |
| Monitoring | LangSmith dashboards for management; weekly quality reports |

**Milestones:**

| Week | Milestone |
|---|---|
| 12 | Infrastructure setup + CRM integration scoping |
| 13–14 | CRM integration development + testing |
| 15 | Office-by-office rollout begins (Hamburg first, then others) |
| 16–17 | Remaining offices onboarded + training completed |
| 18 | Full deployment complete; UC3 development kickoff |

### Phase 4: Scale (Weeks 19–30, optional)

**Objective:** Add UC3 (design brief generator + mood board), explore commercialisation, and expand capabilities.

| Item | Detail |
|---|---|
| UC3 deployment | Design brief generator for interior design team |
| Mood board extension | Generative AI for decoration/furniture concepts (nice-to-have) |
| Advanced features | Batch listing generation, multi-language support, analytics dashboard |
| Commercialisation | Explore licensing to other German real estate firms |

## 2. Timeline Overview

```
Week 1–3      │ POC ✅
Week 4–7      │ MVP Build
Week 8–11     │ Pilot (Hamburg office, 5–8 agents)
              │ ─── GATE DECISION ───
Week 12–18    │ Full Deployment (all 4 offices)
Week 19–24    │ UC3 Development + Deployment
Week 25–30    │ Scale + Commercialisation Exploration
```

**Total: ~7 months from POC to full scale**

## 3. Go-to-Market Strategy

### Internal Deployment (Phase 2–3)

| Element | Detail |
|---|---|
| Buyer | Chleo (CEO) — budget holder and decision-maker |
| Champion | Pilot agents who experience time savings firsthand |
| Channel | Internal rollout: pilot → phased office-by-office deployment |
| Pricing | Internal cost centre — no licensing fee. Cost: ~€15k upfront + ~€400/month |
| Differentiator | Transparency-first approach: LangSmith traces prove AI is not a black box. Human-in-the-loop on every output. Built specifically for German real estate market |

### External Commercialisation (Phase 4)

| Element | Detail |
|---|---|
| Target market | Mid-sized German real estate firms (50–300 employees) combining brokerage with services |
| Buyer persona | CEO/COO concerned about AI transparency and operational efficiency |
| Channel | Direct sales via industry events (IVD network, Expo Real); referral from RaumKraft case study |
| Pricing model | SaaS subscription: €500–1,500/month based on listing volume and number of users |
| Differentiator | German-language AI built for the German real estate market; transparency-first (LangSmith); proven ROI at RaumKraft (275% in 12 months); GDPR and EU AI Act compliant |
| Competitive advantage | Most AI writing tools are generic and English-first. RaumKraft AI Assistant is built specifically for German property listings with market-specific structure and compliance |

## 4. Stakeholder Communication Plan

| Stakeholder | Frequency | Format | Content |
|---|---|---|---|
| Chleo (CEO) | Bi-weekly during pilot; monthly after deployment | 30-min meeting + 1-page summary | ROI progress, adoption metrics, risk updates, key decisions needed |
| Agents (pilot group) | Weekly during pilot | Slack channel + 15-min standup | Feature updates, tips, feedback collection, issue resolution |
| Agents (all) | At rollout; monthly after | Training session + email newsletter | How to use the tool, best practices, success stories from pilot |
| IT / Operations | Weekly during build; bi-weekly after | Technical standup | Integration progress, infrastructure, security, uptime |
| Legal / Compliance | Monthly | Email report | GDPR compliance status, EU AI Act updates, data processing review |
| Interior Design Team | When UC3 begins | Workshop + demo | UC3 scope, how AI assists (not replaces) their workflow |

## 5. KPIs per Phase

### Phase 2: Pilot KPIs

| KPI | Target | Measurement |
|---|---|---|
| Time to generate listing | <10 min (including review) | App analytics + agent self-report |
| Enquiry response time | <2 hours | Email timestamp comparison |
| Agent adoption rate | ≥70% daily use | App usage logs |
| Listing quality score | ≥85% published with minor/no edits | Agent feedback form |
| Cost per listing | <€0.01 | LangSmith cost tracking |
| Agent satisfaction (NPS) | ≥30 | Survey at week 4 and week 8 |

### Phase 3: Full Deployment KPIs

| KPI | Target | Measurement |
|---|---|---|
| Company-wide adoption | ≥80% of agents using weekly | App usage logs |
| Average listing time | <8 min company-wide | App analytics |
| Enquiry response time | <2 hours across all offices | CRM data |
| Monthly API cost | <€400 | LangSmith + OpenAI dashboard |
| ROI (cumulative) | On track for 275% at 12 months | Finance team quarterly review |
| Customer satisfaction | No decline in client NPS | Client survey comparison |

### Phase 4: Scale KPIs

| KPI | Target | Measurement |
|---|---|---|
| UC3 adoption | ≥60% of designers using weekly | App usage logs |
| External pilot customers | 2–3 firms in paid pilot | Sales pipeline |
| MRR from external sales | €1,000–4,500/month | Revenue tracking |
| Listing quality consistency | Cross-office variance <10% | Quality audit |

## 6. Commercialisation Model

### Short-term (internal)

| Model | Detail |
|---|---|
| Type | Internal productivity tool |
| Revenue impact | Indirect — time savings (€74k/year) reinvested in higher-value activities |
| Cost structure | €15k upfront + €400/month operational |
| Owner | RaumKraft IT / Operations |

### Long-term (external, Phase 4)

| Model | Detail |
|---|---|
| Type | B2B SaaS |
| Target | German real estate firms, 50–300 employees |
| Pricing tiers | Starter (€500/mo, 1 office, UC1 only) · Professional (€1,000/mo, multi-office, UC1+UC2) · Enterprise (€1,500/mo, all UCs + custom integrations) |
| Revenue potential | 10 customers × €1,000/mo average = €120,000/year |
| Go-to-market cost | €20–30k (sales hire, marketing, industry events) |
| Break-even (external) | ~6 months after first customer |
| Moat | German-market-specific training prompts; compliance documentation; proven case study from RaumKraft deployment |

### Risks to Commercialisation

| Risk | Mitigation |
|---|---|
| Competitors launch similar tools | Move fast; build German-market expertise moat; lock in early customers |
| OpenAI pricing changes | LangChain abstraction enables model switching; evaluate open-source alternatives |
| RaumKraft decides not to commercialise | The internal tool still delivers 275% ROI — commercialisation is upside, not the core value |
