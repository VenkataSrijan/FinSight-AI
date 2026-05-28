export type HttpMethod = "GET" | "POST" | "PUT" | "PATCH" | "DELETE";

export interface RequestConfig extends RequestInit {
  requireAuth?: boolean;
}

export interface HealthCheckResponse {
  status: string;
  service: string;
}