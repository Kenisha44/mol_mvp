def generate_dashboard_narrative(text: str) -> dict:
    lower_text = text.lower()

    growth_signal = any(word in lower_text for word in ["increase", "grew", "growth", "up", "higher"])
    decline_signal = any(word in lower_text for word in ["decrease", "decline", "down", "drop", "lower"])
    risk_signal = any(word in lower_text for word in ["churn", "cost", "tickets", "complaints", "delays", "risk"])

    executive_summary = (
        "The dashboard indicates meaningful business movement across key performance areas. "
        "Leadership should focus on understanding the drivers behind the strongest changes, "
        "monitoring potential risks, and translating the findings into clear next-step decisions."
    )

    key_findings = []

    if growth_signal:
        key_findings.append("One or more metrics show positive movement, suggesting potential growth momentum.")
    if decline_signal:
        key_findings.append("One or more metrics show negative movement, which may require further investigation.")
    if risk_signal:
        key_findings.append("The dashboard includes possible risk indicators that should be monitored closely.")

    if not key_findings:
        key_findings.append("The dashboard information needs clearer comparisons, time periods, and measurable values.")

    business_risks = []

    if risk_signal:
        business_risks.append("Operational or customer experience risks may be emerging based on the provided notes.")
    if decline_signal:
        business_risks.append("Declining metrics may indicate performance pressure or execution gaps.")

    if not business_risks:
        business_risks.append("No major risk signal is obvious from the current notes, but additional context is needed.")

    opportunities = []

    if growth_signal:
        opportunities.append("Investigate what drove the strongest positive results and determine whether they can be repeated.")
    opportunities.append("Use the dashboard findings to create clearer leadership reporting and decision recommendations.")

    recommendations = [
        "Add time periods, comparison points, and baseline values for stronger executive interpretation.",
        "Separate the most important findings from supporting details.",
        "Translate each metric movement into a business implication."
    ]

    action_items = [
        "Confirm which KPI changes matter most to leadership.",
        "Identify the root cause behind the strongest positive or negative movement.",
        "Prepare a short executive summary for the next leadership discussion."
    ]

    return {
        "executive_summary": executive_summary,
        "key_findings": key_findings,
        "business_risks": business_risks,
        "opportunities": opportunities,
        "recommendations": recommendations,
        "action_items": action_items,
    }