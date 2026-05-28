from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from app.domain.enums import CategoryType


class CategoryCreate(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=100,
    )

    slug: str = Field(
        min_length=1,
        max_length=100,
    )

    color: str | None = Field(
        default=None,
        max_length=20,
    )

    icon: str | None = Field(
        default=None,
        max_length=50,
    )

    type: CategoryType


class CategoryUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )

    color: str | None = Field(
        default=None,
        max_length=20,
    )

    icon: str | None = Field(
        default=None,
        max_length=50,
    )


class CategoryResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: UUID

    user_id: int | None

    name: str

    slug: str

    color: str | None

    icon: str | None

    type: CategoryType

    is_system: bool

    created_at: datetime

    updated_at: datetime

