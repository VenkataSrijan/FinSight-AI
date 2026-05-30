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
    
    async def get_top_merchants(
        self,
        db: AsyncSession,
        *,
        user_id: int,
    ):
        
        result = await db.execute(
            select(
                Transaction.merchant,
                func.sum(
                    Transaction.amount
                ).label(
                    "total_amount"
                ),
                func.count(
                    Transaction.id
                ).label(
                    "transaction_count"
                ),
            )
            .where(
                Transaction.user_id == user_id,
                Transaction.merchant.is_not(None),
            )
            .group_by(
                Transaction.merchant,
            )
            .order_by(
                func.sum(
                    Transaction.amount
                ).desc()
            )
        )

        return result.all()
    
    from sqlalchemy import func, select

# existing imports remain


    async def get_expense_activity_window(
        self,
        db: AsyncSession,
        *,
        user_id: int,
    ):

        result = await db.execute(
            select(
                func.min(
                    Transaction.transaction_date
                ).label(
                    "first_transaction"
                ),
                func.max(
                    Transaction.transaction_date
                ).label(
                    "last_transaction"
                ),
                func.coalesce(
                    func.sum(
                        Transaction.amount
                    ),
                    0,
                ).label(
                    "total_expenses"
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
        )

        return result.one()
    
    async def get_monthly_expense_totals(
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
                func.sum(
                    Transaction.amount
                ).label(
                    "total_expenses"
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
                month_expr,
            )
            .order_by(
                month_expr.desc(),
            )
            .limit(2)
        )

        return result.all()
    
    async def get_top_expense_merchants(
        self,
        db: AsyncSession,
        *,
        user_id: int,
    ):

        result = await db.execute(
            select(
                Transaction.merchant,
                func.sum(
                    Transaction.amount
                ).label(
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
                Transaction.merchant.is_not(None),
            )
            .group_by(
                Transaction.merchant,
            )
            .order_by(
                func.sum(
                    Transaction.amount
                ).desc()
            )
        )

        return result.all()
    
    async def get_recurring_merchants(
        self,
        db: AsyncSession,
        *,
        user_id: int,
    ):
        result = await db.execute(
            select(
                Transaction.merchant,
                func.count(
                    Transaction.id
                ).label(
                    "transaction_count"
                ),
                func.avg(
                    Transaction.amount
                ).label(
                    "average_amount"
                ),
            )
            .where(
                Transaction.user_id == user_id,
                Transaction.merchant.is_not(None),
            )
            .group_by(
                Transaction.merchant,
            )
            .having(
                func.count(
                    Transaction.id
                ) >= 2
            )
            .order_by(
                func.count(
                    Transaction.id
                ).desc()
            )
        )
        return result.all()
    
    async def get_monthly_category_breakdown(
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
                Category.name.label("category_name"),
                func.sum(
                    Transaction.amount
                ).label(
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
                month_expr,
                Category.name,
            )
            .order_by(
                month_expr.desc(),
            )
        )

        return result.all()

    async def get_spending_heatmap(
        self,
        db: AsyncSession,
        *,
        user_id: int,
    ):

        day_expr = func.extract(
            "dow",
            Transaction.transaction_date,
        )

        result = await db.execute(
            select(
                day_expr.label(
                    "day_of_week"
                ),
                func.count(
                    Transaction.id
                ).label(
                    "transaction_count"
                ),
                func.sum(
                    Transaction.amount
                ).label(
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
                day_expr,
            )
            .order_by(
                day_expr,
            )
        )

        return result.all()
analytics_repository = AnalyticsRepository()