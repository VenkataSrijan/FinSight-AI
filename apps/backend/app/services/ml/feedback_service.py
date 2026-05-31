from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.ml_repository import (
    ml_repository,
)


class FeedbackService:

    async def submit_feedback(
        self,
        db: AsyncSession,
        *,
        prediction_id,
        corrected_category: str,
        user_id: int,
    ):

        return await ml_repository.create_feedback(
            db,
            prediction_id=prediction_id,
            corrected_category=corrected_category,
            user_id=user_id,
        )


feedback_service = FeedbackService()