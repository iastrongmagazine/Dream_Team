import type { Metadata } from "next";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

export const metadata: Metadata = {
  title: "Cuerpo Técnico",
  description: "Cuerpo técnico del Platzi FC.",
};

const mockStaff = [
  { id: "1", name: "Roberto Sánchez", role: "Director Técnico", nationality: "Argentina" },
  { id: "2", name: "Miguel Ángel Díaz", role: "Asistente Técnico", nationality: "Colombia" },
  { id: "3", name: "Francisco Ruiz", role: "Preparador Físico", nationality: "España" },
  { id: "4", name: "Eduardo Paz", role: "Entrenador de Porteros", nationality: "Uruguay" },
  { id: "5", name: "Carolina Méndez", role: "Fisioterapeuta", nationality: "México" },
  { id: "6", name: "Alejandro Vega", role: "Analista Táctico", nationality: "Chile" },
];

export default function StaffPage() {
  return (
    <div className="py-8">
      <h1 className="text-3xl font-bold mb-2">Cuerpo Técnico</h1>
      <p className="text-foreground-secondary mb-8">Los profesionales detrás del equipo</p>

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {mockStaff.map((member) => (
          <Card key={member.id} className="hover:shadow-md transition-shadow">
            <CardContent className="flex items-center gap-4 p-5">
              <div className="h-16 w-16 rounded-full bg-primary/10 flex items-center justify-center text-xl font-bold text-primary shrink-0">
                {member.name.split(" ").map((n) => n[0]).join("").slice(0, 2)}
              </div>
              <div>
                <p className="font-semibold">{member.name}</p>
                <Badge variant="outline" className="mt-1">{member.role}</Badge>
                <p className="text-xs text-muted mt-1">{member.nationality}</p>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
