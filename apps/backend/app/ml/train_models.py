import asyncio

from app.dependencies.db import get_db
from app.services.ml.training_service import (
    training_service,
)


async def main():

    async for db in get_db():

        logistic_metrics = (
            await training_service.train_logistic_regression(
                db
            )
        )

        print(
            "\nLogistic Regression Metrics:"
        )
        print(logistic_metrics)

        forest_metrics = (
            await training_service.train_random_forest(
                db
            )
        )

        print(
            "\nRandom Forest Metrics:"
        )
        print(forest_metrics)

        break


if __name__ == "__main__":
    asyncio.run(main())