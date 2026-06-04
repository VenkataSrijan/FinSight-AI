from app.repositories.forecast_model_repository import (
    ForecastModelRepository,
)
from app.repositories.forecast_run_repository import (
    ForecastRunRepository,
)
from app.repositories.forecast_prediction_repository import (
    ForecastPredictionRepository,
)
from app.domain.forecast_run import (
    ForecastRun,
)
from datetime import date

from app.domain.forecast_prediction import (
    ForecastPrediction,
)

from datetime import date
from fastapi import HTTPException

from app.services.forecasting.moving_average_service import (
    MovingAverageForecastService,
)

from app.services.forecasting.forecast_data_loader import (
    ForecastDataLoader,
)


class ForecastInferenceService:

    def __init__(
        self,
        model_repository: ForecastModelRepository,
        run_repository: ForecastRunRepository,
        prediction_repository: ForecastPredictionRepository,
    ):
        self.model_repository = (
            model_repository
        )

        self.run_repository = (
            run_repository
        )

        self.prediction_repository = (
            prediction_repository
        )

        self.data_loader = (
            ForecastDataLoader()
        )

    async def get_active_model(
        self,
    ):
        return await (
            self.model_repository
            .get_active_model()
        )

    async def create_forecast_run(
        self,
        user_id: int,
        forecast_model_id,
    ):
        run = ForecastRun(
            user_id=user_id,
            forecast_model_id=forecast_model_id,
            forecast_horizon=1,
        )

        return await (
            self.run_repository.create(
                run
            )
        )
    
    async def save_prediction(
        self,
        forecast_run_id,
        predicted_income: float,
        predicted_expenses: float,
        predicted_savings: float,
    ):
        prediction = (
            ForecastPrediction(
                forecast_run_id=forecast_run_id,
                forecast_month=date.today(),
                predicted_income=predicted_income,
                predicted_expenses=predicted_expenses,
                predicted_savings=predicted_savings,
                predicted_cashflow=(
                    predicted_income
                    - predicted_expenses
                ),
                confidence_lower=None,
                confidence_upper=None,
            )
        )

        return await (
            self.prediction_repository
            .create(
                prediction
            )
        )
    
    async def generate_forecast(
        self,
        user_id: int,
    ):
        dataframe = (
            self.data_loader.load()
        )

        service = (
            MovingAverageForecastService(
                window_size=3,
            )
        )

        predicted_income = (
            service.forecast(
                dataframe,
                "income",
            )
        )

        predicted_expenses = (
            service.forecast(
                dataframe,
                "expenses",
            )
        )

        predicted_savings = (
            service.forecast(
                dataframe,
                "savings",
            )
        )

        return {
            "predicted_income": round(
                predicted_income,
                2,
            ),
            "predicted_expenses": round(
                predicted_expenses,
                2,
            ),
            "predicted_savings": round(
                predicted_savings,
                2,
            ),
            "predicted_cashflow": round(
                predicted_income
                - predicted_expenses,
                2,
            ),
        }

    async def run_forecast(
        self,
        user_id: int,
    ):
        model = await self.get_active_model()

        run = await self.create_forecast_run(
            user_id=user_id,
            forecast_model_id=model.id,
        )

        forecast = await self.generate_forecast(
            user_id=user_id,
        )

        prediction = await self.save_prediction(
            forecast_run_id=run.id,
            predicted_income=forecast[
                "predicted_income"
            ],
            predicted_expenses=forecast[
                "predicted_expenses"
            ],
            predicted_savings=forecast[
                "predicted_savings"
            ],
        )

        return {
            "run_id": str(run.id),
            "model_name": model.name,
            "model_version": model.version,
            "prediction_id": str(
                prediction.id
            ),
            **forecast,
        }
    
    async def list_runs(
        self,
    ):
        return await (
            self.run_repository
            .list_runs()
        )
    
    async def get_run_details(
        self,
        run_id,
    ):
        run = await (
            self.run_repository
            .get_by_id(run_id)
        )

        if run is None:
            raise HTTPException(
                status_code=404,
                detail="Forecast run not found",
            )

        prediction = await (
            self.prediction_repository
            .get_by_run_id(
                run.id
            )
        )

        return {
            "run": run,
            "prediction": prediction,
        }