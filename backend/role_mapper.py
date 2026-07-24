# backend/role_mapper.py

ROLE_MAPPING = {
    "Web Security": [
        "Penetration Tester",
        "Application Security Engineer",
        "Web Security Analyst"
    ],

    "Network Security": [
        "Network Security Engineer",
        "Security Consultant"
    ],

    "DFIR": [
        "Digital Forensics Analyst",
        "Incident Responder"
    ],

    "SOC / SIEM": [
        "SOC Analyst",
        "Security Monitoring Engineer"
    ],

    "Threat Hunting": [
        "Threat Hunter",
        "Detection Engineer"
    ],

    "Malware / Reverse Engineering": [
        "Malware Analyst",
        "Reverse Engineer"
    ]
}


def recommend_roles(top_domains):

    recommendations = []

    for domain in top_domains:

        if domain in ROLE_MAPPING:

            recommendations.extend(ROLE_MAPPING[domain])

    return recommendations


if __name__ == "__main__":

    top3 = [
        "Web Security",
        "Network Security",
        "DFIR"
    ]

    roles = recommend_roles(top3)

    print("\nRecommended Roles")
    print("-" * 40)

    for role in roles:
        print(role)