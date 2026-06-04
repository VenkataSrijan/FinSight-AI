from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.forecast_run import ForecastRun
from sqlalchemy import select
from sqlalchemy.orm import selectinload


class ForecastRunRepository:

    def __init__(
        self,
        db: AsyncSession,
    ):
        self.db = db

    async def create(
        self,
        forecast_run: ForecastRun,
    ) -> ForecastRun:

        self.db.add(
            forecast_run
        )

        await self.db.flush()

        await self.db.refresh(
            forecast_run
        )

        return forecast_run
    
    async def list_runs(
        self,
    ):
        result = await self.db.scalars(
            select(ForecastRun)
            .order_by(
                ForecastRun.created_at.desc()
            )
        )

        return list(
            result.all()
        )
    
    async def get_by_id(
        self,
        run_id,
    ):
        return await self.db.get(
            ForecastRun,
            run_id,
        )