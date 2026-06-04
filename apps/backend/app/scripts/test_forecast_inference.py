import asyncio

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


async def main():

    async for db in get_db():

        model_repo = (
            ForecastModelRepository(db)
        )

        run_repo = (
            ForecastRunRepository(db)
        )

        prediction_repo = (
            ForecastPredictionRepository(db)
        )

        service = (
            ForecastInferenceService(
                model_repo,
                run_repo,
                prediction_repo,
            )
        )

        model = await (
            service.get_active_model()
        )

        print(
            model.name,
            model.version,
        )

        break


asyncio.run(main())