from decimal import Decimal

from pydantic import BaseModel


class SavingsRateResponse(BaseModel):
    total_income: Decimal
    total_expenses: Decimal
    savings_amount: Decimal
    savings_rate: Decimal