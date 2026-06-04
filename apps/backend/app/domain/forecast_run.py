from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.domain.base import Base,TimestampMixin
from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID


class ForecastRun(Base, TimestampMixin):
    __tablename__ = "forecast_runs"

    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    forecast_model_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(
            "forecast_models.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    forecast_horizon: Mapped[int] = mapped_column(
        Integer,
        default=1,
        nullable=False,
    )

    user = relationship(
        "User",
        back_populates="forecast_runs",
    )

    forecast_model = relationship(
        "ForecastModel",
        back_populates="forecast_runs",
    )

    predictions = relationship(
        "ForecastPrediction",
        back_populates="forecast_run",
        cascade="all, delete-orphan",
    )
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )