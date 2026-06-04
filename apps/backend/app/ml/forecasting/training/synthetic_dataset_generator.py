from __future__ import annotations

from pathlib import Path
from random import randint, uniform

import pandas as pd


class SyntheticForecastDatasetGenerator:

    def __init__(self) -> None:

        self.dataset_dir = Path(
            "app/ml/forecasting/datasets"
        )

        self.dataset_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def generate(
        self,
        months: int = 36,
    ) -> pd.DataFrame:

        records = []

        income = 50000.0
        expenses = 30000.0

        for month_index in range(months):

            income_growth = uniform(
                -0.01,
                0.03,
            )

            expense_growth = uniform(
                -0.02,
                0.04,
            )

            income *= (
                1 + income_growth
            )

            expenses *= (
                1 + expense_growth
            )

            savings = (
                income - expenses
            )

            cashflow = savings

            records.append(
                {
                    "month_index": month_index,
                    "income": round(
                        income,
                        2,
                    ),
                    "expenses": round(
                        expenses,
                        2,
                    ),
                    "savings": round(
                        savings,
                        2,
                    ),
                    "cashflow": round(
                        cashflow,
                        2,
                    ),
                }
            )

        return pd.DataFrame(records)

    def export_csv(
        self,
        months: int = 36,
        filename: str = (
            "forecast_training_dataset.csv"
        ),
    ) -> str:

        dataframe = self.generate(
            months=months,
        )

        output_path = (
            self.dataset_dir / filename
        )

        dataframe.to_csv(
            output_path,
            index=False,
        )

        return str(output_path)