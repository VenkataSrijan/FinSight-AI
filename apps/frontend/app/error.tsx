"use client";

interface ErrorProps {
  error: Error;
  reset: () => void;
}

export default function Error({
  error,
  reset,
}: ErrorProps): React.JSX.Element {
  console.error(error);

  return (
    <div className="flex min-h-screen flex-col items-center justify-center gap-6 px-6 text-center">
      <h1 className="text-3xl font-semibold tracking-tight">
        Something went wrong
      </h1>

      <p className="max-w-xl text-muted-foreground">
        An unexpected frontend error occurred.
      </p>

      <button
        onClick={reset}
        className="rounded-xl border border-border px-5 py-3"
      >
        Retry
      </button>
    </div>
  );
}