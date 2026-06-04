from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.db import get_db

from app.repositories.forecast_model_repository import (
    ForecastModelRepository,
)

from app.services.forecasting.registry_service import (
    ForecastRegistryService,
)


async def get_registry_service(
    db: AsyncSession = Depends(
        get_db
    ),
):
    repository = (
        ForecastModelRepository(db)
    )

    return ForecastRegistryService(
        repository
    )