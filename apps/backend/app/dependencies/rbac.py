from collections.abc import Callable

from fastapi import Depends, HTTPException, status

from app.dependencies.auth import get_current_user
from app.domain.user import User


def require_roles(*allowed_roles: str) -> Callable:
    async def role_checker(
        current_user: User = Depends(get_current_user),
    ) -> User:
        user_roles = {
            role.name
            for role in current_user.roles
        }

        if not user_roles.intersection(allowed_roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions",
            )

        return current_user

    return role_checker