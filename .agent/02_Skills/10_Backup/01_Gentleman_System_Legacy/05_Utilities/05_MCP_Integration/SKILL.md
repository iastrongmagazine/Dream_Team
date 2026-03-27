# 05 MCP Integration

## Trigger
Cuando el usuario menciona: "MCP", "Model Context Protocol", "MCP server", "herramientas MCP", "configurar MCP", "diagnosticar MCP"

## Overview
Skill para gestión completa del ecosistema MCP (Model Context Protocol): discovery, validación, diagnóstico y troubleshooting de servidores MCP.

## SOTA MCP Architecture (2025-2026)

### Server Types

| Type | Transport | Ejemplo |
|------|-----------|---------|
| **stdio** | Standard I/O | filesystem, notion, exa |
| **streamableHttp** | HTTP Streaming | context7, github, supabase |
| **sse** | Server-Sent Events | legacy servers |

### Transport Patterns

#### stdio (Local)
```json
{
  "transport": "stdio",
  "command": "npx.cmd",
  "args": ["-y", "@package/mcp-server"]
}
```

#### streamableHttp (Remote)
```json
{
  "transport": "streamableHttp",
  "url": "https://api.example.com/mcp",
  "headers": {
    "Authorization": "Bearer TOKEN"
  }
}
```

## Workflow

### Step 1: Discovery
Listar todos los servidores MCP configurados:
```bash
# Ver configuración actual
cat .mcp.json

# Listar servers activos
jq '.mcpServers | keys' .mcp.json
```

### Step 2: Validation
Validar estructura de `.mcp.json`:
```bash
# Syntax check
jq . .mcp.json > /dev/null && echo "JSON válido"

# Verificar servers requeridos
jq '.mcpServers | length' .mcp.json
```

### Step 3: Health Check
Verificar conectividad de servers remotos:
```bash
# Test streamableHttp servers
curl -s -o /dev/null -w "%{http_code}" https://mcp.context7.com/mcp

# Test stdio servers
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | npx -y @package/mcp-server
```

### Step 4: Troubleshooting

#### Server no responde
1. Verificar que el command exista
2. Verificar permisos de ejecución
3. Revisar logs de error
4. Reiniciar el server

#### Connection timeout
1. Verificar URL y headers
2. Revisar API keys
3. Probar conectividad manual

#### Schema mismatch
1. Verificar versión del server
2. Reinstalar con `--force`

## MCP Servers en PersonalOS

### Core Servers (Siempre activos)
| Server | Transport | Propósito |
|--------|-----------|-----------|
| **engram** | stdio | Memoria persistente |
| **context7** | streamableHttp | Docs de frameworks |
| **exa** | stdio | Búsqueda web |
| **github** | streamableHttp | GitHub API |

### Integration Servers
| Server | Transport | Propósito |
|--------|-----------|-----------|
| **Notion** | stdio | Base de datos |
| **supabase** | streamableHttp | Database |
| **Playwright** | stdio | Browser automation |
| **Linear** | streamableHttp | Issue tracking |

### Development Servers
| Server | Transport | Propósito |
|--------|-----------|-----------|
| **filesystem** | stdio | File operations |
| **postgres** | stdio | PostgreSQL client |
| **sqlite** | stdio | SQLite client |
| **docker** | stdio | Container management |

## Edge Cases

### Error: Server not found
```bash
# Verificar que el package exista
npm view @package/mcp-server

# Reinstalar
npm install -g @package/mcp-server
```

### Error: Permission denied
```bash
# En Windows: verificar Execution Policy
Get-ExecutionPolicy
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Error: Connection refused
```bash
# Verificar que el servicio esté corriendo
curl http://localhost:PORT/health

# Revisar firewall
netsh advfirewall firewall show rule name="MCP Server"
```

### Error: Invalid JSON in .mcp.json
```bash
# Validar JSON
jq . .mcp.json

# Si hay error, formatear
jq '.' .mcp.json > .mcp.json.tmp && mv .mcp.json.tmp .mcp.json
```

### Error: API key expired
```bash
# Revisar fecha de expiración
# Actualizar en .mcp.json
# O usar variables de entorno
```

## RTM (Requirements Traceability Matrix)

| Req ID | Requirement | Validation | Priority |
|--------|-------------|------------|----------|
| MCP-01 | `.mcp.json` válido | `jq . .mcp.json` | P0 |
| MCP-02 | Servers stdio ejecutables | Test manual | P0 |
| MCP-03 | Servers HTTP respondiendo | `curl` health check | P1 |
| MCP-04 | API keys configuradas | Review `.env` | P1 |
| MCP-05 | Logs de errores | Revisión periódica | P2 |

## Evals

### Unit Tests
```python
# test_mcp_config.py
def test_json_valid():
    """Validar JSON syntax"""
    assert valid_json('.mcp.json')

def test_server_count():
    """Verificar mínimo de servers"""
    servers = load_servers('.mcp.json')
    assert len(servers) >= 5

def test_required_servers():
    """Verificar servers core presentes"""
    servers = load_servers('.mcp.json')
    assert 'engram' in servers
    assert 'context7' in servers
```

### Integration Tests
```python
def test_server_connection():
    """Test conexión a server remoto"""
    for server in get_http_servers('.mcp.json'):
        assert ping(server['url']), f"{server} no responde"
```

## Resources
- [MCP Spec](https://modelcontextprotocol.io)
- [MCP Servers](https://github.com/modelcontextprotocol/servers)
- [Context7](https://context7.com)
