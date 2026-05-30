from decimal import Decimal

from pydantic import BaseModel


class VelocityResponse(BaseModel):
    daily_average: Decimal
    weekly_average: Decimal
    monthly_projection: Decimal