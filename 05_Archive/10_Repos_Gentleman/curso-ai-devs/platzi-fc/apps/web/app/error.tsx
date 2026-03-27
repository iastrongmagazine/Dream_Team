"use client";

import { Button } from "@/components/ui/button";

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  return (
    <div className="flex min-h-[60vh] flex-col items-center justify-center px-4 text-center">
      <h1 className="text-4xl font-bold text-error">Algo salió mal</h1>
      <p className="mt-4 text-foreground-secondary">
        Ocurrió un error inesperado. Por favor intenta de nuevo.
      </p>
      <Button variant="primary" size="lg" className="mt-8" onClick={reset}>
        Reintentar
      </Button>
    </div>
  );
}
