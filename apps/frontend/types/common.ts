export type ThemeMode = "light" | "dark" | "system";

export interface PaginationMeta {
  page: number;
  pageSize: number;
  total: number;
  totalPages: number;
}

export interface TimestampedEntity {
  createdAt: string;
  updatedAt: string;
}