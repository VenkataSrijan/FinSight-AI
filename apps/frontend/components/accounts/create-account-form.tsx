"use client";

import { useState } from "react";

import {
  useMutation,
  useQueryClient,
} from "@tanstack/react-query";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

import { accountService } from "@/services/account.service";
import type {
  AccountType,
} from "@/types/accounts"

export function CreateAccountForm(): React.JSX.Element {
  const queryClient = useQueryClient();

  const [name, setName] =
    useState("");

  const [
    institutionName,
    setInstitutionName,
  ] = useState("");

  const [accountType, setAccountType] =
    useState<AccountType>("checking");

  const [balance, setBalance] =
    useState("");

  const mutation = useMutation({
    mutationFn:
      accountService.createAccount,

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["accounts"],
      });

      setName("");
      setInstitutionName("");
      setBalance("");
      setAccountType("checking");
    },
  });

  function handleSubmit(
    e: React.FormEvent
  ): void {
    e.preventDefault();

    mutation.mutate({
      name,
      institution_name:
        institutionName,
      account_type:accountType,
      currency: "USD",
      balance:
        Number(balance),
    });
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="space-y-4 rounded-2xl border border-border p-6"
    >
      <h2 className="text-xl font-semibold">
        New Account
      </h2>

      <div>
        <Label>Name</Label>

        <Input
          value={name}
          onChange={(e) =>
            setName(e.target.value)
          }
        />
      </div>

      <div>
        <Label>Institution</Label>

        <Input
          value={institutionName}
          onChange={(e) =>
            setInstitutionName(
              e.target.value
            )
          }
        />
      </div>

      <div>
        <Label>Type</Label>

        <select
            value={accountType}
            onChange={(e) =>
                setAccountType(
                e.target.value as AccountType
                )
            }
            className="w-full rounded-md border border-border px-3 py-2"
            >
            <option value="checking">
                Checking
            </option>

            <option value="savings">
                Savings
            </option>

            <option value="credit">
                Credit
            </option>

            <option value="cash">
                Cash
            </option>

            <option value="investment">
                Investment
            </option>

            <option value="crypto">
                Crypto
            </option>
        </select>
      </div>

      <div>
        <Label>Balance</Label>

        <Input
          type="number"
          value={balance}
          onChange={(e) =>
            setBalance(
              e.target.value
            )
          }
        />
      </div>

      <Button
        type="submit"
        disabled={mutation.isPending}
      >
        Create Account
      </Button>
    </form>
  );
}