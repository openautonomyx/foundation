# OpenAutonomyX Agent Threat Model

A structured view of how agent systems are attacked and how the foundation mitigates each threat. Aligned to OWASP agentic threats and STRIDE.

## Assets to Protect

Agent identity and credentials · tools and their authority · memory and knowledge · the supply chain (models, prompts, dependencies) · enterprise data and systems · the audit trail.

## Threats and Mitigations

| Threat | Example | Mitigation |
|---|---|---|
| **Identity spoofing** | Impersonating an agent or principal | SPIFFE/SVID attestation; verify before any exchange |
| **Prompt injection** | Malicious input redirects the agent | Input/output validation; constitution outranks prompt; fail closed |
| **Tool misuse (OWASP T2)** | Coercing destructive tool calls | Least-privilege grants, argument validation, sandboxing, approval for destructive ops |
| **Memory poisoning (OWASP T1)** | Planting false data in memory | Validate/sanitize, isolate per user/session, integrity checks, expiry |
| **Privilege escalation** | Agent expands its own scope | No self-escalation; OpenFGA checks; separation of duty |
| **Supply-chain compromise** | Tampered model/tool/dependency | Signed artifacts, bill-of-materials, provenance verification |
| **Data exfiltration** | Leaking data via tools/egress | Scoped data access, egress controls, evidence/audit |
| **Repudiation** | Cannot prove what happened | Attributable, replayable evidence (OpenTelemetry) |
| **Denial / resource exhaustion** | Runaway loops, cost blowout | Rate/budget caps, circuit breakers, kill switch |
| **Collusion (multi-agent)** | Agents conspire to bypass controls | Per-step authorization, independent audit, separation of duty |

## Trust Boundaries

Boundaries exist at: human↔agent, agent↔agent, agent↔tool, agent↔data, and tenant/workspace edges. Every crossing authenticates, authorizes, and logs.

## Posture

Fail closed on ambiguity, conflict, or low trust. Assume third-party agents and tools are untrusted until verified. Transport encrypted (TLS 1.3); peers authenticated (OAuth2 / SVID).

## Threat Principle

Model the attacker before granting autonomy. Every grant of authority is a grant of attack surface.
