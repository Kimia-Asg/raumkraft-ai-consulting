# EU AI Act Compliance Documentation — RaumKraft AI Assistant

## 1. System Description

The RaumKraft AI Assistant is a text generation and classification system with three use cases:

| Use Case | AI Capability | Input | Output | Human Oversight |
|---|---|---|---|---|
| UC1 — Listing Generator | Natural language generation (NLG) | Structured property data | German sales listing draft | Agent reviews and edits before publishing |
| UC2 — Enquiry Triage | Text classification + response generation | Customer enquiry text | Category, urgency, draft response | Agent reviews and approves before sending |
| UC3 — Design Brief Generator (future) | Text extraction + structuring; optional generative AI for mood board | Meeting notes from client consultation | Structured design brief (room, style, budget, constraints, timeline); optional: two decoration/furniture concepts from room photo | Designer reviews and refines brief; client picks preferred concept |

**Underlying model:** OpenAI GPT-4o-mini (general-purpose LLM, accessed via API)

**Deployment context:** Internal business tool used by RaumKraft employees (agents and designers). Not customer-facing — all outputs are reviewed by a human before reaching any external party.

## 2. Risk Classification — Step-by-Step Reasoning

### Step 1: Is this an Unacceptable Risk system? (Article 5)

**No.** The system does not:
- Employ subliminal or manipulative techniques
- Exploit vulnerabilities of specific groups
- Perform social scoring
- Use real-time remote biometric identification in public spaces
- Perform emotion recognition in workplaces or education

**Conclusion:** Not a Prohibited AI system.

### Step 2: Is this a High-Risk system? (Article 6, Annex III)

High-Risk systems fall into two categories:

**a) AI systems that are safety components of products covered by EU harmonisation legislation (Annex I):**
- The RaumKraft AI Assistant is not a component of any regulated product (medical devices, machinery, vehicles, etc.)
- **Not applicable.**

**b) AI systems in the areas listed in Annex III:**

| Annex III Area | Applicable? | Reasoning |
|---|---|---|
| 1. Biometric identification | No | System does not process biometric data |
| 2. Critical infrastructure | No | Real estate listings are not critical infrastructure |
| 3. Education and vocational training | No | Not used for educational assessment or admissions |
| 4. Employment, workers management | No | Not used for recruitment, promotion, dismissal, or task allocation decisions |
| 5. Essential services (public/private) | No | Property listings and enquiry responses are commercial services, not essential services like credit scoring, insurance, or emergency dispatch |
| 6. Law enforcement | No | Not used by or for law enforcement |
| 7. Migration, asylum, border control | No | Not applicable |
| 8. Administration of justice | No | Not applicable |

**Conclusion:** The system does not fall under any Annex III category. Not a High-Risk AI system.

### Step 3: Is this a Limited Risk system? (Article 50 — Transparency Obligations)

**Article 50(1) — AI systems that interact directly with natural persons:**
- UC2 drafts responses to customers, but a human agent reviews and sends them. The AI does not interact directly with the customer.
- However, if in a future version the system were to interact with customers directly (e.g. chatbot), it would need to disclose that the customer is interacting with AI.
- **Currently not applicable, but flagged for future deployment.**

**Article 50(2) — AI-generated content:**
- UC1 generates marketing text (property listings). Under Article 50(2), AI-generated content must be disclosed when it could be mistaken for human-generated content in matters of public interest.
- Property listings are commercial marketing content. While not strictly public interest, best practice recommends transparency.
- **Applicable as a precaution.** RaumKraft should disclose AI assistance in its listing process.

**Article 50(4) — Deep fakes / synthetic media:**
- UC3 (future) may generate visual concepts using generative AI. If these images could be mistaken for real photographs, they must be labelled as AI-generated.
- **Applicable to UC3 when deployed.**

**Conclusion: Limited Risk — transparency obligations apply.**

### Final Classification

| Use Case | Risk Level | Key Obligation |
|---|---|---|
| UC1 — Listing Generator | **Limited Risk** | Disclose AI involvement in content generation |
| UC2 — Enquiry Triage | **Minimal Risk** (internal tool, human-in-the-loop) | Best practice: log AI use, maintain transparency |
| UC3 — Design Brief Generator | **Minimal Risk** (text structuring); **Limited Risk** if mood board extension is deployed (label AI-generated concepts) |

**Overall system classification: Limited Risk**

We classify conservatively. Although some use cases could be argued as Minimal Risk, applying Limited Risk obligations across the board ensures compliance and builds trust with CEO Chleo — directly addressing her "AI is not transparent" concern.

## 3. Mandatory Requirements for Limited Risk Systems

Under the EU AI Act, Limited Risk systems have **transparency obligations** (Article 50). Here is how RaumKraft addresses each:

| Requirement | How RaumKraft Complies |
|---|---|
| **Disclose AI interaction** — Users must know when they interact with AI | Agents see clear labels in the Streamlit app: "AI-generated draft — review before publishing." All outputs are explicitly marked as AI-generated |
| **Label AI-generated content** — Content that could be mistaken for human-created must be labelled | RaumKraft's internal process notes that listings were AI-assisted. In production: metadata tag on listings indicating AI involvement |
| **Label synthetic media** (UC3 future) — AI-generated images must be marked | Mood board concepts will carry "AI-generated concept — not a real photograph" labels |
| **Inform about emotional recognition** | Not applicable — system does not perform emotion recognition |

### Voluntary Best Practices Adopted (beyond legal requirements)

Even though not legally required for Limited Risk systems, RaumKraft implements these High-Risk-inspired practices to maximise transparency:

| Practice | Implementation |
|---|---|
| Full observability | LangSmith traces every AI interaction — input, output, duration, cost |
| Human oversight | Every AI output requires human review before external use |
| Data governance | GDPR-compliant data handling (see `gdpr_documentation.md`) |
| Quality management | LangSmith evaluation dataset to monitor output quality over time |
| Record-keeping | All traces retained for audit purposes |
| Error reporting | MVP includes basic error handling; production would include incident reporting workflow |

## 4. Conformity Assessment Summary

Since the RaumKraft AI Assistant is classified as **Limited Risk**, a formal conformity assessment (as required for High-Risk systems) is **not legally required**. However, we provide a voluntary self-assessment to demonstrate due diligence.

### 4.1 Purpose and Scope

- **System name:** RaumKraft AI Assistant
- **Provider:** RaumKraft Immobilien & Design (deployer); OpenAI (upstream model provider)
- **Intended use:** Internal business tool for property listing generation, enquiry triage, and design concept generation
- **Not intended for:** Autonomous customer interaction, automated decision-making affecting individuals' rights, or any use without human review

### 4.2 Risk Assessment Outcome

- Classification: Limited Risk (Article 50 transparency obligations)
- No Annex III categories triggered
- No safety component role in regulated products
- Human-in-the-loop on all outputs

### 4.3 Transparency Measures

- All AI outputs labelled as AI-generated in the user interface
- LangSmith monitoring provides full trace audit trail
- Agents trained to review and take responsibility for published content
- CEO and management have LangSmith dashboard access for oversight

### 4.4 Data Protection Integration

- GDPR compliance documented separately (see `gdpr_documentation.md`)
- DPIA completed for UC2 (highest-risk processing involving customer enquiry data)
- Data processing agreement with OpenAI in place
- EU-based API endpoints used

### 4.5 Ongoing Compliance

- Quarterly review of EU AI Act developments (regulation is still being implemented)
- Annual review of risk classification if use cases expand
- Any move to customer-facing AI (chatbot, automated responses) triggers re-classification

## 5. Technical Documentation Outline

This outline follows the structure required by Annex IV of the EU AI Act. While not mandatory for Limited Risk systems, it is provided as a readiness measure in case the system is reclassified or RaumKraft chooses to pursue voluntary compliance.

### Table of Contents

1. **General Description of the AI System**
   - 1.1 System name, version, and intended purpose
   - 1.2 Developer / provider information
   - 1.3 Interaction with hardware and other software
   - 1.4 Versions and release history

2. **Detailed Description of Elements and Development Process**
   - 2.1 Methods and steps in development
   - 2.2 Design specifications: input data, logic, algorithms
   - 2.3 System architecture and computational resources
   - 2.4 Description of the underlying model (GPT-4o-mini)
   - 2.5 Data requirements and data governance
   - 2.6 Human oversight measures
   - 2.7 Pre-determined changes and update procedures

3. **Monitoring, Functioning, and Control**
   - 3.1 Performance metrics and benchmarks
   - 3.2 LangSmith monitoring configuration
   - 3.3 Cybersecurity measures
   - 3.4 Logging capabilities (automatic via LangSmith)

4. **Risk Management**
   - 4.1 Risk management system description
   - 4.2 Known and foreseeable risks (see `roi_risk_assessment.md`)
   - 4.3 Residual risks and mitigation measures
   - 4.4 Testing procedures and results

5. **Data Governance**
   - 5.1 Training data (OpenAI's responsibility — GPT-4o-mini pre-trained model)
   - 5.2 Input data specifications (property data schema, enquiry format)
   - 5.3 Data quality measures
   - 5.4 Bias assessment and mitigation

6. **Transparency and User Information**
   - 6.1 Instructions for use
   - 6.2 Technical capabilities and limitations
   - 6.3 Accuracy, robustness, and cybersecurity levels
   - 6.4 User notification of AI involvement

7. **Record-Keeping and Accountability**
   - 7.1 Logging architecture (LangSmith integration)
   - 7.2 Audit trail specifications
   - 7.3 Roles and responsibilities
   - 7.4 Incident reporting procedures

8. **EU Declaration of Conformity**
   - 8.1 Self-declaration (Limited Risk — voluntary compliance)
   - 8.2 Applicable standards referenced
   - 8.3 Date and signature

**Note:** Sections 2.5 (data governance) and 5.1 (training data) reference OpenAI's model card and data practices, as RaumKraft uses a pre-trained model via API and does not train or fine-tune models in-house. RaumKraft is responsible for input data governance and output oversight, not model training.
