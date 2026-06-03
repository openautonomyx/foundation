# OpenAutonomyX Agent Framework Model

The OpenAutonomyX agent framework model defines how agent-building frameworks are selected, integrated, and governed without lock-in.

## Purpose

Frameworks accelerate building agents but must not dictate governance. The foundation stays framework-neutral: governance, identity, policy, and protocols are owned by the foundation; frameworks are integrations.

## Framework Concerns

A framework typically provides some of: orchestration, planning, tool/function calling, memory, retrieval, evaluation, and runtime.

## Selection Criteria

- open standards support (MCP, A2A)
- portability and avoidance of lock-in
- identity and policy integration points
- observability and evidence hooks
- evaluation and testing support
- security posture and supply-chain hygiene
- community and maintenance health
- alignment with the CNCF AI-native ecosystem

## Governance Posture

Frameworks are registered as governed `standard` objects with a pinned version and an adoption posture (canonical, integration, experimental, evaluating, deprecated).

Adopting or promoting a framework to canonical status proceeds through a decision record.

## Neutrality Rule

No framework may bypass foundation identity, authorization, policy, approval, evidence, or the agent constitution.

## Framework Principle

Frameworks are how agents are built; the foundation is how agents are governed. The second must never be surrendered to the first.
