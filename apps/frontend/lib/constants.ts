export const APP_CONFIG = {
  name: "FinSight AI",
  description: "Enterprise financial intelligence platform",
  apiBaseUrl:
    process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000/api/v1",
  wsBaseUrl:
    process.env.NEXT_PUBLIC_WS_BASE_URL ?? "ws://localhost:8000",
} as const;

export const QUERY_KEYS = {
  health: ["health"] as const,
  profile: ["profile"] as const,
  transactions: ["transactions"] as const,
  analytics: ["analytics"] as const,
  anomalies: ["anomalies"] as const,
} as const;