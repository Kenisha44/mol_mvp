from .schemas import ExecutiveMemoRequest, ExecutiveMemoResponse


def generate_executive_memo(
    request: ExecutiveMemoRequest,
) -> ExecutiveMemoResponse:

    notes = request.notes.strip()

    return ExecutiveMemoResponse(
        title=f"{request.memo_type}",

        summary=(
            "This memo summarizes the most important business updates "
            "provided in the executive notes."
        ),

        background=notes,

        findings=(
            "The submitted notes indicate measurable business activity "
            "that leadership should review."
        ),

        impact=(
            "These observations may influence operational planning, "
            "resource allocation, and executive decision making."
        ),

        recommendations=(
            "Prioritize the highest-impact initiatives, continue "
            "monitoring KPIs, and communicate progress regularly."
        ),

        next_steps=(
            "Validate findings, assign ownership, establish timelines, "
            "and prepare follow-up reporting."
        ),
    )