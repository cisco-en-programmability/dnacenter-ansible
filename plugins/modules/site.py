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
module: site
short_description: Manage Site objects of Sites
description:
- Get Site with area/building/floor with specified hierarchy.
- Creates Site with area/building/floor with specified hierarchy.
- Delete Site with area/building/floor by SiteId.
- Update Site area/building/floor with specified hierarchy and new values.
- API to get Site count.
version_added: '1.0'
author: first last (@GitHubID)
options:
    limit:
        description:
        - Number of Sites to be retrieved.
        type: str
    name:
        description:
        - SiteNameHierarchy (ex: global/groupName).
        type: str
    offset:
        description:
        - Offset/starting row.
        type: str
    site_id:
        description:
        - Site id to which Site details to retrieve.
        - Required for state absent.
        type: str
    type:
        description:
        - Type (ex: area, building, floor).
        - Required for state present.
        type: str
    site:
        description:
        - Site, property of the request body.
        type: dict
        required: True
        suboptions:
            area:
                description:
                - It is the Site's area.
                type: dict
                suboptions:
                    name:
                        description:
                        - It is the Site's name.
                        type: str
                    parentName:
                        description:
                        - It is the Site's parentName.
                        type: str

            building:
                description:
                - It is the Site's building.
                type: dict
                suboptions:
                    address:
                        description:
                        - It is the Site's address.
                        type: str
                    latitude:
                        description:
                        - It is the Site's latitude.
                        type: int
                    longitude:
                        description:
                        - It is the Site's longitude.
                        type: int
                    name:
                        description:
                        - It is the Site's name.
                        type: str
                    parentName:
                        description:
                        - It is the Site's parentName.
                        type: str

            floor:
                description:
                - It is the Site's floor.
                type: dict
                suboptions:
                    height:
                        description:
                        - It is the Site's height.
                        type: int
                    length:
                        description:
                        - It is the Site's length.
                        type: int
                    name:
                        description:
                        - It is the Site's name.
                        type: str
                    parentName:
                        description:
                        - It is the Site's parentName.
                        type: str
                    rfModel:
                        description:
                        - It is the Site's rfModel.
                        type: str
                    width:
                        description:
                        - It is the Site's width.
                        type: int


    count:
        description:
        - If true gets the number of objects.
        type: bool
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.site
# Reference by Internet resource
- name: Site reference
  description: Complete reference of the Site object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: Site reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
"""

RETURN = r"""
data_0:
    description: Get Site with area/building/floor with specified hierarchy.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                parentId:
                    description: It is the Site's parentId.
                    returned: success,changed,always
                    type: str
                    sample: '<parentid>'
                name:
                    description: It is the Site's name.
                    returned: success,changed,always
                    type: str
                    sample: '<name>'
                additionalInfo:
                    description: It is the Site's additionalInfo.
                    returned: success,changed,always
                    type: list
                siteHierarchy:
                    description: It is the Site's SiteHierarchy.
                    returned: success,changed,always
                    type: str
                    sample: '<sitehierarchy>'
                siteNameHierarchy:
                    description: It is the Site's SiteNameHierarchy.
                    returned: success,changed,always
                    type: str
                    sample: '<sitenamehierarchy>'
                instanceTenantId:
                    description: It is the Site's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: '<instancetenantid>'
                id:
                    description: It is the Site's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'


data_1:
    description: Creates Site with area/building/floor with specified hierarchy.
    returned: success,changed,always
    type: dict
    contains:
        executionId:
            description: Execution Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<executionid>'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<executionstatusurl>'
        message:
            description: Message, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<message>'

data_2:
    description: Delete Site with area/building/floor by SiteId.
    returned: success,changed,always
    type: dict
    contains:
        status:
            description: Status, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<status>'
        message:
            description: Message, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<message>'

data_3:
    description: Update Site area/building/floor with specified hierarchy and new values.
    returned: success,changed,always
    type: dict
    contains:
        result:
            description: Result, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<result>'
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                endTime:
                    description: It is the Site's endTime.
                    returned: success,changed,always
                    type: str
                    sample: '<endtime>'
                version:
                    description: It is the Site's version.
                    returned: success,changed,always
                    type: str
                    sample: '1.0'
                startTime:
                    description: It is the Site's startTime.
                    returned: success,changed,always
                    type: str
                    sample: '<starttime>'
                progress:
                    description: It is the Site's progress.
                    returned: success,changed,always
                    type: str
                    sample: '<progress>'
                data:
                    description: It is the Site's data.
                    returned: success,changed,always
                    type: str
                    sample: '<data>'
                serviceType:
                    description: It is the Site's serviceType.
                    returned: success,changed,always
                    type: str
                    sample: '<servicetype>'
                operationIdList:
                    description: It is the Site's operationIdList.
                    returned: success,changed,always
                    type: list
                isError:
                    description: It is the Site's isError.
                    returned: success,changed,always
                    type: str
                    sample: '<iserror>'
                rootId:
                    description: It is the Site's rootId.
                    returned: success,changed,always
                    type: str
                    sample: '<rootid>'
                instanceTenantId:
                    description: It is the Site's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: '<instancetenantid>'
                id:
                    description: It is the Site's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'

        status:
            description: Status, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<status>'

data_4:
    description: API to get Site count.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<response>'
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
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.site import (
    module_definition,
    SiteExistenceCriteria,
)


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec(idempotent=True)
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()

    module = AnsibleModule(
        argument_spec=argument_spec, supports_check_mode=False, required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "query":
        dnac.exec("get")

    elif state == "absent":
        dnac.exec("delete")

    elif state == "present":
        ec = SiteExistenceCriteria(dnac)

        if ec.object_exists():
            dnac.disable_validation()
            dnac.exec("put")
            dnac.result.update({"warning": ec.WARN_OBJECT_EXISTS})

        else:
            dnac.disable_validation()
            dnac.exec("post")

    dnac.exit_json()


if __name__ == "__main__":
    main()
