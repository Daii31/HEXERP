from fastapi import APIRouter
from .config import settings

router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/customers/{customer_id}/modules/{module_name}/enable")
def enable_customer_module(customer_id: str, module_name: str) -> dict:
    settings.enable_module(customer_id, module_name)
    return {"status": "enabled", "customer": customer_id, "module": module_name}


@router.post("/customers/{customer_id}/modules/{module_name}/disable")
def disable_customer_module(customer_id: str, module_name: str) -> dict:
    settings.disable_module(customer_id, module_name)
    return {"status": "disabled", "customer": customer_id, "module": module_name}
