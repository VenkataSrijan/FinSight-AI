from fastapi import APIRouter

from app.api.auth import router as auth_router
from app.api.health import router as health_router
from app.api.transactions import router as transactions_router
from app.api.accounts import router as accounts_router
from app.api.categories import router as categories_router
from app.api.analytics import router as analytics_router
from app.api import ml
from app.api.forecasts import (router as forecasts_router)

api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(auth_router)
api_router.include_router(transactions_router)
api_router.include_router(accounts_router)
api_router.include_router(categories_router)
api_router.include_router(analytics_router)
api_router.include_router(ml.router)
api_router.include_router(forecasts_router)