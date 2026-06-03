# OpenAutonomyX Agent Control Theory Model

The OpenAutonomyX agent control theory model applies classical control theory to governing autonomous agents.

## Purpose

Governing an agent is a control problem: keep a system's behavior within bounds despite disturbance, using feedback. Control theory gives precise language for what governance must guarantee.

## Control Concepts, Applied

- **Reference / setpoint** — the desired state: the agent's approved definition and the constitution.
- **Plant** — the agent and its effects on the world.
- **Sensor** — observability and evidence (OpenTelemetry, audit log).
- **Controller** — the governance system (policy, authorization, approval).
- **Actuator** — allowed actions and tool grants.
- **Feedback loop** — observe → compare to setpoint → correct (the reconciliation / operator pattern).
- **Disturbance** — drift, prompt/tool attacks, environment change.

## Properties Governance Must Provide

- **Observability** — the true state must be inferable from available signals; unobservable agents cannot be governed.
- **Controllability** — the controller must be able to drive the agent back into the allowed region (suspend, revoke, kill switch).
- **Stability** — small disturbances must not cause runaway behavior; bounded inputs yield bounded outputs.
- **Closed-loop over open-loop** — never deploy autonomy without feedback; fail closed when the loop is broken.

## Loop Design

- **Sampling and latency** — sense and decide fast enough to act before harm.
- **Damping** — avoid oscillation and over-correction (e.g. approval thrash).
- **Saturation limits** — rate, budget, and scope caps bound actuation.
- **Hysteresis** — avoid flapping between autonomy levels on noisy signals.
- **Cascaded control** — orchestrators form nested loops; each sub-agent loop is bounded by its parent.

## Relationship to Other Models

This model unifies the reconciliation protocol (the loop), the digital twin (the observed-vs-desired state), evaluation (the error signal), and the principal–agent model (why the loop is needed).

## Control Principle

Autonomy without a closed feedback loop is not control — it is hope. Govern agents as controlled systems: observable, controllable, and stable, or not deployed.
