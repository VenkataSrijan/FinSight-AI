from pydantic import BaseModel


class ForecastModelRegistration(
    BaseModel
):
    name: str
    version: str
    model_type: str
    artifact_path: str

    mae: float
    rmse: float
    mape: float
    r2_score: float