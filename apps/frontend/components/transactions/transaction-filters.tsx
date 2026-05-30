"use client";

import { useQuery } from "@tanstack/react-query";

import { Button } from "@/components/ui/button";

import { accountService } from "@/services/account.service";

interface TransactionFiltersProps {
  accountId: string;
  transactionType: string;

  onAccountChange: (
    value: string
  ) => void;

  onTypeChange: (
    value: string
  ) => void;
}

export function TransactionFilters({
  accountId,
  transactionType,
  onAccountChange,
  onTypeChange,
}: TransactionFiltersProps): React.JSX.Element {
  const {
    data: accounts,
  } = useQuery({
    queryKey: ["accounts"],
    queryFn:
      accountService.getAccounts,
  });

  return (
    <div className="rounded-2xl border border-border bg-card p-6">
      <h2 className="mb-4 text-lg font-semibold">
        Filters
      </h2>

      <div className="flex gap-4">
        <select
          value={accountId}
          onChange={(e) =>
            onAccountChange(
              e.target.value
            )
          }
          className="rounded-md border border-border px-3 py-2"
        >
          <option value="">
            All Accounts
          </option>

          {accounts?.map((account) => (
            <option
              key={account.id}
              value={account.id}
            >
              {account.name}
            </option>
          ))}
        </select>

        <select
          value={transactionType}
          onChange={(e) =>
            onTypeChange(
              e.target.value
            )
          }
          className="rounded-md border border-border px-3 py-2"
        >
          <option value="">
            All Types
          </option>

          <option value="debit">
            Debit
          </option>

          <option value="credit">
            Credit
          </option>
        </select>

        <Button type="button">
          Filters Active
        </Button>
      </div>
    </div>
  );
}