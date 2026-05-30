from decimal import Decimal

from pydantic import BaseModel


class BurnRateResponse(BaseModel):
    burn_rate: Decimal