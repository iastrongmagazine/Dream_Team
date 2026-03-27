---
name: observability-skill
description: >
  Comprehensive observability patterns for AI agents. Includes metrics, logging, tracing, and alerting.
  Trigger: monitoring, observability, metrics, logging, tracing, APM, SRE, alerts, dashboards, Prometheus, Grafana.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

# Observability Skill — SOTA Patterns

## When to Use

- Implementing logging infrastructure
- Setting up metrics collection
- Configuring distributed tracing
- Designing alerting systems
- Debugging production issues with observability data

## Critical Patterns

### 1. The Three Pillars

```
┌─────────────────────────────────────────────────────────────────┐
│                    THE THREE PILLARS                            │
├─────────────────┬─────────────────┬─────────────────────────────┤
│    METRICS      │     LOGS        │          TRACES            │
│  "What happened?"│  "Why happened?"│    "How did it happen?"    │
├─────────────────┼─────────────────┼─────────────────────────────┤
│  • Counters     │  • Structured   │  • Distributed tracing      │
│  • Gauges       │  • JSON format  │  • Span hierarchy          │
│  • Histograms   │  • Correlation  │  • Trace context           │
│  • Aggregation  │    IDs          │  • Latency analysis        │
└─────────────────┴─────────────────┴─────────────────────────────┘
```

### 2. RED Method (Request Metrics)

| Metric | Question | Implementation |
|--------|----------|----------------|
| **Rate** | How many requests/second? | `requests_total / second` |
| **Errors** | How many failures? | `errors_total / requests_total` |
| **Duration** | How slow are they? | `p50, p95, p99 latency` |

### 3. USE Method (Resource Metrics)

| Metric | Question | Implementation |
|--------|----------|----------------|
| **Utilization** | Is resource busy? | CPU %, Memory % |
| **Saturation** | Is resource queued? | Queue depth, Load |
| **Errors** | Are there failures? | Error rate |

## Code Examples

### Python Structured Logging (SOTA)

```python
import structlog
from opentelemetry import trace

# Structured logging with correlation
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer()
    ]
)

# With OpenTelemetry trace context
def log_with_trace(logger, event, **kwargs):
    span = trace.get_current_span()
    ctx = span.get_span_context()
    return logger.info(
        event,
        trace_id=format(ctx.trace_id, '032x'),
        span_id=format(ctx.span_id, '016x'),
        **kwargs
    )
```

### Prometheus Metrics (SOTA)

```python
from prometheus_client import Counter, Histogram, Gauge

# Define metrics
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'endpoint'],
    buckets=[0.01, 0.05, 0.1, 0.5, 1.0, 5.0]
)

ACTIVE_REQUESTS = Gauge(
    'http_requests_active',
    'Active HTTP requests',
    ['endpoint']
)

# Usage
with REQUEST_LATENCY.labels(method='GET', endpoint='/api').time():
    process_request()
```

### OpenTelemetry Distributed Tracing (SOTA)

```python
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Configure tracing
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

# Instrument code
tracer = trace.get_tracer(__name__)

@tracer.start_as_current_span("process_order")
def process_order(order_id: str):
    current_span = trace.get_current_span()
    current_span.set_attribute("order.id", order_id)
    
    with tracer.start_as_current_span("validate_order") as span:
        span.set_attribute("order.status", "validating")
        # validation logic
        pass
    
    with tracer.start_as_current_span("process_payment") as span:
        span.set_attribute("payment.method", "stripe")
        # payment logic
        pass
```

## Commands

```bash
# Prometheus + Grafana stack
docker run -d --name prometheus -p 9090:9090 prom/prometheus
docker run -d --name grafana -p 3000:3000 grafana/grafana

# OpenTelemetry collector
otelcol --config=otel-collector-config.yaml

# Export traces to Jaeger
docker run -d --name jaeger -p 16686:16686 -p 6831:6831/udp jaegertracing/all-in-one

# Check metrics endpoint
curl localhost:9090/metrics

# Prometheus queries
rate(http_requests_total[5m])
histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))
```

## Resources

- **Prometheus**: https://prometheus.io/docs/concepts/metric_types/
- **OpenTelemetry**: https://opentelemetry.io/docs/
- **Grafana Dashboards**: https://grafana.com/docs/grafana/latest/dashboards/
- **Structured Logging**: https://www.structlog.org/en/stable/
