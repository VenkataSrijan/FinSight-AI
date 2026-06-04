from app.services.forecasting.training_service import (
    ForecastTrainingService,
)

service = (
    ForecastTrainingService()
)

dataframe = (
    service.load_dataset()
)

results = {
    "moving_average": (
        service.train_moving_average(
            dataframe,
            "income",
        )
    ),
    "linear_regression": (
        service.train_linear_regression(
            dataframe,
            "income",
        )
    ),
}

print(results)