# ADR 0005: Trust Model

## Status

Accepted

## Context

OpenAutonomyX systems require a consistent way to decide whether identities, agents, organizations, services, tools, datasets, models, artifacts, and workflows can be relied upon.

Identity alone is not enough. A system must also understand evidence, capability, behavior, reliability, compliance, and review history.

## Decision

Adopt a foundation trust model based on explicit trust assertions.

Trust assertions must define:

- subject
- issuer
- claim
- domain
- evidence
- confidence
- score where applicable
- validity period
- review date
- revocation conditions
- lifecycle state

Trust is treated as governed reliance based on evidence, not blind belief.

## Consequences

Trust can influence access, routing, approval requirements, delegation, autonomy level, monitoring, escalation, publication eligibility, certification, suspension, and revocation.

Trust must be reviewable, renewable, suspendable, and revocable.
