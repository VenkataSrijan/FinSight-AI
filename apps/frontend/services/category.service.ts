import { apiClient } from "@/lib/api/client";

import type {
  Category,
} from "@/types/categories";

export const categoryService = {
  getCategories(): Promise<Category[]> {
    return apiClient.get<Category[]>(
      "/categories",
      {
        requireAuth: true,
      }
    );
  },
};