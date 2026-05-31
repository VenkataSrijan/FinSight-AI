import asyncio

from app.dependencies.db import get_db
from app.services.ml.dataset_service import (
    dataset_service,
)


async def main():

    async for db in get_db():

        path = await dataset_service.export_csv(
            db
        )

        print(
            f"Dataset exported to: {path}"
        )

        break


if __name__ == "__main__":
    asyncio.run(main())