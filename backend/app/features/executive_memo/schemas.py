from pydantic import BaseModel


class ExecutiveMemoRequest(BaseModel):
    notes: str
    memo_type: str
    audience: str
    tone: str


class ExecutiveMemoResponse(BaseModel):
    title: str
    summary: str
    background: str
    findings: str
    impact: str
    recommendations: str
    next_steps: str