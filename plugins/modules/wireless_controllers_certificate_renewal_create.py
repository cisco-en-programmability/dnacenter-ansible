#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_certificate_renewal_create
short_description: Resource module for Wireless Controllers Certificate Renewal Create
description:
  - Manage operation create of the resource Wireless Controllers Certificate Renewal Create.
  - This API allows user to renew LSC certificates of access points.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  accessPointMacs:
    description: MAC address of access points on which certificate renewal has to be performed.
    elements: str
    type: list
  deviceId:
    description:
      - DeviceId path parameter. Network Device ID.
      - This value can be obtained by using the API call GET /dna/intent/api/v1/network-device/ip-address/${ipAddress}.
    type: str
  expiryTime:
    description: Expiry time with in which access points certificates are set to expire.
    type: int
  siteTagIds:
    description: Site tag IDs on which LSC instantaneous certificate renewal has to be performed.
    elements: str
    type: list
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Wireless AccessPointsLSCCertificateInstantaneousRenewal
    description: Complete reference of the AccessPointsLSCCertificateInstantaneousRenewal API.
    link: https://developer.cisco.com/docs/dna-center/#!access-points-lsc-certificate-instantaneous-renewal
notes:
  - SDK Method used are
    wireless.Wireless.access_points_l_s_c_certificate_instantaneous_renewal,
  - Paths used are
    post /dna/intent/api/v1/wirelessControllers/{deviceId}/certificateRenewal,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.dnac.wireless_controllers_certificate_renewal_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    accessPointMacs:
      - string
    deviceId: string
    expiryTime: 0
    siteTagIds:
      - string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
