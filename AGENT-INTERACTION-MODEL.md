# OpenAutonomyX Agent Interaction Model

The OpenAutonomyX agent interaction model defines how agents interact with humans, other agents, tools, data, and systems.

## Purpose

Interaction is where value and risk are created. Every interaction must be attributable, scoped, policy-bound, and observable, regardless of who or what is on the other side.

## Interaction Surfaces

- human ↔ agent
- agent ↔ agent
- agent ↔ tool
- agent ↔ data
- agent ↔ system or service
- agent ↔ workspace

## Interaction Modes

- request and response
- conversation and clarification
- delegation and report-back
- propose, approve, execute
- observe and notify
- orchestrate and reconcile
- negotiate and commit
- escalate and resolve

## Interoperability

Agent-to-tool interaction aligns to the Model Context Protocol. Agent-to-agent interaction aligns to the Agent2Agent protocol. Authorization, identity, and policy protocols apply to every interaction (see the agent protocol model).

## Interaction Obligations

Every consequential interaction must:

- authenticate both parties
- carry purpose and scope
- obtain an authorization decision
- respect least authority
- produce evidence
- fail closed on ambiguity, conflict, or low trust

## Human Interaction

Human interaction must preserve clarity, consent, contestability, and the ability to intervene, override, or halt.

## Interaction Principle

An interaction is a governed exchange of intent and authority, not a free conversation. Accountability travels with every message.
