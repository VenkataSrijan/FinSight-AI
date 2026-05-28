from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from app.domain.enums import AccountType


class AccountCreate(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=100,
    )

    institution_name: str | None = Field(
        default=None,
        max_length=100,
    )

    account_type: AccountType

    currency: str = Field(
        default="USD",
        min_length=3,
        max_length=3,
    )

    balance: Decimal = Field(
        default=0,
    )


class AccountUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )

    institution_name: str | None = Field(
        default=None,
        max_length=100,
    )

    currency: str | None = Field(
        default=None,
        min_length=3,
        max_length=3,
    )

    balance: Decimal | None = None

    is_active: bool | None = None


class AccountResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: UUID

    user_id: int

    name: str

    institution_name: str | None

    account_type: AccountType

    currency: str

    balance: Decimal

    is_active: bool

    created_at: datetime

    updated_at: datetime

