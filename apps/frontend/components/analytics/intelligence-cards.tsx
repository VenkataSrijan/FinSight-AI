"use client";

import type {
  SavingsRate,
  BurnRate,
  Velocity,
} from "@/types/analytics";

interface IntelligenceCardsProps {
  savings?: SavingsRate;
  burnRate?: BurnRate;
  velocity?: Velocity;
  isLoading: boolean;
}

export function IntelligenceCards({
  savings,
  burnRate,
  velocity,
  isLoading,
}: IntelligenceCardsProps): React.JSX.Element {
  const cards = [
    {
      title: "Savings Rate",
      value: savings
        ? `${savings.savings_rate}%`
        : "0%",
    },
    {
      title: "Burn Rate",
      value: burnRate
        ? `$${burnRate.burn_rate}`
        : "$0",
    },
    {
      title: "Daily Velocity",
      value: velocity
        ? `$${velocity.daily_average}`
        : "$0",
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
              : card.value}
          </h3>
        </div>
      ))}
    </div>
  );
}