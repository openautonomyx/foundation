# Foundation Taxonomies

Taxonomies define controlled vocabularies, classifications, allowed values, and mappings used across the OpenAutonomyX Foundation.

## Purpose

Taxonomies make foundation concepts consistent, searchable, governable, and interoperable across repositories, agents, platforms, policies, schemas, registries, and enterprise operating models.

## Taxonomy Principles

Every taxonomy should define:

- identifier
- name
- description
- owner
- version
- lifecycle state
- allowed values
- parent-child relationships where applicable
- mappings to external standards where applicable
- deprecated values
- review cadence

## Suggested Taxonomies

```text
taxonomies/
├── capability-taxonomy.yaml
├── risk-taxonomy.yaml
├── control-taxonomy.yaml
├── decision-taxonomy.yaml
├── workspace-taxonomy.yaml
├── knowledge-taxonomy.yaml
├── memory-taxonomy.yaml
├── agent-taxonomy.yaml
├── identity-taxonomy.yaml
├── trust-taxonomy.yaml
├── policy-taxonomy.yaml
└── artifact-taxonomy.yaml
```

## Mapping

Taxonomies may map to external standards and frameworks, including schema.org, SOC 2, ISO 27001, NIST, GDPR, HIPAA, PCI DSS, DORA, AI governance frameworks, enterprise architecture frameworks, and industry-specific taxonomies.

Mappings must preserve source, version, date, and confidence.

## Principle

A governed enterprise system needs shared language. Taxonomies turn shared language into reusable structure.
