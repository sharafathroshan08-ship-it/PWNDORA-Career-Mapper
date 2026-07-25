"""
============================================================
PWNDORA AI
Artificial Intelligence Engine
============================================================
"""

from backend.analytics import (
    generate_dashboard_statistics
)


def generate_strengths(mapping_result):

    strengths = []

    for item in mapping_result["domain_scores"]:

        if item["score"] >= 5:

            strengths.append(
                f"Strong knowledge in {item['domain']}"
            )

    if not strengths:

        strengths.append(
            "Cybersecurity foundation is still developing."
        )

    return strengths


def generate_weaknesses(mapping_result):

    weaknesses = []

    for item in mapping_result["domain_scores"]:

        if item["score"] == 0:

            weaknesses.append(
                f"No demonstrated skills in {item['domain']}"
            )

    return weaknesses


def recommend_next_step(readiness):

    if readiness >= 90:

        return "Start preparing for advanced cybersecurity certifications and real-world projects."

    elif readiness >= 75:

        return "Focus on practical labs and Capture The Flag (CTF) challenges."

    elif readiness >= 60:

        return "Strengthen intermediate cybersecurity skills through hands-on practice."

    elif readiness >= 40:

        return "Build a stronger cybersecurity foundation using guided learning paths."

    else:

        return "Start with cybersecurity fundamentals before specializing."


def generate_ai_summary(
    mapping_result,
    parsed_resume
):

    analytics = generate_dashboard_statistics(
        mapping_result,
        parsed_resume
    )

    strengths = generate_strengths(
        mapping_result
    )

    weaknesses = generate_weaknesses(
        mapping_result
    )

    recommendation = recommend_next_step(
        analytics["career_readiness"]
    )

    summary = {

        "career_readiness": analytics["career_readiness"],

        "readiness_level": analytics["readiness_level"],

        "skill_coverage": analytics["skill_coverage"],

        "strengths": strengths,

        "weaknesses": weaknesses,

        "recommendation": recommendation

    }

    return summary


if __name__ == "__main__":

    sample_mapping = {

        "domain_scores": [

            {
                "domain": "Web Security",
                "score": 5.4
            },

            {
                "domain": "Network Security",
                "score": 2.7
            },

            {
                "domain": "SOC / SIEM",
                "score": 0
            }

        ]

    }

    sample_resume = {

        "matched_skills": [1] * 15,

        "matched_tools": [1] * 5,

        "matched_certificates": [1] * 2

    }

    result = generate_ai_summary(
        sample_mapping,
        sample_resume
    )

    print(result)