import { apiClient } from "@/lib/api/client";

import type {
  AnalyticsSummary,
  CategoryAnalyticsResponse,
  MonthlyTrendsResponse,
  CashflowResponse,
  MerchantAnalyticsResponse,
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
};