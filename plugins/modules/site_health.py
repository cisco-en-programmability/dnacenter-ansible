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
module: site_health
short_description: Manage SiteHealth objects of Sites
description:
- Returns Overall Health information for all sites.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
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
"""

EXAMPLES = r"""
- name: get_site_health
  cisco.dnac.site_health:
    state: query  # required
    timestamp: 1  #  integer
  register: query_result
  
"""

RETURN = """
get_site_health:
    description: Returns Overall Health information for all sites.
    returned: always
    type: dict
    contains:
      response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        siteName:
          description: It is the site health's siteName.
          returned: always
          type: str
          sample: '<sitename>'
        siteId:
          description: It is the site health's siteId.
          returned: always
          type: str
          sample: '<siteid>'
        parentSiteId:
          description: It is the site health's parentSiteId.
          returned: always
          type: str
          sample: '<parentsiteid>'
        parentSiteName:
          description: It is the site health's parentSiteName.
          returned: always
          type: str
          sample: '<parentsitename>'
        siteType:
          description: It is the site health's siteType.
          returned: always
          type: str
          sample: '<sitetype>'
        latitude:
          description: It is the site health's latitude.
          returned: always
          type: dict
        longitude:
          description: It is the site health's longitude.
          returned: always
          type: dict
        healthyNetworkDevicePercentage:
          description: It is the site health's healthyNetworkDevicePercentage.
          returned: always
          type: str
          sample: '<healthynetworkdevicepercentage>'
        healthyClientsPercentage:
          description: It is the site health's healthyClientsPercentage.
          returned: always
          type: str
          sample: '<healthyclientspercentage>'
        clientHealthWired:
          description: It is the site health's clientHealthWired.
          returned: always
          type: str
          sample: '<clienthealthwired>'
        clientHealthWireless:
          description: It is the site health's clientHealthWireless.
          returned: always
          type: dict
        numberOfClients:
          description: It is the site health's numberOfClients.
          returned: always
          type: str
          sample: '<numberofclients>'
        clientNumberOfIssues:
          description: It is the site health's clientNumberOfIssues.
          returned: always
          type: dict
        networkNumberOfIssues:
          description: It is the site health's networkNumberOfIssues.
          returned: always
          type: dict
        numberOfNetworkDevice:
          description: It is the site health's numberOfNetworkDevice.
          returned: always
          type: str
          sample: '<numberofnetworkdevice>'
        networkHealthAverage:
          description: It is the site health's networkHealthAverage.
          returned: always
          type: dict
        networkHealthAccess:
          description: It is the site health's networkHealthAccess.
          returned: always
          type: str
          sample: '<networkhealthaccess>'
        networkHealthCore:
          description: It is the site health's networkHealthCore.
          returned: always
          type: str
          sample: '<networkhealthcore>'
        networkHealthDistribution:
          description: It is the site health's networkHealthDistribution.
          returned: always
          type: str
          sample: '<networkhealthdistribution>'
        networkHealthRouter:
          description: It is the site health's networkHealthRouter.
          returned: always
          type: str
          sample: '<networkhealthrouter>'
        networkHealthWireless:
          description: It is the site health's networkHealthWireless.
          returned: always
          type: dict
        networkHealthOthers:
          description: It is the site health's networkHealthOthers.
          returned: always
          type: dict
        numberOfWiredClients:
          description: It is the site health's numberOfWiredClients.
          returned: always
          type: str
          sample: '<numberofwiredclients>'
        numberOfWirelessClients:
          description: It is the site health's numberOfWirelessClients.
          returned: always
          type: dict
        wiredGoodClients:
          description: It is the site health's wiredGoodClients.
          returned: always
          type: str
          sample: '<wiredgoodclients>'
        wirelessGoodClients:
          description: It is the site health's wirelessGoodClients.
          returned: always
          type: dict
        clientIssueCount:
          description: It is the site health's clientIssueCount.
          returned: always
          type: dict
        overallGoodDevices:
          description: It is the site health's overallGoodDevices.
          returned: always
          type: str
          sample: '<overallgooddevices>'
        accessGoodCount:
          description: It is the site health's accessGoodCount.
          returned: always
          type: str
          sample: '<accessgoodcount>'
        accessTotalCount:
          description: It is the site health's accessTotalCount.
          returned: always
          type: str
          sample: '<accesstotalcount>'
        coreGoodCount:
          description: It is the site health's coreGoodCount.
          returned: always
          type: str
          sample: '<coregoodcount>'
        coreTotalCount:
          description: It is the site health's coreTotalCount.
          returned: always
          type: str
          sample: '<coretotalcount>'
        distributionGoodCount:
          description: It is the site health's distributionGoodCount.
          returned: always
          type: str
          sample: '<distributiongoodcount>'
        distributionTotalCount:
          description: It is the site health's distributionTotalCount.
          returned: always
          type: str
          sample: '<distributiontotalcount>'
        routerGoodCount:
          description: It is the site health's routerGoodCount.
          returned: always
          type: str
          sample: '<routergoodcount>'
        routerTotalCount:
          description: It is the site health's routerTotalCount.
          returned: always
          type: str
          sample: '<routertotalcount>'
        wirelessDeviceGoodCount:
          description: It is the site health's wirelessDeviceGoodCount.
          returned: always
          type: str
          sample: '<wirelessdevicegoodcount>'
        wirelessDeviceTotalCount:
          description: It is the site health's wirelessDeviceTotalCount.
          returned: always
          type: str
          sample: '<wirelessdevicetotalcount>'
        applicationHealth:
          description: It is the site health's applicationHealth.
          returned: always
          type: dict
        applicationGoodCount:
          description: It is the site health's applicationGoodCount.
          returned: always
          type: dict
        applicationTotalCount:
          description: It is the site health's applicationTotalCount.
          returned: always
          type: dict
        applicationBytesTotalCount:
          description: It is the site health's applicationBytesTotalCount.
          returned: always
          type: dict


"""
