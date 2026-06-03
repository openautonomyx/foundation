# OpenAutonomyX Agent Tool Model

The OpenAutonomyX agent tool model defines how agents access external functions, services, and effects under governance.

## Purpose

Tools are how agents touch the world. They are also the primary path to consequential action and the primary attack surface, so tool access must be explicit, scoped, and authorized.

## Tool Types

- read tools (retrieve data or state)
- write / action tools (change state)
- compute and transformation tools
- communication and notification tools
- external service and API tools
- privileged and destructive tools

## Tool Interface

Tools are accessed through the Model Context Protocol where possible, with a declared schema for inputs, outputs, side effects, and required scopes.

## Tool Governance

Every tool binding should declare: purpose, allowed scopes, authorization requirement, approval requirement, rate and budget limits, evidence produced, and risk rating.

Read tools and write tools are governed differently; destructive and privileged tools require approval and separation of duty.

## Tool Security

- least-privilege, time-bound tool grants
- input/output validation and injection defenses
- per-call authorization decision (PDP/PEP)
- provenance for tool artifacts (supply chain)
- fail closed on ambiguity or denied authorization

## Tool Principle

A tool grant is a grant of authority over the world. Grant the least, authorize each use, and record every effect.
