"use client";

import type {
  Account,
} from "@/types/accounts";

interface AccountTableProps {
  accounts: Account[];
}

export function AccountTable({
  accounts,
}: AccountTableProps): React.JSX.Element {
  return (
    <div className="overflow-hidden rounded-2xl border border-border bg-card">
      <table className="w-full">
        <thead>
          <tr className="border-b border-border">
            <th className="px-6 py-4 text-left">
              Account
            </th>

            <th className="px-6 py-4 text-left">
              Institution
            </th>

            <th className="px-6 py-4 text-left">
              Type
            </th>

            <th className="px-6 py-4 text-right">
              Balance
            </th>
          </tr>
        </thead>

        <tbody>
          {accounts.map((account) => (
            <tr
              key={account.id}
              className="border-b border-border"
            >
            <td className="px-6 py-4 font-medium">
                <div>
                    <p>{account.name}</p>

                    <p className="text-xs text-muted-foreground">
                        {account.id}
                    </p>
                </div>
            </td>

              <td className="px-6 py-4 text-muted-foreground">
                {account.institution_name ??
                  "-"}
              </td>

              <td className="px-6 py-4">
                {account.account_type}
              </td>

              <td className="px-6 py-4 text-right font-semibold">
                {account.balance}{" "}
                {account.currency}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}