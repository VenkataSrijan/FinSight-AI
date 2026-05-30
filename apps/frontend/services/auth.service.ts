import { apiClient } from "@/lib/api/client";

import type {
  LoginRequest,
  SignupRequest,
  TokenResponse,
  User,
} from "@/types/auth";

export const authService = {
  login(
    payload: LoginRequest
  ): Promise<TokenResponse> {
    return apiClient.post<TokenResponse>(
      "/auth/login",
      payload
    );
  },

  signup(
    payload: SignupRequest
  ): Promise<User> {
    return apiClient.post<User>(
      "/auth/signup",
      payload
    );
  },

  refresh(
    refresh_token: string
  ): Promise<TokenResponse> {
    return apiClient.post<TokenResponse>(
      "/auth/refresh",
      {
        refresh_token,
      }
    );
  },

  me(): Promise<User> {
    console.log("CALLING /auth/me");

    return apiClient.get<User>(
      "/auth/me",
      {
        requireAuth: true,
      }
    );
  }
};