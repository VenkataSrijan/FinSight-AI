from decimal import Decimal

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.analytics_repository import (
    analytics_repository,
)

from app.schemas.analytics.insight import (
    InsightItem,
    InsightSeverity,
    InsightsResponse,
    InsightType,
)


class InsightService:

    async def get_insights(
        self,
        db: AsyncSession,
        *,
        user_id: int,
    ) -> InsightsResponse:

        insights: list[InsightItem] = []

        monthly_expenses = (
            await analytics_repository.get_monthly_expense_totals(
                db,
                user_id=user_id,
            )
        )

        print(monthly_expenses)

        if len(monthly_expenses) >= 2:

            current_month = monthly_expenses[0]
            previous_month = monthly_expenses[1]

            previous_total = Decimal(
                previous_month.total_expenses
            )

            current_total = Decimal(
                current_month.total_expenses
            )

            if previous_total > 0:

                increase_percent = (
                    (
                        current_total
                        - previous_total
                    )
                    / previous_total
                ) * Decimal("100")

                if increase_percent >= Decimal("20"):

                    insights.append(
                        InsightItem(
                            type=InsightType.SPENDING_SPIKE,
                            severity=InsightSeverity.WARNING,
                            title="Spending Increased",
                            description=(
                                f"Expenses increased by "
                                f"{increase_percent.quantize(Decimal('0.01'))}% "
                                f"compared to last month."
                            ),
                        )
                    )

                
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

        if total_income > 0:

            savings_rate = (
                (
                    total_income
                    - total_expenses
                )
                / total_income
            ) * Decimal("100")

            if savings_rate >= Decimal("20"):

                insights.append(
                    InsightItem(
                        type=InsightType.SAVINGS_HEALTH,
                        severity=InsightSeverity.SUCCESS,
                        title="Strong Savings Rate",
                        description=(
                            f"You are saving "
                            f"{savings_rate.quantize(Decimal('0.01'))}% "
                            f"of your income."
                        ),
                    )
                )

        expense_merchants = (
            await analytics_repository.get_top_expense_merchants(
                db,
                user_id=user_id,
            )
        )

        if expense_merchants:

            total_expense_spending = sum(
                Decimal(
                    merchant.total_amount
                )
                for merchant in expense_merchants
            )

            top_merchant = expense_merchants[0]

            concentration_percent = (
                Decimal(
                    top_merchant.total_amount
                )
                / total_expense_spending
            ) * Decimal("100")

            if concentration_percent >= Decimal("30"):

                insights.append(
                    InsightItem(
                        type=InsightType.MERCHANT_CONCENTRATION,
                        severity=InsightSeverity.WARNING,
                        title="Spending Concentrated",
                        description=(
                            f"{concentration_percent.quantize(Decimal('0.01'))}% "
                            f"of expenses were spent with "
                            f"{top_merchant.merchant}."
                        ),
                    )
                )
        return InsightsResponse(
            insights=insights
        )


insight_service = InsightService()