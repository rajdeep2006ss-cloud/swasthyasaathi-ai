"""
SwasthyaSaathi AI - Curated Knowledge Base Module
Contains verified health education topics, multilingual translations, emergency red-flag triggers,
trusted medical sources, and UI strings.

Strict Guidelines:
- Genuine sources only (MoHFW India, ICMR, WHO, NHS, CDC).
- No medical diagnoses or personalized medication dosage prescriptions.
- Clear simple vs standard reading levels.
- Full privacy compliance (no PII requested or stored).
"""

TRUSTED_SOURCES = {
    "mohfw": {
        "name": "Ministry of Health & Family Welfare (MoHFW), Govt. of India",
        "url": "https://www.mohfw.gov.in"
    },
    "icmr": {
        "name": "Indian Council of Medical Research (ICMR)",
        "url": "https://www.icmr.gov.in"
    },
    "who": {
        "name": "World Health Organization (WHO)",
        "url": "https://www.who.int"
    },
    "nhp": {
        "name": "National Health Portal of India",
        "url": "https://www.nhp.gov.in"
    },
    "nhs": {
        "name": "National Health Service (NHS UK)",
        "url": "https://www.nhs.uk"
    },
    "cdc": {
        "name": "Centers for Disease Control and Prevention (CDC)",
        "url": "https://www.cdc.gov"
    }
}

EMERGENCY_TRIGGERS = {
    "en": {
        "keywords": [
            "chest pain", "heart attack", "difficulty breathing", "shortness of breath",
            "severe bleeding", "unconscious", "fainted", "stroke", "facial drooping",
            "slurred speech", "numbness one side", "poison", "swallowed poison",
            "suicidal", "want to die", "severe burn", "choking", "seizure", "convulsions"
        ],
        "title": "🚨 URGENT EMERGENCY NOTICE",
        "message": "The symptoms or words you entered indicate a potential medical emergency. Please do not wait for online information.",
        "action": "Immediate Actions Required:",
        "steps": [
            "Call National Emergency Services immediately at 108 (Ambulance) or 112 (Emergency Helpline).",
            "Seek immediate care at the nearest hospital emergency room.",
            "If someone has collapsed or stopped breathing, call for nearby help immediately.",
            "Tele-MANAS Mental Health Helpline (India): Call 14416 or 1800-891-4416 for urgent mental distress."
        ]
    },
    "hi": {
        "keywords": [
            "छाती में दर्द", "सीने में दर्द", "सांस लेने में तकलीफ", "सांस फूलना",
            "तेज खून बहना", "बेहोश", "स्ट्रोक", "पैरालिसिस", "ज़हर", "ज़हरीला",
            "आत्महत्या", "जल जाना", "दौरा", "मिर्गी"
        ],
        "title": "🚨 आपातकालीन सूचना (Emergency Warning)",
        "message": "आपके द्वारा दर्ज किए गए लक्षण एक गंभीर आपातकालीन स्थिति का संकेत हो सकते हैं। कृपया ऑनलाइन जानकारी का इंतजार न करें।",
        "action": "तुरंत क्या करें:",
        "steps": [
            "108 (एम्बुलेंस) या 112 (राष्ट्रीय आपातकालीन नंबर) पर तुरंत कॉल करें।",
            "निकटतम अस्पताल के आपातकालीन कक्ष (Emergency Room) में जाएँ।",
            "यदि कोई बेहोश है, तो तुरंत आसपास के लोगों से मदद मांगें।",
            "टेली-मानस (Tele-MANAS) मानसिक स्वास्थ्य हेल्पलाइन: 14416 या 1800-891-4416 पर कॉल करें।"
        ]
    },
    "kn": {
        "keywords": [
            "ಎದೆ ನೋವು", "ಉಸಿರಾಟದ ತೊಂದರೆ", "ಉಸಿರು ಕಟ್ಟುವುದು", "ತೀವ್ರ ರಕ್ತಸ್ರಾವ",
            "ಮೂರ್ಛೆ", "ಪಾರ್ಶ್ವವಾಯು", "ವಿಷ", "ಆತ್ಮಹತ್ಯೆ", "ತೀವ್ರ ಗಾಯ", "ಸೆಳೆತ"
        ],
        "title": "🚨 ತುರ್ತು ಎಚ್ಚರಿಕೆ (Emergency Warning)",
        "message": "ನೀವು ನಮೂದಿಸಿದ ರೋಗಲಕ್ಷಣಗಳು ತುರ್ತು ವೈದ್ಯಕೀಯ ಪರಿಸ್ಥಿತಿಯನ್ನು ಸೂಚಿಸುತ್ತವೆ. ದಯವಿಟ್ಟು ಕಾಯಬೇಡಿ.",
        "action": "ತಕ್ಷಣವೇ ಮಾಡಬೇಕಾದ ಕ್ರಮಗಳು:",
        "steps": [
            "ತಕ್ಷಣವೇ 108 (ಆಂಬ್ಯುಲೆನ್ಸ್) ಅಥವಾ 112 ತುರ್ತು ಸಂಖ್ಯೆಗೆ ಕರೆ ಮಾಡಿ.",
            "ಹತ್ತಿರದ ಆಸ್ಪತ್ರೆಯ ತುರ್ತು ನಿಗಾ ಘಟಕಕ್ಕೆ (Emergency Room) ತೆರಳಿ.",
            "ಟೆಲಿ-ಮಾನಸ್ ಮಾನಸಿಕ ಆರೋಗ್ಯ ಸಹಾಯವಾಣಿ (Tele-MANAS): 14416 ಅಥವಾ 1800-891-4416 ಗೆ ಕರೆ ಮಾಡಿ."
        ]
    }
}

UI_TRANSLATIONS = {
    "en": {
        "app_title": "SwasthyaSaathi AI",
        "app_subtitle": "Accessible Health Education & Doctor Appointment Helper",
        "disclaimer_banner": "⚠️ EDUCATIONAL NOTICE: SwasthyaSaathi AI provides verified health education only. It does NOT provide medical diagnosis, treatment, or personalized medication dosages. Always consult a qualified healthcare professional.",
        "nav_assistant": "💬 Health Assistant",
        "nav_prep": "📋 Doctor Prep Tool",
        "nav_library": "📚 Knowledge Library",
        "nav_emergency": "🚨 Emergency & Helplines",
        "reading_level_label": "Choose Reading Level:",
        "simple_level": "🌱 Simple (Plain language & key actions)",
        "standard_level": "📖 Standard (Detailed health guide)",
        "lang_label": "Language / भाषा / ಕನ್ನಡ:",
        "search_placeholder": "Ask a health question (e.g., How to manage high blood pressure? How to prevent anemia?)...",
        "search_btn": "Search Answer",
        "untranslated_tag": "⚠️ Untranslated Content: Displaying verified English fallback text.",
        "trusted_sources_heading": "🔗 Genuine Official Sources & References",
        "no_pii_notice": "🔒 Privacy Guaranteed: No names, contact details, or medical records are asked or saved. All searches stay local on your device.",
        "ai_notice": "💡 Transparency Notice: Uses rule-based knowledge retrieval from verified public guidelines (WHO/ICMR/MoHFW). No external generative AI APIs or unverified data.",
        "doctor_prep_title": "Doctor Appointment Question Generator",
        "doctor_prep_desc": "Prepare a clear, organized list of questions for your next clinic or hospital visit.",
        "prep_topic_label": "Select Primary Health Concern / Topic:",
        "prep_duration_label": "How long have you noticed these symptoms or concern?",
        "prep_symptoms_label": "Describe your main symptom or question (e.g., fatigue, high sugar readings, joint stiffness):",
        "prep_generate_btn": "Generate Doctor Question Checklist",
        "prep_output_header": "Your Doctor Visit Preparation Guide",
        "prep_copy_instruction": "Copy or note down these questions before your visit:",
        "emergency_tab_title": "Emergency Numbers & Red-Flag Symptoms",
        "emergency_tab_intro": "If you or someone around you experiences any of the following severe red-flag symptoms, contact emergency services immediately."
    },
    "hi": {
        "app_title": "स्वास्थ्य साथी AI (SwasthyaSaathi AI)",
        "app_subtitle": "सुलभ स्वास्थ्य शिक्षा और डॉक्टर परामर्श तैयारी टूल",
        "disclaimer_banner": "⚠️ शैक्षिक सूचना: स्वास्थ्य साथी केवल सत्यापित स्वास्थ्य शिक्षा प्रदान करता है। यह डॉक्टरी निदान, इलाज या दवा की खुराक नहीं बताता। हमेशा योग्य डॉक्टर से परामर्श लें।",
        "nav_assistant": "💬 स्वास्थ्य सहायक",
        "nav_prep": "📋 डॉक्टर परामर्श तैयारी",
        "nav_library": "📚 स्वास्थ्य पुस्तकालय",
        "nav_emergency": "🚨 आपातकालीन हेल्पलाइन",
        "reading_level_label": "पढ़ने का स्तर चुनें:",
        "simple_level": "🌱 सरल (आसान भाषा और मुख्य बिंदु)",
        "standard_level": "📖 मानक (विस्तृत स्वास्थ्य निर्देश)",
        "lang_label": "भाषा / Language:",
        "search_placeholder": "स्वास्थ्य संबंधी प्रश्न पूछें (जैसे: ब्लड प्रेशर कैसे नियंत्रित करें? एनीमिया से बचाव कैसे करें?)...",
        "search_btn": "उत्तर खोजें",
        "untranslated_tag": "⚠️ अनअनुवादित सामग्री: अंग्रेजी भाषा का प्रामाणिक विवरण दर्शाया जा रहा है।",
        "trusted_sources_heading": "🔗 आधिकारिक एवं प्रामाणिक स्रोत",
        "no_pii_notice": "🔒 गोपनीयता की गारंटी: कोई नाम, फोन नंबर या मेडिकल रिकॉर्ड नहीं पूछा या सहेजा जाता।",
        "ai_notice": "💡 पारदर्शिता सूचना: यह टूल WHO/ICMR/MoHFW के प्रामाणिक दिशानिर्देशों पर आधारित नियम-आधारित खोज का उपयोग करता है।",
        "doctor_prep_title": "डॉक्टर परामर्श प्रश्न निर्माता",
        "doctor_prep_desc": "अपने अगले डॉक्टर परामर्श के लिए प्रश्नों की स्पष्ट सूची तैयार करें।",
        "prep_topic_label": "मुख्य स्वास्थ्य विषय चुनें:",
        "prep_duration_label": "आपको यह समस्या कितने समय से महसूस हो रही है?",
        "prep_symptoms_label": "अपने मुख्य लक्षण या प्रश्न का विवरण दें:",
        "prep_generate_btn": "डॉक्टर के लिए प्रश्नों की सूची बनाएं",
        "prep_output_header": "आपकी डॉक्टर मुलाकात गाइड",
        "prep_copy_instruction": "डॉक्टर से मिलने से पहले इन प्रश्नों को नोट कर लें:",
        "emergency_tab_title": "आपातकालीन नंबर और गंभीर लक्षण",
        "emergency_tab_intro": "यदि आपको या आपके आसपास किसी को निम्नलिखित गंभीर लक्षण दिखाई दें, तो तुरंत आपातकालीन सेवाओं से संपर्क करें।"
    },
    "kn": {
        "app_title": "ಸ್ವಾಸ್ಥ್ಯಸಾಥಿ AI (SwasthyaSaathi AI)",
        "app_subtitle": "ಸುಲಭ ಆರೋಗ್ಯ ಶಿಕ್ಷಣ ಮತ್ತು ವೈದ್ಯರ ಭೇಟಿ ತಯಾರಿ ಸಹಾಯಕ",
        "disclaimer_banner": "⚠️ ಶೈಕ್ಷಣಿಕ ಸೂಚನೆ: ಸ್ವಾಸ್ಥ್ಯಸಾಥಿ AI ಕೇವಲ ದೃಢೀಕರಿಸಿದ ಆರೋಗ್ಯ ಶಿಕ್ಷಣವನ್ನು ನೀಡುತ್ತದೆ. ಇದು ರೋಗನಿರ್ಣಯ ಅಥವಾ ಚಿಕಿತ್ಸೆ ನೀಡುವುದಿಲ್ಲ. ವೈದ್ಯರನ್ನು ಸಂಪರ್ಕಿಸಿ.",
        "nav_assistant": "💬 ಆರೋಗ್ಯ ಸಹಾಯಕ",
        "nav_prep": "📋 ವೈದ್ಯರ ಭೇಟಿ ತಯಾರಿ",
        "nav_library": "📚 ಆರೋಗ್ಯ ಗ್ರಂಥಾಲಯ",
        "nav_emergency": "🚨 ತುರ್ತು ಸಹಾಯವಾಣಿ",
        "reading_level_label": "ಓದುವ ಹಂತ ಆಯ್ಕೆಮಾಡಿ:",
        "simple_level": "🌱 ಸರಳ (ಸುಲಭ ಭಾಷೆ)",
        "standard_level": "📖 ಪ್ರಮಾಣಿತ (ವಿವರವಾದ ಮಾಹಿತಿ)",
        "lang_label": "ಭಾಷೆ / Language:",
        "search_placeholder": "ಆರೋಗ್ಯ ಕುರಿತ ಪ್ರಶ್ನೆ ಕೇಳಿ (ಉದಾ: ಮಧುಮೇಹ ನಿಯಂತ್ರಣ ಹೇಗೆ?)...",
        "search_btn": "ಉತ್ತರ ಹುಡುಕಿ",
        "untranslated_tag": "⚠️ [ಅನುವಾದಗೊಳ್ಳದ ವಿಷಯ / English Fallback]",
        "trusted_sources_heading": "🔗 ಅಧಿಕೃತ ವೈದ್ಯಕೀಯ ಮೂಲಗಳು",
        "no_pii_notice": "🔒 ಗೌಪ್ಯತೆ ಭರವಸೆ: ಯಾವುದೇ ವೈಯಕ್ತಿಕ ವಿವರಗಳನ್ನು ಸಂಗ್ರಹಿಸುವುದಿಲ್ಲ.",
        "ai_notice": "💡 ಪಾರದರ್ಶಕತೆ ಸೂಚನೆ: ಇದು WHO/ICMR ಅಧಿಕೃತ ನಿಯಮ ಆಧಾರಿತ ಮಾಹಿತಿಯನ್ನು ಬಳಸುತ್ತದೆ.",
        "doctor_prep_title": "ವೈದ್ಯರ ಭೇಟಿ ಪ್ರಶ್ನೆ ತಯಾರಕ",
        "doctor_prep_desc": "ನಿಮ್ಮ ಮುಂದಿನ ವೈದ್ಯರ ಭೇಟಿಗೆ ಸೂಕ್ತ ಪ್ರಶ್ನೆಗಳ ಪಟ್ಟಿ ಮಾಡಿ.",
        "prep_topic_label": "ಮುಖ್ಯ ಆರೋಗ್ಯ ವಿಷಯ:",
        "prep_duration_label": "ಈ ರೋಗಲಕ್ಷಣಗಳು ಎಷ್ಟು ದಿನಗಳಿಂದ ಇವೆ?",
        "prep_symptoms_label": "ನಿಮ್ಮ ಮುಖ್ಯ ರೋಗಲಕ್ಷಣವನ್ನು ವಿವರಿಸಿ:",
        "prep_generate_btn": "ಪ್ರಶ್ನೆಗಳ ಪಟ್ಟಿ ರಚಿಸಿ",
        "prep_output_header": "ನಿಮ್ಮ ವೈದ್ಯರ ಭೇಟಿ ಮಾರ್ಗದರ್ಶಿ",
        "prep_copy_instruction": "ವೈದ್ಯರನ್ನು ಭೇಟಿಯಾಗುವ ಮುನ್ನ ಈ ಪ್ರಶ್ನೆಗಳನ್ನು ಗುರುತಿಸಿ:",
        "emergency_tab_title": "ತುರ್ತು ಸಂಖ್ಯೆಗಳು ಮತ್ತು ಪ್ರಮುಖ ಲಕ್ಷಣಗಳು",
        "emergency_tab_intro": "ತೀವ್ರ ಸ್ವರೂಪದ ರೋಗಲಕ್ಷಣಗಳಿದ್ದರೆ ತಕ್ಷಣ ತುರ್ತು ಸಹಾಯವಾಣಿಗೆ ಕರೆ ಮಾಡಿ."
    }
}

HEALTH_TOPICS = [
    {
        "id": "diabetes_type2",
        "category": "Chronic Conditions",
        "keywords": ["diabetes", "sugar", "blood sugar", "glucose", "insulin", "मधुमेह", "शुगर", "ब्लड शुगर", "ಮಧುಮೇಹ", "ಸಕ್ಕರೆ ಕಾಯಿಲೆ"],
        "title": {
            "en": "Type 2 Diabetes Education & Self-Care",
            "hi": "टाइप 2 मधुमेह (शुगर) शिक्षा और देखभाल",
            "kn": "ಟೈಪ್ 2 ಮಧುಮೇಹ ಜಾಗೃತಿ ಮತ್ತು ಆರೈಕೆ"
        },
        "is_translated": {
            "en": True,
            "hi": True,
            "kn": True
        },
        "simple": {
            "en": """
- **What it is**: Type 2 Diabetes happens when the body does not use blood sugar (glucose) effectively.
- **Common signs**: Increased thirst, frequent urination (especially at night), unexplained tiredness, slow-healing wounds.
- **Key daily actions**:
  1. Eat balanced meals with high-fiber foods like whole grains, pulses, and green vegetables.
  2. Limit refined sugars, sweets, sweetened tea, and processed snacks.
  3. Engage in brisk walking or light exercise for 30 minutes daily.
  4. Take prescribed medications regularly as directed by your doctor.
  5. Check your feet daily for small cuts or red spots.
            """,
            "hi": """
- **यह क्या है**: टाइप 2 डायबिटीज तब होती है जब शरीर ब्लड शुगर (ग्लूकोज) का सही तरीके से उपयोग नहीं कर पाता।
- **सामान्य लक्षण**: अधिक प्यास लगना, बार-बार पेशाब आना, बिना कारण थकावट, घाव धीरे भरना।
- **मुख्य दैनिक कदम**:
  1. फाइबर युक्त भोजन लें जैसे साबुत अनाज, दालें और हरी सब्जियाँ।
  2. मीठे पेय, मिठाई और प्रसंस्कृत (जंक) भोजन से परहेज करें।
  3. प्रतिदिन 30 मिनट तेज पैदल चलें या हल्का व्यायाम करें।
  4. डॉक्टर द्वारा दी गई दवाएं समय पर लें।
  5. पैरों की रोज जांच करें ताकि कोई घाव या चोट न छूटे।
            """,
            "kn": """
- **ಮಧುಮೇಹ ಎಂದರೇನು**: ದೇಹದಲ್ಲಿ ರಕ್ತದ ಸಕ್ಕರೆ ಪ್ರಮಾಣ ನಿಯಂತ್ರಣ ತಪ್ಪಿದಾಗ ಇದು ಸಂಭವಿಸುತ್ತದೆ.
- **ಸಾಮಾನ್ಯ ಲಕ್ಷಣಗಳು**: ಪದೇ ಪದೇ ಬಾಯಾರಿಕೆ, ರಾತ್ರಿ ಹೆಚ್ಚು ಮೂತ್ರ ವಿಸರ್ಜನೆ, ಆಯಾಸ.
- **ದೈನಂದಿನ ಕ್ರಮಗಳು**:
  1. ನಾರಿನಂಶವಿರುವ ಆಹಾರ, ಧಾನ್ಯಗಳು ಮತ್ತು ತರಕಾರಿಗಳನ್ನು ಸೇವಿಸಿ.
  2. ಸಿಹಿತಿಂಡಿ ಮತ್ತು ತಂಪು ಪಾನೀಯಗಳನ್ನು ಕಡಿಮೆ ಮಾಡಿ.
  3. ದಿನಕ್ಕೆ 30 ನಿಮಿಷ ನಡಿಗೆ ಮಾಡಿ.
  4. ವೈದ್ಯರು ಸೂಚಿಸಿದ ಔಷಧಗಳನ್ನು ಸರಿಯಾಗಿ ತೆಗೆದುಕೊಳ್ಳಿ.
            """
        },
        "standard": {
            "en": """
### Understanding Type 2 Diabetes
Type 2 diabetes is a metabolic condition characterized by insulin resistance and relative insulin deficiency. Persistent high blood glucose levels can affect small and large blood vessels over time.

#### Target Testing Recommendations (ICMR Guidelines)
- **Fasting Blood Glucose**: Usually targeted between 80–130 mg/dL (consult your doctor for personal targets).
- **Post-meal Glucose**: Target < 180 mg/dL two hours after meals.
- **HbA1c**: Reflects average blood sugar over 3 months; recommended every 3 to 6 months.

#### Dietary Guidelines
- Emphasize complex carbohydrates with low glycemic index (millets, oats, legumes).
- Maintain portion control and avoid sugar-sweetened beverages.

#### When to Consult Your Doctor Immediately
- Blood sugar levels dropping below 70 mg/dL (hypoglycemia symptoms: sweating, shakiness, confusion).
- Non-healing foot sores or severe foot numbness.
            """,
            "hi": """
### टाइप 2 मधुमेह को समझें
टाइप 2 मधुमेह एक चयापचय (metabolic) स्थिति है जिसमें शरीर इंसुलिन का सही उपयोग नहीं कर पाता। लंबे समय तक हाई ब्लड शुगर रहने से नसों और रक्त वाहिकाओं पर असर पड़ सकता है।

#### जाँच और मानक (ICMR दिशानिर्देश)
- **खाली पेट ब्लड शुगर (Fasting)**: सामान्यतः 80–130 mg/dL का लक्ष्य।
- **खाने के 2 घंटे बाद**: 180 mg/dL से कम का लक्ष्य।
- **HbA1c टेस्ट**: पिछले 3 महीनों का औसत शुगर स्तर बताता है।

#### आहार निर्देश
- बाजरा, ज्वार, रागी और हरी सब्जियों जैसे कॉम्प्लेक्स कार्बोहाइड्रेट लें।
- मीठे पेय पदार्थों से बचें।

#### डॉक्टर से तुरंत कब मिलें
- यदि शुगर 70 mg/dL से नीचे चली जाए (पसीना आना, घबराहट, चक्कर)।
- पैर में कोई घाव या सुन्नपन महसूस हो।
            """,
            "kn": """
### ಟೈಪ್ 2 ಮಧುಮೇಹ ತಿಳುವಳಿಕೆ
ಇನ್ಸುಲಿನ್ ಪ್ರತಿರೋಧದಿಂದಾಗಿ ರಕ್ತದಲ್ಲಿ ಸಕ್ಕರೆ ಪ್ರಮಾಣ ಹೆಚ್ಚಾಗುತ್ತದೆ.

#### ತಪಾಸಣೆ ಮಾರ್ಗದರ್ಶಿ (ICMR)
- **ಖಾಲಿ ಹೊಟ್ಟೆಯ ರಕ್ತದ ಸಕ್ಕರೆ**: 80–130 mg/dL ನಡುವೆ ಇರಬೇಕು.
- **HbA1c ಪರೀಕ್ಷೆ**: 3 ತಿಂಗಳ ಸರಾಸರಿ ಸಕ್ಕರೆ ಮಟ್ಟವನ್ನು ತೋರಿಸುತ್ತದೆ.

#### ವೈದ್ಯರನ್ನು ತಕ್ಷಣ ಸಂಪರ್ಕಿಸಬೇಕಾದ ಸಂದರ್ಭ:
- ಸಕ್ಕರೆ ಮಟ್ಟ 70 mg/dL ಗಿಂತ ಕಡಿಮೆಯಾದರೆ (ನಡುಕ, ಬೆವರು).
- ಕಾಲಿನಲ್ಲಿ ಗಾಯಗಳು ಕಂಡುಬಂದರೆ.
            """
        },
        "questions_for_doctor": [
            "What is my target HbA1c level?",
            "How often should I monitor my blood sugar at home?",
            "Are there any specific dietary restrictions based on my kidney function?",
            "What step should I take if my blood sugar drops too low (hypoglycemia)?"
        ],
        "trusted_sources": ["icmr", "mohfw", "who"]
    },
    {
        "id": "hypertension",
        "category": "Chronic Conditions",
        "keywords": ["hypertension", "high blood pressure", "bp", "blood pressure", "हाई बीपी", "उच्च रक्तचाप", "रक्तचाप", "ಅಧಿಕ ರಕ್ತದೊತ್ತಡ", "ಬಿಪಿ"],
        "title": {
            "en": "Hypertension (High Blood Pressure) Awareness",
            "hi": "उच्च रक्तचाप (हाई बीपी) प्रबंधन",
            "kn": "ಅಧಿಕ ರಕ್ತದೊತ್ತಡ (High BP) ನಿರ್ವಹಣೆ"
        },
        "is_translated": {
            "en": True,
            "hi": True,
            "kn": True
        },
        "simple": {
            "en": """
- **What it is**: High blood pressure means the force of blood against your artery walls is consistently too high.
- **Why it matters**: Often has no clear symptoms ('silent condition'), but damages heart and blood vessels over time.
- **Simple management steps**:
  1. Reduce salt intake to less than 1 teaspoon (5 grams) per day.
  2. Eat fresh fruits, vegetables, and low-fat dairy products.
  3. Avoid smoking, tobacco products, and excessive alcohol consumption.
  4. Stay physically active with daily exercise or walking.
  5. Take prescribed BP medications every day without skipping doses.
            """,
            "hi": """
- **यह क्या है**: हाई ब्लड प्रेशर का मतलब है कि धमनियों की दीवारों पर खून का दबाव लगातार अधिक बना रहता है।
- **यह महत्वपूर्ण क्यों है**: अक्सर इसके कोई बाहरी लक्षण नहीं होते, लेकिन यह धीरे-धीरे दिल और गुर्दों को नुकसान पहुंचा सकता है।
- **सरल उपाय**:
  1. नमक का सेवन कम करें (दिन भर में 1 छोटी चम्मच या 5 ग्राम से कम)।
  2. ताजे फल, सब्जियां और कम वसा वाले खाद्य पदार्थ खाएं।
  3. धूम्रपान और तंबाकू से दूर रहें।
  4. प्रतिदिन 30 मिनट टहलें।
  5. डॉक्टर द्वारा दी गई बीपी की दवा रोज बिना नागा लें।
            """,
            "kn": """
- **ಅಧಿಕ ರಕ್ತದೊತ್ತಡ ಎಂದರೇನು**: ರಕ್ತನಾಳಗಳಲ್ಲಿ ರಕ್ತದ ಒತ್ತಡ ನಿರಂತರವಾಗಿ ಹೆಚ್ಚಿರುವುದು.
- **ಸರಳ ಕ್ರಮಗಳು**:
  1. ದಿನಕ್ಕೆ 1 ಚಮಚಕ್ಕಿಂತ (5 ಗ್ರಾಂ) ಕಡಿಮೆ ಉಪ್ಪು ಬಳಸಿ.
  2. ತಾಜಾ ಹಣ್ಣು ಮತ್ತು ತರಕಾರಿಗಳನ್ನು ಸೇವಿಸಿ.
  3. ಧೂಮಪಾನ ಹಾಗೂ ತಂಬಾಕು ವರ್ಜಿಸಿ.
  4. ದಿನವೂ 30 ನಿಮಿಷ ವ್ಯಾಯಾಮ ಮಾಡಿ.
  5. ಬಿಪಿ ಮಾತ್ರೆಗಳನ್ನು ತಪ್ಪದೇ ಸೇವಿಸಿ.
            """
        },
        "standard": {
            "en": """
### Clinical Perspective on Hypertension
Hypertension is defined clinically as systolic blood pressure ≥ 140 mmHg and/or diastolic blood pressure ≥ 90 mmHg on repeated clinic readings.

#### Classification (WHO / Indian Guidelines)
- **Normal**: Systolic < 120 mmHg and Diastolic < 80 mmHg.
- **Elevated/Prehypertension**: Systolic 120–139 or Diastolic 80–89 mmHg.
- **Stage 1 Hypertension**: Systolic 140–159 or Diastolic 90–99 mmHg.
- **Stage 2 Hypertension**: Systolic ≥ 160 or Diastolic ≥ 100 mmHg.

#### Key Lifestyle Interventions (DASH Diet Principles)
- Increase dietary potassium (from bananas, green leafy vegetables).
- Maintain healthy body mass index (BMI).
- Limit dietary sodium intake.

#### Urgent Symptoms
If BP is extremely high (>180/120 mmHg) accompanied by chest pain, shortness of breath, blurred vision, or severe headache, seek emergency care immediately.
            """,
            "hi": """
### उच्च रक्तचाप का नैदानिक विवरण
उच्च रक्तचाप तब माना जाता है जब सिस्टोलिक बीपी ≥ 140 mmHg या डायस्टोलिक बीपी ≥ 90 mmHg हो।

#### बीपी का वर्गीकरण
- **सामान्य**: < 120/80 mmHg
- **प्री-हाइपरटेंशन**: 120–139 / 80–89 mmHg
- **स्टेज 1 हाई बीपी**: 140–159 / 90–99 mmHg
- **स्टेज 2 हाई बीपी**: ≥ 160/100 mmHg

#### जीवनशैली में बदलाव
- भोजन में सोडियम (नमक) कम करें और पोटेशियम (केला, हरी पत्तेदार सब्जियां) बढ़ाएं।
- तनाव कम करने के लिए प्राणायाम या योग करें।
            """,
            "kn": """
### ರಕ್ತದೊತ್ತಡದ ವರ್ಗೀಕರಣ
- **ಸಾಮಾನ್ಯ**: < 120/80 mmHg
- **ಅಧಿಕ ಬಿಪಿ (Stage 1)**: 140–159 / 90–99 mmHg

#### ತಕ್ಷಣ ಚಿಕಿತ್ಸೆ ಅಗತ್ಯವಿರುವ ಸಂದರ್ಭ:
ರಕ್ತದೊತ್ತಡ 180/120 ಗಿಂತ ಹೆಚ್ಚಿದ್ದು ಎದೆನೋವು ಅಥವಾ ಉಸಿರಾಟದ ತೊಂದರೆ ಇದ್ದರೆ ತಕ್ಷಣ ಆಸ್ಪತ್ರೆಗೆ ತೆರಳಿ.
            """
        },
        "questions_for_doctor": [
            "What is my average blood pressure target?",
            "How frequently should I check my BP at home?",
            "Does my medication interact with over-the-counter painkillers like ibuprofen?",
            "Should I schedule tests for kidney function or cholesterol?"
        ],
        "trusted_sources": ["icmr", "mohfw", "who", "nhs"]
    },
    {
        "id": "maternal_child",
        "category": "Women & Child Health",
        "keywords": ["pregnancy", "maternal", "pregnant", "antenatal", "baby health", "iron folic acid", "गर्भपात", "गर्भावस्था", "गर्भवती", "माँ और बच्चा", "ಗರ್ಭಿಣಿ", "ತಾಯಿ ಮಗು"],
        "title": {
            "en": "Maternal & Antenatal Health Guidelines",
            "hi": "गर्भावस्था एवं मातृ-शिशु स्वास्थ्य निर्देश",
            "kn": "ಗರ್ಭಿಣಿ ಮತ್ತು ತಾಯಿ-ಮಗು ಆರೈಕೆ ಮಾರ್ಗದರ್ಶಿ"
        },
        "is_translated": {
            "en": True,
            "hi": True,
            "kn": True
        },
        "simple": {
            "en": """
- **Antenatal Care Checkups**: Every pregnant woman should register her pregnancy early and attend at least 4 ANC visits.
- **Key Health Practices**:
  1. Take Iron and Folic Acid (IFA) supplements daily as advised by ANM/Doctor to prevent anemia.
  2. Receive Tetanus-diphtheria (Td) immunization doses.
  3. Eat protein-rich foods, pulses, milk, green leafy vegetables, and seasonal fruits.
  4. Rest adequately (8 hours sleep at night and 2 hours in the afternoon).
  5. Avoid lifting heavy weights or taking non-prescribed medicines.
            """,
            "hi": """
- **गर्भावस्था की देखभाल**: हर गर्भवती महिला को शुरुआती 3 महीनों में पंजीकरण कराना चाहिए और कम से कम 4 एएनसी (ANC) जांच करानी चाहिए।
- **मुख्य आदतें**:
  1. एएनएम/डॉक्टर की सलाह पर रोजाना आयरन और फोलिक एसिड (IFA) की गोलियां लें।
  2. टिटनेस (Td) का टीका अवश्य लगवाएं।
  3. हरी सब्जियां, दालें, दूध, फल और प्रोटीन युक्त भोजन खाएं।
  4. पर्याप्त आराम करें (रात में 8 घंटे और दोपहर में 2 घंटे)।
  5. बिना डॉक्टर की सलाह के कोई दवा न लें।
            """,
            "kn": """
- **ಗರ್ಭಿಣಿ ಆರೈಕೆ**: ಗರ್ಭಿಣಿಯರು ಕನಿಷ್ಠ 4 ಬಾರಿಯಾದರೂ ವೈದ್ಯಕೀಯ ತಪಾಸಣೆ (ANC Checkup) ಮಾಡಿಸಿಕೊಳ್ಳಬೇಕು.
- **ಮುಖ್ಯ ಕ್ರಮಗಳು**:
  1. ಕಬ್ಬಿನಾಂಶ (Iron & Folic Acid) ಮಾತ್ರೆಗಳನ್ನು ತಪ್ಪದೇ ಸೇವಿಸಿ.
  2. ಟೆಟನಸ್ ಚುಚ್ಚುಮದ್ದು ಪಡೆದುಕೊಳ್ಳಿ.
  3. ಪೌಷ್ಟಿಕ ಆಹಾರ ಮತ್ತು ಹಸಿರು ತರಕಾರಿಗಳನ್ನು ಸೇವಿಸಿ.
  4. ಸರಿಯಾದ ವಿಶ್ರಾಂತಿ ಪಡೆಯಿರಿ.
            """
        },
        "standard": {
            "en": """
### MoHFW / WHO Guidelines for Pregnant Women
Early ANC registration (within 12 weeks) enables detection of high-risk factors such as anemia, gestational diabetes, and pre-eclampsia.

#### Essential Components of ANC
- **Blood Pressure & Hemoglobin Monitoring**: Detect pre-eclampsia and severe anemia early.
- **Ultrasound Evaluation**: Assess fetal growth and anatomical development.
- **Nutrition**: Caloric intake increases during 2nd and 3rd trimester. Supplementation with Folic Acid (first trimester) and Iron/Calcium (2nd/3rd trimester).

#### Danger Signs in Pregnancy (Seek Immediate Care)
- Vaginal bleeding or fluid leakage.
- Severe headache with blurred vision or facial swelling.
- Reduced fetal movements after 24 weeks.
- High fever or severe abdominal pain.
            """,
            "hi": """
### मातृ स्वास्थ्य दिशानिर्देश (MoHFW)
12 हफ्तों के भीतर गर्भावस्था का पंजीकरण आवश्यक है ताकि एनीमिया या उच्च रक्तचाप का समय पर पता चल सके।

#### खतरे के लक्षण (तुरंत अस्पताल जाएं)
- योनि से रक्तस्राव या तरल पदार्थ बहना।
- तेज सिरदर्द, आंखों के सामने धुंधलापन या चेहरे पर सूजन।
- बच्चे की हलचल कम महसूस होना।
- तेज बुखार या पेट में तेज दर्द।
            """,
            "kn": """
### ಗರ್ಭಿಣಿಯರಲ್ಲಿ ಅಪಾಯದ ಲಕ್ಷಣಗಳು:
- ರಕ್ತಸ್ರಾವ ಕಂಡುಬಂದರೆ.
- ತೀವ್ರ ತಲೆನೋವು ಮತ್ತು ಕಣ್ಣು ಮಂಜಾಗುವುದು.
- ಮಗುವಿನ ಚಲನೆ ಕಡಿಮೆಯಾದರೆ.
ತಕ್ಷಣ ವೈದ್ಯರನ್ನು ಸಂಪರ್ಕಿಸಿ.
            """
        },
        "questions_for_doctor": [
            "What is my expected due date and blood hemoglobin level?",
            "Are all my required vaccinations (Td/Flu) up to date?",
            "What warning signs should prompt me to go directly to the labor ward?",
            "Are there any ultrasound scans scheduled for this trimester?"
        ],
        "trusted_sources": ["mohfw", "icmr", "who", "nhp"]
    },
    {
        "id": "anemia",
        "category": "Nutrition & Blood Health",
        "keywords": ["anemia", "iron deficiency", "hemoglobin", "low blood", "fatigue", "pale skin", "एनीमिया", "खून की कमी", "हीमोग्लोबिन", "ಅನೇಮಿಯಾ", "ರಕ್ತಹೀನತೆ"],
        "title": {
            "en": "Anemia Awareness & Iron Rich Nutrition",
            "hi": "एनीमिया (खून की कमी) और पोषण",
            "kn": "ರಕ್ತಹೀನತೆ (Anemia) ಮತ್ತು ಪೋಷಕಾಂಶಗಳು"
        },
        "is_translated": {
            "en": True,
            "hi": True,
            "kn": True
        },
        "simple": {
            "en": """
- **What is Anemia**: It is a condition where the red blood cells or hemoglobin level in the blood is lower than normal.
- **Common Symptoms**: Constant weakness, quick tiredness, pale skin or inner eyelids, dizziness, shortness of breath on mild exertion.
- **Prevention & Relief**:
  1. Eat iron-rich foods: spinach, amaranth, jaggery, sesame seeds, lentils, beans, and meat/eggs.
  2. Pair iron foods with Vitamin C (lemons, amla, oranges) for better iron absorption.
  3. Avoid drinking tea or coffee immediately after meals, as it reduces iron absorption.
  4. Take Iron-Folic Acid (IFA) supplements as prescribed by healthcare workers.
            """,
            "hi": """
- **एनीमिया क्या है**: जब शरीर के खून में हीमोग्लोबिन या लाल रक्त कोशिकाओं का स्तर कम हो जाता है।
- **मुख्य लक्षण**: लगातार थकान, कमजोरी, पीली त्वचा या पलकों के अंदर पीलापन, चक्कर आना।
- **बचाव और उपाय**:
  1. आयरन से भरपूर खाना खाएं: पालक, मेथी, गुड़, तिल, दालें, और अंकुरित अनाज।
  2. विटामिन C युक्त चीजें (नींबू, आंवला, संतरा) खाएं क्योंकि यह आयरन सोखने में मदद करता है।
  3. खाने के तुरंत बाद चाय या कॉफी न पिएं।
  4. एएनएम या डॉक्टर द्वारा दी गई आयरन की गोलियां नियमित लें।
            """,
            "kn": """
- **ರಕ್ತಹೀನತೆ ಎಂದರೇನು**: ರಕ್ತದಲ್ಲಿ ಹಿಮೋಗ್ಲೋಬಿನ್ ಪ್ರಮಾಣ ಕಡಿಮೆಯಾಗುವುದು.
- **ಲಕ್ಷಣಗಳು**: ತೀವ್ರ ಸುಸ್ತು, ಆಯಾಸ, ಬಿಳಿಚಿಕೊಂಡ ಮೈಬಣ್ಣ, ತಲೆಸುತ್ತು.
- **ಪರಿಹಾರಗಳು**:
  1. ಕಬ್ಬಿಣಾಂಶವಿರುವ ಆಹಾರ ಸೇವಿಸಿ: ಸೊಪ್ಪು, ಬೆಲ್ಲ, ಧಾನ್ಯಗಳು.
  2. ನಿಂಬೆಹಣ್ಣು, ನೆಲ್ಲಿಕಾಯಿ (ವಿಟಮಿನ್ ಸಿ) ಸೇವಿಸಿ.
  3. ಊಟದ ತಕ್ಷಣ ಟೀ ಅಥವಾ ಕಾಫಿ ಕುಡಿಯಬೇಡಿ.
            """
        },
        "standard": {
            "en": """
### Clinical Standards for Anemia (Anemia Mukt Bharat Guidelines)
Hemoglobin diagnostic cutoffs vary by demographic group:
- Non-pregnant women (15-49 yrs): Hb < 12.0 g/dL
- Pregnant women: Hb < 11.0 g/dL
- Children (6-59 months): Hb < 11.0 g/dL
- Men: Hb < 13.0 g/dL

#### Anemia Management Pillars
- **Prophylactic Supplementation**: Weekly/daily IFA tablets depending on age and physiological stage.
- **Deworming**: Bi-annual administration of Albendazole to combat intestinal helminth infections causing occult blood loss.
- **Dietary Diversification**: Fortified salt (double fortified salt with iron and iodine) and biofortified crops.
            """,
            "hi": """
### एनीमिया मुक्त भारत दिशानिर्देश
हीमोग्लोबिन की सामान्य सीमा:
- महिलाएं: 12.0 g/dL से अधिक
- गर्भवती महिलाएं: 11.0 g/dL से अधिक
- पुरुष: 13.0 g/dL से अधिक

#### मुख्य उपाय
- नियमित रूप से डीवॉर्मिंग (पेट के कीड़े मारने की दवा एल्बेंडाजोल) लें।
- फोर्टिफाइड खाद्य पदार्थ और आयरन युक्त आहार अपनाएं।
            """,
            "kn": """
### ರಕ್ತಹೀನತೆ ತಡೆಗಟ್ಟುವಿಕೆ (Anemia Mukt Bharat)
ಹಿಮೋಗ್ಲೋಬಿನ್ ಪರೀಕ್ಷೆ ಮಾಡಿಸಿಕೊಂಡು ಅಗತ್ಯವಿದ್ದರೆ ಕಬ್ಬಿಣಾಂಶದ ಮಾತ್ರೆಗಳನ್ನು ವೈದ್ಯರ ಸಲಹೆಯಂತೆ ತೆಗೆದುಕೊಳ್ಳಿ.
            """
        },
        "questions_for_doctor": [
            "What is my exact hemoglobin level?",
            "Do I need therapeutic iron dosages or prophylactic supplements?",
            "Are there underlying causes like gut bleeding or heavy menstrual flow?",
            "When should I get a follow-up complete blood count (CBC) test?"
        ],
        "trusted_sources": ["mohfw", "icmr", "who", "nhp"]
    },
    {
        "id": "dengue_fever",
        "category": "Infectious Diseases",
        "keywords": ["dengue", "mosquito", "platelets", "fever", "joint pain", "vector borne", "डेंगू", "बुखार", "प्लेटलेट्स", "ಡೆಂಗ್ಯೂ", "ಜ್ವರ"],
        "title": {
            "en": "Dengue Fever Care & Warning Signs",
            "hi": "डेंगू बुखार: लक्षण, देखभाल और सावधानियां",
            "kn": "ಡೆಂಗ್ಯೂ ಜ್ವರದ ಲಕ್ಷಣಗಳು ಮತ್ತು ಜಾಗೃತಿ"
        },
        "is_translated": {
            "en": True,
            "hi": True,
            "kn": True
        },
        "simple": {
            "en": """
- **What is Dengue**: A viral infection transmitted by the bite of infected Aedes mosquitoes.
- **Key Symptoms**: Sudden high fever, severe headache, pain behind eyes, muscle and joint pain ('breakbone fever'), skin rash.
- **First-Aid & Home Care**:
  1. Drink plenty of clean water, ORS solution, coconut water, or clear soups to prevent dehydration.
  2. Take adequate rest.
  3. Use Paracetamol for fever if advised. **Avoid Aspirin, Ibuprofen, or Painkillers** as they increase bleeding risks.
  4. Use mosquito nets and repellents to prevent further bites.
            """,
            "hi": """
- **डेंगू क्या है**: यह एडीज मच्छर के काटने से फैलने वाला वायरल संक्रमण है।
- **मुख्य लक्षण**: तेज बुखार, सिरदर्द, आंखों के पीछे दर्द, जोड़ों और मांसपेशियों में दर्द, त्वचा पर चकत्ते।
- **घर पर देखभाल**:
  1. प्रचुर मात्रा में तरल पदार्थ पीएं (पानी, ओआरएस, नारियल पानी, सूप)।
  2. पूरा आराम करें।
  3. बुखार के लिए केवल पैरासिटामोल का प्रयोग करें। **एस्पिरिन या कॉम्बिफ्लेम/इबूप्रोफेन का प्रयोग न करें** क्योंकि इनसे ब्लीडिंग का खतरा बढ़ता है।
  4. मच्छरदानी और मच्छर भगाने वाले साधनों का प्रयोग करें।
            """,
            "kn": """
- **ಡೆಂಗ್ಯೂ ಎಂದರೇನು**: ಈಡಿಸ್ ಸೊಳ್ಳೆಯಿಂದ ಹರಡುವ ವೈರಲ್ ಜ್ವರ.
- **ಲಕ್ಷಣಗಳು**: ತೀವ್ರ ಜ್ವರ, ತಲೆನೋವು, ಕಣ್ಣಿನ ಹಿಂಭಾಗದಲ್ಲಿ ನೋವು, ಗಂಟು ನೋವು.
- **ಸರಳ ಪರಿಹಾರಗಳು**:
  1. ಹೆಚ್ಚು ನೀರು, ORS ಮತ್ತು ಎಳನೀರು ಕುಡಿಯಿರಿ.
  2. ಪ್ಯಾರಸಿಟಮಾಲ್ ಬಳಸಿ. **ಆಸ್ಪಿರಿನ್ ಅಥವಾ ಐಬುಪ್ರೊಫೇನ್ ಬಳಸಬೇಡಿ**.
  3. ಸೊಳ್ಳೆ ಪರದೆಗಳನ್ನು ಬಳಸಿ.
            """
        },
        "standard": {
            "en": """
### Dengue Clinical Management Guidelines (NVBDCP / WHO)
Dengue severity can progress rapidly after the initial febrile phase (days 3–7).

#### Critical Warning Signs (Seek Emergency Admission Immediately)
- Severe abdominal pain or continuous vomiting.
- Bleeding from nose or gums, or blood in vomit/stool.
- Extreme drowsiness, restlessness, or confusion.
- Rapid drop in blood platelet count with fluid accumulation (ascites/pleural effusion).

#### Key Precautions
- Platelet transfusion is generally reserved for severe clinical bleeding or extreme drop (<10,000/mcL); do not panic solely over moderate platelet counts. Maintain oral/IV hydration.
            """,
            "hi": """
### गंभीर डेंगू के चेतावनी संकेत (तुरंत अस्पताल जाएं)
- पेट में तेज दर्द या लगातार उल्टी होना।
- नाक या मसूड़ों से खून आना।
- बहुत ज्यादा सुस्ती, घबराहट या होश खोना।
- बिना डॉक्टर की सलाह के कोई एंटीबायोटिक या पेनकिलर न लें।
            """,
            "kn": """
### ಡೆಂಗ್ಯೂ ತೀವ್ರ ಎಚ್ಚರಿಕೆ ಲಕ್ಷಣಗಳು:
- ತೀವ್ರ ಹೊಟ್ಟೆ ನೋವು ಅಥವಾ ವಾಂತಿ.
- ಮೂಗು ಅಥವಾ ಒಸಡಿನಿಂದ ರಕ್ತಸ್ರಾವ.
ತಕ್ಷಣವೇ ತುರ್ತು ಆಸ್ಪತ್ರೆಗೆ ಭೇಟಿ ನೀಡಿ.
            """
        },
        "questions_for_doctor": [
            "What is my blood platelet count and hematocrit value?",
            "Are there any warning signs that indicate I need hospital admission?",
            "How frequently should I repeat the complete blood count (CBC) test?",
            "Is my fluid intake sufficient?"
        ],
        "trusted_sources": ["mohfw", "icmr", "who", "nhp"]
    },
    {
        "id": "respiratory_asthma",
        "category": "Respiratory Health",
        "keywords": ["asthma", "cough", "breathlessness", "wheezing", "pollution", "inhaler", "अस्थमा", "खांसी", "दमा", "सांस", "ಆಸ್ತಮಾ", "ಕೆಮ್ಮು"],
        "title": {
            "en": "Respiratory Hygiene & Asthma Management",
            "hi": "श्वसन स्वास्थ्य एवं अस्थमा देखभाल",
            "kn": "ಉಸಿರಾಟದ ಆರೋಗ್ಯ ಮತ್ತು ಆಸ್ತಮಾ ಜಾಗೃತಿ"
        },
        "is_translated": {
            "en": True,
            "hi": True,
            "kn": True
        },
        "simple": {
            "en": """
- **Overview**: Asthma causes swelling and narrowing of airways, leading to wheezing, chest tightness, and coughing.
- **Everyday Hygiene & Care**:
  1. Avoid known triggers: dust, smoke, incense sticks, strong sprays, cold dry air.
  2. Use prescribed inhalers regularly as advised. Inhalers deliver medicine directly to lungs with minimal side effects.
  3. Cover your mouth and nose with a tissue or elbow when coughing or sneezing.
  4. Wear an N95 mask outdoors during days with severe air pollution (AQI).
            """,
            "hi": """
- **विवरण**: अस्थमा सांस की नालियों की सूजन के कारण होता है, जिससे सांस लेने में सीटी की आवाज (wheezing) और खांसी होती है।
- **रोजमर्रा की सावधानियां**:
  1. धुएं, धूल, अगरबत्ती, और ठंडी हवा जैसे ट्रिगर्स से बचें।
  2. डॉक्टर द्वारा दिया गया इनहेलर (Inhaler) नियमित लें। इनहेलर दवा को सीधे फेफड़ों तक पहुंचाता है।
  3. खांसते या छींकते समय मुंह पर रुमाल या कोहनी रखें।
  4. प्रदूषण के दिनों में बाहर निकलते समय मास्क पहनें।
            """,
            "kn": """
- **ಆಸ್ತಮಾ ಎಂದರೇನು**: ಉಸಿರಾಟದ ನಳಿಕೆಗಳು ಕಿರಿದಾಗುವುದರಿಂದ ಉಸಿರಾಟದ ತೊಂದರೆ ಉಂಟಾಗುತ್ತದೆ.
- **ಮುನ್ನೆಚ್ಚರಿಕೆಗಳು**:
  1. ಧೂಳು, ಹೊಗೆಯಿಂದ ದೂರವಿರಿ.
  2. ವೈದ್ಯರು ನೀಡಿದ ಇನ್ಹೇಲರ್ (Inhaler) ಸರಿಯಾಗಿ ಬಳಸಿ.
  3. ಕೆಮ್ಮುವಾಗ ಬಾಯಿ ಮುಚ್ಚಿಕೊಳ್ಳಿ.
            """
        },
        "standard": {
            "en": """
### Asthma Management Strategy (GINA Guidelines)
Inhaled corticosteroids (ICS) combined with long-acting beta-agonists are the foundation of modern asthma management.

#### Proper Inhaler Technique
- Use a spacer device, especially for children and elderly, to maximize lung deposition and prevent oral thrush.
- Rinse mouth with water and spit after using corticosteroid inhalers.

#### Red-Flag Respiratory Distress
If severe shortness of breath prevents speaking full sentences, or if fingertips turn blue, administer rescue inhaler and seek emergency emergency medical care immediately.
            """,
            "hi": """
### अस्थमा और श्वसन संबंधी निर्देश
- इनहेलर के सही इस्तेमाल के लिए स्पेसर (Spacer) का प्रयोग करें।
- स्टेरॉयड इनहेलर के इस्तेमाल के बाद पानी से गरारा करें।
- यदि सांस इतनी फूले कि एक वाक्य बोलना मुश्किल हो जाए, तो तुरंत आपातकालीन चिकित्सा लें।
            """,
            "kn": """
### ಉಸಿರಾಟದ ತೊಂದರೆಯ ಅಪಾಯದ ಸೂಚನೆ:
ಮಾತನಾಡಲು ಸಾಧ್ಯವಾಗದಷ್ಟು ಉಸಿರಾಟದ ತೊಂದರೆಯಿದ್ದರೆ ತಕ್ಷಣ ಆಸ್ಪತ್ರೆಗೆ ಭೇಟಿ ನೀಡಿ.
            """
        },
        "questions_for_doctor": [
            "Am I using my inhaler device with correct technique?",
            "What is the difference between my daily controller inhaler and emergency rescue inhaler?",
            "Do I have a written Asthma Action Plan for symptom flare-ups?",
            "Should I take an annual influenza (flu) vaccine?"
        ],
        "trusted_sources": ["who", "nhs", "icmr"]
    },
    {
        "id": "ors_dehydration",
        "category": "First Aid & Hygiene",
        "keywords": ["ors", "dehydration", "diarrhea", "vomiting", "heatstroke", "oral rehydration", "दस्त", "उल्टी", "ओआरएस", "निर्जलीकरण", "ಭೇದಿ", "ವಾಂತಿ"],
        "title": {
            "en": "ORS & Dehydration First Aid",
            "hi": "ओआरएस (ORS) और डिहाइड्रेशन प्राथमिक चिकित्सा",
            "kn": "ORS ಮತ್ತು ನಿರ್ಜಲೀಕರಣ ಪ್ರಥಮ ಚಿಕಿತ್ಸೆ"
        },
        "is_translated": {
            "en": True,
            "hi": True,
            "kn": True
        },
        "simple": {
            "en": """
- **What is Dehydration**: Excessive loss of body fluids due to diarrhea, vomiting, sweating, or heatstroke.
- **Signs of Dehydration**: Dry mouth, dark yellow urine, sunken eyes, extreme thirst, lethargy.
- **How to Prepare WHO-Formula ORS**:
  1. Clean hands thoroughly with soap and water.
  2. Mix 1 full packet of ORS in **1 liter of clean drinking water**.
  3. Stir well until completely dissolved.
  4. Sip continuously throughout the day. Discard any unused liquid after 24 hours.
- **Home Solution (If ORS Packet Unavailable)**: Mix 6 level teaspoons of sugar and 1/2 level teaspoon of salt in 1 liter of safe drinking water.
            """,
            "hi": """
- **डिहाइड्रेशन क्या है**: दस्त, उल्टी या तेज धूप के कारण शरीर से पानी और लवण (salt) का अत्यधिक कम हो जाना।
- **लक्षण**: सूखा मुंह, गहरा पीला पेशाब, धंसी हुई आंखें, अत्यधिक प्यास, सुस्ती।
- **ओआरएस (ORS) बनाने की विधि**:
  1. हाथ साबुन से धोएं।
  2. ORS का 1 पैकेट **1 लीटर साफ पीने के पानी** में घोलें।
  3. अच्छी तरह मिलाएं। 24 घंटे के बाद बचा हुआ घोल फेंक दें और नया बनाएं।
- **घरेलू उपाय (यदि ORS पैकेट न हो)**: 1 लीटर पानी में 6 छोटी चम्मच चीनी और 1/2 छोटी चम्मच नमक अच्छी तरह मिलाएं।
            """,
            "kn": """
- **ನಿರ್ಜಲೀಕರಣ ಎಂದರೇನು**: ಭೇದಿ, ವಾಂತಿಯಿಂದ ದೇಹದಲ್ಲಿ ನೀರು ಕಡಿಮೆಯಾಗುವುದು.
- **ORS ತಯಾರಿಸುವ ವಿಧಾನ**:
  1. 1 ಲೀಟರ್ ಶುದ್ಧ ನೀರಿಗೆ 1 ORS ಪ್ಯಾಕೆಟ್ ಸೇರಿಸಿ.
  2. ಚೆನ್ನಾಗಿ ಕಲಸಿ ದಿನವಿಡೀ ಕುಡಿಯಿರಿ. 24 ಗಂಟೆಗಳ ನಂತರ ಹೊಸದು ಮಾಡಿ.
            """
        },
        "standard": {
            "en": """
### Clinical Management of Diarrhea & Dehydration (WHO Standards)
Low-osmolarity Oral Rehydration Salts (ORS) reduce stool volume and need for intravenous therapy.

#### Key Principles
- **Zinc Supplementation**: For children with diarrhea, WHO recommends Zinc supplementation (20 mg/day for 14 days) to shorten episode duration.
- **Continued Feeding**: Never stop breastfeeding or regular nutritious food during acute diarrhea.
- **When to Seek Hospitalization**: Blood in stool, high persistent fever, severe lethargy, or inability to keep fluids down.
            """,
            "hi": """
### दस्त और निर्जलीकरण प्रबंधन (WHO)
- बच्चों में दस्त के दौरान 14 दिनों तक जिंक (Zinc) की गोली अवश्य दें।
- दस्त के दौरान बच्चे का स्तनपान या खाना बंद न करें।
- यदि मल में खून आए या लगातार उल्टी हो तो तुरंत डॉक्टर को दिखाएं।
            """,
            "kn": """
### ವೈದ್ಯರ ಸಲಹೆ:
ಮಗುವಿಗೆ ಭೇದಿಯಿದ್ದರೆ ORS ಜೊತೆಗೆ ಜಿಂಕ್ (Zinc) ನೀಡಿ.
            """
        },
        "questions_for_doctor": [
            "Does this diarrhea require antibiotics or only oral rehydration?",
            "Should I give zinc supplements to my child?",
            "What signs indicate that intravenous (IV) fluids are necessary?"
        ],
        "trusted_sources": ["who", "mohfw", "cdc"]
    },
    {
        "id": "mental_wellness",
        "category": "Mental Health",
        "keywords": ["mental health", "stress", "anxiety", "depression", "sleep", "mindfulness", "तनाव", "मानसिक स्वास्थ्य", "चिंता", "निद्रा", "ಮಾನಸಿಕ ಆರೋಗ್ಯ", "ಒತ್ತಡ"],
        "title": {
            "en": "Mental Wellness & Stress Coping Strategies",
            "hi": "मानसिक स्वास्थ्य और तनाव प्रबंधन",
            "kn": "ಮಾನಸಿಕ ಆರೋಗ್ಯ ಮತ್ತು ಒತ್ತಡ ನಿರ್ವಹಣೆ"
        },
        "is_translated": {
            "en": True,
            "hi": True,
            "kn": True
        },
        "simple": {
            "en": """
- **Understanding Mental Health**: Mental well-being is as important as physical health. Feeling stressed, anxious, or down occasionally happens to everyone.
- **Practical Wellness Habits**:
  1. Maintain a daily routine with consistent sleep (7-8 hours).
  2. Talk to family members, trusted friends, or community counselors.
  3. Practice 10 minutes of deep belly breathing or quiet meditation daily.
  4. Limit late-night screen exposure before sleep.
- **Urgent Support**: If experiencing overwhelming hopelessness or suicidal thoughts, call Tele-MANAS helpline at **14416** or **1800-891-4416** (India, Free 24/7).
            """,
            "hi": """
- **मानसिक स्वास्थ्य का महत्व**: मानसिक स्वास्थ्य भी शारीरिक स्वास्थ्य जितना ही महत्वपूर्ण है।
- **सरल आदतें**:
  1. रोज 7-8 घंटे की पर्याप्त नींद लें।
  2. परिवार या दोस्तों से खुलकर बात करें।
  3. प्रतिदिन 10 मिनट ध्यान (Meditation) या गहरी सांस लेने का अभ्यास करें।
  4. रात को सोने से पहले मोबाइल स्क्रीन का इस्तेमाल कम करें।
- **हेल्पलाइन**: किसी भी मानसिक संकट या उदासी की स्थिति में भारत सरकार की टेली-मानस (Tele-MANAS) हेल्पलाइन **14416** या **1800-891-4416** पर मुफ्त कॉल करें।
            """,
            "kn": """
- **ಮಾನಸಿಕ ಆರೋಗ್ಯ**: ದೈಹಿಕ ಆರೋಗ್ಯದಷ್ಟೇ ಮಾನಸಿಕ ಆರೋಗ್ಯವೂ ಮುಖ್ಯ.
- **ಅಭ್ಯಾಸಗಳು**:
  1. 7-8 ಗಂಟೆಗಳ ನಿದ್ರೆ ಮಾಡಿ.
  2. ಕುಟುಂಬದವರೊಂದಿಗೆ ಮುಕ್ತವಾಗಿ ಮಾತನಾಡಿ.
  3. ದಿನವೂ 10 ನಿಮಿಷ ಧ್ಯಾನ ಮಾಡಿ.
- **ಸಹಾಯವಾಣಿ**: ಟೆಲಿ-ಮಾನಸ್ (Tele-MANAS) ಉಚಿತ ಸಹಾಯವಾಣಿ **14416** ಗೆ ಕರೆ ಮಾಡಿ.
            """
        },
        "standard": {
            "en": """
### Evidence-Based Stress Coping & Mental Health Awareness
Persistent anxiety, low mood lasting over 2 weeks, or disruption in daily functioning warrant professional evaluation by a psychiatrist or clinical psychologist.

#### Tele-MANAS Infrastructure (Govt of India)
National Tele-Mental Health Programme providing free, confidential round-the-clock counseling services in regional languages across India.
            """,
            "hi": """
### टेली-मानस (Tele-MANAS) राष्ट्रीय सेवा
भारत सरकार द्वारा 24x7 मुफ्त क्षेत्रीय भाषाओं में मानसिक स्वास्थ्य परामर्श सेवा।
            """,
            "kn": """
### ಟೆಲಿ-ಮಾನಸ್ ಸೇವೆಯನ್ನು ಉಚಿತವಾಗಿ ಪಡೆಯಿರಿ: 14416
            """
        },
        "questions_for_doctor": [
            "Are my physical symptoms (palpitations, fatigue) related to anxiety?",
            "Would counseling or cognitive behavioral therapy be suitable for me?",
            "What lifestyle adjustments can improve my sleep quality?"
        ],
        "trusted_sources": ["mohfw", "who", "nhp"]
    }
]
