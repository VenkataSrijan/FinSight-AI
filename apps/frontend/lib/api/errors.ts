export class ApiError extends Error {
  readonly status: number;
  readonly code?: string;
  readonly details?: unknown;

  constructor(
    message: string,
    status: number,
    code?: string,
    details?: unknown
  ) {
    super(message);
    this.name = "ApiError";
    this.status = status;
    this.code = code;
    this.details = details;
  }
}

export async function normalizeApiError(response: Response): Promise<ApiError> {
  let payload: unknown;

  try {
    payload = await response.json();
  } catch {
    payload = null;
  }

  const parsed =
    typeof payload === "object" && payload !== null
      ? (payload as {
          error?: {
            code?: string;
            message?: string;
            details?: unknown;
          };
        })
      : undefined;

  return new ApiError(
    parsed?.error?.message ?? "Unexpected API error",
    response.status,
    parsed?.error?.code,
    parsed?.error?.details
  );
}