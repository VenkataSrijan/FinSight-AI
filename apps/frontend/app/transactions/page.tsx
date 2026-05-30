"use client";

import { useQuery } from "@tanstack/react-query";

import { AppShell } from "@/components/layout/app-shell";
import { PageContainer } from "@/components/ui/page-container";

import { transactionService } from "@/services/transaction.service";
import {
  TransactionTable,
} from "@/components/transactions/transaction-table";

export default function TransactionsPage(): React.JSX.Element {
  const {
    data: transactions,
    isLoading,
  } = useQuery({
    queryKey: ["transactions"],
    queryFn:
      transactionService.getTransactions,
  });

  return (
    <AppShell>
      <PageContainer>
        <div className="space-y-6">
          <h1 className="text-3xl font-bold">
            Transactions
          </h1>

          {isLoading ? (
            <p>Loading...</p>
          ) : (
            <TransactionTable
                transactions={
                    transactions ?? []
                }
            />
          )}
        </div>
      </PageContainer>
    </AppShell>
  );
}