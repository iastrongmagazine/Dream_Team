# 🤖 Integración de OpenCode en el Ecosistema Think Different

## 📋 Resumen

OpenCode está completamente integrado en el ecosistema Think Different AI, con acceso a todos los MCPs, agentes y herramientas disponibles en el sistema.

## 🎯 Configuración Actual

### Ubicación de Configuración
- **Principal**: `03_Knowledge/Resources/Gentleman.Dots/GentlemanOpenCode/opencode.json`
- **Sistema**: `.mcp.json` (fuente de verdad para MCPs)

### MCPs Disponibles (22 servidores)

| Servidor                         | Tipo                   | Funcionalidad                                    |
|----------------------------------|------------------------|--------------------------------------------------|
| Engram                           | Local                  | Memoria persistente del sistema                  |
| Agent Teams Lite                 | Local                  | Framework SDD para proyectos                     |
| GGA                              | Local                  | Guardian Angel - Code Review                     |
| Playwright                       | Local                  | Navegación y testing UI                          |
| Fireflies                        | Local                  | Transcripción de reuniones                       |
| Notion                           | Remoto                 | Base de datos y notas                            |
| Exa                              | Local                  | Búsqueda web en tiempo real                      |
| Filesystem                       | Local                  | Gestión de archivos                              |
| Context7                         | Remoto                 | Contexto enriquecido para código                 |
| GitHub                           | Remoto                 | Integración con GitHub API                       |
| y más...                         |                        |                                                  |

## ⚙️ Agentes Configurados

### 1. Gentleman (Principal)
- **Modo**: Primary
- **Descripción**: Senior Architect mentor
- **Personalidad**: Ayuda primero, desafía cuando importa

### 2. Dangerous-Gentleman
- **Modo**: All (sin restricciones)
- **Permisos**: Bash, Read, Write, Edit, Task, etc.
- **Uso**: Tareas que requieren máximo acceso

### 3. SDD-Orchestrator
- **Modo**: All
- **Descripción**: Orquestador de Spec-Driven Development
- **Función**: Delega tareas a sub-agentes especializados

## 🔌 Uso de MCPs en OpenCode

### Comandos Disponibles
- `/mcp-list` - Listar todos los MCPs disponibles
- `/mcp-connect <nombre>` - Conectar a un MCP específico
- `/mcp-disconnect <nombre>` - Desconectar de un MCP

### Ejemplos de Uso

#### 1. Búsqueda con Exa
```
Usa Exa para buscar información sobre [tema]
```

#### 2. Navegación con Playwright
```
Navega a [URL] y captura una screenshot
```

#### 3. Memoria con Engram
```
Guarda este contexto en la memoria del sistema
```

#### 4. Documentación con Notion
```
Crea una página en Notion con [contenido]
```

## 🔄 Sincronización Automática

El script `41_Sync_MCP_OpenCode.py` mantiene sincronizados los MCPs entre:
- `.mcp.json` → Fuente de verdad del sistema
- `opencode.json` → Configuración de OpenCode

### Ejecutar Sincronización
```bash
python 04_Engine/41_Sync_MCP_OpenCode.py
```

### Proceso Automático
1. Crea backups de ambos archivos
2. Convierte formato de `.mcp.json` a `opencode.json`
3. Actualiza la configuración de OpenCode
4. Reporta el número de MCPs sincronizados

## 📚 Documentación Adicional

### Repositorios del Ecosistema
- **Engram**: `https://github.com/Gentleman-Programm...`
- **Agent Teams Lite**: `https://github.com/Gentleman-Programm...`
- **GGA**: `https://github.com/Gentleman-Programm...`
- **Gentleman Skills**: `https://github.com/Gentleman-Programm...`
- **Gentleman.Dots**: `https://github.com/Gentleman-Programm...`

### Scripts Relacionados
- `07_Morning_Standup.py` - Ritual de inicio de sesión
- `26_Multi_Agent_Final_Validation.py` - Validación multi-agente
- `37_Audit_Engineering.py` - Auditoría completa del sistema

## 🔧 Troubleshooting

### Problema: MCP no conecta
1. Verifica que el servidor esté corriendo
2. Revisa los logs de OpenCode
3. Ejecuta la sincronización manual

### Problema: Permisos denegados
1. Revisa la configuración de permisos en `opencode.json`
2. Ajusta las reglas de `permission` si es necesario

### Problema: Caracteres especiales
1. El script de sincronización usa codificación UTF-8
2. Si hay errores, revisa la codificación de los archivos

## 📊 Métricas

- **Total MCPs**: 22 servidores
- **Agentes**: 3 configurados
- **Sincronización**: Automática vía script Python
- **Backup**: Automático con timestamp

## 🎯 Próximos Pasos

1. ✅ Configuración básica completada
2. ✅ Sincronización automática implementada
3. ⏳ Documentación de uso avanzado
4. ⏳ Integración con workflows de SDD
5. ⏳ Monitorización de rendimiento

---

**Última actualización**: 2026-03-10
**Mantenido por**: PersonalOS Engine
