"""
============================================================
PWNDORA AI
Analytics Engine
============================================================
"""

from backend.config import (
    MAX_DOMAIN_SCORE,
    CAREER_READINESS
)


def calculate_resume_score(domain_scores):
    """
    Calculates the total resume score.
    """

    total = 0

    for item in domain_scores:
        total += item["score"]

    return round(total, 2)


def calculate_career_readiness(domain_scores):
    """
    Calculates Career Readiness Percentage.
    """

    total_score = calculate_resume_score(domain_scores)

    maximum_possible = len(domain_scores) * MAX_DOMAIN_SCORE

    if maximum_possible == 0:
        return 0

    percentage = round(
        (total_score / maximum_possible) * 100,
        2
    )

    return percentage


def get_readiness_level(readiness_score):
    """
    Returns readiness level based on percentage.
    """

    for score in sorted(
        CAREER_READINESS.keys(),
        reverse=True
    ):

        if readiness_score >= score:
            return CAREER_READINESS[score]

    return "Unknown"


def calculate_skill_coverage(
    matched_skills,
    total_skills
):
    """
    Skill coverage percentage.
    """

    if total_skills == 0:
        return 0

    return round(
        (matched_skills / total_skills) * 100,
        2
    )


def generate_dashboard_statistics(
    mapping_result,
    parsed_resume
):
    """
    Returns dashboard statistics.
    """

    readiness = calculate_career_readiness(
        mapping_result["domain_scores"]
    )

    coverage = calculate_skill_coverage(
        len(parsed_resume["matched_skills"]),
        42
    )

    level = get_readiness_level(
        readiness
    )

    return {

        "career_readiness": readiness,

        "readiness_level": level,

        "skill_coverage": coverage,

        "matched_skills": len(
            parsed_resume["matched_skills"]
        ),

        "matched_tools": len(
            parsed_resume["matched_tools"]
        ),

        "matched_certificates": len(
            parsed_resume["matched_certificates"]
        )

    }


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
            }

        ]

    }

    sample_resume = {

        "matched_skills": [1] * 15,

        "matched_tools": [1] * 6,

        "matched_certificates": [1] * 3

    }

    print(
        generate_dashboard_statistics(
            sample_mapping,
            sample_resume
        )
    )