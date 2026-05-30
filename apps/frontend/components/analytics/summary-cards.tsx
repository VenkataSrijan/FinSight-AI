"use client";

import type { AnalyticsSummary } from "@/types/analytics";

interface SummaryCardsProps {
  summary?: AnalyticsSummary;
  isLoading: boolean;
}

export function SummaryCards({
  summary,
  isLoading,
}: SummaryCardsProps): React.JSX.Element {
  const cards = [
    {
      title: "Total Income",
      value: summary?.total_income,
    },
    {
      title: "Total Expenses",
      value: summary?.total_expenses,
    },
    {
      title: "Net Cashflow",
      value: summary?.net_cashflow,
    },
  ];

  return (
    <div className="grid gap-6 md:grid-cols-3">
      {cards.map((card) => (
        <div
          key={card.title}
          className="rounded-2xl border border-border bg-card p-6 shadow-sm"
        >
          <p className="text-sm text-muted-foreground">
            {card.title}
          </p>

          <h3 className="mt-2 text-3xl font-bold">
            {isLoading
              ? "..."
              : `$${card.value ?? "0"}`}
          </h3>
        </div>
      ))}
    </div>
  );
}