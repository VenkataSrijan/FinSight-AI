from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.auth import get_current_user
from app.dependencies.db import get_db
from app.schemas.analytics.summary import AnalyticsSummaryResponse
from app.services.analytics.summary_service import summary_service

from app.schemas.analytics.category import (
    CategoryAnalyticsResponse,
)
from app.services.analytics.category_service import (
    category_service,
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get(
    "/summary",
    response_model=AnalyticsSummaryResponse,
)
async def get_summary(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
) -> AnalyticsSummaryResponse:

    return await summary_service.get_summary(
        db,
        user_id=current_user.id,
    )

@router.get(
    "/categories",
    response_model=CategoryAnalyticsResponse,
)
async def get_categories_breakdown(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
) -> CategoryAnalyticsResponse:

    return await category_service.get_expense_breakdown(
        db,
        user_id=current_user.id,
    )