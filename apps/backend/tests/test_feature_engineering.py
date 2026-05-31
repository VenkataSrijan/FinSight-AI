from datetime import datetime

from app.services.ml.feature_engineering_service import (
    FeatureEngineeringService,
)


def test_build_features():

    service = FeatureEngineeringService()

    result = service.build_features(
        merchant="Starbucks",
        description="Coffee Purchase",
        amount=250,
        created_at=datetime(2026, 5, 31),
    )

    assert result["text"] == "Starbucks Coffee Purchase"

    assert result["amount"] == 250.0

    assert result["amount_abs"] == 250.0

    assert result["day_of_week"] == 6

    assert result["month"] == 5

    assert result["is_weekend"] == 1