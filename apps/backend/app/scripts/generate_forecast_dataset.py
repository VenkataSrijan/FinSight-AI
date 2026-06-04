from app.ml.forecasting.training.synthetic_dataset_generator import (
    SyntheticForecastDatasetGenerator,
)

generator = (
    SyntheticForecastDatasetGenerator()
)

path = generator.export_csv(
    months=36,
)

print(path)