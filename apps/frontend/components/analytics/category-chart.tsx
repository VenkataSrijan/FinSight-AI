"use client";

import ReactECharts from "echarts-for-react";

import type {
  CategoryAnalyticsResponse,
} from "@/types/analytics";

interface CategoryChartProps {
  data?: CategoryAnalyticsResponse;
  isLoading: boolean;
}

export function CategoryChart({
  data,
  isLoading,
}: CategoryChartProps): React.JSX.Element {
  if (isLoading) {
    return (
      <div className="rounded-2xl border border-border bg-card p-6">
        Loading chart...
      </div>
    );
  }

  if (!data?.categories.length) {
    return (
      <div className="rounded-2xl border border-border bg-card p-6">
        <h2 className="text-xl font-semibold">
          Category Breakdown
        </h2>

        <p className="mt-4 text-muted-foreground">
          No category data available.
        </p>
      </div>
    );
  }

  const chartData =
    data?.categories.map((category) => ({
      name: category.category_name,
      value: Number(category.amount),
    })) ?? [];

  const option = {
    tooltip: {
      trigger: "item",
    },

    legend: {
      bottom: 0,
    },

    series: [
      {
        type: "pie",
        radius: "70%",
        data: chartData,
      },
    ],
  };

  return (
    <div className="rounded-2xl border border-border bg-card p-6 shadow-sm">
      <h2 className="mb-4 text-xl font-semibold">
        Category Breakdown
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