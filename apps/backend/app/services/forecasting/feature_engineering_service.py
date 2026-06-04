from app.services.forecasting.dataset_service import (
    ForecastDatasetService,
)

from datetime import datetime

MIN_FORECAST_MONTHS = 3


class ForecastFeatureEngineeringService:
    def __init__(
        self,
        dataset_service: ForecastDatasetService,
    ):
        self.dataset_service = dataset_service

    async def build_features(
        self,
        user_id: int,
    ):
        history = await self.dataset_service.build_monthly_dataset(
            user_id=user_id,
        )

        if len(history) < MIN_FORECAST_MONTHS:
            raise ValueError(
                "Insufficient transaction history for forecasting."
            )

        features = []

        for index, row in enumerate(history):

            month_date = datetime.strptime(
                row["month"],
                "%Y-%m",
            )

            quarter = ((month_date.month - 1) // 3) + 1

            income = row["income"]
            expenses = row["expenses"]
            savings = row["savings"]

            savings_rate = (
                savings / income
                if income > 0
                else 0
            )

            burn_rate = (
                expenses / income
                if income > 0
                else 0
            )

            features.append(
                {
                    "month_index": index,
                    "month": row["month"],
                    "quarter": quarter,
                    "income": income,
                    "expenses": expenses,
                    "savings": savings,
                    "cashflow": row["cashflow"],
                    "savings_rate": round(savings_rate, 4),
                    "burn_rate": round(burn_rate, 4),
                }
            )

        return features