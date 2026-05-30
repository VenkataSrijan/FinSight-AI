from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.auth import get_current_user
from app.dependencies.db import get_db
from app.schemas.analytics.summary import AnalyticsSummaryResponse
from app.services.analytics.summary_service import summary_service
from app.domain.user import User

from app.schemas.analytics.category import (
    CategoryAnalyticsResponse,
)
from app.services.analytics.category_service import (
    category_service,
)
from app.schemas.analytics.trends import (
    MonthlyTrendsResponse,
)
from app.services.analytics.trends_service import (
    trends_service,
)

from app.schemas.analytics.cashflow import (
    CashflowResponse,
)

from app.services.analytics.cashflow_service import (
    cashflow_service,
)

from app.schemas.analytics.merchant import (
    MerchantAnalyticsResponse,
)

from app.services.analytics.merchant_service import (
    merchant_service,
)

from app.schemas.analytics.savings import (
    SavingsRateResponse,
)

from app.services.analytics.savings_service import (
    savings_service,
)

from app.schemas.analytics.burn_rate import (
    BurnRateResponse,
)

from app.services.analytics.burn_rate_service import (
    burn_rate_service,
)


from app.schemas.analytics.velocity import (
    VelocityResponse,
)

from app.services.analytics.velocity_service import (
    velocity_service,
)

from app.schemas.analytics.insight import (
    InsightsResponse,
)

from app.services.analytics.insight_service import (
    insight_service,
)

from app.schemas.analytics.heatmap import (
    HeatmapResponse,
)

from app.services.analytics.heatmap_service import (
    heatmap_service,
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

@router.get(
    "/trends/monthly",
    response_model=MonthlyTrendsResponse,
)
async def get_monthly_trends(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
) -> MonthlyTrendsResponse:

    return await trends_service.get_monthly_trends(
        db,
        user_id=current_user.id,
    )

@router.get(
    "/cashflow",
    response_model=CashflowResponse,
)
async def get_cashflow(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
) -> CashflowResponse:

    return await cashflow_service.get_cashflow(
        db,
        user_id=current_user.id,
    )

@router.get(
    "/merchants",
    response_model=MerchantAnalyticsResponse,
)
async def get_merchants(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
) -> MerchantAnalyticsResponse:

    return await merchant_service.get_top_merchants(
        db,
        user_id=current_user.id,
    )

@router.get(
    "/savings-rate",
    response_model=SavingsRateResponse,
)
async def get_savings_rate(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
) -> SavingsRateResponse:

    return await savings_service.get_savings_rate(
        db,
        user_id=current_user.id,
    )

@router.get(
    "/burn-rate",
    response_model=BurnRateResponse,
)
async def get_burn_rate(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
) -> BurnRateResponse:

    return await burn_rate_service.get_burn_rate(
        db,
        user_id=current_user.id,
    )

@router.get(
    "/velocity",
    response_model=VelocityResponse,
)
async def get_velocity(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
) -> VelocityResponse:

    return await velocity_service.get_velocity(
        db,
        user_id=current_user.id,
    )

@router.get(
    "/insights",
    response_model=InsightsResponse,
)
async def get_insights(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
) -> InsightsResponse:

    return await insight_service.get_insights(
        db,
        user_id=current_user.id,
        
    )

@router.get(
    "/heatmap",
    response_model=HeatmapResponse,
)
async def get_heatmap(
    db: AsyncSession = Depends(
        get_db,
    ),
    current_user: User = Depends(
        get_current_user,
    ),
):
    return await heatmap_service.get_heatmap(
        db,
        user_id=current_user.id,
    )
