from fastapi import APIRouter

from app.features.clarity.schemas import ClarityRequest, ClarityResponse
from app.features.clarity.service import analyze_clarity


router = APIRouter(prefix="/clarity", tags=["Clarity Analyzer"])


@router.post("/analyze", response_model=ClarityResponse)
def analyze(request: ClarityRequest):
    return analyze_clarity(request.text)