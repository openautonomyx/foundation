# ADR 0006: Agent Protocol Model

## Status

Accepted

## Context

OpenAutonomyX principles require that everything interoperates through open protocols, yet the foundation defined agent identity, trust, governance, and an operating model without defining how agents actually interoperate.

Without an explicit protocol model, agent-to-agent and agent-to-system interaction risks implicit trust, ambient authority, vendor lock-in, and ungoverned action across system boundaries.

## Decision

Adopt a foundation agent protocol model defining how agents, humans, services, and systems interoperate.

The model defines:

- a layered protocol stack (transport, identity, interaction, semantic, governance)
- a set of named core protocols (identity handshake, capability discovery, intent and task, delegation, context exchange, approval, escalation, trust exchange, evidence and audit, negotiation, termination and revocation)
- a message envelope that makes every exchange attributable
- conformance criteria, including fail-closed behavior on ambiguity or low trust
- an open-standards interoperability posture where external protocols are treated as integrations unless promoted through a decision record

Protocols are treated as governed contracts, not merely wire formats.

## Consequences

Agent interoperability becomes explicit, scoped, verifiable, observable, revocable, and versioned.

Consequential protocol exchanges inherit the same identity, trust, approval, separation-of-duty, traceability, and auditability requirements as any other governed action.

Protocol changes are versioned; breaking changes proceed through decision records. Adopting or promoting an external protocol to canonical status requires a reviewed decision.
