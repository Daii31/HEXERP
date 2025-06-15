from importlib import import_module
from typing import Iterable

from ..core.config import settings


def load_enabled_modules(customer_id: str) -> Iterable:
    for module_name in settings.customer_modules.get(customer_id, set()):
        module = import_module(f"erp.modules.{module_name}.routes")
        yield module.router
