from pydantic import BaseModel


class ForecastModelResponse(
    BaseModel,
):
    id: str

    name: str

    version: str

    model_type: str

    mae: float | None

    rmse: float | None

    mape: float | None

    r2_score: float | None

    is_active: bool


class ForecastPredictionResponse(
    BaseModel,
):
    forecast_month: str

    predicted_income: float

    predicted_expenses: float

    predicted_savings: float

    predicted_cashflow: float