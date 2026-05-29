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