from decimal import Decimal

from pydantic import BaseModel


class CategoryAnalyticsItem(BaseModel):
    category_id: str
    category_name: str
    amount: Decimal
    percentage: float


class CategoryAnalyticsResponse(BaseModel):
    categories: list[CategoryAnalyticsItem]