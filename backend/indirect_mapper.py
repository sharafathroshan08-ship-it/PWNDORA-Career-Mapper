import json


def load_indirect_skills():
    with open("taxonomy/indirect_skills.json", "r", encoding="utf-8") as file:
        return json.load(file)


def calculate_indirect_boost(matched_categories):

    indirect_data = load_indirect_skills()

    boosts = {}

    for item in indirect_data:

        if item["category"] in matched_categories:

            for domain in item["boosts"]:

                boosts[domain] = boosts.get(domain, 0) + 0.30

    return boosts


if __name__ == "__main__":

    matched = [
        "Programming",
        "Networking"
    ]

    result = calculate_indirect_boost(matched)

    print("\nIndirect Domain Boosts")
    print("-" * 40)

    for domain, score in result.items():
        print(f"{domain:<35} +{score}")