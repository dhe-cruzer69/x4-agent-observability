"""Minimal agent/tool/llm span context managers."""
from __future__ import annotations

import json
import time
import uuid
from contextlib import contextmanager
from dataclasses import dataclass, field, asdict
from typing import Any, Iterator


@dataclass
class Event:
    trace_id: str
    event: str
    name: str
    status: str = "success"
    latency_ms: int = 0
    attributes: dict[str, Any] = field(default_factory=dict)


class TraceAPI:
    def __init__(self) -> None:
        self.events: list[Event] = []
        self._trace_id = uuid.uuid4().hex

    @contextmanager
    def agent(self, name: str) -> Iterator[None]:
        t0 = time.perf_counter()
        try:
            yield
            status = "success"
        except Exception:
            status = "error"
            raise
        finally:
            ms = int((time.perf_counter() - t0) * 1000)
            self.events.append(Event(self._trace_id, "agent", name, status, ms))

    @contextmanager
    def tool(self, name: str) -> Iterator[None]:
        t0 = time.perf_counter()
        try:
            yield
            status = "success"
        except Exception:
            status = "error"
            raise
        finally:
            ms = int((time.perf_counter() - t0) * 1000)
            self.events.append(Event(self._trace_id, "tool.call", name, status, ms))

    @contextmanager
    def llm(self, name: str) -> Iterator[None]:
        t0 = time.perf_counter()
        try:
            yield
            status = "success"
        except Exception:
            status = "error"
            raise
        finally:
            ms = int((time.perf_counter() - t0) * 1000)
            self.events.append(Event(self._trace_id, "llm.request", name, status, ms))

    def export_jsonl(self) -> str:
        return "\n".join(json.dumps(asdict(e)) for e in self.events) + ("\n" if self.events else "")


trace = TraceAPI()
