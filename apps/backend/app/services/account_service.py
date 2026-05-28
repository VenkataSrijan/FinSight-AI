from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.account import Account
from app.schemas.account import (
    AccountCreate,
    AccountUpdate,
)


class AccountService:

    async def create_account(
        self,
        db: AsyncSession,
        *,
        user_id: int,
        payload: AccountCreate,
    ) -> Account:

        existing_account = await db.scalar(
            select(Account).where(
                Account.user_id == user_id,
                Account.name == payload.name,
            )
        )

        if existing_account:
            raise ValueError(
                "Account with this name already exists"
            )

        account = Account(
            user_id=user_id,
            name=payload.name,
            institution_name=payload.institution_name,
            account_type=payload.account_type,
            currency=payload.currency,
            balance=payload.balance,
        )

        db.add(account)

        await db.commit()

        await db.refresh(account)

        return account

    async def list_accounts(
        self,
        db: AsyncSession,
        *,
        user_id: int,
    ) -> list[Account]:

        result = await db.scalars(
            select(Account)
            .where(
                Account.user_id == user_id,
            )
            .order_by(
                Account.created_at.desc()
            )
        )

        return list(result.all())

    async def get_account(
        self,
        db: AsyncSession,
        *,
        user_id: int,
        account_id,
    ) -> Account | None:

        account = await db.scalar(
            select(Account).where(
                Account.id == account_id,
                Account.user_id == user_id,
            )
        )

        return account


account_service = AccountService()

