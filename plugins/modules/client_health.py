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
module: client_health
short_description: Manage ClientHealth objects of Clients
description:
- Returns Overall Client Health information by Client type (Wired and Wireless) for any given point of time.
version_added: '1.0'
author: first last (@GitHubID)
options:
  timestamp:
    description:
    - Epoch time(in milliseconds) when the Client health data is required.
    type: int

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.client_health
# Reference by Internet resource
- name: ClientHealth reference
  description: Complete reference of the ClientHealth object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: ClientHealth reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_overall_client_health
  cisco.dnac.client_health:
    state: query  # required
    timestamp: 1  #  integer
  register: query_result
  
"""

RETURN = """
get_overall_client_health:
    description: Returns Overall Client Health information by Client type (Wired and Wireless) for any given point of time.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        siteId:
          description: It is the client health's siteId.
          returned: always
          type: str
          sample: '<siteid>'
        scoreDetail:
          description: It is the client health's scoreDetail.
          returned: always
          type: list
          contains:
            scoreCategory:
              description: It is the client health's scoreCategory.
              returned: always
              type: dict
              contains:
                scoreCategory:
                  description: It is the client health's scoreCategory.
                  returned: always
                  type: str
                  sample: '<scorecategory>'
                value:
                  description: It is the client health's value.
                  returned: always
                  type: str
                  sample: '<value>'

            scoreValue:
              description: It is the client health's scoreValue.
              returned: always
              type: int
              sample: 0
            clientCount:
              description: It is the client health's clientCount.
              returned: always
              type: int
              sample: 0
            clientUniqueCount:
              description: It is the client health's clientUniqueCount.
              returned: always
              type: int
              sample: 0
            starttime:
              description: It is the client health's starttime.
              returned: always
              type: int
              sample: 0
            endtime:
              description: It is the client health's endtime.
              returned: always
              type: int
              sample: 0
            scoreList:
              description: It is the client health's scoreList.
              returned: always
              type: list
              contains:
                scoreCategory:
                  description: It is the client health's scoreCategory.
                  returned: always
                  type: dict
                  contains:
                    scoreCategory:
                      description: It is the client health's scoreCategory.
                      returned: always
                      type: str
                      sample: '<scorecategory>'
                    value:
                      description: It is the client health's value.
                      returned: always
                      type: str
                      sample: '<value>'

                scoreValue:
                  description: It is the client health's scoreValue.
                  returned: always
                  type: int
                  sample: 0
                clientCount:
                  description: It is the client health's clientCount.
                  returned: always
                  type: int
                  sample: 0
                clientUniqueCount:
                  description: It is the client health's clientUniqueCount.
                  returned: always
                  type: int
                  sample: 0
                starttime:
                  description: It is the client health's starttime.
                  returned: always
                  type: int
                  sample: 0
                endtime:
                  description: It is the client health's endtime.
                  returned: always
                  type: int
                  sample: 0
                scoreList:
                  description: It is the client health's scoreList.
                  returned: always
                  type: list
                  contains:
                    scoreCategory:
                      description: It is the client health's scoreCategory.
                      returned: always
                      type: dict
                      contains:
                        scoreCategory:
                          description: It is the client health's scoreCategory.
                          returned: always
                          type: str
                          sample: '<scorecategory>'
                        value:
                          description: It is the client health's value.
                          returned: always
                          type: str
                          sample: '<value>'

                    scoreValue:
                      description: It is the client health's scoreValue.
                      returned: always
                      type: int
                      sample: 0
                    clientCount:
                      description: It is the client health's clientCount.
                      returned: always
                      type: int
                      sample: 0
                    clientUniqueCount:
                      description: It is the client health's clientUniqueCount.
                      returned: always
                      type: dict
                    starttime:
                      description: It is the client health's starttime.
                      returned: always
                      type: int
                      sample: 0
                    endtime:
                      description: It is the client health's endtime.
                      returned: always
                      type: int
                      sample: 0





"""
