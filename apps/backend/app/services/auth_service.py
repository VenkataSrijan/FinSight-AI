from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.role import Role

from app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    hash_password,
    verify_password,
)
from app.domain.user import User
from app.schemas.auth import (
    LoginRequest,
    SignupRequest,
    TokenResponse,
)


class AuthService:
    async def signup(
        self,
        db: AsyncSession,
        payload: SignupRequest,
    ) -> User:
        existing_user = await db.scalar(
            select(User).where(User.email == payload.email)
        )

        if existing_user:
            raise ValueError("Email already registered")

        user = User(
            email=payload.email,
            full_name=payload.full_name,
            hashed_password=hash_password(payload.password),
        )

        default_role = await db.scalar(
            select(Role).where(Role.name == "end_user")
        )

        if default_role:
            user.roles.append(default_role)

        db.add(user)

        await db.commit()
        await db.refresh(user)

        return user

    async def login(
        self,
        db: AsyncSession,
        payload: LoginRequest,
    ) -> TokenResponse:
        user = await db.scalar(
            select(User).where(User.email == payload.email)
        )

        if not user:
            raise ValueError("Invalid credentials")

        if not verify_password(
            payload.password,
            user.hashed_password,
        ):
            raise ValueError("Invalid credentials")

        return TokenResponse(
            access_token=create_access_token(str(user.id)),
            refresh_token=create_refresh_token(str(user.id)),
        )

    async def refresh_access_token(
        self,
        db: AsyncSession,
        refresh_token: str,
    ) -> TokenResponse:
        try:
            payload = decode_token(refresh_token)
        except ValueError as exc:
            raise ValueError("Invalid refresh token") from exc

        if payload.get("type") != "refresh":
            raise ValueError("Invalid token type")

        user_id = payload.get("sub")

        if not user_id:
            raise ValueError("Invalid token payload")

        user = await db.scalar(
            select(User).where(User.id == int(user_id))
        )

        if not user:
            raise ValueError("User not found")

        return TokenResponse(
            access_token=create_access_token(str(user.id)),
            refresh_token=refresh_token,
        )


auth_service = AuthService()