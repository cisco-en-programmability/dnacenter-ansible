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
module: integration_event
short_description: Manage IntegrationEvent objects of Itsm
description:
- Used to retrieve the list of integration events that failed to create tickets in ITSM.
- Allows retry of multiple failed ITSM event instances. The retry request payload can be given as a list of strings: ["instance1","instance2","instance3",..] A minimum of one instance Id is mandatory. The list of failed event instance Ids can be retrieved using the 'Get Failed ITSM Events' API in the 'instanceId' attribute.
version_added: '1.0'
author: Rafael Campos (@racampos)
options:
  instance_id:
    description:
    - Instance Id of the failed event as in the Runtime Dashboard.
    type: str
  payload:
    description:
    - An object to send in the Request body.
    - Required for state create.
    type: list

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.integration_event
# Reference by Internet resource
- name: IntegrationEvent reference
  description: Complete reference of the IntegrationEvent object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: IntegrationEvent reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_failed_itsm_events
  cisco.dnac.integration_event:
    state: query  # required
    instance_id: SomeValue  # string
  register: query_result
  
- name: retry_integration_events
  cisco.dnac.integration_event:
    state: create  # required
    payload:  # required
    - SomeValue  # string
  
"""

RETURN = """
get_failed_itsm_events:
    description: Used to retrieve the list of integration events that failed to create tickets in ITSM.
    returned: always
    type: dict
    contains:
    payload:
      description: It is the integration event's payload.
      returned: always
      type: list
      contains:
        instanceId:
          description: It is the integration event's instanceId.
          returned: always
          type: str
          sample: '<instanceid>'
        eventId:
          description: It is the integration event's eventId.
          returned: always
          type: str
          sample: '<eventid>'
        name:
          description: It is the integration event's name.
          returned: always
          type: str
          sample: '<name>'
        type:
          description: It is the integration event's type.
          returned: always
          type: str
          sample: '<type>'
        category:
          description: It is the integration event's category.
          returned: always
          type: str
          sample: '<category>'
        domain:
          description: It is the integration event's domain.
          returned: always
          type: str
          sample: '<domain>'
        subDomain:
          description: It is the integration event's subDomain.
          returned: always
          type: str
          sample: '<subdomain>'
        severity:
          description: It is the integration event's severity.
          returned: always
          type: str
          sample: '<severity>'
        source:
          description: It is the integration event's source.
          returned: always
          type: str
          sample: '<source>'
        timestamp:
          description: It is the integration event's timestamp.
          returned: always
          type: int
          sample: 0
        enrichmentInfo:
          description: It is the integration event's enrichmentInfo.
          returned: always
          type: dict
          contains:
            eventStatus:
              description: It is the integration event's eventStatus.
              returned: always
              type: str
              sample: '<eventstatus>'
            errorCode:
              description: It is the integration event's errorCode.
              returned: always
              type: str
              sample: '<errorcode>'
            errorDescription:
              description: It is the integration event's errorDescription.
              returned: always
              type: str
              sample: '<errordescription>'
            responseReceivedFromITSMSystem:
              description: It is the integration event's responseReceivedFromITSMSystem.
              returned: always
              type: dict

        description:
          description: It is the integration event's description.
          returned: always
          type: str
          sample: '<description>'


retry_integration_events:
    description: Allows retry of multiple failed ITSM event instances. The retry request payload can be given as a list of strings: ["instance1","instance2","instance3",..] A minimum of one instance Id is mandatory. The list of failed event instance Ids can be retrieved using the 'Get Failed ITSM Events' API in the 'instanceId' attribute.
    returned: success
    type: dict
    contains:
    executionId:
      description: Execution Id, property of the response body.
      returned: success
      type: str
      sample: '<executionid>'
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: success
      type: str
      sample: '<executionstatusurl>'
    message:
      description: Message, property of the response body.
      returned: success
      type: str
      sample: '<message>'

"""
