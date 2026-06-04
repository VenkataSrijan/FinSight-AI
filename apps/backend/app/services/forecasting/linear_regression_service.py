from __future__ import annotations

import pandas as pd
from sklearn.linear_model import LinearRegression


class LinearRegressionForecastService:

    def forecast(
        self,
        dataframe: pd.DataFrame,
        target_column: str,
    ) -> float:

        x = dataframe[
            ["month_index"]
        ]

        y = dataframe[
            target_column
        ]

        model = LinearRegression()

        model.fit(
            x,
            y,
        )

        next_month = pd.DataFrame(
            {
                "month_index": [
                    len(dataframe)
                ]
            }
        )

        prediction = model.predict(
            next_month
        )

        return float(
            prediction[0]
        )