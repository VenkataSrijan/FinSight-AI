from pathlib import Path

import pandas as pd


class ForecastDataLoader:

    DATASET_PATH = (
        Path(
            "app/ml/forecasting/datasets/"
            "forecast_training_dataset.csv"
        )
    )

    def load(self) -> pd.DataFrame:

        return pd.read_csv(
            self.DATASET_PATH
        )