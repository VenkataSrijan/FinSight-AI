from pydantic import BaseModel


class ForecastModelMetrics(BaseModel):
    mae: float
    rmse: float
    mape: float
    r2_score: float