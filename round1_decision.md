# Round 1 Decision — RaumKraft Immobilien & Design

**Date:** 2026-09-01  
**Presenter:** Kimia Asgari  
**Reviewer:** Tejal 

---

## Decision: KEEP

Industry, company, and primary use case hold up. No change needed. Expand scope for Round 2 by building UC2 as a second working capability alongside UC1.

---

## What Feedback Was Most Repeated?

1. **UC1 alone is too simple to justify the capstone.** Listing generation (structured input → LLM → polished text) is technically a 15–20 minute task. It does not reflect the depth of nine weeks of learning. UC2 must also be built.
2. **The mood board / design brief generator (UC3) would be a standout addition.** Tejal strongly encouraged this because it connects my interior design background with the bootcamp's AI skills — a unique differentiator.
3. **Real data over synthetic data.** Synthetic data is acceptable for Round 1, but for Round 2 and portfolio credibility, finding real open-source datasets (Kaggle, Hugging Face) is strongly recommended. Column mapping can be handled with a small script; dashboards do not need to be rebuilt.
4. **Add API cost tracking to LangSmith traces.** Showing per-request cost alongside input/output in LangSmith strengthens the transparency story for Chleo.

## Is the Industry / Use Case Still Worth Deepening?

Yes. The sector, company profile, and transparency framing all landed well. The core issue is scope depth, not direction. Expanding from one use case to two (or three) solves this.

## What Changed Between Round 1 and Round 2?

| Area | Round 1 | Round 2 |
|------|---------|---------|
| UC1 — Listing Generation | n8n POC + LangSmith traces | Streamlit MVP (functional app) |
| UC2 — Inquiry Triage | Proposed only | Must build as working capability |
| UC3 — Design Mood Board | Not in scope | Nice-to-have; strongly encouraged by TA |
| Data | Synthetic (500 properties, 1200 enquiries) | Search for real datasets; replace CSVs if found |
| LangSmith | 5 traces, no cost tracking | Add per-request API cost to traces |

## Which Round 2 Docs Are Highest Risk?

- **EU AI Act compliance** — need to work through classification reasoning carefully
- **GDPR documentation** — data flow mapping and DPIA for the highest-risk processing
- **Working MVP** — must actually run; scope to what is achievable in one day

## What Is the Smallest MVP That Still Proves the Use Case?

A Streamlit app with two tabs:

1. **Listing Generator (UC1):** Input property details → generate German listing via OpenAI → display for agent review
2. **Inquiry Classifier (UC2):** Paste or input a customer enquiry → AI classifies type + drafts a response → agent reviews

Optional third tab for UC3 (mood board) if time allows.

## Decision Gate Checklist

- [x] Feedback captured
- [x] Industry / use case decision: **KEEP**
- [x] Highest-risk Round 2 docs identified
- [x] Smallest viable MVP scoped
- [x] No rewrite of Round 1 research needed
