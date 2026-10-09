# SwasthyaSaathi AI 🩺
> **PromptWars × SNPSU 2026 Challenge Entry: AI for Healthcare Accessibility**

SwasthyaSaathi AI is a privacy-first, offline-capable Python Streamlit web application designed to break health literacy barriers and make evidence-based healthcare education accessible across India. 

---

## 🌟 Key Features

1. **📱 Accessible & Mobile-Friendly Interface**
   - Clean, modern UI with high-contrast text, clear visual hierarchy, and mobile responsive layout.
2. **🌐 Multilingual Support (English, Hindi, Kannada)**
   - Seamlessly switch between English, हिंदी (Hindi), and ಕನ್ನಡ (Kannada).
   - Any content not fully translated displays an explicit `⚠️ [Untranslated / English Fallback]` indicator to ensure transparency.
3. **🌱 Dual Reading Levels (Simple & Standard)**
   - **Simple**: Plain-language summaries with bulleted practical action steps for low health literacy users.
   - **Standard**: Detailed health guides with target ranges, clinical guidelines (ICMR/WHO), and monitoring parameters.
4. **📋 Doctor Appointment Preparation Tool**
   - Helps users generate, customize, and download structured question checklists prior to visiting a doctor or clinic.
5. **🚨 Red-Flag Emergency Warning Rules**
   - Instant detection of urgent triggers (chest pain, shortness of breath, severe bleeding, stroke signs, poison, etc.).
   - Displays clear advice to call **108 (Ambulance)**, **112 (Emergency)**, or **14416 (Tele-MANAS)**.
6. **🔗 Verified Authentic Sources Only**
   - All health guidance cites genuine public health authorities:
     - Ministry of Health & Family Welfare (MoHFW), Govt. of India (`https://www.mohfw.gov.in`)
     - Indian Council of Medical Research (ICMR) (`https://www.icmr.gov.in`)
     - World Health Organization (WHO) (`https://www.who.int`)
     - National Health Portal of India (NHP) (`https://www.nhp.gov.in`)
     - National Health Service UK (NHS) (`https://www.nhs.uk`)
     - Centers for Disease Control and Prevention (CDC) (`https://www.cdc.gov`)
7. **🔒 Privacy Guarantee (Zero PII & 100% Local)**
   - Never requests names, phone numbers, addresses, or medical records.
   - Active input sanitization strips any phone/email patterns before processing.
8. **💡 Transparent Engine Architecture**
   - Uses a deterministic local keyword-search index over curated public medical guidelines.
   - **No external AI APIs, no black-box generative hallucinations, and no false machine learning claims.**

---

## 📂 Repository Structure

```
swasthyasaathi-ai/
├── app.py              # Main Streamlit user interface & tab navigation
├── assistant.py        # Search engine, emergency detection & doctor prep logic
├── knowledge_base.py   # Curated health topics, translations & source database
├── test_app.py         # Automated Pytest suite (10/10 tests passing)
├── requirements.txt    # Application dependencies (streamlit, pytest)
├── .gitignore          # Environment and cache ignores
└── README.md           # Documentation & launch guide
```

---

## 🛠️ Local Installation & Running Instructions

### 1. Prerequisites
Ensure Python 3.9+ is installed on your system.

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

The application will open in your local web browser at `http://localhost:8501`.

---

## 🧪 Verification & Test Suite Summary

The included test suite (`test_app.py`) verifies:
- ✅ **Emergency Warning Triggers**: Accurate red-flag detection in English and Hindi.
- ✅ **Topic Retrieval**: Accurate matching for Diabetes, Hypertension, Dengue, Pregnancy, Anemia, etc.
- ✅ **Reading Levels**: Correct formatting for Simple vs. Standard reading modes.
- ✅ **Fallback Behavior**: Out-of-scope queries return helpful category guidance without inventing medical facts.
- ✅ **Doctor Prep Tool**: Question generation logic based on user input.
- ✅ **Privacy Compliance**: Automatic stripping of phone numbers and emails.
- ✅ **Authentic Sources**: All links point to trusted `.gov`, `.org`, or official domains.

---

## 📜 Educational Notice & Disclaimer

*SwasthyaSaathi AI provides verified healthcare educational information only. It does not provide medical diagnoses, treatment plans, or personalized medication dosages. Users experiencing medical emergencies should immediately contact local emergency services (108/112 in India) or visit the nearest hospital.*