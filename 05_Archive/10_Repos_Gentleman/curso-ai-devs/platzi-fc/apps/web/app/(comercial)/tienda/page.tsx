import type { Metadata } from "next";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { ShoppingBag } from "lucide-react";

export const metadata: Metadata = {
  title: "Tienda Oficial",
  description: "Tienda oficial del Platzi FC. Camisetas, merchandising y más.",
};

const mockProducts = [
  { id: "1", name: "Camiseta Local 25/26", price: 89.99, category: "Equipaciones", isNew: true },
  { id: "2", name: "Camiseta Visitante 25/26", price: 89.99, category: "Equipaciones", isNew: true },
  { id: "3", name: "Camiseta Tercera 25/26", price: 89.99, category: "Equipaciones", isNew: false },
  { id: "4", name: "Bufanda Oficial", price: 19.99, category: "Accesorios", isNew: false },
  { id: "5", name: "Gorra Platzi FC", price: 24.99, category: "Accesorios", isNew: false },
  { id: "6", name: "Balón Réplica", price: 29.99, category: "Accesorios", isNew: true },
  { id: "7", name: "Chaqueta Entrenamiento", price: 69.99, category: "Training", isNew: false },
  { id: "8", name: "Sudadera Casual", price: 54.99, category: "Lifestyle", isNew: false },
];

export default function TiendaPage() {
  return (
    <div className="py-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold">Tienda Oficial</h1>
        <p className="mt-1 text-foreground-secondary">Productos oficiales del Platzi FC</p>
      </div>

      <div className="grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-4">
        {mockProducts.map((product) => (
          <Card key={product.id} className="group overflow-hidden hover:shadow-md transition-shadow">
            <div className="relative aspect-square bg-surface-alt flex items-center justify-center">
              <ShoppingBag className="h-10 w-10 text-muted/30" />
              {product.isNew && (
                <Badge variant="success" className="absolute top-2 left-2">Nuevo</Badge>
              )}
            </div>
            <CardContent className="p-4">
              <p className="text-xs text-muted mb-1">{product.category}</p>
              <p className="font-semibold text-sm group-hover:text-primary transition-colors line-clamp-2">{product.name}</p>
              <p className="mt-2 text-lg font-bold">{product.price}€</p>
              <Button variant="primary" size="sm" className="w-full mt-3">Añadir al carrito</Button>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
