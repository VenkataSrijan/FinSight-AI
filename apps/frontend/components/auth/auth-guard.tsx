"use client";

import { useEffect } from "react";
import { usePathname, useRouter } from "next/navigation";

import { useAuthStore } from "@/store/auth-store";

const PUBLIC_ROUTES = [
  "/login",
  "/signup",
];

export function AuthGuard({
  children,
}: {
  children: React.ReactNode;
}): React.JSX.Element {
  const router = useRouter();

  const pathname = usePathname();

  const accessToken = useAuthStore(
    (state) => state.accessToken
  );

  useEffect(() => {
    const isPublic =
      PUBLIC_ROUTES.includes(pathname);

    if (!accessToken && !isPublic) {
      router.replace("/login");
    }
  }, [
    accessToken,
    pathname,
    router,
  ]);

  const isPublic =
    PUBLIC_ROUTES.includes(pathname);

  if (!accessToken && !isPublic) {
    return (
      <div className="flex min-h-screen items-center justify-center">
        Loading...
      </div>
    );
  }

  return <>{children}</>;
}