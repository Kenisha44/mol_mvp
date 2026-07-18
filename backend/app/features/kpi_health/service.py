from .schemas import KPIHealthResponse

def analyze_kpi_health(data: str) -> KPIHealthResponse:
    return KPIHealthResponse(
        overall_score=84,
        summary="Overall business health is stable with several areas requiring attention.",
        strengths=[
            "Revenue growth remains positive.",
            "Customer acquisition is improving."
        ],
        concerns=[
            "Support ticket volume is elevated.",
            "Customer retention is below target."
        ],
        recommendations=[
            "Improve retention initiatives.",
            "Reduce ticket backlog.",
            "Continue investing in revenue channels."
        ]
    )