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
module: wireless_provision
short_description: Manage WirelessProvision objects of Wireless
description:
- Provision wireless devices.
- Updates wireless provisioning.
version_added: '1.0'
author: first last (@GitHubID)
options:
  payload:
    description:
    - An object to send in the Request body.
    type: list
    required: True
    elements: dict
    suboptions:
      deviceName:
        description:
        - It is the wireless provision's deviceName.
        type: str
        required: True
      dynamicInterfaces:
        description:
        - It is the wireless provision's dynamicInterfaces.
        type: list
        elements: dict
        suboptions:
          interfaceGateway:
            description:
            - It is the wireless provision's interfaceGateway.
            type: str
          interfaceIPAddress:
            description:
            - It is the wireless provision's interfaceIPAddress.
            type: str
          interfaceName:
            description:
            - It is the wireless provision's interfaceName.
            type: str
          interfaceNetmaskInCIDR:
            description:
            - It is the wireless provision's interfaceNetmaskInCIDR.
            type: int
          lagOrPortNumber:
            description:
            - It is the wireless provision's lagOrPortNumber.
            type: int
          vlanId:
            description:
            - It is the wireless provision's vlanId.
            type: int

      managedAPLocations:
        description:
        - It is the wireless provision's managedAPLocations.
        type: list
      site:
        description:
        - It is the wireless provision's site.
        type: str
        required: True


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.wireless_provision
# Reference by Internet resource
- name: WirelessProvision reference
  description: Complete reference of the WirelessProvision object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: WirelessProvision reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: provision
  cisco.dnac.wireless_provision
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: create  # required
    payload:  # required
    - deviceName: SomeValue  # string, required
      site: SomeValue  # string, required
      managedAPLocations:
      - SomeValue  # string
      dynamicInterfaces:
      - interfaceIPAddress: SomeValue  # string
        interfaceNetmaskInCIDR: 1  #  integer
        interfaceGateway: SomeValue  # string
        lagOrPortNumber: 1  #  integer
        vlanId: 1  #  integer
        interfaceName: SomeValue  # string
  delegate_to: localhost
  
- name: provision_update
  cisco.dnac.wireless_provision
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: update  # required
    payload:  # required
    - deviceName: SomeValue  # string, required
      managedAPLocations:
      - SomeValue  # string
      dynamicInterfaces:
      - interfaceIPAddress: SomeValue  # string
        interfaceNetmaskInCIDR: 1  #  integer
        interfaceGateway: SomeValue  # string
        lagOrPortNumber: 1  #  integer
        vlanId: 1  #  integer
        interfaceName: SomeValue  # string
  delegate_to: localhost
  
"""

RETURN = """
provision:
    description: Provision wireless devices.
    returned: success
    type: dict
    contains:
    executionId:
      description: Execution Id, property of the response body.
      returned: success
      type: str
      sample: '<executionid>'
    executionUrl:
      description: Execution Url, property of the response body.
      returned: success
      type: str
      sample: '<executionurl>'
    provisioningTasks:
      description: Provisioning Tasks, property of the response body.
      returned: success
      type: dict
      contains:
        success:
          description: It is the wireless provision's success.
          returned: success
          type: list
        failed:
          description: It is the wireless provision's failed.
          returned: success
          type: list


provision_update:
    description: Updates wireless provisioning.
    returned: changed
    type: dict
    contains:
    executionId:
      description: Execution Id, property of the response body.
      returned: changed
      type: str
      sample: '<executionid>'
    executionUrl:
      description: Execution Url, property of the response body.
      returned: changed
      type: str
      sample: '<executionurl>'
    provisioningTasks:
      description: Provisioning Tasks, property of the response body.
      returned: changed
      type: dict
      contains:
        success:
          description: It is the wireless provision's success.
          returned: changed
          type: list
        failed:
          description: It is the wireless provision's failed.
          returned: changed
          type: list


"""
