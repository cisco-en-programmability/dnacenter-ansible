#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to manage Access Point to the planned locations
in Cisco Catalyst Center, and assign the access point to floor plans."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ["A Mohamed Rafeek, Madhan Sankaranarayanan"]

DOCUMENTATION = r"""
---
module: accesspoint_location_workflow_manager
short_description: Resource module for managing Access Point planned locations and assigned positions in Cisco Catalyst Center
description: >
  This module facilitates the creation, update, assignment and deletion of Access Point planned locations
  in Cisco Catalyst Center.
  - Supports creating, assigning and deleting Access Point planned locations.
  - Enables assignment of the access point to floor plans.
version_added: "6.40.0"
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - A Mohamed Rafeek (@mabdulk2)
  - Madhan Sankaranarayanan (@madhansansel)
options:
  config_verify:
    description: >
      Set to `True` to enable configuration verification on Cisco Catalyst Center after applying the playbook configuration.
      This ensures that the system validates the configuration state after the changes are applied.
    type: bool
    default: false
  state:
    description: >
      Specifies the desired state for the configuration.
      If set to `merged`, the module will create or update the configuration by adding new settings or modifying existing ones.
      If set to `deleted`, the module will remove the specified settings.
    type: str
    choices: ["merged", "deleted"]
    default: merged
  config:
    description: >
      A list containing the details required for creating or updating the Access Point planned location.
    type: list
    elements: dict
    required: true
    suboptions:
      floor_site_hierarchy:
        description: >
          Complete floor site hierarchy for the access point location.
        type: str
        required: true
      access_points:
        description: >
          List of access points to be configured at the specified location.
        type: list
        elements: dict
        required: true
        suboptions:
          accesspoint_name:
            description: >
              Name of the access point to be assigned to the location.
            type: str
            required: true
          action:
            description: >
              The action to be performed on the access point.
              Determines how the access point will be managed within the specified location.
              This field is only required when assigning or deleting the access point to/from an existing planned location.
              It is not required when creating, updating, or deleting a planned access point location itself.
            type: str
            required: true
            choices:
              - C(assign_planned)
              - C(delete_position)
          mac_address:
            description: |
              The MAC address used to identify the access point.
            type: str
            required: false
          accesspoint_model:
            description: Model of the access point.
            type: str
            required: true
          position:
            description: |
              The X,Y and Z coordinates representing the access point's position on the floor plan.
            type: dict
            suboptions:
              x_position:
                description: >
                  The X coordinate of the access point's position. allows from 0 to 100
                type: int
                required: true
              y_position:
                description: >
                  The Y coordinate of the access point's position. allows from 0 to 88
                type: int
                required: true
              z_position:
                description: >
                  The Z coordinate of the access point's position. allows from 3.0 to 10.0
                type: float
                required: true
          radios:
            description: |
              List of radio details for the access point.
            type: list
            elements: dict
            required: true
            suboptions:
              bands:
                description: |
                  Radio band supported by the access point.
                type: str
                required: true
                choices:
                  - C(2.4GHz)
                  - C(5GHz)
                  - C(6GHz)
              channel:
                description: |
                  The channel number for the radio interface.
                  - For C(2.4GHz): valid values are 1 to 14.
                  - For C(5GHz): valid values are
                    36, 40, 44, 48, 52, 56, 60, 64,
                    100, 104, 108, 112, 116, 120, 124,
                    128, 132, 136, 140, 144, 149, 153,
                    157, 161, 165, 169, 173.
                  - For C(6GHz): valid values are
                    1, 5, 9, 13, 17, 21, 25, 29, 33, 37,
                    41, 45, 49, 53, 57, 61, 65, 69, 73,
                    77, 81, 85, 89, 93, 97, 101, 105,
                    109, 113, 117, 121, 125, 129, 133,
                    137, 141, 145, 149, 153, 157, 161,
                    165, 169, 173, 177, 181, 185, 189,
                    193, 197, 201, 205, 209, 213, 217,
                    221, 225, 229, 233.
                type: int
                required: true
              tx_power:
                description: |
                  The transmit power level of the access point.
                type: int
                required: true
              antenna:
                description: |
                  Antenna configuration details of the access point.
                type: dict
                required: true
                suboptions:
                  antenna_name:
                    description: |
                      Model name of the antenna.
                    type: str
                    required: true
                  azimuth:
                    description: |
                      The azimuth angle of the antenna, ranging from 1 to 360.
                    type: int
                    required: true
                  elevation:
                    description: |
                      The elevation angle of the antenna, ranging from -90 to 90.
                    type: int
                    required: true
requirements:
  - dnacentersdk >= 2.8.6
  - python >= 3.9
seealso:
  - name: Cisco Catalyst Center API Documentation
    description: Complete API reference for device management.
    link: https://developer.cisco.com/docs/dna-center/
notes:
    # Version Compatibility
  - Minimum Catalyst Center version 3.1.3.0 required for accesspoint location workflow features.

  - This module utilizes the following SDK methods
    site_design.SiteDesign.get_planned_access_points_positions
    site_design.SiteDesign.add_planned_access_points_positions
    site_design.SiteDesign.edit_planned_access_points_positions
    site_design.SiteDesign.delete_planned_access_points_position
    site_design.SiteDesign.assign_planned_access_points_to_operations_ones
    site_design.SiteDesign.edit_the_access_points_positions
    site_design.SiteDesign.get_access_points_positions
    site_design.SiteDesign.get_sites

  - The following API paths are used
    GET /dna/intent/api/v2/floors/${floorId}/plannedAccessPointPositions
    GET /dna/intent/api/v1/sites
    GET /dna/intent/api/v2/floors/${floorId}/accessPointPositions
    POST /dna/intent/api/v2/floors/${floorId}/plannedAccessPointPositions/${id}
    POST /dna/intent/api/v2/floors/${floorId}/plannedAccessPointPositions/bulk
    POST /dna/intent/api/v2/floors/${floorId}/accessPointPositions/bulkChange
    POST /dna/intent/api/v2/floors/${floorId}/plannedAccessPointPositions/bulkChange
    POST /dna/intent/api/v2/floors/${floorId}/plannedAccessPointPositions/assignAccessPointPositions

"""

EXAMPLES = r"""
---
- hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Create planned access point location for the access points
      cisco.dnac.accesspoint_location_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        config_verify: true
        dnac_api_task_timeout: 1000
        dnac_task_poll_interval: 1
        state: merged
        config:  # Minimum 1; Maximum 100 config hierarchy
          - floor_site_hierarchy: "Global/USA/California/SAN JOSE/BLD24/Floor3"
            access_points:
              - accesspoint_name: IAC-TB4-SJ-AP1
                mac_address: 54:8a:ba:22:eb:c0  # Optional
                accesspoint_model: CW9172H
                position:
                  x_position: 30  # x-axis: from 0 to 100
                  y_position: 20  # y-axis: from 0 to 88
                  z_position: 8  # height: from 3.0 to 10
                radios:  # Minimum Items: 1; Maximum Items: 4
                  - bands: 2.4GHz  # can be 5Ghz and 6GHz
                    channel: 10
                    tx_power: 5  # Decibel milliwatts (dBm)
                    antenna:
                      antenna_name: Internal-CW9172H-x-2.4GHz
                      azimuth: 1  # support upto 360
                      elevation: 30  # support -90 upto 90
                  - bands: 5GHz  # can be 5Ghz and 6GHz
                    channel: 40
                    tx_power: 6  # Decibel milliwatts (dBm)
                    antenna:
                      antenna_name: Internal-CW9172H-x-5GHz
                      azimuth: 1  # support upto 360
                      elevation: 30  # support -90 upto 90

    - name: Create planned access point floor location and assign the access points
      cisco.dnac.accesspoint_location_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        config_verify: true
        dnac_api_task_timeout: 1000
        dnac_task_poll_interval: 1
        state: merged
        config:  # Minimum 1; Maximum 100 config hierarchy
          - floor_site_hierarchy: "Global/USA/California/SAN JOSE/BLD24/Floor3"
            access_points:
              - accesspoint_name: IAC-TB4-SJ-AP1
                action: assign_planned  # Assign the planned location to the access point
                mac_address: 54:8a:ba:22:eb:c0  # Optional
                accesspoint_model: CW9172H
                position:
                  x_position: 30  # x-axis: from 0 to 100
                  y_position: 20  # y-axis: from 0 to 88
                  z_position: 8  # height: from 3.0 to 10
                radios:  # Minimum Items: 1; Maximum Items: 4
                  - bands: 2.4GHz  # can be 5Ghz and 6GHz
                    channel: 10
                    tx_power: 5  # Decibel milliwatts (dBm)
                    antenna:
                      antenna_name: Internal-CW9172H-x-2.4GHz
                      azimuth: 1  # support upto 360
                      elevation: 30  # support -90 upto 90
                  - bands: 5GHz  # can be 5Ghz and 6GHz
                    channel: 40
                    tx_power: 6  # Decibel milliwatts (dBm)
                    antenna:
                      antenna_name: Internal-CW9172H-x-5GHz
                      azimuth: 1  # support upto 360
                      elevation: 30  # support -90 upto 90

    - name: Update planned access point location for the access points
      cisco.dnac.accesspoint_location_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        config_verify: true
        dnac_api_task_timeout: 1000
        dnac_task_poll_interval: 1
        state: merged
        config:  # Minimum 1; Maximum 100 config hierarchy
          - floor_site_hierarchy: "Global/USA/California/SAN JOSE/BLD24/Floor3"
            access_points:
              - accesspoint_name: IAC-TB4-SJ-AP1
                mac_address: 54:8a:ba:22:eb:c0  # Optional
                accesspoint_model: CW9172H
                position:
                  x_position: 30  # x-axis: from 0 to 100
                  y_position: 20  # y-axis: from 0 to 88
                  z_position: 8  # height: from 3.0 to 10
                radios:  # Minimum Items: 1; Maximum Items: 4
                  - bands: 2.4GHz  # can be 5Ghz and 6GHz
                    channel: 10
                    tx_power: 5  # Decibel milliwatts (dBm)
                    antenna:
                      antenna_name: Internal-CW9172H-x-2.4GHz
                      azimuth: 10  # support upto 360
                      elevation: 30  # support -90 upto 90
                  - bands: 5GHz  # can be 5Ghz and 6GHz
                    channel: 40
                    tx_power: 6  # Decibel milliwatts (dBm)
                    antenna:
                      antenna_name: Internal-CW9172H-x-5GHz
                      azimuth: 10  # support upto 360
                      elevation: 30  # support -90 upto 90

    # Delete planned access point location for the access points
    - name: Delete planned access point location for the access points
      cisco.dnac.accesspoint_location_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        config_verify: true
        dnac_api_task_timeout: 1000
        dnac_task_poll_interval: 1
        state: deleted
        config:  # Minimum 1; Maximum 100 config hierarchy
          - floor_site_hierarchy: "Global/USA/California/SAN JOSE/BLD24/Floor3"
            access_points:
              - accesspoint_name: IAC-TB4-SJ-AP1

    # Assign the access point to existing access points planned location.
    - name: Assign the access point to existing access points planned location.
      cisco.dnac.accesspoint_location_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        config_verify: true
        dnac_api_task_timeout: 1000
        dnac_task_poll_interval: 1
        state: merged
        config:  # Minimum 1; Maximum 100 config hierarchy
          - floor_site_hierarchy: "Global/USA/California/SAN JOSE/BLD24/Floor3"
            access_points:
              - accesspoint_name: IAC-TB4-SJ-AP1
                action: assign_planned  # Assign the planned location to the access point
                mac_address: 54:8a:ba:22:eb:c0  # Optional
                accesspoint_model: CW9172H
                position:
                  x_position: 30  # x-axis: from 0 to 100
                  y_position: 20  # y-axis: from 0 to 88
                  z_position: 8  # height: from 3.0 to 10
                radios:  # Minimum Items: 1; Maximum Items: 4
                  - bands: 2.4GHz  # can be 5Ghz and 6GHz
                    channel: 10
                    tx_power: 5  # Decibel milliwatts (dBm)
                    antenna:
                      antenna_name: Internal-CW9172H-x-2.4GHz
                      azimuth: 1  # support upto 360
                      elevation: 30  # support -90 upto 90
                  - bands: 5GHz  # can be 5Ghz and 6GHz
                    channel: 40
                    tx_power: 6  # Decibel milliwatts (dBm)
                    antenna:
                      antenna_name: Internal-CW9172H-x-5GHz
                      azimuth: 1  # support upto 360
                      elevation: 30  # support -90 upto 90

    # Delete assigned access point from the floor location
    - name: Unassign the access point from the floor location
      cisco.dnac.accesspoint_location_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        config_verify: true
        dnac_api_task_timeout: 1000
        dnac_task_poll_interval: 1
        state: deleted
        config:  # Minimum 1; Maximum 100 config hierarchy
          - floor_site_hierarchy: "Global/USA/California/SAN JOSE/BLD24/Floor3"
            access_points:
              - accesspoint_name: IAC-TB4-SJ-AP1
                action: delete_position  # Delete the access point from the floor location
"""

RETURN = r"""
# Case 1: Create planned access point location for the access points
response_create:
  description: >
    A dictionary or list containing the response returned by the Cisco Catalyst Center Python SDK
    when a access point planned location is successfully created. The response confirms the successful
    creation of the planned location and provides details about the status, including its access point name
    and status.
  returned: always
  type: dict
  sample: >
    {
        "msg": "Access Point Location created successfully for 'Global/USA/California/SAN JOSE/BLD24/Floor3'.",
        "response": [
            [
                "IAC-TB4-SJ-AP1"
            ]
        ],
        "status": "success"
    }

# Case 2: Create planned access point floor location and assign the access points
response_create_assign:
  description: >
    A dictionary or list containing the response returned by the Cisco Catalyst Center Python SDK
    when a access point planned location is successfully created and assigned. The response confirms
    the successful creation of the planned location and provides details about the status,
    including its access point name and status.
  returned: always
  type: dict
  sample: >
    {
        "msg": "Access Point Location created successfully for 'Global/USA/California/SAN JOSE/BLD24/Floor3'.
                Following Access Point(s) assigned to planned location(s): '['IAC-TB4-SJ-AP1']'.",
        "response": [
            [
                "IAC-TB4-SJ-AP1"
            ]
        ],
        "status": "success"
    }

# Case 3: Idempotent Create planned access point location for the accesspoint
response_create_idempotent:
  description: >
    A dictionary or list containing the response returned by the Cisco Catalyst Center Python SDK.
    This response is provided when attempting to create planned access point locations in an idempotent manner.
    If the locations are already created, the response indicates that no changes were required.
  returned: always
  type: dict
  sample: >
    {
        "msg": "No Changes required, Access Point Location(s) already exist. Following Access Point Location(s): 'IAC-TB4-SJ-AP1' already exist.",
        "response": [],
        "status": "success"
    }

# Case 4: Update planned access point location for the access points
response_update_location:
  description: >
    A dictionary or list containing the response returned by the Cisco Catalyst Center Python SDK
    when a planned access point location is successfully updated. The response confirms the
    update and provides details about the updated location.
  returned: always
  type: dict
  sample: >
    {
        "msg": "Access Point Location updated successfully for 'Global/USA/California/SAN JOSE/BLD24/Floor3'.",
        "response": [
            [
                "IAC-TB4-SJ-AP1"
            ]
        ],
        "status": "success"
    }

# Case 5: Successfully deleted the planned access point location
response_delete_planned_location:
  description: >
    A dictionary or list containing the response returned by the Cisco Catalyst Center Python SDK
    when a planned access point location is successfully deleted. The response confirms the
    deletion and provides details about the location and access point(s) affected.
  returned: always
  type: dict
  sample: >
    {
        "msg": "Access Point planned Location(s) deleted and verified successfully for '['IAC-TB4-SJ-AP1']'.",
        "response": [
            "IAC-TB4-SJ-AP1"
        ],
        "status": "success"
    }

# Case 6: Idempotent delete the planned access point location
response_unassign_template:
  description: >
    A dictionary or list containing the response returned by the Cisco Catalyst Center Python SDK
    when a template is successfully unassigned from a switch profile. The response confirms the
    unassignment and provides details about the profile and the template(s) affected.
  returned: always
  type: dict
  sample: >
    {
        "msg": "No Changes required, Access Point Location(s) already deleted
                and verified successfully for '['IAC-TB4-SJ-AP1']'.",
        "response": [],
        "status": "success"
    }

# Case 7: Assign the access point to existing access points planned location.
response_create_assign_idempotent:
  description: >
    A dictionary or list containing the response returned by the Cisco Catalyst Center Python SDK
    when a access point planned location is successfully created and assigned. The response confirms
    the successful creation of the planned location and provides details about the status,
    including its access point name and status.
  returned: always
  type: dict
  sample: >
    {
        "msg": "No Changes required, Access Point Location(s) already exist.
                Following Access Point(s) assigned to planned location(s): '['IAC-TB4-SJ-AP1']'.
                Following Access Point Location(s): 'None' already exist.",
        "response": [],
        "status": "success"
    }

# Case 8: Unassign the access point from existing access points planned location.
response_unassign_idempotent:
  description: >
    A dictionary or list containing the response returned by the Cisco Catalyst Center Python SDK
    when a access point planned location is successfully unassigned. The response confirms
    the successful unassignment of the planned location and provides details about the status,
    including its access point name and status.
  returned: always
  type: dict
  sample: >
    {
        "msg": "Access Point planned/assigned Location(s) deleted and verified successfully for '['IAC-TB4-SJ-AP1']'.",
        "response": [
            "IAC-TB4-SJ-AP1"
        ],
        "status": "success"
    }
"""


import time
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
 #   validate_list_of_dicts,
    validate_str,
)
from ansible_collections.cisco.dnac.plugins.module_utils.validation import (
    validate_list_of_dicts,
)
from ansible.module_utils.basic import AnsibleModule


class AccessPointLocation(DnacBase):
    """Class containing member attributes for network profile workflow manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged", "deleted"]
        self.location_created, self.location_updated, self.location_deleted = [], [], []
        self.location_not_created, self.location_not_updated, self.location_not_deleted = [], [], []
        self.location_exist, self.location_already_deleted = [], []
        self.location_assigned, self.location_not_assigned, self.location_already_assigned = [], [], []

        self.result_response = {
            "success_responses": self.location_created,
            "unprocessed": self.location_not_created,
            "already_processed": self.location_exist
        }

        self.keymap = {
            "accesspoint_name": "name",
            "mac_address": "macAddress",
            "accesspoint_model": "type",
            "position": "position",
            "radios": "radios",
            "x_position": "x",
            "y_position": "y",
            "z_position": "z",
            "bands": "bands",
            "channel": "channel",
            "tx_power": "txPower",
            "antenna": "antenna",
            "antenna_name": "name",
            "azimuth": "azimuth",
            "elevation": "elevation"
        }

    def validate_input(self):
        """
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.

        Parameters:
            self: The instance of the class containing the 'config' attribute to be validated.

        Returns:
            The method updates these attributes of the instance:
                - msg: A message describing the validation result.
                - self.status: The status of the validation ('success' or 'failed').
                - self.validated_config: If successful, a validated version of the 'config' parameter.
        """
        temp_spec = {
            "floor_site_hierarchy": {"type": "str", "required": True},
            "access_points": {
                "type": "list",
                "elements": "dict",
                "accesspoint_name": {"type": "str", "required": True},
                "action": {"type": "str", "required": False,
                           "choices": ["assign_planned", "delete_position"]},
                "mac_address": {"type": "str"},
                "serial_number": {"type": "str"},
                "accesspoint_model": {"type": "str", "required": True},
                "position": {
                    "type": "dict",
                    "x_position": {"type": "int", "required": True},
                    "y_position": {"type": "int", "required": True},
                    "z_position": {"type": "int", "required": True},
                },
                "radios": {
                    "type": "list",
                    "elements": "dict",
                    "bands": {"type": "str", "required": True},
                    "channel": {"type": "int", "required": True},
                    "tx_power": {"type": "int", "required": True},
                    "antenna": {
                        "type": "dict",
                        "antenna_name": {"type": "str", "required": True},
                        "azimuth": {"type": "int", "required": True},
                        "elevation": {"type": "int", "required": True},
                    },
                },
            },
        }

        if not self.config:
            msg = "The playbook configuration is empty or missing."
            self.set_operation_result("failed", False, msg, "ERROR")
            return self

        # Validate configuration against the specification
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            msg = f"The playbook contains invalid parameters: {invalid_params}"
            self.result["response"] = msg
            self.set_operation_result("failed", False, msg, "ERROR")
            return self

        self.validated_config = valid_temp
        msg = f"Successfully validated playbook configuration parameters using 'validate_input': {self.pprint(valid_temp)}"
        self.log(msg, "INFO")

        return self

    def input_data_validation(self, config):
        """
        Additional validation to check if the provided input switch profile is correct
        and as per the UI Cisco Catalyst Center.

        Parameters:
            self (object): An instance of a class for interacting with Cisco Catalyst Center.
            config (dict): Dictionary containing the Access point planned location details.

        Returns:
            list: List of invalid access point location data with details.

        Description:
            Iterates through available access point location details and Returns the list of invalid
            data for further action or validation.
        """
        self.log(
            f"Validating input data from Playbook config: {config}", "INFO"
        )
        errormsg = []

        floor_site_hierarchy = config.get("floor_site_hierarchy", "")
        if floor_site_hierarchy:
            param_spec = dict(type="str", length_max=200)
            validate_str(floor_site_hierarchy, param_spec, "floor_site_hierarchy", errormsg)
        else:
            errormsg.append("floor_site_hierarchy: Floor Site Hierarchy is missing in playbook.")

        access_points = config.get("access_points", [])
        if not access_points:
            errormsg.append("access_points: Access Points list is missing in playbook.")
            return errormsg
        elif len(access_points) > 100:
            errormsg.append("access_points: Maximum of 100 Access Points are allowed in playbook.")
            return errormsg

        duplicate_name = self.find_duplicate_value(access_points, "accesspoint_name")
        if duplicate_name:
            errormsg.append(
                f"accesspoint_name: Duplicate Access Point Name(s) '{duplicate_name}' found in playbook."
            )

        for each_access_point in access_points:
            accesspoint_name = each_access_point.get("accesspoint_name")
            if accesspoint_name:
                param_spec = dict(type="str", length_max=255)
                validate_str(accesspoint_name, param_spec, "accesspoint_name", errormsg)
            else:
                errormsg.append("accesspoint_name: Access Point Name is missing in playbook.")

            if self.params.get("state") == "deleted":
                continue

            mac_address = each_access_point.get("mac_address")
            if mac_address:
                param_spec = dict(type="str", length_max=17)
                validate_str(mac_address, param_spec, "mac_address", errormsg)

            serial_number = each_access_point.get("serial_number")
            if serial_number:
                param_spec = dict(type="str", length_max=200)
                validate_str(serial_number, param_spec, "serial_number", errormsg)

            accesspoint_model = each_access_point.get("accesspoint_model")
            if accesspoint_model:
                param_spec = dict(type="str", length_max=50)
                validate_str(accesspoint_model, param_spec, "accesspoint_model", errormsg)
            else:
                errormsg.append("accesspoint_model: Access Point Model is missing in playbook.")

            position = each_access_point.get("position")
            if position and isinstance(position, dict):
                x_position = position.get("x_position")
                if x_position is None:
                    errormsg.append("x_position: X Position is missing in playbook.")
                elif x_position and isinstance(x_position, int) and not (0 < x_position < 100):
                    errormsg.append("x_position: X Position must be between 0 and 100.")

                y_position = position.get("y_position")
                if y_position is None:
                    errormsg.append("y_position: Y Position is missing in playbook.")
                elif y_position and isinstance(y_position, int) and not (0 < y_position < 88):
                    errormsg.append("y_position: Y Position must be between 0 and 88.")

                z_position = position.get("z_position")
                if z_position is None:
                    errormsg.append("z_position: Z Position is missing in playbook.")
                elif z_position and isinstance(z_position, (int, float)) and not (3 < z_position < 10):
                    errormsg.append("z_position: Z Position must be between 3 and 10.")

            radios = each_access_point.get("radios")
            if not radios:
                errormsg.append("radios: Radios is missing in playbook.")
            elif radios and isinstance(radios, list):
                self.validate_radios(radios, errormsg)

        if errormsg:
            self.msg = f"Invalid parameters in playbook config: {' '.join(errormsg)}"
            self.log(self.msg, "ERROR")
            self.fail_and_exit(self.msg)

        msg = f"Successfully validated config params: {str(config)}"
        self.log(msg, "INFO")
        return self

    def validate_radios(self, radios_param, errormsg):
        """
        Validate the radio configuration parameters.

        Parameters:
            self (object): An instance of a class for interacting with Cisco Catalyst Center.
            radios_param (list): A list of radio configuration dictionaries.
            errormsg (list): A list to collect error messages.

        Returns:
            list: List of invalid access point location radios data with details.

        Description:
            Iterates through available access point location radios details and Returns the list of invalid
            data for further action or validation.

        """
        self.log("Validating radio configuration parameters.", "DEBUG")

        if len(radios_param) > 4:
            errormsg.append("Maximum of 4 radio configuration parameters are allowed.")
            return errormsg

        for radio in radios_param:
            bands = radio.get("bands")
            if bands:
                param_spec = dict(type="str", length_max=6)
                validate_str(bands, param_spec, "bands", errormsg)
                if bands not in ["2.4GHz", "5GHz", "6GHz"]:
                    errormsg.append(
                        "bands: Bands must be one of '2.4GHz', '5GHz' or '6GHz'."
                    )
            else:
                errormsg.append("bands: Bands is missing in playbook.")

            channel = radio.get("channel")
            channel_5ghz = (
                list(range(36, 65, 4)) +
                list(range(100, 145, 4)) +
                [149, 153, 157, 161, 165, 169, 173]
            )
            channel_6ghz = list(range(1, 234, 4))
            if channel is None:
                errormsg.append("channel: Channel is missing in playbook.")
            elif channel and isinstance(channel, int):
                if bands == "2.4GHz" and not (0 < channel < 15):
                    errormsg.append("channel: Channel must be between 1 and 14 for 2.4GHz band.")
                elif bands == "5GHz" and channel not in channel_5ghz:
                    errormsg.append(
                        f"channel: Channel must be one of '{channel_5ghz}' for 5GHz band."
                    )
                elif bands == "6GHz" and channel not in channel_6ghz:
                    errormsg.append(
                        f"channel: Channel must be one of '{channel_6ghz}' for 6GHz band."
                    )

            tx_power = radio.get("tx_power")
            if tx_power is None:
                errormsg.append("tx_power: Tx Power is missing in playbook.")
            elif tx_power and isinstance(tx_power, int) and not (0 < tx_power < 101):
                errormsg.append("tx_power: Tx Power must be between 0 and 100.")

            antenna = radio.get("antenna")
            if antenna is None:
                errormsg.append("antenna: Antenna is missing in playbook.")
            elif antenna and isinstance(antenna, dict):
                antenna_name = antenna.get("antenna_name")
                if antenna_name:
                    param_spec = dict(type="str", length_max=50)
                    validate_str(antenna_name, param_spec, "name", errormsg)
                else:
                    errormsg.append("antenna_name: Antenna Name is missing in playbook.")

                azimuth = antenna.get("azimuth")
                if azimuth is None:
                    errormsg.append("azimuth: Azimuth is missing in playbook.")
                elif azimuth and isinstance(azimuth, int) and not (0 < azimuth < 361):
                    errormsg.append("azimuth: Azimuth must be between 1 and 360.")

                elevation = antenna.get("elevation")
                if elevation is None:
                    errormsg.append("elevation: Elevation is missing in playbook.")
                elif elevation and isinstance(elevation, int) and not (-91 < elevation < 91):
                    errormsg.append("elevation: Elevation must be between -90 and 90.")

        self.log("Radio configuration validation completed.", "DEBUG")
        return errormsg

    def get_want(self, config):
        """
        Retrieve access point planned location playbook config

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration dictionary containing access point location details.

        Returns:
            self: The current instance of the class with updated 'want' attributes.

        Description:
            This function parses the playbook configuration to extract information related
            to access point location profile. It stores these details in the 'want' dictionary
            for later use in the Ansible module.
        """
        self.log(f"Validating input data and update to want for: {config}", "INFO")

        self.input_data_validation(config).check_return_status()
        want = {}
        if config:
            want["ap_location"] = config

        self.want = want
        self.log(f"Desired State (want): {self.pprint(self.want)}", "INFO")

        return self

    def get_have(self, config):
        """
        Get required details for the given access point location config from Cisco Catalyst Center

        Parameters:
            config (dict) - Playbook details containing access point location

        Returns:
            self - The current object with site details and access point location
            information collection for create and update.
        """

        self.log(
            f"Collecting access point location related information for: {config}",
            "INFO",
        )

        response = self.get_site(config.get("floor_site_hierarchy"))
        if not response:
            msg = f"No response received from API for the site: {config.get('floor_site_hierarchy')}"
            self.log(msg, "WARNING")
            self.fail_and_exit(msg)

        site = response["response"][0]
        if not site.get("id"):
            msg = f"No site information found for: {config}"
            self.log(msg, "WARNING")
            self.fail_and_exit(msg)

        have = {
            "site_id": site["id"],
            "site_name": config.get("floor_site_hierarchy"),
            "antenna_patterns": self.get_map_supported_ap_antenna_patterns(),
            "selected_ap_model": [],
        }
        for access_point in config.get("access_points", []):

            if self.params.get("state") == "deleted":
                self.log(f"Access point marked for deletion: {access_point}", "INFO")
                continue

            selected_ap_model = self.find_dict_by_key_value(
                have["antenna_patterns"], "apType", access_point.get("accesspoint_model")
            )
            if not selected_ap_model:
                msg = f"No supported access point model found for: {access_point.get('accesspoint_model')}"
                self.log(msg, "WARNING")
                self.fail_and_exit(msg)
            self.log(f"Supported AP Model found: {self.pprint(selected_ap_model)}", "INFO")

            radios = access_point.get("radios")
            for radio in radios:
                band = radio.get("bands").split("GHz")[0]
                antenna_name = radio.get("antenna", {}).get("antenna_name")

                self.log(f"Finding radio band exist on supported AP model for: {band}", "INFO")
                band_exist = self.find_dict_by_key_value(
                    selected_ap_model.get("antennaPatterns"), "band", band
                )
                if not band_exist:
                    msg = f"No supported antenna pattern band found for: {band} {antenna_name}"
                    self.log(msg, "WARNING")
                    self.fail_and_exit(msg)
                self.log(f"Band exist: {self.pprint(band_exist)}", "DEBUG")

                self.log(f"Finding antenna name exist on supported AP model for: {antenna_name}", "INFO")
                if antenna_name not in band_exist.get("names"):
                    msg = f"No supported antenna name found for: {antenna_name}"
                    self.log(msg, "WARNING")
                    self.fail_and_exit(msg)
                self.log(f"Antenna name exist: {antenna_name} in {selected_ap_model.get('name')}", "DEBUG")

            have["selected_ap_model"].append(selected_ap_model)

        accesspoint_exists, new_accesspoint, update_accesspoint = [], [], []
        assigned_accesspoint = []
        access_point_devices = []
        delete_accesspoint = []
        for access_point in config.get("access_points", []):

            self.log(f"Retrieving accesspoint details for {access_point.get('accesspoint_name')}", "INFO")
            ap_device_details = self.get_accesspoint_details(access_point.get("accesspoint_name"))
            if not ap_device_details:
                msg = f"No device details found for access point: {access_point.get('accesspoint_name')}"
                self.log(msg, "WARNING")
                self.fail_and_exit(msg)
            access_point_devices.append(ap_device_details)

            ap_details = self.get_planned_ap_position(
                have["site_id"], have["site_name"], access_point
            )
            if not ap_details:
                ap_details = self.get_planned_ap_position(
                    have["site_id"], have["site_name"], access_point, True
                )
                if ap_details:
                    self.log(f"Access point planned position found for deletion: {access_point.get('accesspoint_name')}", "INFO")
                    if self.params.get("state") == "deleted":
                        ap_details[0]["action"] = access_point.get("action")
                        delete_accesspoint.append(ap_details[0])
                    else:
                        self.log(f"Access point planned position already exist: {access_point.get('accesspoint_name')}", "INFO")
                        assigned_accesspoint.append(ap_details[0])
                    continue

            if ap_details:
                if self.params.get("state") == "deleted":
                    self.log(f"Access point marked for deletion: {access_point}", "INFO")
                    ap_details[0]["action"] = access_point.get("action")
                    delete_accesspoint.append(ap_details[0])
                    continue

                ap_status, ap_update = self.compare_accesspoint_location_details(
                    ap_details[0], access_point)
                if ap_status:
                    self.log(f"Access point planned location already exist: {access_point.get('accesspoint_name')}", "INFO")
                    accesspoint_exists.append(access_point)
                else:
                    update_accesspoint.append(access_point)
            else:
                new_accesspoint.append(access_point)

        have.update({
            "accesspoint_devices": access_point_devices,
            "new_accesspoint": new_accesspoint,
            "update_accesspoint": update_accesspoint,
            "existing_accesspoint": accesspoint_exists,
            "delete_accesspoint": delete_accesspoint,
            "already_assigned_accesspoint": assigned_accesspoint,
        })
        self.have = have
        self.log(f"Current State (have): {self.pprint(self.have)}", "INFO")

        return self

    def get_map_supported_ap_antenna_patterns(self):
        """
        Get the supported access point antenna patterns from Cisco Catalyst Center.

        Parameters:
            None

        Returns:
            dict - A dictionary mapping antenna names to their details.
        """
        self.log("Collecting supported access point antenna patterns", "INFO")

        try:
            response = self.execute_get_request(
                "sites", "maps_supported_access_points", {}
            )
            if not response:
                msg = "No response received from API for supported access point antenna patterns."
                self.log(msg, "WARNING")
                self.fail_and_exit(msg)

            self.log(f"Supported Access Point Antenna Patterns API Response: {self.pprint(response)}", "DEBUG")

            return response

        except Exception as e:
            self.msg = 'An error occurred during get supported AP antenna patterns. '
            self.log(self.msg + str(e), "ERROR")
            self.fail_and_exit(self.msg)

    def get_planned_ap_position(self, floor_id, floor_name, ap_details, recheck=False):
        """
        Get the planned access point position from the playbook config.

        Parameters:
            floor_id (str) - The ID of the floor where the access point is located.
            floor_name (str) - The name of the floor where the access point is located.
            ap_details (dict) - The access point details from the playbook config.
            recheck (bool) - Flag to indicate if this is a recheck for deletion.

        Returns:
            dict - Planned access point position information
        """
        self.log(
            f"Collecting planned access point position for: {floor_name}",
            "INFO",
        )

        payload = {
            "offset": 1,
            "limit": 500,
            "floor_id": floor_id,
            "name": ap_details["accesspoint_name"]
        }

        function_name = None
        if (
            ap_details.get("action") in ["delete_position"]
            or recheck
        ):
            function_name = "get_access_points_positions"
        else:
            function_name = "get_planned_access_points_positions"

            if ap_details.get("accesspoint_model"):
                payload["type"] = ap_details["accesspoint_model"]

        try:
            response = self.execute_get_request(
                "site_design", function_name, payload
            )
            if not response:
                msg = f"No response received from API for the planned access point position: {ap_details}"
                self.log(msg, "WARNING")
                return None

            self.log(f"Planned Access Point Position API Response: {response}", "DEBUG")
            return response.get("response")

        except Exception as e:
            self.msg = 'An error occurred during get planned AP position. '
            self.log(self.msg + str(e), "ERROR")
            return None

    def compare_accesspoint_location_details(self, ap_details, access_point):
        """
        Compare the planned access point details with the actual access point details.

        Parameters:
            ap_details (dict) - Actual access point details.
            access_point (dict) - Planned access point details.

        Returns:
            bool - True if the details match, False otherwise.
            un_matched_value - List of unmatched values.
        """
        self.log(
            f"Comparing access point details: {self.pprint(access_point)} with existing details: {self.pprint(ap_details)}",
            "INFO",
        )

        compare_state = True
        un_matched_value = []
        # Compare relevant fields
        for key in ["accesspoint_name", "mac_address", "accesspoint_model"]:
            self.log(f"Comparing access point field '{key}': {access_point.get(key)} with {ap_details.get(self.keymap[key])}", "DEBUG")

            if access_point.get(key) != ap_details.get(self.keymap[key]):
                self.log(f"Access point details do not match for key: {key}", "INFO")
                un_matched_value.append((key, access_point.get(key), ap_details.get(self.keymap[key])))
                compare_state = False

        position = access_point.get("position", {})
        exist_position = ap_details.get("position", {})
        for key in ["x_position", "y_position", "z_position"]:
            self.log(f"Comparing access point position field '{key}': {position.get(key)} with {exist_position.get(self.keymap[key])}",
                     "DEBUG")

            if ((exist_position.get(self.keymap[key]) and position.get(key)) and
               float(position.get(key)) != float(exist_position.get(self.keymap[key]))):
                self.log(f"Access point position details do not match for key: {key}", "INFO")
                un_matched_value.append((key, position.get(key), exist_position.get(self.keymap[key])))
                compare_state = False

        radios = access_point.get("radios", [])
        exist_radios = ap_details.get("radios", [])
        self.log(
            f"Comparing access point radios: {self.pprint(radios)} with existing radios: {self.pprint(exist_radios)}",
            "INFO"
        )

        for radio in radios:
            for exist_radio in exist_radios:
                band = float(radio.get("bands").split("GHz")[0])
                self.log(
                    f"Finding radio band '{band}' exist on existing AP for: {exist_radio.get('bands', [])}",
                    "INFO"
                )

                if band in exist_radio.get("bands", []):
                    radio["id"] = exist_radio.get("id")
                    for key in ["channel", "tx_power", "antenna"]:
                        self.log(f"Comparing access point radio field '{key}': {radio.get(key)} with {exist_radio.get(self.keymap[key])}", "DEBUG")
                        if key == "antenna":
                            for ant_key in ["antenna_name", "azimuth", "elevation"]:
                                self.log(f"Comparing access point antenna field '{ant_key}': {radio.get('antenna', {}).get(ant_key)} with {exist_radio.get(self.keymap[key], {}).get(self.keymap[ant_key])}", "DEBUG")

                                if ant_key == "azimuth":
                                    current_azimuth = int(radio.get("antenna", {}).get(ant_key))
                                    existing_azimuth = int(exist_radio.get(self.keymap[key], {}).get(self.keymap[ant_key]))
                                    if band == 2.4:
                                        existing_azimuth = existing_azimuth + 1

                                    if current_azimuth != existing_azimuth:
                                        self.log(f"Access point antenna azimuth details do not match: {radio}", "INFO")
                                        radio["id"] = exist_radio.get("id")
                                        un_matched_value.append(("antenna", radio.get("antenna"), None))
                                        compare_state = False

                                if ant_key == "elevation":
                                    current_elevation = int(radio.get("antenna", {}).get(ant_key))
                                    existing_elevation = int(exist_radio.get(self.keymap[key], {}).get(self.keymap[ant_key]))
                                    if current_elevation != existing_elevation:
                                        self.log(f"Access point antenna elevation details do not match: {radio}", "INFO")
                                        radio["id"] = exist_radio.get("id")
                                        un_matched_value.append(("antenna", radio.get("antenna"), None))
                                        compare_state = False

                                if ant_key == "antenna_name":
                                    current_antenna_name = radio.get("antenna", {}).get(ant_key)
                                    existing_antenna_name = exist_radio.get(self.keymap[key], {}).get(self.keymap[ant_key])
                                    if current_antenna_name != existing_antenna_name:
                                        self.log(f"Access point antenna name does not match: {current_antenna_name}, with existing: {existing_antenna_name}", "INFO")
                                        radio["id"] = exist_radio.get("id")
                                        un_matched_value.append(("antenna", radio.get("antenna"), None))
                                        compare_state = False

                        elif radio.get(key) != exist_radio.get(self.keymap[key]):
                            self.log(f"Access point radio details do not match: {radio}", "INFO")
                            un_matched_value.append(("radios", radio, None))
                            compare_state = False

        if un_matched_value:
            access_point["planned_id"] = ap_details.get("id")
            self.log(f"Unmatched access point details found: {un_matched_value}", "WARNING")

        self.log(f"Access point details match for: {access_point}", "INFO")
        return compare_state, un_matched_value

    def get_accesspoint_details(self, accesspoint_name):
        """
        Retrieves the current details of an device in Cisco Catalyst Center.

        Parameters:
            self (object): An instance of the class containing the method.
            accesspoint_name (str): The name of the access point to retrieve details for.

        Returns:
            dict: A dictionary containing the current details of the access point, or an error message.

        """
        input_param = {
            "hostname": accesspoint_name
        }

        try:
            ap_response = self.dnac._exec(
                family="devices",
                function="get_device_list",
                op_modifies=True,
                params=input_param,
            )

            ap_response_data = ap_response.get("response") if ap_response else None

            if ap_response_data:
                self.log(f"Access point details found: {self.pprint(ap_response_data)}", "INFO")
                return ap_response_data[0]

        except Exception as e:
            self.msg = f"The provided device '{input_param}' is either invalid or not present in the Cisco Catalyst Center."
            self.log(f"{self.msg} {e}", "WARNING")
            return None

    def parse_planned_accesspoint(self, accesspoint):
        """
        Parse the access point details to match the API payload format.

        Parameters:
            accesspoint (dict) - Access point details from the playbook config.

        Returns:
            dict - Parsed access point details in API payload format.
        """
        self.log(f"Parsing access point details: {self.pprint(accesspoint)}", "INFO")

        parsed_params = {}
        if accesspoint.get("planned_id"):
            parsed_params["id"] = accesspoint.get("planned_id")

        # if not accesspoint.get("planned_id"):
        parsed_params["name"] = accesspoint.get("accesspoint_name")
        if accesspoint.get("mac_address"):
            parsed_params["macAddress"] = accesspoint.get("mac_address")

        parsed_params["type"] = accesspoint.get("accesspoint_model")

        position = accesspoint.get("position", {})
        parsed_params["position"] = {
            "x": position.get("x_position"),
            "y": position.get("y_position"),
            "z": position.get("z_position"),
        }

        radios_payload = []
        radios = accesspoint.get("radios", [])
        for radio in radios:
            radio_payload = {
                "bands": [radio.get("bands").split("GHz")[0]],
                "channel": radio.get("channel"),
                "txPower": radio.get("tx_power"),
                "antenna": {
                    "name": radio.get("antenna", {}).get("antenna_name"),
                    "azimuth": radio.get("antenna", {}).get("azimuth"),
                    "elevation": radio.get("antenna", {}).get("elevation"),
                },
            }

            if radio.get("id"):
                radio_payload["id"] = radio.get("id")
            radios_payload.append(radio_payload)

        parsed_params["radios"] = radios_payload
        self.log(f"Parsed Access Point Payload: {self.pprint(parsed_params)}", "DEBUG")
        return parsed_params

    def process_location_creation_updation_assign(self, function_name, floor_id, payloads, state):
        """
        Process the creation or updation of access point location based on the desired state.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            function_name (str): The name of the function to call for processing.
            floor_id (str): The ID of the floor where the access point is located.
            payloads (list): The list of payloads to process.
            state (str): The desired state of create/update/assign for the access point location.

        Returns:
            self - The current object with message and response information.
        """
        self.log(
            f"Processing access point location creation/updation for: {self.have.get('site_name')}",
            "INFO",
        )

        try:
            task_id = self.get_taskid_post_api_call(
                "site_design", function_name,
                {
                    "floor_id": floor_id, "payload": payloads
                }
            )
            if not task_id:
                msg = f"No response received from API for creating/updating/assigning Access Point Location: {self.have.get('site_name')}"
                self.log(msg, "WARNING")
                if state == "update":
                    self.location_not_updated.append(self.have.get("site_name"))
                elif state == "assign":
                    self.location_not_assigned.append(self.have.get("site_name"))
                else:
                    self.location_not_created.append(self.have.get("site_name"))

            self.log(f"{state} planned Access Point location API Response: {task_id}", "DEBUG")

            resync_retry_count = int(self.payload.get("dnac_api_task_timeout"))
            resync_retry_interval = int(self.payload.get("dnac_task_poll_interval"))
            while resync_retry_count > 0:
                task_details_response = self.get_tasks_by_id(task_id)

                if not task_details_response:  # Ensure the response is valid
                    self.log(f"Failed to retrieve task details for task ID: {task_id}", "ERROR")
                    return None

                task_status = task_details_response.get("status")
                self.log(f"Task ID: {task_id}, Status: {task_status}, Attempts remaining: {resync_retry_count}", "INFO")

                if task_details_response.get("endTime") is not None:
                    if task_status == "SUCCESS":
                        task_progress = self.get_task_details_by_id(task_id)
                        self.log(f"Task '{task_id}' completed successfully. {task_progress}", "INFO")
                        return task_status
                    elif task_status == "FAILURE":
                        task_progress = self.get_task_details_by_id(task_id)
                        self.log(f"Task '{task_id}' failed. {task_progress}", "ERROR")
                        return task_status

                self.log(f"Pauses execution for {resync_retry_interval} seconds.", "INFO")
                time.sleep(resync_retry_interval)
                resync_retry_count -= 1

            self.log(f"Task {task_id} did not complete within the timeout.", "ERROR")
            return None

        except Exception as e:
            self.msg = 'An error occurred during get task details. '
            self.log(self.msg + str(e), "ERROR")
            return None

    def accesspoint_location_creation_updation(self):
        """
        Create or update access point location in Cisco Catalyst Center based on the
        playbook details.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.

        Returns:
            self - The current object with message and response information.
        """
        self.log(
            f"Starting to create/update access point location for: {self.have.get('site_name')}",
            "INFO",
        )

        floor_id = self.have.get("site_id")
        create_payload, update_payload = [], []
        collect_ap_list = []

        if self.have.get("new_accesspoint"):
            for access_point in self.have.get("new_accesspoint"):
                self.log(f"Processing new access point: {self.pprint(access_point)}", "INFO")
                parsed_ap_details = self.parse_planned_accesspoint(access_point)

                create_payload.append(parsed_ap_details)
                self.log(f"Parsed Access Point Payload: {self.pprint(parsed_ap_details)}", "DEBUG")
                collect_ap_list.append(access_point.get("accesspoint_name"))

            self.log(
                f"Creating Access Point Location with payload: {self.pprint(create_payload)}",
                "DEBUG",
            )

            process_response = self.process_location_creation_updation_assign(
                "add_planned_access_points_positions", floor_id, create_payload, "create"
            )
            if process_response == "SUCCESS":
                self.msg = f"Access Point Location created successfully for: {self.have.get('site_name')}"
                self.log(self.msg , "INFO")
                self.location_created.append(collect_ap_list)
            elif process_response == "FAILURE":
                self.msg = f"Failed to create Access Point Location for: {self.have.get('site_name')}"
                self.log(self.msg, "ERROR")
                self.location_not_created.append(collect_ap_list)
            else:
                self.msg = f"Unable to process Access Point Location creation for: {self.have.get('site_name')}"
                self.log(self.msg, "ERROR")
                self.location_not_created.append(collect_ap_list)

        if self.have.get("update_accesspoint"):
            self.log(f"Updating Access Point Location with payload: {self.pprint(self.have.get('update_accesspoint'))}", "DEBUG")

            for access_point in self.have.get("update_accesspoint"):
                self.log(f"Processing update access point: {self.pprint(access_point)}", "INFO")
                parsed_ap_details = self.parse_planned_accesspoint(access_point)
                update_payload.append(parsed_ap_details)
                self.log(f"Parsed Access Point Payload: {self.pprint(parsed_ap_details)}", "DEBUG")
                collect_ap_list.append(access_point.get("accesspoint_name"))

            self.log(
                f"Updating Access Point Location with payload: {self.pprint(update_payload)}",
                "DEBUG",
            )

            process_response = self.process_location_creation_updation_assign(
                "edit_planned_access_points_positions", floor_id, update_payload, "update"
            )
            if process_response == "SUCCESS":
                self.msg = f"Access Point Location updated successfully for: {self.have.get('site_name')}"
                self.log(self.msg , "INFO")
                self.location_updated.append(collect_ap_list)

                self.log(".", "INFO")
            elif process_response == "FAILURE":
                self.msg = f"Failed to update Access Point Location for: {self.have.get('site_name')}"
                self.log(self.msg, "ERROR")
                self.location_not_updated.append(collect_ap_list)
            else:
                self.msg = f"Unable to process Access Point Location Updation for: {self.have.get('site_name')}"
                self.log(self.msg, "ERROR")
                self.location_not_updated.append(collect_ap_list)

        return self

    def assign_accesspoint_to_location(self):
        """
        Assign an access point to a specific planned location.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.

        Returns:
            self - The current object with message and response information.
        """
        self.log(f"Assigning access point to location for: {self.have.get('site_name')}", "INFO")

        if (self.have.get("new_accesspoint") or self.have.get("update_accesspoint")
           or self.have.get("existing_accesspoint")):
            access_point_devices = self.have.get("accesspoint_devices", [])
            assign_payload = []
            collect_ap_list = []
            for access_point in (self.have.get("new_accesspoint", []) +
                                 self.have.get("update_accesspoint", []) +
                                 self.have.get("existing_accesspoint", [])):
                if access_point.get("action") != "assign_planned":
                    continue

                self.log(f"Processing assign access point to planned location: {self.pprint(access_point)}",
                         "INFO")
                ap_device = self.find_dict_by_key_value(
                    access_point_devices, "hostname",
                    access_point.get("accesspoint_name", access_point.get("name"))
                )
                if not ap_device:
                    msg = f"No device details found for access point: {access_point.get('accesspoint_name')}"
                    self.log(msg, "WARNING")
                    self.fail_and_exit(msg)

                ap_details = self.get_planned_ap_position(
                    self.have["site_id"], self.have["site_name"], access_point
                )
                ap_payload = {
                    "accessPointId": ap_device.get("id"),
                    "plannedAccessPointId": ap_details[0].get("id")
                }
                assign_payload.append(ap_payload)
                collect_ap_list.append(access_point.get("accesspoint_name"))

            if not assign_payload:
                self.log("No valid access points found for assignment.", "DEBUG")
                return self

            self.log(f"Assign Access Point to Location Payload: {self.pprint(assign_payload)}", "DEBUG")

            floor_id = self.have.get("site_id")
            process_response = self.process_location_creation_updation_assign(
                "assign_planned_access_points_to_operations_ones", floor_id, assign_payload, "assign_planned"
            )
            self.log(f"Assign Access Point to Location process response: {self.pprint(process_response)}", "DEBUG")

            if process_response == "SUCCESS":
                self.msg = f"Access Point Location assigned successfully for: {self.have.get('site_name')}"
                self.log(self.msg , "INFO")
                self.location_assigned.append(collect_ap_list)

            elif process_response == "FAILURE":
                self.log(f"Failed to assign Access Point Location for: {self.have.get('site_name')}", "ERROR")

            if process_response == "SUCCESS":
                self.msg = f"Access Point Location assigned successfully for: {self.have.get('site_name')}"
                self.log(self.msg , "INFO")
                self.location_assigned.append(collect_ap_list)

            elif process_response == "FAILURE":
                self.msg = f"Failed to assign Access Point Location for: {self.have.get('site_name')}"
                self.log(self.msg, "ERROR")
                self.location_not_assigned.append(collect_ap_list)
            else:
                self.msg = f"Unable to process Access Point Location assignment for: {self.have.get('site_name')}"
                self.log(self.msg, "ERROR")
                self.location_not_assigned.append(collect_ap_list)

        return self

    def delete_planned_accesspoints_position(self):
        """
        Delete planned access point positions for a specific site.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.

        Returns:
            self - The current object with message and response information.
        """
        self.log(f"Deleting planned access point positions for: {self.have.get('site_name')}", "INFO")

        for access_point in self.have.get("delete_accesspoint", []):
            self.log(f"Processing delete access point: {self.pprint(access_point)}", "INFO")

            delete_payload = {}
            family_name = "site_design"
            function_name = "delete_planned_access_points_position"

            if access_point.get("action") == "delete_position":
                delete_payload["deviceIds"] = [access_point.get("id")]
                function_name = "unassign_network_devices_from_sites"
            else:
                delete_payload["floor_id"] = self.have.get("site_id")
                delete_payload["id"] = access_point.get("id")

            self.log(f"Deleting planned access point position Payload: {self.pprint(delete_payload)}",
                     "DEBUG")

            try:
                task_id = self.get_taskid_post_api_call(
                    family_name, function_name, delete_payload
                )
                if not task_id:
                    msg = f"No response received from API for deleting Access Point Planned Location: {self.have.get('site_name')}"
                    self.log(msg, "WARNING")
                    self.location_not_deleted.append(access_point.get("name"))
                    continue

                self.log(
                    f"Delete planned Access Point delete location API Response: {task_id}",
                    "DEBUG",
                )

                self.get_task_status_from_task_by_id(task_id)
                resync_retry_count = int(self.payload.get("dnac_api_task_timeout"))
                resync_retry_interval = int(self.payload.get("dnac_task_poll_interval"))
                while resync_retry_count > 0:
                    task_details_response = self.get_tasks_by_id(task_id)

                    if not task_details_response:  # Ensure the response is valid
                        self.log(f"Failed to retrieve task details for task ID: {task_id}", "ERROR")
                        self.location_not_deleted.append(access_point.get("name"))
                        break

                    task_status = task_details_response.get("status")
                    self.log(f"Task ID: {task_id}, Status: {task_status}, Attempts remaining: {resync_retry_count}",
                             "INFO")

                    if task_details_response.get("endTime") is not None:
                        if task_status == "SUCCESS":
                            task_progress = self.get_task_details_by_id(task_id)
                            self.log(f"Task '{task_id}' completed successfully. {task_progress}", "INFO")
                            self.location_deleted.append(access_point.get("name"))
                            break
                        elif task_status == "FAILURE":
                            task_progress = self.get_task_details_by_id(task_id)
                            self.log(f"Task '{task_id}' failed. {task_progress}", "ERROR")
                            self.location_not_deleted.append(access_point.get("name"))
                            break

                    self.log(f"Pauses execution for {resync_retry_interval} seconds.", "INFO")
                    time.sleep(resync_retry_interval)
                    resync_retry_count = resync_retry_count - 1

                continue

            except Exception as e:
                self.msg = 'An error occurred during get task details. '
                self.log(self.msg + str(e), "ERROR")
                self.location_not_deleted.append(access_point.get("name"))
                continue

        return self

    def get_diff_merged(self, config):
        """
        Create/Update access points planned location and assign access points to the planned location

        Parameters:
            config (list of dict) - Playbook details containing access point location information.

        Returns:
            self - The current object with message and created/updated/assigned response information.
        """
        self.log(
            f"Starting to create/update access point location for: {config}", "INFO"
        )

        self.changed = False
        self.status = "failed"

        if self.have.get("existing_accesspoint"):
            for access_point in self.have.get("existing_accesspoint", []):
                self.location_exist.append(access_point.get("name"))
            self.msg = "No Changes required, Access Point Location(s) already exist."
            self.changed = False
            self.status = "success"

        if self.have.get("already_assigned_accesspoint"):
            for access_point in self.have.get("already_assigned_accesspoint", []):
                self.location_exist.append(access_point.get("name"))
            self.msg = "No Changes required, Access Point Location(s) already assigned."
            self.changed = False
            self.status = "success"

        if self.have.get("new_accesspoint") or self.have.get("update_accesspoint"):
            responses = self.accesspoint_location_creation_updation()

            if not responses:
                self.msg = "No response received from Access Point Location creation/updation."
                self.log(self.msg, "ERROR")
                self.fail_and_exit(self.msg)

        if self.location_created or self.location_updated or self.location_exist:
            assign_response = self.assign_accesspoint_to_location()
            all_status_msg = str(self.location_created + self.location_updated + self.location_exist)
            self.msg = f"Access Point Location assigned successfully for '{all_status_msg}'."
            self.log(self.msg, "INFO")
            self.changed = True
            self.status = "success"

        if self.location_not_created:
            self.msg += f" Unable to process the following Access Point Location(s):" +\
            f"'{', '.join(map(str, self.location_not_created))}'. They may not have been created or already exist."
            self.log(self.msg, "DEBUG")
            self.changed = False
            self.status = "failed"

        locations = str(self.location_created + self.location_updated)
        self.log(self.msg, "INFO")
        self.set_operation_result(
            self.status, self.changed, self.msg, "INFO", locations
        ).check_return_status()

        return self

    def verify_diff_merged(self, config):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is merged (Create/Update).

        Parameters:
            config (dict) - Playbook details containing access point planned location
                            related information.

        Returns:
            self - The current object with message and response information.
        """
        self.log(
            f"Starting to verify created/updated Access Point Location(s) for: {config}",
            "INFO",
        )

        self.changed = False
        if (self.location_created
           and len(self.location_created) == len(config.get("access_points", []))):
            self.msg = f"Access Point Location created successfully for '{config.get('floor_site_hierarchy')}'."
            self.log(self.msg, "INFO")
            self.changed = True
            self.status = "success"

        if (self.location_exist and not self.location_created and not self.location_updated
           and len(self.location_exist) == len(config.get("access_points", []))):
            self.msg = "No Changes required, Access Point Location(s) already exist."
            self.changed = False
            self.status = "success"

        if (self.location_updated
           and len(self.location_updated) == len(config.get("access_points", []))):
            self.msg = f"Access Point Location updated successfully for '{config.get('floor_site_hierarchy')}'."
            self.log(self.msg, "INFO")
            self.changed = True
            self.status = "success"

        if (self.location_created and self.location_updated
           and len(self.location_created) + len(self.location_updated) == len(config.get("access_points", []))):
            self.msg = f"Access Point Location created/updated successfully for '{str(self.location_created + self.location_updated)}'."
            self.log(self.msg, "INFO")
            self.changed = True
            self.status = "success"

        if self.location_assigned:
            status_msg = ", ".join(map(str, self.location_assigned))
            self.msg += f" Following Access Point(s) assigned to planned location(s): '{status_msg}'."
            self.changed = True
            self.log(self.msg, "DEBUG")

        if self.location_not_assigned:
            status_msg = ", ".join(map(str, self.location_not_assigned))
            self.msg += f" Following Access Point(s) not assigned to planned location(s): '{status_msg}'."
            self.log(self.msg, "DEBUG")

        if self.location_not_updated:
            status_msg = ", ".join(map(str, self.location_not_updated))
            self.msg += f" Unable to update the following Access Point Location(s): '{status_msg}'."
            self.status = "failed"

        if self.location_not_created:
            status_msg = ", ".join(map(str, self.location_not_created))
            self.msg += f" Unable to create the following Access Point Location(s): '{status_msg}'."
            self.status = "failed"

        self.log(self.msg, "INFO")
        unique_list = [list(t) for t in set(map(
            tuple, self.location_created + self.location_updated + self.location_assigned))]
        self.set_operation_result(
            self.status, self.changed, self.msg, "INFO", unique_list
        ).check_return_status()
        return self

    def get_diff_deleted(self, config):
        """
        Delete Access Point planned Location(s) from the Cisco Catalyst Center
        based on playbook details.

        Parameters:
            config (list of dict) - Playbook configuration details

        Returns:
            self - The current object with access point location deletion message and response information.
        """
        self.log(f"Starting to delete Access Point Planned Location(s) for: {config}", "INFO")

        if self.have.get("new_accesspoint") and not self.have.get("delete_accesspoint"):
            for access_point in self.have.get("new_accesspoint", []):
                self.location_already_deleted.append(access_point.get("accesspoint_name"))
            self.msg = "No Changes required, Access Point Planned Location(s) do not exist to delete."
            self.changed = False
            self.status = "success"
            self.log(self.msg, "INFO")

        if self.have.get("delete_accesspoint"):
            responses = self.delete_planned_accesspoints_position()
            self.changed = False
            self.status = "failed"
            if not responses:
                self.msg = "No response received from Access Point Location deletion."
                self.log(self.msg, "ERROR")
                self.fail_and_exit(self.msg)

            if self.location_deleted:
                self.msg = f"Access Point Location deleted successfully for '{self.location_deleted}'."
                self.log(self.msg, "INFO")
                self.changed = True
                self.status = "success"

            if self.location_not_deleted:
                self.msg += f" Unable to delete the following Access Point Location(s): '{self.location_not_deleted}'." 
                self.log(self.msg, "DEBUG")
                self.changed = False
                self.status = "failed"

            if self.location_already_deleted:
                self.msg += f" Access Point Location(s) already deleted for '{self.location_already_deleted}'." 
                self.changed = False
                self.status = "success"

        self.set_operation_result(self.status, self.changed, self.msg, "INFO").check_return_status()
        return self

    def verify_diff_deleted(self, config):
        """
        Validates that the Access Point Location(s) in Cisco Catalyst Center have been deleted
        based on the playbook details.

        Parameters:
            config (dict) - Playbook details containing Network profile switch information.

        Returns:
            self - The current object with message and response.
        """
        self.log(
            f"Starting to verify the deleted Access Point Location(s) for: {config}",
            "INFO",
        )

        if len(self.location_not_deleted) > 0:
            self.msg += f" Unable to delete below Access Point Location(s) '{self.location_not_deleted}'."
            self.changed = False
            self.status = "failed"

        if len(self.location_already_deleted) == len(config.get("access_points", [])):
            self.msg = f"No Changes required, Access Point Location(s) already deleted " +\
                f"and verified successfully for '{self.location_already_deleted}'."
            self.changed = False
            self.status = "success"

        if len(self.location_deleted) == len(config.get("access_points", [])):
            self.msg = f"Access Point planned/assigned Location(s) deleted " +\
                f"and verified successfully for '{self.location_deleted}'."
            self.changed = True
            self.status = "success"

        self.log(self.msg, "INFO")
        self.set_operation_result(
            self.status, self.changed, self.msg, "INFO", self.location_deleted
        ).check_return_status()
        return self


def main():
    """main entry point for module execution"""

    # Define the specification for module arguments
    element_spec = {
        "dnac_host": {"type": "str", "required": True},
        "dnac_port": {"type": "str", "default": "443"},
        "dnac_username": {"type": "str", "default": "admin", "aliases": ["user"]},
        "dnac_password": {"type": "str", "no_log": True},
        "dnac_verify": {"type": "bool", "default": True},
        "dnac_version": {"type": "str", "default": "2.2.3.3"},
        "dnac_debug": {"type": "bool", "default": False},
        "dnac_log": {"type": "bool", "default": False},
        "dnac_log_level": {"type": "str", "default": "WARNING"},
        "dnac_log_file_path": {"type": "str", "default": "dnac.log"},
        "dnac_log_append": {"type": "bool", "default": True},
        "config_verify": {"type": "bool", "default": False},
        "dnac_api_task_timeout": {"type": "int", "default": 1200},
        "dnac_task_poll_interval": {"type": "int", "default": 2},
        "config": {"type": "list", "required": True, "elements": "dict"},
        "state": {"default": "merged", "choices": ["merged", "deleted"]},
        "validate_response_schema": {"type": "bool", "default": True},
    }

    # Create an AnsibleModule object with argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=False)
    ccc_ap_location = AccessPointLocation(module)
    state = ccc_ap_location.params.get("state")

    if (
        ccc_ap_location.compare_dnac_versions(
            ccc_ap_location.get_ccc_version(), "3.1.3.0"
        )
        < 0
    ):
        ccc_ap_location.status = "failed"
        ccc_ap_location.msg = (
            f"The specified version '{ccc_ap_location.get_ccc_version()}' does not support the network profile workflow feature."
            f"Supported version(s) start from '3.1.3.0' onwards."
        )
        ccc_ap_location.log(ccc_ap_location.msg, "ERROR")
        ccc_ap_location.check_return_status()

    if state not in ccc_ap_location.supported_states:
        ccc_ap_location.status = "invalid"
        ccc_ap_location.msg = f"State {state} is invalid"
        ccc_ap_location.check_return_status()

    ccc_ap_location.validate_input().check_return_status()
    config_verify = ccc_ap_location.params.get("config_verify")

    for config in ccc_ap_location.validated_config:
        ccc_ap_location.reset_values()
        ccc_ap_location.get_want(config).check_return_status()
        ccc_ap_location.get_have(config).check_return_status()
        ccc_ap_location.get_diff_state_apply[state](config).check_return_status()
        if config_verify:
            ccc_ap_location.verify_diff_state_apply[state](
                config
            ).check_return_status()

    module.exit_json(**ccc_ap_location.result)


if __name__ == "__main__":
    main()
