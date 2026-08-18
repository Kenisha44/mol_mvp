from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from .schemas import AnalysisExportRequest
from .service import build_analysis_pdf


router = APIRouter(
    prefix="/exports",
    tags=["Exports"]
)


@router.post("/pdf")
def export_pdf(payload: AnalysisExportRequest):
    pdf_buffer = build_analysis_pdf(payload)

    safe_title = (
        payload.title
        .lower()
        .replace(" ", "-")
    )

    filename = f"{safe_title or 'mol-analysis'}.pdf"

    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition":
                f'attachment; filename="{filename}"'
        },
    )