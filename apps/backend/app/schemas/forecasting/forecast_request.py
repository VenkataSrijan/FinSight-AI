from pydantic import BaseModel


class ForecastRunRequest(
    BaseModel,
):
    user_id: int

    forecast_horizon: int = 1