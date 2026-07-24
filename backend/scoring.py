# backend/scoring.py

WEIGHTS = {
    "skill": 1.0,
    "certificate": 1.0,
    "job_title": 0.9,
    "project": 0.8,
    "tool": 0.7,
    "synonym": 0.6,
    "section_bonus": 0.1
}


def calculate_score(
    skill_match=False,
    certificate_match=False,
    tool_match=False,
    job_title_match=False,
    project_match=False,
    synonym_match=False,
    section_bonus=False,
    mention_count=1
):
    score = 0.0

    if skill_match:
        score += WEIGHTS["skill"]

    if certificate_match:
        score += WEIGHTS["certificate"]

    if tool_match:
        score += WEIGHTS["tool"]

    if job_title_match:
        score += WEIGHTS["job_title"]

    if project_match:
        score += WEIGHTS["project"]

    if synonym_match:
        score += WEIGHTS["synonym"]

    if section_bonus:
        score += WEIGHTS["section_bonus"]

    # Simple frequency bonus (preparing for blueprint frequency factor)
    if mention_count > 1:
        score += min((mention_count - 1) * 0.1, 0.5)

    return round(score, 2)