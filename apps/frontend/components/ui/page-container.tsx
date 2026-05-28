import * as React from "react";
import { cn } from "@/lib/utils";

interface PageContainerProps {
  children: React.ReactNode;
  className?: string;
}

export function PageContainer({
  children,
  className,
}: PageContainerProps): React.JSX.Element {
  return (
    <main
      className={cn(
        "mx-auto w-full max-w-7xl px-6 py-8 lg:px-8",
        className
      )}
    >
      {children}
    </main>
  );
}