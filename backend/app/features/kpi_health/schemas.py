from pydantic import BaseModel

class KPIHealthRequest(BaseModel):
    data: str

class KPIHealthResponse(BaseModel):
    overall_score: int
    summary: str
    strengths: list[str]
    concerns: list[str]
    recommendations: list[str]
