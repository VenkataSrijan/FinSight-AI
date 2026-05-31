from __future__ import annotations

import json
from pathlib import Path

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.preprocessing import LabelEncoder

from app.services.ml.dataset_service import (
    DatasetService,
)


class TrainingService:

    def __init__(self) -> None:

        self.dataset_service = (
            DatasetService()
        )

        self.artifacts_dir = Path(
            "app/ml/artifacts"
        )

        self.models_dir = (
            self.artifacts_dir / "models"
        )

        self.vectorizers_dir = (
            self.artifacts_dir / "vectorizers"
        )

        self.models_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.vectorizers_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def _prepare_features(
        self,
        train_df,
        validation_df,
    ):

        vectorizer = (
            TfidfVectorizer(
                max_features=5000,
                stop_words="english",
            )
        )

        x_train_text = vectorizer.fit_transform(
            train_df["text"]
        )

        x_validation_text = (
            vectorizer.transform(
                validation_df["text"]
            )
        )

        label_encoder = (
            LabelEncoder()
        )

        y_train = (
            label_encoder.fit_transform(
                train_df["label"]
            )
        )

        y_validation = (
            label_encoder.transform(
                validation_df["label"]
            )
        )

        return (
            x_train_text,
            x_validation_text,
            y_train,
            y_validation,
            vectorizer,
            label_encoder,
        )

    def _evaluate(
        self,
        model,
        x_validation,
        y_validation,
    ):

        predictions = model.predict(
            x_validation
        )

        return {
            "accuracy": float(
                accuracy_score(
                    y_validation,
                    predictions,
                )
            ),
            "precision": float(
                precision_score(
                    y_validation,
                    predictions,
                    average="weighted",
                    zero_division=0,
                )
            ),
            "recall": float(
                recall_score(
                    y_validation,
                    predictions,
                    average="weighted",
                    zero_division=0,
                )
            ),
            "f1": float(
                f1_score(
                    y_validation,
                    predictions,
                    average="weighted",
                    zero_division=0,
                )
            ),
        }

    async def train_logistic_regression(
        self,
        db,
    ):

        (
            train_df,
            validation_df,
            _,
        ) = await self.dataset_service.train_validation_test_split(
            db
        )

        (
            x_train,
            x_validation,
            y_train,
            y_validation,
            vectorizer,
            label_encoder,
        ) = self._prepare_features(
            train_df,
            validation_df,
        )

        model = LogisticRegression(
            max_iter=1000,
            random_state=42,
        )

        model.fit(
            x_train,
            y_train,
        )

        metrics = self._evaluate(
            model,
            x_validation,
            y_validation,
        )

        self._save_artifacts(
            model=model,
            vectorizer=vectorizer,
            label_encoder=label_encoder,
            model_name="logistic_regression",
            metrics=metrics,
        )

        return metrics

    async def train_random_forest(
        self,
        db,
    ):

        (
            train_df,
            validation_df,
            _,
        ) = await self.dataset_service.train_validation_test_split(
            db
        )

        (
            x_train,
            x_validation,
            y_train,
            y_validation,
            vectorizer,
            label_encoder,
        ) = self._prepare_features(
            train_df,
            validation_df,
        )

        model = RandomForestClassifier(
            n_estimators=200,
            random_state=42,
        )

        model.fit(
            x_train,
            y_train,
        )

        metrics = self._evaluate(
            model,
            x_validation,
            y_validation,
        )

        self._save_artifacts(
            model=model,
            vectorizer=vectorizer,
            label_encoder=label_encoder,
            model_name="random_forest",
            metrics=metrics,
        )

        return metrics

    def _save_artifacts(
        self,
        *,
        model,
        vectorizer,
        label_encoder,
        model_name: str,
        metrics: dict,
    ):

        joblib.dump(
            model,
            self.models_dir
            / f"{model_name}.pkl",
        )

        joblib.dump(
            vectorizer,
            self.vectorizers_dir
            / f"{model_name}_vectorizer.pkl",
        )

        joblib.dump(
            label_encoder,
            self.vectorizers_dir
            / f"{model_name}_label_encoder.pkl",
        )

        metrics_path = (
            self.models_dir
            / f"{model_name}_metrics.json"
        )

        with open(
            metrics_path,
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                metrics,
                file,
                indent=4,
            )


training_service = TrainingService()