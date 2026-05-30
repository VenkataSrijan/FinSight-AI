"use client";

import { useQuery } from "@tanstack/react-query";

import { AppShell } from "@/components/layout/app-shell";
import { PageContainer } from "@/components/ui/page-container";

import { analyticsService } from "@/services/analytics.service";

import {
  SummaryCards,
} from "@/components/analytics/summary-cards";

import {
  CashflowCard,
} from "@/components/analytics/cashflow-card";

import {
  IntelligenceCards,
} from "@/components/analytics/intelligence-cards";

import {
  InsightsPanel,
} from "@/components/analytics/insights-panel";

import {
  MonthlyTrendsChart,
} from "@/components/analytics/monthly-trends-chart";

import {
  CategoryChart,
} from "@/components/analytics/category-chart";

import {
  MerchantChart,
} from "@/components/analytics/merchant-chart";

import {
  SpendingHeatmap,
} from "@/components/analytics/spending-heatmap";


export default function AnalyticsPage(): React.JSX.Element {
  const summaryQuery = useQuery({
    queryKey: ["analytics", "summary"],
    queryFn: analyticsService.getSummary,
  });

  const categoriesQuery = useQuery({
    queryKey: ["analytics", "categories"],
    queryFn: analyticsService.getCategories,
  });

  const trendsQuery = useQuery({
    queryKey: ["analytics", "trends"],
    queryFn: analyticsService.getMonthlyTrends,
    });

  const cashflowQuery = useQuery({
    queryKey: ["analytics", "cashflow"],
    queryFn: analyticsService.getCashflow,
  });

  const merchantsQuery = useQuery({
        queryKey: ["analytics", "merchants"],
        queryFn: analyticsService.getMerchants,
    });

    const savingsQuery = useQuery({
    queryKey: ["analytics", "savings-rate"],
    queryFn: analyticsService.getSavingsRate,
    });

    const burnRateQuery = useQuery({
    queryKey: ["analytics", "burn-rate"],
    queryFn: analyticsService.getBurnRate,
    });

    const velocityQuery = useQuery({
    queryKey: ["analytics", "velocity"],
    queryFn: analyticsService.getVelocity,
    });

    const insightsQuery = useQuery({
    queryKey: ["analytics", "insights"],
    queryFn: analyticsService.getInsights,
    });

    const heatmapQuery = useQuery({
      queryKey: ["analytics", "heatmap"],
      queryFn: analyticsService.getHeatmap,
    });

  return (
    <AppShell>
      <PageContainer>
        <div className="space-y-8">
          <h1 className="text-3xl font-bold">
            Analytics
          </h1>

          <SummaryCards
            summary={summaryQuery.data}
            isLoading={summaryQuery.isLoading}
          />

          <IntelligenceCards
                savings={savingsQuery.data}
                burnRate={burnRateQuery.data}
                velocity={velocityQuery.data}
                isLoading={
                    savingsQuery.isLoading ||
                    burnRateQuery.isLoading ||
                    velocityQuery.isLoading
                }
            />

            <MonthlyTrendsChart
                data={trendsQuery.data}
                isLoading={trendsQuery.isLoading}
            />

          <div className="grid gap-6 lg:grid-cols-2">
            <CategoryChart
                data={categoriesQuery.data}
                isLoading={categoriesQuery.isLoading}
            />

            <CashflowCard
              data={cashflowQuery.data}
              isLoading={cashflowQuery.isLoading}
            />
          </div>

          <MerchantChart
            data={merchantsQuery.data}
            isLoading={merchantsQuery.isLoading}
          />

          <SpendingHeatmap
            data={heatmapQuery.data}
            isLoading={
              heatmapQuery.isLoading
            }
          />

          <InsightsPanel
                data={insightsQuery.data}
                isLoading={insightsQuery.isLoading}
            />
        </div>
      </PageContainer>
    </AppShell>
  );
}