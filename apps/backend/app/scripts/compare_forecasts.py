import pandas as pd

from app.services.forecasting.moving_average_service import (
    MovingAverageForecastService,
)
from app.services.forecasting.linear_regression_service import (
    LinearRegressionForecastService,
)

df = pd.read_csv(
    "app/ml/forecasting/datasets/forecast_training_dataset.csv"
)

ma_service = MovingAverageForecastService(window_size=3)
lr_service = LinearRegressionForecastService()

results = {
    "moving_average": {
        "income": ma_service.forecast(df, "income"),
        "expenses": ma_service.forecast(df, "expenses"),
        "savings": ma_service.forecast(df, "savings"),
    },
    "linear_regression": {
        "income": lr_service.forecast(df, "income"),
        "expenses": lr_service.forecast(df, "expenses"),
        "savings": lr_service.forecast(df, "savings"),
    },
}

print(results)