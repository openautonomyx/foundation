# ADR 0002: Meta-Model

## Status

Accepted

## Context

OpenAutonomyX needs a shared semantic foundation so that repositories, platforms, agents, policies, artifacts, decisions, and governance records use consistent language and structure.

Without a common meta-model, each project may define its own incompatible concepts for identity, entities, actions, events, artifacts, trust, policy, memory, knowledge, and decisions.

## Decision

Adopt a root `Thing` abstraction as the foundation for governed concepts.

A `Thing` may specialize into:

- identity
- trust assertion
- entity
- artifact
- action
- event
- decision
- policy
- relationship
- capability
- skill
- knowledge
- memory
- evaluation

Every governed thing should define identity, type, lifecycle state, ownership, version, provenance, relationships, policy bindings, trust state, evidence, and audit trail where applicable.

## Consequences

All future OpenAutonomyX models should inherit from or map to the meta-model.

This enables consistent governance, traceability, validation, registry design, and cross-repository interoperability.

New concepts should be introduced by extending the meta-model rather than creating isolated terminology.
