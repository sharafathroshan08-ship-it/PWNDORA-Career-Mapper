"""
============================================================
PWNDORA AI
Report Generator
============================================================
"""


def generate_final_report(
    parsed_resume,
    mapping_result,
    recommended_roles,
    gap_analysis,
    learning_path,
    analytics,
    ai_summary,
    roadmap
):

    report = {

        "application": "PWNDORA AI",

        "version": "2.0",

        "parsed_resume": parsed_resume,

        "mapping_result": mapping_result,

        "recommended_roles": recommended_roles,

        "gap_analysis": gap_analysis,

        "learning_path": learning_path,

        "analytics": analytics,

        "ai_summary": ai_summary,

        "roadmap": roadmap

    }

    return report


if __name__ == "__main__":

    print("PWNDORA Report Generator Ready")