import { apiClient } from "@/lib/api/client";
import type { HealthCheckResponse } from "@/lib/api/types";

export const healthService = {
  getHealth(): Promise<HealthCheckResponse> {
    return apiClient.get<HealthCheckResponse>("/health/live");
  },
};