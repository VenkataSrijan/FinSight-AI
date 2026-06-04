import asyncio

from app.dependencies.db import get_db
from app.repositories.forecast_repository import (
    ForecastRepository,
)
from app.services.forecasting.dataset_service import (
    ForecastDatasetService,
)
from app.services.forecasting.feature_engineering_service import (
    ForecastFeatureEngineeringService,
)
from app.services.forecasting.training_dataset_service import (
    ForecastTrainingDatasetService,
)


async def main():
    async for db in get_db():

        repository = ForecastRepository(db)

        dataset_service = (
            ForecastDatasetService(repository)
        )

        feature_service = (
            ForecastFeatureEngineeringService(
                dataset_service
            )
        )

        training_service = (
            ForecastTrainingDatasetService(
                feature_service
            )
        )

        path = await training_service.export_csv(
            user_id=3,
        )

        print(path)

        break


asyncio.run(main())