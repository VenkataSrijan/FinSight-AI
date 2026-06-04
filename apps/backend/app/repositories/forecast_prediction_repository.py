from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.domain.forecast_prediction import (
    ForecastPrediction,
)


class ForecastPredictionRepository:

    def __init__(
        self,
        db: AsyncSession,
    ):
        self.db = db

    async def create(
        self,
        prediction: ForecastPrediction,
    ) -> ForecastPrediction:

        self.db.add(
            prediction
        )

        await self.db.flush()

        await self.db.refresh(
            prediction
        )

        return prediction
    
    async def get_by_run_id(
        self,
        forecast_run_id,
    ):
        return await self.db.scalar(
            select(
                ForecastPrediction
            ).where(
                ForecastPrediction.forecast_run_id
                == forecast_run_id
            )
        )