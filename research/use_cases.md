# Use Case Proposals — RaumKraft Immobilien & Design

## Use Case 1: AI-Assisted Property Listing Generation

### Problem
RaumKraft agents spend 30–45 minutes per listing writing descriptions, often resulting in inconsistent quality and tone. High-performing agents write compelling copy; others produce generic text. International clients need English or Turkish translations that are currently outsourced or skipped.

### Proposed Solution
An n8n workflow triggered when an agent enters structured property data (square meters, rooms, location, features, energy class) into the CRM or a simple form. The workflow:
1. Sends structured data to an LLM with a brand-tone system prompt
2. Generates a German listing draft + optional English translation
3. Routes the draft to the agent for review and approval before publishing
4. Logs the interaction to LangSmith for monitoring

### Why It Fits a Medium Company
- 150 employees means ~40–60 agents producing listings regularly
- At 30 min saved per listing × ~200 listings/month = significant capacity recovery
- No ML infrastructure needed — LLM API + n8n + human review
- Directly visible to Chleo as ROI: faster time-to-market for listings

### Stakeholders
- Agents (daily users)
- Marketing team (brand consistency)
- Chleo / management (cost and quality oversight)

### Success Criteria
- Time-to-publish reduced by ≥40%
- Agent satisfaction with draft quality ≥ 4/5 in pilot survey
- Zero unapproved AI-generated listings published (human-in-the-loop maintained)
- All LLM interactions logged and viewable in LangSmith

### Risks
- Hallucinated property features → structured input fields prevent free-form fabrication
- Inconsistent tone → system prompt engineering + few-shot examples from best-performing listings
- Agent pushback → pilot with 5 volunteer agents, not company-wide mandate

---

## Use Case 2: Client Communication Triage and Auto-Drafting

### Problem
RaumKraft receives 150–300 inbound enquiries per week across email, contact forms, and WhatsApp. Response time averages 8–12 hours; industry benchmark for lead conversion is <2 hours. Many enquiries are repetitive (availability checks, viewing requests, basic pricing questions).

### Proposed Solution
An n8n workflow that:
1. Monitors incoming enquiries (email inbox or form webhook)
2. Classifies the enquiry type (viewing request / pricing / availability / design consultation / other)
3. For routine types: drafts a personalised response using property data from the CRM
4. Routes draft to the assigned agent for one-click send or edit
5. Flags complex/sensitive enquiries for manual handling (e.g., complaints, legal questions)
6. Logs classification accuracy and response drafts to LangSmith

### Why It Fits a Medium Company
- Volume is high enough to justify automation but not so high that a dedicated call centre exists
- Agents wear multiple hats — freeing them from triage lets them focus on viewings and closings
- WhatsApp/email integration via n8n is straightforward
- Classification + drafting is a well-understood LLM task with high accuracy on structured categories

### Stakeholders
- Agents (primary beneficiaries)
- Office managers (queue visibility)
- Clients (faster response)

### Success Criteria
- Average first-response time reduced to <2 hours for routine enquiries
- Classification accuracy ≥ 85% (measured via LangSmith evaluation)
- Agent override rate tracked — if agents rewrite >50% of drafts, prompt tuning needed
- No auto-sent messages — all drafts require human approval

### Risks
- Misclassification of sensitive enquiries → conservative routing: anything uncertain goes to human
- Client discomfort if they suspect they're talking to a bot → drafts sent from agent's account, with human review; no chatbot-style interaction
- GDPR: client email content processed by LLM → use pseudonymisation pipeline; EU-hosted endpoints preferred

---

## Use Case 3: Interior Design Brief Generator

### Problem
When a RaumKraft interior design project kicks off, designers spend 2–4 hours per project converting initial client conversations (often unstructured phone calls or site meetings) into structured design briefs. These briefs cover style preferences, room functions, material preferences, budget range, and timeline. Quality varies by designer experience.

### Proposed Solution
A workflow where:
1. The designer records brief notes or voice memo highlights from the client meeting
2. The notes are processed by an LLM with a structured brief template
3. The AI generates a formatted design brief with: style direction, spatial requirements, material suggestions, budget allocation draft, and open questions for the client
4. The designer reviews, refines, and shares with the client for confirmation

### Why It Fits a Medium Company
- RaumKraft's differentiator is integrated real estate + design — this use case strengthens that value proposition
- Designers are expensive resources; reducing admin time per project increases design capacity
- Structured briefs improve project handoffs between designers and project managers
- This is a "wow factor" use case for Chleo — it touches the company's unique offering

### Stakeholders
- Interior designers (daily users)
- Project managers (handoff recipients)
- Clients (receive clearer briefs, faster)

### Success Criteria
- Brief generation time reduced from 2–4 hours to <30 minutes (including review)
- Client brief approval rate (first-pass) ≥ 70%
- Designer satisfaction ≥ 4/5

### Risks
- AI lacks spatial reasoning — it can structure text but not evaluate whether a 3m × 4m kitchen can fit an island → designer review is essential
- Style vocabulary mismatches — "modern" means different things to different clients → structured style taxonomy in the prompt
- This use case is harder to demo with synthetic data — consider a mock client scenario for the POC

### Round 1 vs Round 2
- **Round 1:** Present the concept + workflow diagram; light demo with synthetic meeting notes
- **Round 2 (if continuing):** Build a working prototype with voice-to-brief pipeline; deeper evaluation

---

## Use Case Comparison Summary

| Dimension | UC1: Listing Generation | UC2: Communication Triage | UC3: Design Brief Generator |
|---|---|---|---|
| Business impact | High (core revenue) | High (lead conversion) | Medium–High (differentiator) |
| Implementation effort | Low | Low–Medium | Medium |
| Data sensitivity | Low (property data) | Medium (client PII in emails) | Low–Medium (preferences) |
| Demo-ability in POC | ⭐ Easy | ⭐ Easy | Moderate |
| Transparency story | Strong (clear input→output) | Strong (classification visible) | Moderate |
| Recommended for Round 1 POC | ✅ Primary | ✅ Secondary | 📋 Concept + diagram |
