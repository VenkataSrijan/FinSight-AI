from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.category import Category
from app.schemas.category import (
    CategoryCreate,
)


class CategoryService:

    async def create_category(
        self,
        db: AsyncSession,
        *,
        user_id: int,
        payload: CategoryCreate,
    ) -> Category:

        existing_category = await db.scalar(
            select(Category).where(
                Category.slug == payload.slug,
                Category.user_id == user_id,
            )
        )

        if existing_category:
            raise ValueError(
                "Category slug already exists"
            )

        category = Category(
            user_id=user_id,
            name=payload.name,
            slug=payload.slug,
            color=payload.color,
            icon=payload.icon,
            type=payload.type,
            is_system=False,
        )

        db.add(category)

        await db.commit()

        await db.refresh(category)

        return category

    async def list_categories(
        self,
        db: AsyncSession,
        *,
        user_id: int,
    ) -> list[Category]:

        result = await db.scalars(
            select(Category)
            .where(
                or_(
                    Category.is_system.is_(True),
                    Category.user_id == user_id,
                )
            )
            .order_by(
                Category.name.asc()
            )
        )

        return list(result.all())

    async def get_category(
        self,
        db: AsyncSession,
        *,
        user_id: int,
        category_id,
    ) -> Category | None:

        category = await db.scalar(
            select(Category).where(
                Category.id == category_id,
                or_(
                    Category.is_system.is_(True),
                    Category.user_id == user_id,
                ),
            )
        )

        return category


category_service = CategoryService()

