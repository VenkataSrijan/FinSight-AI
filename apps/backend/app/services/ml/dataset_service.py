from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.transaction import Transaction
from app.services.ml.feature_engineering_service import (
    FeatureEngineeringService,
)


class DatasetService:

    def __init__(self) -> None:

        self.feature_engineering = (
            FeatureEngineeringService()
        )

        self.dataset_dir = (
            Path("app/ml/datasets")
        )

        self.dataset_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    async def get_training_transactions(
        self,
        db: AsyncSession,
    ) -> list[Transaction]:

        result = await db.scalars(
            select(Transaction).where(
                Transaction.category_id.is_not(None)
            )
        )

        return list(result.all())

    async def build_dataset(
        self,
        db: AsyncSession,
    ) -> list[dict]:

        transactions = (
            await self.get_training_transactions(db)
        )

        dataset: list[dict] = []

        for transaction in transactions:

            features = (
                self.feature_engineering.build_features(
                    merchant=transaction.merchant or "",
                    description=transaction.description or "",
                    amount=float(transaction.amount),
                    transaction_date=transaction.transaction_date,
                )
            )

            dataset.append(
                {
                    **features,
                    "label": str(
                        transaction.category_id
                    ),
                }
            )

        return dataset

    async def build_dataframe(
        self,
        db: AsyncSession,
    ) -> pd.DataFrame:

        dataset = (
            await self.build_dataset(db)
        )

        return pd.DataFrame(dataset)

    async def export_csv(
        self,
        db: AsyncSession,
        filename: str = "training_dataset.csv",
    ) -> str:

        dataframe = (
            await self.build_dataframe(db)
        )

        output_path = (
            self.dataset_dir / filename
        )

        dataframe.to_csv(
            output_path,
            index=False,
        )

        return str(output_path)

    async def train_validation_test_split(
        self,
        db: AsyncSession,
    ):

        dataframe = (
            await self.build_dataframe(db)
        )

        train_df, temp_df = train_test_split(
            dataframe,
            test_size=0.30,
            random_state=42,
            shuffle=True,
        )

        validation_df, test_df = train_test_split(
            temp_df,
            test_size=0.50,
            random_state=42,
            shuffle=True,
        )

        return (
            train_df,
            validation_df,
            test_df,
        )


dataset_service = DatasetService()