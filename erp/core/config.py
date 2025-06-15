from typing import Dict


class Settings:
    """Application configuration settings."""

    def __init__(self):
        # Enabled modules for each customer keyed by customer ID
        self.customer_modules: Dict[str, set[str]] = {}

    def enable_module(self, customer_id: str, module_name: str) -> None:
        modules = self.customer_modules.setdefault(customer_id, set())
        modules.add(module_name)

    def disable_module(self, customer_id: str, module_name: str) -> None:
        modules = self.customer_modules.setdefault(customer_id, set())
        modules.discard(module_name)


settings = Settings()
