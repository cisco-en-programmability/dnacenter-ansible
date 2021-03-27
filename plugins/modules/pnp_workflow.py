#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: pnp_workflow
short_description: Manage PnpWorkflow objects of DeviceOnboardingPnp
description:
- Returns the list of workflows based on filter criteria. If a limit is not specified, it will default to return 50 workflows. Pagination and sorting are also supported by this endpoint.
- Adds a PnP Workflow along with the relevant tasks in the workflow into the PnP database.
- Returns a workflow specified by id.
- Deletes a workflow specified by id.
- Updates an existing workflow.
- Returns the workflow count.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  limit:
    description:
    - Limits number of results.
    type: int
  name:
    description:
    - Workflow Name.
    - Workflow's name.
    type: str
  offset:
    description:
    - Index of first result.
    type: int
  sort:
    description:
    - Comma seperated lost of fields to sort on.
    type: str
  sort_order:
    description:
    - Sort Order Ascending (asc) or Descending (des).
    type: str
  type:
    description:
    - Workflow Type.
    - Workflow's type.
    type: str
  _id:
    description:
    - Workflow's _id.
    type: str
  addToInventory:
    description:
    - Workflow's addToInventory.
    type: bool
  addedOn:
    description:
    - Workflow's addedOn.
    type: int
  configId:
    description:
    - Workflow's configId.
    type: str
  currTaskIdx:
    description:
    - Workflow's currTaskIdx.
    type: int
  description:
    description:
    - Workflow's description.
    type: str
  endTime:
    description:
    - Workflow's endTime.
    type: int
  execTime:
    description:
    - Workflow's execTime.
    type: int
  imageId:
    description:
    - Workflow's imageId.
    type: str
  instanceType:
    description:
    - Workflow's instanceType.
    type: str
  lastupdateOn:
    description:
    - Workflow's lastupdateOn.
    type: int
  startTime:
    description:
    - Workflow's startTime.
    type: int
  state:
    description:
    - Workflow's state.
    type: str
  tasks:
    description:
    - Workflow's tasks (list of objects).
    type: list
    elements: dict
    suboptions:
      currWorkItemIdx:
        description:
        - It is the pnp workflow's currWorkItemIdx.
        type: int
      endTime:
        description:
        - It is the pnp workflow's endTime.
        type: int
      name:
        description:
        - It is the pnp workflow's name.
        type: str
      startTime:
        description:
        - It is the pnp workflow's startTime.
        type: int
      state:
        description:
        - It is the pnp workflow's state.
        type: str
      taskSeqNo:
        description:
        - It is the pnp workflow's taskSeqNo.
        type: int
      timeTaken:
        description:
        - It is the pnp workflow's timeTaken.
        type: int
      type:
        description:
        - It is the pnp workflow's type.
        type: str
      workItemList:
        description:
        - It is the pnp workflow's workItemList.
        type: list
        elements: dict
        suboptions:
          command:
            description:
            - It is the pnp workflow's command.
            type: str
          endTime:
            description:
            - It is the pnp workflow's endTime.
            type: int
          outputStr:
            description:
            - It is the pnp workflow's outputStr.
            type: str
          startTime:
            description:
            - It is the pnp workflow's startTime.
            type: int
          state:
            description:
            - It is the pnp workflow's state.
            type: str
          timeTaken:
            description:
            - It is the pnp workflow's timeTaken.
            type: int


  tenantId:
    description:
    - Workflow's tenantId.
    type: str
  useState:
    description:
    - Workflow's useState.
    type: str
  version:
    description:
    - Workflow's version.
    type: int
  id:
    description:
    - Id path parameter.
    type: str
    required: True
  count:
    description:
    - If true gets the number of objects.
    - Required for state query.
    type: bool

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.pnp_workflow
# Reference by Internet resource
- name: PnpWorkflow reference
  description: Complete reference of the PnpWorkflow object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: PnpWorkflow reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_workflows
  cisco.dnac.pnp_workflow:
    state: query  # required
    limit: 1  #  integer
    name: SomeValue  # string
    offset: 1  #  integer
    sort: SomeValue  # string
    sort_order: SomeValue  # string
    type: SomeValue  # string
  register: query_result

- name: add_a_workflow
  cisco.dnac.pnp_workflow:
    state: create  # required
    _id: SomeValue  # string
    addToInventory: True  # boolean
    addedOn: 1  #  integer
    configId: SomeValue  # string
    currTaskIdx: 1  #  integer
    description: SomeValue  # string
    endTime: 1  #  integer
    execTime: 1  #  integer
    imageId: SomeValue  # string
    instanceType: SomeValue  # string, valid values: 'SystemWorkflow', 'UserWorkflow', 'SystemResetWorkflow'.
    lastupdateOn: 1  #  integer
    name: SomeValue  # string
    startTime: 1  #  integer
    state: SomeValue  # string
    tasks:
    - currWorkItemIdx: 1  #  integer
      endTime: 1  #  integer
      name: SomeValue  # string
      startTime: 1  #  integer
      state: SomeValue  # string
      taskSeqNo: 1  #  integer
      timeTaken: 1  #  integer
      type: SomeValue  # string
      workItemList:
      - command: SomeValue  # string
        endTime: 1  #  integer
        outputStr: SomeValue  # string
        startTime: 1  #  integer
        state: SomeValue  # string
        timeTaken: 1  #  integer
    tenantId: SomeValue  # string
    type: SomeValue  # string
    useState: SomeValue  # string
    version: 1  #  integer

- name: get_workflow_by_id
  cisco.dnac.pnp_workflow:
    state: query  # required
    id: SomeValue  # string, required
  register: query_result

- name: delete_workflow_by_id
  cisco.dnac.pnp_workflow:
    state: delete  # required
    id: SomeValue  # string, required

- name: update_workflow
  cisco.dnac.pnp_workflow:
    state: update  # required
    id: SomeValue  # string, required
    _id: SomeValue  # string
    addToInventory: True  # boolean
    addedOn: 1  #  integer
    configId: SomeValue  # string
    currTaskIdx: 1  #  integer
    description: SomeValue  # string
    endTime: 1  #  integer
    execTime: 1  #  integer
    imageId: SomeValue  # string
    instanceType: SomeValue  # string, valid values: 'SystemWorkflow', 'UserWorkflow', 'SystemResetWorkflow'.
    lastupdateOn: 1  #  integer
    name: SomeValue  # string
    startTime: 1  #  integer
    state: SomeValue  # string
    tasks:
    - currWorkItemIdx: 1  #  integer
      endTime: 1  #  integer
      name: SomeValue  # string
      startTime: 1  #  integer
      state: SomeValue  # string
      taskSeqNo: 1  #  integer
      timeTaken: 1  #  integer
      type: SomeValue  # string
      workItemList:
      - command: SomeValue  # string
        endTime: 1  #  integer
        outputStr: SomeValue  # string
        startTime: 1  #  integer
        state: SomeValue  # string
        timeTaken: 1  #  integer
    tenantId: SomeValue  # string
    type: SomeValue  # string
    useState: SomeValue  # string
    version: 1  #  integer

- name: get_workflow_count
  cisco.dnac.pnp_workflow:
    state: query  # required
    count: True  # boolean, required
    name: SomeValue  # string
  register: query_result

"""

RETURN = """
"""
