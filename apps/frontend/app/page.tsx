"use client";

import { useQuery } from "@tanstack/react-query";
import { AppShell } from "@/components/layout/app-shell";
import { PageContainer } from "@/components/ui/page-container";
import { QUERY_KEYS } from "@/lib/constants";
import { healthService } from "@/services/health.service";
import { analyticsService } from "@/services/analytics.service";
import { useAuthStore } from "@/store/auth-store";
import { SummaryCards } from "@/components/analytics/summary-cards";
import {
  CategoryBreakdown,
} from "@/components/analytics/category-breakdown";

import {
  MonthlyTrends,
} from "@/components/analytics/monthly-trends";

import {
  MerchantInsights,
} from "@/components/analytics/merchant-insights";

import {
  CashflowCard,
} from "@/components/analytics/cashflow-card";  

export default function Home(): React.JSX.Element {

  const accessToken = useAuthStore(
    (state) => state.accessToken
  );

  const { data, error, isLoading } = useQuery({
    queryKey: QUERY_KEYS.health,
    queryFn: healthService.getHealth,
    retry: false,
  });

  const {
    data: summary,
    isLoading: summaryLoading,
    error: _summaryError,
  } = useQuery({
    queryKey: ["analytics", "summary"],
    queryFn: analyticsService.getSummary,
    enabled: !!accessToken,
  });

  const {
    data: categories,
    isLoading: categoriesLoading,
    error: categoriesError,
  } = useQuery({
    queryKey: ["analytics", "categories"],
    queryFn: analyticsService.getCategories,
    enabled: !!accessToken,
  });

  const {
    data: trends,
    isLoading: trendsLoading,
  } = useQuery({
    queryKey: ["analytics", "trends"],
    queryFn: analyticsService.getMonthlyTrends,
    enabled: !!accessToken,
  });

  const {
    data: merchants,
    isLoading: merchantsLoading,
  } = useQuery({
    queryKey: ["analytics", "merchants"],
    queryFn: analyticsService.getMerchants,
    enabled: !!accessToken,
  });

  const {
    data: cashflow,
    isLoading: cashflowLoading,
  } = useQuery({
    queryKey: ["analytics", "cashflow"],
    queryFn: analyticsService.getCashflow,
    enabled: !!accessToken,
  });

  console.log("CATEGORIES ERROR:", categoriesError);

  console.log("SUMMARY:", summary);
  console.log("CATEGORIES:", categories);

  console.log("SUMMARY LOADING:", summaryLoading);
  console.log("CATEGORIES LOADING:", categoriesLoading);

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

          <SummaryCards
            summary={summary}
            isLoading={summaryLoading}
          />
          <CategoryBreakdown
            data={categories}
            isLoading={categoriesLoading}
          />
          <MonthlyTrends
            data={trends}
            isLoading={trendsLoading}
          />
          <MerchantInsights
            data={merchants}
            isLoading={merchantsLoading}
          />
          <CashflowCard
            data={cashflow}
            isLoading={cashflowLoading}
          />
        </div>
      </PageContainer>
    </AppShell>
  );
}

