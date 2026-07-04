from .schemas import ExecutiveMemoResponse

def generate_memo(request):

    return ExecutiveMemoResponse(

        title="Weekly Executive Memo",

        summary="Summary...",

        background="Background...",

        findings="Findings...",

        impact="Impact...",

        recommendations="Recommendations...",

        next_steps="Next steps..."

    )