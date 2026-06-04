from sqlalchemy import Boolean, Float, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.domain.base import Base,TimestampMixin
from uuid import uuid4
from sqlalchemy import Boolean, Float, String, UniqueConstraint

from sqlalchemy.dialects.postgresql import UUID


class ForecastModel(Base, TimestampMixin):
    __tablename__ = "forecast_models"

    __table_args__ = (
        UniqueConstraint(
            "name",
            "version",
            name="uq_forecast_model_name_version",
        ),
    )

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    version: Mapped[str] = mapped_column(String(50), nullable=False)

    model_type: Mapped[str] = mapped_column(String(100), nullable=False)
    feature_version: Mapped[str] = mapped_column(String(50), nullable=False)

    mae: Mapped[float | None] = mapped_column(Float, nullable=True)
    rmse: Mapped[float | None] = mapped_column(Float, nullable=True)
    mape: Mapped[float | None] = mapped_column(Float, nullable=True)
    r2_score: Mapped[float | None] = mapped_column(Float, nullable=True)

    artifact_path: Mapped[str] = mapped_column(String(500), nullable=False)

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    forecast_runs = relationship(
        "ForecastRun",
        back_populates="forecast_model",
    )

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )