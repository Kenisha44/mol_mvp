from pydantic import BaseModel


class KpiCleanerRequest(BaseModel):
    text: str


class KpiCleanerResponse(BaseModel):
    result: str
    issues_found: int
    label: str