import json
import os


def load_taxonomy(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def parse_resume(resume_text, taxonomy):
    resume = resume_text.lower()

    matched_skills = []
    matched_tools = set()
    matched_certificates = set()

    for item in taxonomy:

        if item["skill"].lower() in resume:

            matched_skills.append({
                "domain": item["domain"],
                "skill": item["skill"],
                "difficulty": item["difficulty"],
                "priority": item["priority_level"]
            })

            for tool in item["tools"]:
                matched_tools.add(tool)

            for cert in item["certificate_alignment"]:
                matched_certificates.add(cert)

    return {
        "matched_skills": matched_skills,
        "matched_tools": sorted(list(matched_tools)),
        "matched_certificates": sorted(list(matched_certificates))
    }


def save_output(result):

    os.makedirs("output", exist_ok=True)

    with open("output/parsed_resume.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)

    print("\n✅ Parsed resume saved to output/parsed_resume.json")


if __name__ == "__main__":

    taxonomy = load_taxonomy("taxonomy/taxonomy.json")

    print("=" * 60)
    print("Paste Resume Text")
    print("Type END on a new line when finished.")
    print("=" * 60)

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    resume = "\n".join(lines)

    result = parse_resume(resume, taxonomy)

    save_output(result)

    print("\n========== PARSER RESULT ==========\n")

    print("Matched Skills")
    print("-" * 40)

    if result["matched_skills"]:
        for skill in result["matched_skills"]:
            print(f"Domain      : {skill['domain']}")
            print(f"Skill       : {skill['skill']}")
            print(f"Difficulty  : {skill['difficulty']}")
            print(f"Priority    : {skill['priority']}")
            print("-" * 40)
    else:
        print("None")

    print("\nMatched Tools")
    print("-" * 40)

    if result["matched_tools"]:
        for tool in result["matched_tools"]:
            print(tool)
    else:
        print("None")

    print("\nMatched Certificates")
    print("-" * 40)

    if result["matched_certificates"]:
        for cert in result["matched_certificates"]:
            print(cert)
    else:
        print("None")