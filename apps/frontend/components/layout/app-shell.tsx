"use client";

import * as React from "react";
import { Navbar } from "./navbar";
import { useUiStore } from "@/store/ui-store";
import { cn } from "@/lib/utils";
import Link from "next/link";
import { usePathname } from "next/navigation";

import { navigation } from "@/lib/navigation";

interface AppShellProps {
  children: React.ReactNode;
}

export function AppShell({
  children,
}: AppShellProps): React.JSX.Element {
  const sidebarOpen = useUiStore((state) => state.sidebarOpen);
  const pathname = usePathname();

  return (
    <div className="min-h-screen bg-background text-foreground">
      <Navbar />

      <div className="flex">
        <aside
          className={cn(
            "hidden border-r border-border bg-card transition-all duration-300 lg:block",
            sidebarOpen ? "w-72" : "w-20"
          )}
        >
          <div className="p-6">
            <p className="text-xs uppercase tracking-[0.2em] text-muted-foreground">
              Navigation
            </p>

            <nav className="mt-6 space-y-2">
              {navigation.map((item) => (
                <Link
                  key={item.href}
                  href={item.href}
                  className={cn(
                    "block rounded-lg px-3 py-2 text-sm transition-colors",
                    pathname === item.href
                      ? "bg-primary text-primary-foreground"
                      : "text-muted-foreground hover:bg-accent hover:text-accent-foreground"
                  )}
                >
                  {item.title}
                </Link>
              ))}
            </nav>
          </div>
        </aside>

        <div className="flex-1">{children}</div>
      </div>
    </div>
  );
}