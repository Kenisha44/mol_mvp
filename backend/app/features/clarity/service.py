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
    if score >= 85:
        return "Executive-ready"
    if score >= 70:
        return "Strong, minor edits needed"
    if score >= 50:
        return "Needs simplification"
    return "Too dense or unclear"


def analyze_clarity(text: str) -> dict:
    score = calculate_clarity_score(text)
    label = get_clarity_label(score)

    result = (
        f"Clarity Score: {score}/100\n\n"
        f"Status: {label}\n\n"
        "Recommendation:\n"
        "Simplify long sentences, remove unnecessary jargon, and make the main decision or insight easier to identify."
    )

    return {
        "result": result,
        "score": score,
        "label": label,
    }