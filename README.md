# SwasthyaSaathi AI 🩺
> **PromptWars × SNPSU 2026 Challenge Entry: AI for Healthcare Accessibility**

SwasthyaSaathi AI is a privacy-first, offline-capable Python Streamlit web application designed to break health literacy barriers and make evidence-based healthcare education accessible across India.

---

## 🌟 Key Features

1. **🎨 Theme System (Light, Dark, System Default)**
   - **Sidebar Theme Selector**: Choose between **System Default**, **Light**, and **Dark** themes.
   - Dynamic CSS variable engine (`--bg-app`, `--bg-card`, `--accent-primary`, etc.) ensures readable contrast across cards, buttons, inputs, tabs, and Plotly charts.
   - Keyboard accessibility focus rings and `@media (prefers-reduced-motion: reduce)` support.

2. **🏠 Home Dashboard & Overview Metrics**
   - **Compact Hero Section**: Stethoscope SVG graphic, SwasthyaSaathi AI identity, and healthcare accessibility tagline.
   - **System Overview Cards**: Real verified metrics derived from the database:
     - 📚 **8** Curated Health Topics
     - 🌐 **3** Supported Languages (EN, HI, KN)
     - 🔗 **6** Official Health Bodies (WHO, ICMR, MoHFW, NHP, NHS, CDC)
     - 🚨 **4** Emergency Helplines (108, 112, 104, 14416)
   - **Medical Disclaimer**: High-visibility warning panel clarifying educational purpose.
   - **Emergency Quick Access**: High-visibility emergency strip.
   - **Featured Daily Health Tip**: Curated tip with direct citation link to official health organization source.

3. **📌 Interactive Feature Navigation Grid**
   - 4 Clickable Cards Grid (*Health Assistant*, *Doctor Prep Tool*, *Knowledge Library*, *Emergency Info*).
   - Session-state routing via `st.session_state.active_tab` with hover lift animations and clean buttons.

4. **📊 Redesigned Plotly Data Visualizations ("Health Knowledge Overview")**
   - **Chart A (Curated Knowledge Distribution)**: Horizontal Plotly bar chart showing entry counts per category with long label handling and theme-matching palette (`#0d5c75`, `#0284c7`, etc.).
   - **Chart B (Trusted Source Coverage)**: Plotly bar chart showing reference coverage per official body (ICMR, MoHFW, WHO, NHP, NHS, CDC).
   - Theme-adaptive Plotly templates (`plotly_white` and `plotly_dark`).

5. **💬 Health Assistant & Multilingual Support**
   - Keyword query engine supporting **English**, **हिंदी (Hindi)**, and **ಕನ್ನಡ (Kannada)** with `⚠️ Untranslated` fallback badges.

6. **🌱 Dual Reading Levels**
   - **Simple**: Plain language action steps.
   - **Standard**: Clinical target ranges (ICMR/WHO) and detailed health guides.

7. **📋 Doctor Appointment Prep Tool**
   - Custom question checklist generator with text file export.

8. **🚨 Red-Flag Emergency Detection**
   - Keyword alert rules for urgent symptoms (chest pain, stroke, poison, etc.) displaying 108/112/104 helplines.

9. **🔒 Privacy & Transparency Guarantee**
   - Zero PII (names, numbers, emails) requested or stored. Regex sanitization strips sensitive patterns.
   - 100% local operation — no external generative AI APIs.

---

## 📂 Repository Structure

```
swasthyasaathi-ai/
├── app.py              # Streamlit interface, theme engine & dashboard navigation
├── assistant.py        # Search engine, emergency check, metrics derivation & theme config
├── knowledge_base.py   # Curated health topics, translations & source database
├── test_app.py         # Automated Pytest suite (15/15 tests passing)
├── requirements.txt    # Python dependencies (streamlit, pytest, plotly)
├── .gitignore          # Environment & cache ignores
└── README.md           # Documentation & setup guide
```

---

## 🛠️ Local Setup & Running Instructions

### 1. Prerequisites
Ensure Python 3.9+ is installed.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Automated Tests
```bash
python -m pytest test_app.py -v
```

### 4. Launch the Streamlit Web Application
```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 🧪 Verification & Test Suite Summary

The automated test suite ([`test_app.py`](file:///C:/Users/user/swasthyasaathi-ai/test_app.py)) verifies:
- ✅ Emergency red-flag alerts in English & Hindi.
- ✅ Diabetes, Hypertension, Dengue, Anemia, and Maternal Health topic retrieval.
- ✅ Simple vs Standard reading level formatting.
- ✅ Out-of-scope query fallback handling.
- ✅ Doctor Prep Tool checklist generation.
- ✅ Privacy PII sanitization.
- ✅ Verified HTTPS source links from official domains.
- ✅ Metadata stats derivation & empty data fallbacks.
- ✅ Overview metrics calculation.
- ✅ Theme configuration helper (Light, Dark, System Default).

---

## 📜 Educational Notice & Disclaimer

*SwasthyaSaathi AI provides verified healthcare educational information only. It does not provide medical diagnoses, treatment plans, or personalized medication dosages. Users experiencing medical emergencies should immediately contact local emergency services (108/112 in India) or visit the nearest hospital.*