# OpenAutonomyX Digital Twin Model

The OpenAutonomyX digital twin model defines how a live virtual representation of a real entity — including an agent — is created, synchronized, and governed.

## Purpose

A digital twin is a virtual representation that serves as the real-time digital counterpart of a physical or operational entity, kept in sync through data so it can be observed, simulated, predicted, and reconciled.

In this foundation a twin makes the principle "current state is a projection, not truth" operational: the twin is the governed, evidence-backed projection of the real thing.

## Fidelity Levels

Following the digital-twin literature, twins are classified by direction and automation of data flow:

- **Digital model** — manual data exchange; no automatic flow between physical and virtual.
- **Digital shadow** — automatic one-way flow from the real entity to the virtual one.
- **Digital twin** — automatic two-way flow; the virtual entity can also drive change in the real one.

## Twin Components

- **Real entity** — the physical asset, process, system, organization, or agent.
- **Virtual entity** — the model holding live state, history, and behavior.
- **Data binding** — the telemetry and control connection keeping them in sync.

## Twin Types

asset, product, process, system, infrastructure, environment, organization (digital twin of an organization), and **agent**.

## The Agent Twin

An agent twin pairs:

- **Desired state** — the agent's approved registered definition (capabilities, tools, scopes, autonomy, controls).
- **Observed state** — a runtime snapshot of what the agent actually is and does.

The gap between them is **drift**. The reconciliation protocol (operator pattern) drives observed state back toward desired state; drift detection raises it as a governed signal.

## Enabling Substrate

Twins are fed by observability (OpenTelemetry traces, metrics, logs) and history from an append-only event log, on a cloud-native runtime. Simulation runs "what-if" futures against the twin before changes touch the real entity.

## Governance

A twin is a governed registry object. Acting on the real entity through its twin is a consequential action: it inherits identity, authorization, approval, and evidence requirements. Twin state classification follows the data it reflects.

## Twin Principle

A digital twin is not a copy; it is an accountable, synchronized projection you can reason over, simulate against, and reconcile toward — without first risking the real thing.
