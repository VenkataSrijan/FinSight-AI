export interface Category {
  id: string;

  user_id: number | null;

  name: string;

  slug: string;

  color: string | null;

  icon: string | null;

  type: string;

  is_system: boolean;

  created_at: string;

  updated_at: string;
}