#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_wireless_settings_ssids_v1_info
short_description: Information module for Sites Wireless Settings Ssids V1
description:
- Get all Sites Wireless Settings Ssids V1.
- Get Sites Wireless Settings Ssids V1 by id.
- This API allows the user to get all SSIDs Service Set Identifier at the given site.
- This API allows the user to get an SSID Service Set Identifier by ID at the given site.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
    - SiteId path parameter. Site UUID.
    type: str
  limit:
    description:
    - Limit query parameter.
    type: float
  offset:
    description:
    - Offset query parameter.
    type: float
  id:
    description:
    - Id path parameter. SSID ID.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless GetSSIDByIDV1
  description: Complete reference of the GetSSIDByIDV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-ssid-by-id-v-1
- name: Cisco DNA Center documentation for Wireless GetSSIDBySiteV1
  description: Complete reference of the GetSSIDBySiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-ssid-by-site-v-1
notes:
  - SDK Method used are
    wireless.Wireless.get_ssid_by_id_v1,
    wireless.Wireless.get_ssid_by_site_v1,

  - Paths used are
    get /dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids,
    get /dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids/{id},

"""

EXAMPLES = r"""
- name: Get all Sites Wireless Settings Ssids V1
  cisco.dnac.sites_wireless_settings_ssids_v1_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    limit: 0
    offset: 0
    siteId: string
  register: result

- name: Get Sites Wireless Settings Ssids V1 by id
  cisco.dnac.sites_wireless_settings_ssids_v1_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: string
    id: string
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "ssid": "string",
        "authType": "string",
        "passphrase": "string",
        "isFastLaneEnabled": true,
        "isMacFilteringEnabled": true,
        "ssidRadioType": "string",
        "isBroadcastSSID": true,
        "fastTransition": "string",
        "sessionTimeOutEnable": true,
        "sessionTimeOut": 0,
        "clientExclusionEnable": true,
        "clientExclusionTimeout": 0,
        "basicServiceSetMaxIdleEnable": true,
        "basicServiceSetClientIdleTimeout": 0,
        "directedMulticastServiceEnable": true,
        "neighborListEnable": true,
        "managementFrameProtectionClientprotection": "string",
        "nasOptions": [
          "string"
        ],
        "profileName": "string",
        "policyProfileName": "string",
        "aaaOverride": true,
        "coverageHoleDetectionEnable": true,
        "protectedManagementFrame": "string",
        "multiPSKSettings": [
          {
            "priority": 0,
            "passphraseType": "string",
            "passphrase": "string"
          }
        ],
        "clientRateLimit": 0,
        "rsnCipherSuiteGcmp256": true,
        "rsnCipherSuiteCcmp256": true,
        "rsnCipherSuiteGcmp128": true,
        "rsnCipherSuiteCcmp128": true,
        "ghz6PolicyClientSteering": true,
        "isAuthKey8021x": true,
        "isAuthKey8021xPlusFT": true,
        "isAuthKey8021x_SHA256": true,
        "isAuthKeySae": true,
        "isAuthKeySaePlusFT": true,
        "isAuthKeyPSK": true,
        "isAuthKeyPSKPlusFT": true,
        "isAuthKeyOWE": true,
        "isAuthKeyEasyPSK": true,
        "isAuthKeyPSKSHA256": true,
        "openSsid": "string",
        "isCustomNasIdOptions": true,
        "wlanBandSelectEnable": true,
        "isEnabled": true,
        "authServers": [
          "string"
        ],
        "acctServers": [
          "string"
        ],
        "egressQos": "string",
        "ingressQos": "string",
        "inheritedSiteId": "string",
        "inheritedSiteName": "string",
        "wlanType": "string",
        "l3AuthType": "string",
        "authServer": "string",
        "externalAuthIpAddress": "string",
        "webPassthrough": true,
        "sleepingClientEnable": true,
        "sleepingClientTimeout": 0,
        "aclName": "string",
        "isPosturingEnabled": true,
        "isAuthKeySuiteB1x": true,
        "isAuthKeySuiteB1921x": true,
        "isAuthKeySaeExt": true,
        "isAuthKeySaeExtPlusFT": true,
        "isApBeaconProtectionEnabled": true,
        "ghz24Policy": "string",
        "cckmTsfTolerance": 0,
        "isCckmEnabled": true,
        "isHex": true,
        "isSensorPnp": true,
        "id": "string",
        "isRandomMacFilterEnabled": true,
        "fastTransitionOverTheDistributedSystemEnable": true
      },
      "version": "string"
    }
"""