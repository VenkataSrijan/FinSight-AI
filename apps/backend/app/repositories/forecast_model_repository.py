from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.forecast_model import ForecastModel


class ForecastModelRepository:

    def __init__(
        self,
        db: AsyncSession,
    ):
        self.db = db

    async def create(
        self,
        model: ForecastModel,
    ) -> ForecastModel:

        self.db.add(model)

        await self.db.flush()

        await self.db.refresh(model)

        return model

    async def get_active_model(
        self,
    ) -> ForecastModel | None:

        result = await self.db.scalar(
            select(ForecastModel).where(
                ForecastModel.is_active.is_(True)
            )
        )

        return result

    async def deactivate_all(
        self,
    ) -> None:

        result = await self.db.scalars(
            select(ForecastModel)
        )

        models = result.all()

        for model in models:
            model.is_active = False

    async def list_models(
        self,
    ):
        result = await self.db.scalars(
            select(ForecastModel)
            .order_by(
                ForecastModel.created_at.desc()
            )
        )

        return list(
            result.all()
        )