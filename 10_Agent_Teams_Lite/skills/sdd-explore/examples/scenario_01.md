# Scenario: Explorar Feature de Analytics

## Trigger

Usuario: "Quiero agregar analytics a mi dashboard de React. Cómo lo harías?"

## Proceso

```
1. Entender intención → Dashboard con métricas de usuario
2. Investigar codebase → Revisar estructura actual, dependencias
3. Identificar constraints → 
   - No hay analytics instalado
   - Deadline: 1 semana
   - Presupuesto: limitado
4. Generar opciones:
   - Opción A: Google Analytics (free, easy)
   - Opción B: Mixpanel (paid, powerful)
   - Opción C: Custom solution (time-consuming)
```

## Output

```markdown
# Explore: Analytics Dashboard

## Intención del Usuario
- Dashboard con métricas de uso
- Tracking de eventos clave
- Visualización de datos

## Investigación
- Stack actual: React 19, Next.js 14
- Dependencias disponibles: Ninguna analytics
- Código relevante: None

## Opciones

| Opción | Pros | Contras | Tiempo |
|--------|------|---------|--------|
| GA4 | Free, easy | Limited custom | 2 días |
| Mixpanel | Powerful | Paid | 5 días |
| Custom | Total control | Mucho tiempo | 2 semanas |

## Recomendación
GA4 como MVP, evolucionar a Mixpanel si se necesita más.
```
