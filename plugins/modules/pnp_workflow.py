#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
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
version_added: '1.0'
author: first last (@GitHubID)
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
  cisco.dnac.pnp_workflow
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    limit: 1  #  integer
    name: SomeValue  # string
    offset: 1  #  integer
    sort: SomeValue  # string
    sort_order: SomeValue  # string
    type: SomeValue  # string
  delegate_to: localhost
  register: query_result
  
- name: add_a_workflow
  cisco.dnac.pnp_workflow
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
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
  delegate_to: localhost
  
- name: get_workflow_by_id
  cisco.dnac.pnp_workflow
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    id: SomeValue  # string, required
  delegate_to: localhost
  register: query_result
  
- name: delete_workflow_by_id
  cisco.dnac.pnp_workflow
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: delete  # required
    id: SomeValue  # string, required
  delegate_to: localhost
  
- name: update_workflow
  cisco.dnac.pnp_workflow
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
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
  delegate_to: localhost
  
- name: get_workflow_count
  cisco.dnac.pnp_workflow
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    count: True  # boolean, required
    name: SomeValue  # string
  delegate_to: localhost
  register: query_result
  
"""

RETURN = """
get_workflows:
    description: Returns the list of workflows based on filter criteria. If a limit is not specified, it will default to return 50 workflows. Pagination and sorting are also supported by this endpoint.
    returned: always
    type: dict
    contains:
    payload:
      description: It is the pnp workflow's payload.
      returned: always
      type: list
      contains:
        _id:
          description: It is the pnp workflow's _id.
          returned: always
          type: str
          sample: '<_id>'
        state:
          description: It is the pnp workflow's state.
          returned: always
          type: str
          sample: '<state>'
        type:
          description: It is the pnp workflow's type.
          returned: always
          type: str
          sample: '<type>'
        description:
          description: It is the pnp workflow's description.
          returned: always
          type: str
          sample: '<description>'
        lastupdateOn:
          description: It is the pnp workflow's lastupdateOn.
          returned: always
          type: int
          sample: 0
        imageId:
          description: It is the pnp workflow's imageId.
          returned: always
          type: str
          sample: '<imageid>'
        currTaskIdx:
          description: It is the pnp workflow's currTaskIdx.
          returned: always
          type: int
          sample: 0
        addedOn:
          description: It is the pnp workflow's addedOn.
          returned: always
          type: int
          sample: 0
        tasks:
          description: It is the pnp workflow's tasks.
          returned: always
          type: list
          contains:
            state:
              description: It is the pnp workflow's state.
              returned: always
              type: str
              sample: '<state>'
            type:
              description: It is the pnp workflow's type.
              returned: always
              type: str
              sample: '<type>'
            currWorkItemIdx:
              description: It is the pnp workflow's currWorkItemIdx.
              returned: always
              type: int
              sample: 0
            taskSeqNo:
              description: It is the pnp workflow's taskSeqNo.
              returned: always
              type: int
              sample: 0
            endTime:
              description: It is the pnp workflow's endTime.
              returned: always
              type: int
              sample: 0
            startTime:
              description: It is the pnp workflow's startTime.
              returned: always
              type: int
              sample: 0
            workItemList:
              description: It is the pnp workflow's workItemList.
              returned: always
              type: list
              contains:
                state:
                  description: It is the pnp workflow's state.
                  returned: always
                  type: str
                  sample: '<state>'
                command:
                  description: It is the pnp workflow's command.
                  returned: always
                  type: str
                  sample: '<command>'
                outputStr:
                  description: It is the pnp workflow's outputStr.
                  returned: always
                  type: str
                  sample: '<outputstr>'
                endTime:
                  description: It is the pnp workflow's endTime.
                  returned: always
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp workflow's startTime.
                  returned: always
                  type: int
                  sample: 0
                timeTaken:
                  description: It is the pnp workflow's timeTaken.
                  returned: always
                  type: int
                  sample: 0

            timeTaken:
              description: It is the pnp workflow's timeTaken.
              returned: always
              type: int
              sample: 0
            name:
              description: It is the pnp workflow's name.
              returned: always
              type: str
              sample: '<name>'

        addToInventory:
          description: It is the pnp workflow's addToInventory.
          returned: always
          type: bool
          sample: false
        instanceType:
          description: It is the pnp workflow's instanceType.
          returned: always
          type: str
          sample: '<instancetype>'
        endTime:
          description: It is the pnp workflow's endTime.
          returned: always
          type: int
          sample: 0
        execTime:
          description: It is the pnp workflow's execTime.
          returned: always
          type: int
          sample: 0
        startTime:
          description: It is the pnp workflow's startTime.
          returned: always
          type: int
          sample: 0
        useState:
          description: It is the pnp workflow's useState.
          returned: always
          type: str
          sample: '<usestate>'
        configId:
          description: It is the pnp workflow's configId.
          returned: always
          type: str
          sample: '<configid>'
        name:
          description: It is the pnp workflow's name.
          returned: always
          type: str
          sample: '<name>'
        version:
          description: It is the pnp workflow's version.
          returned: always
          type: int
          sample: 0
        tenantId:
          description: It is the pnp workflow's tenantId.
          returned: always
          type: str
          sample: '<tenantid>'


add_a_workflow:
    description: Adds a PnP Workflow along with the relevant tasks in the workflow into the PnP database.
    returned: success
    type: dict
    contains:
    _id:
      description: Workflow's Id.
      returned: success
      type: str
      sample: '<_id>'
    state:
      description: Workflow's State.
      returned: success
      type: str
      sample: '<state>'
    type:
      description: Workflow's Type.
      returned: success
      type: str
      sample: '<type>'
    description:
      description: Workflow's Description.
      returned: success
      type: str
      sample: '<description>'
    lastupdateOn:
      description: Workflow's lastupdateOn.
      returned: success
      type: int
      sample: 0
    imageId:
      description: Workflow's Image Id.
      returned: success
      type: str
      sample: '<imageid>'
    currTaskIdx:
      description: Workflow's currTaskIdx.
      returned: success
      type: int
      sample: 0
    addedOn:
      description: Workflow's addedOn.
      returned: success
      type: int
      sample: 0
    tasks:
      description: Workflow's Tasks (list of objects).
      returned: success
      type: list
      contains:
        state:
          description: It is the pnp workflow's state.
          returned: success
          type: str
          sample: '<state>'
        type:
          description: It is the pnp workflow's type.
          returned: success
          type: str
          sample: '<type>'
        currWorkItemIdx:
          description: It is the pnp workflow's currWorkItemIdx.
          returned: success
          type: int
          sample: 0
        taskSeqNo:
          description: It is the pnp workflow's taskSeqNo.
          returned: success
          type: int
          sample: 0
        endTime:
          description: It is the pnp workflow's endTime.
          returned: success
          type: int
          sample: 0
        startTime:
          description: It is the pnp workflow's startTime.
          returned: success
          type: int
          sample: 0
        workItemList:
          description: It is the pnp workflow's workItemList.
          returned: success
          type: list
          contains:
            state:
              description: It is the pnp workflow's state.
              returned: success
              type: str
              sample: '<state>'
            command:
              description: It is the pnp workflow's command.
              returned: success
              type: str
              sample: '<command>'
            outputStr:
              description: It is the pnp workflow's outputStr.
              returned: success
              type: str
              sample: '<outputstr>'
            endTime:
              description: It is the pnp workflow's endTime.
              returned: success
              type: int
              sample: 0
            startTime:
              description: It is the pnp workflow's startTime.
              returned: success
              type: int
              sample: 0
            timeTaken:
              description: It is the pnp workflow's timeTaken.
              returned: success
              type: int
              sample: 0

        timeTaken:
          description: It is the pnp workflow's timeTaken.
          returned: success
          type: int
          sample: 0
        name:
          description: It is the pnp workflow's name.
          returned: success
          type: str
          sample: '<name>'

    addToInventory:
      description: Workflow's addToInventory.
      returned: success
      type: bool
      sample: false
    instanceType:
      description: Workflow's Instance Type.
      returned: success
      type: str
      sample: '<instancetype>'
    endTime:
      description: Workflow's endTime.
      returned: success
      type: int
      sample: 0
    execTime:
      description: Workflow's execTime.
      returned: success
      type: int
      sample: 0
    startTime:
      description: Workflow's startTime.
      returned: success
      type: int
      sample: 0
    useState:
      description: Workflow's Use State.
      returned: success
      type: str
      sample: '<usestate>'
    configId:
      description: Workflow's Config Id.
      returned: success
      type: str
      sample: '<configid>'
    name:
      description: Workflow's Name.
      returned: success
      type: str
      sample: '<name>'
    version:
      description: Workflow's version.
      returned: success
      type: int
      sample: 0
    tenantId:
      description: Workflow's Tenant Id.
      returned: success
      type: str
      sample: '<tenantid>'

get_workflow_by_id:
    description: Returns a workflow specified by id.
    returned: always
    type: dict
    contains:
    _id:
      description: Id, property of the response body.
      returned: always
      type: str
      sample: '<_id>'
    state:
      description: State, property of the response body.
      returned: always
      type: str
      sample: '<state>'
    type:
      description: Type, property of the response body.
      returned: always
      type: str
      sample: '<type>'
    description:
      description: Description, property of the response body.
      returned: always
      type: str
      sample: '<description>'
    lastupdateOn:
      description: LastupdateOn, property of the response body.
      returned: always
      type: int
      sample: 0
    imageId:
      description: Image Id, property of the response body.
      returned: always
      type: str
      sample: '<imageid>'
    currTaskIdx:
      description: CurrTaskIdx, property of the response body.
      returned: always
      type: int
      sample: 0
    addedOn:
      description: AddedOn, property of the response body.
      returned: always
      type: int
      sample: 0
    tasks:
      description: Tasks, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        state:
          description: It is the pnp workflow's state.
          returned: always
          type: str
          sample: '<state>'
        type:
          description: It is the pnp workflow's type.
          returned: always
          type: str
          sample: '<type>'
        currWorkItemIdx:
          description: It is the pnp workflow's currWorkItemIdx.
          returned: always
          type: int
          sample: 0
        taskSeqNo:
          description: It is the pnp workflow's taskSeqNo.
          returned: always
          type: int
          sample: 0
        endTime:
          description: It is the pnp workflow's endTime.
          returned: always
          type: int
          sample: 0
        startTime:
          description: It is the pnp workflow's startTime.
          returned: always
          type: int
          sample: 0
        workItemList:
          description: It is the pnp workflow's workItemList.
          returned: always
          type: list
          contains:
            state:
              description: It is the pnp workflow's state.
              returned: always
              type: str
              sample: '<state>'
            command:
              description: It is the pnp workflow's command.
              returned: always
              type: str
              sample: '<command>'
            outputStr:
              description: It is the pnp workflow's outputStr.
              returned: always
              type: str
              sample: '<outputstr>'
            endTime:
              description: It is the pnp workflow's endTime.
              returned: always
              type: int
              sample: 0
            startTime:
              description: It is the pnp workflow's startTime.
              returned: always
              type: int
              sample: 0
            timeTaken:
              description: It is the pnp workflow's timeTaken.
              returned: always
              type: int
              sample: 0

        timeTaken:
          description: It is the pnp workflow's timeTaken.
          returned: always
          type: int
          sample: 0
        name:
          description: It is the pnp workflow's name.
          returned: always
          type: str
          sample: '<name>'

    addToInventory:
      description: AddToInventory, property of the response body.
      returned: always
      type: bool
      sample: false
    instanceType:
      description: Instance Type, property of the response body.
      returned: always
      type: str
      sample: '<instancetype>'
    endTime:
      description: EndTime, property of the response body.
      returned: always
      type: int
      sample: 0
    execTime:
      description: ExecTime, property of the response body.
      returned: always
      type: int
      sample: 0
    startTime:
      description: StartTime, property of the response body.
      returned: always
      type: int
      sample: 0
    useState:
      description: Use State, property of the response body.
      returned: always
      type: str
      sample: '<usestate>'
    configId:
      description: Config Id, property of the response body.
      returned: always
      type: str
      sample: '<configid>'
    name:
      description: Name, property of the response body.
      returned: always
      type: str
      sample: '<name>'
    version:
      description: Version, property of the response body.
      returned: always
      type: int
      sample: 0
    tenantId:
      description: Tenant Id, property of the response body.
      returned: always
      type: str
      sample: '<tenantid>'

delete_workflow_by_id:
    description: Deletes a workflow specified by id.
    returned: success
    type: dict
    contains:
    _id:
      description: Id, property of the response body.
      returned: success
      type: str
      sample: '<_id>'
    state:
      description: State, property of the response body.
      returned: success
      type: str
      sample: '<state>'
    type:
      description: Type, property of the response body.
      returned: success
      type: str
      sample: '<type>'
    description:
      description: Description, property of the response body.
      returned: success
      type: str
      sample: '<description>'
    lastupdateOn:
      description: LastupdateOn, property of the response body.
      returned: success
      type: int
      sample: 0
    imageId:
      description: Image Id, property of the response body.
      returned: success
      type: str
      sample: '<imageid>'
    currTaskIdx:
      description: CurrTaskIdx, property of the response body.
      returned: success
      type: int
      sample: 0
    addedOn:
      description: AddedOn, property of the response body.
      returned: success
      type: int
      sample: 0
    tasks:
      description: Tasks, property of the response body (list of objects).
      returned: success
      type: list
      contains:
        state:
          description: It is the pnp workflow's state.
          returned: success
          type: str
          sample: '<state>'
        type:
          description: It is the pnp workflow's type.
          returned: success
          type: str
          sample: '<type>'
        currWorkItemIdx:
          description: It is the pnp workflow's currWorkItemIdx.
          returned: success
          type: int
          sample: 0
        taskSeqNo:
          description: It is the pnp workflow's taskSeqNo.
          returned: success
          type: int
          sample: 0
        endTime:
          description: It is the pnp workflow's endTime.
          returned: success
          type: int
          sample: 0
        startTime:
          description: It is the pnp workflow's startTime.
          returned: success
          type: int
          sample: 0
        workItemList:
          description: It is the pnp workflow's workItemList.
          returned: success
          type: list
          contains:
            state:
              description: It is the pnp workflow's state.
              returned: success
              type: str
              sample: '<state>'
            command:
              description: It is the pnp workflow's command.
              returned: success
              type: str
              sample: '<command>'
            outputStr:
              description: It is the pnp workflow's outputStr.
              returned: success
              type: str
              sample: '<outputstr>'
            endTime:
              description: It is the pnp workflow's endTime.
              returned: success
              type: int
              sample: 0
            startTime:
              description: It is the pnp workflow's startTime.
              returned: success
              type: int
              sample: 0
            timeTaken:
              description: It is the pnp workflow's timeTaken.
              returned: success
              type: int
              sample: 0

        timeTaken:
          description: It is the pnp workflow's timeTaken.
          returned: success
          type: int
          sample: 0
        name:
          description: It is the pnp workflow's name.
          returned: success
          type: str
          sample: '<name>'

    addToInventory:
      description: AddToInventory, property of the response body.
      returned: success
      type: bool
      sample: false
    instanceType:
      description: Instance Type, property of the response body.
      returned: success
      type: str
      sample: '<instancetype>'
    endTime:
      description: EndTime, property of the response body.
      returned: success
      type: int
      sample: 0
    execTime:
      description: ExecTime, property of the response body.
      returned: success
      type: int
      sample: 0
    startTime:
      description: StartTime, property of the response body.
      returned: success
      type: int
      sample: 0
    useState:
      description: Use State, property of the response body.
      returned: success
      type: str
      sample: '<usestate>'
    configId:
      description: Config Id, property of the response body.
      returned: success
      type: str
      sample: '<configid>'
    name:
      description: Name, property of the response body.
      returned: success
      type: str
      sample: '<name>'
    version:
      description: Version, property of the response body.
      returned: success
      type: int
      sample: 0
    tenantId:
      description: Tenant Id, property of the response body.
      returned: success
      type: str
      sample: '<tenantid>'

update_workflow:
    description: Updates an existing workflow.
    returned: changed
    type: dict
    contains:
    _id:
      description: Workflow's Id.
      returned: changed
      type: str
      sample: '<_id>'
    state:
      description: Workflow's State.
      returned: changed
      type: str
      sample: '<state>'
    type:
      description: Workflow's Type.
      returned: changed
      type: str
      sample: '<type>'
    description:
      description: Workflow's Description.
      returned: changed
      type: str
      sample: '<description>'
    lastupdateOn:
      description: Workflow's lastupdateOn.
      returned: changed
      type: int
      sample: 0
    imageId:
      description: Workflow's Image Id.
      returned: changed
      type: str
      sample: '<imageid>'
    currTaskIdx:
      description: Workflow's currTaskIdx.
      returned: changed
      type: int
      sample: 0
    addedOn:
      description: Workflow's addedOn.
      returned: changed
      type: int
      sample: 0
    tasks:
      description: Workflow's Tasks (list of objects).
      returned: changed
      type: list
      contains:
        state:
          description: It is the pnp workflow's state.
          returned: changed
          type: str
          sample: '<state>'
        type:
          description: It is the pnp workflow's type.
          returned: changed
          type: str
          sample: '<type>'
        currWorkItemIdx:
          description: It is the pnp workflow's currWorkItemIdx.
          returned: changed
          type: int
          sample: 0
        taskSeqNo:
          description: It is the pnp workflow's taskSeqNo.
          returned: changed
          type: int
          sample: 0
        endTime:
          description: It is the pnp workflow's endTime.
          returned: changed
          type: int
          sample: 0
        startTime:
          description: It is the pnp workflow's startTime.
          returned: changed
          type: int
          sample: 0
        workItemList:
          description: It is the pnp workflow's workItemList.
          returned: changed
          type: list
          contains:
            state:
              description: It is the pnp workflow's state.
              returned: changed
              type: str
              sample: '<state>'
            command:
              description: It is the pnp workflow's command.
              returned: changed
              type: str
              sample: '<command>'
            outputStr:
              description: It is the pnp workflow's outputStr.
              returned: changed
              type: str
              sample: '<outputstr>'
            endTime:
              description: It is the pnp workflow's endTime.
              returned: changed
              type: int
              sample: 0
            startTime:
              description: It is the pnp workflow's startTime.
              returned: changed
              type: int
              sample: 0
            timeTaken:
              description: It is the pnp workflow's timeTaken.
              returned: changed
              type: int
              sample: 0

        timeTaken:
          description: It is the pnp workflow's timeTaken.
          returned: changed
          type: int
          sample: 0
        name:
          description: It is the pnp workflow's name.
          returned: changed
          type: str
          sample: '<name>'

    addToInventory:
      description: Workflow's addToInventory.
      returned: changed
      type: bool
      sample: false
    instanceType:
      description: Workflow's Instance Type.
      returned: changed
      type: str
      sample: '<instancetype>'
    endTime:
      description: Workflow's endTime.
      returned: changed
      type: int
      sample: 0
    execTime:
      description: Workflow's execTime.
      returned: changed
      type: int
      sample: 0
    startTime:
      description: Workflow's startTime.
      returned: changed
      type: int
      sample: 0
    useState:
      description: Workflow's Use State.
      returned: changed
      type: str
      sample: '<usestate>'
    configId:
      description: Workflow's Config Id.
      returned: changed
      type: str
      sample: '<configid>'
    name:
      description: Workflow's Name.
      returned: changed
      type: str
      sample: '<name>'
    version:
      description: Workflow's version.
      returned: changed
      type: int
      sample: 0
    tenantId:
      description: Workflow's Tenant Id.
      returned: changed
      type: str
      sample: '<tenantid>'

get_workflow_count:
    description: Returns the workflow count.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: int
      sample: 0

"""
