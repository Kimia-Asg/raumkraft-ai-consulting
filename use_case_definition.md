# Use Case Definition — RaumKraft Immobilien & Design

## 1. Business Problem Statement

RaumKraft Immobilien & Design is a mid-sized German firm combining real estate brokerage with in-house interior design services. The company faces three operational bottlenecks:

1. **Slow listing production:** Agents spend 30–45 minutes writing each property **sales** listing manually. With ~200 listings per month, the average time from data entry to publication is 11 days — creating delays that cost competitive advantage in a fast-moving sales market.

2. **Slow enquiry response:** The company receives 1,200+ enquiries per month across email and contact forms. Average response time is 5–7 hours, far above the internal target of 2 hours. 69% of these enquiries are routine (viewing requests, pricing questions) and follow predictable patterns.

3. **Unstructured design handoffs:** Interior design consultations produce meeting notes that must be manually converted into structured briefs. This process takes significant time and introduces inconsistencies, with ~240 hours per year spent on this task alone.

CEO Chleo's primary concern: **"AI is not transparent."** Any solution must demonstrate full observability — no black boxes.

## 2. Company Profile

| Attribute | Detail |
|---|---|
| Company name | RaumKraft Immobilien & Design (fictional) |
| Industry | Real Estate / Interior Design |
| Size | ~150 employees across 4 regional offices in Germany |
| Headquarters | Hamburg, Germany |
| Revenue (2-year estimate) | Brokerage €7.5M · Interior Design €3.2M · Property Management €1.3M |
| Current listings | ~200/month |
| Monthly enquiries | ~1,200 |
| Active design projects | ~23 |

## 3. Proposed AI Solutions

### UC1 — Property Listing Generator (PRIMARY)

**Type:** Natural language generation (NLG)

**Flow:** Structured property data (size, rooms, location, energy class, features, asking price) → LLM generates a polished German **sales** listing (headline, lifestyle paragraph, key facts, neighbourhood note, CTA, 150–200 words) → agent reviews and edits in the app → publish.

**AI model:** GPT-4o-mini via OpenAI API

**Key constraint:** The system uses ONLY the data provided. It never fabricates amenities, transport connections, or neighbourhood details. This directly addresses Chleo's transparency concern.

### UC2 — Client Enquiry Triage (SECONDARY)

**Type:** Text classification + response generation

**Flow:** Incoming enquiry (email, contact form) → AI classifies by type (viewing request, pricing question, general info, complaint, interior design enquiry) and urgency (high/medium/low) → AI drafts a response → human agent reviews and approves before sending.

**AI model:** GPT-4o-mini via OpenAI API

**Key constraint:** AI never sends anything autonomously. Every draft response requires human approval.

### UC3 — Interior Design Brief Generator + Mood Board Concept (BUILT)

**Type:** Text extraction + structuring (GPT-4o-mini); vision-based design concept generation (Google Gemini 3.6 Flash)

**Flow:**
1. Meeting notes from client consultation pasted into the app
2. AI extracts and structures a formal design brief (room, style, budget, constraints, timeline)
3. AI detects which rooms need redesigning and generates a **tailored image-generation prompt per room**
4. Designer uploads a photo of each room
5. Google Gemini analyzes the room photo + brief → produces a **professional text-based design concept** (color palette, furniture, materials, layout recommendations)
6. The prompt + design concept serve as the designer's foundation to create the mood board and design document

**Obstacles encountered:**
1. **Google Gemini image generation unavailable in Germany via API** — geo-restricted. MVP uses Gemini's vision + text capability instead (analyzes room photo, returns detailed design concept). Production: route via supported region.
2. **OpenAI DALL-E too expensive** (~€0.04–0.08/image) at scale.
3. **Chosen approach:** Per-room professional text prompts + Gemini design concept. Designer can copy prompt into Nano Banana or any external image generator for visual mood board.

## 4. Key Stakeholders and Interests

| Stakeholder | Role | Primary interest |
|---|---|---|
| Chleo (CEO) | Decision-maker | ROI, transparency, brand reputation |
| Real estate agents | End users (UC1, UC2) | Time savings, ease of use, output quality |
| Interior designers | End users (UC3) | Brief accuracy, creative relevance |
| IT / Operations | Technical oversight | Integration, maintenance, security |
| Legal / Compliance | Risk oversight | GDPR compliance, EU AI Act classification |
| Clients (buyers, tenants) | Indirect beneficiaries | Faster responses, quality listings |

## 5. Success Criteria

| Metric | Target | Measurement method |
|---|---|---|
| Listing creation time | Reduce from 30–45 min to under 10 min per listing | Time tracking before/after pilot |
| Time to publish | Reduce from 11 days average to under 5 days | CRM data comparison |
| Enquiry response time | Reduce from 5–7 hours to under 2 hours | Helpdesk/email timestamp analysis |
| Agent adoption rate | ≥70% of agents using the tool weekly by end of pilot | Usage analytics from the app |
| Output quality | ≥85% of generated listings published with minor or no edits | Agent feedback tracking |
| Transparency satisfaction | Chleo and management confirm LangSmith traces meet their expectations | Stakeholder interview at pilot review |

## 6. Out-of-Scope Boundaries

- **No autonomous publishing:** AI never publishes a listing or sends a response without human approval.
- **No personal data processing in the MVP:** The MVP uses structured property data and anonymised enquiry text only. Production deployment requires full GDPR implementation (see `gdpr_documentation.md`).
- **No AI image generation in MVP:** Google Gemini image generation is geo-restricted in Germany. OpenAI DALL-E is too expensive at scale. UC3 produces text-based design concepts and professional prompts that designers can use with external image generators (Nano Banana, etc.).
- **No CRM integration in MVP:** The MVP is a standalone Streamlit app. Production would integrate with RaumKraft's existing CRM and email systems.
- **No multi-language support:** Listings are generated in German only. Multi-language support is a potential future feature.
- **No real-time learning:** The system does not learn from agent edits in the MVP phase. Fine-tuning based on feedback is a production consideration.

## 7. Evolution from Round 1 to Round 2

| Aspect | Round 1 | Round 2 |
|---|---|---|
| Industry/use case | **KEEP** — same sector, same use cases, expanded scope |
| UC1 delivery | n8n POC workflow + LangSmith traces | Working Streamlit MVP with editable output |
| UC2 delivery | Proposed only (data generated, not built) | Working Streamlit MVP with classification + draft response |
| UC3 delivery | Proposed as future phase | Built: brief extraction + per-room prompts + Gemini room analysis + design concept. Image gen blocked in Germany — text concept + exportable prompts as workaround |
| Data | Synthetic datasets | Real data from Kaggle: [Germany Housing - Rent and Price](https://www.kaggle.com/phanindraparashar/germany-housing-rent-and-price-data-set-apr-20) — German real estate sale and rental data with property characteristics (size, rooms, price, location). Sale listings used for UC1 to match RaumKraft's brokerage focus |
| Monitoring | LangSmith traces (5 runs, no cost tracking) | LangSmith with automatic per-request API cost tracking via LangChain — shows Chleo exact cost of each AI interaction for full financial transparency |
| Documentation | Research pack + cost estimation | Full consulting package (ROI, EU AI Act, GDPR, strategy) |

**Decision rationale:** After the Round 1 presentation to teaching staff, the TA confirmed the industry and use cases hold up. Key feedback incorporated into Round 2:

1. **UC1 alone is technically too simple** (~15–20 min task) to justify the capstone — UC2 must also be built as a working capability.
2. **UC3 mood board extension was strongly encouraged** as it connects the consultant's interior design background with AI skills learned in the bootcamp.
3. **Real data should replace synthetic data** for portfolio credibility — recruiters may question why open-source data was not used. The Kaggle ImmobilienScout24 dataset was selected as a replacement.
4. **LangSmith cost tracking** should be added to show Chleo per-request API costs alongside input/output traces.

See `feedback/round1_decision.md` for full feedback details.
