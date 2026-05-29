from decimal import Decimal

from pydantic import BaseModel


class AnalyticsSummaryResponse(BaseModel):
    total_income: Decimal
    total_expenses: Decimal
    net_cashflow: Decimal