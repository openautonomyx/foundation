# Building Safe, Reliable Agents

This guide is the practical synthesis of the OpenAutonomyX foundation: how to build agents that are safe, reliable, governed, and useful.

## Principle

Safety and reliability are designed in, not added on. An agent earns autonomy through evidence and keeps it only while the evidence holds.

## Build Sequence

1. **Define the use case first** — problem, scope, value, risk (see AI use case model).
2. **Give the agent an identity** — verifiable, attested (SPIFFE/SVID).
3. **Scope authority** — least-privilege capabilities, tools, and data; default high-risk off.
4. **Bind the constitution** — inviolable principles outrank objective and prompt.
5. **Set autonomy deliberately** — start low (suggest / draft / execute-with-approval); raise on evidence.
6. **Authorize every action** — policy decision (OPA) and relationship checks (OpenFGA) via AuthZEN PDP/PEP separation.
7. **Gate consequential actions** — human approval and separation of duty.
8. **Govern memory and knowledge** — purpose, consent, provenance, retention; claims are not facts.
9. **Secure the supply chain** — signed components, bill of materials, verified provenance.
10. **Use open protocols** — MCP for tools, A2A for agents; avoid lock-in.
11. **Instrument everything** — attributable, replayable events and evidence.
12. **Evaluate continuously** — quality, safety, compliance against thresholds.
13. **Plan for failure** — fail closed, kill switch, rollback, escalation paths.
14. **Detect drift** — alert when the running agent diverges from the approved definition.

## Reliability Practices

- declarative desired state and idempotent reconciliation
- graceful degradation and bounded retries
- timeouts, rate limits, and budget caps
- circuit breakers and suspension conditions
- cloud-native, observable runtime (Kubernetes / CNCF)

## Safety Practices

- fail closed on ambiguity, conflict, or low trust
- human oversight and contestability preserved
- harm avoidance and refusal of unlawful or out-of-policy instructions
- red-teaming and incident review

## The Test

An agent is ready when you can answer, with evidence: Who is it? What may it do? Who approved that? What did it do? Why? Can we prove it, stop it, and undo it?

## Closing Principle

Safe, reliable autonomy is accountable autonomy. If you cannot govern it, do not deploy it.
