from app.repositories.analytics_repository import (
    analytics_repository,
)

from app.schemas.analytics.heatmap import (
    HeatmapItem,
    HeatmapResponse,
)


class HeatmapService:

    async def get_heatmap(
        self,
        db,
        *,
        user_id: int,
    ) -> HeatmapResponse:

        rows = (
            await analytics_repository.get_spending_heatmap(
                db,
                user_id=user_id,
            )
        )

        DAY_NAMES = {
            0: "Sunday",
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
        }

        return HeatmapResponse(
            items=[
                HeatmapItem(
                    day_of_week=DAY_NAMES[
                        int(row.day_of_week)
                    ],
                    transaction_count=row.transaction_count,
                    total_amount=str(
                        row.total_amount
                    ),
                )
                for row in rows
            ]
        )


heatmap_service = HeatmapService()