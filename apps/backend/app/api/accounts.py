from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.auth import get_current_user
from app.dependencies.db import get_db
from app.domain.user import User
from app.schemas.account import (
    AccountCreate,
    AccountResponse,
)
from app.services.account_service import (
    account_service,
)

router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"],
)


@router.post(
    "",
    response_model=AccountResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_account(
    payload: AccountCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> AccountResponse:

    try:
        account = await account_service.create_account(
            db,
            user_id=current_user.id,
            payload=payload,
        )

        return AccountResponse.model_validate(
            account
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )


@router.get(
    "",
    response_model=list[AccountResponse],
)
async def list_accounts(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[AccountResponse]:

    accounts = await account_service.list_accounts(
        db,
        user_id=current_user.id,
    )

    return [
        AccountResponse.model_validate(account)
        for account in accounts
    ]


@router.get(
    "/{account_id}",
    response_model=AccountResponse,
)
async def get_account(
    account_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> AccountResponse:

    account = await account_service.get_account(
        db,
        user_id=current_user.id,
        account_id=account_id,
    )

    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found",
        )

    return AccountResponse.model_validate(
        account
    )

