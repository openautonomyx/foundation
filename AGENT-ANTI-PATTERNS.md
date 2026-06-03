# OpenAutonomyX Agent Anti-Patterns

Recurring failure modes in agent systems and the foundation mechanism that prevents each.

| Anti-pattern | Why it's dangerous | Prevented by |
|---|---|---|
| **Ambient authority** | Agent holds broad standing access it rarely needs | Least-privilege scopes, OpenFGA, scoped delegation |
| **Unbounded autonomy** | Agent acts without approval on consequential actions | Autonomy levels, human approval, AuthZEN gate |
| **Prompt-as-policy** | Governance rules live only in the prompt and can be overridden | Constitution + policy-as-code outrank the prompt |
| **Silent drift** | Running agent diverges from its approved definition unnoticed | Drift detection, digital twin, re-approval on change |
| **Unverified memory** | Treating recalled or retrieved content as fact | Provenance + validation state; claims ≠ facts |
| **Fail-open** | Agent proceeds under ambiguity, conflict, or low trust | Fail-closed conformance requirement |
| **God agent** | One agent owns end-to-end consequential flow | Separation of duty, orchestrator with scoped sub-agents |
| **Unattributable action** | Cannot reconstruct who did what and why | Verified identity + evidence + OpenTelemetry |
| **Lock-in by default** | Proprietary integration prevents substitution | Open protocols (MCP, A2A), portability posture |
| **Eval theater** | Metrics gamed; no real safety/quality signal | Versioned, protected evaluation; relative + subjective checks |
| **Standing secrets** | Long-lived credentials embedded in the agent | Short-lived attested identity (SPIFFE/SVID) |
| **Unbounded spend** | Autonomous financial commitments without limits | Budget caps, approval thresholds, separation of duty |

## Anti-Pattern Principle

Most agent incidents are a known anti-pattern deployed without its control. Name them, and design them out.
