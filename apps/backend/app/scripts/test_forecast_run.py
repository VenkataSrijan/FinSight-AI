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

        model = (
            await service.get_active_model()
        )

        run = await (
            service.create_forecast_run(
                user_id=3,
                forecast_model_id=model.id,
            )
        )

        await service.save_prediction(
            forecast_run_id=run.id,
            predicted_income=70043.94,
            predicted_expenses=40701.34,
            predicted_savings=29342.60,
        )

        await db.commit()

        print(run.id)

        break


asyncio.run(main())