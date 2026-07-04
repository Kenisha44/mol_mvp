from fastapi import APIRouter

from app.features.dashboard_narrative.schemas import (
    DashboardNarrativeRequest,
    DashboardNarrativeResponse,
)
from app.features.dashboard_narrative.service import generate_dashboard_narrative


router = APIRouter(
    prefix="/dashboard-narrative",
    tags=["Dashboard Narrative Generator"],
)


@router.post("/generate", response_model=DashboardNarrativeResponse)
def generate(request: DashboardNarrativeRequest):
    return generate_dashboard_narrative(request.text)