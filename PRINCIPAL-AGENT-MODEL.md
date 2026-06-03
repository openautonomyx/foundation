# OpenAutonomyX Principal–Agent Model

The OpenAutonomyX principal–agent model grounds agent governance in the classic principal–agent problem from economics.

## Purpose

Autonomous agents are a literal instance of the principal–agent problem: a **principal** (a human or organization) delegates work to an **agent** that acts on the principal's behalf, but whose actions the principal cannot fully observe or perfectly control.

Understanding agent governance as a principal–agent problem tells us exactly what can go wrong and which controls address it.

## The Core Problem

- **Delegation** — the principal grants the agent authority to act.
- **Information asymmetry** — the agent knows more about its own actions, reasoning, and state than the principal can observe.
- **Goal divergence** — the agent's effective objective may drift from the principal's true intent (misspecified goals, reward hacking, prompt/tool influence).
- **Moral hazard** — the agent may take hidden actions the principal would not approve.
- **Adverse selection** — the principal may not know the true capability or trustworthiness of an agent before engaging it.
- **Monitoring cost** — observing the agent enough to trust it has a price.

## Classic Mitigations, Mapped to the Foundation

| Principal–agent mitigation | Foundation mechanism |
|---|---|
| Verify the agent before engaging | identity (SPIFFE), trust assertions, evaluation |
| Reduce information asymmetry | traceability, evidence, OpenTelemetry observability |
| Align incentives and constrain behavior | constitution, policy-as-code (OPA), constraints |
| Limit delegated authority | least-privilege scopes, OpenFGA, delegation protocol |
| Approve consequential actions | human approval, AuthZEN PDP/PEP |
| Prevent unilateral control | separation of duty |
| Detect hidden divergence | drift detection, evaluation, audit |
| Retain ability to intervene | kill switch, suspension, revocation |

## Contracts and Accountability

As in the employment-contract framing of the principal–agent problem, the relationship is governed by an explicit, monitored, enforceable contract: the agent's registered definition, delegation, policy bindings, approvals, and evidence obligations.

The agent constitution sets the non-negotiable terms; evaluation and audit verify performance; trust adjusts based on evidence.

## Multi-Agent Layers

Orchestrators introduce nested principal–agent relationships (an agent delegating to sub-agents). Each layer re-applies the same mitigations: scoped delegation, per-step authorization, and aggregated evidence.

## Principle

Agent governance is principal–agent alignment made operational. Every control exists to close the gap between what the principal intends and what the agent actually does.
