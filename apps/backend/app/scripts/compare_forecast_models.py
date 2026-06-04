from app.services.forecasting.training_service import (
    ForecastTrainingService,
)

service = ForecastTrainingService()

dataframe = service.load_dataset()

result = service.compare_models(
    dataframe,
    "income",
)

print(result)