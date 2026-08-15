import re


POSITIVE_TERMS = [
    "increase", "increased", "grew", "growth", "improved",
    "improvement", "up", "higher", "rose", "gain", "gained",
    "exceeded", "above target", "strong"
]

NEGATIVE_TERMS = [
    "decrease", "decreased", "decline", "declined", "down",
    "lower", "fell", "drop", "dropped", "churn", "risk",
    "missed", "below target", "tickets increased", "cost increased"
]


def split_signals(text: str) -> list[str]:
    signals = re.split(r"[\n]+|(?<=[.!?])\s+", text)

    return [
        signal.strip()
        for signal in signals
        if signal.strip()
    ]


def classify_signal(signal: str) -> str:
    lower_signal = signal.lower()

    positive = any(term in lower_signal for term in POSITIVE_TERMS)
    negative = any(term in lower_signal for term in NEGATIVE_TERMS)

    if positive and negative:
        return "mixed"

    if negative:
        return "negative"

    if positive:
        return "positive"

    return "neutral"


def generate_dashboard_narrative(text: str) -> dict:
    signals = split_signals(text)

    positive_signals = []
    negative_signals = []
    neutral_signals = []

    for signal in signals:
        classification = classify_signal(signal)

        if classification == "positive":
            positive_signals.append(signal)

        elif classification in ["negative", "mixed"]:
            negative_signals.append(signal)

        else:
            neutral_signals.append(signal)

    positive_count = len(positive_signals)
    negative_count = len(negative_signals)
    total_signals = len(signals)

    if positive_count > 0 and negative_count > 0:
        performance_status = "Mixed Performance"
        status_label = "Opportunity + risk"

        executive_summary = (
            "Performance is showing positive momentum, but several risk "
            "signals require management attention before the gains can be "
            "considered sustainable."
        )

        outlook = (
            "Near-term performance remains constructive, provided leadership "
            "addresses the negative operating signals while preserving the "
            "drivers behind current growth."
        )

    elif positive_count > 0:
        performance_status = "Positive Performance"
        status_label = "Growth momentum"

        executive_summary = (
            "The dashboard indicates broadly positive performance with "
            "multiple signals of improving business momentum."
        )

        outlook = (
            "The current trajectory is favorable. Leadership should focus "
            "on protecting the strongest performance drivers and determining "
            "which gains can be scaled."
        )

    elif negative_count > 0:
        performance_status = "Performance Risk"
        status_label = "Attention required"

        executive_summary = (
            "The dashboard indicates meaningful performance pressure that "
            "requires leadership attention."
        )

        outlook = (
            "The near-term outlook remains cautious until the primary "
            "performance risks are understood and corrective actions begin "
            "to produce measurable improvement."
        )

    else:
        performance_status = "Stable Performance"
        status_label = "Monitor"

        executive_summary = (
            "The dashboard does not currently show a dominant positive or "
            "negative performance direction."
        )

        outlook = (
            "Leadership should continue monitoring the available indicators "
            "and add comparison periods or targets to improve interpretation."
        )

    if positive_signals:
        drivers = (
            "Positive performance is being supported by: "
            + " ".join(positive_signals[:3])
        )
    else:
        drivers = (
            "No clear positive performance driver was identified in the "
            "submitted dashboard notes."
        )

    if negative_signals:
        risks = (
            "Management attention should focus on: "
            + " ".join(negative_signals[:3])
        )
    else:
        risks = (
            "No major negative performance signal was identified in the "
            "submitted dashboard notes."
        )

    if negative_count > 0:
        recommended_action = (
            "Investigate the root causes behind the negative indicators, "
            "assign ownership for corrective actions, and monitor whether "
            "those KPIs improve during the next reporting period."
        )

    elif positive_count > 0:
        recommended_action = (
            "Identify the operational drivers behind the strongest gains "
            "and determine which improvements can be repeated or scaled."
        )

    else:
        recommended_action = (
            "Add targets, prior-period comparisons, and additional KPI "
            "context before making a major management decision."
        )

    result = (
        f"Executive Summary:\n{executive_summary}\n\n"
        f"Performance Drivers:\n{drivers}\n\n"
        f"Risks & Watch Items:\n{risks}\n\n"
        f"Recommended Action:\n{recommended_action}\n\n"
        f"Outlook:\n{outlook}"
    )

    return {
        "result": result,
        "performance_status": performance_status,
        "label": status_label,
        "executive_summary": executive_summary,
        "performance_drivers": drivers,
        "risks": risks,
        "recommended_action": recommended_action,
        "outlook": outlook,
        "signal_count": total_signals,
        "positive_signal_count": positive_count,
        "negative_signal_count": negative_count,
    }