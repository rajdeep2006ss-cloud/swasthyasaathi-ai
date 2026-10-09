"""
Automated Test Suite for SwasthyaSaathi AI
Tests query matching, reading levels, multilingual fallback, emergency alerts,
doctor checklist generation, privacy compliance, and source links.
"""

import pytest
from assistant import (
    search_knowledge_base,
    check_emergency_triggers,
    generate_doctor_checklist,
    sanitize_user_input
)
from knowledge_base import (
    HEALTH_TOPICS,
    EMERGENCY_TRIGGERS,
    TRUSTED_SOURCES
)

# ==========================================
# 1. EMERGENCY WARNING TEST SUITE
# ==========================================
def test_emergency_warning_behavior_english():
    """Verify urgent red-flag queries trigger emergency warnings in English."""
    urgent_queries = [
        "I am having severe chest pain",
        "My relative is unconscious and fainted",
        "He has sudden facial drooping and slurred speech",
        "Shortness of breath and difficulty breathing"
    ]
    for q in urgent_queries:
        result = check_emergency_triggers(q, language="en")
        assert result is not None, f"Failed to trigger emergency alert for query: '{q}'"
        assert result["is_emergency"] is True
        assert len(result["steps"]) > 0
        assert "108" in str(result["steps"]) or "112" in str(result["steps"])

def test_emergency_warning_behavior_hindi():
    """Verify urgent red-flag queries trigger emergency warnings in Hindi."""
    urgent_queries = [
        "सीने में दर्द हो रहा है",
        "सांस लेने में तकलीफ है",
        "अचानक बेहोश हो गया"
    ]
    for q in urgent_queries:
        result = check_emergency_triggers(q, language="hi")
        assert result is not None, f"Failed emergency alert for Hindi query: '{q}'"
        assert result["is_emergency"] is True

def test_emergency_warning_in_knowledge_search():
    """Verify search_knowledge_base detects emergency triggers immediately."""
    res = search_knowledge_base("I feel severe chest pain", language="en")
    assert res["is_emergency"] is True
    assert res["emergency_data"]["matched_keyword"] == "chest pain"

# ==========================================
# 2. SUPPORTED TOPICS & READING LEVELS TEST
# ==========================================
def test_supported_topics_diabetes_retrieval():
    """Verify retrieval of Diabetes topic across reading levels."""
    # Simple reading level
    res_simple = search_knowledge_base("how to manage blood sugar", reading_level="simple", language="en")
    assert res_simple["matched"] is True
    assert res_simple["topic_id"] == "diabetes_type2"
    assert res_simple["reading_level"] == "simple"
    assert "What it is" in res_simple["content"] or "Type 2" in res_simple["content"]

    # Standard reading level
    res_standard = search_knowledge_base("diabetes HbA1c target", reading_level="standard", language="en")
    assert res_standard["matched"] is True
    assert res_standard["topic_id"] == "diabetes_type2"
    assert res_standard["reading_level"] == "standard"
    assert "HbA1c" in res_standard["content"]

def test_multilingual_topic_retrieval_hindi():
    """Verify retrieval of Hypertension topic in Hindi."""
    res = search_knowledge_base("उच्च रक्तचाप के लक्षण", reading_level="simple", language="hi")
    assert res["matched"] is True
    assert res["topic_id"] == "hypertension"
    assert res["language"] == "hi"

def test_multilingual_topic_retrieval_kannada():
    """Verify retrieval of Dengue topic in Kannada."""
    res = search_knowledge_base("ಡೆಂಗ್ಯೂ", reading_level="simple", language="kn")
    assert res["matched"] is True
    assert res["topic_id"] == "dengue_fever"

# ==========================================
# 3. UNSUPPORTED / OUT-OF-SCOPE QUESTIONS
# ==========================================
def test_unsupported_questions_fallback():
    """Verify out-of-scope questions return friendly fallback without hallucinating."""
    out_of_scope_queries = [
        "How to fix a broken car engine?",
        "What is the stock market price of Apple?",
        "Quantum computing physics explanation"
    ]
    for q in out_of_scope_queries:
        res = search_knowledge_base(q, language="en")
        assert res["is_emergency"] is False
        assert res["matched"] is False
        assert "could not find an exact match" in res["message"].lower() or "curated local health library" in res["message"].lower()
        assert len(res["suggested_topics"]) > 0

# ==========================================
# 4. APPOINTMENT PREPARATION TOOL TEST
# ==========================================
def test_doctor_checklist_generation():
    """Verify doctor checklist creation with custom symptoms and duration."""
    checklist = generate_doctor_checklist(
        topic_id="hypertension",
        symptoms="morning headache and dizziness",
        duration="3 weeks",
        language="en"
    )
    assert checklist["topic_title"] is not None
    assert len(checklist["questions"]) >= 4
    assert any("morning headache and dizziness" in q for q in checklist["questions"])
    assert any("3 weeks" in q for q in checklist["questions"])

# ==========================================
# 5. PRIVACY COMPLIANCE & PII SANITIZATION
# ==========================================
def test_privacy_sanitization():
    """Verify PII (phone numbers, emails) are stripped before processing."""
    raw_input = "My phone number is 9876543210 and my email is testuser@example.com having high sugar"
    clean = sanitize_user_input(raw_input)
    assert "9876543210" not in clean
    assert "testuser@example.com" not in clean
    assert "[REDACTED_NUMBER]" in clean
    assert "[REDACTED_EMAIL]" in clean

# ==========================================
# 6. GENUINE SOURCE LINKS TEST
# ==========================================
def test_trusted_source_links():
    """Verify all trusted sources use valid HTTPS URLs from official health domains."""
    for key, source in TRUSTED_SOURCES.items():
        url = source["url"]
        assert url.startswith("https://"), f"Source {key} URL is not secure: {url}"
        assert any(domain in url for domain in [
            "mohfw.gov.in", "icmr.gov.in", "who.int", "nhp.gov.in", "nhs.uk", "cdc.gov"
        ]), f"Source {key} domain is unverified: {url}"

# ==========================================
# 7. DASHBOARD STATS & HELPER FUNCTION TESTS
# ==========================================
from assistant import (
    get_knowledge_base_stats,
    get_featured_health_tip,
    get_app_overview_metrics,
    get_theme_config
)

def test_knowledge_base_stats_derivation():
    """Verify get_knowledge_base_stats derives accurate counts from real HEALTH_TOPICS metadata."""
    stats = get_knowledge_base_stats()
    assert stats["total_topics"] == len(HEALTH_TOPICS)
    assert "categories" in stats
    assert len(stats["categories"]) > 0
    assert "sources" in stats
    assert len(stats["sources"]) > 0
    assert stats["languages"]["English"] == len(HEALTH_TOPICS)

def test_knowledge_base_stats_empty_fallback():
    """Verify graceful handling of empty or malformed inputs for dashboard stats."""
    empty_stats = get_knowledge_base_stats(topics=[], sources={})
    assert empty_stats["total_topics"] == 0
    assert empty_stats["categories"] == {}
    assert empty_stats["sources"] == {}

def test_featured_health_tip():
    """Verify get_featured_health_tip returns a valid educational tip from curated data."""
    tip = get_featured_health_tip(language="en")
    assert tip is not None
    assert "title" in tip
    assert "content" in tip
    assert "source_name" in tip
    assert len(tip["content"]) > 10

def test_app_overview_metrics():
    """Verify system overview metrics are accurately derived from knowledge base."""
    metrics = get_app_overview_metrics()
    assert metrics["total_topics"] == len(HEALTH_TOPICS)
    assert metrics["total_sources"] == len(TRUSTED_SOURCES)
    assert metrics["total_languages"] == 3
    assert metrics["total_emergency_lines"] == 4

def test_theme_config_helper():
    """Verify get_theme_config returns valid settings for Light, Dark, and System Default."""
    light_cfg = get_theme_config("Light")
    assert light_cfg["plotly_template"] == "plotly_white"
    assert len(light_cfg["palette"]) > 0

    dark_cfg = get_theme_config("Dark")
    assert dark_cfg["plotly_template"] == "plotly_dark"
    assert dark_cfg["mode"] == "dark"

    sys_cfg = get_theme_config("System Default")
    assert sys_cfg["name"] == "System Default"


