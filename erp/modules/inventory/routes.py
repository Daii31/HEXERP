from fastapi import APIRouter

router = APIRouter(prefix="/inventory", tags=["inventory"])


@router.get("/items")
def list_items() -> list[dict]:
    # Placeholder implementation
    return [{"id": 1, "name": "Sample Item"}]
