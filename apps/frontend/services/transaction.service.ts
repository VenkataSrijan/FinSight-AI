import { apiClient } from "@/lib/api/client";

import type {
  Transaction,
  CreateTransactionRequest,
} from "@/types/transactions";

import type {
  TransactionFilters,
} from "@/types/transactions";

export const transactionService = {
  getTransactions(
    filters?: TransactionFilters
    ): Promise<Transaction[]> {
    const params = new URLSearchParams();

    if (filters?.account_id) {
        params.set(
        "account_id",
        filters.account_id
        );
    }

    if (filters?.transaction_type) {
        params.set(
        "transaction_type",
        filters.transaction_type
        );
    }

    const query = params.toString();

    return apiClient.get<Transaction[]>(
        `/transactions${
        query ? `?${query}` : ""
        }`,
        {
        requireAuth: true,
        }
    );
    },

  createTransaction(
    payload: CreateTransactionRequest
  ): Promise<Transaction> {
    return apiClient.post<Transaction>(
      "/transactions",
      payload,
      {
        requireAuth: true,
      }
    );
  },
};