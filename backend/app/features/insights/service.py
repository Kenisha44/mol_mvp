def generate_insight(text: str) -> dict:
    lower_text = text.lower()

    if any(word in lower_text for word in ["increase", "grew", "growth", "up"]):
        insight_type = "Positive Trend"
        label = "Growth signal"
        recommendation = (
            "Highlight the drivers behind the increase and identify whether this growth is repeatable."
        )
    elif any(word in lower_text for word in ["decrease", "decline", "down", "drop"]):
        insight_type = "Negative Trend"
        label = "Risk signal"
        recommendation = (
            "Identify the root cause of the decline and recommend corrective action."
        )
    elif any(word in lower_text for word in ["stable", "flat", "unchanged"]):
        insight_type = "Stable Performance"
        label = "Monitor signal"
        recommendation = (
            "Explain whether stability is expected, healthy, or a sign of stalled momentum."
        )
    else:
        insight_type = "General Insight"
        label = "Needs context"
        recommendation = (
            "Add numbers, time periods, comparison points, and business context."
        )

    result = (
        f"Insight Type: {insight_type}\n\n"
        f"Executive Interpretation:\n"
        f"{text}\n\n"
        f"Recommendation:\n"
        f"{recommendation}"
    )

    return {
        "result": result,
        "insight_type": insight_type,
        "label": label,
    }