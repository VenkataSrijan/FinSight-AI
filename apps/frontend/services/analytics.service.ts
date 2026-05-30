import { apiClient } from "@/lib/api/client";

import type {
  AnalyticsSummary,
  CategoryAnalyticsResponse,
  MonthlyTrendsResponse,
  CashflowResponse,
  MerchantAnalyticsResponse,
  SavingsRate,
  BurnRate,
  Velocity,
  InsightsResponse,
} from "@/types/analytics";

export const analyticsService = {
  getSummary(): Promise<AnalyticsSummary> {
    return apiClient.get<AnalyticsSummary>(
      "/analytics/summary",
      {
        requireAuth: true,
      }
    );
  },

  getCategories(): Promise<CategoryAnalyticsResponse> {
    return apiClient.get<CategoryAnalyticsResponse>(
      "/analytics/categories",
      {
        requireAuth: true,
      }
    );
  },

  getMonthlyTrends(): Promise<MonthlyTrendsResponse> {
    return apiClient.get<MonthlyTrendsResponse>(
      "/analytics/trends/monthly",
      {
        requireAuth: true,
      }
    );
  },

  getCashflow(): Promise<CashflowResponse> {
    return apiClient.get<CashflowResponse>(
      "/analytics/cashflow",
      {
        requireAuth: true,
      }
    );
  },

  getMerchants(): Promise<MerchantAnalyticsResponse> {
    return apiClient.get<MerchantAnalyticsResponse>(
      "/analytics/merchants",
      {
        requireAuth: true,
      }
    );
  },

  getSavingsRate(): Promise<SavingsRate> {
    return apiClient.get<SavingsRate>(
      "/analytics/savings-rate",
      {
        requireAuth: true,
      }
    );
  },

  getBurnRate(): Promise<BurnRate> {
    return apiClient.get<BurnRate>(
      "/analytics/burn-rate",
      {
        requireAuth: true,
      }
    );
  },

  getVelocity(): Promise<Velocity> {
    return apiClient.get<Velocity>(
      "/analytics/velocity",
      {
        requireAuth: true,
      }
    );
  },

  getInsights(): Promise<InsightsResponse> {
    return apiClient.get<InsightsResponse>(
      "/analytics/insights",
      {
        requireAuth: true,
      }
    );
  },
};