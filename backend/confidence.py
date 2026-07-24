# backend/confidence.py

def classify_confidence(score, thresholds):
    """
    Classify a skill based on the taxonomy confidence thresholds.
    """

    if score >= thresholds["skip"]:
        return "Confirmed"

    elif score >= thresholds["primary"]:
        return "Inferred"

    elif score >= thresholds["foundation"]:
        return "Weakly Inferred"

    return "Missing"


if __name__ == "__main__":

    thresholds = {
        "skip": 0.75,
        "primary": 0.40,
        "foundation": 0.20
    }

    test_scores = [0.90, 0.60, 0.25, 0.05]

    for score in test_scores:
        print(score, "->", classify_confidence(score, thresholds))