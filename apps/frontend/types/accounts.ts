export interface Account {
  id: string;

  user_id: number;

  name: string;

  institution_name: string | null;

  account_type: string;

  currency: string;

  balance: string;

  is_active: boolean;

  created_at: string;

  updated_at: string;
}