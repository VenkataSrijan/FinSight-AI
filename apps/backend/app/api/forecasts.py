from fastapi import APIRouter, Depends

from app.dependencies.forecasting import (
    get_registry_service,
)

from app.services.forecasting.registry_service import (
    ForecastRegistryService,
)

from app.schemas.forecasting.forecast_request import (
    ForecastRunRequest,
)

from app.dependencies.forecasting_inference import (
    get_inference_service,
)

from app.services.forecasting.inference_service import (
    ForecastInferenceService,
)

from uuid import UUID

router = APIRouter(
    prefix="/forecasts",
    tags=["Forecasts"],
)

@router.get(
    "/models",
)
async def list_models(
    service: ForecastRegistryService = Depends(
        get_registry_service
    ),
):
    models = await (
        service.list_models()
    )

    return [
        {
            "id": str(model.id),
            "name": model.name,
            "version": model.version,
            "model_type": model.model_type,
            "mae": model.mae,
            "rmse": model.rmse,
            "mape": model.mape,
            "r2_score": model.r2_score,
            "is_active": model.is_active,
        }
        for model in models
    ]

@router.post(
    "/run",
)
async def run_forecast(
    request: ForecastRunRequest,
    service: ForecastInferenceService = Depends(
        get_inference_service
    ),
):
    return await service.run_forecast(
        user_id=request.user_id,
    )

@router.get(
    "/runs",
)
async def list_runs(
    service: ForecastInferenceService = Depends(
        get_inference_service
    ),
):
    runs = await (
        service.list_runs()
    )

    return [
        {
            "run_id": str(run.id),
            "user_id": run.user_id,
            "forecast_horizon":
                run.forecast_horizon,
            "created_at":
                run.created_at,
        }
        for run in runs
    ]

from uuid import UUID

@router.get(
    "/runs/{run_id}",
)
async def get_run(
    run_id: UUID,
    service: ForecastInferenceService = Depends(
        get_inference_service
    ),
):
    result = await (
        service.get_run_details(
            run_id
        )
    )

    prediction = result["prediction"]

    return {
        "run_id": str(
            result["run"].id
        ),
        "forecast_month":
            prediction.forecast_month,

        "predicted_income":
            round(
                prediction.predicted_income,
                2,
            ),

        "predicted_expenses":
            round(
                prediction.predicted_expenses,
                2,
            ),

        "predicted_savings":
            round(
                prediction.predicted_savings,
                2,
            ),

        "predicted_cashflow":
            round(
                prediction.predicted_cashflow,
                2,
            ),
    }