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
    - Fetch Tasks ended as success or failure. Valid values: true, false.
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
  register: query_result
  
- name: get_task_by_id
  cisco.dnac.task:
    state: query  # required
    task_id: SomeValue  # string, required
  register: query_result
  
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
  register: query_result
  
- name: get_task_by_operationid
  cisco.dnac.task:
    state: query  # required
    limit: 1  #  integer, required
    offset: 1  #  integer, required
    operation_id: SomeValue  # string, required
  register: query_result
  
- name: get_task_tree
  cisco.dnac.task:
    state: query  # required
    task_id: SomeValue  # string, required
    tree: True  # boolean, required
  register: query_result
  
"""

RETURN = """
get_tasks:
    description: Returns Task(s) based on filter criteria.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        additionalStatusURL:
          description: It is the Task's additionalStatusURL.
          returned: always
          type: str
          sample: '<additionalstatusurl>'
        data:
          description: It is the Task's data.
          returned: always
          type: str
          sample: '<data>'
        endTime:
          description: It is the Task's endTime.
          returned: always
          type: str
          sample: '<endtime>'
        errorCode:
          description: It is the Task's errorCode.
          returned: always
          type: str
          sample: '<errorcode>'
        errorKey:
          description: It is the Task's errorKey.
          returned: always
          type: str
          sample: '<errorkey>'
        failureReason:
          description: It is the Task's failureReason.
          returned: always
          type: str
          sample: '<failurereason>'
        id:
          description: It is the Task's id.
          returned: always
          type: str
          sample: '478012'
        instanceTenantId:
          description: It is the Task's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        isError:
          description: It is the Task's isError.
          returned: always
          type: bool
          sample: false
        lastUpdate:
          description: It is the Task's lastUpdate.
          returned: always
          type: str
          sample: '<lastupdate>'
        operationIdList:
          description: It is the Task's operationIdList.
          returned: always
          type: dict
        parentId:
          description: It is the Task's parentId.
          returned: always
          type: str
          sample: '<parentid>'
        progress:
          description: It is the Task's progress.
          returned: always
          type: str
          sample: '<progress>'
        rootId:
          description: It is the Task's rootId.
          returned: always
          type: str
          sample: '<rootid>'
        serviceType:
          description: It is the Task's serviceType.
          returned: always
          type: str
          sample: '<servicetype>'
        startTime:
          description: It is the Task's startTime.
          returned: always
          type: str
          sample: '<starttime>'
        username:
          description: It is the Task's username.
          returned: always
          type: str
          sample: 'devnetuser'
        version:
          description: It is the Task's version.
          returned: always
          type: int
          sample: 0

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_task_by_id:
    description: Returns a Task by specified id.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: dict
      contains:
        additionalStatusURL:
          description: It is the Task's additionalStatusURL.
          returned: always
          type: str
          sample: '<additionalstatusurl>'
        data:
          description: It is the Task's data.
          returned: always
          type: str
          sample: '<data>'
        endTime:
          description: It is the Task's endTime.
          returned: always
          type: str
          sample: '<endtime>'
        errorCode:
          description: It is the Task's errorCode.
          returned: always
          type: str
          sample: '<errorcode>'
        errorKey:
          description: It is the Task's errorKey.
          returned: always
          type: str
          sample: '<errorkey>'
        failureReason:
          description: It is the Task's failureReason.
          returned: always
          type: str
          sample: '<failurereason>'
        id:
          description: It is the Task's id.
          returned: always
          type: str
          sample: '478012'
        instanceTenantId:
          description: It is the Task's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        isError:
          description: It is the Task's isError.
          returned: always
          type: bool
          sample: false
        lastUpdate:
          description: It is the Task's lastUpdate.
          returned: always
          type: str
          sample: '<lastupdate>'
        operationIdList:
          description: It is the Task's operationIdList.
          returned: always
          type: dict
        parentId:
          description: It is the Task's parentId.
          returned: always
          type: str
          sample: '<parentid>'
        progress:
          description: It is the Task's progress.
          returned: always
          type: str
          sample: '<progress>'
        rootId:
          description: It is the Task's rootId.
          returned: always
          type: str
          sample: '<rootid>'
        serviceType:
          description: It is the Task's serviceType.
          returned: always
          type: str
          sample: '<servicetype>'
        startTime:
          description: It is the Task's startTime.
          returned: always
          type: str
          sample: '<starttime>'
        username:
          description: It is the Task's username.
          returned: always
          type: str
          sample: 'devnetuser'
        version:
          description: It is the Task's version.
          returned: always
          type: int
          sample: 0

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_task_count:
    description: Returns Task count.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: int
      sample: 0
    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_task_by_operationid:
    description: Returns root Tasks associated with an Operationid.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        additionalStatusURL:
          description: It is the Task's additionalStatusURL.
          returned: always
          type: str
          sample: '<additionalstatusurl>'
        data:
          description: It is the Task's data.
          returned: always
          type: str
          sample: '<data>'
        endTime:
          description: It is the Task's endTime.
          returned: always
          type: str
          sample: '<endtime>'
        errorCode:
          description: It is the Task's errorCode.
          returned: always
          type: str
          sample: '<errorcode>'
        errorKey:
          description: It is the Task's errorKey.
          returned: always
          type: str
          sample: '<errorkey>'
        failureReason:
          description: It is the Task's failureReason.
          returned: always
          type: str
          sample: '<failurereason>'
        id:
          description: It is the Task's id.
          returned: always
          type: str
          sample: '478012'
        instanceTenantId:
          description: It is the Task's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        isError:
          description: It is the Task's isError.
          returned: always
          type: bool
          sample: false
        lastUpdate:
          description: It is the Task's lastUpdate.
          returned: always
          type: str
          sample: '<lastupdate>'
        operationIdList:
          description: It is the Task's operationIdList.
          returned: always
          type: dict
        parentId:
          description: It is the Task's parentId.
          returned: always
          type: str
          sample: '<parentid>'
        progress:
          description: It is the Task's progress.
          returned: always
          type: str
          sample: '<progress>'
        rootId:
          description: It is the Task's rootId.
          returned: always
          type: str
          sample: '<rootid>'
        serviceType:
          description: It is the Task's serviceType.
          returned: always
          type: str
          sample: '<servicetype>'
        startTime:
          description: It is the Task's startTime.
          returned: always
          type: str
          sample: '<starttime>'
        username:
          description: It is the Task's username.
          returned: always
          type: str
          sample: 'devnetuser'
        version:
          description: It is the Task's version.
          returned: always
          type: int
          sample: 0

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_task_tree:
    description: Returns a Task with its children Tasks by based on their id.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        additionalStatusURL:
          description: It is the Task's additionalStatusURL.
          returned: always
          type: str
          sample: '<additionalstatusurl>'
        data:
          description: It is the Task's data.
          returned: always
          type: str
          sample: '<data>'
        endTime:
          description: It is the Task's endTime.
          returned: always
          type: str
          sample: '<endtime>'
        errorCode:
          description: It is the Task's errorCode.
          returned: always
          type: str
          sample: '<errorcode>'
        errorKey:
          description: It is the Task's errorKey.
          returned: always
          type: str
          sample: '<errorkey>'
        failureReason:
          description: It is the Task's failureReason.
          returned: always
          type: str
          sample: '<failurereason>'
        id:
          description: It is the Task's id.
          returned: always
          type: str
          sample: '478012'
        instanceTenantId:
          description: It is the Task's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        isError:
          description: It is the Task's isError.
          returned: always
          type: bool
          sample: false
        lastUpdate:
          description: It is the Task's lastUpdate.
          returned: always
          type: str
          sample: '<lastupdate>'
        operationIdList:
          description: It is the Task's operationIdList.
          returned: always
          type: dict
        parentId:
          description: It is the Task's parentId.
          returned: always
          type: str
          sample: '<parentid>'
        progress:
          description: It is the Task's progress.
          returned: always
          type: str
          sample: '<progress>'
        rootId:
          description: It is the Task's rootId.
          returned: always
          type: str
          sample: '<rootid>'
        serviceType:
          description: It is the Task's serviceType.
          returned: always
          type: str
          sample: '<servicetype>'
        startTime:
          description: It is the Task's startTime.
          returned: always
          type: str
          sample: '<starttime>'
        username:
          description: It is the Task's username.
          returned: always
          type: str
          sample: 'devnetuser'
        version:
          description: It is the Task's version.
          returned: always
          type: int
          sample: 0

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

"""
