from typing import Any
from pydantic import BaseModel


class AnalysisExportRequest(BaseModel):
    toolId: str
    toolName: str
    title: str
    status: str | None = None
    preview: str | None = None
    input: str | None = None
    result: dict[str, Any]
    createdAt: str | None = None