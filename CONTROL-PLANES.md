# OpenAutonomyX Control Planes

OpenAutonomyX defines a two-plane model that separates **enterprise governance** from **agent operation**.

## The Two Planes

- **Enterprise Control Plane — OpenAutonomyX.** Governs the enterprise: capabilities, risks, controls, policies, identity, trust, decisions, and the governed registry. It defines *what is allowed, by whom, under what evidence*. It does not run agents.
- **Agent Control Plane — AGenNext.** Runs and manages agents operationally; an agent builder platform and runtime. It executes work *within* the constraints the enterprise control plane sets.

Bridging the two is the **Agent Operation Model — AutonomyX**: the model defining *how* agents operate (identity, autonomy levels, delegation, evaluation, reconciliation). OpenAutonomyX **defines** the operation model; AGenNext **implements** it.

```text
Enterprise Control Plane (OpenAutonomyX)   — governs —▶   Agent Control Plane (AGenNext)
   capabilities · risks · controls                          build · run · reconcile agents
   policy · identity · trust · decisions                     tools · memory · workflows
            ▲  evidence, attestation, drift  ◀───────────────────────┘
```

## Responsibilities

| Concern | Enterprise Control Plane (OpenAutonomyX) | Agent Control Plane (AGenNext) |
|---|---|---|
| Policy & approval | defines and adjudicates | enforces at runtime |
| Identity & trust | issues standards, sets thresholds | binds identities, presents evidence |
| Capabilities/risks/controls | owns the governed registry | realizes and operates them |
| Agents | governs lifecycle & autonomy | builds, deploys, runs, reconciles |
| Evidence | requires and audits | emits (telemetry, audit trail) |

## Relationship

The agent control plane operates **within** the enterprise control plane: it requests authorization, honors policy and approval, and returns evidence. The enterprise control plane **governs** the agent control plane: it grants scope, evaluates, and can suspend or revoke.

This mirrors the cloud-native split between a **control plane** (desired state, policy) and a **data/operational plane** (execution) — here applied at two layers: enterprise governance over agent operation.

## Ecosystem Pillars

The control planes sit within a five-pillar ecosystem, each registered as a governed entity:

| Pillar | Brand | Role |
|---|---|---|
| Enterprise Control Plane | **OpenAutonomyX** | Governs the enterprise: capabilities, risks, controls, policy, identity, trust |
| Agent Operation Model | **AutonomyX** | Defines how agents operate (identity, autonomy, delegation, evaluation, reconciliation) |
| Agent Control Plane / Builder | **AGenNext** | Builds, deploys, runs, and reconciles agents |
| Research & Innovation | — | Tracks research; matures candidate capabilities before they become doctrine |
| Economy | — | Value creation, metering, settlement, and economic governance of agent work |

## Vision

The ecosystem is anchored on two ends — **research** and the **realization of value** — and the control planes govern the path between them:

```text
Research & Innovation ─▶ Operation Model ─▶ Agents (built & run) ─▶ Governed Economy ─▶ Realized Value
        (AutonomyX research)     (AutonomyX)        (AGenNext)            (Economy)        (audited outcomes)
                         └──────────── governed throughout by OpenAutonomyX ────────────┘
```

Research turns ideas into candidate capabilities; the enterprise control plane governs their adoption; agents operate them; and value is realized as **measurable, audited outcomes** — not unaccountable activity. Every step is traceable from a research claim to realized, evidenced value.

## Principle

Governance and operation are different planes. The enterprise control plane decides; the agent control plane does. Neither absorbs the other.
