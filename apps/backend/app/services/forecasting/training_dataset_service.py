from __future__ import annotations

from pathlib import Path

import pandas as pd

from app.services.forecasting.feature_engineering_service import (
    ForecastFeatureEngineeringService,
)


class ForecastTrainingDatasetService:

    def __init__(
        self,
        feature_service: ForecastFeatureEngineeringService,
    ) -> None:

        self.feature_service = feature_service

        self.dataset_dir = Path(
            "app/ml/forecasting/datasets"
        )

        self.dataset_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    async def build_dataset(
        self,
        user_id: int,
    ) -> list[dict]:

        return await self.feature_service.build_features(
            user_id=user_id,
        )

    async def build_dataframe(
        self,
        user_id: int,
    ) -> pd.DataFrame:

        dataset = await self.build_dataset(
            user_id=user_id,
        )

        return pd.DataFrame(dataset)

    async def export_csv(
        self,
        user_id: int,
        filename: str = (
            "forecast_training_dataset.csv"
        ),
    ) -> str:

        dataframe = await self.build_dataframe(
            user_id=user_id,
        )

        output_path = (
            self.dataset_dir / filename
        )

        dataframe.to_csv(
            output_path,
            index=False,
        )

        return str(output_path)
    
    