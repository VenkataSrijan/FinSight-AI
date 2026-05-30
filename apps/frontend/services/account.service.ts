import { apiClient } from "@/lib/api/client";

import type {
  Account,
  CreateAccountRequest,
} from "@/types/accounts";

export const accountService = {
  getAccounts(): Promise<Account[]> {
    return apiClient.get<Account[]>(
      "/accounts",
      {
        requireAuth: true,
      }
    );
  },

  createAccount(
    payload: CreateAccountRequest
  ): Promise<Account> {
    return apiClient.post<Account>(
      "/accounts",
      payload,
      {
        requireAuth: true,
      }
    );
  },
};