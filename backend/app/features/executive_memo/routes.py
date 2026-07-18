from fastapi import APIRouter

from .schemas import (
    ExecutiveMemoRequest,
    ExecutiveMemoResponse,
)

from .service import generate_executive_memo

router = APIRouter(
    prefix="/executive-memo",
    tags=["Executive Memo"],
)


@router.post(
    "/generate",
    response_model=ExecutiveMemoResponse,
)
def generate(
    request: ExecutiveMemoRequest,
):
    return generate_executive_memo(request)