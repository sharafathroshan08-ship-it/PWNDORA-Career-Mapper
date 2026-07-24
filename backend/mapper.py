import json
import os
from scoring import calculate_score
from confidence import classify_confidence


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def run_mapper():

    parsed_resume = load_json("output/parsed_resume.json")
    taxonomy = load_json("taxonomy/taxonomy.json")

    domain_scores = {}

    for item in taxonomy:
        domain_scores[item["domain"]] = 0

    print("=" * 60)
    print("PWNDORA MAPPING ENGINE")
    print("=" * 60)

    for matched in parsed_resume["matched_skills"]:

        skill_name = matched["skill"]

        for tax in taxonomy:

            if tax["skill"].strip().lower() == skill_name.strip().lower():

                score = calculate_score(
                    skill_match=True,
                    tool_match=len(tax["tools"]) > 0,
                    certificate_match=len(tax["certificate_alignment"]) > 0
                )

                confidence = classify_confidence(
                    score / 3,
                    {
                        "skip": 0.75,
                        "primary": 0.40,
                        "foundation": 0.20
                    }
                )

                print(f"{tax['skill']} -> {tax['domain']} ({confidence})")

                domain_scores[tax["domain"]] += score

                break

    ranked_domains = sorted(
        domain_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    result = {
        "domain_scores": [],
        "top_3_domains": []
    }

    for domain, score in ranked_domains:
        result["domain_scores"].append({
            "domain": domain,
            "score": round(score, 2)
        })

    for domain, score in ranked_domains[:3]:
        result["top_3_domains"].append(domain)

    os.makedirs("output", exist_ok=True)

    with open("output/mapping_result.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4)

    print()
    print("=" * 60)
    print("PWNDORA DOMAIN RANKING")
    print("=" * 60)

    for i, item in enumerate(result["domain_scores"], start=1):
        print(f"{i}. {item['domain']:<35} {item['score']}")

    print()
    print("Top 3 Recommended Domains")
    print("-" * 40)

    for domain in result["top_3_domains"]:
        print(domain)

    print()
    print("✅ Mapping results saved to output/mapping_result.json")

    return result


if __name__ == "__main__":
    run_mapper()