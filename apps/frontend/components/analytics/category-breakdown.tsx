"use client";

import ReactECharts from "echarts-for-react";

import type {
  CategoryAnalyticsResponse,
} from "@/types/analytics";

interface CategoryBreakdownProps {
  data?: CategoryAnalyticsResponse;
  isLoading: boolean;
}

export function CategoryBreakdown({
  data,
  isLoading,
}: CategoryBreakdownProps): React.JSX.Element {
      const chartData =
            data?.categories.map((category) => ({
            value: Number(category.amount),
            name: category.category_name,
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
                radius: "65%",
                data: chartData,
            },
            ],
        };
  return (
    <div className="rounded-2xl border border-border bg-card p-6 shadow-sm">
      <h2 className="text-xl font-semibold">
        Expense Breakdown
      </h2>

      {isLoading ? (
        <p className="mt-4 text-muted-foreground">
          Loading...
        </p>
      ) : (
        <ReactECharts
           option={option}
           style={{
              height: 350,
           }}
        />
      )}
    </div>
  );
}