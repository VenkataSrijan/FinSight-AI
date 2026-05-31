from datetime import datetime


class FeatureEngineeringService:

    def combine_text_features(
        self,
        merchant: str,
        description: str,
    ) -> str:

        merchant = merchant or ""
        description = description or ""

        return f"{merchant} {description}".strip()

    def extract_numerical_features(
        self,
        amount: float,
    ) -> dict:

        amount = float(amount)

        return {
            "amount": amount,
            "amount_abs": abs(amount),
        }

    def extract_temporal_features(
        self,
        transaction_date: datetime,
    ) -> dict:

        return {
            "day_of_week": transaction_date.weekday(),
            "month": transaction_date.month,
            "is_weekend": int(transaction_date.weekday() >= 5),
        }

    def build_features(
        self,
        merchant: str,
        description: str,
        amount: float,
        transaction_date: datetime,
    ) -> dict:

        features = {}

        features["text"] = self.combine_text_features(
            merchant,
            description,
        )

        features.update(
            self.extract_numerical_features(amount)
        )

        features.update(
            self.extract_temporal_features(transaction_date)
        )

        return features