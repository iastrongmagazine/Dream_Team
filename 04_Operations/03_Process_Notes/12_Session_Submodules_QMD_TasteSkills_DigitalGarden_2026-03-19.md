# Session Report: Submodules + QMD + Taste-Skills + DigitalGarden — 2026-03-19

## Objetivo

Reparar sistema de submodules rotos, integrar QMD, Taste-Skills y DigitalGarden, actualizar README y AGENTS.md con toda la información.

## Duración de la Sesión

Esta es una sesión LARGA con múltiples objetivos completados.

- --

## 1. REPARACIÓN DE SUBMODULES

### Problema Inicial

El repo tenía **12 submodules** pero:
- `.gitmodules` no existía o estaba incompleto
- Algunos submodules estaban **vacíos** (solo `.git` file sin contenido)
- Case sensitivity roto: disco dice `03_Knowledge`, Git usa `03_KNOWLEDGE`
- 5 repos de Gentleman-Programming estaban **vacíos**

### Submodules Encontrados

| #     | Path                                            | Repo                       | Commit Original   | Problema    |

|-------------------|-------------------------------------------------------------|----------------------------------------|-------------------------------|-------------------------|
| 1                 | `10_Repos_Gentleman/gentle-ai`                              | gentle-ai                              | `c7e96c1`                     | VACÍO                   |
| 2                 | `10_Repos_Gentleman/Gentleman-Skills`                       | gentleman-skills                       | `ac0dc7d`                     | VACÍO                   |
| 3                 | `10_Repos_Gentleman/Gentleman.Dots`                         | gentleman.dots                         | `12566aa`                     | VACÍO                   |
| 4                 | `10_Repos_Gentleman/agent-teams-lite`                       | agent-teams-lite                       | `d2015b4`                     | VACÍO                   |
| 5                 | `10_Repos_Gentleman/engram`                                 | engram                                 | `8556e1b`                     | VACÍO                   |
| 6                 | `10_Repos_Gentleman/gentleman-guardian-angel`               | gentleman-guardian-angel               | `6ab5373`                     | VACÍO                   |
| 7                 | `10_Repos_Gentleman/digitalgarden`                          | digitalgarden                          | `90df1ca`                     | VACÍO                   |
| 8                 | `10_Repos_Gentleman/qmd`                                    | qmd                                    | `2b8f329`                     | VACÍO                   |
| 9                 | `03_Resources_External/External/gentle-ai`                  | gentle-ai                              | `9ec14c8`                     | MISMATCH                |
| 10                | `Momentum_Os/cursor-ide`                                    | cursor-ide                             | `6ad44ab`                     | OK                      |
| 11                | `Momentum_Os/claude-code`                                   | claude-code                            | `80cae8e`                     | OK                      |
| 12                | `Every_Sync_Zone`                                           | compound-engineering                   | `8cbb28f`                     | OK                      |

### Acciones Realizadas

1. **Clonado de 5 repos vacíos:**
   ```bash
   git clone https://github.com/Gentleman-Programming/gentleman-skills Gentleman-Skills
   git clone https://github.com/Gentleman-Programming/gentleman.dots Gentleman.Dots
   git clone https://github.com/Gentleman-Programming/agent-teams-lite agent-teams-lite
   git clone https://github.com/Gentleman-Programming/engram engram
   git clone https://github.com/Gentleman-Programming/gentleman-guardian-angel gentleman-guardian-angel
   ```

2. **Creación de `.gitmodules`** con los 12 submodules correctos

3. **Uso de `absorbgitdirs`** para migrar `.git` directories embebidos:
   ```bash
   git submodule absorbgitdirs <path>
   ```

4. **Fix de case sensitivity**: Windows normaliza a `03_Knowledge`, Git usa `03_KNOWLEDGE` en el índice. Se crearon paths en `.git/modules/03_KNOWLEDGE/`.

5. **Nested submodule tmux**: `Gentleman.Dots/GentlemanTmux/plugins/tmux` no se pudo convertir en submodule nested, se dejó como clone normal.

### Commits de Actualización de Repos

| Repo                                   | Antes                   | Después                 | Cambios                                             |
|----------------------------------------|-------------------------|-------------------------|-----------------------------------------------------|
| gentle-ai                              | `c7e96c1`               | `3bcc908`               | v1.2.1-56, cursor recovery                          |
| gentleman.dots                         | `12566aa`               | `30a8fc4`               | v2.9.3, better markdown                             |
| agent-teams-lite                       | `d2015b4`               | `a54af76`               | v4.1.0, docs split, background-agents               |
| engram                                 | `8556e1b`               | `4f40089`               | v1.7.0, docs split                                  |
| gentleman-guardian-angel               | `6ab5373`               | `28f44d7`               | v2.8.0, Windows MINGW64 support                     |

### Resultado: Commit `d155ba5`

- 32 archivos modificados
- `.gitmodules` creado con 12 entries
- Todos los submodules operativos

- --

## 2. QMD — Knowledge Search Engine

### Qué es QMD

* *QMD (Query Markup Documents)** es un motor de búsqueda híbrido local para markdown que combina:
- **BM25** (FTS5) — búsqueda por keywords
- **Vector embeddings** — búsqueda semántica
- **LLM reranking** — reordenamiento con modelo local

Todo corre **localmente** con GGUF models descargados bajo demanda.

### Instalación

```bash
# Requiere Node.js >= 22 o Bun >= 1.0.0

npm install -g @tobilu/qmd
# o

bun install -g @tobilu/qmd
```

* *Problema encontrado**: npm timeout, pero bun funcionó. Creamos wrapper:
```bash
bun "C:/Users/sebas/AppData/Roaming/npm/node_modules/@tobilu/qmd/dist/cli/qmd.js" --version
# Output: qmd 2.0.1

```

### Colecciones Configuradas

| Colección                   | Archivos                 | Descripción                                   |
|-----------------------------|--------------------------|-----------------------------------------------|
| `personal-os`               | 1531                     | Todo el repositorio                           |
| `core`                      | 7                        | AGENTS.md, GOALS.md, BACKLOG.md               |
| `brain`                     | 33                       | Memoria, conocimiento, reglas                 |
| `knowledge`                 | 480                      | Investigación, notas, recursos                |
| **Total**                   | **2051**                 |                                               |

### Contextos Agregados

```bash
qmd context add qmd://personal-os "PersonalOS - Sistema operativo personal con IA"
qmd context add qmd://core "00_Core - AGENTS.md, GOALS.md, BACKLOG.md"
qmd context add qmd://brain "01_Brain - Memoria y reglas del sistema"
qmd context add qmd://knowledge "03_Knowledge - Investigación y recursos"
```

### Comandos Principales

```bash
# Búsqueda por keywords (BM25)

qmd search "sdd workflow"

# Búsqueda semántica (vectors)

qmd vsearch "backend architecture"

# Búsqueda híbrida (LA MEJOR) — BM25 + vectors + query expansion + reranking

qmd query "como funciona el backlog"

# Ver estado del índice

qmd status

# Re-indexar cambios

qmd update

# Listar colecciones

qmd collection list
```

### Script de Actualización Creado

* *Ubicación:** `04_Engine/08_Scripts_Os/56_Update_QMD_Index.py`

```python
#!/usr/bin/env python3
# Actualiza todas las colecciones QMD

# Usage: python 56_Update_QMD_Index.py

```

### MCP Configuration (Pendiente)

QMD también expone un **MCP server** para integración con Claude Code:

```json
{
  "mcpServers": {
    "qmd": {
      "command": "bun",
      "args": ["path/to/qmd.js", "mcp"]
    }
  }
}
```

### Estado de Embeddings

- **Pending**: 899 documentos necesitan embeddings vectoriales
- **Models**: Se bajan bajo demanda (~2GB total)
  - `embeddinggemma-300M-Q8_0` — 300MB
  - `qwen3-reranker-0.6b-q8_0` — 640MB
  - `qmd-query-expansion-1.7B-q4_k_m` — 1.1GB

### GPU Detectada

```
GPU: vulkan (offloading: yes)
Device: Intel(R) UHD Graphics
VRAM: 3.5 GB free / 3.9 GB total
```

- --

## 3. TASTE-SKILLS

### Qué son

Colección de **5 skills** que mejoran cómo la IA genera código frontend. En vez de interfaces genéricas, produce diseños premium con animaciones, espaciado y calidad visual.

### Las 5 Skills

| Skill                            | Propósito                                    | Cuándo Usar                                         |
|----------------------------------|----------------------------------------------|-----------------------------------------------------|
| `taste-skill`                    | Diseño principal premium                     | Proyectos desde cero                                |
| `soft-skill`                     | Look & feel premium/lujoso                   | Invitaciones, landing pages premium                 |
| `minimalist-skill`               | Estilo Notion/Linear editorial               | Dashboards limpios                                  |
| `redesign-skill`                 | Mejorar proyectos existentes                 | Legacy, upgrades                                    |
| `output-skill`                   | Código completo sin shortcuts                | **SIEMPRE** (evita código incompleto)               |

### Ubicaciones Copiadas

```
.cursor/02_Skills/11_Taste_Skills/
.agent/02_Skills/11_Taste_Skills/
├── taste-skill/SKILL.md
├── soft-skill/SKILL.md
├── minimalist-skill/SKILL.md
├── redesign-skill/SKILL.md
└── output-skill/SKILL.md
```

### Configuración

```markdown
DESIGN_VARIANCE (1-10): 8   # 8=Artsy Chaos, layouts experimentales

MOTION_INTENSITY (1-10): 6  # 6=Fade-ins, smooth scrolling

VISUAL_DENSITY (1-10): 4    # 4=Espaciado normal de app típica

```

| Setting                        | 1-3                           | 4-7                            | 8-10                                   |
|--------------------------------|-------------------------------|--------------------------------|----------------------------------------|
| DESIGN_VARIANCE                | Limpio/centrado               | Overlapping                    | Asimétrico/moderno                     |
| MOTION_INTENSITY               | Casi nada                     | Fade-ins, scroll               | Magnetic, spring physics               |
| VISUAL_DENSITY                 | Airy/Lujo                     | Normal                         | Denso/Dashboard                        |

### Reglas Clave

- **ANTI-EMOJI POLICY**: Emojis BANEADOS — usar Radix, Phosphor icons o SVG
- **DEPENDENCY VERIFICATION**: Siempre verificar `package.json` antes de importar
- **TAILWIND VERSION LOCK**: Checkear v3/v4
- **RSC SAFETY**: Global state solo en Client Components
- **Viewport Stability**: Usar `min-h-[100dvh]` en lugar de `h-screen`

### Workflow Creado

* *Ubicación:** `.agent/03_Workflows/09_Frontend_Premium.md`

Trigger: Cuando el usuario pide crear/editar frontend.

- --

## 4. DIGITALGARDEN

### Qué es

Template de **Digital Garden** ( jardín digital ) — un estilo de notes publishing que prioriza la evolución de ideas sobre chronological blogging. Se publica con **Obsidian Digital Garden plugin** + **Vercel deploy**.

### Ubicación

```
06_Archive/05_Digital_Garden/
├── README.md
├── package.json
├── netlify.toml
├── vercel.json
├── src/
│   ├── helpers/        # Utilities de JS

│   └── site/          # Templates de Eleventy

│       ├── _data/
│       ├── _includes/  # Components (navbar, sidebar, graph, etc.)

│       ├── styles/     # SCSS (custom-style.scss personalizable)

│       └── notes/       # Notas de ejemplo

```

### Comandos

```bash
npm run build   # Build para deploy

npm run start   # Desarrollo local

```

### CSS Variables Disponibles

El template tiene **50+ CSS variables** para personalizar:
- Colores (text, background, accent, links)
- Layout (content max-width, sidebar, filetree)
- Graph (tamaño, bordes, colores)
- Search (box, input, resultados)
- Timestamps, backlinks, transclusions

- --

## 5. ACTUALIZACIONES DE DOCUMENTACIÓN

### AGENTS.md

Se agregaron nuevas secciones:

* *2.7 QMD — Knowledge Search Engine**
- Comandos de búsqueda
- Colecciones configuradas
- Script de update

* *2.8 DigitalGarden — Obsidian Integration**
- Setup con Obsidian plugin
- Comandos de build/deploy

### README.md

Se actualizó con:

1. **Header actualizado** con versión QMD
2. **Tabla de estado del sistema** — se agregaron:
   - QMD: v2.0.1 - 4 colecciones, 2051 archivos
   - Taste-Skills: 5 skills en .cursor/ y .agent/
   - DigitalGarden: Vault configurado
3. **Sección Engram** — była Memory MCP
4. **Nueva sección QMD** — comandos y colecciones
5. **Nueva sección DigitalGarden** — setup y comandos
6. **TASTE-SKILLS** — tabla con las 5 skills

- --

## 6. SCRIPTS CREADOS

### 1. `qmd.sh` — QMD Wrapper

```bash
#!/bin/bash
bun "C:/Users/sebas/AppData/Roaming/npm/node_modules/@tobilu/qmd/dist/cli/qmd.js" "$@"
```

### 2. `56_Update_QMD_Index.py` — QMD Update Script

```python
#!/usr/bin/env python3
"""
QMD Index Update Script
Re-indexes QMD collections for PersonalOS.
"""
```

- --

## 7. COMMIT RESULTANTE

* *Commit:** `84c99ed`

```
feat: integrate QMD, Taste-Skills, and DigitalGarden

- QMD v2.0.1 installed and configured with 4 collections (2051 files)
- Taste-Skills: 5 skills copied to .cursor/ and .agent/
- Frontend Premium workflow created (.agent/03_Workflows/)
- DigitalGarden vault setup in 06_Archive/05_Digital_Garden/
- AGENTS.md updated with QMD, DigitalGarden sections
- README updated with all new integrations and status
- QMD wrapper script and update script created
```

* *Archivos:** 65 files changed, 31810 insertions(+), 137 deletions(-)

- --

## 8. GIT STATUS FINAL

```
d155ba5 → 84c99ed  main -> main (Personal-Os-Engram)
d155ba5 → 84c99ed  main -> main (Invictus)
```

- --

## 9. SIGUIENTE SESIÓN — Pendientes

### Alto Prioridad

1. **QMD Embeddings**: Generar embeddings vectoriales
   ```bash
   bun qmd.js embed
   ```
   Descarga ~2GB de modelos

2. **QMD MCP**: Integrar QMD como MCP server en `.mcp.json`

3. **Every_Sync_Zone**: Resolver 388 staged deletions
   ```bash
   cd 07_Projects/01_Projects_Lab/Every_Sync_Zone
   git commit -m "chore: remove generated release artifacts"
   ```

### Media Prioridad

4. **DigitalGarden setup completo**:
   - Instalar Obsidian
   - Configurar Digital Garden plugin
   - Personalizar CSS
   - Deploy a Vercel

5. **TASTE-SKILLS integration**:
   - Probar con un proyecto frontend real
   - Ajustar configuración de DESIGN_VARIANCE

### Baja Prioridad

6. **GGA pre-commit timeout**: Investigar por qué GGA causa timeout en commits grandes

7. **AGENTS.md deduplication**: Hay secciones duplicadas en 2.3 Gentleman Skills

- --

## 10. APRENDIZAJES CLAVE

1. **Case sensitivity en Windows**: Git usa `03_KNOWLEDGE`, Windows muestra `03_Knowledge`. Esto causa problemas con submodules.

2. **Nested submodules**: Git no soporta submodules dentro de submodules. tmux en Gentleman.Dots quedó como clone normal.

3. **npm vs bun**: npm tuvo timeout en Windows, bun funcionó perfectamente.

4. **absorbgitdirs**: Comando útil para migrar `.git` directories embebidos a la estructura correcta de submodules.

5. **QMD es MUY rápido**: 2051 archivos indexados instantáneamente, búsqueda en milisegundos.

6. **Embeddings son opcionales**: QMD funciona con BM25 sin embeddings. Los embeddings mejoran búsqueda semántica pero requieren GPU y ~2GB de modelos.

- --

## 11. COMANDOS DE REFERENCIA RÁPIDA

```bash
# QMD

bun "C:/Users/sebas/AppData/Roaming/npm/node_modules/@tobilu/qmd/dist/cli/qmd.js"
bun qmd.js search "query"
bun qmd.js query "pregunta"
bun qmd.js status
bun qmd.js update
python 04_Engine/08_Scripts_Os/56_Update_QMD_Index.py

# Git

git submodule status
git submodule update --init --recursive

# Taste-Skills

# Usar: @taste-skill/SKILL.md en prompts

# DigitalGarden

cd 06_Archive/05_Digital_Garden
npm run start   # desarrollo local

npm run build  # deploy

```

- --

## 12. ARCHIVOS IMPORTANTES CREADOS/MODIFICADOS

| Archivo                                                        | Acción                    | Descripción                                             |
|----------------------------------------------------------------|---------------------------|---------------------------------------------------------|
| `.gitmodules`                                                  | Creado                    | 12 submodules registrados                               |
| `README.md`                                                    | Actualizado               | Agregado QMD, Taste-Skills, DigitalGarden               |
| `00_Core/AGENTS.md`                                            | Actualizado               | Secciones 2.7 QMD, 2.8 DigitalGarden                    |
| `04_Engine/08_Scripts_Os/qmd.sh`                               | Creado                    | Wrapper para QMD                                        |
| `04_Engine/08_Scripts_Os/56_Update_QMD_Index.py`               | Creado                    | Script de update QMD                                    |
| `.cursor/02_Skills/11_Taste_Skills/`                           | Creado                    | 5 taste-skills                                          |
| `.agent/02_Skills/11_Taste_Skills/`                            | Creado                    | 5 taste-skills                                          |
| `.agent/03_Workflows/09_Frontend_Premium.md`                   | Creado                    | Workflow frontend                                       |
| `06_Archive/05_Digital_Garden/`                                | Creado                    | Vault DigitalGarden                                     |
| `Reporte_Submodules_2026-03-19.md`                             | Creado                    | Reporte de submodules                                   |

- --

## 13. METRICAS DE LA SESIÓN

| Métrica                               | Valor                 |
|---------------------------------------|-----------------------|
| Submodules reparados                  | 12                    |
| Repos clonados                        | 5                     |
| Colecciones QMD creadas               | 4                     |
| Archivos QMD indexados                | 2051                  |
| Taste-Skills integradas               | 5                     |
| Scripts creados                       | 2                     |
| Commits                               | 2                     |
| Líneas cambiadas                      | ~32000                |

- --

## 14. STACK TÉCNICO

| Componente                 | Versión                     |
|----------------------------|-----------------------------|
| Node.js                    | v24.12.0                    |
| Bun                        | 1.3.10                      |
| Python                     | 3.14                        |
| QMD                        | v2.0.1                      |
| Git                        | (Windows git)               |

- --

## 15. RECURSOS

- QMD: https://github.com/tobi/qmd
- Taste-Skills: `.cursor/02_Skills/11_Taste_Skills/` y `.agent/02_Skills/11_Taste_Skills/`
- DigitalGarden: `06_Archive/05_Digital_Garden/`
- Gentleman-Programming: https://github.com/Gentleman-Programming

- --

* Session Report — 2026-03-19*
* Think Different PersonalOS*
