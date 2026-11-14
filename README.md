# AI Arsenal

*A flexible registry for everything about AI from agent skills to research papers.*

## What is AI Arsenal?

AI Arsenal is an open-source project that aims to bring the fragmented world of AI engineering into a convenient, searchable and verifiable registry.

Getting access to the correct information requires traversing lots of sites, repos, journals, and communities. No matter whether an agent skill, an MCP server, an implementation of ML or a research paper, obtaining reliable sources may take quite some time.

AI Arsenal aims to make it more convenient for people by sorting all the relevant sources in one classification and verification system.

### Current Stage

Currently AI Arsenal is in its **M0 — Planning and Foundation** stage.

The first planned collection is dedicated to **AI and Machine Learning for Space Systems** and includes all sorts of research and engineering sources related to this field.

The project is under development and does not include any populated collections and user-facing interfaces. For now we are working on defining classification, scope and contribution guidelines for our collections.

### Long-Term Plans

Although the first collection will focus specifically on the needs of the space industry, the ultimate goal is much more ambitious.

Further collections can include:

- **Agent Ecosystem:** Agent skills, MCP servers, tools, frameworks, and workflows.
- **Machine Learning:** ML/DL architectures, implementations, libraries, and datasets.
- **Research:** Scientific papers, journals, publications, and technical reports.
- **AI Engineering:** Developer tools, inference engines, deployment options, and infrastructure.
- **Emerging Technologies:** Additional sources from AI community.

The goal is to slowly but steadily create a good enough registry without losing the quality and manageability of the resources included in it.

## Running Locally

You can clone the repo and setup the environment for developing locally.

```bash
git clone https://github.com/TempestTwilight/ai-arsenal
cd ai-arsenal
uv sync
```

### Developing

Before making the push to the repository make sure that all the validations are passed in the current project state.

```bash
uv run ruff check .
uv run ruff format --check .
uv run ty check
uv run pytest
```

All of them need to be passed successfully in order for the contribution to be reviewed.

## Documentation

Here are links to the documents which describe current structure of the project and it's plans:

- [Classification for Resource Collections](docs/resource_classification.md) — Describes classification system used in registry.
- [Scope of Individual Resource Collection](docs/scope.md) — Describes the objectives and boundaries of individual collections.

## Licensing

AI Arsenal employs two licensing models for different aspects of the project:

- Apache License 2.0 – for the source code.
- CC BY 4.0 International – for original registry metadata and contributions.

Third-party resources included in the AI Arsenal registry retain their own licensing terms. The mere fact that they are included in the registry does not mean that AI Arsenal claims ownership of them, licenses them, or approves of them.

Refer to the actual license files for the terms that apply.

## Contributing

Contributions, suggestions, fixes, and discussion are all welcome.

With the growth of the project, the contribution guidelines and verification processes will be used to ensure consistency and reliability of the collections.

If you would like to contribute to the formation of a well-structured AI engineering ecosystem, feel free to join us.