from __future__ import annotations

from datetime import datetime
from pathlib import Path

import joblib

from app.services.ml.feature_engineering_service import (
    FeatureEngineeringService,
)


class InferenceService:

    def __init__(self) -> None:

        self.feature_engineering = (
            FeatureEngineeringService()
        )

        self.models_dir = Path(
            "app/ml/artifacts/models"
        )

        self.vectorizers_dir = Path(
            "app/ml/artifacts/vectorizers"
        )

        self.model_name = (
            "logistic_regression"
        )

        self.model = None
        self.vectorizer = None
        self.label_encoder = None

        self._load_artifacts()

    def _load_artifacts(
        self,
    ) -> None:

        model_path = (
            self.models_dir
            / f"{self.model_name}.pkl"
        )

        vectorizer_path = (
            self.vectorizers_dir
            / (
                f"{self.model_name}"
                "_vectorizer.pkl"
            )
        )

        label_encoder_path = (
            self.vectorizers_dir
            / (
                f"{self.model_name}"
                "_label_encoder.pkl"
            )
        )

        if not model_path.exists():
            return

        self.model = joblib.load(
            model_path
        )

        self.vectorizer = joblib.load(
            vectorizer_path
        )

        self.label_encoder = joblib.load(
            label_encoder_path
        )

    def classify_transaction(
        self,
        *,
        merchant: str | None,
        description: str | None,
        amount: float,
    ) -> dict:

        if self.model is None:
            raise RuntimeError(
                "No trained model found."
            )

        features = (
            self.feature_engineering.build_features(
                merchant=merchant or "",
                description=description or "",
                amount=amount,
                transaction_date=datetime.utcnow(),
            )
        )

        transformed_text = (
            self.vectorizer.transform(
                [features["text"]]
            )
        )

        prediction = (
            self.model.predict(
                transformed_text
            )
        )[0]

        confidence = (
            self.model.predict_proba(
                transformed_text
            )[0]
        )

        predicted_label = (
            self.label_encoder.inverse_transform(
                [prediction]
            )[0]
        )

        return {
            "predicted_category":
                predicted_label,
            "confidence":
                float(max(confidence)),
            "model_name":
                self.model_name,
        }


inference_service = (
    InferenceService()
)