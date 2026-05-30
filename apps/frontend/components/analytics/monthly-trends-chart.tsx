"use client";

import ReactECharts from "echarts-for-react";

import type {
  MonthlyTrendsResponse,
} from "@/types/analytics";

interface MonthlyTrendsChartProps {
  data?: MonthlyTrendsResponse;
  isLoading: boolean;
}

export function MonthlyTrendsChart({
  data,
  isLoading,
}: MonthlyTrendsChartProps): React.JSX.Element {
  if (isLoading) {
    return (
      <div className="rounded-2xl border border-border bg-card p-6">
        Loading chart...
      </div>
    );
  }

  const months =
    data?.months.map((item) => item.month) ?? [];

  const income =
    data?.months.map((item) =>
      Number(item.income)
    ) ?? [];

  const expenses =
    data?.months.map((item) =>
      Number(item.expenses)
    ) ?? [];

  const cashflow =
    data?.months.map((item) =>
      Number(item.net_cashflow)
    ) ?? [];

  const option = {
    tooltip: {
      trigger: "axis",
    },

    legend: {
      data: [
        "Income",
        "Expenses",
        "Cashflow",
      ],
    },

    xAxis: {
      type: "category",
      data: months,
    },

    yAxis: {
      type: "value",
    },

    series: [
      {
        name: "Income",
        type: "line",
        smooth: true,
        data: income,
      },
      {
        name: "Expenses",
        type: "line",
        smooth: true,
        data: expenses,
      },
      {
        name: "Cashflow",
        type: "line",
        smooth: true,
        data: cashflow,
      },
    ],
  };

  return (
    <div className="rounded-2xl border border-border bg-card p-6 shadow-sm">
      <h2 className="mb-4 text-xl font-semibold">
        Monthly Trends
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