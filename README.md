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

## Receipts

Every sensitive action can emit a hashed receipt (before/after, actor, approval).

## License

Apache-2.0
