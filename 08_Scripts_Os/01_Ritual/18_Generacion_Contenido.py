#!/usr/bin/env python3
"""
18_Generacion_Contenido.py - PersonalOS Content Generation v3.0
=============================================================
Basado en: examples/workflows/content-generation.md

Genera contenido en la voz auténtica del usuario.

Usage:
    python 18_Generacion_Contenido.py              # Modo interactivo
    python 18_Generacion_Contenido.py --blog       # Generar blog post
    python 18_Generacion_Contenido.py --linkedin   # Generar LinkedIn
    python 18_Generacion_Contenido.py --email      # Generar email
"""

import sys
import os
import io
import argparse
from pathlib import Path
from datetime import datetime

# Fix Windows encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# Path resolution
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "08_Scripts_Os" / "Legacy_Backup"))
from config_paths import ROOT_DIR, KNOWLEDGE_DIR


# ============================================================================
# CONFIGURATION
# ============================================================================

KNOWLEDGE_DIR = PROJECT_ROOT / "02_Knowledge"
VOICE_SAMPLES_DIR = KNOWLEDGE_DIR / "voice-samples"
VOICE_GUIDE_FILE = KNOWLEDGE_DIR / "voice-guide.md"
GOALS_FILE = PROJECT_ROOT / "00_Winter_is_Coming" / "GOALS.md"


# ============================================================================
# FUNCTIONS
# ============================================================================


def print_banner():
    """Print content generation banner."""
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║          ✍️  C O N T E N T   G E N E R A T I O N                 ║
║              Think Different PersonalOS v3.0                           ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
""")


def step1_check_voice_samples():
    """Step 1: Check for voice samples."""
    print("\n" + "=" * 70)
    print("📝 STEP 1: Buscando Voice Samples...")
    print("=" * 70)

    if VOICE_SAMPLES_DIR.exists():
        samples = list(VOICE_SAMPLES_DIR.glob("*.md")) + list(
            VOICE_SAMPLES_DIR.glob("*.txt")
        )
        if samples:
            print(f"\n✅ Se encontraron {len(samples)} voice samples:")
            for s in samples[:3]:
                print(f"   • {s.name}")
            return True
        else:
            print("\n⚠️  Directorio existe pero vacío")
    else:
        print(f"\n📭 No existe: {VOICE_SAMPLES_DIR}")

    print("\n💡 Opciones:")
    print("   1. Compartir ejemplos de tu escritura")
    print("   2. Usar tono profesional neutral")
    print("   3. Describir estilo preferido")

    return False


def step2_check_voice_guide():
    """Step 2: Check for voice guide."""
    print("\n" + "=" * 70)
    print("📝 STEP 2: Buscando Voice Guide...")
    print("=" * 70)

    if VOICE_GUIDE_FILE.exists():
        print(f"\n✅ Voice Guide encontrado: {VOICE_GUIDE_FILE.name}")
        # Read first lines
        content = VOICE_GUIDE_FILE.read_text(encoding="utf-8")
        lines = [l for l in content.split("\n") if l.strip()][:10]
        print("\n📋 Primeros puntos:")
        for line in lines:
            if line.strip().startswith("-"):
                print(f"   {line.strip()}")
        return True
    else:
        print(f"\n📭 No existe: {VOICE_GUIDE_FILE}")
        print("   Generando desde samples o usando defaults...")

    return False


def step3_gather_context(content_type: str):
    """Step 3: Gather context based on content type."""
    print("\n" + "=" * 70)
    print("📝 STEP 3: Recopilando Contexto...")
    print("=" * 70)

    print(f"\n📌 Tipo de contenido: {content_type}")

    # Check Knowledge for relevant docs
    if KNOWLEDGE_DIR.exists():
        docs = list(KNOWLEDGE_DIR.glob("*.md"))[:5]
        if docs:
            print(f"\n📚 Documentos relevantes en Knowledge:")
            for doc in docs:
                print(f"   • {doc.name}")

    # Check GOALS
    if GOALS_FILE.exists():
        print(f"\n🎯 Goals disponibles")

    return True


def step4_draft_content(content_type: str, topic: str):
    """Step 4: Draft content (template generation)."""
    print("\n" + "=" * 70)
    print("📝 STEP 4: Generando Borrador...")
    print("=" * 70)

    templates = {
        "blog": """# {topic}

## Introducción
[Hook - comenzar con el punto más interesante]

## Contenido Principal
[Puntos clave del tema]

## Conclusión
[Resumen + CTA]

---
*Generado: {date}*
""",
        "linkedin": """🎯 {topic}

[Hook en 1 línea]

💡 Punto principal:
- [Insight 1]
- [Insight 2]
- [Insight 3]

🔥 ¿Qué opinas? 💬

---
*Generado: {date}*
""",
        "email": """Hola [Nombre],

[Breve introducción - max 2 líneas]

[Mensaje principal]

[CTA o siguiente paso]

Saludos,
---
*Generado: {date}*
""",
    }

    template = templates.get(content_type, templates["blog"])
    date = datetime.now().strftime("%Y-%m-%d")

    draft = template.format(topic=topic, date=date)

    print(f"\n📝 BORRADOR GENERADO ({content_type}):")
    print("-" * 40)
    print(draft)
    print("-" * 40)

    return draft


def step5_present_options():
    """Step 5: Present draft with options."""
    print("\n" + "=" * 70)
    print("📝 STEP 5: Opciones de Ajuste...")
    print("=" * 70)

    print("\n📌 ¿Querés que ajuste el borrador?")
    print("   1. ✅ Aprobar como está")
    print("   2. 📝 Ajustar tono (más casual / más formal)")
    print("   3. ✂️  Acortar o expandir secciones")
    print("   4. 🔄 Cambiar estructura o énfasis")

    print("\n" + "=" * 70)


def run_full_workflow(content_type: str, topic: str):
    """Run the complete 5-step content generation workflow."""
    print_banner()
    print(f"🚀 Iniciando Content Generation para: {content_type}")

    # Step 1: Voice Samples
    has_samples = step1_check_voice_samples()

    # Step 2: Voice Guide
    has_guide = step2_check_voice_guide()

    # Step 3: Gather Context
    step3_gather_context(content_type)

    # Step 4: Draft
    draft = step4_draft_content(content_type, topic)

    # Step 5: Present
    step5_present_options()

    print("\n✅ Workflow completado!")
    return draft


def interactive_mode():
    """Run in interactive mode."""
    print_banner()

    print("\n📌 ¿Qué tipo de contenido?")
    print("   1. 📝 Blog Post")
    print("   2. 💼 LinkedIn")
    print("   3. 📧 Email")
    print("   4. 🐦 Twitter/X Thread")

    choice = input("\n👉 Opción (1-4): ").strip()

    types = {"1": "blog", "2": "linkedin", "3": "email", "4": "twitter"}
    content_type = types.get(choice, "blog")

    topic = input("\n📌 Tema del contenido: ").strip()

    if not topic:
        topic = "Nuevo contenido"

    run_full_workflow(content_type, topic)


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Content Generation v3.0")
    parser.add_argument("--blog", action="store_true", help="Generar blog post")
    parser.add_argument("--linkedin", action="store_true", help="Generar LinkedIn")
    parser.add_argument("--email", action="store_true", help="Generar email")
    parser.add_argument("--twitter", action="store_true", help="Generar Twitter thread")
    parser.add_argument(
        "--topic", type=str, default="Nuevo contenido", help="Tema del contenido"
    )

    args = parser.parse_args()

    if args.blog:
        run_full_workflow("blog", args.topic)
    elif args.linkedin:
        run_full_workflow("linkedin", args.topic)
    elif args.email:
        run_full_workflow("email", args.topic)
    elif args.twitter:
        run_full_workflow("twitter", args.topic)
    else:
        interactive_mode()
