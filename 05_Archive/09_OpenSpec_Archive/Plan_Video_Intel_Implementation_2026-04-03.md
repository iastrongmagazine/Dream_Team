# PLAN DE IMPLEMENTACIÓN: Skill Video_Intel (2026-04-03)

## 🎯 Visión
Skill para extraer conocimiento estructurado de YouTube/GitHub y actualizar el PersonalOS.

## 🛠 Componentes
1. **SKILL.md**: YAML frontmatter + Workflow + Gotchas.
2. **scripts/video_analyzer.py**: Extracción (yt-dlp, whisper).
3. **scripts/repo_scanner.py**: Análisis AST (GitHub).
4. **scripts/synthesis_engine.py**: Metodologías + Verificación OS + Plan.
5. **scripts/cli.py**: Interfaz Click CLI.

## 📋 Flujo de Trabajo
1. `analyze <URL>`
2. Extracción de contenido
3. Análisis de metodologías
4. Extracción de demos/prompts
5. Verificación vs OS
6. Generar documento en raíz
7. Migrar a `02_Knowledge/05_Unicorn/`
8. Registro en `video_analysis_registry.md`

## 📊 Integración al OS
- Inyección de contexto en cada sesión.
- Guardado persistente en Engram (topic: `unicorn/video-intel-skill`).

---

*Implementado mediante SDD Workflow (2026-04-03)*

PAN COMPLETO - Video_Intel Skill
Guardé el plan en Engram con topic_key: unicorn/video-intel-skill.
Estructura basada en Skill_Auditor:
01_Core/03_Skills/XX_Video_Intel/
├── SKILL.md                    # < 200 líneas
├── scripts/
│   ├── video_analyzer.py       # Core: extracción + análisis
│   ├── video_registry.py      # Registro de videos analizados
│   └── os_integration.py      # Verificación vs OS
└── references/
    ├── methodology-mapping.md
    ├── prompt-extraction.md
    └── implementation-templates.md
    
Cumplimiento con estándares Skill_Auditor:
Criterio
YAML frontmatter
Esencia Original
Gotchas (3+ errores)
Progressive disclosure
State persistence
scripts/ folder
Flujo completo (9 pasos):
1. Input URL → YouTube o GitHub
2. Extraer contenido → Transcripts, README, código
3. Analizar metodologías → Identificar patrones SOTA
4. Extraer demos/prompts → Lists de ejemplos
5. Verificar vs OS → Detectar gaps
6. Crear plan de implementación → Skill vs Script vs MCP
7. Generar documento en raíz → Video_Analysis_{fecha}_{tema}.md
8. Migrar conocimiento → 02_Knowledge/05_Unicorn/
9. Actualizar registro → Video registry con temas + recomendaciones
Triggers (qué dice el usuario para activar):
- "analiza este video"
- "analiza repo"
- "saca los prompts"
- "verifica vs OS"
- "video analysis"
Gotchas documentadas (3+):
- Videos sin transcript disponible
- Repos con documentación incompleta
- Metodologías implícitas, no explícitas
- Demos necesitan adaptación al OS
---
📋 RESUMEN EJECUTIVO DE TODO EL PLAN MAESTRO
Guardé en Engram:
1. ✅ Unicorn Engineering - 21 archivos SOTA
2. ✅ Metodologías 2026 por área
3. ✅ Video analysis del YouTube
4. ✅ Video_Intel skill plan completo
Próximo paso: Cuando digas "APROBADO" salgo del modo Plan y ejecuto TODO:
-Creo la Skill Video_Intel
-La audito con Skill_Auditor
-Analizo el primer video/repo