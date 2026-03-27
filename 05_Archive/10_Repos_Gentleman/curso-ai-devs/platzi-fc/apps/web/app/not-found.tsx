import Link from "next/link";
import { Button } from "@/components/ui/button";

export default function NotFound() {
  return (
    <div className="flex min-h-[60vh] flex-col items-center justify-center px-4 text-center">
      <h1 className="text-8xl font-bold text-primary">404</h1>
      <p className="mt-4 text-xl text-foreground-secondary">
        La página que buscas no existe o fue movida.
      </p>
      <Link href="/" className="mt-8">
        <Button variant="primary" size="lg">
          Volver al inicio
        </Button>
      </Link>
    </div>
  );
}
