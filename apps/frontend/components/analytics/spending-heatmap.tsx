"use client";

import ReactECharts from "echarts-for-react";

import type {
  HeatmapResponse,
} from "@/types/analytics";

interface Props {
  data?: HeatmapResponse;
  isLoading: boolean;
}

const DAYS = [
  "Sunday",
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
  "Saturday",
];

export function SpendingHeatmap({
  data,
  isLoading,
}: Props): React.JSX.Element {
  if (isLoading) {
    return (
      <div className="rounded-2xl border border-border p-6">
        Loading heatmap...
      </div>
    );
  }

  if (!data?.items.length) {
        return (
            <div className="rounded-2xl border border-border bg-card p-6">
            <h2 className="text-xl font-semibold">
                Spending Heatmap
            </h2>

            <p className="mt-4 text-muted-foreground">
                No spending activity available.
            </p>
            </div>
        );
    }

  const values: [string, number][] = DAYS.map(
    (day) => {
      const item =
        data?.items.find(
          (entry) =>
            entry.day_of_week === day
        );

      return [
        day,
        item?.transaction_count ?? 0,
      ];
    }
  );

  const option = {
    tooltip: {
      trigger: "item",
    },

    xAxis: {
      type: "category",
      data: DAYS,
    },

    yAxis: {
      type: "category",
      data: ["Spending"],
    },

    visualMap: {
      min: 0,
      max: Math.max(
        ...values.map(
          (item) => item[1]
        ),
        1
      ),
      calculable: true,
      orient: "horizontal",
      left: "center",
      bottom: 0,
    },

    series: [
      {
        type: "heatmap",
        data: values.map(
          ([, value], index) => [
            index,
            0,
            value,
          ]
        ),
      },
    ],
  };

  return (
    <div className="rounded-2xl border border-border bg-card p-6 shadow-sm">
      <h2 className="mb-4 text-xl font-semibold">
        Spending Heatmap
      </h2>

      <ReactECharts
        option={option}
        style={{
          height: "350px",
        }}
      />
    </div>
  );
}