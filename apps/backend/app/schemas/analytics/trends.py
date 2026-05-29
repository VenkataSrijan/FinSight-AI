from decimal import Decimal

from pydantic import BaseModel


class MonthlyTrendItem(BaseModel):
    month: str
    income: Decimal
    expenses: Decimal
    net_cashflow: Decimal


class MonthlyTrendsResponse(BaseModel):
    months: list[MonthlyTrendItem]