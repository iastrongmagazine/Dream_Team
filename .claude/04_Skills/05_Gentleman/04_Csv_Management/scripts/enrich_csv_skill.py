#!/usr/bin/env python3
"""
SKILL 4: EXTERNAL DATA ENRICHMENT
Archivo: enrich_csv.py
Descripción: Enriquece datasets con datos externos (APIs, scraping, DBs).

Use Cases:
- Agregar funding data de Crunchbase
- Enriquecer con datos de mercado
- Completar información faltante con fuentes públicas

Execution Mode: Isolated subprocess (network I/O, rate limits)
"""

import sys
import json
import time
import requests
import pandas as pd
import re
from pathlib import Path
from typing import Dict, Any, Optional, List
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from dataclasses import dataclass, asdict

@dataclass
class EnrichmentResult:
    """Resultado de enriquecimiento por compañía"""
    company_name: str
    status: str  # 'success', 'partial', 'failed'
    data: Dict[str, Any]
    source: str
    timestamp: str

class StartupEnricher:
    """
    Enriquecedor de datos de startups usando fuentes externas.

    IMPORTANTE: En producción, usar API keys reales y manejar rate limits.
    """

    def __init__(self, csv_path: str, output_path: str):
        self.csv_path = Path(csv_path)
        self.output_path = Path(output_path)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (DataAnalyticsAgent/1.0)',
            'Accept': 'application/json, text/html'
        })
        self.rate_limit_delay = 1.0  # segundos entre requests
        self.enrichment_results: List[EnrichmentResult] = []

    def _clean_company_name(self, name: str) -> str:
        """Normaliza nombre de compañía para búsqueda"""
        # Remover caracteres especiales, normalizar espacios
        cleaned = re.sub(r'[^\w\s-]', '', str(name))
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()
        return cleaned

    def get_crunchbase_data(self, company_name: str) -> Dict[str, Any]:
        """
        Obtiene datos de Crunchbase.

        NOTA DE PRODUCCIÓN:
        - Usar Crunchbase API oficial con API key
        - Endpoint: https://api.crunchbase.com/api/v4/entities/organizations/{name}
        - Requiere suscripción: https://www.crunchbase.com/products/api

        Esta versión usa datos simulados para demostración.
        """
        clean_name = self._clean_company_name(company_name)

        # En producción, descomentar y usar API real:
        # api_key = os.environ.get('CRUNCHBASE_API_KEY')
        # url = f"https://api.crunchbase.com/api/v4/entities/organizations/{clean_name}"
        # headers = {"X-cb-user-key": api_key}
        # response = self.session.get(url, headers=headers)

        # VERSIÓN DEMO: Simulación de respuesta
        time.sleep(self.rate_limit_delay)  # Respetar rate limits

        # Simular datos basados en nombre
        simulated_data = {
            "name": clean_name,
            "total_funding_usd": self._simulate_funding(clean_name),
            "last_funding_type": self._simulate_stage(clean_name),
            "employee_count": self._simulate_employees(clean_name),
            "founded_on": "2020-01-01",
            "categories": ["Technology", "SaaS"],
            "website_url": f"https://{clean_name.lower().replace(' ', '')}.com",
            "headquarters_location": "San Francisco, CA",
            "source": "Crunchbase (Simulated)"
        }

        return simulated_data

    def _simulate_funding(self, name: str) -> int:
        """Genera funding simulado basado en hash del nombre"""
        hash_val = sum(ord(c) for c in name)
        return (hash_val % 50 + 1) * 1000000  # Entre $1M y $50M

    def _simulate_stage(self, name: str) -> str:
        """Genera stage simulado"""
        stages = ["Seed", "Series A", "Series B", "Series C"]
        hash_val = sum(ord(c) for c in name)
        return stages[hash_val % len(stages)]

    def _simulate_employees(self, name: str) -> int:
        """Genera employee count simulado"""
        hash_val = sum(ord(c) for c in name)
        return (hash_val % 200) + 10  # Entre 10 y 210

    def get_linkedin_data(self, company_name: str) -> Dict[str, Any]:
        """
        Enriquece con datos de LinkedIn Company Pages.

        NOTA DE PRODUCCIÓN:
        - Usar LinkedIn API oficial (requiere partnership)
        - O herramientas como Phantombuster, Apify
        - Respetar robots.txt y términos de servicio
        """
        # Placeholder para mantener la estructura
        return {
            "employee_count_linkedin": None,
            "industry": "Technology",
            "specialties": ["Software Development"],
            "source": "LinkedIn (Not Implemented)"
        }

    def get_company_website_info(self, website: str) -> Dict[str, Any]:
        """
        Extrae información básica del website de la compañía.
        Información técnica como tecnologías usadas, presencia en redes.
        """
        if not website or not website.startswith('http'):
            return {"error": "Invalid website URL"}

        try:
            response = self.session.get(website, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extraer metadatos básicos
            title = soup.find('title')
            description = soup.find('meta', {'name': 'description'})

            return {
                "page_title": title.text if title else None,
                "meta_description": description.get('content') if description else None,
                "has_blog": bool(soup.find('a', href=re.compile(r'/blog'))),
                "has_careers": bool(soup.find('a', href=re.compile(r'/careers|/jobs'))),
                "social_media": {
                    "twitter": bool(soup.find('a', href=re.compile(r'twitter.com'))),
                    "linkedin": bool(soup.find('a', href=re.compile(r'linkedin.com')))
                }
            }
        except Exception as e:
            return {"error": str(e)}

    def enrich_row(self, row: pd.Series, company_col: str = 'Company Name') -> Dict[str, Any]:
        """
        Enriquece una fila individual del dataset.
        """
        company_name = row.get(company_col, '')

        if not company_name or pd.isna(company_name):
            return {
                "status": "skipped",
                "reason": "No company name provided"
            }

        # Intentar múltiples fuentes
        enriched_data = {}

        try:
            # Fuente 1: Crunchbase
            cb_data = self.get_crunchbase_data(company_name)
            enriched_data.update({
                "cb_funding": cb_data.get('total_funding_usd'),
                "cb_stage": cb_data.get('last_funding_type'),
                "cb_employees": cb_data.get('employee_count'),
                "cb_founded": cb_data.get('founded_on'),
                "cb_location": cb_data.get('headquarters_location')
            })

            # Fuente 2: Website (si está disponible)
            if 'website' in row and pd.notna(row['website']):
                web_data = self.get_company_website_info(row['website'])
                enriched_data['website_analysis'] = web_data

            result = EnrichmentResult(
                company_name=company_name,
                status='success',
                data=enriched_data,
                source='crunchbase_simulated',
                timestamp=time.strftime('%Y-%m-%d %H:%M:%S')
            )

        except Exception as e:
            result = EnrichmentResult(
                company_name=company_name,
                status='failed',
                data={},
                source='error',
                timestamp=time.strftime('%Y-%m-%d %H:%M:%S')
            )
            enriched_data = {"error": str(e)}

        self.enrichment_results.append(result)
        return enriched_data

    def process(self, max_rows: Optional[int] = None, company_col: str = 'Company Name') -> str:
        """
        Procesa el CSV completo y genera versión enriquecida.

        Args:
            max_rows: Limitar procesamiento (útil para testing)
            company_col: Nombre de la columna con nombres de compañías

        Returns:
            Path del archivo enriquecido
        """
        print(f"🔄 Enriqueciendo {self.csv_path.name}...")

        try:
            df = pd.read_csv(self.csv_path)

            if max_rows:
                df = df.head(max_rows)
                print(f"⚠️  Limitado a {max_rows} filas para demostración")

            print(f"📊 Procesando {len(df)} compañías...")

            # Aplicar enriquecimiento
            enrichment_data = []
            for idx, row in df.iterrows():
                print(f"  [{idx+1}/{len(df)}] {row.get(company_col, 'Unknown')}", end='\r')
                enriched = self.enrich_row(row, company_col)
                enrichment_data.append(enriched)

            print()  # Nueva línea después del progreso

            # Expandir datos enriquecidos en columnas
            enriched_df = pd.DataFrame(enrichment_data)

            # Combinar con dataset original
            result_df = pd.concat([df, enriched_df], axis=1)

            # Guardar
            result_df.to_csv(self.output_path, index=False)

            # Estadísticas
            success_count = sum(1 for r in self.enrichment_results if r.status == 'success')

            summary = f"""
✅ Enriquecimiento completado!
📁 Archivo guardado: {self.output_path}
📊 Estadísticas:
   - Total procesado: {len(df)}
   - Exitosos: {success_count}
   - Fallidos: {len(df) - success_count}
   - Nuevas columnas: {len(enriched_df.columns)}
"""
            return summary

        except Exception as e:
            return f"❌ Error en enriquecimiento: {e}"

    def get_enrichment_report(self) -> Dict[str, Any]:
        """Genera reporte del proceso de enriquecimiento"""
        return {
            "total_processed": len(self.enrichment_results),
            "successful": sum(1 for r in self.enrichment_results if r.status == 'success'),
            "failed": sum(1 for r in self.enrichment_results if r.status == 'failed'),
            "sources_used": list(set(r.source for r in self.enrichment_results)),
            "results": [asdict(r) for r in self.enrichment_results[:10]]  # Primeros 10
        }

# ============================================================================
# ISOLATED AGENT MODE
# ============================================================================

def run_isolated_enrichment(params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Ejecuta enriquecimiento en modo aislado.
    """
    input_csv = params.get('input_csv')
    output_csv = params.get('output_csv', 'enriched_output.csv')
    max_rows = params.get('max_rows', 50)  # Limitar por defecto
    company_col = params.get('company_col', 'Company Name')

    if not input_csv:
        raise ValueError("input_csv is required")

    enricher = StartupEnricher(input_csv, output_csv)
    summary = enricher.process(max_rows=max_rows, company_col=company_col)
    report = enricher.get_enrichment_report()

    return {
        "summary": summary,
        "report": report,
        "output_file": output_csv
    }

def main():
    """Entry point for isolated execution"""
    if len(sys.argv) != 3:
        print("Usage: enrich_csv.py <input.json> <output.json>", file=sys.stderr)
        sys.exit(1)

    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2])

    try:
        with open(input_file, 'r') as f:
            params = json.load(f)

        result = run_isolated_enrichment(params)

        with open(output_file, 'w') as f:
            json.dump({
                "status": "success",
                "result": result,
                "metadata": {
                    "agent": "startup_enricher",
                    "version": "2.0",
                    "sources": ["crunchbase_simulated", "website_scraping"]
                }
            }, f, indent=2)

    except Exception as e:
        with open(output_file, 'w') as f:
            json.dump({
                "status": "error",
                "result": None,
                "metadata": {
                    "error": str(e),
                    "agent": "startup_enricher"
                }
            }, f, indent=2)
        sys.exit(1)

if __name__ == "__main__":
    main()
