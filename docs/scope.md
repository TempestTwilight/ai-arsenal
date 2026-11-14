# Scope

AI Arsenal will eventually host multiple collections. This document defines only the first.

Resource classes and the evidence standard for relevance are defined in
[`resource_classification.md`](resource_classification.md). This document applies them to
Collection 1.

## Collection 1 — AI/ML for Space Systems

### Purpose

The collection helps someone move from a space-systems problem to a verifiable AI/ML
resource: a first working example for newcomers, and the primary literature and reference
implementations for those going deeper.

### Admission

A resource enters this collection only if all of the following hold:

1. **Attributable origin.** It has an official source that can be cited: the author's
   repository, the publisher's page, or a DOI.
2. **AI/ML substance.** It is a model, dataset, framework, infrastructure component, or
   the publication or specification that defines a method. Learning material about these
   is admitted as a Supporting resource.
3. **Demonstrated space-system applicability.** It satisfies the relevance standard in
   [`resource_classification.md`](resource_classification.md) for the intended domain,
   "space systems". Space-system constraints such as radiation tolerance, limited onboard
   compute, power limits, communication latency, and autonomous operation may strengthen
   the evidence but never establish it on their own.

Clause 3 is the binding one. A general-purpose resource is not admitted because it might
be useful in space; it is admitted only with development, validation, or integration
evidence for a specific space-system application.

### In scope

Resources that directly enable, support, or improve the development, deployment,
operation, or maintenance of space systems through AI/ML.

- **Spacecraft and satellite operations.** AI/ML models, techniques, and frameworks for
  autonomous operations, attitude determination and control, orbit determination,
  trajectory optimization, collision avoidance, fault detection, and mission planning.

- **Spacecraft-side Earth observation.** Onboard image processing, autonomous
  acquisition, sensor calibration, payload management, and compression.

- **Space robotics and autonomous systems.** Robotic manipulation, planetary rovers,
  autonomous navigation, terrain analysis, docking, rendezvous, and in-space servicing.

- **Space situational awareness.** AI/ML resources for object detection, tracking,
  identification, orbit prediction, conjunction assessment, debris monitoring, and
  traffic management.

- **Space communications and networking.** AI/ML techniques for communication
  optimization, signal processing, adaptive networking, inter-satellite links, resource
  allocation, and communication anomaly detection.

- **Spacecraft health monitoring and reliability.** Predictive maintenance, anomaly
  detection, fault diagnosis, failure prediction, telemetry analysis, and subsystem
  health assessment.

- **Scientific payload autonomy.** AI/ML for instrument telemetry, onboard data triage,
  observation scheduling, and payload health. Analysis of the resulting science data is
  out of scope (see below).

- **Onboard and edge AI.** Models, frameworks, and deployment or optimization tooling for
  inference and training under space-specific constraints: radiation, power, memory,
  compute, and communication limits.

- **Space-specific AI/ML infrastructure.** Simulation environments, digital twins,
  synthetic data pipelines, testing frameworks, and deployment infrastructure designed
  for space systems.

- **Research and foundational methods.** AI/ML architectures, algorithms, and techniques
  with development, validation, or integration evidence for a specific space-system
  application.

### Out of scope

- **Generic AI/ML resources.** General-purpose models, algorithms, datasets, and
  frameworks without demonstrated space-system applicability.

- **Astrophysics and general astronomy.** Observational or interpretive science content,
  and science datasets, that do not address a space-system problem.

- **News and general-interest publications.** News, blogs, opinion, industry updates,
  marketing material, and other non-technical space content.

- **Business and policy.** Market analysis, investment reports, business strategy,
  regulation, and policy documents unrelated to the technical development or operation of
  space systems.

- **General software development.** Programming tutorials, utilities, and software
  engineering material not specific to AI/ML in space systems.

- **Non-AI/ML space technology.** Space technology and engineering resources with no
  meaningful AI/ML component.

- **Unattributable or aggregated content.** Listicles, unofficial summaries, unsourced
  claims, and reposts whose origin cannot be established.

- **Earth-side Earth-observation applications.** Satellite imagery analysis,
  environmental monitoring, land classification, and disaster assessment performed on the
  ground for Earth purposes.

### Rulings on known neighbours

Each case was tested against the relevance standard. A category is never admitted on its
own; a specific resource inside it is admitted only with evidence.

| Case                                                                                    | Verdict           | Basis                                                                                                              |
| --------------------------------------------------------------------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| General-purpose models and frameworks                                                   | Out               | Fails the evidence standard; "could be adapted" is not evidence                                                    |
| General-purpose datasets used for pretraining or benchmarking                           | Out               | Fails the evidence standard                                                                                        |
| General simulation and digital-twin platforms                                           | Out as a category | Admitted as Core only if a specific platform has published space validation or integration                         |
| Earth-based analogues (terrestrial robotics, terrestrial remote sensing)                | Out               | Fails the evidence standard; the operating environment is the distinguishing requirement                           |
| Emerging techniques with potential space use                                            | Out               | Lacks demonstrated implementation                                                                                  |
| General hardware, edge platforms, accelerators                                          | Out               | Hardware is not an AI/ML resource; frameworks targeting space-qualified hardware are in scope                      |
| Mathematical and scientific foundations (optimization, control, reinforcement learning) | Out               | Fails the evidence standard; the paper is admitted only if it demonstrates a space-system application              |
| Courses, textbooks, tutorials, documentation                                            | In as Supporting  | Attributable, and either documents an admitted Core resource or declares a space-system application as its subject |

### Non-goals (product)

This collection does not attempt to:

- host or execute third-party code;
- provide user accounts, submission workflows, or a hosted API in v0.1;
- rank or score resources automatically;
- offer AI/ML-based semantic search.

These are product decisions, not statements about resource admission.
