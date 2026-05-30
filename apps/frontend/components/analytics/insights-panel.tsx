"use client";

import type {
  InsightsResponse,
} from "@/types/analytics";

interface InsightsPanelProps {
  data?: InsightsResponse;
  isLoading: boolean;
}

export function InsightsPanel({
  data,
  isLoading,
}: InsightsPanelProps): React.JSX.Element {
  return (
    <div className="rounded-2xl border border-border bg-card p-6 shadow-sm">
      <h2 className="text-xl font-semibold">
        Financial Insights
      </h2>

      <div className="mt-4 space-y-4">
        {isLoading ? (
          <p className="text-muted-foreground">
            Loading insights...
          </p>
        ) : data?.insights.length ? (
          data.insights.map((insight) => (
            <div
              key={`${insight.type}-${insight.title}`}
              className="rounded-xl border border-border p-4"
            >
              <h3 className="font-medium">
                {insight.title}
              </h3>

              <p className="mt-1 text-sm text-muted-foreground">
                {insight.description}
              </p>
            </div>
          ))
        ) : (
          <p className="text-muted-foreground">
            No insights available.
          </p>
        )}
      </div>
    </div>
  );
}