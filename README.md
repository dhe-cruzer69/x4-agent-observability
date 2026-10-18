# x4-agent-observability

[![CI](https://github.com/dhe-cruzer69/x4-agent-observability/actions/workflows/ci.yml/badge.svg)](https://github.com/dhe-cruzer69/x4-agent-observability/actions)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)

**Local-first agent telemetry with evidence receipts.**

Vendor-neutral event model. Console and JSONL exporters first; OpenTelemetry-compatible when enabled.

## Quick start

```bash
pip install -e ".[dev]"
python -c "from x4_obs import trace; 
with trace.agent('demo'):
    with trace.tool('ping'):
        pass"
```

<!-- X4-APEX-DIAGRAM-START:x4-agent-observability -->

```mermaid
flowchart LR
    AGENT[Agent or Tool Span] --> EVENT[Structured Event]
    EVENT --> REDACT[Secret and Sensitive-Field Redaction]
    REDACT --> SAFE[Sanitized Event]
    SAFE --> CONSOLE[Console Exporter]
    SAFE --> JSONL[JSONL Exporter]
    SAFE --> OTEL[Optional OpenTelemetry-Compatible Export]
    SAFE --> RECEIPT[Hashed Action Receipt]
    RECEIPT --> AUDIT[Evidence Consumer]
    TEST[Redaction and Serialization Tests] --> REDACT
```

<!-- X4-APEX-DIAGRAM-END:x4-agent-observability -->

## Receipts

Every sensitive action can emit a hashed receipt (before/after, actor, approval).

## License

Apache-2.0

## APEX Architecture Map

> Status: architecture documentation; implementation and deployment claims require independent verification.

```mermaid
flowchart LR
  Producer[Agent or runtime] --> Envelope[Event envelope]
  Envelope --> Validate[Validate event schema]
  Validate --> Redactor[Secret and PII redaction]
  Redactor --> LeakTest{Redaction checks pass?}
  LeakTest -->|no| Quarantine[Drop or quarantine event]
  LeakTest -->|yes| Correlate[Attach trace / run / sequence IDs]
  Correlate --> Buffer[Bounded exporter buffer]
  Buffer --> Export[Configured exporter]
  Export --> Store[(Telemetry backend)]
  Store --> Query[Trace and event query]
  Query --> Dashboard[Operational dashboard]
  Quarantine --> Counter[Redaction failure metric]
```

**Evidence note:** Redaction guarantees, exporter retries, buffer limits, and backend integrations need implementation-level verification. Never send raw secrets to telemetry.

