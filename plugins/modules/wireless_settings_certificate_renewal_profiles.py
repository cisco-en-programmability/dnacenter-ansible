#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_settings_certificate_renewal_profiles
short_description: Resource module for Wireless Settings Certificate Renewal Profiles
description:
  - Manage operations create, update and delete of the resource Wireless Settings Certificate Renewal Profiles.
  - This API is used to Create LSC Certificate Renewal Profile.
  - Delete LSC Certificate Renewal Profile by ID.
  - This API allows users to update access point certificate renewal profiles by profile ID.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  CalendarProfileSetting:
    description: Wireless Settings Certificate Renewal Profiles's CalendarProfileSetting.
    suboptions:
      duration:
        description: Wireless Settings Certificate Renewal Profiles's duration.
        suboptions:
          schedulerDate:
            description: Dates in a month (1 to 31) on which execution is scheduled. If the specified date does not exist
              in that month, no execution will be triggered for that date. For example, on the dates 1, 10, 30 in February,
              execution would occur only on dates 1 and 10.
            type: str
          schedulerDay:
            description: List of days in a week on which certificate renewal has to be scheduled. Example SUNDAY, MONDAY,
              TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATERDAY.
            elements: str
            type: list
          schedulerEndTime:
            description: End time on the wireless controller at which the scheduler should stop any execution. Format HH MM
              in 24-hour notation. Example 23 59.
            type: str
          schedulerStartTime:
            description: Start time on the wireless controller at which the scheduler should begin any execution. Format HH
              MM in 24-hour notation. Example 13 00.
            type: str
        type: dict
      schedulerType:
        description: Type of scheduler (e.g., DAILY, WEEKLY, MONTHLY) * DAILY schedule requires a schedulerStartTime input
          and an optional schedulerEndTime in the duration. * WEEKLY schedule requires schedulerDay input in the duration
          along with a schedulerStartTime input and an optional schedulerEndTime in the duration. * MONTHLY schedule requires
          schedulerDate input in the duration along with a schedulerStartTime input and an optional schedulerEndTime in the
          duration.
        type: str
    type: dict
  id:
    description: Id path parameter. LSC Certificate Renewal Profile ID.
    type: str
  lscProfileName:
    description: Name of the LSC profile.
    type: str
  renewalDueInDays:
    description: Type of renewal (e.g., ONESHOT, STAGGERED) * STAGGERED execution when configured with calendarProfileSetting
      requires both start time and end time input from scheduler. STAGGERED execution also requires a percentage input which
      specifies the percentage of access points that can be considered for certificate renewal per iteration. * ONESHOT execution
      when configured with calendarProfileSetting requires a start time input. ONESHOT execution does not need percentage
      input as all the access points certificate renewal happens at oneshot.
    type: int
  renewalType:
    description: Type of renewal (e.g., ONESHOT, STAGGERED) * STAGGERED execution when configured with calendarProfileSetting
      requires both start time and end time input from scheduler. STAGGERED execution also requires a percentage input which
      specifies the percentage of access points that can be considered for certificate renewal per iteration. * ONESHOT execution
      when configured with calendarProfileSetting requires a start time input. ONESHOT execution does not need percentage
      input as all the access points certificate renewal happens at oneshot.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Wireless CreateLSCCertificateRenewalProfile
    description: Complete reference of the CreateLSCCertificateRenewalProfile API.
    link: https://developer.cisco.com/docs/dna-center/#!create-lsc-certificate-renewal-profile
  - name: Cisco DNA Center documentation for Wireless DeleteLSCCertificateRenewalProfileByID
    description: Complete reference of the DeleteLSCCertificateRenewalProfileByID API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-lsc-certificate-renewal-profile-by-id
  - name: Cisco DNA Center documentation for Wireless UpdateLSCCertificateRenewalProfile
    description: Complete reference of the UpdateLSCCertificateRenewalProfile API.
    link: https://developer.cisco.com/docs/dna-center/#!update-lsc-certificate-renewal-profile
notes:
  - SDK Method used are
    wireless.Wireless.create_l_s_c_certificate_renewal_profile,
    wireless.Wireless.delete_l_s_c_certificate_renewal_profile_by_id,
    wireless.Wireless.update_l_s_c_certificate_renewal_profile,
  - Paths used are
    post /dna/intent/api/v1/wirelessSettings/certificateRenewalProfiles,
    delete /dna/intent/api/v1/wirelessSettings/certificateRenewalProfiles/{id},
    put /dna/intent/api/v1/wirelessSettings/certificateRenewalProfiles/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.dnac.wireless_settings_certificate_renewal_profiles:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    CalendarProfileSetting:
      duration:
        schedulerDate: string
        schedulerDay:
          - string
        schedulerEndTime: string
        schedulerStartTime: string
      schedulerType: string
    lscProfileName: string
    renewalDueInDays: 0
    renewalType: string
- name: Delete by id
  cisco.dnac.wireless_settings_certificate_renewal_profiles:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string
- name: Update by id
  cisco.dnac.wireless_settings_certificate_renewal_profiles:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    CalendarProfileSetting:
      duration:
        schedulerDate: string
        schedulerDay:
          - string
        schedulerEndTime: string
        schedulerStartTime: string
      schedulerType: string
    id: string
    lscProfileName: string
    renewalDueInDays: 0
    renewalType: string
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
