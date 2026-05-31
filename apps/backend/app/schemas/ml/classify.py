from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel


class TransactionClassificationRequest(
    BaseModel
):
    merchant: str | None = None

    description: str | None = None

    amount: Decimal


class TransactionClassificationResponse(
    BaseModel
):
    prediction_id: UUID

    predicted_category: str

    confidence: float

    model_name: str