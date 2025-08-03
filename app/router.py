from fastapi import APIRouter

from app.admin.api.account import router as account_router
from app.plugin.api.plugin import router as plugin_router

router = APIRouter()
router.include_router(plugin_router)
router.include_router(account_router)
