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
      subtitle: "Excellent" ,
      accent:
        "border-green-500/30 bg-green-500/5",
    },

    {
      title: "Burn Rate",
      value: burnRate
        ? `$${burnRate.burn_rate}`
        : "$0",
      subtitle: "Monthly Spend",
      accent:
        "border-amber-500/30 bg-amber-500/5",
    },

    {
      title: "Daily Velocity",
      value: velocity
        ? `$${velocity.daily_average}`
        : "$0",
      subtitle: "Per Day",
      accent:
        "border-blue-500/30 bg-blue-500/5",
    },
  ];

  return (
    <div className="grid gap-6 md:grid-cols-3">
      {cards.map((card) => (
        <div
          key={card.title}
          className={`rounded-2xl border p-6 shadow-sm ${card.accent}`}
        >
          <p className="text-sm text-muted-foreground">
            {card.title}
          </p>

          <h3 className="mt-2 text-3xl font-bold">
            <p className="mt-2 text-sm text-muted-foreground">
              {card.subtitle}
            </p>
            {isLoading
              ? "..."
              : card.value}
          </h3>
        </div>
      ))}
    </div>
  );
}