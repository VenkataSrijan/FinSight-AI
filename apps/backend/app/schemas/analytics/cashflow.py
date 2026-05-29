from decimal import Decimal

from pydantic import BaseModel


class CashflowResponse(BaseModel):
    total_income: Decimal
    total_expenses: Decimal
    net_cashflow: Decimal
    savings_rate: float
    expense_ratio: float