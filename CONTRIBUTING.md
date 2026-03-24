# Contributing

This document applies to the entire `cisco.dnac` collection and defines
the coding and code review standards for Ansible modules.

## Core Principles

- Follow Ansible core module development standards.
- Follow PEP 8 with a maximum of 100 characters per line.
- Keep YAML `DOCUMENTATION` blocks to a maximum of 80 characters per
  line.
- Code must be idempotent.
- Avoid unnecessary complexity.
- Use early returns for failure cases.
- Keep logic linear and easy to follow.

## Ansible Module Structure

- Use `AnsibleModule` properly with `argument_spec`.
- Validate required parameters via `argument_spec`, not manual checks.
- Use `supports_check_mode=True` where applicable.
- Respect `check_mode` and do not make changes in check mode.
- Always return:
  - `changed` (`bool`)
  - `failed` (`bool`) when applicable
  - meaningful result data
- Use `module.exit_json()` and `module.fail_json()`.
- Do not raise raw exceptions. Wrap errors using `fail_json()`.
- Ensure idempotency:
  - compare current state with desired state
  - set `changed=True` only when an actual change occurs

## Early Returns and Flow

- Use early return for:
  - validation failures
  - unsupported states
  - no-op and idempotent cases
- Avoid nested `if`/`else` blocks where possible.
- Keep execution flow sequential.

## Logging Standards

- Use `module.log()` for logging.
- Do not use `print()` or the Python `logging` module.
- Add an entry log describing the action.
- Log input parameters, excluding sensitive data.
- Do not log the function name directly.
- Logs must describe the action.
  - Example: `Validating VLAN configuration for vlan_id=10`
- Log major decision points.
- Log external API calls and why they are made.
- Never log passwords, tokens, or sensitive values.
- Logs must explain why an action is happening.

## Documentation Requirements

### `DOCUMENTATION` Block

The `DOCUMENTATION` block must include:

- `module`
- `short_description`
- `description`
- `version_added`
- `options` with `type`, `required`, `default`, and `choices` where
  applicable
- `author`

### `EXAMPLES` Block

- Keep examples minimal but meaningful.
- Demonstrate idempotent usage.

### `RETURN` Block

- Document returned fields.
- Include type and sample values.
- Keep lines at 80 characters or fewer.

### Documentation Rules

- Be concise and accurate.
- Keep descriptions clear and action-oriented.
- Avoid unnecessary verbosity.
- Follow consistent formatting across modules.

## API Review Instructions

- Review only the API logic.
- In function docstrings include only:
  - short description
  - long description
  - `Args`
  - `Returns`
- Do not include extra explanation.

## Code Quality and Maintainability

- Avoid redundant key lookups.
- Avoid repeated validations.
- Use helper functions only if they are reusable.
- Do not split logic unnecessarily.
- Keep state comparison clean and explicit.
- Suggest better naming if unclear, but do not modify directly.
- Ensure consistent naming patterns such as `success_count` and
  `failed_count`.

## Error Handling

- Use `fail_json(msg=..., details=...)` where helpful.
- Provide actionable error messages.
- Include relevant identifiers in errors.
- Avoid generic error messages.

## Security Considerations

- Mark sensitive parameters with `no_log=True`.
- Never log sensitive data.
- Avoid exposing secrets in return values.
- Validate input types strictly.

## Performance and Scalability

- Avoid unnecessary API calls.
- Cache fetched state when possible.
- Minimize repeated lookups.
- Prefer bulk operations when supported.

## Suggestions Policy

When suggesting improvements during review, suggestions may cover:

- refactoring
- optimization
- documentation
- tests
- security
- performance
- readability
- maintainability
- scalability
- compatibility
- best practices
- design patterns
- architecture
- conventions
- anti-patterns

Suggestions must:

- be clear and actionable
- not directly modify original code
- preserve structure unless reuse justifies refactoring
