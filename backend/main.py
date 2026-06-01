from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re
from typing import List

app = FastAPI(title="Moon Onyx Labs Executive Insight Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text: str

def clean_lines(text: str) -> List[str]:
    return [line.strip(" -•\t") for line in text.splitlines() if line.strip(" -•\t")]

@app.get("/")
def read_root():
    return {
        "status": "Moon Onyx Labs backend running",
        "tools": ["clarity", "kpi-cleaner", "insights"]
    }

@app.post("/clarity")
def clarity_analyzer(input: TextInput):
    text = input.text.strip()
    words = re.findall(r"\w+", text)
    word_count = len(words)
    sentence_count = max(1, len(re.findall(r"[.!?]+", text)))
    avg_sentence = word_count / sentence_count if sentence_count else word_count

    score = 88
    if word_count > 180:
        score -= 12
    if avg_sentence > 24:
        score -= 14
    if not any(term in text.lower() for term in ["because", "therefore", "result", "impact", "recommend", "next"]):
        score -= 10
    score = max(42, min(96, score))

    issues = []
    if word_count > 180:
        issues.append("The text may be too long for an executive slide or summary.")
    if avg_sentence > 24:
        issues.append("Sentences are running long; break them into sharper decision-ready points.")
    if "recommend" not in text.lower() and "next" not in text.lower():
        issues.append("Add a clear recommendation or next action.")
    if not issues:
        issues.append("The structure is usable; tighten the wording and strengthen the conclusion.")

    first_sentence = re.split(r"[.!?]", text)[0][:180] if text else "No text provided"
    executive_summary = f"{first_sentence.strip()} — frame the takeaway around business impact, risk, and the next decision."

    return {
        "tool": "Executive Clarity Analyzer",
        "clarity_score": score,
        "executive_summary": executive_summary,
        "issues": issues,
        "improved_bullets": [
            "Lead with the business impact first.",
            "Separate the evidence from the recommendation.",
            "End with a clear next step or decision request."
        ],
        "cta": "Need this turned into a polished executive deck? Route this to Johken Design."
    }

@app.post("/kpi-cleaner")
def kpi_cleaner(input: TextInput):
    raw_lines = clean_lines(input.text)
    cleaned = []

    replacements = {
        "rev": "Revenue",
        "mrr": "Monthly Recurring Revenue",
        "arr": "Annual Recurring Revenue",
        "cust": "Customer",
        "churn": "Churn Rate",
        "cac": "Customer Acquisition Cost",
        "ltv": "Lifetime Value",
        "roi": "Return on Investment",
        "qoq": "Quarter-over-Quarter",
        "yoy": "Year-over-Year",
        "conv": "Conversion Rate",
        "sales": "Sales",
        "profit": "Profit",
        "margin": "Margin"
    }

    for line in raw_lines:
        normalized = line.lower().replace("_", " ").replace("-", " ")
        tokens = normalized.split()
        cleaned_tokens = [replacements.get(t, t.title()) for t in tokens]
        label = " ".join(cleaned_tokens)
        category = (
            "Financial" if any(x in normalized for x in ["rev", "sales", "profit", "margin", "arr", "mrr"])
            else "Customer" if any(x in normalized for x in ["cust", "churn", "cac", "ltv"])
            else "Performance"
        )
        cleaned.append({
            "original": line,
            "clean_label": label,
            "category": category,
            "slide_ready": f"{label}: track trend, variance, and decision impact."
        })

    if not cleaned:
        cleaned = [{
            "original": "No KPI entered",
            "clean_label": "Example: Revenue Growth Rate",
            "category": "Financial",
            "slide_ready": "Revenue Growth Rate: track trend, variance, and decision impact."
        }]

    return {
        "tool": "KPI Cleaner",
        "cleaned_kpis": cleaned,
        "recommendation": "Group KPIs by decision area: Financial, Customer, Operations, and Growth."
    }

@app.post("/insights")
def insight_generator(input: TextInput):
    text = input.text.strip()
    lines = clean_lines(text)
    sample = lines[:5] if lines else [text[:180] or "No input provided"]

    insights = []
    for idx, item in enumerate(sample[:5], start=1):
        insights.append({
            "insight": f"Insight {idx}: {item[:120]}",
            "so_what": "So what: connect this point to revenue, cost, risk, retention, or operational speed.",
            "slide_title": f"Decision Signal {idx}: What changed and why it matters",
            "chart_suggestion": "Bar chart, trend line, or KPI callout depending on the metric."
        })

    return {
        "tool": "Insight Generator Lite",
        "insights": insights,
        "executive_narrative": "Use these insights to build a concise story: what changed, why it matters, and what should happen next.",
        "cta": "Upgrade path: export these insights into a polished executive report or slide deck."
    }
