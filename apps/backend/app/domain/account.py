from decimal import Decimal
from uuid import uuid4

from sqlalchemy import (
    Boolean,
    Enum,
    ForeignKey,
    Numeric,
    String,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.domain.base import Base, TimestampMixin
from app.domain.enums import AccountType


class Account(Base, TimestampMixin):
    __tablename__ = "accounts"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "name",
            name="uq_accounts_user_name",
        ),
    )

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    from sqlalchemy import Integer
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    institution_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    account_type: Mapped[AccountType] = mapped_column(
        Enum(
        AccountType,
        name="account_type_enum",
        values_callable=lambda obj: [e.value for e in obj],
        ),
        nullable=False,
    )

    currency: Mapped[str] = mapped_column(
        String(3),
        nullable=False,
        default="USD",
    )

    balance: Mapped[Decimal] = mapped_column(
        Numeric(18, 2),
        nullable=False,
        default=0,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    user = relationship(
        "User",
        back_populates="accounts",
    )

    transactions = relationship(
        "Transaction",
        back_populates="account",
        cascade="all, delete-orphan",
    )