# 🌟 05_GGA — Gentleman Guardian Angel

**Provider-agnostic code review usando IA.**

---

## 📋 Qué es

GGA es una herramienta de **Code Review con IA** que:
- Lee tu `AGENTS.md` y valida el código contra tus reglas
- Corre como **pre-commit hook** — revisa antes de cada commit
- Es **provider agnostic** — usa Claude, Gemini, Codex, Ollama, etc.
- Es **pure Bash** — cero dependencias externas

---

## 🏗️ Ubicación en el Sistema

```
.agent/
├── 01_Agents/
├── 02_Skills/
├── 03_Workflows/
├── 04_Extensions/    ← Hooks activos del sistema
└── 05_GGA/         ← Code Review Tool (este)
```

---

## 🚀 Quick Start

### 1. Navegar a tu proyecto

```bash
cd /tu/proyecto
```

### 2. Inicializar config

```bash
.agent/05_GGA/install.sh
```

### 3. Inicializar GGA en el proyecto

```bash
gga init
```

### 4. Instalar git hook

```bash
gga install
```

### 5. Listo! El hook corre en cada commit

---

## 📦 Comandos

| Comando     | Descripción              |
| ----------- | ------------------------ |
| `gga run`   | Revisar archivos staged  |
| `gga install` | Instalar pre-commit hook |
| `gga config` | Ver/editar configuración |
| `gga --help` | Mostrar ayuda            |

---

## 🔗 Integración con Think Different AI

| Componente              | Relación                              |
| ----------------------- | ------------------------------------- |
| `AGENTS.md`             | Lee las reglas de编码标准 desde aquí      |
| `04_Extensions/`        | GGA complementa los hooks del sistema |
| `05_Gentleman/03_Review/` | Skills relacionadas con revisión      |

---

## 📁 Estructura

```
05_GGA/
├── bin/
│   └── gga              # Binary principal
├── lib/
│   ├── providers.sh     # Providers de IA
│   ├── cache.sh         # Smart caching
│   └── pr_mode.sh      # PR review mode
├── spec/               # Tests (ShellSpec)
├── install.sh          # Installer
├── uninstall.sh        # Uninstaller
├── README.md           # Este archivo
└── README.md (original)# Documentación completa
```

---

## 🔧 Configuración

Archivo: `.gga` en tu proyecto

```bash
# Provider (claude, gemini, openai, etc.)
PROVIDER="claude"

# Archivos a revisar
FILE_PATTERNS="*.py *.js *.ts"

# Archivos a excluir
EXCLUDE_PATTERNS="*.test.js __pycache__"

# Archivo de reglas
RULES_FILE="AGENTS.md"

# Modo estricto (fail en respuestas ambiguas)
STRICT_MODE=false
```

---

## 📚 Recursos

- **GitHub**: [Gentleman-Programming/gentleman-guardian-angel](https://github.com/Gentleman-Programming/gentleman-guardian-angel)
- **Version**: 2.7.0
- **Tests**: 174 passing

---

## 🧹 Desinstalar

```bash
.agent/05_GGA/uninstall.sh
```

---

**Last Updated**: 2026-03-18  
**Version**: 2.7.0  
**Maintainer**: Think Different AI System
