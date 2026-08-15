from pydantic import BaseModel


class DashboardNarrativeRequest(BaseModel):
    text: str


class DashboardNarrativeResponse(BaseModel):
    result: str
    performance_status: str
    label: str

    executive_summary: str
    performance_drivers: str
    risks: str
    recommended_action: str
    outlook: str

    signal_count: int
    positive_signal_count: int
    negative_signal_count: int