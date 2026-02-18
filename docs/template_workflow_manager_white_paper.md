# White Paper: `template_workflow_manager` Module

## Executive Summary

The `cisco.dnac.template_workflow_manager` Ansible module provides an orchestration layer for Cisco Catalyst Center template lifecycle management. It consolidates multiple operational concerns into a single workflow entry point:

- Project lifecycle (create, update, delete)
- Configuration template lifecycle (create, update, commit, delete)
- Template import/export operations
- Template deployment to devices
- Optional post-change verification (`config_verify`)
- Network profile attach/detach workflows for CLI templates (version-gated)

This module is designed for day-2 operations where consistency, idempotency, and controlled task polling are required across large template estates.

## Problem Statement

Template operations in Catalyst Center are not a single API call in practice. Common enterprise workflows require chained operations:

- Ensure a project exists
- Create or update a template
- Commit/version it
- Optionally bind profiles
- Deploy with device- or site-scoped targeting
- Verify final state

Without orchestration, each step becomes fragile and hard to standardize in playbooks. The `template_workflow_manager` module addresses this by composing these steps into deterministic state-driven execution.

## Module Scope

Primary source implementation: `plugins/modules/template_workflow_manager.py`

High-level states:

- `state: merged`
- `state: deleted`

Primary top-level config domains:

- `projects`
- `configuration_templates`
- `import`
- `export`
- `deploy_template`

## Architecture Overview

The module is implemented as class `Template(NetworkProfileFunctions)` and follows a predictable execution pipeline:

1. Validate input schema and semantic constraints
2. Build `have` (current Catalyst Center state)
3. Build `want` (desired state from playbook)
4. Execute state handler (`get_diff_merged` or `get_diff_deleted`)
5. Optionally verify (`verify_diff_merged` / `verify_diff_deleted`)

Core internal state containers:

- `self.have`: discovered current state
- `self.want`: desired normalized state
- `self.result`: structured operation output

## Version and Feature Gating

The module enforces runtime compatibility:

- Fails if Catalyst Center version is below `2.3.7.6` (entry guard in `main()`)
- Profile assignment/detachment flow requires Catalyst Center `>= 3.1.3.0`

Important implementation note:

- A legacy delete branch exists for `<= 2.3.5.3`, but this path is practically unreachable under the current minimum-version gate (`2.3.7.6`).

## Input Normalization and Validation

Validation is performed in two layers:

1. Structural validation via `validate_list_of_dicts` against `temp_spec`
2. Semantic validation via `input_data_validation()`

Key validations include:

- Required project/template identifiers in relevant flows
- Enforced enums (language, product family, software type, etc.)
- Profile feature availability based on Catalyst Center version
- File path existence and extension checks for template content files (`.j2`, `.txt`)
- Deploy-time requirement for template parameters

## `merged` State Behavior

### 1) Project Management (`projects`)

For each project entry:

- If `new_name` exists: update flow
- Else: create flow

Idempotency logic compares requested and existing project keys; if no effective delta exists, the module reports no change.

### 2) Template Management (`configuration_templates`)

Template flow includes:

- Project existence resolution
- Template existence and commit-pending status discovery
- Create or update decision
- Optional rename via `new_template_name` with duplicate-name check
- Conditional commit (`commit: true` by default)

Update detection relies on deep comparison of key fields plus dedicated handling of `containingTemplates`.

### 3) Profile Assignment (CLI Template + Network Profile)

When `profile_names` are provided and platform version allows:

- Profiles are retrieved with pagination by mapped profile category
- Each profile is validated for existence
- Assignment status is checked per profile
- Only non-assigned profiles are attached (idempotent behavior)

### 4) Import Operations (`import`)

Project import:

- Accepts `payload` or `project_file` (JSON)
- Skips already existing projects when payload-driven

Template import:

- Requires `project_name` to exist
- Accepts `payload` or `template_file` (JSON)
- Enforces alignment between global import `project_name` and template payload project

### 5) Export Operations (`export`)

- Project export by project name list
- Template export by resolving template IDs from `(project_name, template_name)` tuples

### 6) Deployment (`deploy_template`)

Device targeting supports two modes:

- Direct device selectors (`device_details`): priority `device_ips > device_hostnames > serial_numbers > mac_addresses`
- Site-scoped selectors (`site_provisioning_details`) with optional filters:
  - `device_family`
  - `device_role`
  - `device_tag` (intersection with site-assigned inventory)

Deployment payload composition includes:

- `forcePushTemplate`
- `isComposite`
- `copyingConfig`
- `targetInfo[]` with template parameter map
- Optional `resourceParams` supporting runtime-resolved types:
  - `MANAGED_DEVICE_UUID`
  - `MANAGED_DEVICE_IP`
  - `MANAGED_DEVICE_HOSTNAME`
  - `SITE_UUID`

The module polls task state and deployment state with timeout/poll-interval controls.

## `deleted` State Behavior

Delete flow supports:

- Template deletion by `template_name`
- Project deletion when template name is not provided and project is deletable
- Batch project deletion through `projects` list

For profile-capable environments (`>= 3.1.3.0`), associated profiles are detached before delete operations when applicable.

Explicit constraint:

- Deployment-based rollback/removal is not supported in deleted state.

## Idempotency Strategy

Idempotency is implemented through:

- Explicit `have`/`want` modeling
- Field-level equality checks (`dnac_compare_equality`)
- Short-circuit behavior when no change is required
- Commit checks for uncommitted templates
- Deployment short-circuit when backend reports "already deployed with same params"

## Observability and Operational Safety

The module provides robust operational telemetry via structured logs and task polling:

- Uses task ID retrieval and polling for asynchronous Catalyst Center operations
- Applies configurable timeout and poll interval:
  - `dnac_api_task_timeout` (default `1200`)
  - `dnac_task_poll_interval` (default `2`)
- Surfaces explicit messages for failure reason, missing resources, and invalid input

Result messaging aggregates outcomes across projects, templates, commits, profile assignment/detachment, import/export, and deploy.

## File-Based Template Content

`template_content_file_path` behavior:

- Accepted extensions: `.j2`, `.txt`
- File content source has priority over inline `template_content`
- Missing file or invalid extension fails fast

Implementation behavior currently reads file content directly and submits it in API payload. Operators should treat template rendering expectations according to their pipeline and Catalyst Center behavior.

## Test Coverage Summary

Primary unit test file: `tests/unit/modules/dnac/test_template_workflow_manager.py`

Covered flows include:

- Create template
- Update template
- Delete template
- Export project/template
- Import project/template
- Project create/update/delete sequences
- File-path-driven template content cases:
  - valid file path
  - invalid extension
  - missing file

Fixture-driven API response simulation is provided in `tests/unit/modules/dnac/fixtures/template_workflow_manager.json`.

## Recommended Usage Patterns

1. Use single-responsibility playbook tasks when possible (project lifecycle separate from deployment lifecycle) for easier rollback and observability.
2. Enable `config_verify: true` in production pipelines.
3. Pin and validate Catalyst Center version before profile operations.
4. Prefer explicit device targeting for change windows; use site/tag scoping for broad operational policies.
5. Keep template parameter naming consistent and treat runtime `resource_parameters` as deployment-time bindings.

## Known Constraints and Considerations

- Deleted state does not support removing device configuration through deployment semantics.
- Profile assignment/detachment is version-gated.
- Template import requires existing project context.
- Deployment success interpretation depends on backend task/deployment progress payload content.

## Conclusion

`template_workflow_manager` is a high-value orchestration module for Catalyst Center template operations, especially in enterprise environments where repeatability and operational safety matter. Its state-driven design, version checks, asynchronous task monitoring, and idempotent behavior make it suitable for CI/CD pipelines and controlled network automation at scale.
