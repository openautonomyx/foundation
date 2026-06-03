# OpenAutonomyX Agent Protocol Model

The OpenAutonomyX agent protocol model defines how agents, humans, services, and systems interoperate through open, governed, observable protocols.

## Purpose

Agents must coordinate without inheriting trust implicitly, leaking authority, or escaping governance.

A protocol is the contract that makes interaction between two parties attributable, authorized, policy-bounded, and auditable — regardless of vendor, runtime, or model.

Protocols exist so that interoperability does not require shared ownership, and autonomy does not require blind trust.

## Why This Matters

Agent protocols must simultaneously serve three needs that often pull against each other:

- **Adoption** — agents only deliver value when teams can discover, integrate, and reuse them with low friction across vendors, runtimes, and models. Open, versioned protocols make adoption portable instead of locked in.
- **Governance** — autonomy at scale is only safe when every consequential exchange is identified, authorized, policy-bound, approved where required, and traceable. Governance must be native to the protocol, not bolted on after adoption.
- **Security** — agents expand the attack surface (identity spoofing, ambient authority, prompt and tool abuse, supply-chain compromise). Protocols must authenticate both parties, enforce least authority, fail closed, and produce evidence.

The foundation treats adoption, governance, and security as co-equal design constraints: a protocol that advances one at the expense of the others is not conformant.

## Protocol Principles

1. Open over proprietary.
2. Explicit over implicit.
3. Scoped over ambient authority.
4. Verifiable over assumed identity.
5. Governed over best-effort.
6. Observable over opaque.
7. Revocable over permanent.
8. Versioned over silently changed.

## Protocol Stack

```text
Governance      → policy, approval, trust, audit binding
Semantic        → intent, capability, knowledge, evidence meaning
Interaction     → request, response, delegation, escalation, negotiation
Identity        → authentication, attestation, authorization
Transport       → open, secure, portable message exchange
```

Each layer is independent: a party may be reachable (transport) yet unauthorized (identity), or authorized yet out of policy (governance).

## Core Protocols

Agent interoperability is composed of named protocols, each with a defined contract.

- **Identity handshake** — mutual authentication and attestation before any consequential exchange.
- **Capability discovery** — advertise and request purpose, skills, tools, data scopes, and autonomy level.
- **Intent and task** — express objective, inputs, constraints, expected output, and acceptance criteria.
- **Delegation** — pass scoped, revocable, expiring authority with explicit allowed actions.
- **Context exchange** — share governed context with provenance, classification, and consent state.
- **Approval** — request and record human authorization for consequential actions.
- **Escalation** — hand off to a human or higher-trust party when thresholds are not met.
- **Trust exchange** — present and verify trust assertions and their validity.
- **Evidence and audit** — emit attributable events sufficient to reconstruct what happened and why.
- **Negotiation** — agree terms, scope, cost, and constraints before commitment.
- **Termination and revocation** — end a session, revoke delegation, or trigger a kill switch.

## Message Envelope

Every protocol message should carry:

- identifier
- protocol and version
- sender identity
- recipient identity
- intent or message type
- payload
- authorization context
- policy context
- trust context
- correlation and causation identifiers
- timestamp
- signature or integrity proof

The envelope is the unit of attribution: a message without a verifiable envelope is not a governed interaction.

## Interaction Patterns

Protocols may compose into patterns:

- request and response
- delegation and report-back
- propose, approve, execute
- observe and notify
- escalate and resolve
- negotiate and commit
- orchestrate and reconcile

Higher-impact patterns require stronger identity, trust, approval, monitoring, and rollback.

## Conformance

A protocol implementation is conformant when it:

- authenticates both parties
- enforces scope and least authority
- honors policy and approval requirements
- carries provenance and trust context
- emits evidence for consequential exchanges
- fails closed on ambiguity, conflict, or low trust
- supports revocation and expiry
- declares and respects protocol version

## Interoperability Posture

OpenAutonomyX prefers open, standard agent and integration protocols over proprietary contracts.

External protocols are treated as integrations: bounded, attributable, and policy-bound, unless explicitly promoted to canonical status through a reviewed decision.

Protocol changes are versioned and backward-compatible where practical, and breaking changes proceed through decision records.

## Open Standards Alignment

The foundation pins agent protocols to specific open standards. Each is governed as a registry `standard` object with a pinned version.

| Concern | Protocol | Standard | Version | Posture |
|---|---|---|---|---|
| Agent identity | agent-identity | SPIFFE / SPIRE | SPIRE 1.14.1 | canonical |
| Authorization decision | authorization-decision | OpenID AuthZEN Authorization API | 1.0 (Final) | canonical |
| Policy evaluation | policy-evaluation | Open Policy Agent (OPA) | 1.14.0 | canonical |
| Relationship authorization | relationship-authorization | OpenFGA | 1.x | canonical |
| Reconciliation (agent-as-operator) | reconciliation | Operator Framework (operator-sdk) | 1.42.2 | integration |
| Orchestration (agent-as-orchestrator) | orchestration | — (operator-framework aligned) | — | experimental |
| Capability discovery | capability-discovery | Artifact Hub | rolling | integration |

Authorization separates decision from enforcement (AuthZEN PDP/PEP), with policy decisions backed by OPA and relationship decisions backed by OpenFGA. Versions are tracked in `registry/standards/`.

## Operator and Orchestrator Patterns

Agents may act as **operators** — running a declarative, idempotent reconciliation loop that drives observed state toward governed desired state — and as **orchestrators** — decomposing objectives and delegating scoped, revocable work to sub-agents.

Both patterns require per-step authorization decisions, approval gates for consequential actions, fail-closed behavior, and aggregated evidence.

## Governance

Agent protocols are governed by identity, trust, policy, approval, separation of duty, traceability, and auditability.

Protocol exchanges that perform consequential actions are subject to the same approval and evidence requirements as any other governed action.

## Protocol Principle

A protocol is not just a wire format. A protocol is the governed contract that lets independent parties cooperate without surrendering accountability.
