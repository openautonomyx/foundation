# OpenAutonomyX Action Model

The OpenAutonomyX action model defines intentional operations performed by humans, agents, services, applications, devices, or external systems.

## Purpose

Actions are the observable bridge between intent and system change.

Every consequential action must be attributable, authorized, policy-bounded, logged, reviewable, and connected to evidence.

## Action Types

Core action types include:

- create
- read
- update
- delete
- approve
- reject
- review
- publish
- archive
- execute
- delegate
- escalate
- reconcile
- evaluate
- certify
- revoke
- notify
- transform
- import
- export

## Common Action Fields

Every action should define:

- identifier
- action type
- actor
- target
- tool or interface
- input
- output
- authorization context
- policy context
- approval state
- execution state
- result
- evidence
- timestamp
- duration where applicable
- error state where applicable
- audit trail

## Actor

The actor is the entity that performs or requests the action.

Actors may be humans, agents, services, applications, devices, or integrations.

## Target

The target is the thing being acted upon.

Targets may include entities, artifacts, data, policies, workflows, decisions, credentials, relationships, or external systems.

## Authorization

Actions must be authorized before execution where required.

Authorization should consider:

- identity
- role
- relationship
- capability
- trust state
- policy
- context
- risk
- approval requirements

## Execution State

Common action execution states include:

- proposed
- pending approval
- approved
- denied
- scheduled
- running
- completed
- failed
- rolled back
- cancelled
- expired

## Evidence

Actions should produce or reference evidence sufficient to explain what happened, why it happened, who or what performed it, what changed, and whether the result matched the expected outcome.

## Action Principle

An action is not merely an operation. An action is an accountable, governed, observable unit of change.
