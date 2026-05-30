"use client";

import { useQuery } from "@tanstack/react-query";

import { AppShell } from "@/components/layout/app-shell";
import { PageContainer } from "@/components/ui/page-container";

import { transactionService } from "@/services/transaction.service";
import {
  TransactionTable,
} from "@/components/transactions/transaction-table";

import {
  CreateTransactionForm,
} from "@/components/transactions/create-transaction-form";

import { useState } from "react";

import {
  TransactionFilters,
} from "@/components/transactions/transaction-filters";


export default function TransactionsPage(): React.JSX.Element {

  const [accountId, setAccountId] =
    useState("");

  const [transactionType, setTransactionType] =
    useState("");

  const {
        data: transactions,
        isLoading,
    } = useQuery({
    queryKey: [
        "transactions",
        accountId,
        transactionType,
    ],

    queryFn: () =>
        transactionService.getTransactions({
        account_id:
            accountId || undefined,

        transaction_type:
            transactionType || undefined,
        }),
    });

  return (
    <AppShell>
      <PageContainer>
        <div className="space-y-6">
          <h1 className="text-3xl font-bold">
            Transactions
          </h1>

          <TransactionFilters
                accountId={accountId}
                transactionType={transactionType}
                onAccountChange={setAccountId}
                onTypeChange={setTransactionType}
          />

          <CreateTransactionForm />

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