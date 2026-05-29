from collections import defaultdict
from decimal import Decimal
from datetime import date
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

    def _generate_month_range(
        self,
        start_month: str,
        end_month: str,
    ) -> list[str]:

        start_year, start_mon = map(
            int,
            start_month.split("-"),
        )

        end_year, end_mon = map(
            int,
            end_month.split("-"),
        )

        current = date(
            start_year,
            start_mon,
            1,
        )

        end = date(
            end_year,
            end_mon,
            1,
        )

        months = []

        while current <= end:

            months.append(
                current.strftime("%Y-%m")
            )

            if current.month == 12:
                current = date(
                    current.year + 1,
                    1,
                    1,
                )
            else:
                current = date(
                    current.year,
                    current.month + 1,
                    1,
                )

        return months

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

        existing_months = sorted(
            monthly_data.keys()
        )

        months_sorted = (
            self._generate_month_range(
                existing_months[0],
                existing_months[-1],
            )
        )

        trend_items = []

        for month in months_sorted:

            income = monthly_data.get(
                month,
                {},
            ).get(
                "income",
                Decimal("0"),
            )

            expenses = monthly_data.get(
                month,
                {},
            ).get(
                "expenses",
                Decimal("0"),
            )

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