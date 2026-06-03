# OpenAutonomyX Agent Patterns

Reusable, governed patterns for building agents. Each pattern names the problem it solves and the governance it must carry.

## Reasoning & Execution

- **Reflection** — the agent critiques and revises its own output before acting. Carry confidence; escalate when low.
- **Planning / decomposition** — break an objective into sub-tasks with explicit acceptance criteria.
- **Tool use** — invoke external functions via MCP; each call is authorized and least-privilege (see tool model).
- **ReAct (reason + act)** — interleave reasoning and tool calls; every action emits evidence.
- **RAG (retrieval-augmented generation)** — ground answers in retrieved, provenance-tracked knowledge; unverified content stays a claim.

## Coordination

- **Operator / reconciliation** — drive observed state toward declared desired state idempotently (see reconciliation protocol).
- **Orchestrator–worker** — a coordinator delegates scoped, revocable work to sub-agents and reconciles results.
- **Nested teams** — form small sparse subgroups to reduce communication overhead (Internet of Agents).
- **Handoff / escalation** — pass control to a human or higher-trust party when thresholds aren't met.

## Governance

- **Human-in-the-loop** — require approval before consequential actions.
- **Propose–approve–execute** — separate who proposes, approves, and executes (separation of duty).
- **Policy-as-code gate** — every action checked against policy (OPA) and relationships (OpenFGA) before execution.
- **Kill switch & rollback** — always retain the ability to halt and undo.

## Pattern Principle

A pattern is reusable structure plus the governance that makes it safe. Reuse the structure without reusing the risk.
