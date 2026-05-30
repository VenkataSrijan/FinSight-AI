import { APP_CONFIG } from "@/lib/constants";
import { normalizeApiError } from "./errors";
import type { RequestConfig } from "./types";
import { useAuthStore } from "@/store/auth-store";
import { authService } from "@/services/auth.service";

async function getAccessToken(): Promise<string | null> {
  return useAuthStore.getState().accessToken;
}

class ApiClient {
  private readonly baseUrl = APP_CONFIG.apiBaseUrl;

  async request<T>(
    endpoint: string,
    config: RequestConfig = {}
  ): Promise<T> {
    const headers = new Headers(config.headers);

    headers.set("Content-Type", "application/json");

    if (config.requireAuth) {
      const token = await getAccessToken();

      if (token) {
        headers.set("Authorization", `Bearer ${token}`);
      }
    }

    const response = await fetch(`${this.baseUrl}${endpoint}`, {
      ...config,
      headers,
      cache: "no-store",
    });

    if (response.status === 401 && config.requireAuth) {
      try {
        const {
          refreshToken,
          setTokens,
          logout,
        } = useAuthStore.getState();

        if (!refreshToken) {
          logout();
          throw await normalizeApiError(response);
        }

        const tokens =
          await authService.refresh(
            refreshToken
          );

        setTokens(
          tokens.access_token,
          tokens.refresh_token
        );

        headers.set(
          "Authorization",
          `Bearer ${tokens.access_token}`
        );

        const retryResponse = await fetch(
          `${this.baseUrl}${endpoint}`,
          {
            ...config,
            headers,
            cache: "no-store",
          }
        );

        if (!retryResponse.ok) {
          logout();
          throw await normalizeApiError(
            retryResponse
          );
        }

        return retryResponse.json() as Promise<T>;
      } catch {
        useAuthStore.getState().logout();

        throw await normalizeApiError(
          response
        );
      }
    }

    if (!response.ok) {
      throw await normalizeApiError(response);
    }

    return response.json() as Promise<T>;
  }

  get<T>(endpoint: string, config?: RequestConfig): Promise<T> {
    return this.request<T>(endpoint, {
      ...config,
      method: "GET",
    });
  }

  post<T>(
    endpoint: string,
    body?: unknown,
    config?: RequestConfig
  ): Promise<T> {
    return this.request<T>(endpoint, {
      ...config,
      method: "POST",
      body: body ? JSON.stringify(body) : undefined,
    });
  }

  patch<T>(
    endpoint: string,
    body?: unknown,
    config?: RequestConfig
  ): Promise<T> {
    return this.request<T>(endpoint, {
      ...config,
      method: "PATCH",
      body: body ? JSON.stringify(body) : undefined,
    });
  }

  delete<T>(endpoint: string, config?: RequestConfig): Promise<T> {
    return this.request<T>(endpoint, {
      ...config,
      method: "DELETE",
    });
  }
}

export const apiClient = new ApiClient();