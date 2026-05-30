"use client";

import { useState } from "react";
import { useMutation, useQueryClient } from "@tanstack/react-query";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

import { transactionService } from "@/services/transaction.service";

interface CreateTransactionFormProps {
  accountId: string;
  categoryId?: string;
}

export function CreateTransactionForm({
  accountId,
  categoryId,
}: CreateTransactionFormProps): React.JSX.Element {
  const queryClient = useQueryClient();

  const [merchant, setMerchant] =
    useState("");

  const [amount, setAmount] =
    useState("");

  const mutation = useMutation({
    mutationFn:
      transactionService.createTransaction,

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["transactions"],
      });

      setMerchant("");
      setAmount("");
    },
  });

  function handleSubmit(
    e: React.FormEvent
  ): void {
    e.preventDefault();

    mutation.mutate({
      account_id: accountId,
      category_id: categoryId,
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