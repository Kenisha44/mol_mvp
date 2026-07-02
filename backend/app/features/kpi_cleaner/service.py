def clean_kpi_text(text: str) -> dict:
    issues = []

    if "%" not in text and any(word in text.lower() for word in ["growth", "increase", "decrease", "conversion"]):
        issues.append("Consider adding percentages for clearer KPI context.")

    if "$" not in text and any(word in text.lower() for word in ["revenue", "sales", "profit", "cost"]):
        issues.append("Consider adding currency values for financial KPIs.")

    if not any(char.isdigit() for char in text):
        issues.append("No numbers detected. KPIs should include measurable values.")

    if len(text.split()) > 120:
        issues.append("KPI explanation may be too long. Consider shortening it.")

    if not issues:
        issues.append("KPI text is clear, measurable, and executive-ready.")

    issues_found = 0 if issues == ["KPI text is clear, measurable, and executive-ready."] else len(issues)

    label = "Clean KPI" if issues_found == 0 else "Needs cleanup"

    result = "KPI Cleaner Results:\n\n" + "\n".join(f"- {issue}" for issue in issues)

    return {
        "result": result,
        "issues_found": issues_found,
        "label": label,
    }