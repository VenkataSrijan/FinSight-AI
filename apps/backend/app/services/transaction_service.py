from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.hashing import generate_transaction_hash
from app.domain.account import Account
from app.domain.category import Category
from app.domain.transaction import Transaction
from app.schemas.transaction import TransactionCreate


class TransactionService:

    async def create_transaction(
        self,
        db: AsyncSession,
        *,
        user_id: int,
        payload: TransactionCreate,
    ) -> Transaction:

        # Validate account ownership
        account = await db.scalar(
            select(Account).where(
                Account.id == payload.account_id,
                Account.user_id == user_id,
            )
        )

        if not account:
            raise ValueError(
                "Account not found"
            )

        # Reject inactive accounts
        if not account.is_active:
            raise ValueError(
                "Cannot create transaction for inactive account"
            )

        # Validate category ownership
        category = None

        if payload.category_id:
            category = await db.scalar(
                select(Category).where(
                    Category.id == payload.category_id,
                )
            )

            if not category:
                raise ValueError(
                    "Category not found"
                )

            # Allow:
            # - system categories (user_id=None)
            # - user's own categories
            if (
                category.user_id is not None
                and category.user_id != user_id
            ):
                raise ValueError(
                    "Unauthorized category access"
                )

        # Generate deterministic hash
        hash_signature = generate_transaction_hash(
            user_id=user_id,
            account_id=payload.account_id,
            amount=payload.amount,
            merchant=payload.merchant,
            transaction_date=payload.transaction_date,
        )

        # Duplicate detection
        existing_transaction = await db.scalar(
            select(Transaction).where(
                Transaction.user_id == user_id,
                Transaction.hash_signature == hash_signature,
            )
        )

        if existing_transaction:
            raise ValueError(
                "Duplicate transaction detected"
            )

        # Create transaction entity
        transaction = Transaction(
            user_id=user_id,
            account_id=payload.account_id,
            category_id=payload.category_id,
            amount=payload.amount,
            currency=payload.currency,
            merchant=payload.merchant,
            description=payload.description,
            transaction_date=payload.transaction_date,
            posted_at=payload.posted_at,
            type=payload.type,
            status=payload.status,
            source=payload.source,
            external_id=payload.external_id,
            notes=payload.notes,
            metadata_json=payload.metadata_json,
            hash_signature=hash_signature,
        )

        db.add(transaction)

        await db.commit()

        await db.refresh(transaction)

        return transaction
    

    async def get_transaction(
        self,
        db: AsyncSession,
        *,
        user_id: int,
        transaction_id,
    ) -> Transaction | None:

        transaction = await db.scalar(
            select(Transaction).where(
                Transaction.id == transaction_id,
                Transaction.user_id == user_id,
            )
        )

        return transaction
    
    
    async def list_transactions(
        self,
        db: AsyncSession,
        *,
        user_id: int,
        limit: int = 20,
        offset: int = 0,
    ) -> list[Transaction]:

        result = await db.scalars(
            select(Transaction)
            .where(
                Transaction.user_id == user_id,
            )
            .order_by(
                Transaction.transaction_date.desc()
            )
            .limit(limit)
            .offset(offset)
        )

        return list(result.all())





transaction_service = TransactionService()
