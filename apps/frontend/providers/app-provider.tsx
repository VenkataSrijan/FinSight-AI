"use client";

import * as React from "react";
import { ThemeProvider } from "./theme-provider";
import { QueryProvider } from "./query-provider";
import { Toaster } from "sonner";
import { AuthProvider } from "./auth-provider";
import { AuthGuard } from "@/components/auth/auth-guard";

export function AppProvider({
  children,
}: {
  children: React.ReactNode;
}): React.JSX.Element {
  return (
    <ThemeProvider
      attribute="class"
      defaultTheme="system"
      enableSystem
      disableTransitionOnChange
    >
      <QueryProvider>
        <AuthProvider>
          <AuthGuard>
            {children}
          </AuthGuard>
        </AuthProvider>

        <Toaster
          richColors
          position="top-right"
        />
      </QueryProvider>
    </ThemeProvider>
  );
}