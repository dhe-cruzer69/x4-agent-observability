from x4_obs.trace import TraceAPI
from x4_obs.receipt import make_receipt


def test_trace_events():
    t = TraceAPI()
    with t.agent("a"):
        with t.tool("t"):
            pass
    assert len(t.events) == 2
    assert t.events[0].event == "tool.call"
    assert t.events[1].event == "agent"


def test_receipt():
    r = make_receipt("filesystem.write", "README.md", approved=True, actor="human", before=b"a", after=b"b")
    assert r.sha256_before != r.sha256_after
    assert r.approved is True
