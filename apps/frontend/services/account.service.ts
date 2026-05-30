import { apiClient } from "@/lib/api/client";

import type {
  Account,
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
};