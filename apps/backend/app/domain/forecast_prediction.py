from datetime import date

from sqlalchemy import Date, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.domain.base import Base,TimestampMixin
from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID


class ForecastPrediction(Base, TimestampMixin):
    __tablename__ = "forecast_predictions"

    forecast_run_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(
            "forecast_runs.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    forecast_month: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    predicted_income: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    predicted_expenses: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    predicted_savings: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    predicted_cashflow: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    confidence_lower: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    confidence_upper: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    forecast_run = relationship(
        "ForecastRun",
        back_populates="predictions",
    )

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )