from fastapi import APIRouter

from app.api.routers.v1 import charge

router = APIRouter()
router.include_router(charge.router, tags=["Charge"])
