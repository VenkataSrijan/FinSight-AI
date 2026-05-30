"use client";

import { useQuery } from "@tanstack/react-query";

import { AppShell } from "@/components/layout/app-shell";
import { PageContainer } from "@/components/ui/page-container";

import { analyticsService } from "@/services/analytics.service";

import {
  SummaryCards,
} from "@/components/analytics/summary-cards";

import {
  CategoryBreakdown,
} from "@/components/analytics/category-breakdown";

import {
  CashflowCard,
} from "@/components/analytics/cashflow-card";

import {
  MerchantInsights,
} from "@/components/analytics/merchant-insights";

export default function AnalyticsPage(): React.JSX.Element {
  const summaryQuery = useQuery({
    queryKey: ["analytics", "summary"],
    queryFn: analyticsService.getSummary,
  });

  const categoriesQuery = useQuery({
    queryKey: ["analytics", "categories"],
    queryFn: analyticsService.getCategories,
  });

  const cashflowQuery = useQuery({
    queryKey: ["analytics", "cashflow"],
    queryFn: analyticsService.getCashflow,
  });

  const merchantsQuery = useQuery({
    queryKey: ["analytics", "merchants"],
    queryFn: analyticsService.getMerchants,
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

          <div className="grid gap-6 lg:grid-cols-2">
            <CategoryBreakdown
              data={categoriesQuery.data}
              isLoading={categoriesQuery.isLoading}
            />

            <CashflowCard
              data={cashflowQuery.data}
              isLoading={cashflowQuery.isLoading}
            />
          </div>

          <MerchantInsights
            data={merchantsQuery.data}
            isLoading={merchantsQuery.isLoading}
          />
        </div>
      </PageContainer>
    </AppShell>
  );
}