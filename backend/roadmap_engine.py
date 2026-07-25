"""
============================================================
PWNDORA AI
Roadmap Engine
============================================================
"""


def generate_learning_roadmap(gap_analysis):

    roadmap = {

        "Foundation": [],

        "Primary": [],

        "Advanced": [],

        "Expert": []

    }

    for skill in gap_analysis:

        task = {

            "skill": skill["skill"],

            "domain": skill["domain"],

            "priority": skill["priority"]

        }

        difficulty = skill["difficulty"].lower()

        if difficulty == "beginner":

            roadmap["Foundation"].append(task)

        elif difficulty == "intermediate":

            roadmap["Primary"].append(task)

        elif difficulty == "advanced":

            roadmap["Advanced"].append(task)

        else:

            roadmap["Expert"].append(task)

    return roadmap


def roadmap_statistics(roadmap):

    return {

        "Foundation": len(roadmap["Foundation"]),

        "Primary": len(roadmap["Primary"]),

        "Advanced": len(roadmap["Advanced"]),

        "Expert": len(roadmap["Expert"])

    }


if __name__ == "__main__":

    sample_gap = [

        {

            "skill": "SQL Injection",

            "domain": "Web Security",

            "difficulty": "Beginner",

            "priority": "High"

        },

        {

            "skill": "API Security",

            "domain": "Web Security",

            "difficulty": "Intermediate",

            "priority": "Medium"

        },

        {

            "skill": "Threat Hunting",

            "domain": "Threat Hunting",

            "difficulty": "Advanced",

            "priority": "High"

        }

    ]

    roadmap = generate_learning_roadmap(sample_gap)

    print(roadmap)

    print()

    print(roadmap_statistics(roadmap))