from decimal import Decimal

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.category import Category
from app.domain.enums import CategoryType
from app.domain.transaction import Transaction


class AnalyticsRepository:

    async def get_total_income(
        self,
        db: AsyncSession,
        *,
        user_id: int,
    ) -> Decimal:

        result = await db.scalar(
            select(
                func.coalesce(
                    func.sum(Transaction.amount),
                    0,
                )
            )
            .join(
                Category,
                Transaction.category_id == Category.id,
            )
            .where(
                Transaction.user_id == user_id,
                Category.type == CategoryType.INCOME,
            )
        )

        return Decimal(result)

    async def get_total_expenses(
        self,
        db: AsyncSession,
        *,
        user_id: int,
    ) -> Decimal:

        result = await db.scalar(
            select(
                func.coalesce(
                    func.sum(Transaction.amount),
                    0,
                )
            )
            .join(
                Category,
                Transaction.category_id == Category.id,
            )
            .where(
                Transaction.user_id == user_id,
                Category.type == CategoryType.EXPENSE,
            )
        )

        return Decimal(result)
    
    from sqlalchemy import func, select

# existing imports remain


    async def get_expense_breakdown(
        self,
        db: AsyncSession,
        *,
        user_id: int,
    ):

        result = await db.execute(
            select(
                Category.id,
                Category.name,
                func.sum(Transaction.amount).label(
                    "total_amount"
                ),
            )
            .join(
                Category,
                Transaction.category_id == Category.id,
            )
            .where(
                Transaction.user_id == user_id,
                Category.type == CategoryType.EXPENSE,
            )
            .group_by(
                Category.id,
                Category.name,
            )
            .order_by(
                func.sum(Transaction.amount).desc()
            )
        )

        return result.all()
    
    async def get_monthly_totals(
        self,
        db: AsyncSession,
        *,
        user_id: int,
    ):

        month_expr = func.date_trunc(
            "month",
            Transaction.transaction_date,
        )

        result = await db.execute(
            select(
                month_expr.label("month"),
                Category.type.label("category_type"),
                func.sum(Transaction.amount).label(
                    "total_amount"
                ),
            )
            .join(
                Category,
                Transaction.category_id == Category.id,
            )
            .where(
                Transaction.user_id == user_id,
                Category.type.in_(
                    [
                        CategoryType.INCOME,
                        CategoryType.EXPENSE,
                    ]
                ),
            )
            .group_by(
                month_expr,
                Category.type,
            )
            .order_by(
                month_expr,
            )
        )

        return result.all()

analytics_repository = AnalyticsRepository()