from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.db import get_db

from app.repositories.forecast_model_repository import (
    ForecastModelRepository,
)
from app.repositories.forecast_run_repository import (
    ForecastRunRepository,
)
from app.repositories.forecast_prediction_repository import (
    ForecastPredictionRepository,
)

from app.services.forecasting.inference_service import (
    ForecastInferenceService,
)


async def get_inference_service(
    db: AsyncSession = Depends(get_db),
):
    return ForecastInferenceService(
        ForecastModelRepository(db),
        ForecastRunRepository(db),
        ForecastPredictionRepository(db),
    )