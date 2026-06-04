# OpenAutonomyX Agent Language Model

The OpenAutonomyX agent language model defines the foundation as a formal graph language: a vocabulary of node terms, a grammar of edge types, and queries over the resulting graph.

## Purpose

A shared language lets humans and agents describe, validate, and reason over the governed world consistently. The registry is not just storage — it is a language whose sentences are well-formed governance statements.

## The Language as a Graph

```text
Vocabulary (nodes)  +  Grammar (edges)  =  Language (well-formed graph)
```

- **Vocabulary** — the canonical terms (agent, principal, capability, control, risk, trust, protocol, skill, digital-twin, …), defined in `taxonomy.agent-vocabulary`.
- **Grammar** — the allowed relationship (edge) types and which node types they may connect, defined in `taxonomy.agent-grammar`.
- **Sentences** — registry objects plus their typed relationships (e.g. *agent realizes-capability capability*, *control mitigates risk*).
- **Well-formedness** — every node validates against its schema and every edge resolves to a defined node (no dangling edges).

## Layers

- **Lexical** — vocabulary terms with definitions and aliases (mappable to schema.org DefinedTerm).
- **Syntactic** — grammar of valid edges between node types.
- **Semantic** — meaning carried by relationships, trust, provenance, and policy.
- **Pragmatic** — how statements drive action: authorization, approval, reconciliation.

## Querying the Graph

The graph is meant to be queried — to answer "which agents are subject to this risk?", "what controls mitigate it?", "what is this agent's desired vs observed state?". GraphQL/indexing approaches (e.g. The Graph) are referenced as a query and indexing model.

## Governance

Vocabulary and grammar are themselves governed taxonomies: versioned, reviewed, and mappable to external standards. Extending the language proceeds through decision records.

## Language Principle

If it cannot be said in the language — a typed node connected by a grammatical edge — it cannot be governed. Express the world as a well-formed graph, and governance becomes queryable.
