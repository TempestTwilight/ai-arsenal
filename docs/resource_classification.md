# Resource Classification Standard

This document defines how a resource is classified and how its relevance to a collection's
domain is established. It applies to every AI Arsenal collection. Collection-specific
boundaries belong in that collection's scope document.

## Resource classes

| Class | Definition | Examples |
| --- | --- | --- |
| Core | A standalone artifact that provides value on its own | Research paper, original dataset, model, framework, technical specification |
| Supporting | Material that explains, teaches, or documents a Core resource or the domain | Tutorial, course, textbook, documentation, technical guide |

| Requirement | Core | Supporting |
| --- | --- | --- |
| Attributable origin | Mandatory | Mandatory |
| Relevance | Demonstrated, using the evidence below | Documents an admitted Core resource, or declares the domain application as its subject |
| Standalone value | Required | Not required |

A Supporting resource is admitted by its relationship to a Core resource or by its declared
subject, never by being generically useful.

## Relevance and Applicability

A resource must establish a substantive and technically meaningful relationship with an
identifiable problem, application, workflow, or requirement within the intended domain.

At least one of the following forms of evidence must be established:

- Development: The resource was designed, developed, or adapted to address a specific
  technical problem, requirement, or use case within the intended domain.

- Validation: The resource was experimentally evaluated, benchmarked, or validated using
  relevant datasets, scenarios, test environments, or requirements, with results
  demonstrating its applicability to the identified use case.

- Integration: The resource was implemented, integrated, or demonstrated within an existing
  system, subsystem, application, or operational workflow relevant to the intended domain.

Additional technical characteristics, performance optimizations, and domain-specific
constraints may strengthen the evidence of applicability but shall not independently
establish eligibility.

### Evidence for learning material

Tutorials, courses, textbooks, guides, and documentation sets are not developed, validated,
or integrated in the sense above. They establish relevance through declared scope: the
resource's official description states that its subject is the intended domain application,
and it is attributable to a publisher, institution, or named author.

Declared scope is not available to datasets, models, frameworks, or infrastructure. Those
require development, validation, or integration evidence.

## Insufficient Evidence

The following shall not constitute sufficient evidence of relevance or applicability:

- Merely mentioning a domain or application as a potential use case.

- Using domain-associated datasets without addressing a meaningful problem or requirement
  within that domain.

- Demonstrating general-purpose capabilities that could theoretically be applied to the
  intended domain.

- Optimizing for generic performance, computational, or operational constraints without
  establishing their relevance to an identifiable domain-specific requirement.

- Claiming applicability based solely on theoretical potential without supporting technical
  methodology, implementation details, experimental results, or documented requirements.

## Evaluation Principle

A resource shall be evaluated based on what it demonstrably enables, addresses, or
contributes to within the intended domain, rather than what it could theoretically be used
for.

All claims of relevance and applicability must be traceable to authoritative documentation,
original publications, experimental evidence, or other verifiable sources.
