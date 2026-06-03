# ADR 0007: Digital Twin Model

## Status

Accepted

## Context

The foundation holds that current state is a projection reconstructed from events, and it governs long-lived agents whose running state can diverge from their approved definition.

A consistent way was needed to represent the live, synchronized state of a real entity — especially an agent — so governance can observe, simulate, and reconcile it.

## Decision

Adopt a digital twin model.

A digital twin is a governed registry object representing a real entity with:

- a fidelity level (digital model, digital shadow, or digital twin) classified by direction and automation of data flow
- a real entity (subject) and a virtual entity holding live state and history
- a data binding (manual, one-way-automatic, two-way-automatic)
- desired vs observed state, with drift as the governed gap between them
- telemetry sources (OpenTelemetry), simulation capabilities, and a reconciliation path

The agent twin pairs an agent's approved definition (desired state) with a runtime snapshot (observed state); drift detection and the reconciliation protocol close the gap.

## Consequences

Twins make state inspectable, simulatable, and reconcilable without first risking the real entity.

Acting on a real entity through its twin is a consequential action and inherits identity, authorization, approval, and evidence requirements. Twin state classification follows the data it reflects.
