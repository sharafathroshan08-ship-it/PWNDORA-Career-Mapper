import json


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def run_learning_path():

    taxonomy = load_json("taxonomy/taxonomy.json")
    parsed = load_json("output/parsed_resume.json")

    matched_skills = set()

    for skill in parsed["matched_skills"]:
        matched_skills.add(skill["skill"])

    foundation = []
    primary = []
    stretch = []

    for item in taxonomy:

        if item["skill"] in matched_skills:
            continue

        lab = {
            "lab_category": item["lab_category"],
            "skill": item["skill"],
            "hours": item["estimated_hours"],
            "difficulty": item["difficulty"],
            "priority": item["priority_level"]
        }

        if item["difficulty"] == "Beginner":
            foundation.append(lab)

        elif item["difficulty"] == "Intermediate":
            primary.append(lab)

        else:
            stretch.append(lab)

    print("=" * 60)
    print("PWNDORA PERSONALIZED LAB PATH")
    print("=" * 60)

    print("\nFOUNDATION LABS")
    print("-" * 40)

    for lab in foundation:
        print(f"{lab['lab_category']}")
        print(f"  Skill : {lab['skill']}")
        print(f"  Hours : {lab['hours']}")
        print()

    print("\nPRIMARY LABS")
    print("-" * 40)

    for lab in primary:
        print(f"{lab['lab_category']}")
        print(f"  Skill : {lab['skill']}")
        print(f"  Hours : {lab['hours']}")
        print()

    print("\nSTRETCH LABS")
    print("-" * 40)

    for lab in stretch:
        print(f"{lab['lab_category']}")
        print(f"  Skill : {lab['skill']}")
        print(f"  Hours : {lab['hours']}")
        print()

    return {
        "foundation": foundation,
        "primary": primary,
        "stretch": stretch
    }


if __name__ == "__main__":
    run_learning_path()