import re


POSITIVE_WORDS = [
    "increase",
    "increased",
    "grew",
    "growth",
    "improved",
    "improvement",
    "rose",
    "gain",
    "gained",
    "higher",
    "up",
    "expanded",
]

NEGATIVE_WORDS = [
    "decrease",
    "decreased",
    "decline",
    "declined",
    "down",
    "drop",
    "dropped",
    "fell",
    "lower",
    "loss",
    "lost",
    "churn",
    "risk",
    "complaints",
]


def split_signals(text: str) -> list[str]:
    """
    Break input into individual business observations.
    Supports both sentences and line-separated notes.
    """
    signals = re.split(r"[\n]+|(?<=[.!?])\s+", text)

    return [
        signal.strip()
        for signal in signals
        if signal.strip()
    ]


def detect_direction(signal: str) -> str:
    lower_signal = signal.lower()

    positive = any(
        word in lower_signal
        for word in POSITIVE_WORDS
    )

    negative = any(
        word in lower_signal
        for word in NEGATIVE_WORDS
    )

    if positive and negative:
        return "mixed"

    if positive:
        return "positive"

    if negative:
        return "negative"

    return "neutral"


def create_executive_title(
    positive_count: int,
    negative_count: int
) -> str:

    if positive_count and negative_count:
        return "Growth Momentum Emerges Alongside Performance Risk"

    if positive_count:
        return "Performance Signals Point to Continued Growth"

    if negative_count:
        return "Performance Pressure Requires Leadership Attention"

    return "Business Performance Requires Additional Context"


def create_chart_suggestion(
    positive_count: int,
    negative_count: int
) -> str:

    if positive_count and negative_count:
        return (
            "Use a comparison chart showing improving KPIs "
            "alongside declining or risk-oriented KPIs."
        )

    if positive_count:
        return (
            "Use a trend chart showing KPI growth over time "
            "with prior-period comparisons."
        )

    if negative_count:
        return (
            "Use a variance or trend chart highlighting "
            "declining KPIs against targets or prior periods."
        )

    return (
        "Use a KPI summary table until additional "
        "time-series or comparison data is available."
    )


def generate_insight(text: str) -> dict:
    signals = split_signals(text)

    analyzed_signals = [
        {
            "text": signal,
            "direction": detect_direction(signal),
        }
        for signal in signals
    ]

    positive_signals = [
        item["text"]
        for item in analyzed_signals
        if item["direction"] == "positive"
    ]

    negative_signals = [
        item["text"]
        for item in analyzed_signals
        if item["direction"] == "negative"
    ]

    positive_count = len(positive_signals)
    negative_count = len(negative_signals)

    # Determine overall insight type
    if positive_count and negative_count:
        insight_type = "Mixed Performance"
        label = "Opportunity + risk signal"

    elif positive_count:
        insight_type = "Positive Trend"
        label = "Growth signal"

    elif negative_count:
        insight_type = "Negative Trend"
        label = "Risk signal"

    else:
        insight_type = "General Insight"
        label = "Needs context"


    # PRIMARY INSIGHT
    if positive_count and negative_count:
        primary_insight = (
            "The business is showing positive momentum in some areas "
            "while simultaneous negative signals may threaten the "
            "sustainability of that performance."
        )

    elif positive_count:
        primary_insight = (
            "The supplied business signals indicate improving "
            "performance and positive operating momentum."
        )

    elif negative_count:
        primary_insight = (
            "The supplied business signals indicate performance "
            "pressure that may require leadership attention."
        )

    else:
        primary_insight = (
            "The supplied information does not yet establish a clear "
            "performance direction."
        )


    # SO WHAT
    if positive_count and negative_count:
        so_what = (
            "Leadership should avoid evaluating the positive results "
            "in isolation. The negative signals may reveal operational, "
            "customer, or retention pressures beneath headline growth."
        )

    elif positive_count:
        so_what = (
            "The organization may have an opportunity to reinforce "
            "the drivers behind current growth and determine whether "
            "the improvement can be sustained."
        )

    elif negative_count:
        so_what = (
            "If the decline continues, it may affect future performance, "
            "customer outcomes, operating efficiency, or growth."
        )

    else:
        so_what = (
            "Leadership needs stronger comparison points, time periods, "
            "targets, or quantitative context before drawing conclusions."
        )


    # RECOMMENDED ACTION
    if positive_count and negative_count:
        recommended_action = (
            "Identify which negative signals could undermine the positive "
            "performance, investigate their root causes, and prioritize "
            "corrective action before accelerating growth initiatives."
        )

    elif positive_count:
        recommended_action = (
            "Identify the primary drivers behind the improvement, compare "
            "them with prior periods, and determine which drivers are "
            "repeatable or scalable."
        )

    elif negative_count:
        recommended_action = (
            "Investigate the root causes behind the declining indicators, "
            "quantify their business impact, and define corrective actions."
        )

    else:
        recommended_action = (
            "Add measurable KPIs, time periods, benchmarks, and comparison "
            "points before making an executive recommendation."
        )


    executive_title = create_executive_title(
        positive_count,
        negative_count
    )

    chart_suggestion = create_chart_suggestion(
        positive_count,
        negative_count
    )


    # Maintain legacy result field for compatibility
    result = (
        f"Primary Insight:\n{primary_insight}\n\n"
        f"So What?\n{so_what}\n\n"
        f"Recommended Action:\n{recommended_action}\n\n"
        f"Executive Title:\n{executive_title}\n\n"
        f"Chart Suggestion:\n{chart_suggestion}"
    )


    return {
        "result": result,
        "insight_type": insight_type,
        "label": label,

        # Structured V1 fields
        "primary_insight": primary_insight,
        "so_what": so_what,
        "recommended_action": recommended_action,
        "executive_title": executive_title,
        "chart_suggestion": chart_suggestion,

        # Useful metadata
        "positive_signal_count": positive_count,
        "negative_signal_count": negative_count,
        "signal_count": len(signals),
    }