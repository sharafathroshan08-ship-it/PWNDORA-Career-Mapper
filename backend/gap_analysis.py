import json


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def run_gap_analysis():

    taxonomy = load_json("taxonomy/taxonomy.json")
    parsed = load_json("output/parsed_resume.json")

    matched = set()

    for skill in parsed["matched_skills"]:
        matched.add(skill["skill"])

    missing = []

    for item in taxonomy:

        if item["skill"] not in matched:

            missing.append({
                "domain": item["domain"],
                "skill": item["skill"],
                "difficulty": item["difficulty"],
                "priority": item["priority_level"]
            })

    print("=" * 60)
    print("PWNDORA GAP ANALYSIS")
    print("=" * 60)

    print(f"Missing Skills : {len(missing)}")

    for skill in missing[:10]:
        print(
            f"{skill['domain']} -> {skill['skill']} ({skill['priority']})"
        )

    return missing


if __name__ == "__main__":
    run_gap_analysis()