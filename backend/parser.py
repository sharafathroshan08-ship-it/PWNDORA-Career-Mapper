import json

def load_taxonomy(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def find_skills(resume_text, taxonomy):
    found_skills = []

    resume_lower = resume_text.lower()

    for skill in taxonomy["skills"]:
        if skill.lower() in resume_lower:
            found_skills.append(skill)

    return found_skills 