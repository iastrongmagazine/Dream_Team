# docker

> **Categoría:** Development (Tier 3)
> **Uso:** Container management

## Descripción

Integración con Docker para gestión de contenedores.

## Uso Principal

```bash
# Listar contenedores
docker ps

# Ejecutar comando
docker run --rm -i image_name
```

## Configuración

```json
"docker": {
  "command": "docker",
  "args": ["run", "--rm", "-i", "--mount", "type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock", "mcp/docker:latest"]
}
```

## Casos de Uso

- 🐳 Gestión de contenedores
- 🔧 Desarrollo en containers
- 📦 Despliegue

---

*Tier 3 - Development*
