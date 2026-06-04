from sqlalchemy import case, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.enums import TransactionType
from app.domain.transaction import Transaction


class ForecastRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_monthly_financial_history(
        self,
        user_id: int,
    ):
        month_bucket = func.date_trunc(
            "month",
            Transaction.transaction_date,
        )

        stmt = (
            select(
                month_bucket.label("month"),
                func.coalesce(
                    func.sum(
                        case(
                            (
                                Transaction.type
                                == TransactionType.CREDIT,
                                Transaction.amount,
                            ),
                            else_=0,
                        )
                    ),
                    0,
                ).label("income"),
                func.coalesce(
                    func.sum(
                        case(
                            (
                                Transaction.type
                                == TransactionType.DEBIT,
                                Transaction.amount,
                            ),
                            else_=0,
                        )
                    ),
                    0,
                ).label("expenses"),
            )
            .where(Transaction.user_id == user_id)
            .group_by(month_bucket)
            .order_by(month_bucket)
        )

        result = await self.db.execute(stmt)

        rows = result.all()

        history = []

        for row in rows:
            income = float(row.income)
            expenses = float(row.expenses)

            history.append(
                {
                    "month": row.month.strftime("%Y-%m"),
                    "income": income,
                    "expenses": expenses,
                    "savings": income - expenses,
                    "cashflow": income - expenses,
                }
            )

        return history