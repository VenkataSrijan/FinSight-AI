"use client";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

import { transactionService } from "@/services/transaction.service";

import { accountService } from "@/services/account.service";
import { useState } from "react";
import { categoryService } from "@/services/category.service";

import {
  useMutation,
  useQuery,
  useQueryClient,
} from "@tanstack/react-query";

export function CreateTransactionForm(): React.JSX.Element {
  const queryClient = useQueryClient();

  const [merchant, setMerchant] =
    useState("");

  const [amount, setAmount] =
    useState("");

  const [accountId, setAccountId] =
    useState("");

  const [
    selectedCategoryId,
    setSelectedCategoryId,
    ] = useState("");

  const {
    data: categories,
    } = useQuery({
    queryKey: ["categories"],
    queryFn:
        categoryService.getCategories,
    });

  const {
    data: accounts,
  } = useQuery({
    queryKey: ["accounts"],
    queryFn:
        accountService.getAccounts,
  });

  const mutation = useMutation({
    mutationFn:
      transactionService.createTransaction,

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["transactions"],
      });

      setMerchant("");
      setAmount("");
      setSelectedCategoryId("");
    },
  });

  function handleSubmit(
    e: React.FormEvent
    ): void {
    e.preventDefault();

    if (!accountId) {
        return;
    }

    mutation.mutate({
        account_id: accountId,
        category_id: selectedCategoryId || undefined,
        amount: Number(amount),
        merchant,
        currency: "USD",
        transaction_date:
        new Date().toISOString(),
        type: "debit",
    });
    }

  return (
    <form
      onSubmit={handleSubmit}
      className="space-y-4 rounded-2xl border border-border p-6"
    >
      <h2 className="text-xl font-semibold">
        New Transaction
      </h2>

      <div>
            <Label>Account</Label>

            <select
                value={accountId}
                onChange={(e) =>
                setAccountId(e.target.value)
                }
                className="w-full rounded-md border border-border px-3 py-2"
            >
                <option value="">
                Select Account
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
        </div>


        <div>
            <Label>Category</Label>

            <select
                value={selectedCategoryId}
                onChange={(e) =>
                setSelectedCategoryId(
                    e.target.value
                )
                }
                className="w-full rounded-md border border-border px-3 py-2"
            >
                <option value="">
                Select Category
                </option>

                {categories?.map((category) => (
                <option
                    key={category.id}
                    value={category.id}
                >
                    {category.name}
                </option>
                ))}
            </select>
            </div>

        <div>
            <Label>Merchant</Label>

            <Input
                value={merchant}
                onChange={(e) =>
                setMerchant(e.target.value)
                }
            />
            </div>

                <div>
                    <Label>Amount</Label>

                    <Input
                    type="number"
                    value={amount}
                    onChange={(e) =>
                        setAmount(e.target.value)
                    }
                    />
      </div>

      <Button
        type="submit"
        disabled={mutation.isPending}
      >
        Create Transaction
      </Button>
    </form>
  );
}