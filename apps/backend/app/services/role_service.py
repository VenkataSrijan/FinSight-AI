from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.role import Role
from app.domain.user import User


class RoleService:
    async def assign_role(
        self,
        db: AsyncSession,
        user_email: str,
        role_name: str,
    ) -> None:
        user = await db.scalar(
            select(User).where(User.email == user_email)
        )

        if not user:
            raise ValueError("User not found")

        role = await db.scalar(
            select(Role).where(Role.name == role_name)
        )

        if not role:
            raise ValueError("Role not found")

        existing_roles = {
            r.name
            for r in user.roles
        }

        if role.name in existing_roles:
            return

        user.roles.append(role)

        await db.commit()


role_service = RoleService()