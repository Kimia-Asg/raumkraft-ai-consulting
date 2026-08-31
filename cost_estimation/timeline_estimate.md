# Implementation Timeline — RaumKraft AI Integration

## Overview

This timeline covers the path from Chleo's initial meeting to a production-ready first use case. It is structured in decision-gated phases — RaumKraft commits to one phase at a time.

## Phase Overview

```
Discovery (2 weeks) → POC Build (3 weeks) → Pilot (4 weeks) → Production (2 weeks) → Ongoing
                    ↓ GATE                 ↓ GATE            ↓ GATE
                  Go / No-Go            Expand / Adjust    Full rollout decision
```

**Total to production-ready UC1:** ~11 weeks (~3 months)

## Detailed Timeline

### Phase 0: Discovery & Alignment (Weeks 1–2)
| Week | Activity | Output |
|---|---|---|
| 1 | Stakeholder interviews (Chleo, head of sales, lead designer, office manager) | Needs assessment document |
| 1 | Data audit — what systems exist, what data is available | Data landscape map |
| 2 | Workflow mapping — current listing creation process end-to-end | Process documentation + bottleneck analysis |
| 2 | Confirm use case scope and success criteria | Signed-off scope document |

**Gate:** RaumKraft reviews findings and decides whether to proceed with POC build.

### Phase 1: POC Build (Weeks 3–5)
| Week | Activity | Output |
|---|---|---|
| 3 | Set up n8n environment; connect to test data | Working n8n instance |
| 3 | Prompt engineering — develop and test listing generation prompt | Prompt v1 + evaluation results |
| 4 | Build full workflow (trigger → format → LLM → review → output) | Working POC workflow |
| 4 | Set up LangSmith monitoring and evaluation dataset | Monitoring dashboard |
| 5 | Internal demo to project team; iterate on feedback | POC demo recording + revision notes |

**Gate:** Demo POC to Chleo + key stakeholders. Decision: proceed to pilot or adjust scope.

### Phase 2: Pilot (Weeks 6–9)
| Week | Activity | Output |
|---|---|---|
| 6 | Select 5 volunteer agents; train on workflow and review process | Training materials; pilot group ready |
| 6–8 | Pilot runs — agents use AI-assisted listings alongside normal process | Usage data, quality metrics |
| 7 | Mid-pilot check-in — review LangSmith data, agent feedback | Interim report |
| 9 | Pilot evaluation — time saved, quality scores, agent satisfaction | Pilot results report |

**Gate:** Review pilot results. Decision: expand to full team, adjust, or pause.

### Phase 3: Production Rollout (Weeks 10–11)
| Week | Activity | Output |
|---|---|---|
| 10 | Harden workflow — error handling, CRM integration, agent UI | Production-ready workflow |
| 10 | GDPR documentation — data processing records, DPA with API provider | Compliance docs |
| 11 | Full team training; launch monitoring alerts | Training delivery; go-live |
| 11 | Handoff documentation for internal team or ongoing support | Operations manual |

### Post-Launch: Ongoing (Month 4+)
- Monthly LangSmith review (quality drift, cost tracking)
- Quarterly prompt refinement based on agent feedback
- Evaluate readiness for Use Case 2 (communication triage)
- If UC1 + UC2 stable: scope Use Case 3 (design brief generator)

## Assumptions Behind This Timeline

| Assumption | If different, impact on timeline |
|---|---|
| RaumKraft has a CRM with structured property data | If not: add 1–2 weeks for data structuring |
| Stakeholders are available for interviews in Week 1 | If not: Discovery stretches to 3 weeks |
| 5 agents volunteer for pilot without resistance | If not: change management work adds 1 week |
| No custom ML models needed (LLM API is sufficient) | If custom model needed: add 4–8 weeks |
| GDPR compliance is straightforward (no special categories of data) | If complex data flows: add 1–2 weeks for DPIA |

## Resource Requirements from RaumKraft

| Role | Time commitment | Phase |
|---|---|---|
| Chleo (CEO) | 2 hours for kickoff; 1 hour per gate review | All |
| Head of Sales | 3–4 hours total for interviews + pilot oversight | Discovery + Pilot |
| IT / Admin | 4–6 hours for CRM access, API setup | POC + Production |
| 5 Pilot agents | ~2 hours training + normal workflow during pilot | Pilot |
| Lead interior designer | 2 hours for UC3 scoping (if continuing) | Discovery |
