"use client";

import * as React from "react";
import { Moon, Sun, PanelLeft, Wallet } from "lucide-react";
import { useTheme } from "next-themes";
import { Button } from "@/components/ui/button";
import { useUiStore } from "@/store/ui-store";

export function Navbar(): React.JSX.Element {
  const { theme, setTheme } = useTheme();
  const toggleSidebar = useUiStore((state) => state.toggleSidebar);

  return (
    <header className="sticky top-0 z-50 border-b border-border bg-background/80 backdrop-blur-xl">
      <div className="flex h-16 items-center justify-between px-6 lg:px-8">
        <div className="flex items-center gap-4">
          <Button
            variant="ghost"
            size="icon"
            onClick={toggleSidebar}
            aria-label="Toggle sidebar"
          >
            <PanelLeft className="h-5 w-5" />
          </Button>

          <div className="flex items-center gap-3">
            <div className="rounded-xl border border-border p-2">
              <Wallet className="h-5 w-5" />
            </div>

            <div>
              <p className="text-sm font-semibold tracking-tight">
                FinSight AI
              </p>
              <p className="text-xs text-muted-foreground">
                Financial Intelligence
              </p>
            </div>
          </div>
        </div>

        <Button
          variant="ghost"
          size="icon"
          onClick={() =>
            setTheme(theme === "dark" ? "light" : "dark")
          }
          aria-label="Toggle theme"
        >
          <Sun className="h-5 w-5 rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
          <Moon className="absolute h-5 w-5 rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100" />
        </Button>
      </div>
    </header>
  );
}