export default function NotFound(): React.JSX.Element {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center gap-6 px-6 text-center">
      <h1 className="text-4xl font-semibold tracking-tight">
        404
      </h1>

      <p className="text-muted-foreground">
        Page not found.
      </p>
    </div>
  );
}