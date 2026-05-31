from uuid import UUID

from pydantic import BaseModel


class FeedbackRequest(
    BaseModel
):
    prediction_id: UUID

    corrected_category: str


class FeedbackResponse(
    BaseModel
):
    id: UUID

    prediction_id: UUID

    corrected_category: str

    user_id: int