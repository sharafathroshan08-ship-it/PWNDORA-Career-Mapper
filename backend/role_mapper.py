import json


ROLE_WEIGHTS = {

    "Penetration Tester": {
        "Web Security": 1.0,
        "Network Security": 0.4,
        "Threat Hunting": 0.2
    },

    "Application Security Engineer": {
        "Web Security": 1.0,
        "SOC / SIEM": 0.2
    },

    "SOC Analyst": {
        "SOC / SIEM": 1.0,
        "Threat Hunting": 0.6,
        "Network Security": 0.4
    },

    "Threat Hunter": {
        "Threat Hunting": 1.0,
        "SOC / SIEM": 0.7,
        "DFIR": 0.3
    },

    "DFIR Analyst": {
        "DFIR": 1.0,
        "SOC / SIEM": 0.5
    },

    "Malware Analyst": {
        "Malware / Reverse Engineering": 1.0,
        "Threat Hunting": 0.5
    },

    "Network Security Engineer": {
        "Network Security": 1.0,
        "SOC / SIEM": 0.3
    }

}


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def run_role_mapper():

    mapping = load_json("output/mapping_result.json")

    role_scores = {}

    for role, weights in ROLE_WEIGHTS.items():

        score = 0

        for item in mapping["domain_scores"]:

            domain = item["domain"]

            if domain in weights:
                score += item["score"] * weights[domain]

        role_scores[role] = round(score, 2)

    ranked = sorted(
        role_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print("=" * 60)
    print("PWNDORA ROLE FIT ENGINE")
    print("=" * 60)

    for role, score in ranked:
        print(f"{role:<35} {score}")

    return ranked


if __name__ == "__main__":
    run_role_mapper()