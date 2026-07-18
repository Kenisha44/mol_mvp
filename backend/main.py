from fastapi import FastAPI

from app.core.cors import add_cors_middleware
from app.features.clarity.routes import router as clarity_router
from app.features.kpi_cleaner.routes import router as kpi_cleaner_router
from app.features.insights.routes import router as insights_router
from app.features.dashboard_narrative.routes import router as dashboard_narrative_router
from app.features.executive_memo.routes import (
    router as executive_memo_router,
)
from app.features.kpi_health.routes import (
    router as kpi_health_router
)


app = FastAPI(
    title="Moon Onyx Labs API",
    version="1.0.0",
    description="Executive intelligence tools for clarity, KPIs, insights, and decision support.",
)
app.include_router(executive_memo_router)

add_cors_middleware(app)
app.include_router(clarity_router)
app.include_router(kpi_cleaner_router)
app.include_router(insights_router)
app.include_router(dashboard_narrative_router)
app.include_router(kpi_health_router)

@app.get("/")
def root():
    return {
        "message": "Moon Onyx Labs API is running",
        "version": "1.0.0",
        "status": "healthy",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "mol-api",
    }