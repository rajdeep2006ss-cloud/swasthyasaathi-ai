"""
SwasthyaSaathi AI - Accessible Healthcare Education Application
PromptWars × SNPSU 2026 Challenge Entry: AI for Healthcare Accessibility

Built with Streamlit & Python.
"""

import streamlit as st
from knowledge_base import (
    HEALTH_TOPICS,
    TRUSTED_SOURCES,
    UI_TRANSLATIONS,
    EMERGENCY_TRIGGERS
)
from assistant import (
    search_knowledge_base,
    generate_doctor_checklist,
    check_emergency_triggers,
    sanitize_user_input
)

# Page configuration
st.set_page_config(
    page_title="SwasthyaSaathi AI - Healthcare Accessibility",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern, high-contrast, accessible & mobile-friendly design
st.markdown("""
<style>
    /* Global Styles & Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Header Banner */
    .main-header {
        background: linear-gradient(135deg, #0d5c75 0%, #198294 100%);
        color: white;
        padding: 1.5rem 2rem;
        border-radius: 12px;
        margin-bottom: 1.2rem;
        box-shadow: 0 4px 15px rgba(13, 92, 117, 0.2);
    }
    .main-header h1 {
        margin: 0;
        font-size: 2.2rem;
        font-weight: 700;
        color: #ffffff;
    }
    .main-header p {
        margin: 0.3rem 0 0 0;
        font-size: 1.05rem;
        opacity: 0.95;
        color: #e0f2fe;
    }

    /* Disclaimer Alert Box */
    .disclaimer-box {
        background-color: #fff8e6;
        border-left: 5px solid #f59e0b;
        padding: 0.9rem 1.2rem;
        border-radius: 6px;
        color: #78350f;
        font-weight: 500;
        font-size: 0.92rem;
        margin-bottom: 1.5rem;
    }
    
    /* Emergency Alert Banner */
    .emergency-box {
        background-color: #fef2f2;
        border: 2px solid #ef4444;
        border-radius: 10px;
        padding: 1.2rem 1.5rem;
        color: #991b1b;
        margin-bottom: 1.5rem;
    }
    .emergency-box h3 {
        color: #dc2626;
        margin-top: 0;
        font-size: 1.3rem;
    }
    .emergency-steps {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 1rem;
        margin-top: 0.8rem;
        border: 1px solid #fca5a5;
    }

    /* Health Cards */
    .health-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }
    .badge-simple {
        background-color: #dcfce7;
        color: #166534;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 600;
    }
    .badge-standard {
        background-color: #dbeafe;
        color: #1e40af;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 600;
    }
    .badge-untranslated {
        background-color: #fef3c7;
        color: #92400e;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 600;
    }
    
    /* Source Pill */
    .source-pill {
        display: inline-block;
        background-color: #f1f5f9;
        color: #0f172a;
        padding: 6px 12px;
        border-radius: 6px;
        margin-right: 8px;
        margin-top: 6px;
        font-size: 0.85rem;
        text-decoration: none;
        border: 1px solid #cbd5e1;
        transition: background-color 0.2s;
    }
    .source-pill:hover {
        background-color: #e2e8f0;
        text-decoration: underline;
    }
    
    /* Privacy Footer Note */
    .privacy-footer {
        font-size: 0.85rem;
        color: #64748b;
        background-color: #f8fafc;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State
if "language" not in st.session_state:
    st.session_state.language = "en"
if "reading_level" not in st.session_state:
    st.session_state.reading_level = "simple"

# Sidebar Configuration & Controls
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/doctor-female.png", width=70)
    st.title("SwasthyaSaathi AI")
    st.caption("PromptWars × SNPSU 2026")
    st.markdown("---")
    
    # Language Selection
    lang_choice = st.selectbox(
        "🌐 Choose Language / भाषा / ಕನ್ನಡ:",
        options=["English", "हिंदी (Hindi)", "ಕನ್ನಡ (Kannada)"],
        index=0 if st.session_state.language == "en" else (1 if st.session_state.language == "hi" else 2)
    )
    if "हिंदी" in lang_choice:
        st.session_state.language = "hi"
    elif "ಕನ್ನಡ" in lang_choice:
        st.session_state.language = "kn"
    else:
        st.session_state.language = "en"
        
    lang = st.session_state.language
    ui = UI_TRANSLATIONS[lang]

    # Reading Level Selection
    level_choice = st.radio(
        ui["reading_level_label"],
        options=[ui["simple_level"], ui["standard_level"]],
        index=0 if st.session_state.reading_level == "simple" else 1
    )
    if "Simple" in level_choice or "सरल" in level_choice or "ಸರಳ" in level_choice:
        st.session_state.reading_level = "simple"
    else:
        st.session_state.reading_level = "standard"
        
    st.markdown("---")
    st.markdown(f"**{ui['no_pii_notice']}**")
    st.markdown(f"*{ui['ai_notice']}*")

# Main Header Banner
st.markdown(f"""
<div class="main-header">
    <h1>🩺 {ui['app_title']}</h1>
    <p>{ui['app_subtitle']}</p>
</div>
""", unsafe_allow_html=True)

# Prominent Educational Disclaimer Notice
st.markdown(f"""
<div class="disclaimer-box">
    {ui['disclaimer_banner']}
</div>
""", unsafe_allow_html=True)

# Navigation Tabs
tab_assistant, tab_prep, tab_library, tab_emergency = st.tabs([
    ui["nav_assistant"],
    ui["nav_prep"],
    ui["nav_library"],
    ui["nav_emergency"]
])

# ==========================================
# TAB 1: HEALTH ASSISTANT (QUERY RETRIEVAL)
# ==========================================
with tab_assistant:
    st.subheader("💬 Ask SwasthyaSaathi Assistant")
    st.write("Type a health query, symptom, or question below to search our verified local medical knowledge library.")
    
    # Quick Topic Selector buttons for easy access
    st.markdown("**Quick Topics:**")
    q_cols = st.columns(4)
    quick_query = None
    if q_cols[0].button("🩸 Diabetes", use_container_width=True):
        quick_query = "diabetes blood sugar"
    if q_cols[1].button("❤️ High BP", use_container_width=True):
        quick_query = "high blood pressure hypertension"
    if q_cols[2].button("🤰 Pregnancy Care", use_container_width=True):
        quick_query = "pregnancy antenatal care"
    if q_cols[3].button("🦟 Dengue Fever", use_container_width=True):
        quick_query = "dengue fever mosquito"

    user_query = st.text_input(
        "Search Query:",
        value=quick_query if quick_query else "",
        placeholder=ui["search_placeholder"],
        key="assistant_query_input"
    )

    if user_query:
        # Sanitize input
        clean_query = sanitize_user_input(user_query)
        
        # Execute Knowledge Retrieval
        response = search_knowledge_base(
            clean_query,
            reading_level=st.session_state.reading_level,
            language=lang
        )
        
        # Emergency Red-Flag Warning UI
        if response["is_emergency"]:
            em_data = response["emergency_data"]
            st.markdown(f"""
            <div class="emergency-box">
                <h3>{em_data['title']}</h3>
                <p><strong>Matched red-flag keyword:</strong> "{em_data['matched_keyword']}"</p>
                <p>{em_data['message']}</p>
                <div class="emergency-steps">
                    <strong>{em_data['action']}</strong>
                    <ul>
                        {''.join([f'<li>{step}</li>' for step in em_data['steps']])}
                    </ul>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        elif response["matched"]:
            # Display matched topic
            badge_class = "badge-simple" if response["reading_level"] == "simple" else "badge-standard"
            badge_text = "🌱 Simple Reading Level" if response["reading_level"] == "simple" else "📖 Standard Reading Level"
            
            st.markdown(f"### {response['title']}")
            
            # Badges line
            badge_html = f'<span class="{badge_class}">{badge_text}</span> '
            if response["is_untranslated"]:
                badge_html += f'<span class="badge-untranslated">{ui["untranslated_tag"]}</span>'
            st.markdown(badge_html, unsafe_allow_html=True)
            st.write("")
            
            st.markdown(response["content"])
            
            st.markdown("---")
            st.markdown(f"#### {ui['trusted_sources_heading']}")
            for src in response["sources"]:
                st.markdown(f"- [{src['name']}]({src['url']})")
                
            st.markdown("---")
            st.info("💡 Tip: Use the 'Doctor Prep Tool' tab to generate questions for your next doctor appointment based on this topic.")

        else:
            st.warning(response["message"])
            if "suggested_topics" in response:
                st.write("**Suggested Topics You Can Explore:**")
                for top_title in response["suggested_topics"]:
                    st.markdown(f"- {top_title}")

# ==========================================
# TAB 2: DOCTOR APPOINTMENT PREP TOOL
# ==========================================
with tab_prep:
    st.subheader(f"📋 {ui['doctor_prep_title']}")
    st.write(ui["doctor_prep_desc"])
    
    topic_options = {t["id"]: t["title"].get(lang, t["title"]["en"]) for t in HEALTH_TOPICS}
    selected_topic_id = st.selectbox(
        ui["prep_topic_label"],
        options=list(topic_options.keys()),
        format_func=lambda x: topic_options[x]
    )
    
    duration_input = st.text_input(
        ui["prep_duration_label"],
        placeholder="e.g., 2 weeks, 3 months..."
    )
    
    symptoms_input = st.text_area(
        ui["prep_symptoms_label"],
        placeholder="e.g., Feeling dizzy in the morning, high blood sugar readings after dinner..."
    )
    
    if st.button(ui["prep_generate_btn"], type="primary"):
        checklist = generate_doctor_checklist(
            topic_id=selected_topic_id,
            symptoms=symptoms_input,
            duration=duration_input,
            language=lang
        )
        
        st.markdown(f"### {ui['prep_output_header']}")
        st.caption(f"Topic: {checklist['topic_title']} | Duration: {checklist['duration']}")
        st.markdown(f"*{ui['prep_copy_instruction']}*")
        
        questions_formatted = ""
        for idx, q in enumerate(checklist["questions"], 1):
            st.markdown(f"**{idx}.** {q}")
            questions_formatted += f"{idx}. {q}\n"
            
        st.download_button(
            label="💾 Download Questions as Text File",
            data=f"SwasthyaSaathi AI - Doctor Visit Checklist\nTopic: {checklist['topic_title']}\nDuration: {checklist['duration']}\nSymptoms: {checklist['symptoms']}\n\nQuestions:\n" + questions_formatted,
            file_name="doctor_visit_checklist.txt",
            mime="text/plain"
        )

# ==========================================
# TAB 3: HEALTH KNOWLEDGE LIBRARY
# ==========================================
with tab_library:
    st.subheader("📚 Curated Health Knowledge Library")
    st.write("Browse all verified medical topics available offline in SwasthyaSaathi AI.")
    
    category_filter = st.selectbox(
        "Filter by Category:",
        options=["All Categories"] + sorted(list(set(t["category"] for t in HEALTH_TOPICS)))
    )
    
    filtered_topics = HEALTH_TOPICS if category_filter == "All Categories" else [t for t in HEALTH_TOPICS if t["category"] == category_filter]
    
    for topic in filtered_topics:
        t_title = topic["title"].get(lang, topic["title"]["en"])
        with st.expander(f"📌 {t_title} ({topic['category']})"):
            level = st.session_state.reading_level
            t_content = topic[level].get(lang) or topic[level]["en"]
            
            if not topic["is_translated"].get(lang, False):
                st.warning(ui["untranslated_tag"])
                
            st.markdown(t_content)
            
            st.markdown("**Genuine References:**")
            for src_key in topic.get("trusted_sources", []):
                if src_key in TRUSTED_SOURCES:
                    src = TRUSTED_SOURCES[src_key]
                    st.markdown(f"- [{src['name']}]({src['url']})")

# ==========================================
# TAB 4: EMERGENCY & HELPLINES
# ==========================================
with tab_emergency:
    st.subheader(f"🚨 {ui['emergency_tab_title']}")
    st.markdown(ui["emergency_tab_intro"])
    
    col_em1, col_em2 = st.columns(2)
    
    with col_em1:
        st.error("🚑 National Ambulance: **108**")
        st.error("🆘 National Emergency Number: **112**")
        st.warning("📞 Health Helpline (State): **104**")
        st.info("🧠 Tele-MANAS Mental Health: **14416** or **1800-891-4416**")
        
    with col_em2:
        st.markdown("### Red-Flag Symptoms Requiring Emergency Care:")
        st.markdown("""
        - 💔 **Chest Pain or Pressure**: Heavy sensation, pain spreading to left arm, neck, or jaw.
        - 🫁 **Severe Shortness of Breath**: Inability to speak complete sentences.
        - 🩸 **Severe Uncontrolled Bleeding**: Or vomiting blood.
        - 🧠 **Sudden Stroke Symptoms (FAST)**: Face drooping, Arm weakness, Slurred speech.
        - 🤢 **Severe Sudden Poisoning or Chemical Exposure**.
        - ⚡ **Seizures / Loss of Consciousness**.
        """)

# Footer Notice
st.markdown("---")
st.markdown(f"""
<div class="privacy-footer">
    <strong>SwasthyaSaathi AI — Healthcare Accessibility Project</strong><br>
    Developed for PromptWars × SNPSU 2026 Challenge.<br>
    <em>Educational information based on ICMR, MoHFW, and WHO guidelines. Zero tracking or data collection.</em>
</div>
""", unsafe_allow_html=True)
