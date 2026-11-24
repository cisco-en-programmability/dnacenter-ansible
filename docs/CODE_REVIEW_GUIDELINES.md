# Code review and development guidelines

These guidelines apply to Ansible modules, action plugins, shared helpers, and
playbooks in the `cisco.dnac` collection. Contributors and reviewers
should use them to check correctness, idempotency, security, compatibility,
readability, logging, documentation, and test coverage.

## Applying the guidelines

Apply the relevant requirements to the contribution being developed or reviewed.
Read related code and tests when needed to understand the behavior. Preserve
existing public contracts and supported API behavior when suggesting changes.
Avoid expanding a focused contribution into unrelated cleanup.

Requirements using **must** or **never** describe required behavior. Guidance
using **prefer** describes a recommendation to weigh against clarity,
compatibility, and the surrounding code. A valid alternative is not a syntax
error. Existing code is useful context, but does not override correctness or
security requirements.

During review, report confirmed defects separately from optional improvements.
For each finding, give a severity, file and line reference, triggering condition,
impact, relevant guideline, and an actionable recommendation. Explain expected
and actual behavior for defects. Report checks performed and verification gaps.
A review does not authorize changes to the code being reviewed.

## 1 Core guidelines

### 1.1 Code structure and readability

- Keep logic linear and easy to follow.
- Prefer early returns to reduce nesting only when exiting the whole method
  preserves its intended behavior. Do not skip later workflow steps.
- Extract helpers when logic is reused or the main flow becomes hard to read.
  Avoid splitting simple logic without a clear benefit.
- Avoid redundant checks, repeated lookups, and repeated API calls.
- Store frequently reused nested values in local variables instead of repeating
  chained `.get()` calls. Validate nested types before using dictionary methods.
- Use descriptive names for functions, variables, and results.
- Use "Catalyst Center" in user-facing text. Preserve legacy terms in API fields,
  SDK identifiers, existing public parameters, and compatibility references when
  changing them would be inaccurate or break callers.

### 1.2 Idempotency

- Modules must not report changes when the desired state is already met.
- Compare current and desired state before create, update, or delete operations.
- Report `changed=True` only for actual changes, or predicted changes in supported
  check mode. Keep `changed` and applicable `failed` results Boolean.
- Treat deletion of a confirmed non-existent resource as a successful no-op with
  `changed=False`.
- Never treat authentication, permission, timeout, or other retrieval failures as
  proof that a resource is absent.
- Use positive, state-based messages for no-op delete cases.

For example: `Template 'Onboard-Access' is already absent. Nothing to delete.`

Avoid describing confirmed absence as a failure, such as
`Unable to delete the item as it is not found.`

### 1.3 Performance and efficiency

- Minimize unnecessary API calls. Cache fetched state when it avoids repeated
  work, and refresh it when later operations require up-to-date state.
- Prefer bulk operations when supported by the API and consistent with the
  required error handling and per-resource results.
- Polling loops must have a timeout or another bounded exit condition.
- Use asynchronous or parallel work only when it materially improves throughput
  while preserving correctness, ordering requirements, and traceability.

## 2 Python module guidelines

### 2.1 Layout and formatting

- Use four spaces for indentation, with no tabs.
- Follow PEP 8 for spacing, naming, and readability. The collection's maximum
  Python code line length is 100 characters.
- Keep lines in YAML `DOCUMENTATION`, `EXAMPLES`, and `RETURN` blocks at 80
  characters or fewer.
- Use two blank lines around top-level classes and functions, and one blank line
  between methods in a class.
- Do not leave trailing whitespace.
- Use LF line endings and UTF-8 without a byte order mark.
- End files with a single newline.

### 2.2 Imports

- In Ansible modules, place normal imports below `DOCUMENTATION`, `EXAMPLES`, and
  `RETURN`. Preserve any required `__future__` imports in their valid position.
- Group imports as standard library, third-party, and collection-local imports.
- Prefer one import per line and absolute imports where practical.
- Preserve established handling of optional dependencies so missing dependencies
  produce useful module errors.

### 2.3 Naming conventions

- Use `snake_case` for variables and functions, `PascalCase` for classes, and
  `UPPER_CASE_WITH_UNDERSCORES` for constants.
- Avoid vague names such as `response1`, `result_msg_list_1`, or `rmkey`.
- Prefer names that describe the value, such as `response_device_details`,
  `device_provision_results`, `key_to_remove`, and `filtered_data`.
- Keep related counters and results consistent, such as `success_count` and
  `failed_count`.

### 2.4 Comments

- Add comments when the reason for a branch or operation is not obvious.
- Explain why the code exists, rather than narrating each line.
- Use sentence case and start ordinary comments with `# `.
- Avoid style-only rules that reduce readability without a clear benefit.

### 2.5 Error handling

- At the module boundary, use `module.exit_json()` for success and
  `module.fail_json()` for failures, directly or through the established wrapper.
- Helper and workflow classes may use the established project result object.
  Keep its structure consistent across code paths and propagate failures to the
  module boundary.
- Do not expose unhandled exceptions or raw tracebacks to users.
- Wrap API failures with actionable context. Include relevant identifiers only
  when they are safe to disclose.
- Return only selected, sanitized error details. Raw exception text can contain
  secrets, request headers, or payloads.
- Keep return types consistent. A function documented to return `bool` must
  return `True` or `False` on every normal return path.

For example:

```python
module.fail_json(
    msg="Failed to fetch the template. Check connectivity and permissions."
)
```

### 2.6 String formatting

- Avoid repeated string concatenation when formatting or joining values makes
  the code clearer.
- Prefer the formatting style already established in the file or module.
- Be consistent within a file and preserve supported Python versions.

### 2.7 Variable shadowing

- Never reuse an outer loop's index variable in a nested `enumerate()` loop.
- Use descriptive inner names such as `param_idx`, `device_idx`, `member_idx`, or
  `site_idx`.

Avoid:

```python
for idx, member in enumerate(members):
    for idx, param in enumerate(member["params"]):
        ...
```

Prefer:

```python
for member_idx, member in enumerate(members):
    for param_idx, param in enumerate(member["params"]):
        ...
```

## 3 Logging guidelines

### 3.1 General rules

- In modules, use `module.log()`. In existing helper or workflow classes, use the
  project's logging wrapper consistently. Do not use `print()` for diagnostics
  in module execution; it can corrupt the JSON result.
- Log actions and major decisions. A function name alone does not explain what
  happened or why.
- Log only selected, reviewed fields. Never log passwords, tokens, authorization
  headers, or raw request and response payloads.
- Custom logging wrappers must honor `module.no_log` and mask sensitive values.
  Do not assume `argument_spec` settings with `no_log=True` automatically protect
  a separate logging system.
- Log before and after external API calls when the call materially affects
  control flow or debugging.
- Log before `sleep()` or retry waits, with the reason and duration.
- Explain `continue`, `break`, or early returns in loops and validation flows
  when that reason helps debugging.
- Avoid excessive logging. Each message should add debugging value.

### 3.2 Log levels

| Level | Use |
| --- | --- |
| `DEBUG` | Selected, sanitized metadata, computed state, filters, and retries. |
| `INFO` | Major milestones, successful actions, and high-level progress. |
| `WARNING` | Recoverable or unexpected conditions. |
| `ERROR` or `CRITICAL` | Failed operations, according to their severity. |

Log levels do not make sensitive data safe. Apply the same protection at every
level and avoid duplicating severity prefixes in the message text.

### 3.3 Logging examples

These fragments assume an existing logging wrapper that honors `module.no_log`
and masks sensitive values:

```python
self.log("Validating site input for site_name='HQ'.", "DEBUG")
self.log("Calling 'get_site' for site name 'HQ'.", "DEBUG")
self.log(
    "Skipping device '192.0.2.10': management IP does not match the filter.",
    "INFO",
)
self.log("Polling task status; waiting 10 seconds before retrying.", "DEBUG")
```

Avoid messages such as `Entering get_site_id()` with no useful action context,
or an `INFO` message that starts with `Warning:`.

## 4 Documentation guidelines

### 4.1 Python docstrings

- Use docstrings for public modules, classes, functions, and methods.
- Prefer a consistent format with a short description, any necessary longer
  description, `Args`, and `Returns` as applicable.
- Describe actual runtime types, including optional values.
- Update all affected docstrings when parameter structures change.
- Return descriptions must match every normal return path.

### 4.2 YAML documentation blocks

- Keep `DOCUMENTATION` concise, accurate, action-oriented, and valid YAML.
- Include `module`, `short_description`, `description`, `version_added`, `options`,
  and `author`, as applicable to the module. Shared options may come from
  documentation fragments.
- Document `type`, `required`, `default`, `choices`, and `elements` where
  applicable. These values must match the argument specification and runtime
  behavior.
- Ensure each option description matches its actual type.
- When child options belong to a list of dictionaries, explain that users add
  multiple entries to the parent list.
- New parameters must explain their purpose, omitted behavior, and scope, with an
  example value where useful. For filters, state what is matched.
- Parent descriptions must summarize all child filtering capabilities.
- Avoid inline severity prefixes such as `Warning:` in option descriptions.
- Keep `RETURN` fields, types, and sample values consistent with the result.
- Document check mode support and any limits on its predictions.

### 4.3 Filter combination semantics

When multiple filters act on the same items, document:

- Whether different filter types combine with AND or OR logic.
- Whether multiple values within one type use AND or OR logic.
- The scope of each filter, including whether it applies only to its parent list
  entry.
- What omitted and explicitly empty filters mean, including any difference.
- Evaluation order and short-circuit behavior when they affect results or errors.

Explain the overall contract in the parent description and each child's role in
its option description. Demonstrate it in `EXAMPLES`. Methods that build or
consume the filters must describe the same behavior in their docstrings.

For an implementation that uses AND across types, OR within a type, and rejects
explicitly empty lists, a parent description could say:

> Filters apply within each list entry. A device must match any supplied IP
> address and any supplied hostname. An omitted filter type imposes no
> restriction. Explicitly empty filter lists are invalid.

This is an example contract. Describe the implementation's actual behavior;
do not change existing semantics merely to match this example.

### 4.4 Examples

- Give every example a unique, descriptive task name.
- Use valid YAML, realistic inputs, and idempotent usage where supported.
- When adding a filter, show it alone, combined with existing filters, and in a
  multi-entry example that demonstrates per-entry scope.
- Use fictional resource names, documentation IP addresses, and placeholders or
  variable references for credentials. Exclude internal-only links and local
  workstation paths from public examples.

These YAML lists have different meanings:

```yaml
---
# One string containing a comma; not two feature names.
features: ["port_assignments, port_channels"]
```

```yaml
---
# Two feature names.
features: ["port_assignments", "port_channels"]
```

## 5 Function and API design

### 5.1 Consistent return values

- All normal return paths must match the documented type and structure.
- If a function returns a tuple, preserve its arity and field meanings across
  branches.
- If a function returns `bool`, do not return `None` on another path.
- Include useful result data for both changed and unchanged outcomes.

### 5.2 Compatible method changes

- When adding parameters to shared methods, provide safe defaults when needed to
  preserve existing callers. Review positional and keyword callers.
- Preserve public parameter names, defaults, and behavior unless an intentional
  compatibility change follows the project's release process.

For example, an optional optimization input can preserve existing calls:

```python
# Before
def get_device_details_from_site(self, site_name):
    ...
```

```python
# After
def get_device_details_from_site(self, site_name, site_id=None):
    ...
```

### 5.3 Friendly names first

- Prefer human-readable public inputs such as `site_name` or `image_name`.
- Accept technical IDs as optional optimization inputs when helpful and
  compatible with the API contract.

### 5.4 Read and write operations

- Classify API operations by their actual effect.
- Do not mark read-only GET operations as modifying operations.
- Use `op_modifies=True` only for operations that modify state through wrappers
  that support this flag. Omit it only when the wrapper's default is read-only.
- Do not assume classifying an operation as a write automatically guards it in
  check mode. Verify the execution path.

For example, the collection's `_exec()` wrapper accepts an explicit read-only
classification:

```python
response = self.dnac._exec(
    family="devices",
    function="get_device_list",
    op_modifies=False,
    params={"management_ip_address": management_ip_address},
)
```

### 5.5 Polling loops

- Refresh task state inside the loop.
- Handle success, failure, timeout, and unexpected responses explicitly.
- Use a timeout or another bounded exit condition.
- Log the reason and duration before waiting.

## 6 Security and validation

- Never hardcode credentials or tokens in code, playbooks, fixtures, or examples.
  Use clearly identified placeholders or variable references in public examples.
- Mark sensitive parameters with `no_log=True`.
- Never expose secrets, authorization headers, raw sensitive payloads, or
  unsanitized exception details through logs or results.
- Validate input types, especially nested lists and dictionaries, before
  accessing their contents.
- Validate domain-specific constraints, ranges, and relationships where needed.
- Prefer `argument_spec` and Ansible's validation features for required
  parameters, types, choices, and supported parameter relationships. Use
  additional validation for constraints they cannot express.
- Preserve missing, empty, zero, and `False` values according to the input
  contract. Do not use truthiness as a substitute for validation.

## 7 Playbook guidelines

- Start YAML documents with `---` and use two-space indentation.
- Give every task a clear, action-oriented name.
- Prefer variables and defaults over hardcoded deployment values.
- Prefer a space inside Jinja delimiters, for example `{{ variable }}` and
  `{% if condition %}`, as checked by the ansible-lint `jinja[spacing]` rule.
  CI does not run ansible-lint on `tests/` or on the playbooks excluded in
  `.github/workflows/ansible-lint.yml`, so check those files during review.
- In a Jinja template that generates YAML, insert passwords and other free-form
  strings as `{{ value | to_json }}`, without surrounding quotes. Inside
  `"{{ value }}"`, a `"` or `\` in the value breaks the YAML or changes the
  value.
- Use `when`, `failed_when`, and `ignore_errors` deliberately. Do not hide failures
  that prevent the requested state from being achieved.
- Prefer tags as YAML lists for consistency. Scalar tags are valid Ansible
  syntax and must not be reported as syntax errors.
- Follow the surrounding directory's `.yml` or `.yaml` naming convention.

Preferred tag form:

```yaml
---
tags:
  - playbook
```

Also valid Ansible syntax:

```yaml
---
tags: playbook
```

## 8 Testing and sanity

- Before submitting code changes, run `ansible-test sanity` and the relevant
  tests. Reviewers should inspect available CI results and run focused checks
  when needed to verify a finding.
- Add or update tests for changed behavior, including relevant normal, edge,
  failure, and idempotency paths.
- Use realistic inputs and verify both changed and unchanged results explicitly.
- Use obvious placeholders such as `<password>` for secrets in fixtures and
  tests, even where other inputs are realistic. When the module validates a
  secret's format, choose a placeholder that still passes the rule, such as
  `<File_Password_1>`, or that still fails it in negative tests.
- When a module supports multiple backend API paths, cover affected older and
  newer paths without assuming their response structures are identical.
- For modules that support check mode, declare `supports_check_mode=True` and
  guard every mutating operation with `module.check_mode`, directly or through a
  verified shared implementation. Read-only calls may compute the plan.
- In check mode, predict whether a change is required without sending create,
  update, or delete requests. Document any limits on that prediction.
- Test supported check mode with both already-correct state and state requiring
  changes. Assert `changed` and verify that no mutating API calls occur.
- Do not declare check mode support unless the implementation provides it.
- Record the checks run, their results, and anything not verified. Missing tools
  or credentials must not be reported as passing checks.
- For documentation-only changes, check formatting, links, and affected examples.
  Run code tests when the change also affects executable behavior.

Run commands from the collection root, under
`ansible_collections/cisco/dnac`, using a supported `ansible-core`
environment. Container-based sanity checks require Docker or a supported
container runtime:

```bash
# All sanity checks, matching the container-based CI approach.
ansible-test sanity --docker

# Focus sanity checks on a module being changed.
ansible-test sanity plugins/modules/site_workflow_manager.py --docker
```

Use an isolated test environment for integration tests that modify Catalyst
Center resources, and identify those tests separately from local static checks.

## 9 Code review checklist

- [ ] Is the module idempotent, including confirmed no-op deletions?
- [ ] Are `changed=True` and `changed=False` both correct?
- [ ] Where check mode is supported, are writes prevented and predictions tested?
- [ ] Are required parameters and nested inputs validated appropriately?
- [ ] Are logs useful, safe, and correctly leveled?
- [ ] Are API calls necessary and correctly classified as reads or writes?
- [ ] Are polling loops bounded and refreshed on each iteration?
- [ ] Are return values consistent across all normal return paths?
- [ ] Do docstrings, `DOCUMENTATION`, `EXAMPLES`, and `RETURN` match the code?
- [ ] Do filter docs explain matching across types, within a type, per-entry
  scope, and omitted or empty filters?
- [ ] Are secrets protected with `no_log`, including custom logging wrappers?
- [ ] Do code, fixtures, examples, and sample playbooks use placeholders or variables
  instead of real-looking secrets?
- [ ] Are raw payloads and unsanitized exceptions excluded from logs and errors?
- [ ] Is duplicated logic removed or intentionally retained for clarity?
- [ ] Are public interfaces and supported backend paths compatible?
- [ ] Are relevant tests updated and sanity results available?

Mark items that do not apply as not applicable in review notes rather than
inventing findings or requiring unrelated changes.

## 10 Practical patterns and examples

The following fragments illustrate individual patterns. They assume surrounding
module setup and validation where stated.

### 10.1 Early returns and local variables

Extract repeated lookups without changing which later workflow steps execute.

Before:

```python
if self.want.get("lan_automation"):
    seed_ip_address = self.want.get("lan_automation").get(
        "primaryDeviceManagmentIPAddress"
    )
```

After validating `lan_automation` as an optional dictionary:

```python
lan_automation = self.want.get("lan_automation")
if lan_automation:
    seed_ip_address = lan_automation.get("primaryDeviceManagmentIPAddress")
# Continue with any remaining workflow steps.
```

An early return when `lan_automation` is absent is appropriate only if the whole
method handles LAN automation and no later work should run. The API field's
spelling is preserved intentionally.

### 10.2 Logging around API calls

Use meaningful milestones without exposing raw payloads. This fragment assumes
the logging wrapper honors `module.no_log` and masks sensitive values:

```python
self.log("Fetching the device list for the requested management IP.", "DEBUG")
response = self.dnac._exec(
    family="devices",
    function="get_device_list",
    op_modifies=False,
    params={"management_ip_address": management_ip_address},
)
self.log("Received the device list response.", "DEBUG")
```

Handle API failures with safe, actionable messages. If more detail is needed,
log only explicitly selected and sanitized metadata. Never use
`self.pprint(response)` to log the complete API response.

### 10.3 Optional integer values

An optional integer may be `int` or `None`; document both possibilities. Do not
use truthiness to detect missing numeric values.

Avoid:

```python
port = netflow_details.get("collector").get("port")
if port:
    port = int(port)
else:
    port = ""
```

After validating `netflow_details` and `collector` as dictionaries, and `port` as
an optional integer in the allowed range:

```python
collector = netflow_details.get("collector", {})
port = collector.get("port")
```

If the input contract also accepts numeric strings, validate and convert them
explicitly. Define how empty strings, explicit nulls, Boolean values, and
out-of-range values are handled. Do not silently treat every falsy value as
absent.

### 10.4 No-op delete behavior

When absence has been confirmed, return `changed=False` and a state-based message
such as:

```text
Requested item is already absent. Nothing to delete.
```

Authentication, permission, timeout, and other retrieval failures are not
evidence of absence and must follow the error path.

### 10.5 Preserving Boolean comparison semantics

Reorder conditions only when both the result and evaluation behavior remain
correct. Preserve an explicit `True` comparison unless validation guarantees a
Boolean.

Before:

```python
if not pool_values.get("ipv4PrefixLength") and pool_values.get("ipv4Prefix") is True:
    ...
```

For a validated dictionary with no side effects in these lookups, the following
preserves the Boolean test:

```python
if pool_values.get("ipv4Prefix") is True and not pool_values.get("ipv4PrefixLength"):
    ...
```

Replacing `is True` with a truthiness check also accepts values such as `1` and
non-empty strings, including `"false"`. Simplify only after validating or
normalizing the value as a Boolean. Separately define whether prefix length `0`
is valid; if it is, test explicitly for a missing value instead of using `not`.

## Ansible references

- [Module format and documentation](https://docs.ansible.com/projects/ansible/latest/dev_guide/developing_modules_documenting.html)
- [Module architecture and argument validation](https://docs.ansible.com/projects/ansible/latest/dev_guide/developing_program_flow_modules.html)
- [Sanity tests](https://docs.ansible.com/projects/ansible/latest/dev_guide/testing_sanity.html)
