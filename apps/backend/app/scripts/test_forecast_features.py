import asyncio

from app.dependencies.db import get_db
from app.repositories.forecast_repository import ForecastRepository
from app.services.forecasting.dataset_service import (
    ForecastDatasetService,
)
from app.services.forecasting.feature_engineering_service import (
    ForecastFeatureEngineeringService,
)


async def main():
    async for db in get_db():
        repository = ForecastRepository(db)

        dataset_service = ForecastDatasetService(
            repository,
        )

        feature_service = ForecastFeatureEngineeringService(
            dataset_service,
        )

        features = await feature_service.build_features(
            user_id=3,
        )

        print(features)

        break


asyncio.run(main())