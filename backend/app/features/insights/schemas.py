from pydantic import BaseModel


class InsightRequest(BaseModel):
    text: str


class InsightResponse(BaseModel):
    result: str
    insight_type: str
    label: str

    primary_insight: str
    so_what: str
    recommended_action: str
    executive_title: str
    chart_suggestion: str

    positive_signal_count: int
    negative_signal_count: int
    signal_count: int