#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: discoverys_jobs_discovered_network_devices_count_info
short_description: Information module for Discoverys Jobs Discovered Network Devices Count
description:
  - Get all Discoverys Jobs Discovered Network Devices Count.
  - API to get the details of all the devices discovered by the given jobId and discoveryId.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  discoveryId:
    description:
      - DiscoveryId path parameter. The id of the discovery.
    type: str
  jobId:
    description:
      - JobId path parameter. The id of the discovery job.
    type: str
  managementIpAddress:
    description:
      - ManagementIpAddress query parameter. Management IP address of the network device.
    type: str
  reachabilityStatus:
    description:
      - ReachabilityStatus query parameter. Reachability status of the network device.
    type: str
  ping:
    description:
      - Ping query parameter. Ping status for the IP during the job run.
    type: str
  cli:
    description:
      - Cli query parameter. CLI status for the IP during the job run.
    type: str
  snmp:
    description:
      - Snmp query parameter. SNMP status for the IP during the job run.
    type: str
  http:
    description:
      - Http query parameter. HTTP status for the IP during the job run.
    type: str
  netconf:
    description:
      - Netconf query parameter. Netconf status for the IP during the job run.
    type: str
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices CountTheNumberOfDiscoveredNetworkDevicesByDiscoveryId
    description: Complete reference of the CountTheNumberOfDiscoveredNetworkDevicesByDiscoveryId API.
    link: https://developer.cisco.com/docs/dna-center/#!count-the-number-of-discovered-network-devices-by-discovery-id
notes:
  - SDK Method used are
    devices.Devices.count_the_number_of_discovered_network_devices_by_discovery_id,
  - Paths used are
    get /dna/intent/api/v1/discoverys/{discoveryId}/jobs/{jobId}/discoveredNetworkDevices/count,
"""

EXAMPLES = r"""
---
- name: Get all Discoverys Jobs Discovered Network Devices Count
  cisco.dnac.discoverys_jobs_discovered_network_devices_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    managementIpAddress: string
    reachabilityStatus: string
    ping: string
    cli: string
    snmp: string
    http: string
    netconf: string
    limit: 0
    offset: 0
    discoveryId: string
    jobId: string
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
        "count": 0
      },
      "version": "string"
    }
"""
