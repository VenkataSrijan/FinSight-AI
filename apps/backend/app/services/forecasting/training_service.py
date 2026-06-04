from pathlib import Path

import pandas as pd
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

from pathlib import Path

import pandas as pd
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

from app.services.forecasting.linear_regression_service import (
    LinearRegressionForecastService,
)
from app.services.forecasting.moving_average_service import (
    MovingAverageForecastService,
)

class ForecastTrainingService:

    def __init__(self):

        self.dataset_path = Path(
            "app/ml/forecasting/datasets/forecast_training_dataset.csv"
        )

    def load_dataset(
        self,
    ) -> pd.DataFrame:

        return pd.read_csv(
            self.dataset_path
        )
    
    def evaluate(
        self,
        actual,
        predicted,
    ):
        mae = mean_absolute_error(
            actual,
            predicted,
        )

        rmse = (
            mean_squared_error(
                actual,
                predicted,
            )
            ** 0.5
        )

        r2 = r2_score(
            actual,
            predicted,
        )

        return {
            "mae": mae,
            "rmse": rmse,
            "r2_score": r2,
        }
    
    def train_validation_split(
        self,
        dataframe: pd.DataFrame,
        validation_size: int = 6,
    ):
        train_df = dataframe.iloc[:-validation_size]
        validation_df = dataframe.iloc[-validation_size:]

        return train_df, validation_df
    
    def calculate_mape(
        self,
        actual,
        predicted,
    ) -> float:

        actual = pd.Series(actual)
        predicted = pd.Series(predicted)

        mask = actual != 0

        if mask.sum() == 0:
            return 0.0

        return float(
            (
                (
                    (
                        actual[mask]
                        - predicted[mask]
                    ).abs()
                    / actual[mask]
                ).mean()
            ) * 100
        )
    
    def train_validation_split(
        self,
        dataframe: pd.DataFrame,
        validation_size: int = 6,
    ):

        train_df = dataframe.iloc[
            :-validation_size
        ]

        validation_df = dataframe.iloc[
            -validation_size:
        ]

        return (
            train_df,
            validation_df,
        )
    
    def evaluate(
        self,
        actual,
        predicted,
    ):

        mae = mean_absolute_error(
            actual,
            predicted,
        )

        rmse = (
            mean_squared_error(
                actual,
                predicted,
            ) ** 0.5
        )

        r2 = r2_score(
            actual,
            predicted,
        )

        mape = self.calculate_mape(
            actual,
            predicted,
        )

        return {
            "mae": float(mae),
            "rmse": float(rmse),
            "mape": float(mape),
            "r2_score": float(r2),
        }
    
    def train_moving_average(
        self,
        dataframe: pd.DataFrame,
        target_column: str,
    ):

        train_df, validation_df = (
            self.train_validation_split(
                dataframe
            )
        )

        service = (
            MovingAverageForecastService(
                window_size=3
            )
        )

        predictions = []

        for _ in range(
            len(validation_df)
        ):
            predictions.append(
                service.forecast(
                    train_df,
                    target_column,
                )
            )

        actual = validation_df[
            target_column
        ]

        return self.evaluate(
            actual,
            predictions,
        )
    
    def train_linear_regression(
        self,
        dataframe: pd.DataFrame,
        target_column: str,
    ):

        train_df, validation_df = (
            self.train_validation_split(
                dataframe
            )
        )

        service = (
            LinearRegressionForecastService()
        )

        predictions = []

        for _ in range(
            len(validation_df)
        ):
            predictions.append(
                service.forecast(
                    train_df,
                    target_column,
                )
            )

        actual = validation_df[
            target_column
        ]

        return self.evaluate(
            actual,
            predictions,
        )
    
    def compare_models(
        self,
        dataframe: pd.DataFrame,
        target_column: str,
    ):
        moving_average_metrics = (
            self.train_moving_average(
                dataframe,
                target_column,
            )
        )

        linear_regression_metrics = (
            self.train_linear_regression(
                dataframe,
                target_column,
            )
        )

        models = {
            "moving_average":
                moving_average_metrics,
            "linear_regression":
                linear_regression_metrics,
        }

        best_model = min(
            models.items(),
            key=lambda item:
                item[1]["mae"],
        )

        return {
            "best_model": best_model[0],
            "metrics": models,
        }