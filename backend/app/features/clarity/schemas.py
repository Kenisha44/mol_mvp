from pydantic import BaseModel


class ClarityRequest(BaseModel):
    text: str


class ClarityResponse(BaseModel):
    result: str
    score: int
    label: str
    recommendation: str
    refined_text: str