from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.analytics_repository import (
    analytics_repository,
)
from app.schemas.analytics.burn_rate import (
    BurnRateResponse,
)


class BurnRateService:

    async def get_burn_rate(
        self,
        db: AsyncSession,
        *,
        user_id: int,
    ) -> BurnRateResponse:

        total_expenses = (
            await analytics_repository.get_total_expenses(
                db,
                user_id=user_id,
            )
        )

        return BurnRateResponse(
            burn_rate=total_expenses,
        )


burn_rate_service = BurnRateService()