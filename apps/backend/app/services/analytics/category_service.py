from decimal import Decimal

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.analytics_repository import (
    analytics_repository,
)
from app.schemas.analytics.category import (
    CategoryAnalyticsItem,
    CategoryAnalyticsResponse,
)


class CategoryService:

    async def get_expense_breakdown(
        self,
        db: AsyncSession,
        *,
        user_id: int,
    ) -> CategoryAnalyticsResponse:

        rows = (
            await analytics_repository.get_expense_breakdown(
                db,
                user_id=user_id,
            )
        )

        total_expenses = sum(
            row.total_amount
            for row in rows
        )

        categories = []

        for row in rows:

            percentage = 0.0

            if total_expenses > 0:
                percentage = round(
                    float(
                        (row.total_amount / total_expenses)
                        * 100
                    ),
                    2,
                )

            categories.append(
                CategoryAnalyticsItem(
                    category_id=str(row.id),
                    category_name=row.name,
                    amount=row.total_amount,
                    percentage=percentage,
                )
            )

        return CategoryAnalyticsResponse(
            categories=categories
        )


category_service = CategoryService()