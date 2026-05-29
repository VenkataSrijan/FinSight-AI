"use client";

import { useQuery } from "@tanstack/react-query";
import { AppShell } from "@/components/layout/app-shell";
import { PageContainer } from "@/components/ui/page-container";
import { QUERY_KEYS } from "@/lib/constants";
import { healthService } from "@/services/health.service";
import { analyticsService } from "@/services/analytics.service";

export default function Home(): React.JSX.Element {
  const { data, error, isLoading } = useQuery({
    queryKey: QUERY_KEYS.health,
    queryFn: healthService.getHealth,
    retry: false,
  });

  return (
    <AppShell>
      <PageContainer>
        <div className="space-y-8">
          <div>
            <p className="text-sm font-medium uppercase tracking-[0.2em] text-muted-foreground">
              FinSight AI
            </p>

            <h1 className="mt-4 text-4xl font-semibold tracking-tight lg:text-6xl">
              Enterprise Financial Intelligence Platform
            </h1>

            <p className="mt-6 max-w-3xl text-lg text-muted-foreground">
              AI-powered transaction intelligence, forecasting,
              anomaly detection, behavioral analytics, and
              real-time financial observability.
            </p>

            <p className="mt-4 text-sm text-muted-foreground">
              Backend health:{" "}
              {isLoading
                ? "checking..."
                : error
                ? `error: ${error.message}`
                : data?.status}
            </p>
          </div>

          <div className="grid gap-6 md:grid-cols-3">
            {[
              "Transaction Intelligence",
              "Cash Flow Forecasting",
              "Real-Time Anomaly Detection",
            ].map((item) => (
              <div
                key={item}
                className="rounded-2xl border border-border bg-card p-6 shadow-sm"
              >
                <h3 className="font-semibold tracking-tight">{item}</h3>
              </div>
            ))}
          </div>
        </div>
      </PageContainer>
    </AppShell>
  );
}

const {
  data: summary,
  isLoading: summaryLoading,
} = useQuery({
  queryKey: ["analytics", "summary"],
  queryFn: analyticsService.getSummary,
});