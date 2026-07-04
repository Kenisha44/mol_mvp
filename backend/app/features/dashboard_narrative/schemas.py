from pydantic import BaseModel
from typing import List


class DashboardNarrativeRequest(BaseModel):
    text: str


class DashboardNarrativeResponse(BaseModel):
    executive_summary: str
    key_findings: List[str]
    business_risks: List[str]
    opportunities: List[str]
    recommendations: List[str]
    action_items: List[str]