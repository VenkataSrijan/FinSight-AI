import asyncio

from sqlalchemy import select

from app.domain.role import Role
from app.infrastructure.database import AsyncSessionLocal

ROLES = [
    {
        "name": "admin",
        "description": "Platform administrator",
    },
    {
        "name": "analyst",
        "description": "Financial analyst",
    },
    {
        "name": "end_user",
        "description": "Standard platform user",
    },
]


async def seed_roles() -> None:
    async with AsyncSessionLocal() as session:
        for role_data in ROLES:
            existing_role = await session.scalar(
                select(Role).where(
                    Role.name == role_data["name"]
                )
            )

            if existing_role:
                continue

            role = Role(**role_data)

            session.add(role)

        await session.commit()

    print("Roles seeded successfully")


if __name__ == "__main__":
    asyncio.run(seed_roles())