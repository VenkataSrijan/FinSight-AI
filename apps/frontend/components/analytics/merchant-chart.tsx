"use client";

import ReactECharts from "echarts-for-react";

import type {
  MerchantAnalyticsResponse,
} from "@/types/analytics";

interface MerchantChartProps {
  data?: MerchantAnalyticsResponse;
  isLoading: boolean;
}

export function MerchantChart({
  data,
  isLoading,
}: MerchantChartProps): React.JSX.Element {
  if (isLoading) {
    return (
      <div className="rounded-2xl border border-border bg-card p-6">
        Loading chart...
      </div>
    );
  }

  if (!data?.merchants.length) {
    return (
        <div className="rounded-2xl border border-border bg-card p-6">
        <h2 className="text-xl font-semibold">
            Top Merchants
        </h2>

        <p className="mt-4 text-muted-foreground">
            No merchant data available.
        </p>
        </div>
    );
    }

  const merchants =
    data?.merchants.map(
      (merchant) => merchant.merchant
    ) ?? [];

  const amounts =
    data?.merchants.map(
      (merchant) =>
        Number(merchant.amount)
    ) ?? [];

  const option = {
    tooltip: {
      trigger: "axis",
    },

    xAxis: {
      type: "value",
    },

    yAxis: {
      type: "category",
      data: merchants,
    },

    series: [
      {
        type: "bar",
        data: amounts,
      },
    ],
  };

  return (
    <div className="rounded-2xl border border-border bg-card p-6 shadow-sm">
      <h2 className="mb-4 text-xl font-semibold">
        Top Merchants
      </h2>

      <ReactECharts
        option={option}
        style={{
          height: "400px",
        }}
      />
    </div>
  );
}