from decimal import Decimal

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.analytics_repository import (
    analytics_repository,
)
from app.schemas.analytics.savings import (
    SavingsRateResponse,
)


class SavingsService:

    async def get_savings_rate(
        self,
        db: AsyncSession,
        *,
        user_id: int,
    ) -> SavingsRateResponse:

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

        savings_amount = (
            total_income - total_expenses
        )

        if total_income == Decimal("0"):
            savings_rate = Decimal("0")
        else:
            savings_rate = (
                savings_amount / total_income
            ) * Decimal("100")

        return SavingsRateResponse(
            total_income=total_income,
            total_expenses=total_expenses,
            savings_amount=savings_amount,
            savings_rate=savings_rate.quantize(
                Decimal("0.01")
            ),
        )


savings_service = SavingsService()