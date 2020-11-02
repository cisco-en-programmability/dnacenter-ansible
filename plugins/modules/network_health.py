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
module: network_health
short_description: Manage NetworkHealth objects of Topology
description:
- Returns Overall Network Health information by Device category (Access, Distribution, Core, Router, Wireless) for any given point of time.
version_added: '1.0'
author: first last (@GitHubID)
options:
    timestamp:
        description:
        - Epoch time(in milliseconds) when the Network health data is required.
        type: int

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_health
# Reference by Internet resource
- name: NetworkHealth reference
  description: Complete reference of the NetworkHealth object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkHealth reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Returns Overall Network Health information by Device category (Access, Distribution, Core, Router, Wireless) for any given point of time.
    returned: success,changed,always
    type: dict
    contains:
        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                time:
                    description: It is the network health's time.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                healthScore:
                    description: It is the network health's healthScore.
                    returned: success,changed,always
                    type: int
                    sample: 0
                totalCount:
                    description: It is the network health's totalCount.
                    returned: success,changed,always
                    type: int
                    sample: 0
                goodCount:
                    description: It is the network health's goodCount.
                    returned: success,changed,always
                    type: int
                    sample: 0
                unmonCount:
                    description: It is the network health's unmonCount.
                    returned: success,changed,always
                    type: int
                    sample: 0
                fairCount:
                    description: It is the network health's fairCount.
                    returned: success,changed,always
                    type: int
                    sample: 0
                badCount:
                    description: It is the network health's badCount.
                    returned: success,changed,always
                    type: int
                    sample: 0
                entity:
                    description: It is the network health's entity.
                    returned: success,changed,always
                    type: dict
                timeinMillis:
                    description: It is the network health's timeinMillis.
                    returned: success,changed,always
                    type: int
                    sample: 0

        measuredBy:
            description: Measured By, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        latestMeasuredByEntity:
            description: Latest Measured By Entity, property of the response body.
            returned: success,changed,always
            type: dict
        latestHealthScore:
            description: LatestHealthScore, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        monitoredDevices:
            description: MonitoredDevices, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        monitoredHealthyDevices:
            description: MonitoredHealthyDevices, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        monitoredUnHealthyDevices:
            description: MonitoredUnHealthyDevices, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        unMonitoredDevices:
            description: UnMonitoredDevices, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        healthDistirubution:
            description: Health Distirubution, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                category:
                    description: It is the network health's category.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                totalCount:
                    description: It is the network health's totalCount.
                    returned: success,changed,always
                    type: int
                    sample: 0
                healthScore:
                    description: It is the network health's healthScore.
                    returned: success,changed,always
                    type: int
                    sample: 0
                goodPercentage:
                    description: It is the network health's goodPercentage.
                    returned: success,changed,always
                    type: int
                    sample: 0
                badPercentage:
                    description: It is the network health's badPercentage.
                    returned: success,changed,always
                    type: int
                    sample: 0
                fairPercentage:
                    description: It is the network health's fairPercentage.
                    returned: success,changed,always
                    type: int
                    sample: 0
                unmonPercentage:
                    description: It is the network health's unmonPercentage.
                    returned: success,changed,always
                    type: int
                    sample: 0
                goodCount:
                    description: It is the network health's goodCount.
                    returned: success,changed,always
                    type: int
                    sample: 0
                badCount:
                    description: It is the network health's badCount.
                    returned: success,changed,always
                    type: int
                    sample: 0
                fairCount:
                    description: It is the network health's fairCount.
                    returned: success,changed,always
                    type: int
                    sample: 0
                unmonCount:
                    description: It is the network health's unmonCount.
                    returned: success,changed,always
                    type: int
                    sample: 0
                kpiMetrics:
                    description: It is the network health's kpiMetrics.
                    returned: success,changed,always
                    type: list


'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.network_health import module_definition


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