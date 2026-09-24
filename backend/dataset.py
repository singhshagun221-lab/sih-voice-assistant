"""
backend/dataset.py
Production-ready dataset for SIH Problem Statement SIH26097:
"Voice Assistant for Livelihood" - Ministry of Social Justice and Empowerment (MoSJE).

Contains curated NSQF skill qualifications, MoSJE & Central welfare schemes,
and geo-localized district training centers for Uttar Pradesh / North India.
"""

from typing import Dict, List, Any

# ============================================================================
# 1. NSQF SKILL MODULES (National Skills Qualifications Framework)
# ============================================================================

NSQF_SKILL_MODULES: Dict[str, Dict[str, Any]] = {
    "charmakar": {
        "id": "SKILL-CHRM-01",
        "trade_name_en": "Charmakar / Leather Work & Footwear Artisan",
        "trade_name_hi": "चर्मकार / चमड़ा शिल्प व जूता निर्माण (Leather Work / Charmakar)",
        "nsqf_level": 4,
        "qp_code": "LSS/Q2301",
        "sector_skill_council": "Leather Sector Skill Council (LSSC)",
        "duration_hours": 240,
        "daily_stipend_inr": 500,
        "curriculum_highlights": [
            "चमड़ा ग्रेडिंग, सटीक कटिंग, स्टिचिंग व फिनिशिंग तकनीक",
            "आधुनिक फुटवियर, सैंडल, लेदर बैग व बेल्ट निर्माण",
            "इलेक्ट्रिक लेदर सीविंग व सोल पेस्टिंग मशीन का उपयोग",
            "माइक्रो-एंटरप्राइज वर्कशॉप सेटअप, वित्तीय साक्षरता व ऑनलाइन बिक्री"
        ],
        "tool_kit_name": "आधुनिक चर्मकार टूलकिट एवं इलेक्ट्रिक लेदर सिलाई मशीन",
        "keywords": [
            "charmakar", "leather", "leather work", "chamra", "mochi", "joota", "chappal",
            "shoe", "footwear", "charm", "leathercraft", "sandal", "belt", "purse",
            "चर्मकार", "चमड़ा", "मोची", "जूता", "चप्पल", "लेदर", "लेदर वर्क",
            "चर्मशिल्प", "सैंडल", "पॉलिश", "चमड़े का काम", "जूता सिलाई"
        ]
    },
    "handloom": {
        "id": "SKILL-BUNK-02",
        "trade_name_en": "Bunkar / Handloom Weaving & Textile Artisan",
        "trade_name_hi": "बुनकर / हथकरघा बुनाई व वस्त्र शिल्प (Handloom / Bunkar)",
        "nsqf_level": 4,
        "qp_code": "TSC/Q7301",
        "sector_skill_council": "Textile Sector Skill Council (TSC) / Handloom Council",
        "duration_hours": 240,
        "daily_stipend_inr": 500,
        "curriculum_highlights": [
            "पारंपरिक व आधुनिक हथकरघा (Handloom) संचालन व ताना-बाना (Warp & Weft)",
            "सिल्क, कॉटन, खादी एवं बनारसी ब्रोकेड बुनाई तकनीक",
            "जैकार्ड डिजाइनिंग, धागा रंगाई (Dyeing) व प्रिंटिंग",
            "हथकरघा क्लस्टर, स्वयं सहायता समूह (SHG) व ई-मार्केटप्लेस मार्केटिंग"
        ],
        "tool_kit_name": "उन्नत हथकरघा व वीविंग एक्सेसरी टूलकिट (Advanced Handloom Kit)",
        "keywords": [
            "bunkar", "handloom", "weaver", "weaving", "bunai", "kapda", "sari", "saree",
            "dhaga", "soot", "tana", "bana", "reshmi", "silk", "khadi", "loom", "kargha",
            "बुनकर", "हथकरघा", "बुनाई", "साड़ी", "कपड़ा", "सूत", "ताना", "बाना",
            "धागा", "सिल्क", "रेशम", "खादी", "हैंडलूम", "बुनकरी", "करघा", "बनारसी"
        ]
    },
    "masonry": {
        "id": "SKILL-MASN-03",
        "trade_name_en": "Rajmistri / Masonry & Construction",
        "trade_name_hi": "राजमिस्त्री / भवन निर्माण (Masonry)",
        "nsqf_level": 4,
        "qp_code": "CON/Q0102",
        "sector_skill_council": "Construction Skill Development Council of India (CSDCI)",
        "duration_hours": 300,
        "daily_stipend_inr": 500,
        "curriculum_highlights": [
            "ईंट-पत्थर की चुनाई, लेवलिंग और प्लंब-लाइन संरेखण",
            "सीमेंट प्लास्टरिंग, वॉटरप्रूफिंग और टाइल फिक्सिंग",
            "भूकंपरोधी निर्माण तकनीक एवं आरसीसी शटरिंग समझ",
            "डिजिटल लेजर लेवलर और कंक्रीट मिक्सर टूल्स"
        ],
        "tool_kit_name": "उन्नत राजमिस्त्री टूलकिट (Precision Masonry Toolkit)",
        "keywords": [
            "mistri", "rajmistri", "mason", "masonry", "chunai", "deewar",
            "cement", "construction", "plaster", "tile", "eent", "int", "karigar",
            "मिस्त्री", "राजमिस्त्री", "चुनाई", "दीवार", "प्लास्टर", "सीमेंट",
            "ईंट", "मकान", "भवन", "टाइल", "जोड़ाई"
        ]
    },
    "carpentry": {
        "id": "SKILL-CARP-04",
        "trade_name_en": "Badhai / Carpentry",
        "trade_name_hi": "बढ़ई / काष्ठशिल्प (Carpentry)",
        "nsqf_level": 4,
        "qp_code": "CON/Q0103",
        "sector_skill_council": "Construction Skill Development Council of India (CSDCI)",
        "duration_hours": 240,
        "daily_stipend_inr": 500,
        "curriculum_highlights": [
            "लकड़ी की कटाई, घिसाई और सटीक नाप-जोख",
            "आधुनिक इलेक्ट्रिक पावर टूल्स का सुरक्षित उपयोग",
            "मॉड्यूलर किचन, दरवाजे-खिड़कियां और फर्नीचर निर्माण",
            "कार्यस्थल सुरक्षा एवं प्राथमिक चिकित्सा (Safety Standards)"
        ],
        "tool_kit_name": "आधुनिक बढ़ई टूलकिट (Modern Power Woodworking Kit)",
        "keywords": [
            "badhai", "badhaiya", "carpenter", "carpentry", "lakdi", "furniture",
            "wood", "woodwork", "kathi", "sutar", "mez", "kursi", "darwaza",
            "बढ़ई", "बढई", "काठ", "लकड़ी", "फर्नीचर", "कुर्सी", "मेज", "दरवाजा",
            "सुतार", "काष्ठकारी", "बढ़ईगिरी", "लकड़ी का काम"
        ]
    },
    "tailoring": {
        "id": "SKILL-TAIL-05",
        "trade_name_en": "Darzi / Tailoring & Garment Making",
        "trade_name_hi": "दर्जी / सिलाई-कढ़ाई (Garment Construction)",
        "nsqf_level": 3,
        "qp_code": "AMH/Q1947",
        "sector_skill_council": "Apparel, Made-Ups & Home Furnishing Sector Skill Council",
        "duration_hours": 200,
        "daily_stipend_inr": 500,
        "curriculum_highlights": [
            "वस्त्रों की ड्राफ्टिंग, पैटर्न मेकिंग और फैब्रिक कटिंग",
            "इलेक्ट्रिक सिलाई मशीन का संचालन और रख-रखाव",
            "पारंपरिक एवं आधुनिक परिधान सिलाई और इंटरलॉकिंग",
            "स्व-रोजगार बुटीक और परिधान लागत निर्धारण"
        ],
        "tool_kit_name": "प्रोफेशनल सिलाई एवं कटिंग टूलकिट (Electric Sewing & Cutting Kit)",
        "keywords": [
            "darzi", "silai", "tailor", "tailoring", "kapda", "kurta", "pant",
            "sewing", "boutique", "suit", "embroidery", "dress",
            "दर्जी", "सिलाई", "टेलर", "कपड़ा", "सूट", "सलवार", "कढ़ाई",
            "कुर्ता", "पैंट", "सिलाई मशीन", "दर्जीगीरी", "वस्त्र"
        ]
    },
    "electrician": {
        "id": "SKILL-ELEC-06",
        "trade_name_en": "Bijli Mechanic / Wireman & Electrician",
        "trade_name_hi": "बिजली मैकेनिक / इलेक्ट्रीशियन (Domestic Electrician)",
        "nsqf_level": 4,
        "qp_code": "ELE/Q6301",
        "sector_skill_council": "Electronics Sector Skills Council of India (ESSCI)",
        "duration_hours": 350,
        "daily_stipend_inr": 500,
        "curriculum_highlights": [
            "घरेलू वायरिंग, एमसीबी बॉक्स और इन्वर्टर कनेक्शन",
            "अर्थिंग स्थापना और थ्री-फेज लोड डिस्ट्रीब्यूशन",
            "सोलर पैनल रूफटॉप बेसिक इंस्टॉलेशन एवं रिपेयर",
            "इलेक्ट्रिकल सेफ्टी, मल्टीमीटर टेस्टिंग और शॉर्ट सर्किट प्रिवेंशन"
        ],
        "tool_kit_name": "डिजिटल इलेक्ट्रीशियन सेफ्टी टूलकिट (Digital Wireman & Safety Kit)",
        "keywords": [
            "bijli", "electrician", "wireman", "wiring", "light", "motor",
            "current", "switch", "inverter", "fan", "solar", "fuse",
            "बिजली", "इलेक्ट्रीशियन", "वायरमैन", "वायरिंग", "लाइट", "करंट",
            "मोटर", "पंखा", "इन्वर्टर", "बिजली मिस्त्री", "तार"
        ]
    },
    "potter": {
        "id": "SKILL-POTT-07",
        "trade_name_en": "Kumhar / Potter & Terracotta Artisan",
        "trade_name_hi": "कुम्हार / मृत्तिका शिल्प (Terracotta & Pottery)",
        "nsqf_level": 3,
        "qp_code": "HCS/Q0801",
        "sector_skill_council": "Handicrafts and Carpet Sector Skill Council",
        "duration_hours": 200,
        "daily_stipend_inr": 500,
        "curriculum_highlights": [
            "इलेक्ट्रिक चाक (Electric Potter Wheel) का सुरक्षित संचालन",
            "मिट्टी की छनाई, मिक्सिंग और टेराकोटा सांचा ढलाई",
            "ऊष्मा-नियंत्रित भट्टी (Eco-Kiln) में पकाना और ग्लेज़िंग",
            "उत्पादों की पैकेजिंग एवं ई-कॉमर्स / स्थानीय बाजार बिक्री"
        ],
        "tool_kit_name": "इलेक्ट्रिक चाक एवं भट्टी टूलकिट (Electric Potter Wheel Kit)",
        "keywords": [
            "kumhar", "mitti", "bartan", "diya", "potter", "pottery", "matka",
            "कुम्हार", "मिट्टी", "बर्तन", "दीया", "मटका", "कुल्हड़", "मृत्तिका"
        ]
    }
}

# Cobbler alias mapping to charmakar for backwards compatibility
NSQF_SKILL_MODULES["cobbler"] = NSQF_SKILL_MODULES["charmakar"]

# ============================================================================
# 2. MoSJE & GOVERNMENT WELFARE SCHEMES (PM-AJAY GIA COMPONENT HIGHLIGHTED)
# ============================================================================

GOVERNMENT_SCHEMES: Dict[str, Dict[str, Any]] = {
    "pm_ajay": {
        "scheme_code": "MoSJE-PMAJAY-GIA-26097",
        "scheme_name_en": "PM-AJAY (Grants-in-Aid / GIA Component for SC Communities)",
        "scheme_name_hi": "प्रधानमंत्री अनुसूचित जाति अभ्युदय योजना - सहायता अनुदान (GIA घटक)",
        "nodal_ministry": "Ministry of Social Justice and Empowerment (MoSJE), GoI",
        "component_name": "Grants-in-Aid (GIA) for Comprehensive Livelihood Projects for SC Communities",
        "component_name_hi": "अनुसूचित जाति आजीविका परियोजना हेतु सहायता अनुदान (GIA घटक)",
        "financial_grant_inr": 50000,
        "grant_details_hi": "सूक्ष्म उद्यम टूलकिट व कार्यशील पूंजी हेतु ₹50,000 तक का 100% सरकारी सहायता अनुदान (GIA Component Subsidy - शून्य ऋण, No Repayment required)",
        "training_subsidy": "100% निःशुल्क NSQF कौशल विकास प्रशिक्षण, स्टडी किट व परीक्षा शुल्क MoSJE के GIA घटक द्वारा वहन",
        "stipend_during_training": "प्रशिक्षण अवधि में ₹1,500 से ₹3,000 प्रति माह भोजन व आवागमन स्टाइपेंड (Grant-in-Aid Stipend)",
        "eligibility_criteria_hi": "अनुसूचित जाति (SC) समुदाय के पारंपरिक दस्तकार (चर्मकार, हथकरघा बुनकर, राजमिस्त्री आदि) जिनकी पारिवारिक वार्षिक आय ₹2.5 लाख तक हो",
        "target_beneficiaries_hi": "अनुसूचित जाति (SC) समुदाय के कारीगर, हथकरघा बुनकर (Bunkar), चर्मकार (Charmakar), राजमिस्त्री व असंगठित कामगार",
        "required_documents_hi": [
            "आधार कार्ड (Aadhaar Card - बैंक खाते से लिंक)",
            "अनुसूचित जाति (SC) प्रमाण पत्र अथवा स्व-घोषणा",
            "सक्रिय बैंक खाता पासबुक (DBT सक्षम बचत खाता)",
            "आय प्रमाण पत्र अथवा राशन कार्ड",
            "पासपोर्ट साइज फोटो"
        ],
        "official_portal": "https://socialjustice.gov.in/schemes/pm-ajay",
        "toll_free_helpline": "1800-11-2001 (सामाजिक न्याय एवं अधिकारिता मंत्रालय)"
    },
    "pm_vishwakarma": {
        "scheme_code": "MSME-PMVISHWA-2023",
        "scheme_name_en": "PM-Vishwakarma Kaushal Samman Yojana",
        "scheme_name_hi": "प्रधानमंत्री विश्वकर्मा योजना (PM-Vishwakarma)",
        "nodal_ministry": "Ministry of Micro, Small & Medium Enterprises (MSME) & MoSJE",
        "financial_grant_inr": 15000,
        "grant_details_hi": "₹15,000 की निःशुल्क आधुनिक टूलकिट ई-वाउचर अनुदान",
        "collateral_free_credit": "₹3,00,000 तक बिना गारंटी रियायती 5% ब्याज पर आसान सरकारी ऋण (चरण 1: ₹1 लाख, चरण 2: ₹2 लाख)",
        "training_subsidy": "5 से 7 दिन का बुनियादी प्रशिक्षण + ₹500 प्रतिदिन छात्रवृत्ति (Stipend)",
        "eligibility_criteria_hi": "18 पारंपरिक कारीगरी शिल्पों (चर्मकार, बुनकर, बढ़ई, मिस्त्री, दर्जी, लोहार आदि) में कार्यरत 18 वर्ष से अधिक आयु के कारीगर",
        "required_documents_hi": [
            "आधार कार्ड मोबाइल से लिंक (Mobile Linked Aadhaar)",
            "सक्रिय बैंक खाता विवरण (Active Bank Account)",
            "पारंपरिक व्यवसाय का विवरण"
        ],
        "official_portal": "https://pmvishwakarma.gov.in",
        "toll_free_helpline": "1800-267-7777 / 011-23061500"
    }
}

# ============================================================================
# 3. LOCALIZED TRAINING CENTERS (District Wise)
# ============================================================================

DISTRICT_TRAINING_CENTERS: Dict[str, Dict[str, Any]] = {
    "prayagraj": {
        "district_id": "DIST-UP-PRG",
        "district_name_en": "Prayagraj",
        "district_name_hi": "प्रयागराज (इलाहाबाद)",
        "center_name_hi": "प्रधानमंत्री कौशल केंद्र (PMKK) - प्रयागराज",
        "center_name_en": "Pradhan Mantri Kaushal Kendra (PMKK) - Prayagraj",
        "address_hi": "प्लॉट संख्या 42, तेलियरगंज रोड, निकट एमएनएनआईटी गेट, प्रयागराज, उत्तर प्रदेश - 211004",
        "address_en": "Plot 42, Teliarganj Road, Near MNNIT Campus Gate, Prayagraj, UP - 211004",
        "contact_person": "श्री विमलेश त्रिपाठी (केंद्र निदेशक)",
        "helpline_phone": "+91-532-2408912",
        "mobile_dial": "05322408912",
        "available_seats": 35,
        "operating_hours": "प्रातः 9:30 बजे से सायं 5:30 बजे तक (सोमवार से शनिवार)",
        "supported_trades": ["charmakar", "handloom", "masonry", "carpentry", "tailoring", "electrician", "cobbler"],
        "next_batch_date": "10 अक्टूबर 2026",
        "distance_hint_hi": "शहर के मुख्य बस स्टैंड से केवल 3.5 किमी दूर"
    },
    "varanasi": {
        "district_id": "DIST-UP-VNS",
        "district_name_en": "Varanasi",
        "district_name_hi": "वाराणसी (काशी / बनारस)",
        "center_name_hi": "राजकीय औद्योगिक प्रशिक्षण संस्थान (ITI) व PMKK केंद्र - वाराणसी",
        "center_name_en": "Govt ITI & PMKK Skill Hub - Karaundi, Varanasi",
        "address_hi": "करौंदी आईटीआई परिसर, बीएचयू मार्ग, सुंदरपुर के पास, वाराणसी, उत्तर प्रदेश - 221005",
        "address_en": "Karaundi ITI Complex, BHU Main Road, Near Sundarpur, Varanasi, UP - 221005",
        "contact_person": "श्रीमती सुनीता यादव (प्रशिक्षण समन्वयक)",
        "helpline_phone": "+91-542-2503411",
        "mobile_dial": "05422503411",
        "available_seats": 28,
        "operating_hours": "प्रातः 9:00 बजे से सायं 5:00 बजे तक (सोमवार से शनिवार)",
        "supported_trades": ["handloom", "charmakar", "masonry", "tailoring", "carpentry", "electrician", "potter", "cobbler"],
        "next_batch_date": "05 अक्टूबर 2026",
        "distance_hint_hi": "कैंट रेलवे स्टेशन से 4 किमी, ऑटो व ई-रिक्शा सीधे उपलब्ध"
    },
    "lucknow": {
        "district_id": "DIST-UP-LKO",
        "district_name_en": "Lucknow",
        "district_name_hi": "लखनऊ",
        "center_name_hi": "राष्ट्रीय कौशल प्रशिक्षण संस्थान (NSTI) व MoSJE प्रशिक्षण केंद्र - लखनऊ",
        "center_name_en": "National Skill Training Institute (NSTI), Alambagh, Lucknow",
        "address_hi": "कानपुर रोड, आलमबाग बस टर्मिनल के सामने, लखनऊ, उत्तर प्रदेश - 226005",
        "address_en": "Kanpur Road, Opposite Alambagh Bus Terminal, Lucknow, UP - 226005",
        "contact_person": "इंजीनियर आलोक वर्मा (वरिष्ठ नोडल अधिकारी)",
        "helpline_phone": "+91-522-2451980",
        "mobile_dial": "05222451980",
        "available_seats": 42,
        "operating_hours": "प्रातः 9:00 बजे से सायं 6:00 बजे तक (सोमवार से शनिवार)",
        "supported_trades": ["masonry", "charmakar", "handloom", "carpentry", "tailoring", "electrician", "potter", "cobbler"],
        "next_batch_date": "12 अक्टूबर 2026",
        "distance_hint_hi": "आलमबाग मेट्रो स्टेशन गेट संख्या 2 से 200 मीटर"
    },
    "gorakhpur": {
        "district_id": "DIST-UP-GKP",
        "district_name_en": "Gorakhpur",
        "district_name_hi": "गोरखपुर",
        "center_name_hi": "प्रधानमंत्री कौशल केंद्र (PMKK) - असुरन, गोरखपुर",
        "center_name_en": "Pradhan Mantri Kaushal Kendra (PMKK), Asuran, Gorakhpur",
        "address_hi": "मेडिकल कॉलेज रोड, असुरन चौराहा, गोरखपुर, उत्तर प्रदेश - 273001",
        "address_en": "Medical College Road, Asuran Chowk, Gorakhpur, UP - 273001",
        "contact_person": "श्री राजेश्वर प्रताप (केंद्र प्रबंधक)",
        "helpline_phone": "+91-551-2201944",
        "mobile_dial": "05512201944",
        "available_seats": 24,
        "operating_hours": "प्रातः 9:30 बजे से सायं 5:00 बजे तक",
        "supported_trades": ["handloom", "charmakar", "masonry", "carpentry", "tailoring", "electrician"],
        "next_batch_date": "08 अक्टूबर 2026",
        "distance_hint_hi": "रेलवे स्टेशन से 2.5 किमी की दूरी पर"
    }
}

# Default Regional Fallback Center (Used if user district is remote or unlisted)
DEFAULT_FALLBACK_CENTER: Dict[str, Any] = {
    "district_id": "DIST-UP-STATE",
    "district_name_en": "Regional Skill Support Hub (Uttar Pradesh)",
    "district_name_hi": "राज्य आजीविका एवं कौशल सहायता केंद्र (उत्तर प्रदेश)",
    "center_name_hi": "सामाजिक न्याय एवं कौशल विकास राज्य नोडल केंद्र",
    "center_name_en": "State Directorate of Social Justice & Skill Development",
    "address_hi": "विकास भवन, आजीविका प्रकोष्ठ, 4th फ्लोर, जनपथ, लखनऊ, उत्तर प्रदेश - 226001",
    "address_en": "Vikas Bhawan, Livelihood Cell, 4th Floor, Janpath, Lucknow, UP - 226001",
    "contact_person": "हेल्पडेस्क अधिकारी",
    "helpline_phone": "+91-522-2287100",
    "mobile_dial": "05222287100",
    "available_seats": 50,
    "operating_hours": "प्रातः 9:00 बजे से सायं 6:00 बजे तक",
    "supported_trades": ["charmakar", "handloom", "masonry", "carpentry", "tailoring", "electrician", "potter", "cobbler"],
    "next_batch_date": "निरंतर प्रवेश (Continuous Admissions)",
    "distance_hint_hi": "सभी जिलों में ब्लॉक स्तर पर निःशुल्क काउंसलिंग उपलब्ध"
}

# District alias mapping for NLP extraction (Hindi, Bhojpuri, Hinglish)
DISTRICT_ALIASES: Dict[str, List[str]] = {
    "prayagraj": [
        "prayagraj", "allahabad", "ilhabad", "pryj", "teerthraj", "naini",
        "प्रयागराज", "इलाहाबाद", "इलाहाबादी", "नैनी", "फूलपुर", "झूंसी"
    ],
    "varanasi": [
        "varanasi", "banaras", "kashi", "benares", "vns", "sarnath",
        "वाराणसी", "बनारस", "काशी", "सारनाथ", "शिवपुर", "मुगलसराय"
    ],
    "lucknow": [
        "lucknow", "lakhnau", "lko", "alambagh", "gomti nagar", "charbagh",
        "लखनऊ", "लखनउ", "आलमबाग", "हजरतगंज", "चारबाग"
    ],
    "gorakhpur": [
        "gorakhpur", "gkp", "asuran", "deoria", "basti",
        "गोरखपुर", "देवरिया", "बस्ती", "असुरन"
    ]
}
