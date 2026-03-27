#!/usr/bin/env python3
"""
Ejemplo Avanzado: Procesamiento de Facturas con Claude API
Usa Claude para extracción más inteligente y precisa de datos
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Optional
import base64

# Nota: Requiere pip install anthropic
try:
    import anthropic
    CLAUDE_AVAILABLE = True
except ImportError:
    CLAUDE_AVAILABLE = False
    print("⚠️ Para usar Claude API: pip install anthropic --break-system-packages")


class ClaudeInvoiceExtractor:
    """
    Extractor de facturas mejorado con Claude API
    Usa visión de Claude para analizar PDFs directamente
    """

    def __init__(self, api_key: Optional[str] = None):
        if not CLAUDE_AVAILABLE:
            raise ImportError("El módulo 'anthropic' no está instalado")

        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key requerida. Configura ANTHROPIC_API_KEY o pásala como argumento"
            )

        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.model = "claude-sonnet-4-20250514"

    def extract_from_pdf(self, pdf_path: str) -> Dict:
        """
        Extrae datos de factura usando Claude Vision

        Args:
            pdf_path: Ruta al archivo PDF

        Returns:
            Dict con datos estructurados de la factura
        """

        # Convertir PDF a imagen para visión de Claude
        from pdf2image import convert_from_path

        print(f"📄 Procesando con Claude: {Path(pdf_path).name}")

        # Convertir primera página a imagen
        images = convert_from_path(pdf_path, dpi=200, first_page=1, last_page=1)

        if not images:
            raise ValueError("No se pudo convertir el PDF a imagen")

        # Convertir imagen a base64
        import io
        img_byte_arr = io.BytesIO()
        images[0].save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        image_base64 = base64.b64encode(img_byte_arr).decode('utf-8')

        # Prompt para Claude
        prompt = """Analiza esta factura/invoice y extrae la siguiente información en formato JSON:

{
  "invoice_number": "número de factura",
  "invoice_date": "fecha en formato DD/MM/YYYY",
  "due_date": "fecha de vencimiento DD/MM/YYYY",
  "vendor_name": "nombre del proveedor/vendedor",
  "vendor_address": "dirección del proveedor",
  "vendor_tax_id": "RFC/TAX ID del proveedor",
  "customer_name": "nombre del cliente",
  "customer_address": "dirección del cliente",
  "subtotal": monto subtotal numérico,
  "tax_amount": monto de impuestos numérico,
  "total_amount": monto total numérico,
  "currency": "USD/EUR/MXN/etc",
  "payment_terms": "términos de pago",
  "items": [
    {
      "description": "descripción del item",
      "quantity": cantidad numérica,
      "unit_price": precio unitario numérico,
      "amount": monto total del item
    }
  ]
}

Responde SOLO con el JSON, sin texto adicional. Si algún campo no está presente, usa null."""

        # Llamar a Claude con visión
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": "image/png",
                                    "data": image_base64
                                }
                            },
                            {
                                "type": "text",
                                "text": prompt
                            }
                        ]
                    }
                ]
            )

            # Extraer respuesta
            response_text = message.content[0].text

            # Parsear JSON
            # Limpiar markdown si existe
            if "```json" in response_text:
                response_text = response_text.split("```json")[1].split("```")[0]
            elif "```" in response_text:
                response_text = response_text.split("```")[1].split("```")[0]

            invoice_data = json.loads(response_text.strip())

            print(f"✅ Extraído con Claude: {invoice_data.get('invoice_number', 'N/A')}")

            return invoice_data

        except Exception as e:
            print(f"❌ Error con Claude API: {e}")
            raise

    def batch_extract(self, pdf_files: List[str], output_file: str = "claude_results.json"):
        """
        Extrae datos de múltiples facturas

        Args:
            pdf_files: Lista de rutas a PDFs
            output_file: Archivo de salida JSON
        """

        print(f"\n🚀 Procesando {len(pdf_files)} facturas con Claude API\n")

        results = []

        for i, pdf_path in enumerate(pdf_files, 1):
            try:
                print(f"[{i}/{len(pdf_files)}] ", end="")
                data = self.extract_from_pdf(pdf_path)
                data['filename'] = Path(pdf_path).name
                data['status'] = 'success'
                results.append(data)

            except Exception as e:
                print(f"❌ Error: {e}")
                results.append({
                    'filename': Path(pdf_path).name,
                    'status': 'error',
                    'error': str(e)
                })

        # Guardar resultados
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

        print(f"\n✅ Resultados guardados en: {output_file}")

        # Estadísticas
        success = sum(1 for r in results if r.get('status') == 'success')
        print(f"\n📊 Exitosas: {success}/{len(results)}")

        return results


def example_usage():
    """Ejemplo de uso del extractor con Claude"""

    if not CLAUDE_AVAILABLE:
        print("❌ Instala 'anthropic' primero: pip install anthropic")
        return

    # Verificar API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ Configura tu API key:")
        print("   export ANTHROPIC_API_KEY='tu-api-key'")
        print("\nObtén tu API key en: https://console.anthropic.com/")
        return

    # Crear extractor
    extractor = ClaudeInvoiceExtractor(api_key=api_key)

    # Buscar PDFs de ejemplo
    invoice_dir = Path("./sample_invoices")
    if not invoice_dir.exists():
        print(f"❌ Directorio no encontrado: {invoice_dir}")
        print("Genera facturas primero con: python test_invoice_system.py generate")
        return

    pdf_files = list(invoice_dir.glob("*.pdf"))

    if not pdf_files:
        print("❌ No se encontraron PDFs")
        return

    # Limitar a 3 para ejemplo (evitar costos)
    pdf_files = pdf_files[:3]

    print(f"🔍 Procesando {len(pdf_files)} facturas con Claude Vision...")

    # Extraer datos
    results = extractor.batch_extract(pdf_files, "claude_results.json")

    # Mostrar resultados
    print("\n" + "="*60)
    print("📋 RESULTADOS")
    print("="*60)

    for result in results:
        if result.get('status') == 'success':
            print(f"\n✅ {result['filename']}")
            print(f"   Factura: {result.get('invoice_number', 'N/A')}")
            print(f"   Fecha: {result.get('invoice_date', 'N/A')}")
            print(f"   Total: {result.get('currency', '')} ${result.get('total_amount', 0):,.2f}")
            print(f"   Items: {len(result.get('items', []))}")
        else:
            print(f"\n❌ {result['filename']}")
            print(f"   Error: {result.get('error', 'Unknown')}")


def compare_extractors():
    """
    Compara extracción tradicional vs Claude API
    Útil para evaluar precisión y costo
    """

    print("⚖️ COMPARACIÓN: Extracción Tradicional vs Claude API")
    print("="*60)

    # Generar factura de prueba
    from test_invoice_system import generate_sample_invoices
    invoice_dir = generate_sample_invoices(num_invoices=1)
    pdf_file = list(invoice_dir.glob("*.pdf"))[0]

    print(f"\n📄 Factura de prueba: {pdf_file.name}\n")

    # Método 1: Extracción tradicional
    print("1️⃣ Extracción Tradicional (OCR + Regex)")
    print("-" * 60)

    from invoice_processor import InvoiceExtractor
    import time

    start = time.time()
    extractor_traditional = InvoiceExtractor(
        invoice_id=1,
        pdf_path=str(pdf_file),
        output_dir="./comparison",
        use_ocr=False
    )
    result_traditional = extractor_traditional.extract()
    time_traditional = time.time() - start

    print(f"⏱️ Tiempo: {time_traditional:.2f}s")
    print(f"📊 Resultado:")
    print(f"   Factura: {result_traditional.invoice_number}")
    print(f"   Fecha: {result_traditional.invoice_date}")
    print(f"   Total: {result_traditional.total_amount}")
    print(f"   Status: {result_traditional.status}")

    # Método 2: Claude API
    if CLAUDE_AVAILABLE and os.environ.get("ANTHROPIC_API_KEY"):
        print(f"\n2️⃣ Extracción con Claude API")
        print("-" * 60)

        start = time.time()
        extractor_claude = ClaudeInvoiceExtractor()
        result_claude = extractor_claude.extract_from_pdf(str(pdf_file))
        time_claude = time.time() - start

        print(f"⏱️ Tiempo: {time_claude:.2f}s")
        print(f"📊 Resultado:")
        print(f"   Factura: {result_claude.get('invoice_number')}")
        print(f"   Fecha: {result_claude.get('invoice_date')}")
        print(f"   Total: {result_claude.get('total_amount')}")
        print(f"   Items: {len(result_claude.get('items', []))}")

        # Comparación
        print(f"\n📈 COMPARACIÓN")
        print("-" * 60)
        print(f"Velocidad: Tradicional {time_traditional:.2f}s vs Claude {time_claude:.2f}s")
        print(f"Precisión: Evalúa manualmente comparando los resultados")
        print(f"Costo: Tradicional $0 vs Claude ~$0.015 por factura")

    else:
        print("\n⚠️ Configura ANTHROPIC_API_KEY para probar Claude API")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] == "example":
            example_usage()
        elif sys.argv[1] == "compare":
            compare_extractors()
        else:
            print("Comandos disponibles:")
            print("  python advanced_examples.py example   - Ejemplo con Claude API")
            print("  python advanced_examples.py compare   - Comparar métodos")
    else:
        print("🎓 Ejemplos Avanzados de Procesamiento de Facturas")
        print("="*60)
        print("\nUso:")
        print("  python advanced_examples.py example   - Procesar con Claude API")
        print("  python advanced_examples.py compare   - Comparar métodos")
        print("\nRequisitos:")
        print("  1. pip install anthropic --break-system-packages")
        print("  2. export ANTHROPIC_API_KEY='tu-api-key'")
        print("\nObtén tu API key en: https://console.anthropic.com/")
