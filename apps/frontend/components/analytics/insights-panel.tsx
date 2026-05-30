"use client";

import type {
  InsightsResponse,
} from "@/types/analytics";

function getSeverityClasses(
  severity: string
): string {
  switch (severity) {
    case "success":
      return (
        "border-green-500/30 " +
        "bg-green-500/5"
      );

    case "warning":
      return (
        "border-amber-500/30 " +
        "bg-amber-500/5"
      );

    case "info":
      return (
        "border-blue-500/30 " +
        "bg-blue-500/5"
      );

    default:
      return (
        "border-border bg-card"
      );
  }
}

function getSeverityIcon(
  severity: string
): string {
  switch (severity) {
    case "success":
      return "🟢";

    case "warning":
      return "🟠";

    case "info":
      return "🔵";

    default:
      return "⚪";
  }
}

interface InsightsPanelProps {
  data?: InsightsResponse;
  isLoading: boolean;
}

export function InsightsPanel({
  data,
  isLoading,
}: InsightsPanelProps): React.JSX.Element {

  if (!data?.insights.length) {
    return (
      <div className="rounded-2xl border border-border bg-card p-6">
        <h2 className="text-xl font-semibold">
          Financial Insights
        </h2>

        <p className="mt-4 text-muted-foreground">
          No insights available yet.
        </p>
      </div>
    );
  }
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
              className={`rounded-xl border p-4 ${getSeverityClasses(
                insight.severity
              )}`}
            >
              <h3 className="font-medium">
                {getSeverityIcon(
                  insight.severity
                )}{" "}
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