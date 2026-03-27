import { Breadcrumbs } from "@/components/shared/breadcrumbs";

export default function DeportivoLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="mx-auto max-w-7xl px-4">
      <Breadcrumbs />
      {children}
    </div>
  );
}
