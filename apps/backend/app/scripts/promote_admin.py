import asyncio

from app.infrastructure.database import AsyncSessionLocal
from app.services.role_service import role_service


async def promote() -> None:
    async with AsyncSessionLocal() as session:
        await role_service.assign_role(
            session,
            user_email="admin@finsight.ai",
            role_name="admin",
        )

    print("Admin role assigned successfully")


if __name__ == "__main__":
    asyncio.run(promote())