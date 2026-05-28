import hashlib
from decimal import Decimal
from uuid import UUID
from datetime import datetime


def normalize_string(value: str | None) -> str:
    if not value:
        return ""

    return value.strip().lower()


def normalize_decimal(value: Decimal) -> str:
    return f"{value:.2f}"


def normalize_datetime(value: datetime) -> str:
    return value.isoformat()


def generate_transaction_hash(
    *,
    user_id: int,
    account_id: UUID,
    amount: Decimal,
    merchant: str | None,
    transaction_date: datetime,
) -> str:
    raw_string = "|".join(
        [
            str(user_id),
            str(account_id),
            normalize_decimal(amount),
            normalize_string(merchant),
            normalize_datetime(transaction_date),
        ]
    )

    return hashlib.sha256(
        raw_string.encode("utf-8")
    ).hexdigest()