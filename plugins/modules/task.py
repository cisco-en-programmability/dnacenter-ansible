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
module: task
short_description: Manage Task objects of Task
description:
- Returns Task(s) based on filter criteria.
- Returns a Task by specified id.
- Returns Task count.
- Returns root Tasks associated with an Operationid.
- Returns a Task with its children Tasks by based on their id.
version_added: '1.0'
author: first last (@GitHubID)
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
        type: str
    offset:
        description:
        - Offset query parameter.
        type: str
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
"""

RETURN = r"""
data_0:
    description: Returns Task(s) based on filter criteria.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                additionalStatusURL:
                    description: It is the Task's additionalStatusURL.
                    returned: success,changed,always
                    type: str
                    sample: '<additionalstatusurl>'
                data:
                    description: It is the Task's data.
                    returned: success,changed,always
                    type: str
                    sample: '<data>'
                endTime:
                    description: It is the Task's endTime.
                    returned: success,changed,always
                    type: str
                    sample: '<endtime>'
                errorCode:
                    description: It is the Task's errorCode.
                    returned: success,changed,always
                    type: str
                    sample: '<errorcode>'
                errorKey:
                    description: It is the Task's errorKey.
                    returned: success,changed,always
                    type: str
                    sample: '<errorkey>'
                failureReason:
                    description: It is the Task's failureReason.
                    returned: success,changed,always
                    type: str
                    sample: '<failurereason>'
                id:
                    description: It is the Task's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
                instanceTenantId:
                    description: It is the Task's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: '<instancetenantid>'
                isError:
                    description: It is the Task's isError.
                    returned: success,changed,always
                    type: bool
                    sample: false
                lastUpdate:
                    description: It is the Task's lastUpdate.
                    returned: success,changed,always
                    type: str
                    sample: '<lastupdate>'
                operationIdList:
                    description: It is the Task's operationIdList.
                    returned: success,changed,always
                    type: dict
                parentId:
                    description: It is the Task's parentId.
                    returned: success,changed,always
                    type: str
                    sample: '<parentid>'
                progress:
                    description: It is the Task's progress.
                    returned: success,changed,always
                    type: str
                    sample: '<progress>'
                rootId:
                    description: It is the Task's rootId.
                    returned: success,changed,always
                    type: str
                    sample: '<rootid>'
                serviceType:
                    description: It is the Task's serviceType.
                    returned: success,changed,always
                    type: str
                    sample: '<servicetype>'
                startTime:
                    description: It is the Task's startTime.
                    returned: success,changed,always
                    type: str
                    sample: '<starttime>'
                username:
                    description: It is the Task's username.
                    returned: success,changed,always
                    type: str
                    sample: 'devnetuser'
                version:
                    description: It is the Task's version.
                    returned: success,changed,always
                    type: int
                    sample: 0

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_1:
    description: Returns a Task by specified id.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                additionalStatusURL:
                    description: It is the Task's additionalStatusURL.
                    returned: success,changed,always
                    type: str
                    sample: '<additionalstatusurl>'
                data:
                    description: It is the Task's data.
                    returned: success,changed,always
                    type: str
                    sample: '<data>'
                endTime:
                    description: It is the Task's endTime.
                    returned: success,changed,always
                    type: str
                    sample: '<endtime>'
                errorCode:
                    description: It is the Task's errorCode.
                    returned: success,changed,always
                    type: str
                    sample: '<errorcode>'
                errorKey:
                    description: It is the Task's errorKey.
                    returned: success,changed,always
                    type: str
                    sample: '<errorkey>'
                failureReason:
                    description: It is the Task's failureReason.
                    returned: success,changed,always
                    type: str
                    sample: '<failurereason>'
                id:
                    description: It is the Task's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
                instanceTenantId:
                    description: It is the Task's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: '<instancetenantid>'
                isError:
                    description: It is the Task's isError.
                    returned: success,changed,always
                    type: bool
                    sample: false
                lastUpdate:
                    description: It is the Task's lastUpdate.
                    returned: success,changed,always
                    type: str
                    sample: '<lastupdate>'
                operationIdList:
                    description: It is the Task's operationIdList.
                    returned: success,changed,always
                    type: dict
                parentId:
                    description: It is the Task's parentId.
                    returned: success,changed,always
                    type: str
                    sample: '<parentid>'
                progress:
                    description: It is the Task's progress.
                    returned: success,changed,always
                    type: str
                    sample: '<progress>'
                rootId:
                    description: It is the Task's rootId.
                    returned: success,changed,always
                    type: str
                    sample: '<rootid>'
                serviceType:
                    description: It is the Task's serviceType.
                    returned: success,changed,always
                    type: str
                    sample: '<servicetype>'
                startTime:
                    description: It is the Task's startTime.
                    returned: success,changed,always
                    type: str
                    sample: '<starttime>'
                username:
                    description: It is the Task's username.
                    returned: success,changed,always
                    type: str
                    sample: 'devnetuser'
                version:
                    description: It is the Task's version.
                    returned: success,changed,always
                    type: int
                    sample: 0

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_2:
    description: Returns Task count.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_3:
    description: Returns root Tasks associated with an Operationid.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                additionalStatusURL:
                    description: It is the Task's additionalStatusURL.
                    returned: success,changed,always
                    type: str
                    sample: '<additionalstatusurl>'
                data:
                    description: It is the Task's data.
                    returned: success,changed,always
                    type: str
                    sample: '<data>'
                endTime:
                    description: It is the Task's endTime.
                    returned: success,changed,always
                    type: str
                    sample: '<endtime>'
                errorCode:
                    description: It is the Task's errorCode.
                    returned: success,changed,always
                    type: str
                    sample: '<errorcode>'
                errorKey:
                    description: It is the Task's errorKey.
                    returned: success,changed,always
                    type: str
                    sample: '<errorkey>'
                failureReason:
                    description: It is the Task's failureReason.
                    returned: success,changed,always
                    type: str
                    sample: '<failurereason>'
                id:
                    description: It is the Task's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
                instanceTenantId:
                    description: It is the Task's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: '<instancetenantid>'
                isError:
                    description: It is the Task's isError.
                    returned: success,changed,always
                    type: bool
                    sample: false
                lastUpdate:
                    description: It is the Task's lastUpdate.
                    returned: success,changed,always
                    type: str
                    sample: '<lastupdate>'
                operationIdList:
                    description: It is the Task's operationIdList.
                    returned: success,changed,always
                    type: dict
                parentId:
                    description: It is the Task's parentId.
                    returned: success,changed,always
                    type: str
                    sample: '<parentid>'
                progress:
                    description: It is the Task's progress.
                    returned: success,changed,always
                    type: str
                    sample: '<progress>'
                rootId:
                    description: It is the Task's rootId.
                    returned: success,changed,always
                    type: str
                    sample: '<rootid>'
                serviceType:
                    description: It is the Task's serviceType.
                    returned: success,changed,always
                    type: str
                    sample: '<servicetype>'
                startTime:
                    description: It is the Task's startTime.
                    returned: success,changed,always
                    type: str
                    sample: '<starttime>'
                username:
                    description: It is the Task's username.
                    returned: success,changed,always
                    type: str
                    sample: 'devnetuser'
                version:
                    description: It is the Task's version.
                    returned: success,changed,always
                    type: int
                    sample: 0

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_4:
    description: Returns a Task with its children Tasks by based on their id.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                additionalStatusURL:
                    description: It is the Task's additionalStatusURL.
                    returned: success,changed,always
                    type: str
                    sample: '<additionalstatusurl>'
                data:
                    description: It is the Task's data.
                    returned: success,changed,always
                    type: str
                    sample: '<data>'
                endTime:
                    description: It is the Task's endTime.
                    returned: success,changed,always
                    type: str
                    sample: '<endtime>'
                errorCode:
                    description: It is the Task's errorCode.
                    returned: success,changed,always
                    type: str
                    sample: '<errorcode>'
                errorKey:
                    description: It is the Task's errorKey.
                    returned: success,changed,always
                    type: str
                    sample: '<errorkey>'
                failureReason:
                    description: It is the Task's failureReason.
                    returned: success,changed,always
                    type: str
                    sample: '<failurereason>'
                id:
                    description: It is the Task's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
                instanceTenantId:
                    description: It is the Task's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: '<instancetenantid>'
                isError:
                    description: It is the Task's isError.
                    returned: success,changed,always
                    type: bool
                    sample: false
                lastUpdate:
                    description: It is the Task's lastUpdate.
                    returned: success,changed,always
                    type: str
                    sample: '<lastupdate>'
                operationIdList:
                    description: It is the Task's operationIdList.
                    returned: success,changed,always
                    type: dict
                parentId:
                    description: It is the Task's parentId.
                    returned: success,changed,always
                    type: str
                    sample: '<parentid>'
                progress:
                    description: It is the Task's progress.
                    returned: success,changed,always
                    type: str
                    sample: '<progress>'
                rootId:
                    description: It is the Task's rootId.
                    returned: success,changed,always
                    type: str
                    sample: '<rootid>'
                serviceType:
                    description: It is the Task's serviceType.
                    returned: success,changed,always
                    type: str
                    sample: '<servicetype>'
                startTime:
                    description: It is the Task's startTime.
                    returned: success,changed,always
                    type: str
                    sample: '<starttime>'
                username:
                    description: It is the Task's username.
                    returned: success,changed,always
                    type: str
                    sample: 'devnetuser'
                version:
                    description: It is the Task's version.
                    returned: success,changed,always
                    type: int
                    sample: 0

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    ModuleDefinition,
    DNACModule,
    dnac_argument_spec,
)
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.task import (
    module_definition,
)


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()

    module = AnsibleModule(
        argument_spec=argument_spec, supports_check_mode=False, required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "query":
        dnac.exec("get")

    dnac.exit_json()


if __name__ == "__main__":
    main()
