from app.repositories.forecast_repository import ForecastRepository


class ForecastDatasetService:
    def __init__(
        self,
        repository: ForecastRepository,
    ):
        self.repository = repository

    async def build_monthly_dataset(
        self,
        user_id: int,
    ):
        history = await self.repository.get_monthly_financial_history(
            user_id=user_id,
        )

        return history