import pandas as pd

from app.services.forecasting.linear_regression_service import (
    LinearRegressionForecastService,
)

dataframe = pd.read_csv(
    "app/ml/forecasting/datasets/forecast_training_dataset.csv"
)

service = (
    LinearRegressionForecastService()
)

print(
    {
        "income": service.forecast(
            dataframe,
            "income",
        ),
        "expenses": service.forecast(
            dataframe,
            "expenses",
        ),
        "savings": service.forecast(
            dataframe,
            "savings",
        ),
    }
)