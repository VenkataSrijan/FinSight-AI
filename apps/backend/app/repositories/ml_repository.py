from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.ml_feedback import MLFeedback
from app.domain.ml_prediction import MLPrediction


class MLRepository:

    async def create_prediction(
        self,
        db: AsyncSession,
        *,
        user_id: int,
        predicted_category: str,
        confidence: float,
        model_version: str,
    ) -> MLPrediction:

        prediction = MLPrediction(
            user_id=user_id,
            predicted_category=predicted_category,
            confidence=confidence,
            model_version=model_version,
        )

        db.add(prediction)

        await db.commit()

        await db.refresh(prediction)

        return prediction

    async def create_feedback(
        self,
        db: AsyncSession,
        *,
        prediction_id,
        corrected_category: str,
        user_id: int,
    ) -> MLFeedback:

        feedback = MLFeedback(
            prediction_id=prediction_id,
            corrected_category=corrected_category,
            user_id=user_id,
        )

        db.add(feedback)

        await db.commit()

        await db.refresh(feedback)

        return feedback


ml_repository = MLRepository()