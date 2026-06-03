# OpenAutonomyX Internet of Agents Model

The OpenAutonomyX Internet of Agents (IoA) model describes how heterogeneous agents interconnect, discover one another, and collaborate at scale under governance.

## Purpose

As agents proliferate across virtual and physical environments, they need a unified, agent-centric infrastructure for interconnection, discovery, and collaboration — an "Internet of Agents" — that remains governed, secure, and accountable.

## Operational Enablers

Grounded in the IoA literature, the key enablers are:

- **Capability notification and discovery** — agents advertise and find capabilities (foundation: capability discovery protocol, Artifact Hub).
- **Adaptive communication protocols** — open interoperability across vendors and frameworks (foundation: MCP for tools, A2A for agents).
- **Dynamic task matching** — route work to the best-suited agent.
- **Consensus and conflict resolution** — reconcile disagreement among agents.
- **Incentive models** — align agent behavior with principal intent (foundation: principal–agent model, skills).

## Governance Overlay

The IoA must not be an ungoverned mesh. The foundation overlays:

- verifiable identity for every participant (SPIFFE)
- per-interaction authorization (AuthZEN / OPA / OpenFGA)
- trust assertions and evaluation gating participation
- evidence and observability (OpenTelemetry) for every exchange
- fail-closed behavior on low trust or policy conflict

## Reference Framework (IoA, Chen et al., ICLR 2025)

A concrete IoA framework demonstrates these enablers and informs this model:

- **Agent integration protocol** — wrap heterogeneous, third-party agents (built in different ecosystems) behind a uniform interface (e.g. a `run()` adapter, often containerized) so they can collaborate.
- **Instant-messaging-like architecture** — a server routes messages and coordinates; each agent is a client with its own connection; layered into interaction, data, and foundation layers.
- **Nested team formation** — agents discover collaborators by capability and form small, sparse subgroups, reducing communication overhead versus fully-connected topologies.
- **Conversation flow control (FSM)** — a finite state machine governs states (discussion, synchronous/asynchronous task assignment, pause-and-trigger, conclusion), with an LLM deciding transitions and the next speaker.

The foundation adopts these patterns under governance: integration adapters are supply-chain-verified, message routing is authorized and logged, team formation respects trust thresholds, and FSM transitions emit evidence.

## Architecture Posture

Hierarchical and federated rather than flat: nested principal–agent relationships, scoped delegation, and cascaded control loops, on a cloud-native substrate.

## IoA Principle

An Internet of Agents is only as safe as its governance is native. Interconnection at scale demands identity, authorization, trust, and evidence by default.
