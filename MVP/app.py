"""
RaumKraft AI Assistant — MVP
=============================
Streamlit app with two use cases:
  Tab 1 (UC1): Property Listing Generator
  Tab 2 (UC2): Client Enquiry Triage

Run:  streamlit run app.py
Requires: .env with OPENAI_API_KEY, LANGSMITH_API_KEY
"""

import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# --- LangSmith tracing setup ---
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_PROJECT"] = "raumkraft-mvp"

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# --- Page config ---
st.set_page_config(
    page_title="RaumKraft AI Assistant",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 RaumKraft AI Assistant")
st.caption("AI-powered tools for RaumKraft Immobilien & Design")

# --- Initialize LLM (cost tracking automatic via langchain_openai) ---
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
)

# =====================================================================
# TAB LAYOUT
# =====================================================================
tab1, tab2 = st.tabs(["📝 Listing Generator (UC1)", "📬 Enquiry Triage (UC2)"])

# =====================================================================
# UC1 — LISTING GENERATOR
# =====================================================================
with tab1:
    st.header("Property Listing Generator")
    st.markdown("Enter property details → AI generates a polished German listing → you review before publishing.")

    col1, col2 = st.columns(2)

    with col1:
        property_type = st.selectbox(
            "Property Type",
            ["Wohnung (Apartment)", "Haus (House)", "Büro (Office)", "Penthouse", "Loft"],
            key="uc1_type"
        )
        district = st.text_input("District / Neighbourhood", placeholder="e.g. Hamburg-Eppendorf", key="uc1_district")
        size_sqm = st.number_input("Size (m²)", min_value=10, max_value=1000, value=75, key="uc1_size")
        rooms = st.number_input("Rooms", min_value=1, max_value=20, value=3, key="uc1_rooms")
        floor = st.text_input("Floor (e.g. 3 of 5)", placeholder="3 of 5", key="uc1_floor")

    with col2:
        energy_class = st.selectbox(
            "Energy Class",
            ["A+", "A", "B", "C", "D", "E", "F", "G", "H"],
            index=2,
            key="uc1_energy"
        )
        asking_price = st.number_input("Asking Price (€)", min_value=10000, max_value=10000000, value=350000, step=5000, key="uc1_price")
        features = st.text_area(
            "Features (comma-separated)",
            placeholder="e.g. Balkon, Einbauküche, Fußbodenheizung, Aufzug",
            key="uc1_features"
        )
        target_audience = st.selectbox(
            "Target Audience",
            ["General", "Young professionals", "Families", "Seniors", "Investors"],
            key="uc1_audience"
        )
        neighbourhood_notes = st.text_area(
            "Neighbourhood Notes (optional)",
            placeholder="e.g. Near Eppendorfer Baum, cafés, park nearby",
            key="uc1_neighbourhood"
        )

    if st.button("🚀 Generate Listing", key="uc1_generate", type="primary"):
        if not district:
            st.warning("Please enter a district.")
        else:
            system_prompt = """You are a copywriter for RaumKraft Immobilien & Design, a premium German real estate and interior design firm. Write property listings in German that are:
- Professional but warm — not robotic, not overly salesy
- Factually accurate — use ONLY the data provided, never invent features
- Structured: headline, lifestyle paragraph, key facts, neighbourhood note, CTA
- Length: 150–200 words
- Mention energy class naturally
- If target audience is specified, subtly tailor the tone

Never fabricate amenities, transportation connections, or neighbourhood details not provided in the input. If information is missing, omit it — do not guess."""

            user_prompt = f"""Property type: {property_type}
District: {district}
Size: {size_sqm} sqm
Rooms: {rooms}
Floor: {floor}
Features: {features}
Energy class: {energy_class}
Asking price: €{asking_price:,}
Target audience: {target_audience}
Neighbourhood notes: {neighbourhood_notes}"""

            with st.spinner("Generating listing..."):
                response = llm.invoke([
                    SystemMessage(content=system_prompt),
                    HumanMessage(content=user_prompt),
                ])

            st.success("Listing generated!")
            st.markdown("---")
            st.subheader("Generated Listing Draft")
            edited_listing = st.text_area(
                "Edit the listing below before publishing:",
                value=response.content,
                height=300,
                key="uc1_edit"
            )
            if st.button("✅ Approve & Copy", key="uc1_approve"):
                st.code(edited_listing, language=None)
                st.success("Listing approved! Copy the text above and publish.")
            st.caption("🔍 This draft was traced in LangSmith for full transparency.")


# =====================================================================
# UC2 — ENQUIRY TRIAGE
# =====================================================================
with tab2:
    st.header("Client Enquiry Triage")
    st.markdown("Paste a customer enquiry → AI classifies it and drafts a response → you review before sending.")

    enquiry_text = st.text_area(
        "Paste the customer enquiry here",
        height=150,
        placeholder="e.g. Guten Tag, ich interessiere mich für die 3-Zimmer-Wohnung in Eppendorf. Ist eine Besichtigung am Samstag möglich? Mit freundlichen Grüßen, Herr Müller",
        key="uc2_enquiry"
    )

    enquiry_language = st.selectbox(
        "Response language",
        ["German (Deutsch)", "English"],
        key="uc2_lang"
    )

    if st.button("📨 Classify & Draft Response", key="uc2_classify", type="primary"):
        if not enquiry_text.strip():
            st.warning("Please paste an enquiry first.")
        else:
            lang_instruction = "Respond in German." if "German" in enquiry_language else "Respond in English."

            system_prompt = f"""You are the AI assistant for RaumKraft Immobilien & Design, a premium German real estate and interior design firm.

Your job:
1. CLASSIFY the incoming enquiry into exactly one category:
   - Viewing Request
   - Pricing Question
   - General Information
   - Complaint
   - Interior Design Enquiry
   - Other

2. Assess URGENCY: High / Medium / Low

3. DRAFT a professional, warm response that the human agent can review and send.

{lang_instruction}

Output format:
📋 **Category:** [category]
⚡ **Urgency:** [High/Medium/Low]
💬 **Suggested Response:**
[draft response]

Keep the draft response concise (80–120 words), professional but warm, and never commit to anything — always frame as "we will get back to you" or "let me check with the team." The human agent will finalize."""

            with st.spinner("Classifying and drafting response..."):
                response = llm.invoke([
                    SystemMessage(content=system_prompt),
                    HumanMessage(content=f"Customer enquiry:\n\n{enquiry_text}"),
                ])

            st.success("Enquiry classified!")
            st.markdown("---")
            st.markdown(response.content)
            st.markdown("---")
            st.info("✅ Agent: review the classification and draft above, edit if needed, then send. This interaction was traced in LangSmith.")


# =====================================================================
# SIDEBAR
# =====================================================================
with st.sidebar:
    st.markdown("### About")
    st.markdown("""
    **RaumKraft AI Assistant** — MVP for AI Consulting Capstone

    **Use Cases:**
    - **UC1:** Property listing generation
    - **UC2:** Client enquiry triage

    **How it works:**
    - AI generates drafts; humans review before action
    - Every AI interaction is traced in LangSmith
    - All costs are tracked per request

    **Tech:** Streamlit · LangChain · OpenAI GPT-4o-mini · LangSmith
    """)

    st.markdown("---")
    st.markdown("### Transparency")
    st.markdown("All AI calls are logged to [LangSmith](https://smith.langchain.com) for full observability. No black box.")