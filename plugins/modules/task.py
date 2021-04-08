#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: task
short_description: Manage Task objects of Task
description:
- Returns Task(s) based on filter criteria.
- Returns a Task by specified id.
- Returns Task count.
- Returns root Tasks associated with an Operationid.
- Returns a Task with its children Tasks by based on their id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  data:
    description:
    - Fetch Tasks that contains this data.
    type: str
  end_time:
    description:
    - This is the epoch end time upto which audit records need to be fetched.
    type: str
  error_code:
    description:
    - Fetch Tasks that have this error code.
    type: str
  failure_reason:
    description:
    - Fetch Tasks that contains this failure reason.
    type: str
  is_error:
    description:
    - Fetch Tasks ended as success or failure. Valid values true, false.
    type: str
  limit:
    description:
    - Limit query parameter.
    - The maximum value of {limit} supported is 500. Base 1 indexing for {limit}, minimum value is 1.
    - Type str for state query.
    - Type int for state query.
    type: raw
  offset:
    description:
    - Offset query parameter.
    - Index, minimum value is 0.
    - Type str for state query.
    - Type int for state query.
    type: raw
  order:
    description:
    - Sort order - asc or dsc.
    type: str
  parent_id:
    description:
    - Fetch Tasks that have this parent Id.
    type: str
  progress:
    description:
    - Fetch Tasks that contains this progress.
    type: str
  service_type:
    description:
    - Fetch Tasks with this service type.
    type: str
  sort_by:
    description:
    - Sort results by this field.
    type: str
  start_time:
    description:
    - This is the epoch start time from which Tasks need to be fetched.
    type: str
  username:
    description:
    - Fetch Tasks with this username.
    type: str
  task_id:
    description:
    - UUID of the Task.
    type: str
    required: True
  count:
    description:
    - If true gets the number of objects.
    type: bool
    required: True
  operation_id:
    description:
    - OperationId path parameter.
    type: str
    required: True
  tree:
    description:
    - If true retrieves the Task tree.
    type: bool
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.task
# Reference by Internet resource
- name: Task reference
  description: Complete reference of the Task object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: Task reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_tasks
  cisco.dnac.task:
    state: query  # required
    data: SomeValue  # string
    end_time: SomeValue  # string
    error_code: SomeValue  # string
    failure_reason: SomeValue  # string
    is_error: SomeValue  # string
    limit: SomeValue  # string
    offset: SomeValue  # string
    order: SomeValue  # string
    parent_id: SomeValue  # string
    progress: SomeValue  # string
    service_type: SomeValue  # string
    sort_by: SomeValue  # string
    start_time: SomeValue  # string
    username: SomeValue  # string
  register: nm_get_tasks

- name: get_task_by_id
  cisco.dnac.task:
    state: query  # required
    task_id: SomeValue  # string, required
  register: nm_get_task_by_id

- name: get_task_count
  cisco.dnac.task:
    state: query  # required
    count: True  # boolean, required
    data: SomeValue  # string
    end_time: SomeValue  # string
    error_code: SomeValue  # string
    failure_reason: SomeValue  # string
    is_error: SomeValue  # string
    parent_id: SomeValue  # string
    progress: SomeValue  # string
    service_type: SomeValue  # string
    start_time: SomeValue  # string
    username: SomeValue  # string
  register: nm_get_task_count

- name: get_task_by_operationid
  cisco.dnac.task:
    state: query  # required
    limit: 1  #  integer, required
    offset: 1  #  integer, required
    operation_id: SomeValue  # string, required
  register: nm_get_task_by_operationid

- name: get_task_tree
  cisco.dnac.task:
    state: query  # required
    task_id: SomeValue  # string, required
    tree: True  # boolean, required
  register: nm_get_task_tree

"""

RETURN = r"""
dnac_response:
  description: A dictionary with the response returned by the DNA Center Python SDK
  returned: always
  type: dict
  sample: {"response": 29, "version": "1.0"}
sdk_function:
  description: The DNA Center SDK function used to execute the task
  returned: always
  type: str
  sample: task.get_task_by_id
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""
