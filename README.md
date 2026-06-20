# Nexus v2

Canonical integration surface for the AnarchI deterministic systems stack.

Hardcoding freedom into the systems of tomorrow.

## Purpose

Nexus v2 is the cleaned successor to the earlier Nexus design-kit experiments. It connects incoming events, deterministic rules, execution adapters, audit trails, and AI escalation boundaries into one coherent operating layer.

## What Is Fixed

- Replaced a broken public pipeline entrypoint that referenced missing modules.
- Added a dependency-free deterministic orchestration core.
- Added tests for execute, hold, review, and AI-escalation decisions.
- Clarified that `Nexusv2` is the canonical Nexus path while `Nexus` remains legacy research.

## Structure

```text
.
├── nexus_orchestration_core.py   # Tested public pipeline spine
├── Distributed_Bus/              # Event transport experiments
├── Event_Queue/                  # Async queue primitive
├── Execution_Adapters/           # External action adapters
├── Schema_Registry/              # Schema direction
├── Worker_Nodes/                 # Worker node experiments
└── tests/                        # Verification suite
```

## Verify

```bash
python -m unittest discover -s tests -q
```

## Operating Rule

Deterministic checks route every event first. AI is used only when confidence is too low after the deterministic gates have done their work.

## Public Safety

This repo is safe for public presentation. It does not include private credentials, live runtime state, wallet material, customer data, or unreleased CERBERUS decision chains.
