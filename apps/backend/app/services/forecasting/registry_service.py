from app.domain.forecast_model import (
    ForecastModel,
)
from app.repositories.forecast_model_repository import (
    ForecastModelRepository,
)


class ForecastRegistryService:

    def __init__(
        self,
        repository: ForecastModelRepository,
    ):
        self.repository = repository


    async def register_model(
        self,
        name: str,
        version: str,
        model_type: str,
        artifact_path: str,
        mae: float,
        rmse: float,
        mape: float,
        r2_score: float,
        is_active: bool = True,
    ):
        if is_active:
            await self.repository.deactivate_all()

        model = ForecastModel(
            name=name,
            version=version,
            model_type=model_type,
            feature_version="v1",
            artifact_path=artifact_path,
            mae=mae,
            rmse=rmse,
            mape=mape,
            r2_score=r2_score,
            is_active=is_active,
        )

        return await self.repository.create(
            model
        )
    
    async def list_models(
        self,
    ):
        return await (
            self.repository
            .list_models()
        )