# MCP Tools

## Server
- Name: `@open-pencil/mcp`
- Install: `npm install -g @open-pencil/mcp`

## Tools

### generate_screen
Creates complete screens from prompts.

```json
{
  "tool": "generate_screen",
  "params": {
    "prompt": "A modern dashboard with sidebar navigation",
    "style": "premium",
    "output": "dashboard.pen"
  }
}
```

### modify_component
Adjusts styles and properties of existing components.

```json
{
  "tool": "modify_component",
  "params": {
    "component": "button-primary",
    "changes": {
      "color": "#3B82F6",
      "borderRadius": "8px"
    }
  }
}
```

### export_to_code
Generates code snippets from designs.

```json
{
  "tool": "export_to_code",
  "params": {
    "design": "dashboard.pen",
    "framework": "react-tailwind"
  }
}
```

## Output Formats
- `.pen`: Pencil source file
- `.tsx`: React component
- `.css`: Pure CSS
- `.svg`: Vector export
