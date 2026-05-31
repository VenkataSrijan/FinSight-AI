import asyncio

from sqlalchemy import func, select

from app.dependencies.db import get_db
from app.domain.transaction import Transaction


async def main():

    async for db in get_db():

        count = await db.scalar(
            select(func.count())
            .select_from(Transaction)
            .where(Transaction.category_id.is_not(None))
        )

        print(f"Categorized Transactions: {count}")

        break


asyncio.run(main())