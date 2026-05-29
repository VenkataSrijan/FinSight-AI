from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.analytics_repository import (
    analytics_repository,
)
from app.schemas.analytics.merchant import (
    MerchantAnalyticsItem,
    MerchantAnalyticsResponse,
)


class MerchantService:

    async def get_top_merchants(
        self,
        db: AsyncSession,
        *,
        user_id: int,
    ) -> MerchantAnalyticsResponse:

        rows = (
            await analytics_repository.get_top_merchants(
                db,
                user_id=user_id,
            )
        )

        merchants = []

        for row in rows:

            merchants.append(
                MerchantAnalyticsItem(
                    merchant=row.merchant,
                    amount=row.total_amount,
                    transaction_count=row.transaction_count,
                )
            )

        return MerchantAnalyticsResponse(
            merchants=merchants
        )


merchant_service = MerchantService()