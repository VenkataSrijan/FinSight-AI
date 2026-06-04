import asyncio

from app.dependencies.db import get_db
from app.repositories.forecast_repository import ForecastRepository
from app.services.forecasting.dataset_service import (
    ForecastDatasetService,
)


async def main():
    async for db in get_db():
        repository = ForecastRepository(db)

        service = ForecastDatasetService(repository)

        dataset = await service.build_monthly_dataset(
            user_id=3,
        )

        print(dataset)

        break


asyncio.run(main())