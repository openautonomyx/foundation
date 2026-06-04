# OpenAutonomyX Agent Memory Model

The OpenAutonomyX agent memory model defines how agents capture, retain, recall, and dispose of context and knowledge under governance.

## Purpose

Memory makes agents useful and dangerous in equal measure. It must be governed by purpose, consent, privacy, retention, provenance, and access controls.

## Memory Types

- **Working memory** — transient, task-scoped context.
- **Session memory** — bounded to an interaction or workspace session.
- **Long-term memory** — durable, governed recall across sessions.
- **Episodic memory** — records of past actions and outcomes.
- **Semantic / knowledge memory** — validated facts and approved knowledge.
- **Shared memory** — workspace or team context with access controls.

## Knowledge Gradient

Agents must distinguish:

```text
source data → extracted claim → inferred knowledge
→ reviewed knowledge → approved canonical knowledge → remembered context
```

Confidence and provenance travel with every item; unverified content must not be treated as fact.

## Memory Governance

Every memory item should define purpose, consent context, classification, retention rule, review date, disposition rule, and access rules.

Memory is append-over-overwrite where practical, with prior states reconstructable.

## Memory Risks

- retention beyond purpose
- leakage across tenants or workspaces
- poisoning and injection
- stale or drifted knowledge
- unconsented personal data

These are mitigated by classification, scoping, provenance, review, and disposition.

## Memory Principle

An agent should remember only what it is permitted to remember, for only as long as it is permitted to remember it, and should know how sure it is of what it remembers.
