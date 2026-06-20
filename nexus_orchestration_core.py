from __future__ import annotations

from dataclasses import dataclass, field
from time import time
from typing import Any


@dataclass(frozen=True)
class NexusEvent:
    tenant_id: str
    event_type: str
    payload: dict[str, Any]
    confidence: float = 1.0
    risk: float = 0.0


@dataclass(frozen=True)
class NexusDecision:
    action: str
    reason: str
    requires_ai: bool = False
    audit_record: dict[str, Any] = field(default_factory=dict)


def run_pipeline(event: NexusEvent) -> NexusDecision:
    """Normalize an event and route it through deterministic gates."""
    normalized = _normalize(event)
    decision = _route(normalized)
    return NexusDecision(
        action=decision["action"],
        reason=decision["reason"],
        requires_ai=decision["requires_ai"],
        audit_record={
            "tenant_id": normalized["tenant_id"],
            "event_type": normalized["event_type"],
            "action": decision["action"],
            "reason": decision["reason"],
            "timestamp": normalized["timestamp"],
        },
    )


def _normalize(event: NexusEvent) -> dict[str, Any]:
    if not event.tenant_id.strip():
        raise ValueError("tenant_id is required")
    if not event.event_type.strip():
        raise ValueError("event_type is required")

    return {
        "tenant_id": event.tenant_id.strip(),
        "event_type": event.event_type.strip().upper(),
        "payload": dict(event.payload),
        "confidence": event.confidence,
        "risk": event.risk,
        "timestamp": int(time()),
    }


def _route(event: dict[str, Any]) -> dict[str, Any]:
    confidence = event["confidence"]
    risk = event["risk"]

    if not 0 <= confidence <= 1:
        return _decision("reject", "confidence must be between 0 and 1")
    if not 0 <= risk <= 1:
        return _decision("reject", "risk must be between 0 and 1")
    if risk >= 0.8:
        return _decision("hold", "risk gate blocked automatic execution")
    if event["event_type"] in {"PAYMENT", "TRANSFER", "DEPLOY"} and risk >= 0.45:
        return _decision("review", "write-capable event requires operator review")
    if confidence >= 0.75 and risk <= 0.35:
        return _decision("execute", "deterministic gates cleared")
    if confidence < 0.45:
        return _decision("escalate", "ambiguity remains after deterministic checks", True)
    return _decision("review", "valid event needs operator review")


def _decision(action: str, reason: str, requires_ai: bool = False) -> dict[str, Any]:
    return {"action": action, "reason": reason, "requires_ai": requires_ai}


if __name__ == "__main__":
    sample = NexusEvent("tenant_anarchi_demo", "MESSAGE", {"message": "hello"}, 0.9, 0.1)
    print(run_pipeline(sample))
