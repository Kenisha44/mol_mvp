from pydantic import BaseModel


class TextRequest(BaseModel):
    text: str


class AnalysisResponse(BaseModel):
    result: str