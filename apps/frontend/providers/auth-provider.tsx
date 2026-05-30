"use client";

import { useEffect } from "react";

import { authService } from "@/services/auth.service";
import { useAuthStore } from "@/store/auth-store";

export function AuthProvider({
  children,
}: {
  children: React.ReactNode;
}): React.JSX.Element {
  const accessToken = useAuthStore(
    (state) => state.accessToken
  );

  const setUser = useAuthStore(
    (state) => state.setUser
  );

  const logout = useAuthStore(
    (state) => state.logout
  );

  useEffect(() => {
    async function bootstrap(): Promise<void> {
      if (!accessToken) {
        return;
      }

      try {
        const user = await authService.me();

        setUser(user);
      } catch (error){
        console.error(
          "AUTH BOOTSTRAP FAILED:",
          error
        );
      }
    }

    void bootstrap();
  }, [
    accessToken,
    setUser,
    logout,
  ]);

  return <>{children}</>;
}