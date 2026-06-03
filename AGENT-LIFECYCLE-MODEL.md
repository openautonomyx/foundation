# OpenAutonomyX Agent Lifecycle Model

The OpenAutonomyX agent lifecycle model defines the governed stages an agent passes through from conception to retirement.

## Purpose

An agent is not a static artifact. It is a long-lived, evolving participant whose identity, capability, trust, and authority change over time and must remain governed at every stage.

## Lifecycle Stages

```text
proposed → designed → registered → identity-issued → approved
→ deployed → operating → evaluated → adapted
→ suspended → revoked → retired → archived
```

Each transition is an accountable event with an owner, evidence, and policy context.

## Stage Obligations

- **Proposed** — purpose, sponsor, intended value, and candidate risks declared.
- **Designed** — capabilities, tools, data scopes, autonomy level, and controls specified.
- **Registered** — recorded as a governed registry object with version and ownership.
- **Identity-issued** — verifiable identity bound (see agent identity protocol).
- **Approved** — human approval recorded for deployment and autonomy level.
- **Deployed** — released into a governed workspace with kill switch enabled.
- **Operating** — actions are authorized, policy-bound, and evidence-producing.
- **Evaluated** — performance, safety, and compliance assessed against thresholds.
- **Adapted** — capability, prompt, model, or scope changes re-enter design and approval.
- **Suspended** — paused on policy violation, lost trust, or detected risk.
- **Revoked** — authority and identity withdrawn.
- **Retired / Archived** — decommissioned with retained audit trail.

## Drift and Change

Long-lived agents drift as prompts, tools, models, memory, knowledge, and configuration change.

Material change must trigger re-design, re-evaluation, and re-approval rather than silent mutation. Drift between the approved definition and the running agent is itself a governed signal.

## Lifecycle Principle

An agent is trustworthy only while its current state still matches what was approved. Lifecycle governance keeps that statement true over time.
