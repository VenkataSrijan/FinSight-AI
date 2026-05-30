from enum import Enum

from pydantic import BaseModel


class InsightSeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    SUCCESS = "success"


class InsightType(str, Enum):
    SPENDING_SPIKE = "spending_spike"
    SAVINGS_HEALTH = "savings_health"
    MERCHANT_CONCENTRATION = "merchant_concentration"
    SUBSCRIPTION_DETECTED = "subscription_detected"
    CATEGORY_DRIFT = "category_drift"



class InsightItem(BaseModel):
    type: InsightType
    severity: InsightSeverity
    title: str
    description: str


class InsightsResponse(BaseModel):
    insights: list[InsightItem]



