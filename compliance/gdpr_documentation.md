# GDPR Documentation — RaumKraft AI Assistant

## 1. Data Flow Map

### UC1 — Property Listing Generator

```
Property Database (structured data)
        │
        ▼
┌─────────────────────┐
│  Streamlit App      │  Agent enters property details
│  (RaumKraft server) │  (no personal data)
└─────────┬───────────┘
          │ API call (HTTPS, encrypted)
          ▼
┌─────────────────────┐
│  OpenAI API         │  Generates German listing
│  (EU endpoint)      │  No personal data processed
└─────────┬───────────┘
          │ Response
          ▼
┌─────────────────────┐
│  Streamlit App      │  Agent reviews and edits
└─────────┬───────────┘
          │ Trace logged
          ▼
┌─────────────────────┐
│  LangSmith          │  Input, output, cost tracked
│  (US-hosted)        │  No personal data in traces
└─────────────────────┘
```

**GDPR exposure: LOW** — UC1 processes structured property data only (size, rooms, price, location). No personal data is involved at any stage.

### UC2 — Client Enquiry Triage

```
Customer Enquiry (email / contact form)
        │
        │  ⚠️ May contain personal data:
        │  name, email, phone, address
        ▼
┌─────────────────────┐
│  Streamlit App      │  Agent pastes enquiry text
│  (RaumKraft server) │
└─────────┬───────────┘
          │ API call (HTTPS, encrypted)
          │ ⚠️ Personal data may be sent to OpenAI
          ▼
┌─────────────────────┐
│  OpenAI API         │  Classifies + drafts response
│  (EU endpoint)      │  Data not used for training
└─────────┬───────────┘  (API terms: zero data retention)
          │ Response
          ▼
┌─────────────────────┐
│  Streamlit App      │  Agent reviews draft
└─────────┬───────────┘
          │ Trace logged
          ▼
┌─────────────────────┐
│  LangSmith          │  ⚠️ Trace may contain
│  (US-hosted)        │  personal data from enquiry
└─────────────────────┘
```

**GDPR exposure: MEDIUM** — Customer enquiries may contain personal data (name, email, phone number, address). This data flows through OpenAI and is logged in LangSmith.

### UC3 — Design Brief Generator + Mood Board (Built)

**Core function:** Meeting notes → structured design brief

```
Meeting Notes (text from client consultation)
        │
        ▼
┌─────────────────────┐
│  Streamlit App      │  Designer pastes meeting notes
│  (RaumKraft server) │
└─────────┬───────────┘
          │ API call (HTTPS, encrypted)
          ▼
┌─────────────────────┐
│  OpenAI API         │  Extracts and structures brief
│  (EU endpoint)      │  (room, style, budget, timeline)
└─────────┬───────────┘
          │ Response
          ▼
┌─────────────────────┐
│  Streamlit App      │  Designer reviews and refines
└─────────────────────┘
```

**Built: Per-room prompt generation + Gemini design concept**

```
Structured Brief (rooms detected)
        │
        ▼
┌─────────────────────┐
│  OpenAI API          │  Generates tailored image
│  (EU endpoint)       │  prompt per detected room
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  Streamlit App       │  Designer uploads photo
│                      │  of each specific room
└─────────┬───────────┘
          │ API call (HTTPS, encrypted)
          ▼
┌─────────────────────┐
│  Google Gemini API   │  Analyzes room photo + brief
│  (3.6 Flash, US)     │  → text-based design concept
└─────────┬───────────┘  (image generation unavailable
          │              in Germany — see note below)
          ▼
┌─────────────────────┐
│  Streamlit App       │  Designer reviews concept +
│                      │  uses prompt with external
│                      │  image generator (Nano Banana)
└─────────────────────┘
```

**Note on Gemini processing:** Google Gemini's image generation API is not available in Germany. The MVP uses Gemini's vision + text capability instead — the room photo is sent to Gemini (US-hosted), analyzed, and a text-based design concept is returned. No image is generated or stored by Gemini in this flow.

**GDPR exposure: MEDIUM** — Meeting notes may contain client names and personal preferences. Room photos may incidentally contain personal items. Design briefs reference client-specific details.

## 2. Processing Activities Register

| # | Processing Activity | Data Categories | Data Subjects | Purpose | Legal Basis (Art. 6) | Retention | Recipients |
|---|---|---|---|---|---|---|---|
| 1 | Property listing generation (UC1) | Property data (address, size, price, features) | None (no personal data) | Generate marketing content for property sales | Art. 6(1)(f) — Legitimate interest | Session only — not stored after generation | OpenAI (processor), LangSmith (sub-processor) |
| 2 | Enquiry classification and draft response (UC2) | Customer name, email, phone, address, enquiry content | Prospective buyers, tenants, clients | Classify and respond to customer enquiries efficiently | Art. 6(1)(f) — Legitimate interest in efficient customer service | Session only in MVP; production: per retention policy (max 30 days in AI system) | OpenAI (processor), LangSmith (sub-processor) |
| 3 | AI interaction monitoring (LangSmith) | Input prompts, output text, metadata (tokens, cost, duration) | Indirectly: customers whose enquiry data appears in traces | Transparency, quality assurance, cost tracking | Art. 6(1)(f) — Legitimate interest in system oversight | 90 days (configurable) | LangSmith / LangChain Inc. (processor, US-based) |
| 4 | Design brief generation + mood board concept (UC3) | Meeting notes (may contain client name, preferences), room photos, design preferences | Interior design clients | Extract structured brief; generate per-room image prompts; analyze room photo to produce text-based design concept | Art. 6(1)(b) — Performance of contract (design service) | Session only; briefs and concepts retained if client approves | OpenAI (processor for brief extraction and prompts), Google (processor for Gemini room photo analysis, US-based) |

## 3. Data Protection Impact Assessment (DPIA) — UC2 Enquiry Triage

### 3.1 Why a DPIA?

UC2 is the highest-risk processing activity because:
- Customer enquiries contain personal data (names, contact details, sometimes financial information like budget)
- Data is sent to a third-party AI provider (OpenAI) via API
- Data is logged in a US-hosted monitoring service (LangSmith)
- Processing is systematic — 1,200 enquiries per month, 69% processed by AI

Under GDPR Article 35, a DPIA is required when processing is likely to result in high risk to data subjects' rights and freedoms.

### 3.2 Description of Processing

| Aspect | Detail |
|---|---|
| What data | Customer name, email, phone number, property preferences, enquiry text |
| How many data subjects | ~828 per month (69% of 1,200 enquiries) |
| Purpose | Classify enquiry type, assess urgency, draft response for agent review |
| Technology | OpenAI GPT-4o-mini via API, monitored via LangSmith |
| Decision-making | No automated decisions — AI drafts, human agent reviews and sends |

### 3.3 Necessity and Proportionality

| Question | Assessment |
|---|---|
| Is processing necessary for the purpose? | Yes — manual classification of 1,200 enquiries/month is unsustainable with current staffing |
| Is the data minimised? | Partially — enquiry text is sent in full. Production should implement anonymisation layer to strip unnecessary personal details before API call |
| Is there a less intrusive alternative? | Rule-based classification (no AI) is less intrusive but significantly less accurate for nuanced enquiries |
| Are data subjects informed? | In production: yes, via privacy policy update. MVP phase: internal testing only |

### 3.4 Risk Assessment

| Risk | Likelihood | Severity | Mitigation |
|---|---|---|---|
| Personal data exposed to OpenAI | Medium | Medium | OpenAI API terms: zero data retention for API calls, data not used for training. EU endpoint used |
| Personal data logged in LangSmith (US) | Medium | Medium | Standard Contractual Clauses (SCCs) with LangChain Inc. In production: configure LangSmith to redact PII from traces |
| Unauthorised access to traces | Low | High | LangSmith access restricted to authorised RaumKraft personnel. SSO/MFA enforced |
| Data breach at OpenAI or LangChain | Low | High | Data Processing Agreements in place. Incident notification clauses per GDPR Art. 33/34 |
| Customer unaware data is AI-processed | Medium | Low | Update privacy policy to disclose AI processing. No automated decisions — human reviews all outputs |

### 3.5 Measures to Mitigate Risks

| Measure | Status |
|---|---|
| Use EU-based OpenAI API endpoints | ✅ Implemented |
| OpenAI Data Processing Agreement (DPA) | ✅ Available via OpenAI's standard terms |
| LangSmith access controls (team-only) | ✅ Implemented |
| Standard Contractual Clauses with LangChain Inc. | 🔲 Required before production |
| PII redaction layer before API calls | 🔲 Required before production (anonymise names, emails, phone numbers in enquiry text) |
| Privacy policy update disclosing AI use | 🔲 Required before production |
| LangSmith PII filtering in traces | 🔲 Required before production |
| Data retention policy (auto-delete traces after 90 days) | 🔲 Configure before production |

### 3.6 DPIA Conclusion

UC2 processing **can proceed** with the mitigations listed above. The MVP is used internally for testing only. Before production deployment, the four items marked 🔲 must be completed. The highest residual risk is the US-based hosting of LangSmith traces — this is mitigated by SCCs and PII redaction.

## 4. Data Subject Rights

Under GDPR, individuals whose data is processed have the following rights. Here is how RaumKraft supports each:

| Right | Article | How RaumKraft Supports It |
|---|---|---|
| **Right of access** (Art. 15) | Data subjects can request what data is held about them | LangSmith traces are searchable. RaumKraft can retrieve and provide any trace containing a data subject's enquiry within 30 days |
| **Right to rectification** (Art. 16) | Data subjects can request correction of inaccurate data | Agent can update enquiry records. AI-generated drafts are editable before sending |
| **Right to erasure** (Art. 17) | Data subjects can request deletion of their data | LangSmith traces can be deleted. OpenAI does not retain API data. Deletion request fulfilled within 30 days |
| **Right to restriction** (Art. 18) | Data subjects can request processing be restricted | Specific enquiries can be excluded from AI triage and handled manually |
| **Right to data portability** (Art. 20) | Data subjects can request their data in machine-readable format | Enquiry data can be exported as JSON/CSV from the system |
| **Right to object** (Art. 21) | Data subjects can object to processing based on legitimate interest | If a customer objects to AI processing, their enquiries are routed to manual handling only |
| **Right not to be subject to automated decisions** (Art. 22) | Individuals shall not be subject to solely automated decisions with legal/significant effects | Not applicable — all AI outputs are reviewed by a human agent before any action is taken. No automated decision-making |

**Process:** Data subject requests are handled by RaumKraft's data protection contact. Response timeline: within 30 days per GDPR requirements.

## 5. Third-Party and Cross-Border Transfers

| Third Party | Role | Data Transferred | Location | Transfer Mechanism |
|---|---|---|---|---|
| **OpenAI** (OpenAI LP) | Data processor | UC1: property data (no personal data). UC2: customer enquiry text (may contain personal data). UC3: design brief text | EU endpoint (data processed in EU) | Data Processing Agreement (DPA) via OpenAI's standard terms. Zero data retention policy for API calls |
| **Google** (Gemini API) | Data processor | UC3: room photos (may incidentally show personal items) + design brief context, for photo analysis | US-hosted (Gemini API — no EU endpoint currently available for this feature) | Google Cloud Data Processing Addendum. Standard Contractual Clauses (SCCs) apply for EU-US transfer |
| **LangChain Inc.** (LangSmith) | Sub-processor | AI interaction traces: input prompts, outputs, metadata | US-hosted | Standard Contractual Clauses (SCCs) required. PII redaction recommended before logging |
| **Streamlit / Cloud provider** (production) | Infrastructure | Application data in transit | EU (planned) | EU-hosted deployment. No cross-border transfer |

### Safeguards for US Transfers (Gemini)

- Google Cloud Data Processing Addendum governs Gemini API usage
- Standard Contractual Clauses (SCCs) as the transfer mechanism
- Room photos are processed transiently for analysis — not stored by RaumKraft or retained by Google beyond the API call per Google's stated policy
- Recommendation: obtain explicit client consent before uploading room photos, noting the photo will be analyzed by a US-based AI service
- This is flagged as a residual risk in `roi_risk_assessment.md` (Risk #9) — production deployment should route this through an EU-supported service or provider once available

### Safeguards for US Transfers (LangSmith)

- EU-US Data Privacy Framework: LangChain Inc. compliance status to be verified
- Standard Contractual Clauses (SCCs) as fallback mechanism
- PII redaction layer to minimise personal data in traces
- LangSmith data retention set to 90 days with auto-deletion
- Access restricted to authorised RaumKraft personnel only

### OpenAI Data Processing Terms

- OpenAI's API data usage policy: data submitted via API is **not used to train models**
- Zero data retention available for Enterprise/API customers
- EU-based processing endpoints available and used by RaumKraft
- DPA available as part of OpenAI's standard business terms
