from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.auth import get_current_user
from app.domain.user import User
from app.dependencies.db import get_db
from app.schemas.transaction import (
    TransactionCreate,
    TransactionResponse,
)
from app.services.transaction_service import (
    transaction_service,
)

from datetime import datetime
from app.domain.enums import (
    TransactionStatus,
    TransactionType,
)

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
)


@router.post(
    "",
    response_model=TransactionResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_transaction(
    payload: TransactionCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> TransactionResponse:

    try:
        transaction = await transaction_service.create_transaction(
            db,
            user_id=current_user.id,
            payload=payload,
        )

        return TransactionResponse.model_validate(
            transaction
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )


@router.get(
    "/{transaction_id}",
    response_model=TransactionResponse,
)
async def get_transaction(
    transaction_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> TransactionResponse:

    transaction = await transaction_service.get_transaction(
        db,
        user_id=current_user.id,
        transaction_id=transaction_id,
    )

    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found",
        )

    return TransactionResponse.model_validate(
        transaction
    )


@router.get(
    "",
    response_model=list[TransactionResponse],
)
async def list_transactions(
    limit: int = 20,
    offset: int = 0,
    account_id: UUID | None = None,
    category_id: UUID | None = None,
    transaction_type: TransactionType | None = None,
    status: TransactionStatus | None = None,
    start_date: datetime | None = None,
    end_date: datetime | None = None,
    sort_by: str = "transaction_date",
    sort_order: str = "desc",
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[TransactionResponse]:

    transactions = await transaction_service.list_transactions(
        db,
        user_id=current_user.id,
        limit=limit,
        offset=offset,
        account_id=account_id,
        category_id=category_id,
        transaction_type=transaction_type,
        status=status,
        start_date=start_date,
        end_date=end_date,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    return [
        TransactionResponse.model_validate(tx)
        for tx in transactions
    ]

