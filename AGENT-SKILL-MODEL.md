# OpenAutonomyX Agent Skill Model

The OpenAutonomyX agent skill model defines reusable, governed units of agent know-how that can be authored, shared, and composed.

## Purpose

A skill packages procedural knowledge — how to perform a class of task — so capability can be reused across agents without copying prompts or code. Skills make capability portable, versioned, and governed.

## Skill vs Capability vs Tool

- **Capability** — what the enterprise can do (strategic).
- **Skill** — how an agent performs a class of task (procedural know-how).
- **Tool** — an external function the skill invokes (mechanism).

## Skill Attributes

A governed skill should declare: identifier, purpose, inputs and outputs, required tools and data scopes, procedure or instructions, examples, autonomy level, policy bindings, evaluation method, version, and provenance.

## Authoring and Distribution

Skills are authored as portable packages, signed, versioned, and discoverable via the capability discovery protocol. Adopting a skill verifies provenance and runs a policy check first.

## Composition

Skills compose into larger workflows; an orchestrator may sequence skills across sub-agents. Composition inherits the strictest governance of its parts.

## Governance

High-impact skills default off and require approval to enable. Skill use produces evidence like any other action.

## Skill Principle

A skill is governed, reusable know-how — not an ungoverned prompt. Reuse capability without reusing risk.
