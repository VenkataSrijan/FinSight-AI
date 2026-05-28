from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from app.domain.enums import (
    TransactionSource,
    TransactionStatus,
    TransactionType,
)


class TransactionCreate(BaseModel):
    account_id: UUID
    category_id: UUID | None = None

    amount: Decimal = Field(
        gt=0,
    )

    currency: str = Field(
        min_length=3,
        max_length=3,
    )

    merchant: str | None = None
    description: str | None = None

    transaction_date: datetime
    posted_at: datetime | None = None

    type: TransactionType

    status: TransactionStatus = (
        TransactionStatus.POSTED
    )

    source: TransactionSource = (
        TransactionSource.MANUAL
    )

    external_id: str | None = None

    notes: str | None = None

    metadata_json: dict | None = None


class TransactionResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: UUID

    user_id: int

    account_id: UUID

    category_id: UUID | None

    amount: Decimal

    currency: str

    merchant: str | None

    description: str | None

    transaction_date: datetime

    posted_at: datetime | None

    type: TransactionType

    status: TransactionStatus

    source: TransactionSource

    external_id: str | None

    notes: str | None

    metadata_json: dict | None

    created_at: datetime

    updated_at: datetime

