# Repository guidance for coding agents

This repository contains the `cisco.dnac` Ansible collection. Read
[CONTRIBUTING.md](CONTRIBUTING.md) before changing code or reviewing contributions.

## Code review instructions

Whenever asked to review code in this repository, read
[the code review guidelines](docs/CODE_REVIEW_GUIDELINES.md) in full before
reviewing. Apply the relevant sections to the requested files, commit, branch, or
pull request.

- Establish the review scope and compare the requested changes against the
  appropriate base. Inspect related callers, helpers, documentation, and tests
  when needed to verify behavior.
- Prioritize correctness, idempotency, check mode where supported, security,
  compatibility, and accurate documentation. Apply style preferences in context.
- Focus findings on issues introduced or exposed by the changes. Avoid requiring
  unrelated refactors or broad renaming of existing code.
- For each finding, include its severity, file and line reference, triggering
  condition, impact, relevant guideline, and an actionable recommendation.
  Explain the expected and actual behavior for defects.
- Keep confirmed defects separate from optional improvements. Do not present a
  preference as a syntax error or invent findings to fill a checklist.
- Review without modifying files unless the user also asks for fixes. Do not
  commit, push, or publish review comments unless explicitly requested.
- Report which checks were run or which existing CI results were inspected.
  State any verification gaps; do not claim that unrun checks passed.
- If no defects are found, say so and identify any remaining testing gaps.

## Making changes

Follow the shared standards in
[the code review guidelines](docs/CODE_REVIEW_GUIDELINES.md). Preserve public
interfaces and established module or workflow patterns. Validate the change
using the relevant checks described in the guidelines.
