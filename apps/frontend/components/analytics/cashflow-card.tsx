"use client";

import type {
  CashflowResponse,
} from "@/types/analytics";

interface CashflowCardProps {
  data?: CashflowResponse;
  isLoading: boolean;
}

export function CashflowCard({
  data,
  isLoading,
}: CashflowCardProps): React.JSX.Element {
  const metrics = [
    {
      label: "Savings Rate",
      value: `${data?.savings_rate ?? 0}%`,
    },
    {
      label: "Expense Ratio",
      value: `${data?.expense_ratio ?? 0}%`,
    },
    {
      label: "Net Cashflow",
      value: `$${data?.net_cashflow ?? 0}`,
    },
  ];

  return (
    <div className="rounded-2xl border border-border bg-card p-6 shadow-sm">
      <h2 className="mb-4 text-xl font-semibold">
        Cashflow Metrics
      </h2>

      <div className="grid gap-4 md:grid-cols-3">
        {metrics.map((metric) => (
          <div
            key={metric.label}
            className="rounded-xl border border-border p-4"
          >
            <p className="text-sm text-muted-foreground">
              {metric.label}
            </p>

            <p className="mt-2 text-2xl font-bold">
              {isLoading
                ? "..."
                : metric.value}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}