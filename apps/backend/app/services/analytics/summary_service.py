from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.analytics_repository import (
    analytics_repository,
)
from app.schemas.analytics.summary import (
    AnalyticsSummaryResponse,
)


class SummaryService:

    async def get_summary(
        self,
        db: AsyncSession,
        *,
        user_id: int,
    ) -> AnalyticsSummaryResponse:

        total_income = (
            await analytics_repository.get_total_income(
                db,
                user_id=user_id,
            )
        )

        total_expenses = (
            await analytics_repository.get_total_expenses(
                db,
                user_id=user_id,
            )
        )

        net_cashflow = (
            total_income - total_expenses
        )

        return AnalyticsSummaryResponse(
            total_income=total_income,
            total_expenses=total_expenses,
            net_cashflow=net_cashflow,
        )


summary_service = SummaryService()