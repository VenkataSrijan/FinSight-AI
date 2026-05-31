from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.auth import get_current_user
from app.dependencies.db import get_db

from app.repositories.ml_repository import (
    ml_repository,
)

from app.schemas.ml.classify import (
    TransactionClassificationRequest,
    TransactionClassificationResponse,
)

from app.schemas.ml.feedback import (
    FeedbackRequest,
    FeedbackResponse,
)

from app.services.ml.feedback_service import (
    feedback_service,
)

from app.services.ml.inference_service import (
    inference_service,
)

router = APIRouter(
    prefix="/ml",
    tags=["Machine Learning"],
)


@router.post(
    "/classify",
    response_model=
    TransactionClassificationResponse,
)
async def classify_transaction(
    payload:
    TransactionClassificationRequest,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(
        get_current_user
    ),
):

    result = (
        inference_service
        .classify_transaction(
            merchant=payload.merchant,
            description=payload.description,
            amount=float(payload.amount),
        )
    )

    prediction = (
        await ml_repository
        .create_prediction(
            db,
            user_id=current_user.id,
            predicted_category=result[
                "predicted_category"
            ],
            confidence=result[
                "confidence"
            ],
            model_version=result[
                "model_name"
            ],
        )
    )

    return (
        TransactionClassificationResponse(
            prediction_id=prediction.id,
            predicted_category=result[
                "predicted_category"
            ],
            confidence=result[
                "confidence"
            ],
            model_name=result[
                "model_name"
            ],
        )
    )


@router.post(
    "/feedback",
    response_model=
    FeedbackResponse,
)
async def submit_feedback(
    payload: FeedbackRequest,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(
        get_current_user
    ),
):

    feedback = (
        await feedback_service
        .submit_feedback(
            db,
            prediction_id=
            payload.prediction_id,
            corrected_category=
            payload.corrected_category,
            user_id=current_user.id,
        )
    )

    return FeedbackResponse(
        id=feedback.id,
        prediction_id=
        feedback.prediction_id,
        corrected_category=
        feedback.corrected_category,
        user_id=
        feedback.user_id,
    )