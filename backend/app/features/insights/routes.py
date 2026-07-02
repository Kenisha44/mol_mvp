from fastapi import APIRouter

from app.features.insights.schemas import InsightRequest, InsightResponse
from app.features.insights.service import generate_insight


router = APIRouter(prefix="/insights", tags=["Insight Generator"])


@router.post("/generate", response_model=InsightResponse)
def generate(request: InsightRequest):
    return generate_insight(request.text)