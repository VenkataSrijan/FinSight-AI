import { apiClient } from "@/lib/api/client";

import type {
  Transaction,
} from "@/types/transactions";

export const transactionService = {
  getTransactions(): Promise<Transaction[]> {
    return apiClient.get<Transaction[]>(
      "/transactions",
      {
        requireAuth: true,
      }
    );
  },
};