from fastapi import APIRouter

router = APIRouter(prefix="/sales", tags=["sales"])


@router.get("/orders")
def list_orders() -> list[dict]:
    # Placeholder implementation
    return [{"id": 1, "total": 100.0}]
