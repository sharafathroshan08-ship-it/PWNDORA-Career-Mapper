import json
import os
from scoring import calculate_score
from confidence import classify_confidence


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


# Load files
parsed_resume = load_json("output/parsed_resume.json")
taxonomy = load_json("taxonomy/taxonomy.json")

# Domain scores
domain_scores = {}

# Initialize all domains
for item in taxonomy:
    domain_scores[item["domain"]] = 0

# Calculate weighted scores
for matched in parsed_resume["matched_skills"]:
    skill_name = matched["skill"]

    for tax in taxonomy:
        if tax["skill"] == skill_name:

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

print(f"{tax['skill']} -> {confidence}")

domain_scores[tax["domain"]] += score

# Sort domains
ranked_domains = sorted(
    domain_scores.items(),
    key=lambda x: x[1],
    reverse=True
)

# Prepare JSON output
result = {
    "domain_scores": [
        {
            "domain": domain,
            "score": score
        }
        for domain, score in ranked_domains
    ],
    "top_3_domains": [
        domain
        for domain, score in ranked_domains[:3]
    ]
}

# Create output folder if needed
os.makedirs("output", exist_ok=True)

# Save mapping result
with open("output/mapping_result.json", "w", encoding="utf-8") as file:
    json.dump(result, file, indent=4)

# Display results
print("=" * 60)
print("PWNDORA DOMAIN RANKING")
print("=" * 60)

for i, item in enumerate(result["domain_scores"], start=1):
    print(f"{i}. {item['domain']:<30} Score : {item['score']}")

print("\nTop 3 Recommended Domains")
print("-" * 40)

for domain in result["top_3_domains"]:
    print(domain)

print("\n✅ Mapping results saved to output/mapping_result.json")