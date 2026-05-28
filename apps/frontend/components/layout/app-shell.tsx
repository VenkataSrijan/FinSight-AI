"use client";

import * as React from "react";
import { Navbar } from "./navbar";
import { useUiStore } from "@/store/ui-store";
import { cn } from "@/lib/utils";

interface AppShellProps {
  children: React.ReactNode;
}

export function AppShell({
  children,
}: AppShellProps): React.JSX.Element {
  const sidebarOpen = useUiStore((state) => state.sidebarOpen);

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
          </div>
        </aside>

        <div className="flex-1">{children}</div>
      </div>
    </div>
  );
}