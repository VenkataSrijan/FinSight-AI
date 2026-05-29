from collections import defaultdict
from decimal import Decimal

from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.enums import CategoryType
from app.repositories.analytics_repository import (
    analytics_repository,
)
from app.schemas.analytics.trends import (
    MonthlyTrendItem,
    MonthlyTrendsResponse,
)


class TrendsService:

    async def get_monthly_trends(
        self,
        db: AsyncSession,
        *,
        user_id: int,
    ) -> MonthlyTrendsResponse:

        rows = await analytics_repository.get_monthly_totals(
            db,
            user_id=user_id,
        )

        monthly_data = defaultdict(
            lambda: {
                "income": Decimal("0"),
                "expenses": Decimal("0"),
            }
        )

        for row in rows:

            month_key = row.month.strftime(
                "%Y-%m"
            )

            if row.category_type == CategoryType.INCOME:
                monthly_data[month_key]["income"] = (
                    row.total_amount
                )

            elif row.category_type == CategoryType.EXPENSE:
                monthly_data[month_key]["expenses"] = (
                    row.total_amount
                )

        if not monthly_data:
            return MonthlyTrendsResponse(
                months=[]
            )

        months_sorted = sorted(
            monthly_data.keys()
        )

        trend_items = []

        for month in months_sorted:

            income = monthly_data[month]["income"]
            expenses = monthly_data[month]["expenses"]

            trend_items.append(
                MonthlyTrendItem(
                    month=month,
                    income=income,
                    expenses=expenses,
                    net_cashflow=income - expenses,
                )
            )

        return MonthlyTrendsResponse(
            months=trend_items
        )


trends_service = TrendsService()