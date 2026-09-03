# Project Management Addendum — RaumKraft AI Assistant

*Prepared as supplementary material for the IHK "KI-Manager (IHK)" certification (Projektarbeit). This addendum applies project management frameworks to the RaumKraft AI Assistant capstone project.*

---

## 1. Stacey Matrix — Classifying This Project's Complexity

### What the Stacey Matrix is

The Stacey Matrix (developed by Ralph Douglas Stacey) is a decision-making framework used to determine the right project management approach based on two dimensions:

- **Y-axis — Requirements/Agreement:** How clear and agreed-upon are the requirements? (Unclear at top, Clear at bottom)
- **X-axis — Technology/Certainty:** How well-understood and proven is the technology or method? (Unproven/Novel on the left, Proven/Established on the right)

These two axes create **four zones**, each calling for a different management approach:

| Zone | Requirements | Technology | Recommended Approach |
|---|---|---|---|
| **Simple** | Clear | Proven | Traditional/Waterfall — use checklists, best practices |
| **Complicated** | Clear | Some unknowns | Expert analysis, specialist input, still largely plannable |
| **Complex** | Unclear | Unproven | Agile — iterate, experiment, adapt as you learn |
| **Chaotic** | Unclear | Unproven, no cause-effect known | Rapid experimentation, act first, sense-make after |

The core insight: **projects near the origin (high agreement, high certainty) can be planned in detail up front. Projects far from the origin need iteration, not planning.** Using a waterfall approach on a complex project wastes effort on plans that will be wrong; using heavy agile ceremony on a simple project wastes effort on process.

### Classifying each use case

| Use Case | Requirements Clarity | Technology Certainty | Zone | Why |
|---|---|---|---|---|
| **UC1 — Listing Generator** | High — Chleo and agents agreed on the exact output format (headline, lifestyle paragraph, key facts, CTA) from Round 1 | High — GPT-4o-mini text generation via LangChain is a proven, well-documented pattern | **Simple → Complicated** | The "what" was clear from Round 1 feedback. The "how" (prompt engineering) needed some iteration to get tone and factual-accuracy right, but the core technology (LLM text generation) is mature and predictable |
| **UC2 — Enquiry Triage** | High — classification categories and urgency levels were defined upfront | High — text classification + generation is a standard LLM pattern | **Simple → Complicated** | Same pattern as UC1. Main uncertainty was prompt tuning for tone (never overpromise to the customer) |
| **UC3 — Design Brief + Mood Board** | Medium-Low — the mood board concept evolved significantly during development (single photo → per-room photos → text concept vs. image generation) based on iterative feedback from Isabella and Tejal | Low — this required discovering, through trial and error, that Gemini image generation is geo-restricted in Germany, that model names change between API versions, and that a workaround (vision + text concept) was needed | **Complex** | Neither the requirements nor the technology were settled at the start. The final design (per-room prompts + Gemini vision analysis) only emerged through experimentation |

### Why this matters for the project's management approach

This classification is not just theoretical — it explains **why an agile, iterative approach was the right choice** for this project, and validates the decision-making process used throughout:

- **UC1 and UC2** could be built in focused, short work sessions with minimal rework — consistent with their "Simple/Complicated" classification.
- **UC3** genuinely required an agile approach: build a first version → get it in front of a mentor (Isabella) → get concrete feedback → pivot the whole interaction model (single mood board → per-room workflow) → hit a technical wall (Gemini geo-restriction) → adapt again (text concept instead of image). A waterfall plan written on Day 1 for UC3 would have been wrong by Day 2.

This is a textbook illustration of the Stacey Matrix's core teaching: **match your process to the level of uncertainty, not the other way around.**

---

## 2. Sprint Breakdown

The project was executed as a series of short, focused sprints rather than a single long build phase. Each sprint had a clear goal and ended with a working, demonstrable increment — consistent with agile practice for the Complex-zone work (UC3) and efficient for the Complicated-zone work (UC1, UC2).

| Sprint | Duration | Goal | Key Deliverables | Zone (Stacey) |
|---|---|---|---|---|
| **Sprint 0 — Round 1 Foundation** | 3 weeks (pre-capstone) | Validate the AI capability and get staff sign-off on direction | Research pack, synthetic data, Tableau dashboards, n8n POC, LangSmith traces, cost estimate, Round 1 presentation | Simple/Complicated |
| **Sprint 1 — Decision & Scoping** | 1 day | Process Round 1 feedback, decide KEEP vs. CHANGE, scope Round 2 | `round1_decision.md`, Round 2 requirements breakdown | Simple |
| **Sprint 2 — Core MVP (UC1 + UC2)** | 1 day | Working Streamlit app with listing generation and enquiry triage | `app.py` (UC1 + UC2 tabs), `requirements.txt`, `.env.example`, initial `mvp_documentation.md` | Complicated |
| **Sprint 3 — Documentation Package** | 1 day | Complete the required consulting deliverables in parallel with development | `use_case_definition.md`, `roi_risk_assessment.md`, `eu_ai_act_compliance.md`, `gdpr_documentation.md`, `strategic_plan.md` | Simple/Complicated |
| **Sprint 4 — UC3 Discovery** | 0.5 day | Build first version of design brief extraction | Basic UC3 tab: meeting notes → structured brief | Complex |
| **Sprint 5 — UC3 Mentor Feedback & Pivot** | 0.5 day | Incorporate mentor consultation feedback | Redesigned UC3 flow: per-room prompt generation instead of single combined prompt | Complex |
| **Sprint 6 — UC3 Image Generation Attempt** | 0.5 day | Attempt to integrate real image generation | Discovered Gemini model deprecations (3 model name changes) and Germany geo-restriction | Complex → Chaotic (briefly) |
| **Sprint 7 — UC3 Adapted Solution** | 0.5 day | Pivot to a working, honest solution given the constraint | Gemini vision + text design concept per room; documented obstacle transparently | Complex |
| **Sprint 8 — Deployment** | 0.5 day | Get the MVP publicly accessible, not just localhost | Live deployment on Render, environment variables configured, auto-deploy via GitHub | Complicated |
| **Sprint 9 — Documentation Alignment** | 0.5 day | Ensure all docs reflect what was actually built (not what was planned) | Updated `gdpr_documentation.md`, `eu_ai_act_compliance.md`, `use_case_definition.md`, `poc_documentation.md`, `README.md` | Simple |
| **Sprint 10 — Presentation & Delivery** | 1 day | Package everything for the final pitch | Presentation deck, demo recording, rehearsal | Simple |

**Total: ~7 working days across two rounds**, reflecting a realistic compressed capstone timeline rather than the 7-month production roadmap described in `strategic_plan.md` (which covers the *client-facing* deployment plan, not the *development* timeline).

### What the sprint structure demonstrates

- **Retrospective-driven pivots:** Sprint 5 and Sprint 7 exist because real feedback (from Isabella, from API errors) changed the plan. This is the agile principle of "respond to change over following a plan" in action.
- **Working software over comprehensive documentation — but not at its expense:** MVP functionality was prioritized (Sprints 2, 4-7) while documentation ran in parallel (Sprint 3, 9) rather than being deferred to the end, avoiding a last-minute documentation crunch.
- **Timeboxing under real constraints:** With a hard deadline (Thursday presentation), each sprint was deliberately scoped small enough to finish and produce something demoable, rather than large and open-ended.

---

## 3. Use Case Priority Matrix

Before Round 2 development began, the three use cases were evaluated against two dimensions: **business impact** and **implementation effort** — a standard prioritization technique for deciding what to build first when time is constrained.

```
High Impact
    │
    │        UC2                    UC1
    │    (Enquiry Triage)      (Listing Generator)
    │    Quick win — build       Quick win — build
    │    first                   first
    │
    │        UC3
    │    (Design Brief +
    │     Mood Board)
    │    Major project —
    │    build with care
    │
    └─────────────────────────────────────────────
      Low Effort                      High Effort
```

| Use Case | Business Impact | Implementation Effort | Priority | Rationale |
|---|---|---|---|---|
| **UC1** | High — €31,200/year value; addresses the most time-consuming daily task | Low — single LLM call, well-defined output format | **1st (Quick Win)** | Highest value-to-effort ratio; also the use case Round 1 staff feedback said was "too simple alone," making it the natural anchor to build on |
| **UC2** | High — €43,056/year value; largest volume (1,200 enquiries/month, 69% routine) | Low-Medium — classification + generation, similar pattern to UC1 | **2nd (Quick Win)** | Second-highest value; Round 1 feedback explicitly required this be built, not just proposed |
| **UC3** | Medium (long-term) — €0 quantified in current ROI model (future value), but highest **strategic differentiation** value (connects consultant's design background, most likely to impress evaluators) | High — required discovering and working around external API constraints, multi-model integration, more complex UI (per-room state management) | **3rd (Major Project)** | Correctly sequenced last — it needed the most iteration and carried the most technical risk. Building it last meant UC1/UC2 were already secured as a safety net if UC3 ran over budget on time |

### Why this sequencing was correct in hindsight

The priority matrix predicted, correctly, that UC3 would be the highest-risk item — and it was: three model deprecation errors, a geo-restriction discovery, and a full UX redesign (single mood board → per-room workflow) all happened during UC3 development. Because UC1 and UC2 were secured first, this risk never threatened the overall deliverable — even if UC3 had been cut entirely, the project would still have met the Round 1 requirement that "UC1 alone is too simple; UC2 must also be built."

---

## 4. Process Model — Implementation Approach

This section documents the recurring process used across sprints, particularly for the Complex-zone UC3 work, as a lightweight, repeatable model:

```
1. BUILD    → Ship the smallest working version of the feature
2. DEMO     → Show it to a real stakeholder (mentor, TA) or test it live
3. LISTEN   → Capture concrete feedback (not assumptions about what they'll want)
4. DIAGNOSE → When something breaks (API error, wrong output), read the actual
              error message before guessing at a fix
5. ADAPT    → Change the approach — sometimes the UX, sometimes the technical
              architecture — based on what was learned
6. DOCUMENT → Update the relevant docs (use case, GDPR, risk) to reflect
              what was actually built, not what was originally planned
7. REPEAT   → Return to step 1 for the next increment
```

This loop was applied explicitly in UC3 development:
- Build (basic brief extraction) → Demo (to Isabella) → Listen ("prompts should be per-room, generated one by one") → Adapt (redesigned to per-room loop) → Document.
- Build (Gemini image generation) → Diagnose (404 model errors, three times) → Adapt (updated model name each time) → Diagnose (geo-restriction error) → Adapt (pivoted to vision + text concept) → Document (added an "Obstacles" section to `mvp_documentation.md` and a new risk entry to `roi_risk_assessment.md`).

---

## 5. Summary — Frameworks Applied

| Framework | Purpose | Where Applied |
|---|---|---|
| Stacey Matrix | Classify project/use-case complexity to justify management approach | Section 1 — shows why UC1/UC2 could be planned but UC3 needed iteration |
| Sprint-based delivery | Break work into short, demoable increments | Section 2 — 11 sprints across Round 1 + Round 2 |
| Impact/Effort Priority Matrix | Sequence use cases by value and risk | Section 3 — justified building UC1 → UC2 → UC3 in that order |
| Build-Demo-Listen-Adapt loop | Lightweight process model for uncertain (Complex-zone) work | Section 4 — applied twice during UC3 development |

This addendum demonstrates that the RaumKraft AI Assistant project was not built ad hoc, but followed a deliberate — if lightweight and startup-appropriate — project management discipline, matched to the genuine uncertainty of each work package.
