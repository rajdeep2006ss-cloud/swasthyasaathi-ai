"""
SwasthyaSaathi AI - Core Logic & Query Engine
Handles keyword-based knowledge search, red-flag emergency detection,
doctor question list generation, and PII protection.
"""

import re
from knowledge_base import (
    HEALTH_TOPICS,
    EMERGENCY_TRIGGERS,
    UI_TRANSLATIONS,
    TRUSTED_SOURCES
)

def sanitize_user_input(text: str) -> str:
    """
    Strips potential PII (like 10-digit phone numbers, email addresses, or 12-digit Aadhaar numbers)
    to enforce privacy compliance.
    """
    if not text:
        return ""
    # Strip emails
    text = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '[REDACTED_EMAIL]', text)
    # Strip 10-digit or 12-digit numbers
    text = re.sub(r'\b\d{10}\b|\b\d{12}\b|\b\d{4}\s\d{4}\s\d{4}\b', '[REDACTED_NUMBER]', text)
    return text.strip()

def check_emergency_triggers(query: str, language: str = "en") -> dict:
    """
    Checks if query contains any emergency red-flag keywords across languages.
    Returns emergency dictionary if trigger is detected, else None.
    """
    if not query:
        return None
    
    clean_q = query.lower()
    
    # Check current selected language triggers first, then fall back to all languages
    langs_to_check = [language] + [l for l in ["en", "hi", "kn"] if l != language]
    
    for lang in langs_to_check:
        trigger_data = EMERGENCY_TRIGGERS.get(lang, EMERGENCY_TRIGGERS["en"])
        for kw in trigger_data["keywords"]:
            if kw.lower() in clean_q:
                return {
                    "is_emergency": True,
                    "matched_keyword": kw,
                    "title": trigger_data["title"],
                    "message": trigger_data["message"],
                    "action": trigger_data["action"],
                    "steps": trigger_data["steps"]
                }
    return None

def search_knowledge_base(query: str, reading_level: str = "simple", language: str = "en") -> dict:
    """
    Searches curated local knowledge base using keyword matching and scoring.
    Returns matched topic data with proper reading level, language translation,
    and untranslated badges if applicable.
    """
    query = sanitize_user_input(query)
    
    # First check emergency
    emergency_alert = check_emergency_triggers(query, language)
    if emergency_alert:
        return {
            "is_emergency": True,
            "emergency_data": emergency_alert,
            "results": []
        }
    
    if not query or len(query.strip()) < 2:
        return {
            "is_emergency": False,
            "matched": False,
            "message": "Please enter a valid health topic or symptom question.",
            "results": []
        }
    
    query_words = set(re.findall(r'\w+', query.lower()))
    
    best_topic = None
    best_score = 0
    
    for topic in HEALTH_TOPICS:
        score = 0
        # Check topic keywords
        for kw in topic["keywords"]:
            kw_lower = kw.lower()
            if kw_lower in query.lower():
                score += 3
            else:
                kw_words = set(re.findall(r'\w+', kw_lower))
                if kw_words and kw_words.issubset(query_words):
                    score += 2
        
        # Check topic titles across languages
        for lang_code in ["en", "hi", "kn"]:
            title_text = topic["title"].get(lang_code, "").lower()
            if any(w in title_text for w in query_words if len(w) > 2):
                score += 1

        if score > best_score:
            best_score = score
            best_topic = topic
            
    # Threshold for matching
    if best_topic and best_score >= 2:
        # Format response based on reading level & language
        lang = language if language in ["en", "hi", "kn"] else "en"
        level = "simple" if reading_level.lower() == "simple" else "standard"
        
        title = best_topic["title"].get(lang) or best_topic["title"]["en"]
        content = best_topic[level].get(lang) or best_topic[level]["en"]
        
        is_untranslated = not best_topic["is_translated"].get(lang, False) or not best_topic[level].get(lang)
        
        # Gather source objects
        sources = [TRUSTED_SOURCES[src_key] for src_key in best_topic.get("trusted_sources", []) if src_key in TRUSTED_SOURCES]
        
        return {
            "is_emergency": False,
            "matched": True,
            "topic_id": best_topic["id"],
            "category": best_topic["category"],
            "title": title,
            "content": content,
            "reading_level": level,
            "language": lang,
            "is_untranslated": is_untranslated,
            "questions_for_doctor": best_topic.get("questions_for_doctor", []),
            "sources": sources
        }

    # Fallback for out-of-scope / unsupported questions
    ui_texts = UI_TRANSLATIONS.get(language, UI_TRANSLATIONS["en"])
    fallback_msg = {
        "en": "I could not find an exact match for your specific search term in our curated local health library. SwasthyaSaathi AI currently covers high-priority topics like Diabetes, Hypertension, Pregnancy Care, Dengue Fever, Anemia, Respiratory Health, ORS/Dehydration First Aid, and Mental Wellness. Please try selecting a category from the Knowledge Library tab or rephrase your question.",
        "hi": "हमार स्थानीय स्वास्थ्य पुस्तकालय में आपकी खोज का सटीक उत्तर नहीं मिला। SwasthyaSaathi AI वर्तमान में मधुमेह, उच्च रक्तचाप, गर्भावस्था देखभाल, डेंगू, एनीमिया, श्वसन स्वास्थ्य, ओआरएस/निर्जलीकरण और मानसिक स्वास्थ्य जैसे विषयों को कवर करता है। कृपया मुख्य पुस्तकालय से विषय चुनें।",
        "kn": "ನಮ್ಮ ಆರೋಗ್ಯ ಗ್ರಂಥಾಲಯದಲ್ಲಿ ಈ ಪ್ರಶ್ನೆಗೆ ನಿಖರವಾದ ವಿಷಯ ದೊರೆತಿಲ್ಲ. ನಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ ಮಧುಮೇಹ, ಅಧಿಕ ರಕ್ತದೊತ್ತಡ, ಗರ್ಭಿಣಿ ಆರೈಕೆ, ಡೆಂಗ್ಯೂ, ರಕ್ತಹೀನತೆ, ಆಸ್ತಮಾ ಹಾಗೂ ಮಾನಸಿಕ ಆರೋಗ್ಯ ವಿಷಯಗಳನ್ನು ಒಳಗೊಂಡಿದೆ."
    }
    
    return {
        "is_emergency": False,
        "matched": False,
        "message": fallback_msg.get(language, fallback_msg["en"]),
        "suggested_topics": [t["title"].get(language, t["title"]["en"]) for t in HEALTH_TOPICS]
    }

def generate_doctor_checklist(topic_id: str, symptoms: str = "", duration: str = "", language: str = "en") -> dict:
    """
    Generates a structured list of questions for doctor appointment preparation.
    """
    symptoms = sanitize_user_input(symptoms)
    duration = sanitize_user_input(duration)
    
    topic = next((t for t in HEALTH_TOPICS if t["id"] == topic_id), HEALTH_TOPICS[0])
    topic_title = topic["title"].get(language, topic["title"]["en"])
    
    base_questions = topic.get("questions_for_doctor", [])
    
    custom_questions = []
    if symptoms:
        custom_questions.append(f"Regarding my symptom ('{symptoms}'): Are there specific diagnostic tests recommended?")
        custom_questions.append(f"Could these symptoms ('{symptoms}') be related to my medication or lifestyle?")
    
    if duration:
        custom_questions.append(f"Since I have experienced this for {duration}, does it require specialist evaluation?")

    all_questions = custom_questions + base_questions
    
    return {
        "topic_title": topic_title,
        "symptoms": symptoms or "Not specified",
        "duration": duration or "Not specified",
        "questions": all_questions
    }
