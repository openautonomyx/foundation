# ADR 0004: Identity Model

## Status

Accepted

## Context

OpenAutonomyX systems need explicit identity for humans, agents, organizations, teams, services, applications, devices, tenants, and workspaces.

Without a shared identity model, access, accountability, trust, authorization, auditability, and governance become inconsistent across repositories.

## Decision

Adopt a foundation identity model that defines:

- identity types
- lifecycle states
- credential bindings
- verification states
- ownership
- roles and permissions
- capability bindings
- policy bindings
- trust state
- audit trail

Identity is treated as the accountable root for action, trust, responsibility, and governance.

## Consequences

All OpenAutonomyX systems should bind consequential actions to explicit identities.

Agent identity, human identity, organization identity, and service identity must be lifecycle-managed and revocable.

Identity records should support future DID, verifiable credential, SSO, SCIM, IGA, and PAM integrations.
