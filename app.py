"""
SwasthyaSaathi AI - Accessible Healthcare Education Application
PromptWars × SNPSU 2026 Challenge Entry: AI for Healthcare Accessibility

Built with Streamlit, Python & Plotly.
Features Light / Dark / System Default Theme Engine, Interactive Dashboard Navigation,
and Verified Health Knowledge Visualizations.
"""

import streamlit as st
import pandas as pd

try:
    import plotly.express as px
    HAS_PLOTLY = True
except ImportError:
    HAS_PLOTLY = False

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
    sanitize_user_input,
    get_knowledge_base_stats,
    get_featured_health_tip,
    get_app_overview_metrics,
    get_theme_config
)

# Page configuration
st.set_page_config(
    page_title="SwasthyaSaathi AI - Healthcare Accessibility",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session State
if "language" not in st.session_state:
    st.session_state.language = "en"
if "reading_level" not in st.session_state:
    st.session_state.reading_level = "simple"
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "home"
if "theme" not in st.session_state:
    st.session_state.theme = "System Default"

# Sidebar Controls & Theme Selector
with st.sidebar:
    # Medical Icon SVG
    st.markdown("""
    <div style="text-align: center; margin-bottom: 0.5rem;">
        <svg width="60" height="60" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect width="24" height="24" rx="12" fill="#0d5c75"/>
            <path d="M12 5V19M5 12H19" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
        </svg>
    </div>
    """, unsafe_allow_html=True)
    st.title("SwasthyaSaathi AI")
    st.caption("PromptWars × SNPSU 2026 Entry")
    st.markdown("---")
    
    # Language Selection
    lang_choice = st.selectbox(
        "🌐 Language / भाषा / ಕನ್ನಡ:",
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
    
    # Theme System Selector
    selected_theme = st.selectbox(
        "🎨 Appearance Theme:",
        options=["System Default", "Light", "Dark"],
        index=["System Default", "Light", "Dark"].index(st.session_state.theme)
    )
    st.session_state.theme = selected_theme
    
    if selected_theme == "System Default":
        st.caption("ℹ️ System Default adapts to your OS/browser setting with fallback to clean light mode.")

    st.markdown("---")
    st.markdown(f"**{ui['no_pii_notice']}**")
    st.markdown(f"*{ui['ai_notice']}*")

# Retrieve active theme configuration
theme_cfg = get_theme_config(st.session_state.theme)
is_dark = (theme_cfg["mode"] == "dark")

# Inject Dynamic CSS Variables and Style System based on Selected Theme
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    :root {{
        --bg-app: {'#0b1120' if is_dark else '#f8fafc'};
        --bg-card: {'#1e293b' if is_dark else '#ffffff'};
        --bg-sidebar: {'#0f172a' if is_dark else '#ffffff'};
        --border-color: {'#334155' if is_dark else '#e2e8f0'};
        --text-primary: {'#f8fafc' if is_dark else '#0f172a'};
        --text-secondary: {'#cbd5e1' if is_dark else '#475569'};
        --text-muted: {'#94a3b8' if is_dark else '#64748b'};
        --accent-primary: {'#14b8a6' if is_dark else '#0d5c75'};
        --accent-hover: {'#38bdf8' if is_dark else '#0284c7'};
        --disclaimer-bg: {'#331f00' if is_dark else '#fff8e6'};
        --disclaimer-border: {'#d97706' if is_dark else '#f59e0b'};
        --disclaimer-text: {'#fef3c7' if is_dark else '#78350f'};
        --emergency-bg: {'#450a0a' if is_dark else '#fef2f2'};
        --emergency-border: {'#f87171' if is_dark else '#ef4444'};
        --emergency-text: {'#fecaca' if is_dark else '#991b1b'};
        --tip-bg: {'#064e3b' if is_dark else '#f0fdf4'};
        --tip-border: {'#34d399' if is_dark else '#16a34a'};
        --tip-text: {'#d1fae5' if is_dark else '#14532d'};
    }}

    /* Global App Background & Typography */
    html, body, [class*="css"], .stApp {{
        font-family: 'Inter', system-ui, -apple-system, sans-serif !important;
        background-color: var(--bg-app) !important;
        color: var(--text-primary) !important;
    }}

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {{
        background-color: var(--bg-sidebar) !important;
        border-right: 1px solid var(--border-color) !important;
    }}
    section[data-testid="stSidebar"] * {{
        color: var(--text-primary) !important;
    }}

    /* Content Padding */
    .main .block-container {{
        padding-top: 1rem !important;
        padding-bottom: 2.5rem !important;
        max-width: 1200px !important;
    }}

    /* Compact Hero Header */
    .welcome-card {{
        background-color: var(--bg-card) !important;
        border: 1px solid var(--border-color) !important;
        border-left: 6px solid var(--accent-primary) !important;
        border-radius: 12px !important;
        padding: 1.25rem 1.5rem !important;
        margin-bottom: 1rem !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05) !important;
    }}
    .welcome-card h2 {{
        color: var(--accent-primary) !important;
        margin: 0 0 0.3rem 0 !important;
        font-size: 1.65rem !important;
        font-weight: 700 !important;
    }}
    .welcome-card p {{
        color: var(--text-secondary) !important;
        margin: 0 !important;
        font-size: 0.95rem !important;
    }}

    /* Educational Disclaimer Banner */
    .disclaimer-banner {{
        background-color: var(--disclaimer-bg) !important;
        border: 1px solid var(--disclaimer-border) !important;
        border-left: 5px solid var(--disclaimer-border) !important;
        border-radius: 8px !important;
        padding: 0.85rem 1.1rem !important;
        color: var(--disclaimer-text) !important;
        font-weight: 500 !important;
        font-size: 0.9rem !important;
        margin-bottom: 1rem !important;
    }}

    /* Emergency Strip */
    .emergency-strip {{
        background-color: var(--emergency-bg) !important;
        border: 1px solid var(--emergency-border) !important;
        border-left: 5px solid var(--emergency-border) !important;
        border-radius: 8px !important;
        padding: 0.85rem 1.1rem !important;
        color: var(--emergency-text) !important;
        margin-bottom: 1.2rem !important;
        font-size: 0.9rem !important;
    }}

    /* Dashboard Navigation Cards Grid */
    .dashboard-card {{
        background-color: var(--bg-card) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 12px !important;
        padding: 1.2rem !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04) !important;
        transition: all 0.2s ease-in-out !important;
        height: 100% !important;
    }}
    .dashboard-card:hover {{
        border-color: var(--accent-hover) !important;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12) !important;
        transform: translateY(-3px) !important;
    }}
    .dashboard-card h3 {{
        margin: 0 0 0.4rem 0 !important;
        color: var(--accent-primary) !important;
        font-size: 1.15rem !important;
    }}
    .dashboard-card p {{
        color: var(--text-secondary) !important;
        font-size: 0.88rem !important;
        line-height: 1.4 !important;
        margin: 0 0 0.8rem 0 !important;
    }}

    /* Metric Cards */
    .metric-box {{
        background-color: var(--bg-card) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 10px !important;
        padding: 1rem !important;
        text-align: center !important;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03) !important;
    }}
    .metric-box .number {{
        font-size: 1.7rem !important;
        font-weight: 800 !important;
        color: var(--accent-primary) !important;
    }}
    .metric-box .label {{
        font-size: 0.82rem !important;
        color: var(--text-muted) !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
    }}

    /* Featured Health Tip Card */
    .tip-card {{
        background-color: var(--tip-bg) !important;
        border: 1px solid var(--tip-border) !important;
        border-left: 5px solid var(--tip-border) !important;
        border-radius: 10px !important;
        padding: 1rem 1.25rem !important;
        color: var(--tip-text) !important;
        margin-bottom: 1.2rem !important;
    }}
    .tip-card h4 {{
        margin: 0 0 0.3rem 0 !important;
        color: var(--tip-text) !important;
        font-size: 1.05rem !important;
    }}

    /* Emergency Full Details Box */
    .emergency-box {{
        background-color: var(--emergency-bg) !important;
        border: 2px solid var(--emergency-border) !important;
        border-radius: 12px !important;
        padding: 1.2rem 1.5rem !important;
        color: var(--emergency-text) !important;
        margin-bottom: 1.5rem !important;
    }}
    .emergency-box h3 {{
        color: var(--emergency-text) !important;
        margin-top: 0 !important;
        font-size: 1.3rem !important;
    }}
    .emergency-steps {{
        background-color: var(--bg-card) !important;
        border-radius: 8px !important;
        padding: 1rem 1.2rem !important;
        margin-top: 0.8rem !important;
        border: 1px solid var(--border-color) !important;
        color: var(--text-primary) !important;
    }}

    /* Badges */
    .badge-simple {{
        background-color: #dcfce7 !important;
        color: #166534 !important;
        padding: 4px 12px !important;
        border-radius: 20px !important;
        font-size: 0.82rem !important;
        font-weight: 600 !important;
    }}
    .badge-standard {{
        background-color: #dbeafe !important;
        color: #1e40af !important;
        padding: 4px 12px !important;
        border-radius: 20px !important;
        font-size: 0.82rem !important;
        font-weight: 600 !important;
    }}
    .badge-untranslated {{
        background-color: #fef3c7 !important;
        color: #92400e !important;
        padding: 4px 12px !important;
        border-radius: 20px !important;
        font-size: 0.82rem !important;
        font-weight: 600 !important;
    }}

    /* Inputs & Selectboxes */
    .stTextInput input, .stTextArea textarea, .stSelectbox [data-baseweb="select"] {{
        background-color: var(--bg-card) !important;
        color: var(--text-primary) !important;
        border-color: var(--border-color) !important;
    }}
    
    /* Footer Note */
    .privacy-footer {{
        font-size: 0.85rem !important;
        color: var(--text-muted) !important;
        background-color: var(--bg-card) !important;
        padding: 1rem !important;
        border-radius: 8px !important;
        border: 1px solid var(--border-color) !important;
        margin-top: 2rem !important;
    }}

    /* Keyboard Focus Ring */
    button:focus-visible, input:focus-visible, select:focus-visible {{
        outline: 3px solid var(--accent-hover) !important;
        outline-offset: 2px !important;
    }}

    /* Reduced Motion */
    @media (prefers-reduced-motion: reduce) {{
        .dashboard-card {{
            transition: none !important;
            transform: none !important;
        }}
    }}
</style>
""", unsafe_allow_html=True)

# System Top Navigation Controls
nav_cols = st.columns(5)
tabs_info = [
    ("home", ui.get("nav_home", "🏠 Home"), "top_nav_home"),
    ("assistant", ui["nav_assistant"], "top_nav_asst"),
    ("prep", ui["nav_prep"], "top_nav_prep"),
    ("library", ui["nav_library"], "top_nav_lib"),
    ("emergency", ui["nav_emergency"], "top_nav_em")
]

for col, (tab_key, tab_label, btn_key) in zip(nav_cols, tabs_info):
    is_active = (st.session_state.active_tab == tab_key)
    btn_type = "primary" if is_active else "secondary"
    if col.button(tab_label, key=btn_key, use_container_width=True, type=btn_type):
        if st.session_state.active_tab != tab_key:
            st.session_state.active_tab = tab_key
            st.rerun()

current_tab = st.session_state.active_tab
st.markdown("<div style='margin-bottom: 0.8rem;'></div>", unsafe_allow_html=True)

# ==========================================
# PAGE 1: HOME DASHBOARD
# ==========================================
if current_tab == "home":
    # Hero Welcome Section with Stethoscope Graphic
    st.markdown(f"""
    <div class="welcome-card">
        <div style="display: flex; align-items: center; gap: 15px;">
            <div style="flex-shrink: 0;">
                <svg width="45" height="45" viewBox="0 0 24 24" fill="none" stroke="{theme_cfg['palette'][0]}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M4.8 2.3A.3.3 0 0 0 4.5 2.6V12a7.5 7.5 0 0 0 15 0V2.6a.3.3 0 0 0-.3-.3h-1.4a.3.3 0 0 0-.3.3V12a5.5 5.5 0 0 1-11 0V2.6a.3.3 0 0 0-.3-.3H4.8z"/>
                    <path d="M12 19.5v2.7a.3.3 0 0 0 .3.3h1.4a.3.3 0 0 0 .3-.3v-2.7"/>
                    <circle cx="18" cy="18" r="3"/>
                </svg>
            </div>
            <div>
                <h2>🩺 {ui['app_title']}</h2>
                <p>{ui['app_subtitle']} — Accessible, privacy-first healthcare education & doctor preparation for India.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Overview Metrics Row (Calculated from Real Knowledge Base Metadata)
    overview_metrics = get_app_overview_metrics()
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    
    with m_col1:
        st.markdown(f"""
        <div class="metric-box">
            <div class="number">{overview_metrics['total_topics']}</div>
            <div class="label">Curated Health Topics</div>
        </div>
        """, unsafe_allow_html=True)

    with m_col2:
        st.markdown(f"""
        <div class="metric-box">
            <div class="number">{overview_metrics['total_languages']}</div>
            <div class="label">Languages (EN, HI, KN)</div>
        </div>
        """, unsafe_allow_html=True)

    with m_col3:
        st.markdown(f"""
        <div class="metric-box">
            <div class="number">{overview_metrics['total_sources']}</div>
            <div class="label">Official Health Bodies</div>
        </div>
        """, unsafe_allow_html=True)

    with m_col4:
        st.markdown(f"""
        <div class="metric-box">
            <div class="number">{overview_metrics['total_emergency_lines']}</div>
            <div class="label">Emergency Helplines</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 0.8rem;'></div>", unsafe_allow_html=True)

    # Educational Medical Disclaimer Notice
    st.markdown(f"""
    <div class="disclaimer-banner">
        {ui['disclaimer_banner']}
    </div>
    """, unsafe_allow_html=True)

    # High-Visibility Emergency Access Panel
    st.markdown("""
    <div class="emergency-strip">
        <strong>🚨 Quick Emergency Contacts (India):</strong> 
        Ambulance: <strong>108</strong> &nbsp;|&nbsp; 
        National Emergency: <strong>112</strong> &nbsp;|&nbsp; 
        Health Line: <strong>104</strong> &nbsp;|&nbsp; 
        Tele-MANAS Mental Health: <strong>14416</strong> (24/7 Free)
    </div>
    """, unsafe_allow_html=True)

    # Featured Educational Health Tip Card with Genuine Link
    tip_data = get_featured_health_tip(lang)
    st.markdown(f"""
    <div class="tip-card">
        <h4>💡 Featured Daily Health Tip: {tip_data['title']} ({tip_data['category']})</h4>
        <div>{tip_data['content']}</div>
        <div style="margin-top: 6px; font-size: 0.84rem;">
            <em>Source: <a href="{tip_data['source_url']}" target="_blank" style="color: inherit; text-decoration: underline;">{tip_data['source_name']}</a></em>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📌 Navigation Cards")
    st.caption("Click any feature card below to navigate directly:")

    # 4 Interactive Dashboard Navigation Cards Grid
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="dashboard-card">
            <h3>💬 Health Assistant</h3>
            <p>Search local medical knowledge, ask health questions, and view reading-level guidelines.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Launch Assistant 💬", key="dash_btn_asst", use_container_width=True, type="primary"):
            st.session_state.active_tab = "assistant"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="dashboard-card">
            <h3>📋 Doctor Prep Tool</h3>
            <p>Generate and download custom question lists for your next clinic or doctor visit.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Prepare Questions 📋", key="dash_btn_prep", use_container_width=True, type="primary"):
            st.session_state.active_tab = "prep"
            st.rerun()

    with col3:
        st.markdown("""
        <div class="dashboard-card">
            <h3>📚 Knowledge Library</h3>
            <p>Browse all 8 curated topics, guidelines, and verified official source references.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Explore Library 📚", key="dash_btn_lib", use_container_width=True, type="primary"):
            st.session_state.active_tab = "library"
            st.rerun()

    with col4:
        st.markdown("""
        <div class="dashboard-card">
            <h3>🚨 Emergency Info</h3>
            <p>Access emergency helpline numbers (108/112/104) and red-flag symptom checklists.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Emergency Info 🚨", key="dash_btn_em", use_container_width=True, type="primary"):
            st.session_state.active_tab = "emergency"
            st.rerun()

    st.markdown("---")
    st.markdown("### 📊 Health Knowledge Overview")
    
    # Interactive Data Visualizations derived directly from knowledge_base.py
    stats = get_knowledge_base_stats()

    if stats and stats.get("categories"):
        c_col1, c_col2 = st.columns(2)

        with c_col1:
            df_cat = pd.DataFrame(list(stats["categories"].items()), columns=["Medical Category", "Curated Topics"])
            df_cat = df_cat.sort_values(by="Curated Topics", ascending=True)
            
            st.markdown("#### Curated Knowledge Distribution")
            if HAS_PLOTLY:
                fig_cat = px.bar(
                    df_cat,
                    y="Medical Category",
                    x="Curated Topics",
                    orientation="h",
                    text="Curated Topics",
                    color="Medical Category",
                    color_discrete_sequence=theme_cfg["palette"],
                    template=theme_cfg["plotly_template"]
                )
                fig_cat.update_layout(
                    showlegend=False,
                    margin=dict(l=10, r=10, t=25, b=10),
                    height=300,
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    xaxis=dict(gridcolor="rgba(128,128,128,0.2)"),
                    yaxis=dict(gridcolor="rgba(128,128,128,0.2)")
                )
                st.plotly_chart(fig_cat, use_container_width=True)
            else:
                st.bar_chart(df_cat.set_index("Medical Category"))

            st.caption("📊 Note: Describes the distribution of curated educational topics in SwasthyaSaathi AI's local health database. It does NOT represent personal patient records or medical statistics.")

        with c_col2:
            df_src = pd.DataFrame(list(stats["sources"].items()), columns=["Official Source", "References Count"])
            df_src = df_src.sort_values(by="References Count", ascending=False)
            
            st.markdown("#### Trusted Source Reference Coverage")
            if HAS_PLOTLY:
                fig_src = px.bar(
                    df_src,
                    x="Official Source",
                    y="References Count",
                    text="References Count",
                    color="Official Source",
                    color_discrete_sequence=theme_cfg["palette"],
                    template=theme_cfg["plotly_template"]
                )
                fig_src.update_layout(
                    showlegend=False,
                    margin=dict(l=10, r=10, t=25, b=10),
                    height=300,
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    xaxis=dict(gridcolor="rgba(128,128,128,0.2)"),
                    yaxis=dict(gridcolor="rgba(128,128,128,0.2)")
                )
                st.plotly_chart(fig_src, use_container_width=True)
            else:
                st.bar_chart(df_src.set_index("Official Source"))

            st.caption("📊 Note: Displays citation reference frequency from official public health bodies (ICMR, MoHFW, WHO, NHP, NHS, CDC).")

    else:
        # Graceful Empty-Data Fallback
        st.info("ℹ️ Knowledge base metadata is currently unavailable.")

# ==========================================
# PAGE 2: HEALTH ASSISTANT
# ==========================================
elif current_tab == "assistant":
    st.subheader("💬 Ask SwasthyaSaathi Assistant")
    st.write("Type a health query, symptom, or question below to search our verified local medical knowledge library.")
    
    # Quick Topic Selector buttons
    st.markdown("**Quick Topics:**")
    q_cols = st.columns(4)
    quick_query = None
    if q_cols[0].button("🩸 Diabetes", key="q_db_asst", use_container_width=True):
        quick_query = "diabetes blood sugar"
    if q_cols[1].button("❤️ High BP", key="q_bp_asst", use_container_width=True):
        quick_query = "high blood pressure hypertension"
    if q_cols[2].button("🤰 Pregnancy Care", key="q_preg_asst", use_container_width=True):
        quick_query = "pregnancy antenatal care"
    if q_cols[3].button("🦟 Dengue Fever", key="q_dengue_asst", use_container_width=True):
        quick_query = "dengue fever mosquito"

    user_query = st.text_input(
        "Search Query:",
        value=quick_query if quick_query else "",
        placeholder=ui["search_placeholder"],
        key="assistant_query_input"
    )

    if user_query:
        clean_query = sanitize_user_input(user_query)
        response = search_knowledge_base(
            clean_query,
            reading_level=st.session_state.reading_level,
            language=lang
        )
        
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
            badge_class = "badge-simple" if response["reading_level"] == "simple" else "badge-standard"
            badge_text = "🌱 Simple Reading Level" if response["reading_level"] == "simple" else "📖 Standard Reading Level"
            
            st.markdown(f"### {response['title']}")
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
            st.info("💡 Tip: Use the 'Doctor Prep Tool' to generate questions for your next doctor appointment based on this topic.")

        else:
            st.warning(response["message"])
            if "suggested_topics" in response:
                st.write("**Suggested Topics You Can Explore:**")
                for top_title in response["suggested_topics"]:
                    st.markdown(f"- {top_title}")

# ==========================================
# PAGE 3: DOCTOR APPOINTMENT PREP TOOL
# ==========================================
elif current_tab == "prep":
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
# PAGE 4: HEALTH KNOWLEDGE LIBRARY
# ==========================================
elif current_tab == "library":
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
# PAGE 5: EMERGENCY & HELPLINES
# ==========================================
elif current_tab == "emergency":
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

# Global Footer Notice
st.markdown("---")
st.markdown(f"""
<div class="privacy-footer">
    <strong>SwasthyaSaathi AI — Healthcare Accessibility Project</strong><br>
    Developed for PromptWars × SNPSU 2026 Challenge.<br>
    <em>Educational information based on ICMR, MoHFW, and WHO guidelines. Zero tracking or data collection.</em>
</div>
""", unsafe_allow_html=True)
