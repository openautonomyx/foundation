# OpenAutonomyX Foundation

OpenAutonomyX Foundation is the canonical home for the mission, principles, governance model, architecture doctrine, operating model, schemas, policies, and decision records that guide OpenAutonomyX projects.

## Purpose

OpenAutonomyX exists to help individuals, teams, institutions, and societies build reliable, governed, transparent, and human-aligned autonomous systems.

This repository defines the shared foundation used across OpenAutonomyX work:

- Mission and manifesto
- Founding principles
- Governance and operating model
- Architecture doctrine
- AI-native and cloud-native principles
- Open standards posture
- Privacy, consent, traceability, reliability, and auditability policies
- JSON schemas for foundation artifacts
- Architecture decision records
- Contribution, security, and review process

## Core Beliefs

Everything is data.  
Everything is temporal.  
Everything is governed.  
Everything is observable.  
Everything is traceable.  
Everything is replayable.  
Everything is composable.  
Everything interoperates through open protocols.

Current state is a projection, not truth.  
Time is a first-class primitive.  
Identities persist; relationships evolve.  
Append over overwrite.  
Humans approve; systems reconcile.

AI-native and cloud-native are foundational principles.  
Governance must be native, not bolted on.  
Production-grade is the baseline, not the goal.

## Repository Structure

```text
.
├── README.md
├── MANIFESTO.md
├── PRINCIPLES.md
├── GOVERNANCE.md
├── OPERATING-MODEL.md
├── ARCHITECTURE.md
├── ROADMAP.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── LICENSE
├── docs/            # published searchable catalog (GitHub Pages)
├── registry/       # governed objects + INDEX.md catalog
├── schemas/        # JSON schemas for every object type
├── scripts/        # build_catalog.py (validate + generate catalog)
├── taxonomies/
├── adr/
├── policies/
└── .github/        # auto-update workflow
```

## Registry & Searchable Catalog

All governed objects live in `registry/`, validated against JSON schemas in `schemas/`.

- **Searchable catalog** — `docs/index.html` (published to GitHub Pages): full-text search and filters over every governed node.
- **Index** — `registry/INDEX.md`: human-readable catalog grouped by type and standard domain.
- **Machine-readable** — `docs/catalog.json`: the full node graph for external tooling.

The catalog is regenerated and revalidated automatically on every push by
`.github/workflows/catalog.yml` (which runs `scripts/build_catalog.py`); the
build fails if any object is schema-invalid or any relationship edge is
dangling.

## Foundation Contract

Every OpenAutonomyX project should be:

- Human-aligned
- Privacy-respecting
- Consent-aware
- Auditable
- Traceable
- Recoverable
- Interoperable
- Governed by default
- Open-standards aligned
- Production-grade by default

## Status

This repository is an initial foundation scaffold. Content is intentionally versioned and expected to evolve through reviewed decision records.
