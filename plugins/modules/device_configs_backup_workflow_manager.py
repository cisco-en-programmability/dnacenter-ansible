#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("Abinash Mishra, Rugvedi Kapse, Madhan Sankaranarayanan, Sonali Deepthi Kesali")

DOCUMENTATION = r"""
---
module: device_configs_backup_workflow_manager
short_description: Device Configs Backup module for taking configuration backups of reachable devices in the Cisco Catalyst Center.
description:
  - Manage operation related to taking the backup of running config, static config and vlan.dat.bat
version_added: "6.14.0"
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author: Abinash Mishra (@abimishr)
        Rugvedi Kapse (@rukapse)
        Madhan Sankaranarayanan (@madhansansel)
        Sonali Deepthi Kesali (@skesali)
options:
  config_verify:
    description: Set to True to verify the Cisco Catalyst Center config after applying the playbook config.
    type: bool
    default: false
  state:
    description: The state of Cisco Catalyst Center after module completion.
    type: str
    choices: [ merged ]
    default: merged
  config:
    description:
      - List of details of the devices for which configuration backups need to be taken.
      - At least one parameter from the suboptions must be provided in the config.
      - When providing multiple parameters at once (excluding "site_list"), all the filters will be applied together in an AND operation.
        This means that only the devices matching all the specified criteria will be included in the configuration backup operation.
        For example, if both `hostname` and `device_type` are provided, only devices matching both the specified hostname and device
        type will be selected.
      - Note - Once all devices matching the parameters are retrieved, any device that is not reachable or is an Access Point (AP) will be skipped.
    type: list
    elements: dict
    required: true
    suboptions:
      hostname_list:
        description:
          - List of hostnames of the devices for which a configuration backup is to be taken.
          - The hostnames must be identical to those displayed under the inventory section in the Cisco Catalyst Center GUI.
          - For example - ["DC-T-9300.cisco.local", "NY-BN-9300.cisco.local"]
        type: str
      ip_address_list:
        description:
          - List of IP addresses of the devices for which configuration backups need to be taken.
          - The IP addresses should match those displayed in the inventory GUI of the Cisco Catalyst Center,
            specifically the management IP addresses of the devices.
          - For example - ["204.1.2.2", "204.1.2.5", "204.1.2.4"]
        type: str
      site_list:
        description:
          - Specifies a list of sites. The module takes a configuration backup of all devices located within the specified site(s).
          - Each site should be represented as a string value that indicates the complete hierarchical path of the site.
          - For example - ["Global/USA/San Francisco/Building_2/floor_1", "Global/USA/New York/Building_3/floor_2"]
          - Note -  When additional parameters are provided along with `site_list`, the operation will include all devices in the specified site(s)
                    and any devices matching the additional criteria (excluding `site_list`).
                    In other words, the operation will be performed on devices within the site(s) and those that meet the additional criteria.

        type: str
      mac_address_list:
        description:
          - Specifies list of MAC addresses of the devices for which configuration backups are to be taken.
        type: str
      serial_number_list:
        description:
          - Specifies the list of serial numbers of the devices for which configuration backups need to be taken.
          - For example - ["FCW2225C020", "FJB2334D06N", "FJC2327U0S2", "FJC2721271T"]
        type: str
      family:
        description:
          - Specifies list of families for which device configuration backups need to be taken.
          - For example - ["Switches and Hubs", "Routers"]
        type: str
      type:
        description:
          - Specifies the list of types of device(s) from a specific device family for which configuration backups need to be taken.
          - For example - ["Cisco Catalyst 9300 Switch", "Cisco Catalyst 9500 Switch"]
        type: str
      series:
        description:
          - Specifies the list of series of the device(s) for a specific device type for which configuration backups need to be taken.
          - For example - ["Cisco Catalyst 9300 Series Switches"]
        type: str
      collection_status:
        description:
          - Specifies the list of collection status of the device(s) as displayed in the inventory GUI of the Cisco Catalyst Center.
          - For example - ["Managed"]
        type: str
      file_path:
        description:
          - The location or directory where the configuration backups need to be exported on the local system.
          - If the "file_path" is not provided, the backup file(s) will be stored in a directory named
            "tmp" in the same directory as the playbook.
        type: str
        default: tmp
      file_password:
        description:
          - Optional file password for zipping and unzipping the config file.
          - Password must meet the following criteria -
            - Minimum password length is 8
            - It should contain atleast one lower case letter, one uppercase letter,
            - one digit
            - one special characters from -=\\\\\\\\;,./~!@$%^&*()_+{}[]|:?"
        type: str
      unzip_backup:
        description:
          - Determines whether the downloaded backup file should be unzipped after download.
          - If set to True, the backup file will be extracted to the specified directory.
          - If set to False, the file will remain in its zipped state.
        type: bool
        default: true

requirements:
  - dnacentersdk == 2.9.2
  - python >= 3.5

notes:
  - SDK Methods used are
    sites.Sites.get_site
    Site_design.Site_design.get_sites
    sites.Sites.get_membership
    site_design.Site_design.get_site_assigned_network_devices
    devices.Devices.get_device_list
    devices.Devices.get_device_by_id
    configuration_archive.ConfigurationsArchive.export_device_configurations
    file.Files.download_a_file_by_fileid

  - Paths used are
    get /dna/intent/api/v1/site
    get /dna/intent/api/v1/membership/${siteId}
    get /dna/intent/api/v1/network-device
    post /dna/intent/api/v1/network-device-archive/cleartext
    get /dna/intent/api/v1/file/${fileId}
    get /dna/intent/api/v1/networkDevices/assignedToSite
    get /dna/intent/api/v1/sites
    get /dna/intent/api/v1/network-device/${id}
"""

EXAMPLES = r"""
- name: Take backup of all devices in the Cisco Catalyst Center
  cisco.dnac.device_configs_backup_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config:
        - file_password: qsaA12!asdasd

- name: Take backup of device(s) using hostname(s)
  cisco.dnac.device_configs_backup_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config:
        - hostname_list: ["DC-T-9300.cisco.local", "NY-BN-9300.cisco.local"]
          file_path: backup
          unzip_backup: false

- name: Take backup of device(s) using hostname(s) and provide file password
  cisco.dnac.device_configs_backup_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config:
        - hostname_list: ["DC-T-9300.cisco.local"]
          file_path: backup
          file_password: qsaA12!asdasd
          unzip_backup: true

- name: Take backup of all devices in a site(s)
  cisco.dnac.device_configs_backup_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config:
        - site_list: ["Global/USA/RTP/BLD10", "Global/USA/New York/BLDNYC/FLOOR1"]
          file_path: backup

- name: Take backup of device(s) using IP Address List
  cisco.dnac.device_configs_backup_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config:
        - ip_address_list: ["204.1.2.5", "204.1.2.4", "204.1.2.2"]
          file_path: backup

- name: Take backup of device(s) using MAC Address List
  cisco.dnac.device_configs_backup_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config:
        - mac_address_list: ["d4:ad:bd:c1:67:00", " 00:b6:70:32:b8:00", "0c:75:bd:42:c3:80", "90:88:55:07:59:00"]
          file_path: backup
          unzip_backup: false

- name: Take backup of device(s) using Serial Number List
  cisco.dnac.device_configs_backup_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config:
        - serial_number_list: ["FCW2225C020", "FJB2334D06N", "FJC2327U0S2", "FJC2721271T"]
          file_path: backup

- name: Take backup of device(s) using Family List
  cisco.dnac.device_configs_backup_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config:
        - family_list: ["Switches and Hubs", "Routers"]
          file_path: backup
          unzip_backup: true

- name: Take backup of device(s) using Device Family Type List
  cisco.dnac.device_configs_backup_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config:
        - type_list: ["Cisco Catalyst 9300 Switch"]
          file_path: backup
          unzip_backup: false

- name: Take backup of device(s) using Device Series
  cisco.dnac.device_configs_backup_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config:
        - series_list: ["Cisco Catalyst 9300 Series Switches"]
          file_path: backup

- name: Take backup of devices with certain Collection Status
  cisco.dnac.device_configs_backup_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config:
        - collection_status_list: ["Managed"]
          file_path: backup

- name: Take backup of device(s) in a site and also that meet other parameters
  cisco.dnac.device_configs_backup_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config:
        - site_list: ["Global"]
          family_list: ["Switches and Hubs"]
          series_list: ["Cisco Catalyst 9300 Series Switches"]
          ip_address_list: ["204.1.2.5"]
          file_path: backup
          unzip_backup: false
"""

RETURN = r"""
# Case_1: Successful creation and exportation of device configs
response_1:
  description: A dictionary with  with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response":
        {
          "response": String,
          "version": String
        },
      "msg": String
    }

# Case_2: Error while taking a device_configs_backup
response_2:
  description: A string with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: list
  sample: >
    {
      "response": [],
      "msg": String
    }
"""
# common approach when a module relies on optional dependencies that are not available during the validation process.
try:
    import pyzipper
    HAS_PYZIPPER = True
except ImportError:
    HAS_PYZIPPER = False
    pyzipper = None

try:
    import pathlib
    HAS_PATHLIB = True
except ImportError:
    HAS_PATHLIB = False
    pathlib = None

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts
)
from io import BytesIO
import random
import string
import re
import time
import datetime


class DeviceConfigsBackup(DnacBase):

    """
    Class containing member attributes for device_configs_backup workflow_manager module
    """
    def __init__(self, module):
        super().__init__(module)
        self.skipped_devices_list = []

    def validate_input(self):
        """
        Validate the fields provided in the playbook.  Checks the
        configuration provided in the playbook against a predefined
        specification to ensure it adheres to the expected structure
        and data types.
        Parameters:
          - self: The instance of the class containing the "config" attribute
                  to be validated.
        Returns:
          The method returns an instance of the class with updated attributes:
          - self.msg: A message describing the validation result.
          - self.status: The status of the validation (either "success" or "failed").
          - self.validated_config: If successful, a validated version of the
                                   "config" parameter.
        """
        # Check if Pyzipper is installed
        if HAS_PYZIPPER is False:
            msg = "Pyzipper is not installed. Please install it using 'pip install pyzipper' command"
            self.log(msg, "CRITICAL")
            self.module.fail_json(msg=msg)

        # Check if Pathlib is installed
        if HAS_PATHLIB is False:
            msg = "Pathlib is not installed. Please install it using 'pip install pathlib' command"
            self.log(msg, "CRITICAL")
            self.module.fail_json(msg=msg)

        # Check if the config is provided in the playbook
        if not self.config:
            self.msg = "config not available in playbook for validattion"
            self.status = "success"
            return self

        # Define the specification for device configuration backup parameters
        device_configs_backup_spec = {
            "hostname_list": {"type": "list", "elements": "str", "required": False},
            "site_list": {"type": "list", "elements": "str", "required": False},
            "ip_address_list": {"type": "list", "elements": "str", "required": False},
            "mac_address_list": {"type": "list", "elements": "str", "required": False},
            "serial_number_list": {"type": "list", "elements": "str", "required": False},
            "family_list": {"type": "list", "elements": "str", "required": False},
            "type_list": {"type": "list", "elements": "str", "required": False},
            "series_list": {"type": "list", "elements": "str", "required": False},
            "collection_status_list": {"type": "list", "elements": "str", "required": False},
            "file_path": {"type": "str", "required": False, "default": "tmp"},
            "file_password": {"type": "str", "required": False},
            "unzip_backup": {"type": "bool", "required": False, "default": True}
        }

        # Validate device_configs_backup params
        valid_device_configs_backup, invalid_params = validate_list_of_dicts(
            self.config, device_configs_backup_spec
        )

        # Check if there are any invalid parameters
        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(
                "\n".join(invalid_params))
            self.log(str(self.msg), "ERROR")
            self.status = "failed"
            return self

        # If validation is successful, update the result
        self.validated_config = valid_device_configs_backup
        self.msg = "Successfully validated playbook configuration parameters using 'validate_input': {0}".format(str(valid_device_configs_backup))
        self.status = "success"
        return self

    def get_device_list_params(self, config):
        """
        Generates a dictionary of device parameters for querying Cisco Catalyst Center.
        Parameters:
            config (dict): A dictionary containing device filter criteria.
        Returns:
            dict: A dictionary mapping internal parameter names to their corresponding values from the config.
        Description:
            This method takes a configuration dictionary containing various device filter criteria and maps them to the internal parameter
            names required by Cisco Catalyst Center.
            It returns a dictionary of these mapped parameters which can be used to query devices based on the provided filters.
        """
        # Initialize an empty dictionary to store the mapped parameters
        get_device_list_params = {}

        # Mapping from input parameters names to API Specific parameter names
        parameters_list = {
            "hostname_list": "hostname",
            "ip_address_list": "management_ip_address",
            "mac_address_list": "mac_address",
            "serial_number_list": "serial_number",
            "family_list": "family",
            "type_list": "type",
            "series_list": "series",
            "collection_status_list": "collection_status"
        }

        # Iterate over the parameters and add them to the result dictionary if present in the config
        for parameter, parameter_name in parameters_list.items():
            if config.get(parameter):
                get_device_list_params[parameter_name] = config.get(parameter)
        self.log("get_device_list_params: {0}".format(get_device_list_params), "DEBUG")
        return get_device_list_params

    def get_device_ids_by_params(self, get_device_list_params):
        """Retrieves device IDs based on specified parameters from Cisco Catalyst Center.
        Parameters:
            get_device_list_params (dict): A dictionary of parameters to filter devices.
        Returns:
            dict: A dictionary mapping management IP addresses to instance IDs of reachable devices that are not Unified APs.
        Description:
            This method queries Cisco Catalyst Center to retrieve device information based on the provided filter parameters.
            It paginates through the results, filters out unreachable devices and Unified APs, and returns a dictionary of management IP addresses
            mapped to their instance IDs.
            Logs detailed information about the number of devices processed, skipped, and the final list of devices available for configuration backup.
        """
        mgmt_ip_to_instance_id_map = {}
        processed_device_count = 0
        skipped_device_count = 0

        try:
            offset = 1
            limit = 500
            while True:
                # Update params with current offset and limit
                get_device_list_params.update({
                    "offset": offset,
                    "limit": limit
                })

                # Query Cisco Catalyst Center for device information using the parameters
                response = self.dnac._exec(
                    family="devices",
                    function="get_device_list",
                    op_modifies=True,
                    params=get_device_list_params
                )
                self.log("Response received post 'get_device_list' API call with offset {0}: {1}".format(offset, str(response)), "DEBUG")

                # Check if a valid response is received
                if not response.get("response"):
                    self.log("Exiting the loop because no devices were returned after increasing the offset. Current offset: {0}".format(offset))
                    break  # Exit loop if no devices are returned

                # Iterate over the devices in the response
                for device_info in response.get("response", []):
                    processed_device_count += 1
                    device_ip = device_info.get("managementIpAddress", "Unknown IP")

                    # Check if the device is reachable and managed
                    if device_info.get("reachabilityStatus") == "Reachable" and device_info.get("collectionStatus") == "Managed":
                        # Skip Unified AP devices
                        if device_info.get("family") != "Unified AP" :
                            device_id = device_info["id"]
                            mgmt_ip_to_instance_id_map[device_ip] = device_id
                        else:
                            skipped_device_count += 1
                            self.skipped_devices_list.append(device_ip)
                            msg = (
                                "Skipping device {0} as its family is: {1}.".format(
                                    device_ip, device_info.get("family")
                                )
                            )
                            self.log(msg, "INFO")

                    else:
                        skipped_device_count += 1
                        self.skipped_devices_list.append(device_ip)
                        msg = (
                            "Skipping device {0} as its status is {1} or its collectionStatus is {2}.".format(
                                device_ip, device_info.get("reachabilityStatus"), device_info.get("collectionStatus")
                            )
                        )
                        self.log(msg, "INFO")

                # Increment offset for next batch
                offset += limit

            # Log the total number of devices processed and skipped
            self.log("Total number of devices received: {0}".format(processed_device_count), "INFO")
            self.log("Number of devices that will be skipped: {0}".format(skipped_device_count), "INFO")
            self.log("Config Backup Operation can be performed on the following filtered devices: {0}".format(len(mgmt_ip_to_instance_id_map)), "INFO")

        except Exception as e:
            # Log an error message if any exception occurs during the process
            self.log("Error fetching device IDs from Cisco Catalyst Center. Error details: {0}".format(str(e)), "ERROR")

        # Log an error if no reachable devices are found
        if not mgmt_ip_to_instance_id_map:
            self.log("No reachable devices found among the provided parameters: {0}".format(mgmt_ip_to_instance_id_map), "ERROR")

        return mgmt_ip_to_instance_id_map

    def get_device_id_list(self, config):
        """
        Retrieves device IDs based on site list or specified parameters from Cisco Catalyst Center.
        Parameters:
            config (dict): A dictionary containing device filter criteria, optionally including a list of sites.
        Returns:
            dict: A dictionary mapping management IP addresses to instance IDs of devices that match the provided criteria.
        Description:
            This method queries Cisco Catalyst Center to retrieve device information based on the provided filter criteria.
            If a list of sites is provided, it retrieves device IDs for those sites. Additionally, it can use other parameters to filter devices.
            Logs detailed information about the processing steps and the final list of device IDs retrieved.
        """
        # Initialize the mapping dictionary
        mgmt_ip_to_instance_id_map = {}

        # Check if site_list is provided in the config
        site_list = config.get("site_list")
        if site_list:
            self.log("List of site(s) provided in the input: {0}".format(site_list))

            # Use a set to ensure unique sites
            unique_sites = set(site_list)
            self.log("Attempting to get Device Id(s) of all device(s) from the provided for site(s): {0}".format(unique_sites), "DEBUG")

            # Retrieve device IDs for each site in the unique_sites set
            for site_name in unique_sites:
                site_mgmt_ip_to_instance_id_map, skipped_devices_list = self.get_reachable_devices_from_site(site_name)
                self.skipped_devices_list.extend(skipped_devices_list)
                self.log("Retrieved following Device Id(s) of device(s): {0} from the provided site: {1}".format(
                    site_mgmt_ip_to_instance_id_map, site_name), "DEBUG")
                mgmt_ip_to_instance_id_map.update(site_mgmt_ip_to_instance_id_map)
                self.log("Devices from site: '{0}' that will be skipped: {1}".format(site_name, skipped_devices_list), "DEBUG")

            # Get additional device list parameters excluding site_list
            get_device_list_params = self.get_device_list_params(config)
            if get_device_list_params:
                self.log("Attempting to get Device Id(s) of all device(s) using parameters(excluding site_list): {0}".format(
                    get_device_list_params), "DEBUG")
                params_mgmt_ip_to_instance_id_map = self.get_device_ids_by_params(get_device_list_params)
                mgmt_ip_to_instance_id_map.update(params_mgmt_ip_to_instance_id_map)
                self.log("Retrieved following Device Id(s) of device(s): {0} from the provided parameters(excluding site_list).".format(
                    mgmt_ip_to_instance_id_map), "DEBUG")

        # If no site_list is provided, use other parameters to get device IDs
        else:
            get_device_list_params = self.get_device_list_params(config)
            self.log("Attempting to get Device Id(s) of all device(s) using parameters(excluding site_list): {0}".format(
                get_device_list_params), "DEBUG")
            params_mgmt_ip_to_instance_id_map = self.get_device_ids_by_params(get_device_list_params)
            mgmt_ip_to_instance_id_map.update(params_mgmt_ip_to_instance_id_map)
            self.log("Retrieved following Device Id(s) of device(s): {0} from the provided parameters(excluding site_list).".format(
                mgmt_ip_to_instance_id_map), "DEBUG")

        return mgmt_ip_to_instance_id_map

    def validate_ip4_address_list(self, ip_address_list):
        """
        Validates the list of IPv4 addresses provided in the playbook.
        Parameters:
            ip_address_list (list): A list of IPv4 addresses to be validated.
        Description:
            This method iterates through each IP address in the list and checks if it is a valid IPv4 address.
            If any address is found to be invalid, it logs an error message and fails the module.
            After validating all IP addresses, it logs a success message.
        """
        # Iterate through each IP address in the list to validate
        for ip in ip_address_list:
            # Check if the IP address is a valid IPv4 address
            if not self.is_valid_ipv4(ip):
                self.msg = "IP address: {0} is not valid".format(ip)
                self.log(self.msg, "ERROR")
                self.module.fail_json(self.msg)

        # Log a success message indicating all IP addresses are valid
        ip_address_list_str = ", ".join(ip_address_list)
        self.log("Successfully validated the IP address(es): {0}".format(ip_address_list_str), "DEBUG")

    def validate_file_password(self, file_password):
        """
        Validates the provided file password against specified criteria.
        Parameters:
            file_password (str): The password to be validated.
        Description:
            This method checks if the provided password meets the criteria of having at least 8 characters,
            including at least one lowercase letter, one uppercase letter, one digit, and one special character.
            If the password does not meet these criteria, it logs a critical error message and fails the module.
        """
        # Define the regex pattern for a valid password
        password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[-=\\;,./~!@#$%^&*()_+{}[\]|:?\"]).{8,}$"

        # Log the user-defined password for debugging purposes
        self.log("User defined password is {0}".format(file_password), "DEBUG")

        # Check if the password matches the defined pattern
        if not re.match(password_pattern, file_password):
            msg = (
                "Invalid password input. The password must be at least 8 characters long and include "
                "at least one lowercase letter, one uppercase letter, one digit, and one special character "
                "from -=\\\\;,./~!@#$%^&*()_+{}[]|:?"
            )
            self.log(msg, "CRITICAL")
            self.module.fail_json(msg=msg)

    def password_generator(self):
        """
        Creates a password that matches Cisco Catalyst Center's requirements.
        Description:
            This method generates a password that meets the following criteria:
            - Minimum length of 8 characters.
            - Contains at least one lowercase letter.
            - Contains at least one uppercase letter.
            - Contains at least one digit.
            - Contains at least one special character from -=\\\\;,./~!@#$%^&*()_+{}[]|:?
            The generated password is shuffled to ensure randomness.
        """
        # Define the set of punctuation characters allowed in the password
        allowed_special_chars = "-=;,.~!@#$%^&*()_+{}[]|:?"

        # Combine allowed characters: punctuation, letters, and digits
        allowed_chars = allowed_special_chars + string.ascii_letters + string.digits

        # Create a list ensuring the password meets the criteria
        password_list = [
            random.choice(allowed_special_chars),
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice(allowed_chars),
            random.choice(allowed_chars),
            random.choice(allowed_chars),
            random.choice(allowed_chars),
        ]

        # Form the password
        password = []
        random.shuffle(password_list)
        password = "".join(password_list)

        # Log the password generation event
        self.log("File password is generated using the password generator API", "INFO")

        return password

    def export_device_configurations_params(self, file_password, mgmt_ip_to_instance_id_map):
        """
        Creates parameters for exporting device configurations from Cisco Catalyst Center.
        Parameters:
            file_password (str): The password to secure the exported device configurations.
            mgmt_ip_to_instance_id_map (dict): A dictionary mapping management IP addresses
            to instance IDs of devices.
        Returns:
            dict: A dictionary containing the device IDs and the file password for exporting device configurations.
        Description:
            This method constructs a dictionary of parameters required to export device configurations
            from Cisco Catalyst Center.
            The parameters include a list of device IDs and a password to secure the exported configurations.
        """
        # Construct the parameters dictionary for exporting device configurations
        export_device_configurations_params = {
            "deviceId": list(mgmt_ip_to_instance_id_map.values()),
            "password": file_password
        }

        return export_device_configurations_params

    def export_device_configurations(self, export_device_configurations_params):
        """
        Exports device configurations from Cisco Catalyst Center using the provided parameters.
        Parameters:
            export_device_configurations_params (dict): A dictionary containing parameters for the export operation,
            including device IDs and a file password.
        Returns:
            str or None: The task ID of the export operation if successful, or None if the operation failed
            or no response was received.
        Description:
            This method initiates the export of device configurations from Cisco Catalyst Center using the provided parameters.
            It logs detailed information about the process, including the response from the API call and the
            task ID of the export operation.
            If an error occurs, it logs an error message, updates the result, and checks the return status.
        """
        task_id = self.get_taskid_post_api_call("configuration_archive", "export_device_configurations", export_device_configurations_params)
        try:
            # Make an API call to export device configurations
            response = self.dnac._exec(
                family="configuration_archive",
                function="export_device_configurations",
                op_modifies=True,
                params=export_device_configurations_params,
            )
            self.log("Response received post 'export_device_configurations' API call: {0}".format(str(response)), "DEBUG")

            # Process the response if available
            if response["response"]:
                self.result.update(dict(response=response["response"]))
                task_id = response["response"].get("taskId")
                self.log("Task Id for the 'export_device_configurations' task is {0}".format(task_id), "INFO")
                # Return the task ID
                return task_id
            else:
                self.log("No response received from the 'export_device_configurations' API call.", "WARNING")
                return None

        except Exception as e:
            # Log an error message and fail if an exception occurs
            self.msg = (
                "An error occurred while Exporting Device Configurations from the Cisco Catalyst Center. "
                "export_device_configurations_params: {0}  Error: {1}".format(export_device_configurations_params, str(e))
            )
            self.set_operation_result("failed", False, self.msg, "ERROR")
            self.check_return_status()

    def download_file(self, additional_status_url=None):
        """
        Downloads a file from Cisco Catalyst Center and stores it locally.
        Parameters:
            additionalStatusURL (str): The URL containing the file ID to be downloaded.
        Returns:
            tuple or None: A tuple containing the file ID and the file data if successful, or None if the download failed.
        Description:
            This method downloads a file from Cisco Catalyst Center using the provided URL, which contains the file ID.
            It logs the download process and checks the response from the API call. If successful, it returns the file
            ID and file data.
            If an error occurs, it logs an error message, updates the result, and checks the return status.
        """
        # Log the download URL for debugging purposes
        self.log("Initiating download from URL: {0}".format(additional_status_url), "INFO")
        file_id = additional_status_url.split("/")[-1]
        try:
            response = self.dnac._exec(
                family="file",
                function="download_a_file_by_fileid",
                op_modifies=True,
                params={"file_id": file_id},
            )
            self.log("Response received post 'download_a_file_by_fileid' API Call : {0}".format(str(response)), "DEBUG")

            # Check if response returned
            if response and response.data:
                return (file_id, response.data)

            self.msg = "No response received post the 'download_a_file_by_fileid' API call."
            return None
        except Exception as e:
            self.msg = "The Backup Config file with File ID: {0} could not be downloaded due to the following error: {1}".format(file_id, e)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            self.check_return_status()

    def unzip_data(self, file_id, file_data):
        """
        Unzips the downloaded file data and stores it in the specified directory.
        Parameters:
            file_id (str): The ID of the file to be unzipped.
            file_data (bytes): The binary data of the downloaded file.
        Returns:
            bool: True if the file is successfully unzipped, otherwise it logs an error and fails the module.
        Description:
            This method takes the binary data of a downloaded file, unzips it using the provided file password, and stores the
            contents in the specified directory.
            It logs the unzipping process and handles any exceptions that may occur during the extraction.
        """
        # Create the directory path if it does not exist
        file_path = self.want.get("file_path")
        self.log("Creating directory path: {0}".format(file_path), "DEBUG")
        pathlib.Path(file_path).mkdir(parents=True, exist_ok=True)

        if not self.want.get("unzip_backup"):
            # Generate a timestamp and set the zipped file path
            timestamp = datetime.datetime.now().strftime("%d_%b_%Y_%H_%M_%S_%f")[:-3]
            zipped_file_path = "{0}/{1}_{2}.zip".format(file_path, timestamp, file_id)

            try:
                with open(zipped_file_path, "wb") as file:
                    file.write(file_data)

                self.log("Downloaded the zipped backup to {0} without unzipping.".format(zipped_file_path), "INFO")
                return True
            except OSError as e:
                self.log("Failed to write zipped backup to {0}. Error: {1}".format(zipped_file_path, str(e)), "ERROR")
                return False

        try:
            # Convert the binary file data to a BytesIO object for processing
            zip_data = BytesIO(file_data)
            self.log("Collected ZIP Data for file with ID: {0}".format(file_id), "INFO")

            # Unzip the file using the provided file password
            self.log("Unzipping Backup Config file with file ID: {0} after completion of download.".format(file_id), "INFO")
            file_password = self.want.get("file_password")
            with pyzipper.AESZipFile(zip_data, "r") as f:
                f.pwd = bytes(file_password, encoding="utf-8")
                f.extractall(path=str(file_path))
            return True
        except Exception as e:
            self.msg = "Error in unzipping Backup Config file with file ID: {0}. Error: {1}".format(file_id, e)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            self.check_return_status()

    def get_export_device_config_task_status(self, task_id):
        """
        Checks the status of a device configuration export task in Cisco Catalyst Center.
        Parameters:
            task_id (str): The ID of the task to check the status for.
        Returns:
            self: The instance of the class, potentially updated with task results.
        Description:
            This method repeatedly checks the status of a device configuration export task using the provided task ID.
            It logs progress, handles errors, and performs additional tasks such as downloading and unzipping the
            file if the task completes successfully.
        """
        task_name = "Backup Device Configuration"
        success_msg = "{0} Task with task ID {1} completed successfully. Exiting the loop.".format(task_name, task_id)
        if self.dnac_version <= self.version_2_3_5_3:
            progress_validation = "Device configuration Successfully exported as password protected ZIP"
            failure_msg = (
                "An error occurred while performing {0} task with task ID {1} for export_device_configurations_params: {2}"
                .format(task_name, task_id, self.want.get("export_device_configurations_params"))
            )
            self.get_task_status_from_task_by_id(task_id, task_name, failure_msg, success_msg, progress_validation=progress_validation)
        else:
            self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg)

        if self.status == "success":
            self.log("Task '{0}' completed successfully for task ID {1}.".format(task_name, task_id), "INFO")
            if self.dnac_version <= self.version_2_3_5_3:
                response = self.get_task_details(task_id)
                additional_status_url = response.get("additionalStatusURL")
            else:
                response = self.get_tasks_by_id(task_id)
                additional_status_url = response.get("resultLocation")

            if not additional_status_url:
                self.msg = "Error retrieving the Device Config Backup file ID for task ID {0}".format(task_id)
                self.fail_and_exit(self.msg)
            self.log("Additional status URL retrieved: {0}".format(additional_status_url), "DEBUG")

            # Perform additional tasks after breaking the loop
            mgmt_ip_to_instance_id_map = self.want.get("mgmt_ip_to_instance_id_map")

            # Download the file using the additional status URL
            self.log("Downloading the Device Config Backup file from {0}.".format(additional_status_url), "DEBUG")
            file_id, downloaded_file = self.download_file(additional_status_url=additional_status_url)
            self.log("Retrived file data for file ID: {0}.".format(file_id), "DEBUG")
            if not downloaded_file:
                self.msg = "Error downloading Device Config Backup file(s) with file ID: {0}. ".format(file_id)
                self.fail_and_exit(self.msg)

            # Unzip the downloaded file
            self.log("Unzipping the downloaded Device Config Backup file(s) for file ID: {0}.".format(file_id), "DEBUG")
            download_status = self.unzip_data(file_id, downloaded_file)
            if download_status:
                self.log("{0} task has been successfully performed on {1} device(s): {2}.".format(
                    task_name, len(mgmt_ip_to_instance_id_map), list(mgmt_ip_to_instance_id_map.keys())), "INFO")
                self.log("{0} task has been skipped for {1} device(s): {2}".format(
                    task_name, len(self.skipped_devices_list), self.skipped_devices_list), "INFO")
                self.msg = (
                    "{0} task has been successfully performed on {1} device(s) and skipped on {2} device(s). "
                    "The backup configuration files can be found at: {3}.".format(
                        task_name,
                        len(mgmt_ip_to_instance_id_map),
                        len(self.skipped_devices_list),
                        pathlib.Path(self.want.get("file_path")).resolve()
                    )
                )

                # Append password information if unzipping is not required
                if not self.want.get("unzip_backup", False):
                    self.msg += " The password to unzip the files is: '{0}'.".format(self.want.get("file_password"))
                self.set_operation_result("success", True, self.msg, "INFO")
            else:
                self.msg = "Error unzipping Device Config Backup file(s) with file ID: {0}. ".format(file_id)
                self.fail_and_exit(self.msg)

        return self

    def get_want(self, config):
        """
        Prepares the desired state (want) based on the provided configuration.
        Parameters:
            config (dict): A dictionary containing the configuration parameters.
        Returns:
            self: The instance of the class, potentially updated with the desired state.
        Description:
            This method processes the provided configuration to prepare the desired state (want).
            It validates the IP address list and file password, generates a new password if none is provided,
            retrieves device IDs, and updates the desired state with necessary parameters.
        """
        self.want = {}

        # Retrieve configuration parameters
        file_path = config.get("file_path")
        file_password = config.get("file_password")
        ip_address_list = config.get("ip_address_list")

        # Validate the IP address list if provided
        if ip_address_list:
            self.validate_ip4_address_list(ip_address_list)

        # Validate the file password or generate a new one if not provided
        if file_password:
            self.validate_file_password(file_password)
        else:
            file_password = self.password_generator()

        # Retrieve the device ID list based on the provided configuration
        mgmt_ip_to_instance_id_map = self.get_device_id_list(config)
        self.log("Retrived the Device ID list based on the provided parameters: {0}".format(mgmt_ip_to_instance_id_map), "DEBUG")
        if not mgmt_ip_to_instance_id_map:
            self.msg = "No reachable devices found among the provided parameters: {0}".format(config)
            self.set_operation_result("failed", False, self.msg, "WARNING")
            return self

        self.log("Based on provided parameters, retrieved Device Id(s) of {0} device(s): {1} ".format(
            len(mgmt_ip_to_instance_id_map), mgmt_ip_to_instance_id_map))

        # Prepare the desired state (want)
        self.want["export_device_configurations_params"] = self.export_device_configurations_params(file_password, mgmt_ip_to_instance_id_map)
        self.want["mgmt_ip_to_instance_id_map"] = mgmt_ip_to_instance_id_map
        self.want["file_password"] = file_password
        self.want["file_path"] = file_path
        self.want["unzip_backup"] = config.get("unzip_backup")
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

        return self

    def get_diff_merged(self):
        """
        This method is designed to Execute and Monitor Device Configuration Export Actions.
        Returns:
            self (object): An instance of the class used for continuing the chaining of method calls.
        Description:
            This method logs its execution, iterates through a predefined map of actions and their corresponding status-checking functions,
            executes the required actions based on provided parameters, and verifies the success of each action by checking its status.
        """
        self.log("Executing the get_diff_merged function", "DEBUG")

        # Define a map of action parameters to their corresponding action and status functions
        action_map = {
            "export_device_configurations_params": (self.export_device_configurations, self.get_export_device_config_task_status),
        }

        # Iterate over each action parameter and its associated functions
        for action_param, (action_func, status_func) in action_map.items():
            # Execute the action and check its status
            if self.want.get(action_param):
                result_task_id = action_func(self.want.get(action_param))
                status_func(result_task_id).check_return_status()

        return self

    def verify_diff_merged(self):
        """
        This method is designed to Verify the Success of Device Configuration Backup Operation.
        Returns:
            self (object): An instance of the class used for continuing the chaining of method calls.
        Description:
            This method validates the Cisco Catalyst Center configuration for a merged state by checking if any backup files were created
            within a specified time window. It logs the desired state, checks the modification time of files in the specified directory,
            and sets the operation status based on whether recent backup files are found.
        """

        file_path = self.want.get("file_path")
        self.log("File Path: {0}".format(file_path))
        if file_path:
            abs_file_path = pathlib.Path(file_path).resolve()
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

        # Define the time window in seconds to check for recently modified files
        window_seconds = 10
        current_time = time.time()
        window_start_time = current_time - window_seconds

        # List of files modified within the specified time window
        files_modified_within_window = []

        try:
            for f in abs_file_path.iterdir():
                if f.stat().st_mtime > window_start_time:
                    files_modified_within_window.append(f.name)
        except Exception as e:
            self.msg = (
                "An error occurred while verifying the success of the backup configuration operation. "
                "The Device Config Backup operation may not have been successful since the backup files "
                "were not found at the specified path. Error: {0}".format(str(e))
            )
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        # Check if there are any files modified within the window
        if len(files_modified_within_window) > 0:
            self.log("Verified the success of the Device Config Backup operation. Back up has been taken in the following files {0}".format(
                str(files_modified_within_window)), "INFO")
            self.status = "success"
        else:
            self.log("The Device Config Backup operation may not have been successful since back up files not found at path: {0}".format(
                abs_file_path), "WARNING")

        return self


def main():
    """
    main entry point for module execution
    """
    # Define the specification for the module"s arguments
    element_spec = {"dnac_host": {"required": True, "type": "str"},
                    "dnac_port": {"type": "str", "default": "443"},
                    "dnac_username": {"type": "str", "default": "admin", "aliases": ["user"]},
                    "dnac_password": {"type": "str", "no_log": True},
                    "dnac_verify": {"type": "bool", "default": "True"},
                    "dnac_version": {"type": "str", "default": "2.2.3.3"},
                    "dnac_debug": {"type": "bool", "default": False},
                    "dnac_log": {"type": "bool", "default": False},
                    "dnac_log_level": {"type": "str", "default": "WARNING"},
                    "dnac_log_file_path": {"type": "str", "default": "dnac.log"},
                    "dnac_log_append": {"type": "bool", "default": True},
                    "config_verify": {"type": "bool", "default": False},
                    "dnac_api_task_timeout": {"type": "int", "default": 1200},
                    "dnac_task_poll_interval": {"type": "int", "default": 2},
                    "validate_response_schema": {"type": "bool", "default": True},
                    "config": {"required": True, "type": "list", "elements": "dict"},
                    "state": {"default": "merged", "choices": ["merged"]}
                    }

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)

    # Initialize the NetworkCompliance object with the module
    ccc_device_configs_backup = DeviceConfigsBackup(module)

    # Get the state parameter from the provided parameters
    state = ccc_device_configs_backup.params.get("state")

    # Check if the state is valid
    if state not in ccc_device_configs_backup.supported_states:
        ccc_device_configs_backup.status = "invalid"
        ccc_device_configs_backup.msg = "State {0} is invalid".format(state)
        ccc_device_configs_backup.check_return_status()

    # Get the config_verify parameter from the provided parameters
    config_verify = ccc_device_configs_backup.params.get("config_verify")

    # Validate the input parameters and check the return status
    ccc_device_configs_backup.validate_input().check_return_status()

    # Iterate over the validated configuration parameters
    for config in ccc_device_configs_backup.validated_config:
        ccc_device_configs_backup.reset_values()
        ccc_device_configs_backup.get_want(config).check_return_status()
        ccc_device_configs_backup.get_diff_state_apply[state]().check_return_status()
        if config_verify:
            ccc_device_configs_backup.verify_diff_state_apply[state]().check_return_status()

    # Exit with the result obtained from the NetworkCompliance object
    module.exit_json(**ccc_device_configs_backup.result)


if __name__ == "__main__":
    main()
