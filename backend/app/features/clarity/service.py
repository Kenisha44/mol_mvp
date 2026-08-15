def calculate_clarity_score(text: str) -> int:
    word_count = len(text.split())
    sentence_count = max(text.count(".") + text.count("!") + text.count("?"), 1)
    avg_sentence_length = word_count / sentence_count

    score = 100

    if avg_sentence_length > 25:
        score -= 20
    elif avg_sentence_length > 18:
        score -= 10

    if word_count > 180:
        score -= 15
    elif word_count > 100:
        score -= 8

    jargon_words = [
        "synergy",
        "leverage",
        "optimize",
        "streamline",
        "paradigm",
        "stakeholder",
        "utilize",
        "bandwidth",
    ]

    jargon_count = sum(1 for word in jargon_words if word in text.lower())
    score -= jargon_count * 5

    return max(0, min(100, score))


def get_clarity_label(score: int) -> str:
    if score >= 90:
        return "Executive-ready"
    if score >= 75:
        return "Nearly executive-ready"
    if score >= 60:
        return "Needs refinement"
    return "Needs significant revision"


def get_recommendation(score: int) -> str:
    if score >= 90:
        return (
            "Strong executive communication. The message is clear, concise, "
            "and appropriately focused for leadership."
        )

    if score >= 75:
        return (
            "The core message is strong. Tighten longer sentences, move the "
            "main business implication earlier, and remove unnecessary detail."
        )

    if score >= 60:
        return (
            "Clarify the primary takeaway, reduce unnecessary wording, and "
            "make the business implication or requested decision more explicit."
        )

    return (
        "Restructure the message around one primary takeaway. Simplify the "
        "language, remove distracting detail, and clearly state what leadership "
        "needs to know or decide."
    )


def refine_executive_text(text: str) -> str:
    cleaned = " ".join(text.split())

    replacements = {
        "utilize": "use",
        "leverage": "use",
        "in order to": "to",
        "due to the fact that": "because",
        "at this point in time": "now",
    }

    for old, new in replacements.items():
        cleaned = cleaned.replace(old, new)
        cleaned = cleaned.replace(old.title(), new.title())

    return cleaned


def analyze_clarity(text: str) -> dict:
    score = calculate_clarity_score(text)
    label = get_clarity_label(score)
    recommendation = get_recommendation(score)
    refined_text = refine_executive_text(text)

    result = (
        f"Clarity Score: {score}/100\n\n"
        f"Status: {label}\n\n"
        f"Recommendation:\n{recommendation}\n\n"
        f"Refined Executive Copy:\n{refined_text}"
    )

    return {
        "result": result,
        "score": score,
        "label": label,
        "recommendation": recommendation,
        "refined_text": refined_text,
    }