"""
# 🚀 PersonalOS: Invoice Intelligence (OCR)
# Motor de Procesamiento Paralelo de Alto Rendimiento
# Armor Layer v1.0 | Pure Green Certified
"""

import os
import sys
import logging
import multiprocessing as mp
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime
from dataclasses import dataclass, asdict
import json
import traceback
import subprocess

# --- Armor Layer: Ruta Absoluta Segura ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def notify_voice(message: str):
    """Notificación de voz (Speak/TTS) para hitos del sistema"""
    try:
        # Intenta usar el sistema de voz de PersonalOS si está disponible
        # De lo contrario, imprime en consola con formato branding
        print(f"\n[PersonalOS Voice] 🔊 {message}")
        # Comando de voz (Windows)
        subprocess.run(["powershell", "-Command", f"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{message}')"], capture_output=True)
    except Exception:
        pass

# PDF & OCR libraries
import pytesseract
from pdf2image import convert_from_path
import pdfplumber
from pypdf import PdfReader

# Data processing
import pandas as pd
import re


@dataclass
class InvoiceData:
    """Estructura de datos de factura extraída"""
    filename: str
    invoice_number: Optional[str] = None
    invoice_date: Optional[str] = None
    vendor_name: Optional[str] = None
    vendor_address: Optional[str] = None
    total_amount: Optional[float] = None
    currency: Optional[str] = None
    tax_amount: Optional[float] = None
    subtotal: Optional[float] = None
    items: Optional[List[Dict]] = None
    payment_terms: Optional[str] = None
    due_date: Optional[str] = None
    customer_name: Optional[str] = None
    customer_address: Optional[str] = None
    status: str = "pending"
    error: Optional[str] = None
    processing_time: Optional[float] = None
    ocr_confidence: Optional[float] = None


class InvoiceExtractor:
    """Subagente Worker - Procesa una factura individual"""

    def __init__(self, invoice_id: int, pdf_path: str, output_dir: str, use_ocr: bool = True):
        self.invoice_id = invoice_id
        self.pdf_path = Path(pdf_path)
        self.output_dir = Path(output_dir)
        self.use_ocr = use_ocr
        self.logger = self._setup_logger()

    def _setup_logger(self) -> logging.Logger:
        """Configura logger específico para este worker"""
        logger = logging.getLogger(f"Worker-{self.invoice_id}")
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                f'[Worker-{self.invoice_id}] %(asctime)s - %(levelname)s - %(message)s',
                datefmt='%H:%M:%S'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        return logger

    def extract(self) -> InvoiceData:
        """Extrae datos de la factura"""
        start_time = datetime.now()
        invoice_data = InvoiceData(filename=self.pdf_path.name)

        try:
            self.logger.info(f"📄 Iniciando extracción: {self.pdf_path.name}")

            # Intentar extracción directa de texto primero
            text = self._extract_text_direct()

            # Si el texto es insuficiente o muy corto, usar OCR
            if not text or len(text.strip()) < 50:
                if self.use_ocr:
                    self.logger.info("📸 Texto insuficiente, activando OCR...")
                    text, ocr_conf = self._extract_text_ocr()
                    invoice_data.ocr_confidence = ocr_conf
                else:
                    self.logger.warning("⚠️ Texto insuficiente y OCR desactivado")

            # Extraer tablas
            tables = self._extract_tables()

            # Parsear datos de la factura
            self._parse_invoice_data(invoice_data, text, tables)

            # Marcar como exitoso
            invoice_data.status = "success"

            # Tiempo de procesamiento
            processing_time = (datetime.now() - start_time).total_seconds()
            invoice_data.processing_time = processing_time

            self.logger.info(f"✅ Completado en {processing_time:.2f}s - Factura #{invoice_data.invoice_number or 'N/A'}")

        except Exception as e:
            invoice_data.status = "error"
            invoice_data.error = str(e)
            self.logger.error(f"❌ Error: {str(e)}")
            self.logger.debug(traceback.format_exc())

        return invoice_data

    def _extract_text_direct(self) -> str:
        """Extrae texto directamente del PDF (sin OCR)"""
        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                text = ""
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                return text
        except Exception as e:
            self.logger.warning(f"⚠️ Extracción directa falló: {e}")
            return ""

    def _extract_text_ocr(self) -> tuple[str, float]:
        """Extrae texto usando OCR"""
        try:
            # Configuración de Tesseract para español
            custom_config = r'--oem 3 --psm 6 -l spa+eng'

            # Convertir PDF a imágenes
            images = convert_from_path(
                self.pdf_path,
                dpi=300,  # Alta resolución para mejor OCR
                first_page=1,
                last_page=5  # Limitar a primeras 5 páginas para facturas grandes
            )

            text = ""
            total_conf = 0

            for i, image in enumerate(images):
                self.logger.debug(f"  OCR página {i+1}/{len(images)}")

                # OCR con datos de confianza
                ocr_data = pytesseract.image_to_data(
                    image,
                    lang='spa+eng',
                    config=custom_config,
                    output_type=pytesseract.Output.DICT
                )

                # Extraer texto
                page_text = pytesseract.image_to_string(
                    image,
                    lang='spa+eng',
                    config=custom_config
                )
                text += page_text + "\n"

                # Calcular confianza promedio
                confidences = [int(conf) for conf in ocr_data['conf'] if conf != '-1']
                if confidences:
                    total_conf += sum(confidences) / len(confidences)

            avg_confidence = total_conf / len(images) if images else 0
            self.logger.info(f"  📊 Confianza OCR: {avg_confidence:.1f}%")

            return text, avg_confidence

        except Exception as e:
            self.logger.error(f"❌ OCR falló: {e}")
            return "", 0.0

    def _extract_tables(self) -> List[List[List[str]]]:
        """Extrae tablas del PDF"""
        tables = []
        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                for page in pdf.pages:
                    page_tables = page.extract_tables()
                    if page_tables:
                        tables.extend(page_tables)
        except Exception as e:
            self.logger.warning(f"⚠️ Extracción de tablas falló: {e}")

        return tables

    def _parse_invoice_data(self, invoice_data: InvoiceData, text: str, tables: List):
        """Parsea datos estructurados de la factura"""

        # Número de factura
        invoice_data.invoice_number = self._extract_invoice_number(text)

        # Fechas
        invoice_data.invoice_date = self._extract_date(text, ["fecha", "date", "fecha de emisión"])
        invoice_data.due_date = self._extract_date(text, ["vencimiento", "due date", "fecha de vencimiento"])

        # Montos
        invoice_data.total_amount = self._extract_amount(text, ["total", "importe total", "amount"])
        invoice_data.tax_amount = self._extract_amount(text, ["iva", "tax", "impuesto"])
        invoice_data.subtotal = self._extract_amount(text, ["subtotal", "base imponible"])

        # Moneda
        invoice_data.currency = self._extract_currency(text)

        # Vendedor
        invoice_data.vendor_name = self._extract_vendor(text)

        # Items de la factura
        invoice_data.items = self._extract_items(tables)

        # Cliente
        invoice_data.customer_name = self._extract_customer(text)

        # Términos de pago
        invoice_data.payment_terms = self._extract_payment_terms(text)

    def _extract_invoice_number(self, text: str) -> Optional[str]:
        """Extrae número de factura"""
        patterns = [
            r'(?:factura|invoice|#|no\.|número)[\s:]*([A-Z0-9\-]+)',
            r'(?:folio|ref)[\s:]*([A-Z0-9\-]+)',
            r'\b([A-Z]{1,3}[\-/]?\d{4,10})\b'
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        return None

    def _extract_date(self, text: str, keywords: List[str]) -> Optional[str]:
        """Extrae fechas"""
        for keyword in keywords:
            # Buscar fecha cerca del keyword
            pattern = rf'{keyword}[\s:]*(\d{{1,2}}[\/\-\.]\d{{1,2}}[\/\-\.]\d{{2,4}})'
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1)

        # Buscar cualquier fecha en formato común
        date_pattern = r'\b(\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{2,4})\b'
        match = re.search(date_pattern, text)
        if match:
            return match.group(1)

        return None

    def _extract_amount(self, text: str, keywords: List[str]) -> Optional[float]:
        """Extrae montos monetarios"""
        for keyword in keywords:
            # Buscar monto cerca del keyword
            pattern = rf'{keyword}[\s:]*[\$€£]?\s*([\d,]+\.?\d{{0,2}})'
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                amount_str = match.group(1).replace(',', '')
                try:
                    return float(amount_str)
                except ValueError:
                    continue

        return None

    def _extract_currency(self, text: str) -> Optional[str]:
        """Extrae moneda"""
        currencies = {
            r'\$|USD|usd|dólar': 'USD',
            r'€|EUR|euro': 'EUR',
            r'£|GBP|libra': 'GBP',
            r'MXN|mxn|peso': 'MXN'
        }

        for pattern, currency in currencies.items():
            if re.search(pattern, text):
                return currency

        return None

    def _extract_vendor(self, text: str) -> Optional[str]:
        """Extrae nombre del vendedor"""
        # Buscar después de keywords comunes
        patterns = [
            r'(?:vendedor|proveedor|de|from)[\s:]+([A-Z][A-Za-z\s&\.]+?)(?:\n|RFC|TAX)',
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()

        # Si no encuentra, tomar primera línea con nombre propio
        lines = text.split('\n')
        for line in lines[:10]:  # Primeras 10 líneas
            if re.match(r'^[A-Z][A-Za-z\s&\.]{5,50}$', line.strip()):
                return line.strip()

        return None

    def _extract_customer(self, text: str) -> Optional[str]:
        """Extrae nombre del cliente"""
        patterns = [
            r'(?:cliente|customer|bill to)[\s:]+([A-Z][A-Za-z\s&\.]+?)(?:\n|RFC|TAX)',
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()

        return None

    def _extract_items(self, tables: List) -> Optional[List[Dict]]:
        """Extrae items de las tablas"""
        if not tables:
            return None

        items = []
        for table in tables:
            if len(table) < 2:  # Necesita al menos header + 1 fila
                continue

            # Intentar identificar columnas
            header = [str(h).lower() if h else '' for h in table[0]]

            # Buscar índices de columnas importantes
            desc_idx = self._find_column_index(header, ['descripción', 'description', 'concepto', 'item'])
            qty_idx = self._find_column_index(header, ['cantidad', 'qty', 'quantity'])
            price_idx = self._find_column_index(header, ['precio', 'price', 'unit price'])
            amount_idx = self._find_column_index(header, ['importe', 'amount', 'total'])

            # Procesar filas
            for row in table[1:]:
                if not any(row):  # Fila vacía
                    continue

                item = {}

                if desc_idx is not None and desc_idx < len(row):
                    item['description'] = row[desc_idx]

                if qty_idx is not None and qty_idx < len(row):
                    item['quantity'] = self._parse_number(row[qty_idx])

                if price_idx is not None and price_idx < len(row):
                    item['unit_price'] = self._parse_number(row[price_idx])

                if amount_idx is not None and amount_idx < len(row):
                    item['amount'] = self._parse_number(row[amount_idx])

                if item:  # Si se extrajo algo
                    items.append(item)

        return items if items else None

    def _find_column_index(self, header: List[str], keywords: List[str]) -> Optional[int]:
        """Encuentra índice de columna por keywords"""
        for i, col in enumerate(header):
            for keyword in keywords:
                if keyword in col:
                    return i
        return None

    def _parse_number(self, value: Any) -> Optional[float]:
        """Parsea número de string"""
        if value is None:
            return None

        value_str = str(value).replace(',', '').replace('$', '').replace('€', '').strip()
        try:
            return float(value_str)
        except ValueError:
            return None

    def _extract_payment_terms(self, text: str) -> Optional[str]:
        """Extrae términos de pago"""
        patterns = [
            r'(?:términos|terms|payment terms)[\s:]+([^\n]{10,50})',
            r'(net \d+ days)',
            r'(\d+ días)'
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()

        return None


class InvoiceProcessingAgent:
    """Agente Principal - Coordina el procesamiento paralelo"""

    def __init__(self,
                 input_dir: str,
                 output_dir: str = "./processed_invoices",
                 max_workers: Optional[int] = None,
                 use_ocr: bool = True):

        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.use_ocr = use_ocr

        # Número de workers (CPUs - 1 por defecto)
        self.max_workers = max_workers or max(1, mp.cpu_count() - 1)

        # Setup
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.logger = self._setup_logger()

        # Directorios de salida
        self.logs_dir = self.output_dir / "logs"
        self.processed_dir = self.output_dir / "processed"
        self.failed_dir = self.output_dir / "failed"

        for dir_path in [self.logs_dir, self.processed_dir, self.failed_dir]:
            dir_path.mkdir(exist_ok=True)

    def _setup_logger(self) -> logging.Logger:
        """Configura logger principal"""
        logger = logging.getLogger("MainAgent")
        logger.setLevel(logging.INFO)

        # Console handler
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter(
            '[MAIN] %(asctime)s - %(levelname)s - %(message)s',
            datefmt='%H:%M:%S'
        )
        console_handler.setFormatter(console_formatter)

        # File handler
        log_file = self.output_dir / "logs" / f"processing_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        log_file.parent.mkdir(exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(file_formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        return logger

    def find_invoices(self) -> List[Path]:
        """Encuentra todos los PDFs en el directorio de entrada"""
        pdf_files = list(self.input_dir.glob("*.pdf"))
        self.logger.info(f"📁 Encontradas {len(pdf_files)} facturas en {self.input_dir}")
        return pdf_files

    def process_single_invoice(self, args: tuple) -> InvoiceData:
        """Procesa una factura (usado por multiprocessing)"""
        invoice_id, pdf_path, output_dir, use_ocr = args

        extractor = InvoiceExtractor(
            invoice_id=invoice_id,
            pdf_path=str(pdf_path),
            output_dir=output_dir,
            use_ocr=use_ocr
        )

        return extractor.extract()

    def process_all(self) -> pd.DataFrame:
        """Procesa todas las facturas en paralelo"""

        self.logger.info("=" * 80)
        self.logger.info("🚀 PERSONAL OS | INVOICE INTELLIGENCE (OCR)")
        self.logger.info("=" * 80)

        notify_voice(f"Iniciando procesamiento paralelo de {len(pdf_files)} facturas.")

        start_time = datetime.now()

        # Encontrar facturas
        pdf_files = self.find_invoices()

        if not pdf_files:
            self.logger.warning("⚠️ No se encontraron facturas para procesar")
            return pd.DataFrame()

        self.logger.info(f"⚙️ Configuración:")
        self.logger.info(f"   • Workers: {self.max_workers}")
        self.logger.info(f"   • OCR: {'Activado' if self.use_ocr else 'Desactivado'}")
        self.logger.info(f"   • Facturas: {len(pdf_files)}")
        self.logger.info("")

        # Preparar argumentos para workers
        worker_args = [
            (i, pdf_path, str(self.output_dir), self.use_ocr)
            for i, pdf_path in enumerate(pdf_files, 1)
        ]

        # Procesar en paralelo
        self.logger.info(f"🔄 Desplegando {self.max_workers} subagentes...")

        results = []

        with mp.Pool(processes=self.max_workers) as pool:
            # Usar imap_unordered para obtener resultados conforme terminan
            for result in pool.imap_unordered(self.process_single_invoice, worker_args):
                results.append(result)

                # Log de progreso
                completed = len(results)
                progress = (completed / len(pdf_files)) * 100
                self.logger.info(f"📊 Progreso: {completed}/{len(pdf_files)} ({progress:.1f}%)")

        # Crear DataFrame con resultados
        df = self._create_results_dataframe(results)

        # Guardar resultados
        self._save_results(df, results)

        # Organizar PDFs procesados
        self._organize_processed_pdfs(results, pdf_files)

        # Resumen final
        end_time = datetime.now()
        total_time = (end_time - start_time).total_seconds()

        self._print_summary(df, total_time)

        notify_voice(f"Procesamiento completado. {len(df[df['status'] == 'success'])} facturas exitosas.")

        return df

    def _create_results_dataframe(self, results: List[InvoiceData]) -> pd.DataFrame:
        """Crea DataFrame con los resultados"""
        data = [asdict(r) for r in results]
        df = pd.DataFrame(data)

        # Convertir items a string para CSV
        if 'items' in df.columns:
            df['items'] = df['items'].apply(lambda x: json.dumps(x) if x else None)

        return df

    def _save_results(self, df: pd.DataFrame, results: List[InvoiceData]):
        """Guarda resultados en múltiples formatos"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        # CSV
        csv_path = self.output_dir / f"invoices_{timestamp}.csv"
        df.to_csv(csv_path, index=False, encoding='utf-8-sig')
        self.logger.info(f"💾 CSV guardado: {csv_path}")

        # Excel con formato
        excel_path = self.output_dir / f"invoices_{timestamp}.xlsx"
        with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Facturas', index=False)

            # Auto-ajustar ancho de columnas
            worksheet = writer.sheets['Facturas']
            for column in worksheet.columns:
                max_length = 0
                column = [cell for cell in column]
                for cell in column:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(cell.value)
                    except:
                        pass
                adjusted_width = min(max_length + 2, 50)
                worksheet.column_dimensions[column[0].column_letter].width = adjusted_width

        self.logger.info(f"💾 Excel guardado: {excel_path}")

        # JSON detallado
        json_path = self.output_dir / f"invoices_{timestamp}.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump([asdict(r) for r in results], f, indent=2, ensure_ascii=False, default=str)

        self.logger.info(f"💾 JSON guardado: {json_path}")

    def _organize_processed_pdfs(self, results: List[InvoiceData], pdf_files: List[Path]):
        """Organiza PDFs procesados en carpetas por fecha"""

        for result, pdf_path in zip(results, pdf_files):
            try:
                # Determinar carpeta destino
                if result.status == "success":
                    # Organizar por fecha si existe
                    if result.invoice_date:
                        # Extraer año y mes
                        date_parts = result.invoice_date.replace('-', '/').replace('.', '/').split('/')
                        if len(date_parts) >= 3:
                            year = date_parts[2] if len(date_parts[2]) == 4 else f"20{date_parts[2]}"
                            month = date_parts[1].zfill(2)
                            dest_dir = self.processed_dir / f"{year}-{month}"
                        else:
                            dest_dir = self.processed_dir / "no_date"
                    else:
                        dest_dir = self.processed_dir / "no_date"
                else:
                    dest_dir = self.failed_dir

                # Crear directorio y mover
                dest_dir.mkdir(parents=True, exist_ok=True)
                dest_path = dest_dir / pdf_path.name

                # Si ya existe, agregar sufijo
                counter = 1
                while dest_path.exists():
                    dest_path = dest_dir / f"{pdf_path.stem}_{counter}{pdf_path.suffix}"
                    counter += 1

                # Copiar en lugar de mover para no perder originales
                import shutil
                shutil.copy2(pdf_path, dest_path)

            except Exception as e:
                self.logger.warning(f"⚠️ No se pudo organizar {pdf_path.name}: {e}")

    def _print_summary(self, df: pd.DataFrame, total_time: float):
        """Imprime resumen del procesamiento"""

        self.logger.info("")
        self.logger.info("=" * 80)
        self.logger.info("📊 RESUMEN DE PROCESAMIENTO")
        self.logger.info("=" * 80)

        total = len(df)
        success = len(df[df['status'] == 'success'])
        failed = len(df[df['status'] == 'error'])

        self.logger.info(f"Total facturas: {total}")
        self.logger.info(f"✅ Exitosas: {success} ({success/total*100:.1f}%)")
        self.logger.info(f"❌ Fallidas: {failed} ({failed/total*100:.1f}%)")
        self.logger.info(f"⏱️ Tiempo total: {total_time:.2f}s")
        self.logger.info(f"⚡ Tiempo promedio por factura: {total_time/total:.2f}s")

        # Estadísticas de montos
        if 'total_amount' in df.columns:
            amounts = df[df['total_amount'].notna()]['total_amount']
            if len(amounts) > 0:
                self.logger.info("")
                self.logger.info("💰 Estadísticas de montos:")
                self.logger.info(f"   Total: ${amounts.sum():,.2f}")
                self.logger.info(f"   Promedio: ${amounts.mean():,.2f}")
                self.logger.info(f"   Mínimo: ${amounts.min():,.2f}")
                self.logger.info(f"   Máximo: ${amounts.max():,.2f}")

        # OCR confidence si aplica
        if 'ocr_confidence' in df.columns:
            ocr_confs = df[df['ocr_confidence'].notna()]['ocr_confidence']
            if len(ocr_confs) > 0:
                self.logger.info("")
                self.logger.info(f"📸 Confianza OCR promedio: {ocr_confs.mean():.1f}%")

        self.logger.info("=" * 80)


def main():
    """Función principal"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Sistema de Procesamiento Paralelo de Facturas con OCR',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:

  # Procesar facturas en carpeta actual
  python invoice_processor.py ./invoices

  # Especificar carpeta de salida y workers
  python invoice_processor.py ./invoices -o ./results -w 8

  # Desactivar OCR (solo texto directo)
  python invoice_processor.py ./invoices --no-ocr

  # Limitar número de workers
  python invoice_processor.py ./invoices -w 4
        """
    )

    parser.add_argument('input_dir', help='Directorio con PDFs de facturas')
    parser.add_argument('-o', '--output-dir', default='./processed_invoices',
                       help='Directorio de salida (default: ./processed_invoices)')
    parser.add_argument('-w', '--workers', type=int, default=None,
                       help='Número de workers paralelos (default: CPUs-1)')
    parser.add_argument('--no-ocr', action='store_true',
                       help='Desactivar OCR (solo extracción directa de texto)')

    args = parser.parse_args()

    # Verificar que existe el directorio de entrada
    if not Path(args.input_dir).exists():
        print(f"❌ Error: El directorio {args.input_dir} no existe")
        sys.exit(1)

    # Crear agente y procesar
    agent = InvoiceProcessingAgent(
        input_dir=args.input_dir,
        output_dir=args.output_dir,
        max_workers=args.workers,
        use_ocr=not args.no_ocr
    )

    try:
        df = agent.process_all()

        print("\n✅ Procesamiento completado exitosamente!")
        print(f"📁 Resultados guardados en: {agent.output_dir}")

        return 0

    except KeyboardInterrupt:
        print("\n\n⚠️ Procesamiento interrumpido por el usuario")
        return 1
    except Exception as e:
        print(f"\n❌ Error fatal: {e}")
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
