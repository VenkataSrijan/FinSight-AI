export interface AnalyticsSummary {
  total_income: string;
  total_expenses: string;
  net_cashflow: string;
}

export interface CategoryAnalyticsItem {
  category_id: string;
  category_name: string;
  amount: string;
  percentage: number;
}

export interface CategoryAnalyticsResponse {
  categories: CategoryAnalyticsItem[];
}

export interface MonthlyTrendItem {
  month: string;
  income: string;
  expenses: string;
  net_cashflow: string;
}

export interface MonthlyTrendsResponse {
  months: MonthlyTrendItem[];
}

export interface CashflowResponse {
  total_income: string;
  total_expenses: string;
  net_cashflow: string;
  savings_rate: number;
  expense_ratio: number;
}

export interface MerchantAnalyticsItem {
  merchant: string;
  amount: string;
  transaction_count: number;
}

export interface MerchantAnalyticsResponse {
  merchants: MerchantAnalyticsItem[];
}

export interface SavingsRate {
  total_income: string;
  total_expenses: string;
  savings_amount: string;
  savings_rate: string;
}

export interface BurnRate {
  burn_rate: string;
}

export interface Velocity {
  daily_average: string;
  weekly_average: string;
  monthly_projection: string;
}

export type InsightSeverity =
  | "info"
  | "warning"
  | "success";

export type InsightType =
  | "spending_spike"
  | "savings_health"
  | "merchant_concentration";

export interface Insight {
  type: InsightType;
  severity: InsightSeverity;
  title: string;
  description: string;
}

export interface InsightsResponse {
  insights: Insight[];
}

export interface HeatmapItem {
  day_of_week: string;
  transaction_count: number;
  total_amount: string;
}

export interface HeatmapResponse {
  items: HeatmapItem[];
}