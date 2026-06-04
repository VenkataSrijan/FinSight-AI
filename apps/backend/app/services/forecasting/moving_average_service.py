from __future__ import annotations

import pandas as pd


class MovingAverageForecastService:

    def __init__(
        self,
        window_size: int = 3,
    ):
        self.window_size = window_size

    def forecast(
        self,
        dataframe: pd.DataFrame,
        target_column: str,
    ) -> float:

        if len(dataframe) < self.window_size:
            raise ValueError(
                "Not enough observations."
            )

        recent_values = (
            dataframe[target_column]
            .tail(self.window_size)
        )

        return float(
            recent_values.mean()
        )