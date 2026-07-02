from fastapi import FastAPI

from app.core.cors import add_cors_middleware
from app.features.clarity.routes import router as clarity_router
from app.features.kpi_cleaner.routes import router as kpi_cleaner_router
from app.features.insights.routes import router as insights_router

app = FastAPI(
    title="Moon Onyx Labs API",
    version="1.0.0",
    description="Executive intelligence tools for clarity, KPIs, insights, and decision support.",
)

add_cors_middleware(app)
app.include_router(clarity_router)
app.include_router(kpi_cleaner_router)
app.include_router(insights_router)

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