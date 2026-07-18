from fastapi import APIRouter
from .schemas import KPIHealthRequest
from .service import analyze_kpi_health

router = APIRouter(
    prefix="/kpi-health",
    tags=["KPI Health Checker"]
)

@router.post("/analyze")
def analyze(request: KPIHealthRequest):
    return analyze_kpi_health(request.data)