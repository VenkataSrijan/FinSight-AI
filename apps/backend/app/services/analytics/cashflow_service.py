from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.analytics_repository import (
    analytics_repository,
)
from app.schemas.analytics.cashflow import (
    CashflowResponse,
)


class CashflowService:

    async def get_cashflow(
        self,
        db: AsyncSession,
        *,
        user_id: int,
    ) -> CashflowResponse:

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

        savings_rate = 0.0
        expense_ratio = 0.0

        if total_income > 0:

            savings_rate = round(
                float(
                    (net_cashflow / total_income)
                    * 100
                ),
                2,
            )

            expense_ratio = round(
                float(
                    (total_expenses / total_income)
                    * 100
                ),
                2,
            )

        return CashflowResponse(
            total_income=total_income,
            total_expenses=total_expenses,
            net_cashflow=net_cashflow,
            savings_rate=savings_rate,
            expense_ratio=expense_ratio,
        )


cashflow_service = CashflowService()