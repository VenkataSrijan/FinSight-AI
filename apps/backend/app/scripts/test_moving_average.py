import pandas as pd

from app.services.forecasting.moving_average_service import (
    MovingAverageForecastService,
)

dataframe = pd.read_csv(
    "app/ml/forecasting/datasets/forecast_training_dataset.csv"
)

service = (
    MovingAverageForecastService(
        window_size=3,
    )
)

income_forecast = service.forecast(
    dataframe,
    "income",
)

expense_forecast = service.forecast(
    dataframe,
    "expenses",
)

savings_forecast = service.forecast(
    dataframe,
    "savings",
)

print(
    {
        "income": income_forecast,
        "expenses": expense_forecast,
        "savings": savings_forecast,
    }
)