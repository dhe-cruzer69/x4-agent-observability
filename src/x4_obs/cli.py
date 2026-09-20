"""CLI for observability."""
from __future__ import annotations

import argparse

from .trace import trace


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="x4-obs")
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args(argv)
    if args.demo:
        with trace.agent("demo-agent"):
            with trace.tool("ping"):
                pass
            with trace.llm("local-model"):
                pass
        print(trace.export_jsonl())
    else:
        print("x4-obs — use --demo or import x4_obs.trace")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
