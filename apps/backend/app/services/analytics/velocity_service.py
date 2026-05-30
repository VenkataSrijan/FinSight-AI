from decimal import Decimal

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.analytics_repository import (
    analytics_repository,
)
from app.schemas.analytics.velocity import (
    VelocityResponse,
)



class VelocityService:

    async def get_velocity(
        self,
        db: AsyncSession,
        *,
        user_id: int,
    ) -> VelocityResponse:

        row = (
            await analytics_repository.get_expense_activity_window(
                db,
                user_id=user_id,
            )
        )

        if (
            row.first_transaction is None
            or row.last_transaction is None
        ):
            return VelocityResponse(
                daily_average=Decimal("0"),
                weekly_average=Decimal("0"),
                monthly_projection=Decimal("0"),
            )

        days_active = (
            row.last_transaction.date()
            - row.first_transaction.date()
        ).days + 1

        days_active = max(
            days_active,
            1,
        )

        total_expenses = Decimal(
            row.total_expenses
        )

        daily_average = (
            total_expenses
            / Decimal(days_active)
        )

        weekly_average = (
            daily_average
            * Decimal("7")
        )

        monthly_projection = (
            daily_average
            * Decimal("30")
        )

        print(row.first_transaction)
        print(row.last_transaction)
        print(days_active)  

        return VelocityResponse(
            daily_average=daily_average.quantize(
                Decimal("0.01")
            ),
            weekly_average=weekly_average.quantize(
                Decimal("0.01")
            ),
            monthly_projection=monthly_projection.quantize(
                Decimal("0.01")
            ),
        )


velocity_service = VelocityService()
