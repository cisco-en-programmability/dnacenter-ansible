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
module: site_health
short_description: Manage SiteHealth objects of Sites
description:
- Returns Overall Health information for all sites.
version_added: '1.0'
author: first last (@GitHubID)
options:
    timestamp:
        description:
        - Epoch time(in milliseconds) when the Site Hierarchy data is required.
        type: int

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.site_health
# Reference by Internet resource
- name: SiteHealth reference
  description: Complete reference of the SiteHealth object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SiteHealth reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Returns Overall Health information for all sites.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                siteName:
                    description: It is the site health's siteName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                siteId:
                    description: It is the site health's siteId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                parentSiteId:
                    description: It is the site health's parentSiteId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                parentSiteName:
                    description: It is the site health's parentSiteName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                siteType:
                    description: It is the site health's siteType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                latitude:
                    description: It is the site health's latitude.
                    returned: success,changed,always
                    type: dict
                longitude:
                    description: It is the site health's longitude.
                    returned: success,changed,always
                    type: dict
                healthyNetworkDevicePercentage:
                    description: It is the site health's healthyNetworkDevicePercentage.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                healthyClientsPercentage:
                    description: It is the site health's healthyClientsPercentage.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                clientHealthWired:
                    description: It is the site health's clientHealthWired.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                clientHealthWireless:
                    description: It is the site health's clientHealthWireless.
                    returned: success,changed,always
                    type: dict
                numberOfClients:
                    description: It is the site health's numberOfClients.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                clientNumberOfIssues:
                    description: It is the site health's clientNumberOfIssues.
                    returned: success,changed,always
                    type: dict
                networkNumberOfIssues:
                    description: It is the site health's networkNumberOfIssues.
                    returned: success,changed,always
                    type: dict
                numberOfNetworkDevice:
                    description: It is the site health's numberOfNetworkDevice.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                networkHealthAverage:
                    description: It is the site health's networkHealthAverage.
                    returned: success,changed,always
                    type: dict
                networkHealthAccess:
                    description: It is the site health's networkHealthAccess.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                networkHealthCore:
                    description: It is the site health's networkHealthCore.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                networkHealthDistribution:
                    description: It is the site health's networkHealthDistribution.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                networkHealthRouter:
                    description: It is the site health's networkHealthRouter.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                networkHealthWireless:
                    description: It is the site health's networkHealthWireless.
                    returned: success,changed,always
                    type: dict
                networkHealthOthers:
                    description: It is the site health's networkHealthOthers.
                    returned: success,changed,always
                    type: dict
                numberOfWiredClients:
                    description: It is the site health's numberOfWiredClients.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                numberOfWirelessClients:
                    description: It is the site health's numberOfWirelessClients.
                    returned: success,changed,always
                    type: dict
                wiredGoodClients:
                    description: It is the site health's wiredGoodClients.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                wirelessGoodClients:
                    description: It is the site health's wirelessGoodClients.
                    returned: success,changed,always
                    type: dict
                clientIssueCount:
                    description: It is the site health's clientIssueCount.
                    returned: success,changed,always
                    type: dict
                overallGoodDevices:
                    description: It is the site health's overallGoodDevices.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                accessGoodCount:
                    description: It is the site health's accessGoodCount.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                accessTotalCount:
                    description: It is the site health's accessTotalCount.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                coreGoodCount:
                    description: It is the site health's coreGoodCount.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                coreTotalCount:
                    description: It is the site health's coreTotalCount.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                distributionGoodCount:
                    description: It is the site health's distributionGoodCount.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                distributionTotalCount:
                    description: It is the site health's distributionTotalCount.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                routerGoodCount:
                    description: It is the site health's routerGoodCount.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                routerTotalCount:
                    description: It is the site health's routerTotalCount.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                wirelessDeviceGoodCount:
                    description: It is the site health's wirelessDeviceGoodCount.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                wirelessDeviceTotalCount:
                    description: It is the site health's wirelessDeviceTotalCount.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                applicationHealth:
                    description: It is the site health's applicationHealth.
                    returned: success,changed,always
                    type: dict
                applicationGoodCount:
                    description: It is the site health's applicationGoodCount.
                    returned: success,changed,always
                    type: dict
                applicationTotalCount:
                    description: It is the site health's applicationTotalCount.
                    returned: success,changed,always
                    type: dict
                applicationBytesTotalCount:
                    description: It is the site health's applicationBytesTotalCount.
                    returned: success,changed,always
                    type: dict


'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.site_health import module_definition


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