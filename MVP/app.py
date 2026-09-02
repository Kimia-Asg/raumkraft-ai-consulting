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
tab1, tab2, tab3 = st.tabs(["📝 Listing Generator (UC1)", "📬 Enquiry Triage (UC2)", "🎨 Design Brief Generator (UC3)"])

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
# UC3 — DESIGN BRIEF GENERATOR
# =====================================================================
with tab3:
    st.header("Design Brief Generator")
    st.markdown("Paste meeting notes from a client consultation → AI extracts and structures a formal design brief → designer reviews and refines.")

    meeting_notes = st.text_area(
        "Paste meeting notes / consultation transcript here",
        height=200,
        placeholder="e.g. Met with Mr. and Mrs. Keller today about their new apartment in Winterhude. They want a modern, minimalist style for the living room. Budget around €15,000. They mentioned they love natural light and want to keep the existing hardwood floors. Timeline: want it done before Christmas, so end of November latest. They also have a cat, so nothing too fragile for lower shelves...",
        key="uc3_notes"
    )

    brief_language = st.selectbox(
        "Brief language",
        ["German (Deutsch)", "English"],
        key="uc3_lang"
    )

    if st.button("📋 Extract Design Brief", key="uc3_extract", type="primary"):
        if not meeting_notes.strip():
            st.warning("Please paste meeting notes first.")
        else:
            lang_instruction = "Write the brief in German." if "German" in brief_language else "Write the brief in English."

            system_prompt = f"""You are an assistant for RaumKraft Immobilien & Design's interior design team. Your job is to extract and structure a formal design brief from raw client meeting notes.

{lang_instruction}

Extract the following fields from the notes. If a field is not mentioned, write "Not specified" — never guess or invent information.

Output format:
🏠 **Room(s):** [which rooms are being designed]
🎨 **Style Preference:** [design style mentioned]
💰 **Budget:** [budget amount or range]
⏰ **Timeline:** [deadline or timeframe]
⚠️ **Constraints:** [any constraints — pets, allergies, existing items to keep, structural limits, etc.]
✨ **Additional Notes:** [anything else relevant for the designer]

Be factual and only use information present in the notes. This brief will be reviewed and refined by a human designer before use."""

            with st.spinner("Extracting design brief..."):
                response = llm.invoke([
                    SystemMessage(content=system_prompt),
                    HumanMessage(content=f"Meeting notes:\n\n{meeting_notes}"),
                ])

            # Store in session_state so it survives the rerun triggered by the next button
            st.session_state["uc3_brief_text"] = response.content

    # Show the extracted brief (persists across reruns via session_state)
    if "uc3_brief_text" in st.session_state:
        st.success("Design brief extracted!")
        st.markdown("---")
        edited_brief = st.text_area(
            "Edit the brief below before sending to the design team:",
            value=st.session_state["uc3_brief_text"],
            height=300,
            key="uc3_edit"
        )
        st.markdown("---")
        st.markdown("#### 🖼️ Mood Board Concept (nice-to-have)")
        st.caption("Generate a ready-to-use prompt for an image generator (e.g. Google Gemini / Nano Banana), based on the design brief above. In production, this prompt would be paired with a photo of the client's current room inside the image generator itself.")

        if st.button("✨ Generate Image Prompt", key="uc3_prompt_gen"):
            prompt_system = """You are an expert prompt engineer for AI image generation models (like Google Gemini / Nano Banana). Given a structured interior design brief, write ONE detailed, professional image-generation prompt that instructs the model to transform a room photo according to the client's requirements.

The prompt must:
- Reference that an existing room photo will be provided as input by the user
- Describe the desired style, color palette, and mood clearly
- Mention specific furniture/decor elements implied by the brief
- Respect any constraints (e.g. pet safety, keep existing floors)
- Stay within the stated budget tier (translate budget into a realism level — e.g. "budget-friendly" vs "premium/luxury" pieces)
- Be a single, ready-to-use prompt (not a list of instructions) — written as one paragraph of 80–120 words
- End with a technical instruction for realistic, photorealistic rendering that keeps the room's architecture (windows, doors, layout) unchanged

Output ONLY the final prompt text — no preamble, no explanation."""

            with st.spinner("Generating image prompt..."):
                prompt_response = llm.invoke([
                    SystemMessage(content=prompt_system),
                    HumanMessage(content=f"Design brief:\n\n{edited_brief}"),
                ])

            st.session_state["uc3_image_prompt_text"] = prompt_response.content

        if "uc3_image_prompt_text" in st.session_state:
            st.success("Image prompt generated!")
            st.text_area(
                "Ready-to-use prompt for Nano Banana / Gemini / other image generator:",
                value=st.session_state["uc3_image_prompt_text"],
                height=150,
                key="uc3_image_prompt"
            )
            st.caption("📋 Copy this prompt into your image generator of choice (e.g. Google Gemini / Nano Banana) along with a photo of the client's room to produce the mood board concept.")

        st.caption("🔍 This extraction was traced in LangSmith for full transparency.")


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
    - **UC3:** Design brief generation (+ mood board planned)

    **How it works:**
    - AI generates drafts; humans review before action
    - Every AI interaction is traced in LangSmith
    - All costs are tracked per request

    **Tech:** Streamlit · LangChain · OpenAI GPT-4o-mini · LangSmith
    """)

    st.markdown("---")
    st.markdown("### Transparency")
    st.markdown("All AI calls are logged to [LangSmith](https://smith.langchain.com) for full observability. No black box.")
