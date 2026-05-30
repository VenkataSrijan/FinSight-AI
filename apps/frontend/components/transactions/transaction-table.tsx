"use client";

import type {
  Transaction,
} from "@/types/transactions";

interface TransactionTableProps {
  transactions: Transaction[];
}

export function TransactionTable({
  transactions,
}: TransactionTableProps): React.JSX.Element {
  return (
    <div className="overflow-hidden rounded-2xl border border-border bg-card">
      <table className="w-full">
        <thead>
          <tr className="border-b border-border">
            <th className="px-6 py-4 text-left">
              Merchant
            </th>

            <th className="px-6 py-4 text-left">
              Description
            </th>

            <th className="px-6 py-4 text-left">
              Type
            </th>

            <th className="px-6 py-4 text-right">
              Amount
            </th>
          </tr>
        </thead>

        <tbody>
          {transactions.map((tx) => (
            <tr
              key={tx.id}
              className="border-b border-border"
            >
              <td className="px-6 py-4 font-medium">
                {tx.merchant ??
                  "Unknown Merchant"}
              </td>

              <td className="px-6 py-4 text-muted-foreground">
                {tx.description ?? "-"}
              </td>

              <td className="px-6 py-4">
                <span
                    className={
                        tx.type === "credit"
                        ? "text-green-500 font-medium"
                        : "text-red-500 font-medium"
                    }
                >
                    {tx.type.toUpperCase()}
                </span>
              </td>

              <td className="px-6 py-4 text-right font-semibold">
                {tx.amount} {tx.currency}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}