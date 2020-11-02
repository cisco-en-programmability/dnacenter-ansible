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
module: import_image
short_description: Manage ImportImage objects of SoftwareImageManagementSwim
description:
- Returns software image list based on a filter criteria. For example: "filterbyName = cat3k%".
version_added: '1.0'
author: first last (@GitHubID)
options:
    application_type:
        description:
        - ApplicationType query parameter.
        type: str
    created_time:
        description:
        - Time in milliseconds (epoch format).
        type: int
    family:
        description:
        - Family query parameter.
        type: str
    image_integrity_status:
        description:
        - ImageIntegrityStatus - FAILURE, UNKNOWN, VERIFIED.
        type: str
    image_name:
        description:
        - Image Name.
        type: str
    image_series:
        description:
        - Image Series.
        type: str
    image_size_greater_than:
        description:
        - Size in bytes.
        type: int
    image_size_lesser_than:
        description:
        - Size in bytes.
        type: int
    image_uuid:
        description:
        - ImageUuid query parameter.
        type: str
    is_cco_latest:
        description:
        - Is latest from cisco.com.
        type: bool
    is_cco_recommended:
        description:
        - Is recommended from cisco.com.
        type: bool
    is_tagged_golden:
        description:
        - Is Tagged Golden.
        type: bool
    limit:
        description:
        - Limit query parameter.
        type: int
    name:
        description:
        - Name query parameter.
        type: str
    offset:
        description:
        - Offset query parameter.
        type: int
    sort_by:
        description:
        - Sort results by this field.
        type: str
    sort_order:
        description:
        - Sort order - 'asc' or 'des'. Default is asc.
        type: str
    version:
        description:
        - Software Image Version.
        type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.import_image
# Reference by Internet resource
- name: ImportImage reference
  description: Complete reference of the ImportImage object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: ImportImage reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Returns software image list based on a filter criteria. For example: "filterbyName = cat3k%".
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                applicableDevicesForImage:
                    description: It is the import image's applicableDevicesForImage.
                    returned: success,changed,always
                    type: list
                    contains:
                        mdfId:
                            description: It is the import image's mdfId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        productId:
                            description: It is the import image's productId.
                            returned: success,changed,always
                            type: list
                        productName:
                            description: It is the import image's productName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                applicationType:
                    description: It is the import image's applicationType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                createdTime:
                    description: It is the import image's createdTime.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                extendedAttributes:
                    description: It is the import image's extendedAttributes.
                    returned: success,changed,always
                    type: dict
                family:
                    description: It is the import image's family.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                feature:
                    description: It is the import image's feature.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                fileServiceId:
                    description: It is the import image's fileServiceId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                fileSize:
                    description: It is the import image's fileSize.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                imageIntegrityStatus:
                    description: It is the import image's imageIntegrityStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                imageName:
                    description: It is the import image's imageName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                imageSeries:
                    description: It is the import image's imageSeries.
                    returned: success,changed,always
                    type: list
                imageSource:
                    description: It is the import image's imageSource.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                imageType:
                    description: It is the import image's imageType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                imageUuid:
                    description: It is the import image's imageUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                importSourceType:
                    description: It is the import image's importSourceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                isTaggedGolden:
                    description: It is the import image's isTaggedGolden.
                    returned: success,changed,always
                    type: bool
                    sample: false
                md5Checksum:
                    description: It is the import image's md5Checksum.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the import image's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                profileInfo:
                    description: It is the import image's profileInfo.
                    returned: success,changed,always
                    type: list
                    contains:
                        description:
                            description: It is the import image's description.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        extendedAttributes:
                            description: It is the import image's extendedAttributes.
                            returned: success,changed,always
                            type: dict
                        memory:
                            description: It is the import image's memory.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        productType:
                            description: It is the import image's productType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        profileName:
                            description: It is the import image's profileName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        shares:
                            description: It is the import image's shares.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        vCpu:
                            description: It is the import image's vCpu.
                            returned: success,changed,always
                            type: int
                            sample: 0

                shaCheckSum:
                    description: It is the import image's shaCheckSum.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                vendor:
                    description: It is the import image's vendor.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                version:
                    description: It is the import image's version.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.import_image import module_definition


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

    dnac.exit_json()


if __name__ == "__main__":
    main()