"use client";

import { useQuery } from "@tanstack/react-query";

import { AppShell } from "@/components/layout/app-shell";
import { PageContainer } from "@/components/ui/page-container";

import { accountService } from "@/services/account.service";

import {
  AccountTable,
} from "@/components/accounts/account-table";

import {
  CreateAccountForm,
} from "@/components/accounts/create-account-form";

export default function AccountsPage(): React.JSX.Element {
  const {
    data: accounts,
    isLoading,
  } = useQuery({
    queryKey: ["accounts"],
    queryFn:
      accountService.getAccounts,
  });

  return (
    <AppShell>
      <PageContainer>
        <div className="space-y-6">
          <h1 className="text-3xl font-bold">
            Accounts
          </h1>

          <CreateAccountForm />

          {isLoading ? (
            <p>Loading...</p>
          ) : (
            <AccountTable
              accounts={accounts ?? []}
            />
          )}
        </div>
      </PageContainer>
    </AppShell>
  );
}