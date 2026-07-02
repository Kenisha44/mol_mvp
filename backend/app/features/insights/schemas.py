from pydantic import BaseModel


class InsightRequest(BaseModel):
    text: str


class InsightResponse(BaseModel):
    result: str
    insight_type: str
    label: str