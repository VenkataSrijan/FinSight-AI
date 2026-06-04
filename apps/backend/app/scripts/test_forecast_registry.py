import asyncio

from app.dependencies.db import get_db
from app.repositories.forecast_model_repository import (
    ForecastModelRepository,
)
from app.services.forecasting.registry_service import (
    ForecastRegistryService,
)


async def main():

    async for db in get_db():

        repository = (
            ForecastModelRepository(db)
        )

        service = (
            ForecastRegistryService(
                repository
            )
        )

        model = (
            await service.register_model(
                name="Moving Average",
                version="1.0.0",
                model_type="moving_average",
                artifact_path="artifacts/moving_average.pkl",
                mae=2352.88,
                rmse=2696.49,
                mape=0.0,
                r2_score=-3.19,
            )
        )

        await db.commit()

        print(model.id)

        break


asyncio.run(main())