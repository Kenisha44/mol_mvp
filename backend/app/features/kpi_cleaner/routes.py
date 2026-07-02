from fastapi import APIRouter

from app.features.kpi_cleaner.schemas import KpiCleanerRequest, KpiCleanerResponse
from app.features.kpi_cleaner.service import clean_kpi_text


router = APIRouter(prefix="/kpi-cleaner", tags=["KPI Cleaner"])


@router.post("/clean", response_model=KpiCleanerResponse)
def clean(request: KpiCleanerRequest):
    return clean_kpi_text(request.text)