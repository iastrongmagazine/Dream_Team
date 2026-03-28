# github

> **Categoría:** Core (Tier 1)
> **Uso:** Gestión de repositorios y PRs

## Descripción

Integración con GitHub para management de repos, issues y pull requests.

## Uso Principal

```bash
# Crear issue
gh issue create --title "Bug in auth"

# Listar PRs
gh pr list

# Crear PR
gh pr create --title "feat: new feature"
```

## Configuración

```json
"github": {
  "transport": "streamableHttp",
  "url": "https://api.githubcopilot.com/mcp/",
  "headers": {
    "Authorization": "github_pat_..."
  }
}
```

## Casos de Uso

- 🐙 Gestión de Issues
- 🔀 Pull Requests
- 📊 Repo stats

---

*Tier 1 - Siempre activa*
