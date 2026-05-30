"use client";

import { useRouter } from "next/navigation";
import { useMutation } from "@tanstack/react-query";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { toast } from "sonner";

import { authService } from "@/services/auth.service";
import { useAuthStore } from "@/store/auth-store";

import {
  loginSchema,
  type LoginFormValues,
} from "@/lib/validations/auth";

import { Card, CardContent, CardHeader } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";


export default function LoginPage(): React.JSX.Element {
  const router = useRouter();

  const setTokens = useAuthStore(
    (state) => state.setTokens
  );

  const form = useForm<LoginFormValues>({
    resolver: zodResolver(loginSchema),
    defaultValues: {
      email: "",
      password: "",
    },
  });

  const loginMutation = useMutation({
    mutationFn: authService.login,

    onSuccess: async (tokens) => {
        console.log("TOKENS RECEIVED:", tokens);

        setTokens(
            tokens.access_token,
            tokens.refresh_token
        );

        console.log(
            "STORE AFTER SET:",
            useAuthStore.getState()
        );

        toast.success("Logged in successfully");

        router.push("/");
    },

    onError: (error: Error) => {
      toast.error(error.message);
    },
  });

  function onSubmit(
    values: LoginFormValues
  ): void {
    loginMutation.mutate(values);
  }

  return (
    <div className="flex min-h-screen items-center justify-center p-6">
      <Card className="w-full max-w-md">
        <CardHeader>
          <h1 className="text-2xl font-semibold">
            Sign in
          </h1>
        </CardHeader>

        <CardContent>
          <form
            onSubmit={form.handleSubmit(onSubmit)}
            className="space-y-4"
          >
            <div className="space-y-2">
              <Label htmlFor="email">
                Email
              </Label>

              <Input
                id="email"
                type="email"
                {...form.register("email")}
              />

              {form.formState.errors.email && (
                <p className="text-sm text-destructive">
                  {
                    form.formState.errors.email
                      .message
                  }
                </p>
              )}
            </div>

            <div className="space-y-2">
              <Label htmlFor="password">
                Password
              </Label>

              <Input
                id="password"
                type="password"
                {...form.register("password")}
              />

              {form.formState.errors.password && (
                <p className="text-sm text-destructive">
                  {
                    form.formState.errors.password
                      .message
                  }
                </p>
              )}
            </div>

            <Button
              type="submit"
              className="w-full"
              disabled={loginMutation.isPending}
            >
              {loginMutation.isPending
                ? "Signing in..."
                : "Sign in"}
            </Button>
          </form>
        </CardContent>
      </Card>
    </div>
  );
}