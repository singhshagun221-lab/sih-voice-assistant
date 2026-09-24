"""
backend/main.py
FastAPI Server for SIH Problem Statement SIH26097: "Voice Assistant for Livelihood"
Under Ministry of Social Justice and Empowerment (MoSJE).

Features:
- CORS middleware for multi-origin access.
- Pydantic models for structured voice payloads and responses.
- Robust NLP Rule-based + Fuzzy Intent Extraction (Hindi, Bhojpuri, Hinglish).
- Mapping Engine for NSQF Skills, PM-AJAY / PM-Vishwakarma Schemes, and Training Centers.
- Empathetic Colloquial Hindi TTS generation (Devanagari script).
- Static file serving for standalone zero-configuration deployment.
"""

import os
import re
import difflib
from typing import Optional, Dict, Any, List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from backend.dataset import (
    NSQF_SKILL_MODULES,
    GOVERNMENT_SCHEMES,
    DISTRICT_TRAINING_CENTERS,
    DEFAULT_FALLBACK_CENTER,
    DISTRICT_ALIASES
)

# ----------------------------------------------------------------------------
# FASTAPI APP SETUP
# ----------------------------------------------------------------------------
app = FastAPI(
    title="MoSJE Voice Assistant for Livelihood (SIH26097)",
    description="Vernacular Voice-First Assistant for Unorganized Artisans & Marginalized Laborers",
    version="1.0.0"
)

# Enable CORS for all origins so Web Speech API and fetch() work without blocking
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------------------------------------------------------
# PYDANTIC DATA MODELS
# ----------------------------------------------------------------------------
class VoiceQueryRequest(BaseModel):
    speech_text: str = Field(
        ...,
        description="Vernacular speech transcript recognized from browser microphone in Hindi/Hinglish",
        examples=["Mera naam Raju hai, main badhai ka kaam karta hoon aur Prayagraj mein rehta hoon"]
    )
    user_district: Optional[str] = Field(
        default=None,
        description="Optional pre-selected or GPS-inferred district name"
    )
    audio_metadata: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Optional client audio metadata (sampleRate, duration, confidence)"
    )


class SkillDetail(BaseModel):
    id: str
    trade_name_en: str
    trade_name_hi: str
    nsqf_level: int
    qp_code: str
    sector_skill_council: str
    duration_hours: int
    daily_stipend_inr: int
    curriculum_highlights: List[str]
    tool_kit_name: str


class SchemeDetail(BaseModel):
    primary_scheme_name: str
    primary_nodal_ministry: str
    equipment_grant_inr: int
    training_subsidy_info: str
    stipend_info: str
    vishwakarma_toolkit_inr: int
    vishwakarma_loan_info: str
    key_benefit_highlight: str
    required_documents: List[str]
    toll_free_helpline: str
    official_portal: str


class CenterDetail(BaseModel):
    district_name_en: str
    district_name_hi: str
    center_name_hi: str
    address_hi: str
    contact_person: str
    helpline_phone: str
    mobile_dial: str
    available_seats: int
    operating_hours: str
    next_batch_date: str
    distance_hint_hi: str


class ProcessVoiceResponse(BaseModel):
    success: bool
    detected_user_name: Optional[str]
    recognized_transcript: str
    detected_trade_key: str
    detected_district_key: str
    nlp_confidence_score: float
    spoken_response_hi: str
    skill: SkillDetail
    scheme: SchemeDetail
    center: CenterDetail


# ----------------------------------------------------------------------------
# NLP & FUZZY INTENT EXTRACTION ENGINE
# ----------------------------------------------------------------------------

COMMON_STOPWORDS = {
    "hai", "hoon", "hun", "ho", "ka", "ki", "ke", "ko", "se", "mein", "me",
    "par", "aur", "ya", "hum", "main", "mera", "meri", "mere", "hamar", "hamara",
    "kaam", "karta", "karti", "karna", "rehta", "rahte", "rehti", "rahila",
    "ba", "baate", "sikhna", "chahiye", "chahta", "chahiti", "ji", "ek", "do"
}

def clean_vernacular_text(raw_text: str) -> str:
    """Normalize input text, retain Devanagari and Latin letters, remove noise."""
    lowered = raw_text.lower()
    cleaned = re.sub(r"[^\w\s\u0900-\u097F]", " ", lowered)
    return re.sub(r"\s+", " ", cleaned).strip()


def extract_user_name(text: str) -> Optional[str]:
    """
    Extract user's name from Hindi / Bhojpuri / Hinglish phrasing.
    Examples:
    - 'Mera naam Raju hai' -> 'Raju'
    - 'हमारा नाम महेश बा' -> 'महेश'
    - 'Main Sunita hoon' -> 'Sunita'
    """
    patterns = [
        r"(?:मेरा नाम|हमार नाम|हमारा नाम|हमार नांव|नाम)\s*(?:hai|ba|bata|hai\s+ki)?\s+([A-Za-z\u0900-\u097F]+)",
        r"(?:mera naam|hamar naam|hamara naam|my name is)\s+([A-Za-z]+)",
        r"(?:main|mai|hum)\s+([A-Za-z\u0900-\u097F]+)\s+(?:hoon|hun|ba|bata)",
    ]

    for pat in patterns:
        match = re.search(pat, text, re.IGNORECASE)
        if match:
            candidate = match.group(1).strip()
            # Ignore false matches like stopwords or occupations
            candidate_lower = candidate.lower()
            if candidate_lower not in COMMON_STOPWORDS and len(candidate) > 1:
                # Do not treat known trades as name
                trade_keys = [
                    "badhai", "darzi", "mistri", "electrician", "mochi", "kumhar",
                    "charmakar", "bunkar", "handloom", "weaver", "leather", "rajmistri",
                    "बढ़ई", "दर्जी", "मिस्त्री", "राजमिस्त्री", "बिजली", "चर्मकार", "बुनकर", "हथकरघा", "मोची"
                ]
                if not any(tk in candidate_lower for tk in trade_keys):
                    return candidate.capitalize()
    return None


def extract_trade_intent(text: str) -> tuple[str, float]:
    """
    NLP Rule + Fuzzy Matcher to identify NSQF skill trade from voice transcript.
    Returns: (trade_key, confidence_score)
    """
    cleaned = clean_vernacular_text(text)
    words = cleaned.split()

    trade_scores: Dict[str, float] = {k: 0.0 for k in NSQF_SKILL_MODULES.keys()}

    # 1. Exact & Substring Keyword Matching
    for trade_key, trade_data in NSQF_SKILL_MODULES.items():
        for kw in trade_data["keywords"]:
            kw_clean = kw.lower().strip()
            # Full phrase match
            if kw_clean in cleaned:
                # Direct mentions of primary trade get high score
                bonus = 1.0 if kw_clean in [trade_key, trade_data["trade_name_hi"]] else 0.8
                trade_scores[trade_key] += bonus

            # Word level match
            for word in words:
                if word == kw_clean:
                    trade_scores[trade_key] += 0.9

    # 2. Fuzzy Matching for ASR / Voice transcription typos (e.g. 'badhaii', 'mistree')
    for word in words:
        if len(word) < 4:
            continue
        for trade_key, trade_data in NSQF_SKILL_MODULES.items():
            for kw in trade_data["keywords"]:
                ratio = difflib.SequenceMatcher(None, word, kw.lower()).ratio()
                if ratio > 0.82:
                    trade_scores[trade_key] += (ratio * 0.75)

    # Find highest scored trade
    best_trade = max(trade_scores, key=trade_scores.get)
    max_score = trade_scores[best_trade]

    if max_score >= 0.8:
        confidence = min(0.98, 0.65 + (max_score * 0.12))
        return best_trade, round(confidence, 2)

    # Default fallback if user spoke generically about tools/work
    if any(term in cleaned for term in ["rozgar", "hunar", "kaam", "training", "काम", "शिल्प", "श्रम"]):
        return "charmakar", 0.70

    # Default safe fallback
    return "charmakar", 0.60


def extract_district_intent(text: str, override_district: Optional[str] = None) -> tuple[str, float]:
    """
    NLP Rule + Fuzzy Matcher to identify district from speech transcript.
    Returns: (district_key, confidence_score)
    """
    if override_district and override_district.strip().lower() in DISTRICT_TRAINING_CENTERS:
        return override_district.strip().lower(), 0.99

    cleaned = clean_vernacular_text(text)
    words = cleaned.split()

    district_scores: Dict[str, float] = {k: 0.0 for k in DISTRICT_TRAINING_CENTERS.keys()}

    for dist_key, aliases in DISTRICT_ALIASES.items():
        for alias in aliases:
            alias_clean = alias.lower()
            if alias_clean in cleaned:
                district_scores[dist_key] += 1.2
            for word in words:
                if word == alias_clean:
                    district_scores[dist_key] += 1.0
                elif len(word) >= 5:
                    ratio = difflib.SequenceMatcher(None, word, alias_clean).ratio()
                    if ratio > 0.85:
                        district_scores[dist_key] += (ratio * 0.8)

    best_district = max(district_scores, key=district_scores.get)
    if district_scores[best_district] >= 0.8:
        return best_district, 0.95

    # Default fallback to Prayagraj (high population center in eastern UP)
    return "prayagraj", 0.65


def construct_empathetic_hindi_speech(
    user_name: Optional[str],
    skill_info: Dict[str, Any],
    scheme_pm_ajay: Dict[str, Any],
    scheme_vishwakarma: Dict[str, Any],
    center_info: Dict[str, Any]
) -> str:
    """
    Construct a warm, colloquial, respectful Hindi script (Devanagari)
    specifically designed for SpeechSynthesis text-to-speech engine.
    Semi-literate workers respond best to clear, polite, reassuring tone.
    """
    greeting = f"नमस्ते {user_name} जी!" if user_name else "नमस्ते भैया!"

    trade_name = skill_info["trade_name_hi"].split("/")[0].strip()
    nsqf_lvl = skill_info["nsqf_level"]
    dist_name = center_info["district_name_hi"].split("(")[0].strip()
    seats = center_info["available_seats"]

    speech = (
        f"{greeting} आपके {trade_name} कार्य के लिए सामाजिक न्याय एवं अधिकारिता मंत्रालय (MoSJE) द्वारा "
        f"पीएम-अजय योजना के सहायता अनुदान (GIA) घटक के तहत ₹50,000 तक का 100% टूलकिट व सूक्ष्म उद्यम अनुदान, "
        f"मुफ्त कौशल प्रशिक्षण और दैनिक स्टाइपेंड दिया जा रहा है। "
        f"साथ ही NSQF लेवल {nsqf_lvl} का सरकारी प्रमाण पत्र मिलेगा। "
        f"आपके {dist_name} कौशल केंद्र पर अभी {seats} सीटें उपलब्ध हैं। "
        f"सीधे संपर्क करने के लिए नीचे दिए गए कॉल बटन को दबाएं!"
    )
    return speech


# ----------------------------------------------------------------------------
# API ENDPOINTS
# ----------------------------------------------------------------------------

@app.get("/api/health")
def healthcheck():
    """Health check endpoint for SIH live evaluation."""
    return {
        "status": "healthy",
        "service": "AI Voice Assistant for Livelihood - PM-AJAY (GIA Component) MoSJE",
        "problem_statement": "SIH26097",
        "supported_trades_count": len(NSQF_SKILL_MODULES),
        "supported_districts_count": len(DISTRICT_TRAINING_CENTERS),
        "active_schemes": ["PM-AJAY (GIA Component)", "PM-Vishwakarma"]
    }


@app.post("/api/process-voice", response_model=ProcessVoiceResponse)
def process_voice_query(request: VoiceQueryRequest):
    """
    Core Voice Processing API:
    1. Extracts User Name, Trade, and District using NLP & Fuzzy matching.
    2. Maps to NSQF level certification standard.
    3. Bundles eligible financial incentives from PM-AJAY (GIA component) and PM-Vishwakarma.
    4. Finds closest localized government training center with seat inventory.
    5. Returns empathetic Devanagari spoken string for instant browser TTS playback.
    """
    raw_transcript = request.speech_text.strip()
    if not raw_transcript:
        raise HTTPException(status_code=400, detail="Voice transcript cannot be empty.")

    # 1. NLP Extraction
    detected_name = extract_user_name(raw_transcript)
    trade_key, trade_conf = extract_trade_intent(raw_transcript)
    dist_key, dist_conf = extract_district_intent(raw_transcript, request.user_district)

    combined_conf = round((trade_conf * 0.6) + (dist_conf * 0.4), 2)

    # 2. Retrieve matched dataset objects
    skill_data = NSQF_SKILL_MODULES.get(trade_key, NSQF_SKILL_MODULES["charmakar"])
    scheme_ajay = GOVERNMENT_SCHEMES["pm_ajay"]
    scheme_vishwa = GOVERNMENT_SCHEMES["pm_vishwakarma"]
    center_data = DISTRICT_TRAINING_CENTERS.get(dist_key, DEFAULT_FALLBACK_CENTER)

    # 3. Generate Colloquial Empathetic Hindi Script
    spoken_hi = construct_empathetic_hindi_speech(
        user_name=detected_name,
        skill_info=skill_data,
        scheme_pm_ajay=scheme_ajay,
        scheme_vishwakarma=scheme_vishwa,
        center_info=center_data
    )

    # 4. Assemble structured response
    skill_resp = SkillDetail(
        id=skill_data["id"],
        trade_name_en=skill_data["trade_name_en"],
        trade_name_hi=skill_data["trade_name_hi"],
        nsqf_level=skill_data["nsqf_level"],
        qp_code=skill_data["qp_code"],
        sector_skill_council=skill_data["sector_skill_council"],
        duration_hours=skill_data["duration_hours"],
        daily_stipend_inr=skill_data["daily_stipend_inr"],
        curriculum_highlights=skill_data["curriculum_highlights"],
        tool_kit_name=skill_data["tool_kit_name"]
    )

    scheme_resp = SchemeDetail(
        primary_scheme_name=scheme_ajay["scheme_name_hi"],
        primary_nodal_ministry=scheme_ajay["nodal_ministry"],
        equipment_grant_inr=scheme_ajay["financial_grant_inr"],
        training_subsidy_info=scheme_ajay["training_subsidy"],
        stipend_info=scheme_ajay["stipend_during_training"],
        vishwakarma_toolkit_inr=scheme_vishwa["financial_grant_inr"],
        vishwakarma_loan_info=scheme_vishwa["collateral_free_credit"],
        key_benefit_highlight="PM-AJAY GIA घटक: ₹50,000 टूलकिट अनुदान + ₹1,500-₹3,000 स्टाइपेंड व 100% मुफ्त NSQF प्रशिक्षण",
        required_documents=scheme_ajay["required_documents_hi"],
        toll_free_helpline=f"{scheme_ajay['toll_free_helpline']} / {scheme_vishwa['toll_free_helpline']}",
        official_portal=scheme_ajay["official_portal"]
    )

    center_resp = CenterDetail(
        district_name_en=center_data["district_name_en"],
        district_name_hi=center_data["district_name_hi"],
        center_name_hi=center_data["center_name_hi"],
        address_hi=center_data["address_hi"],
        contact_person=center_data["contact_person"],
        helpline_phone=center_data["helpline_phone"],
        mobile_dial=center_data["mobile_dial"],
        available_seats=center_data["available_seats"],
        operating_hours=center_data["operating_hours"],
        next_batch_date=center_data["next_batch_date"],
        distance_hint_hi=center_data["distance_hint_hi"]
    )

    return ProcessVoiceResponse(
        success=True,
        detected_user_name=detected_name,
        recognized_transcript=raw_transcript,
        detected_trade_key=trade_key,
        detected_district_key=dist_key,
        nlp_confidence_score=combined_conf,
        spoken_response_hi=spoken_hi,
        skill=skill_resp,
        scheme=scheme_resp,
        center=center_resp
    )


# ----------------------------------------------------------------------------
# SERVE FRONTEND (Single-port self-contained deployment)
# ----------------------------------------------------------------------------
frontend_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "frontend")

if os.path.exists(frontend_dir):
    # Mount frontend directory at root after all /api routes
    app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
