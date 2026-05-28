from decimal import Decimal
from uuid import uuid4

from sqlalchemy import (
    Enum,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    String,
    UniqueConstraint,
    DateTime,
)
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.domain.base import Base, TimestampMixin
from app.domain.enums import (
    TransactionSource,
    TransactionStatus,
    TransactionType,
)


class Transaction(Base, TimestampMixin):
    __tablename__ = "transactions"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "hash_signature",
            name="uq_transactions_user_hash",
        ),
        Index(
            "ix_transactions_user_id",
            "user_id",
        ),
        Index(
            "ix_transactions_account_id",
            "account_id",
        ),
        Index(
            "ix_transactions_category_id",
            "category_id",
        ),
        Index(
            "ix_transactions_transaction_date",
            "transaction_date",
        ),
        Index(
            "ix_transactions_posted_at",
            "posted_at",
        ),
        Index(
            "ix_transactions_user_date",
            "user_id",
            "transaction_date",
        ),
    )

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    account_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("accounts.id", ondelete="CASCADE"),
        nullable=False,
    )

    category_id: Mapped[UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("categories.id", ondelete="SET NULL"),
        nullable=True,
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(18, 2),
        nullable=False,
    )

    currency: Mapped[str] = mapped_column(
        String(3),
        nullable=False,
        default="USD",
    )

    merchant: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    transaction_date: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    posted_at: Mapped[DateTime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    type: Mapped[TransactionType] = mapped_column(
        Enum(
            TransactionType,
            name="transaction_type_enum",
            values_callable=lambda obj: [e.value for e in obj],
        ),
        nullable=False,
    )

    status: Mapped[TransactionStatus] = mapped_column(
        Enum(
            TransactionStatus,
            name="transaction_status_enum",
            values_callable=lambda obj: [e.value for e in obj],
        ),
        nullable=False,
        default=TransactionStatus.POSTED,
    )

    source: Mapped[TransactionSource] = mapped_column(
        Enum(
            TransactionSource,
            name="transaction_source_enum",
            values_callable=lambda obj: [e.value for e in obj],
        ),
        nullable=False,
        default=TransactionSource.MANUAL,
    )

    external_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    hash_signature: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )

    notes: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    metadata_json: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    user = relationship(
        "User",
        back_populates="transactions",
    )

    account = relationship(
        "Account",
        back_populates="transactions",
    )

    category = relationship(
        "Category",
        back_populates="transactions",
    )