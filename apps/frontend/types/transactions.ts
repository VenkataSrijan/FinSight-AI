export interface Transaction {
  id: string;

  user_id: number;

  account_id: string;

  category_id: string | null;

  amount: string;

  currency: string;

  merchant: string | null;

  description: string | null;

  transaction_date: string;

  posted_at: string | null;

  type: string;

  status: string;

  source: string;

  external_id: string | null;

  notes: string | null;

  metadata_json: Record<string, unknown> | null;

  created_at: string;

  updated_at: string;
}