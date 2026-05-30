from pydantic import BaseModel


class HeatmapItem(BaseModel):
    day_of_week: str
    transaction_count: int
    total_amount: str


class HeatmapResponse(BaseModel):
    items: list[HeatmapItem]