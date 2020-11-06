#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '0.0.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
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
        type: bool
        required: True

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
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Returns the list of workflows based on filter criteria. If a limit is not specified, it will default to return 50 workflows. Pagination and sorting are also supported by this endpoint.
    returned: success,changed,always
    type: list
    contains:
        _id:
            description: It is the pnp workflow's _id.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        state:
            description: It is the pnp workflow's state.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        type:
            description: It is the pnp workflow's type.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        description:
            description: It is the pnp workflow's description.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        lastupdateOn:
            description: It is the pnp workflow's lastupdateOn.
            returned: success,changed,always
            type: int
            sample: 0
        imageId:
            description: It is the pnp workflow's imageId.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        currTaskIdx:
            description: It is the pnp workflow's currTaskIdx.
            returned: success,changed,always
            type: int
            sample: 0
        addedOn:
            description: It is the pnp workflow's addedOn.
            returned: success,changed,always
            type: int
            sample: 0
        tasks:
            description: It is the pnp workflow's tasks.
            returned: success,changed,always
            type: list
            contains:
                state:
                    description: It is the pnp workflow's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the pnp workflow's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                currWorkItemIdx:
                    description: It is the pnp workflow's currWorkItemIdx.
                    returned: success,changed,always
                    type: int
                    sample: 0
                taskSeqNo:
                    description: It is the pnp workflow's taskSeqNo.
                    returned: success,changed,always
                    type: int
                    sample: 0
                endTime:
                    description: It is the pnp workflow's endTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                startTime:
                    description: It is the pnp workflow's startTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                workItemList:
                    description: It is the pnp workflow's workItemList.
                    returned: success,changed,always
                    type: list
                    contains:
                        state:
                            description: It is the pnp workflow's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        command:
                            description: It is the pnp workflow's command.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        outputStr:
                            description: It is the pnp workflow's outputStr.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        endTime:
                            description: It is the pnp workflow's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp workflow's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        timeTaken:
                            description: It is the pnp workflow's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0

                timeTaken:
                    description: It is the pnp workflow's timeTaken.
                    returned: success,changed,always
                    type: int
                    sample: 0
                name:
                    description: It is the pnp workflow's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        addToInventory:
            description: It is the pnp workflow's addToInventory.
            returned: success,changed,always
            type: bool
            sample: false
        instanceType:
            description: It is the pnp workflow's instanceType.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        endTime:
            description: It is the pnp workflow's endTime.
            returned: success,changed,always
            type: int
            sample: 0
        execTime:
            description: It is the pnp workflow's execTime.
            returned: success,changed,always
            type: int
            sample: 0
        startTime:
            description: It is the pnp workflow's startTime.
            returned: success,changed,always
            type: int
            sample: 0
        useState:
            description: It is the pnp workflow's useState.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        configId:
            description: It is the pnp workflow's configId.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        name:
            description: It is the pnp workflow's name.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        version:
            description: It is the pnp workflow's version.
            returned: success,changed,always
            type: int
            sample: 0
        tenantId:
            description: It is the pnp workflow's tenantId.
            returned: success,changed,always
            type: str
            sample: 'sample_string'


data_1:
    description: Adds a PnP Workflow along with the relevant tasks in the workflow into the PnP database.
    returned: success,changed,always
    type: dict
    contains:
        _id:
            description: Workflow's Id.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        state:
            description: Workflow's State.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        type:
            description: Workflow's Type.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        description:
            description: Workflow's Description.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        lastupdateOn:
            description: Workflow's lastupdateOn.
            returned: success,changed,always
            type: int
            sample: 0
        imageId:
            description: Workflow's Image Id.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        currTaskIdx:
            description: Workflow's currTaskIdx.
            returned: success,changed,always
            type: int
            sample: 0
        addedOn:
            description: Workflow's addedOn.
            returned: success,changed,always
            type: int
            sample: 0
        tasks:
            description: Workflow's Tasks (list of objects).
            returned: success,changed,always
            type: list
            contains:
                state:
                    description: It is the pnp workflow's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the pnp workflow's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                currWorkItemIdx:
                    description: It is the pnp workflow's currWorkItemIdx.
                    returned: success,changed,always
                    type: int
                    sample: 0
                taskSeqNo:
                    description: It is the pnp workflow's taskSeqNo.
                    returned: success,changed,always
                    type: int
                    sample: 0
                endTime:
                    description: It is the pnp workflow's endTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                startTime:
                    description: It is the pnp workflow's startTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                workItemList:
                    description: It is the pnp workflow's workItemList.
                    returned: success,changed,always
                    type: list
                    contains:
                        state:
                            description: It is the pnp workflow's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        command:
                            description: It is the pnp workflow's command.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        outputStr:
                            description: It is the pnp workflow's outputStr.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        endTime:
                            description: It is the pnp workflow's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp workflow's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        timeTaken:
                            description: It is the pnp workflow's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0

                timeTaken:
                    description: It is the pnp workflow's timeTaken.
                    returned: success,changed,always
                    type: int
                    sample: 0
                name:
                    description: It is the pnp workflow's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        addToInventory:
            description: Workflow's addToInventory.
            returned: success,changed,always
            type: bool
            sample: false
        instanceType:
            description: Workflow's Instance Type.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        endTime:
            description: Workflow's endTime.
            returned: success,changed,always
            type: int
            sample: 0
        execTime:
            description: Workflow's execTime.
            returned: success,changed,always
            type: int
            sample: 0
        startTime:
            description: Workflow's startTime.
            returned: success,changed,always
            type: int
            sample: 0
        useState:
            description: Workflow's Use State.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        configId:
            description: Workflow's Config Id.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        name:
            description: Workflow's Name.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        version:
            description: Workflow's version.
            returned: success,changed,always
            type: int
            sample: 0
        tenantId:
            description: Workflow's Tenant Id.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_2:
    description: Returns a workflow specified by id.
    returned: success,changed,always
    type: dict
    contains:
        _id:
            description: Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        state:
            description: State, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        type:
            description: Type, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        description:
            description: Description, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        lastupdateOn:
            description: LastupdateOn, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        imageId:
            description: Image Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        currTaskIdx:
            description: CurrTaskIdx, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        addedOn:
            description: AddedOn, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        tasks:
            description: Tasks, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                state:
                    description: It is the pnp workflow's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the pnp workflow's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                currWorkItemIdx:
                    description: It is the pnp workflow's currWorkItemIdx.
                    returned: success,changed,always
                    type: int
                    sample: 0
                taskSeqNo:
                    description: It is the pnp workflow's taskSeqNo.
                    returned: success,changed,always
                    type: int
                    sample: 0
                endTime:
                    description: It is the pnp workflow's endTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                startTime:
                    description: It is the pnp workflow's startTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                workItemList:
                    description: It is the pnp workflow's workItemList.
                    returned: success,changed,always
                    type: list
                    contains:
                        state:
                            description: It is the pnp workflow's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        command:
                            description: It is the pnp workflow's command.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        outputStr:
                            description: It is the pnp workflow's outputStr.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        endTime:
                            description: It is the pnp workflow's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp workflow's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        timeTaken:
                            description: It is the pnp workflow's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0

                timeTaken:
                    description: It is the pnp workflow's timeTaken.
                    returned: success,changed,always
                    type: int
                    sample: 0
                name:
                    description: It is the pnp workflow's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        addToInventory:
            description: AddToInventory, property of the response body.
            returned: success,changed,always
            type: bool
            sample: false
        instanceType:
            description: Instance Type, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        endTime:
            description: EndTime, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        execTime:
            description: ExecTime, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        startTime:
            description: StartTime, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        useState:
            description: Use State, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        configId:
            description: Config Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        name:
            description: Name, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        tenantId:
            description: Tenant Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_3:
    description: Deletes a workflow specified by id.
    returned: success,changed,always
    type: dict
    contains:
        _id:
            description: Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        state:
            description: State, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        type:
            description: Type, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        description:
            description: Description, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        lastupdateOn:
            description: LastupdateOn, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        imageId:
            description: Image Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        currTaskIdx:
            description: CurrTaskIdx, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        addedOn:
            description: AddedOn, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        tasks:
            description: Tasks, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                state:
                    description: It is the pnp workflow's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the pnp workflow's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                currWorkItemIdx:
                    description: It is the pnp workflow's currWorkItemIdx.
                    returned: success,changed,always
                    type: int
                    sample: 0
                taskSeqNo:
                    description: It is the pnp workflow's taskSeqNo.
                    returned: success,changed,always
                    type: int
                    sample: 0
                endTime:
                    description: It is the pnp workflow's endTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                startTime:
                    description: It is the pnp workflow's startTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                workItemList:
                    description: It is the pnp workflow's workItemList.
                    returned: success,changed,always
                    type: list
                    contains:
                        state:
                            description: It is the pnp workflow's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        command:
                            description: It is the pnp workflow's command.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        outputStr:
                            description: It is the pnp workflow's outputStr.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        endTime:
                            description: It is the pnp workflow's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp workflow's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        timeTaken:
                            description: It is the pnp workflow's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0

                timeTaken:
                    description: It is the pnp workflow's timeTaken.
                    returned: success,changed,always
                    type: int
                    sample: 0
                name:
                    description: It is the pnp workflow's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        addToInventory:
            description: AddToInventory, property of the response body.
            returned: success,changed,always
            type: bool
            sample: false
        instanceType:
            description: Instance Type, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        endTime:
            description: EndTime, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        execTime:
            description: ExecTime, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        startTime:
            description: StartTime, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        useState:
            description: Use State, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        configId:
            description: Config Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        name:
            description: Name, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        tenantId:
            description: Tenant Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_4:
    description: Updates an existing workflow.
    returned: success,changed,always
    type: dict
    contains:
        _id:
            description: Workflow's Id.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        state:
            description: Workflow's State.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        type:
            description: Workflow's Type.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        description:
            description: Workflow's Description.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        lastupdateOn:
            description: Workflow's lastupdateOn.
            returned: success,changed,always
            type: int
            sample: 0
        imageId:
            description: Workflow's Image Id.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        currTaskIdx:
            description: Workflow's currTaskIdx.
            returned: success,changed,always
            type: int
            sample: 0
        addedOn:
            description: Workflow's addedOn.
            returned: success,changed,always
            type: int
            sample: 0
        tasks:
            description: Workflow's Tasks (list of objects).
            returned: success,changed,always
            type: list
            contains:
                state:
                    description: It is the pnp workflow's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the pnp workflow's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                currWorkItemIdx:
                    description: It is the pnp workflow's currWorkItemIdx.
                    returned: success,changed,always
                    type: int
                    sample: 0
                taskSeqNo:
                    description: It is the pnp workflow's taskSeqNo.
                    returned: success,changed,always
                    type: int
                    sample: 0
                endTime:
                    description: It is the pnp workflow's endTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                startTime:
                    description: It is the pnp workflow's startTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                workItemList:
                    description: It is the pnp workflow's workItemList.
                    returned: success,changed,always
                    type: list
                    contains:
                        state:
                            description: It is the pnp workflow's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        command:
                            description: It is the pnp workflow's command.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        outputStr:
                            description: It is the pnp workflow's outputStr.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        endTime:
                            description: It is the pnp workflow's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp workflow's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        timeTaken:
                            description: It is the pnp workflow's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0

                timeTaken:
                    description: It is the pnp workflow's timeTaken.
                    returned: success,changed,always
                    type: int
                    sample: 0
                name:
                    description: It is the pnp workflow's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        addToInventory:
            description: Workflow's addToInventory.
            returned: success,changed,always
            type: bool
            sample: false
        instanceType:
            description: Workflow's Instance Type.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        endTime:
            description: Workflow's endTime.
            returned: success,changed,always
            type: int
            sample: 0
        execTime:
            description: Workflow's execTime.
            returned: success,changed,always
            type: int
            sample: 0
        startTime:
            description: Workflow's startTime.
            returned: success,changed,always
            type: int
            sample: 0
        useState:
            description: Workflow's Use State.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        configId:
            description: Workflow's Config Id.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        name:
            description: Workflow's Name.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        version:
            description: Workflow's version.
            returned: success,changed,always
            type: int
            sample: 0
        tenantId:
            description: Workflow's Tenant Id.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_5:
    description: Returns the workflow count.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.pnp_workflow import module_definition


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()
    
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
        required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "query":
        dnac.exec("get")

    elif state == "delete":
        dnac.exec("delete")

    elif state == "create":
        dnac.disable_validation()
        dnac.exec("post")

    elif state == "update":
        dnac.disable_validation()
        dnac.exec("put")

    dnac.exit_json()


if __name__ == "__main__":
    main()