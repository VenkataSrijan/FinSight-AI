from decimal import Decimal

from pydantic import BaseModel


class MerchantAnalyticsItem(BaseModel):
    merchant: str
    amount: Decimal
    transaction_count: int


class MerchantAnalyticsResponse(BaseModel):
    merchants: list[MerchantAnalyticsItem]
