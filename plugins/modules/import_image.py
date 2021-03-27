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
module: import_image
short_description: Manage ImportImage objects of SoftwareImageManagementSwim
description:
- Returns software image list based on a filter criteria. For example: "filterbyName = cat3k%".
version_added: '1.0'
author: Rafael Campos (@racampos)
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
"""

EXAMPLES = r"""
- name: get_software_image_details
  cisco.dnac.import_image:
    state: query  # required
    application_type: SomeValue  # string
    created_time: 1  #  integer
    family: SomeValue  # string
    image_integrity_status: SomeValue  # string
    image_name: SomeValue  # string
    image_series: SomeValue  # string
    image_size_greater_than: 1  #  integer
    image_size_lesser_than: 1  #  integer
    image_uuid: SomeValue  # string
    is_cco_latest: True  # boolean
    is_cco_recommended: True  # boolean
    is_tagged_golden: True  # boolean
    limit: 1  #  integer
    name: SomeValue  # string
    offset: 1  #  integer
    sort_by: SomeValue  # string
    sort_order: SomeValue  # string
    version: SomeValue  # string
  register: query_result
  
"""

RETURN = """
get_software_image_details:
    description: Returns software image list based on a filter criteria. For example: "filterbyName = cat3k%".
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        applicableDevicesForImage:
          description: It is the import image's applicableDevicesForImage.
          returned: always
          type: list
          contains:
            mdfId:
              description: It is the import image's mdfId.
              returned: always
              type: str
              sample: '<mdfid>'
            productId:
              description: It is the import image's productId.
              returned: always
              type: list
            productName:
              description: It is the import image's productName.
              returned: always
              type: str
              sample: '<productname>'

        applicationType:
          description: It is the import image's applicationType.
          returned: always
          type: str
          sample: '<applicationtype>'
        createdTime:
          description: It is the import image's createdTime.
          returned: always
          type: str
          sample: '<createdtime>'
        extendedAttributes:
          description: It is the import image's extendedAttributes.
          returned: always
          type: dict
        family:
          description: It is the import image's family.
          returned: always
          type: str
          sample: '<family>'
        feature:
          description: It is the import image's feature.
          returned: always
          type: str
          sample: '<feature>'
        fileServiceId:
          description: It is the import image's fileServiceId.
          returned: always
          type: str
          sample: '<fileserviceid>'
        fileSize:
          description: It is the import image's fileSize.
          returned: always
          type: str
          sample: '<filesize>'
        imageIntegrityStatus:
          description: It is the import image's imageIntegrityStatus.
          returned: always
          type: str
          sample: '<imageintegritystatus>'
        imageName:
          description: It is the import image's imageName.
          returned: always
          type: str
          sample: '<imagename>'
        imageSeries:
          description: It is the import image's imageSeries.
          returned: always
          type: list
        imageSource:
          description: It is the import image's imageSource.
          returned: always
          type: str
          sample: '<imagesource>'
        imageType:
          description: It is the import image's imageType.
          returned: always
          type: str
          sample: '<imagetype>'
        imageUuid:
          description: It is the import image's imageUuid.
          returned: always
          type: str
          sample: '<imageuuid>'
        importSourceType:
          description: It is the import image's importSourceType.
          returned: always
          type: str
          sample: '<importsourcetype>'
        isTaggedGolden:
          description: It is the import image's isTaggedGolden.
          returned: always
          type: bool
          sample: false
        md5Checksum:
          description: It is the import image's md5Checksum.
          returned: always
          type: str
          sample: '<md5checksum>'
        name:
          description: It is the import image's name.
          returned: always
          type: str
          sample: '<name>'
        profileInfo:
          description: It is the import image's profileInfo.
          returned: always
          type: list
          contains:
            description:
              description: It is the import image's description.
              returned: always
              type: str
              sample: '<description>'
            extendedAttributes:
              description: It is the import image's extendedAttributes.
              returned: always
              type: dict
            memory:
              description: It is the import image's memory.
              returned: always
              type: int
              sample: 0
            productType:
              description: It is the import image's productType.
              returned: always
              type: str
              sample: '<producttype>'
            profileName:
              description: It is the import image's profileName.
              returned: always
              type: str
              sample: '<profilename>'
            shares:
              description: It is the import image's shares.
              returned: always
              type: int
              sample: 0
            vCpu:
              description: It is the import image's vCpu.
              returned: always
              type: int
              sample: 0

        shaCheckSum:
          description: It is the import image's shaCheckSum.
          returned: always
          type: str
          sample: '<shachecksum>'
        vendor:
          description: It is the import image's vendor.
          returned: always
          type: str
          sample: '<vendor>'
        version:
          description: It is the import image's version.
          returned: always
          type: str
          sample: '1.0'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

"""
