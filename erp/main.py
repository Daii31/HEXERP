from fastapi import FastAPI, Request

from .core.admin import router as admin_router
from .modules import load_enabled_modules

app = FastAPI(title="HEXERP")
app.include_router(admin_router)


@app.middleware("http")
async def add_customer_modules(request: Request, call_next):
    customer_id = request.headers.get("X-Customer-ID")
    if customer_id:
        for router in load_enabled_modules(customer_id):
            app.include_router(router)
    response = await call_next(request)
    return response


@app.get("/")
async def root() -> dict:
    return {"message": "Welcome to HEXERP"}
