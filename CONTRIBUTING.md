Contributions to the `cisco.dnac` Ansible collection are welcome.
Use the [code review and development guidelines](docs/CODE_REVIEW_GUIDELINES.md)
for the shared coding standards, examples, testing expectations, and review
checklist. They apply to modules, action plugins, shared helpers, and
playbooks.

## Preparing a contribution

1. Keep the change focused and explain the problem or desired behavior in the
   pull request.
2. Follow the shared guidelines and preserve public interfaces and supported API
   behavior.
3. Update affected documentation, examples, and tests with the implementation.
4. Run the relevant checks described in the
   [testing and sanity guidance](docs/CODE_REVIEW_GUIDELINES.md#8-testing-and-sanity).
   Include results and any verification gaps in the pull request.
5. Use the [pull request template](.github/PULL_REQUEST_TEMPLATE.md) and complete
   the applicable checklist items.

## Reviewing a contribution

Use the [review checklist](docs/CODE_REVIEW_GUIDELINES.md#9-code-review-checklist)
and apply the relevant detailed guidelines. Review correctness, idempotency,
security, compatibility, documentation, and tests within the contribution's
scope. Inspect related code when needed to verify behavior.

Keep findings specific and actionable, with severity, file and line references,
the triggering condition, impact, and a suggested correction. Separate confirmed
defects from optional improvements, and avoid unrelated refactoring requests.
Review feedback does not authorize changes to the contributor's code.

## Reviews with coding agents

[AGENTS.md](AGENTS.md) directs Codex and other agents that support this file to
read the shared guidelines whenever a code review is requested. Start the review
in the repository and identify the files, commit, branch, or pull request to
review. For example:

```text
Review my uncommitted changes using the repository's code review guidelines.
```

Tools that do not support `AGENTS.md` need their own configuration or an explicit
reference to the guidelines. The repository instructions guide requested
reviews; they do not schedule reviews or enable automatic pull request reviews.

## Code of conduct

All contributors must follow the project's
[Code of Conduct](README.md#code-of-conduct).
