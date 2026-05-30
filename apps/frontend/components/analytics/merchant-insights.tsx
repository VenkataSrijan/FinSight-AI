"use client";

import type {
  MerchantAnalyticsResponse,
} from "@/types/analytics";

interface MerchantInsightsProps {
  data?: MerchantAnalyticsResponse;
  isLoading: boolean;
}

export function MerchantInsights({
  data,
  isLoading,
}: MerchantInsightsProps): React.JSX.Element {
  return (
    <div className="rounded-2xl border border-border bg-card p-6 shadow-sm">
      <h2 className="mb-4 text-xl font-semibold">
        Merchant Insights
      </h2>

      {isLoading ? (
        <p>Loading...</p>
      ) : (
        <table className="w-full">
          <thead>
            <tr className="border-b border-border">
              <th className="pb-3 text-left">
                Merchant
              </th>

              <th className="pb-3 text-right">
                Amount
              </th>

              <th className="pb-3 text-right">
                Transactions
              </th>
            </tr>
          </thead>

          <tbody>
            {data?.merchants.map((merchant) => (
              <tr
                key={merchant.merchant}
                className="border-b border-border"
              >
                <td className="py-3">
                  {merchant.merchant}
                </td>

                <td className="py-3 text-right">
                  ${merchant.amount}
                </td>

                <td className="py-3 text-right">
                  {merchant.transaction_count}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}