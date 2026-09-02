"""
RaumKraft AI Assistant — MVP
=============================
Streamlit app with three use cases:
  Tab 1 (UC1): Property Listing Generator
  Tab 2 (UC2): Client Enquiry Triage
  Tab 3 (UC3): Design Brief Generator + Mood Board

Run:  streamlit run app.py
Requires: .env with OPENAI_API_KEY, LANGSMITH_API_KEY, GEMINI_API_KEY
"""

import os
import re
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

# --- Initialize LLM ---
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

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
        property_type = st.selectbox("Property Type", ["Wohnung (Apartment)", "Haus (House)", "Büro (Office)", "Penthouse", "Loft"], key="uc1_type")
        district = st.text_input("District / Neighbourhood", placeholder="e.g. Hamburg-Eppendorf", key="uc1_district")
        size_sqm = st.number_input("Size (m²)", min_value=10, max_value=1000, value=75, key="uc1_size")
        rooms = st.number_input("Rooms", min_value=1, max_value=20, value=3, key="uc1_rooms")
        floor = st.text_input("Floor (e.g. 3 of 5)", placeholder="3 of 5", key="uc1_floor")

    with col2:
        energy_class = st.selectbox("Energy Class", ["A+", "A", "B", "C", "D", "E", "F", "G", "H"], index=2, key="uc1_energy")
        asking_price = st.number_input("Asking Price (€)", min_value=10000, max_value=10000000, value=350000, step=5000, key="uc1_price")
        features = st.text_area("Features (comma-separated)", placeholder="e.g. Balkon, Einbauküche, Fußbodenheizung, Aufzug", key="uc1_features")
        target_audience = st.selectbox("Target Audience", ["General", "Young professionals", "Families", "Seniors", "Investors"], key="uc1_audience")
        neighbourhood_notes = st.text_area("Neighbourhood Notes (optional)", placeholder="e.g. Near Eppendorfer Baum, cafés, park nearby", key="uc1_neighbourhood")

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
                response = llm.invoke([SystemMessage(content=system_prompt), HumanMessage(content=user_prompt)])

            st.success("Listing generated!")
            st.markdown("---")
            st.subheader("Generated Listing Draft")
            edited_listing = st.text_area("Edit the listing below before publishing:", value=response.content, height=300, key="uc1_edit")
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

    enquiry_text = st.text_area("Paste the customer enquiry here", height=150,
        placeholder="e.g. Guten Tag, ich interessiere mich für die 3-Zimmer-Wohnung in Eppendorf. Ist eine Besichtigung am Samstag möglich?",
        key="uc2_enquiry")

    enquiry_language = st.selectbox("Response language", ["German (Deutsch)", "English"], key="uc2_lang")

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
                response = llm.invoke([SystemMessage(content=system_prompt), HumanMessage(content=f"Customer enquiry:\n\n{enquiry_text}")])

            st.success("Enquiry classified!")
            st.markdown("---")
            st.markdown(response.content)
            st.markdown("---")
            st.info("✅ Agent: review the classification and draft above, edit if needed, then send. This interaction was traced in LangSmith.")


# =====================================================================
# UC3 — DESIGN BRIEF GENERATOR + MOOD BOARD
# =====================================================================
with tab3:
    st.header("Design Brief Generator")
    st.markdown("Paste meeting notes from a client consultation → AI extracts a design brief → generates per-room prompts → optionally creates mood boards with Gemini AI.")

    meeting_notes = st.text_area("Paste meeting notes / consultation transcript here", height=200,
        placeholder="e.g. Met with Mr. and Mrs. Keller about their apartment in Winterhude. They want a modern style for the living room and kitchen...",
        key="uc3_notes")

    brief_language = st.selectbox("Brief language", ["German (Deutsch)", "English"], key="uc3_lang")

    # --- STEP 1: Extract Brief ---
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
                response = llm.invoke([SystemMessage(content=system_prompt), HumanMessage(content=f"Meeting notes:\n\n{meeting_notes}")])

            st.session_state["uc3_brief_text"] = response.content
            # Clear old room data
            for key in list(st.session_state.keys()):
                if key.startswith("uc3_room") or key.startswith("uc3_gen"):
                    del st.session_state[key]

    # --- Show extracted brief ---
    if "uc3_brief_text" in st.session_state:
        st.success("Design brief extracted!")
        st.markdown("---")
        edited_brief = st.text_area("Edit the brief below before sending to the design team:", value=st.session_state["uc3_brief_text"], height=250, key="uc3_edit")

        # --- STEP 2: Generate per-room prompts ---
        st.markdown("---")
        st.markdown("#### 🖼️ Mood Board Concept Generator")
        st.caption("Based on the brief above, the AI detects which rooms need redesigning and generates a tailored image-generation prompt for each room.")

        if st.button("✨ Generate Prompts Per Room", key="uc3_gen_prompts", type="primary"):
            room_system = """You are an expert prompt engineer for AI image generation. Given a design brief:

1. Identify ALL rooms mentioned for redesign.
2. For EACH room, write a separate image-generation prompt (80–120 words) that:
   - References that an existing room photo will be provided as input
   - Describes the desired style, color palette, and mood for THAT specific room
   - Mentions specific furniture/decor elements relevant to THAT room
   - Respects constraints (pets, kids, items to keep, etc.)
   - Translates budget into a realism level
   - Ends with instruction for photorealistic rendering keeping architecture unchanged

Output format (strictly follow — one section per room):
===ROOM: [Room Name]===
[prompt text]
===END===

If only one room is mentioned, output one section. If the client wants to redesign the whole apartment without specifying rooms, create sections for: Living Room, Kitchen, Bedroom, Bathroom."""

            with st.spinner("Detecting rooms and generating prompts..."):
                room_response = llm.invoke([SystemMessage(content=room_system), HumanMessage(content=f"Design brief:\n\n{edited_brief}")])

            room_blocks = re.findall(r'===ROOM:\s*(.+?)===\s*(.*?)===END===', room_response.content, re.DOTALL)

            if room_blocks:
                rooms_list = []
                for room_name, room_prompt in room_blocks:
                    rooms_list.append({"name": room_name.strip(), "prompt": room_prompt.strip()})
                st.session_state["uc3_rooms"] = rooms_list
            else:
                st.warning("Could not detect rooms. Please check the brief and try again.")

        # --- STEP 3: Per-room prompts + upload + mood board ---
        if "uc3_rooms" in st.session_state:
            rooms_list = st.session_state["uc3_rooms"]
            st.success(f"{len(rooms_list)} room(s) detected for redesign")

            gemini_available = os.getenv("GEMINI_API_KEY") is not None

            for i, room in enumerate(rooms_list):
                st.markdown("---")
                st.markdown(f"### 🏠 {room['name']}")

                # Show prompt
                st.text_area(f"Generated prompt for {room['name']}:", value=room["prompt"], height=120, key=f"uc3_prompt_{i}")

                # Photo upload
                photo = st.file_uploader(f"Upload photo of {room['name']}", type=["jpg", "jpeg", "png"], key=f"uc3_photo_{i}")
                if photo:
                    st.image(photo, caption=f"Current {room['name']}", width=350)

                # Generate mood board
                if gemini_available and photo:
                    if st.button(f"🎨 Generate Design Concept for {room['name']}", key=f"uc3_mood_{i}"):
                        from google import genai
                        from google.genai import types
                        from PIL import Image
                        import io

                        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
                        image = Image.open(photo)

                        # Convert image to bytes
                        img_bytes = io.BytesIO()
                        image.save(img_bytes, format='PNG')
                        img_bytes = img_bytes.getvalue()

                        mood_prompt = f"""You are a professional interior designer at RaumKraft Immobilien & Design.

Look at this photo of the client's current {room['name']} and create a detailed redesign concept based on the following requirements:

{room['prompt']}

Provide:
1. **Design Concept Overview** — 2-3 sentences describing the overall vision
2. **Color Palette** — specific colors for walls, furniture, and accents
3. **Furniture & Layout** — what to keep, what to replace, specific recommendations
4. **Materials & Textures** — fabrics, wood types, finishes
5. **Key Design Elements** — 3-5 standout pieces or features that define the space
6. **Constraints Addressed** — how the design respects the client's constraints

Be specific and professional. Reference what you see in the current room photo and explain what changes."""

                        with st.spinner(f"Generating design concept for {room['name']}... (15-30 seconds)"):
                            try:
                                gen_response = client.models.generate_content(
                                    model="gemini-3.6-flash",
                                    contents=[
                                        mood_prompt,
                                        types.Part.from_bytes(data=img_bytes, mime_type="image/png")
                                    ]
                                )

                                st.session_state[f"uc3_gen_txt_{i}"] = gen_response.text

                            except Exception as e:
                                st.error(f"Gemini failed for {room['name']}: {str(e)}")
                                st.info("Copy the prompt above and use it manually in Google Gemini or Nano Banana.")

                elif not gemini_available and photo:
                    st.caption(f"📋 Copy the prompt above + your photo into Google Gemini or Nano Banana to generate the mood board.")

                # Show results
                if f"uc3_gen_img_{i}" in st.session_state:
                    from PIL import Image
                    import io
                    gen_img = Image.open(io.BytesIO(st.session_state[f"uc3_gen_img_{i}"]))
                    st.image(gen_img, caption=f"AI-generated concept for {room['name']}", width=500)
                    st.caption("⚠️ AI-generated concept — not a real photograph. For client presentation only.")

                if f"uc3_gen_txt_{i}" in st.session_state:
                    st.info(f"Gemini text concept for {room['name']}:")
                    st.markdown(st.session_state[f"uc3_gen_txt_{i}"])

        st.caption("🔍 All AI interactions are traced in LangSmith for full transparency.")


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
    - **UC3:** Design brief generation + mood board

    **How it works:**
    - AI generates drafts; humans review before action
    - Every AI interaction is traced in LangSmith
    - All costs are tracked per request

    **Tech:** Streamlit · LangChain · OpenAI GPT-4o-mini · Google Gemini · LangSmith
    """)

    st.markdown("---")
    st.markdown("### Transparency")
    st.markdown("All AI calls are logged to [LangSmith](https://smith.langchain.com) for full observability. No black box.")
