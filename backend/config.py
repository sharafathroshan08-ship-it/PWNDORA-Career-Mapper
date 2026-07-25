"""
============================================================
PWNDORA AI
Central Configuration
============================================================
"""

# ============================================================
# Application Information
# ============================================================

APP_NAME = "PWNDORA AI"

VERSION = "2.0.0"

AUTHOR = "PWNDORA Team"

DESCRIPTION = "AI Powered Cybersecurity Career Intelligence Platform"


# ============================================================
# Upload Settings
# ============================================================

SUPPORTED_EXTENSIONS = [
    ".pdf",
    ".docx"
]

MAX_UPLOAD_SIZE_MB = 10


# ============================================================
# Resume Parser
# ============================================================

CASE_SENSITIVE = False

REMOVE_PUNCTUATION = True

MATCH_TOOLS = True

MATCH_CERTIFICATES = True


# ============================================================
# Domain Mapping
# ============================================================

MAX_DOMAIN_SCORE = 10.0

TOP_RECOMMENDED_DOMAINS = 3


# ============================================================
# Role Recommendation
# ============================================================

TOP_RECOMMENDED_ROLES = 5


# ============================================================
# Skill Gap
# ============================================================

MAX_GAP_DISPLAY = 10


# ============================================================
# Learning Path
# ============================================================

FOUNDATION_LEVEL = "Beginner"

PRIMARY_LEVEL = "Intermediate"

ADVANCED_LEVEL = "Advanced"


# ============================================================
# Confidence Thresholds
# ============================================================

CONFIDENCE_THRESHOLDS = {

    "skip": 0.75,

    "primary": 0.40,

    "foundation": 0.20

}


# ============================================================
# Career Readiness Levels
# ============================================================

CAREER_READINESS = {

    90: "Industry Ready",

    75: "Advanced",

    60: "Intermediate",

    40: "Beginner",

    0: "Foundation"

}


# ============================================================
# Dashboard Settings
# ============================================================

SHOW_TOP_DOMAINS = 3

SHOW_TOP_ROLES = 5

SHOW_TOP_GAPS = 10


# ============================================================
# AI Report
# ============================================================

GENERATE_REPORT = True

ENABLE_AI_SUMMARY = True

ENABLE_ANALYTICS = True

ENABLE_ROADMAP = True


# ============================================================
# PWNDORA Academy
# ============================================================

ROADMAP_PHASES = [

    "Foundation",

    "Primary",

    "Advanced",

    "Expert"

]


# ============================================================
# Output Files
# ============================================================

OUTPUT_FOLDER = "output"

PARSED_RESUME_FILE = "output/parsed_resume.json"

MAPPING_RESULT_FILE = "output/mapping_result.json"

FINAL_REPORT_FILE = "output/final_report.json"


# ============================================================
# Future AI Integration
# ============================================================

AI_ENABLED = False

LLM_PROVIDER = None

API_KEY = None


# ============================================================
# Logging
# ============================================================

DEBUG = True

LOG_LEVEL = "INFO"