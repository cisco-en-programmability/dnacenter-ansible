# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type
__author__ = ("Ajith Andrew J, Syed khadeer Ahmed")

DOCUMENTATION = r"""
---
module: user_role_workflow_manager
short_description: Resource module for managing users and roles in Cisco Catalyst Center
description:
  - Manages operations to create, update, and delete users and roles in Cisco Catalyst Center
  - Provides APIs to create, update, and delete users and roles
version_added: "6.17.0"
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - Ajith Andrew J (@ajithandrewj)
  - Syed Khadeer Ahmed (@syed-khadeerahmed)
  - Rangaprabhu Deenadayalu (@rangaprabha-d)
options:
  config_verify:
    description: Set to True to verify the Cisco Catalyst Center after applying the playbook config
    type: bool
    default: False
  state:
    description: The state of Cisco Catalyst Center after module completion
    type: str
    choices: ["merged", "deleted"]
    default: merged
  config:
    description: Dict of user or role details being managed
    type: dict
    required: true
    suboptions:
      user_details:
        description: Manages the user details
        type: list
        elements: dict
        suboptions:
          username:
            description: The username for the user's account
            type: str
          first_name:
            description: The first name of the user
            type: str
          last_name:
            description: The last name of the user
            type: str
          email:
            description:
              - The email address of the user (e.g., syedkhadeerahmed@example.com)
              - Used to fetch user data if the username is forgotten
              - Required for user deletion if the username is forgotten
            type: str
          password:
            description:
              - The password for the user's account. Must contain at least one special character,
                one capital letter, one lowercase letter, and a minimum length of 15 characters
              - Required for user creation
            type: str
          role_list:
            description:
              - Default Role "Observer-role"
              - A role name assigned to the user. It must match exactly with the role in Cisco Catalyst Center
              - Required for user creation and updates
            type: list
            elements: str
      role_details:
        description: Manages the role details
        type: list
        elements: dict
        suboptions:
          role_name:
            description: Name of the role
            type: str
          description:
            description: Description for the role
            type: str
          assurance:
            description: Assure consistent service levels with complete visibility across all aspects of your network
            choices: ["deny", "read", "write"]
            default: "read"
            suboptions:
              overall:
                description: Provides the same choice for all sub-parameters
                choices: ["deny", "read", "write"]
                default: "read"
              monitoring_and_troubleshooting:
                description:
                  - Monitor and manage the health of your network with issue troubleshooting
                    and remediation, proactive network monitoring, and insights driven by AI Network Analytics
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              monitoring_settings:
                description:
                  - Configure and manage issues. Update network, client, and application health thresholds
                  - You must have at least Read permission on Monitoring and Troubleshooting
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              troubleshooting_tools:
                description:
                  - Create and manage sensor tests. Schedule on-demand forensic packet captures (Intelligent Capture) for troubleshooting clients
                  - You must have at least Read permission on Monitoring and Troubleshooting
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
          network_analytics:
            description: Manage network analytics-related components
            suboptions:
              overall:
                description: Provides the same choice for all sub-parameters
                choices: ["deny", "read", "write"]
                default: "read"
              data_access:
                description:
                  - Enable access to query engine APIs. Control functions such as global search, rogue management, and aWIPS
                  - Setting the permission to Deny affects Search and Assurance functionality
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
          network_design:
            description: Set up the network hierarchy, update your software image repository,
                         and configure network profiles and settings for managing your sites and network devices
            suboptions:
              overall:
                description: Provides the same choice for all sub-parameters
                choices: ["deny", "read", "write"]
                default: "read"
              advanced_network_settings:
                description:
                  - Update network settings, such as global device credentials, authentication and policy servers,
                    certificates, trustpool, cloud access keys, Stealthwatch, Umbrella, and data anonymization
                  - Export the device inventory and its credentials
                  - To complete this task, you must have Read permission on Network Settings
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              image_repository:
                description: Manage software images and facilitate upgrades and updates on physical and virtual network entities
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              network_hierarchy:
                description: Define and create a network hierarchy of sites, buildings, floors, and areas based on geographic location.
              network_profiles:
                description:
                  - Create network profiles for routing, switching, and wireless. Assign profiles to sites.
                    This role includes Template Editor, Tagging, Model Config Editor, and Authentication Template.
                  - To create SSIDs, you must have Write permission on Network Settings.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              network_settings:
                description:
                  - Common site-wide network settings such as AAA, NTP, DHCP, DNS, Syslog, SNMP, and Telemetry.
                  - Users with this role can add an SFTP server and modify the Network Resync Interval in System > Settings.
                  - To create wireless profiles, you must have Write permission on Network Profiles.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              virtual_network:
                description: Manage virtual networks (VNs). Segment physical networks into multiple logical networks
                             for traffic isolation and controlled inter-VN communication.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
          network_provision:
            description: Configure, upgrade, provision, and manage your network devices.
            suboptions:
              overall:
                description: It gives the same choice for all sub-parameters.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              compliance:
                description: Manage compliance provisioning.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              exo:
                description: Scan the network for details on publicly announced information pertaining to the End of Life, End of Sales,
                             or End of Support of the hardware and software in your network.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              image_update:
                description: Upgrade software images on devices that don't match the Golden Image settings after a complete upgrade lifecycle
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              inventory_management:
                description:
                  - Discover, add, replace, or delete devices on your network while managing device attributes and configuration properties.
                  - To replace a device, you must have Write permission.
                  - Network Provision > PnP.
                type: list
                elements: dict
                suboptions:
                  overall:
                    description: It gives the same choice for all sub-parameters.
                    choices: ["deny", "read", "write"]
                    default: "read"
                    type: str
                  device_configuration:
                    description: Display the running configuration of a device.
                    choices: ["deny", "read", "write"]
                    default: "read"
                    type: str
                  discovery:
                    description: Display the running configuration of a device.
                    choices: ["deny", "read", "write"]
                    default: "read"
                    type: str
                  network_device:
                    description: Add devices from Inventory, view device details, and perform device-level actions.
                    choices: ["deny", "read", "write"]
                    default: "read"
                    type: str
                  port_management:
                    description: Allow port actions on a device.
                    choices: ["deny", "read", "write"]
                    default: "read"
                    type: str
                  topology:
                    description:
                      - Display network device and link connectivity. Manage device roles, tag devices, customize the display, and save custom topology layouts.
                      - To view the SD-Access Fabric window, you must have at least Read permission on Network Provision > Inventory Management > Topology.
                    choices: ["deny", "read", "write"]
                    default: "read"
                    type: str
              license:
                description:
                 - Unified view of your software and network assets relative to license usage and compliance.
                 - The role also controls permissions for cisco.com and Smart accounts.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              network_telemetry:
                description:
                  - Enable or disable the collection of application telemetry from devices.
                  - Configure the telemetry settings associated with the assigned site.
                  - Configure other settings like wireless service assurance and controller certificates.
                  - To enable or disable network telemetry, you must have Write permission on Provision.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              pnp:
                description: Automatically onboard new devices, assign them to sites, and configure them with site-specific contextual settings.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              provision:
                description:
                  - Provision devices with the site-specific settings and policies that are configured for the network.
                  - This role includes Fabric, Application Policy, Application Visibility, Cloud, Site-to-Site VPN, Network/Application Telemetry,
                    Stealthwatch, Sync Start vs Run Configuration, and Umbrella provisioning.
                  - On the main dashboards for rogue and aWIPS, you can enable or disable certain actions, including rogue containment.
                  - To provision devices, you must have Write permission on Network Design and Network Provision.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
          network_services:
            description: Configure additional capabilities on the network beyond basic network connectivity and access.
            default: "read"
            suboptions:
              overall:
                description: It gives the same choice for all sub-parameters.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              app_hosting:
                description: Deploy, manage, and monitor virtualized and container-based applications running on network devices.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              bonjour:
                description: Enable the Wide Area Bonjour service across your network to enable policy-based service discovery.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              stealthwatch:
                description:
                  - Configure network elements to send data to Cisco Stealthwatch to detect and mitigate threats, even in encrypted traffic.
                  - To provision Stealthwatch, you must have Write permission on the following components.
                  - Network Design > Network Settings
                  - Network Provision > Provision
                  - Network Services > Stealthwatch
                  - Network Design > Advanced Settings
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              umbrella:
                description:
                  - Configure network elements to use Cisco Umbrella as the first line of defense against cybersecurity threats.
                  - To provision Umbrella, you must have Write permission on the following components
                    - Network Design > Network Settings
                    - Network Provision > Provision
                    - Network Provision > Scheduler
                    - Network Services > Umbrella
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
          platform:
            description: Open platform for accessible, intent-based workflows, data exchange, notifications, and third-party app integrations.
            default: "deny"
            suboptions:
              overall:
                description: It gives the same choice for all sub-parameters.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              apis:
                description: Drive value by accessing Cisco Catalyst Center through REST APIs.
                choices: ["deny", "read", "write"]
                default: "deny"
                type: str
              bundles:
                description: Enhance productivity by configuring and activating preconfigured bundles for ITSM integration.
                choices: ["deny", "read", "write"]
                default: "deny"
                type: str
              events:
                description:
                  - Subscribe to get notified in near real time about network and system events of interest and initiate corrective actions.
                  - You can configure email and syslog logs in System > Settings > Destinations.
                choices: ["deny", "read", "write"]
                default: "deny"
                type: str
              reports:
                description:
                  - Generate reports using predefined reporting templates for all aspects of your network.
                  - Generate reports for rogue devices and for aWIPS.
                  - You can configure webhooks in System > Settings > Destinations.
                choices: ["deny", "read", "write"]
                default: "deny"
                type: str
          security:
            description: Manage and control secure access to the network.
            default: "read"
            suboptions:
              overall:
                description: It gives the same choice for all sub-parameters.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              group_based_policy:
                description:
                  - Manage group-based policies for networks that enforce segmentation and access control based on Cisco security group tags.
                  - This role includes Endpoint Analytics.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              ip_based_access_control:
                description: Manage IP-based access control lists that enforce network segmentation based on IP addresses.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              security_advisories:
                description: Scan the network for security advisories. Review and understand the impact of published
                             Cisco security advisories that may affect your network.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
          system:
            description: Centralized administration of Cisco Catalyst Center, which includes configuration management,
                         network connectivity, software upgrades, and more.
            default: "read"
            suboptions:
              overall:
                description: It gives the same choice for all sub-parameters.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              machine_reasoning:
                description: Configure automatic updates to the machine reasoning knowledge base to rapidly identify
                             security vulnerabilities and improve automated issue analysis.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              system_management:
                description:
                  - Manage core system functionality and connectivity settings. Manage user roles and configure external authentication.
                  - This role includes Cisco Credentials, Integrity Verification, Device EULA, HA, Integration Settings, Disaster Recovery,
                    Debugging Logs, Telemetry Collection, System EULA, IPAM, vManage Servers, Cisco AI Analytics, Backup & Restore, and Data Platform.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
          utilities:
            description: One-stop-shop productivity resource for the most commonly used troubleshooting tools and services.
            suboptions:
              overall:
                description: It gives the same choice for all sub-parameters.
                choices: ["deny", "read", "write"]
                type: str
              audit_log:
                description: Detailed log of changes made via UI or API interface to network devices or Cisco Catalyst Center.
                choices: ["deny", "read", "write"]
                default: "deny"
                type: str
              event_viewer:
                description: View network device and client events for troubleshooting.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              network_reasoner:
                description:
                  - Allow the Cisco support team to remotely troubleshoot the network devices managed by Cisco Catalyst Center.
                  - With this role enabled, an engineer from the Cisco Technical Assistance Center TAC can connect remotely to a
                    customer's Cisco Catalyst Center setup for troubleshooting purposes.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              remote_device_support:
                description: Allow Cisco support team to remotely troubleshoot any network devices managed by Cisco DNA Center.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              scheduler:
                description: Integrated with other back-end services, scheduler lets you run, schedule, and monitor network tasks and
                             activities such as deploy policies, provision, or upgrade the network.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
              search:
                description: Search for various objects in Cisco Catalyst Center, such as sites, network devices, clients, applications,
                             policies, settings, tags, menu items, and more.
                choices: ["deny", "read", "write"]
                default: "read"
                type: str
requirements:
  - dnacentersdk >= 2.7.1
  - python >= 3.10
notes:
  - SDK Methods used
    - user_and_roles.UserandRoles.get_user_ap_i
    - user_and_roles.UserandRoles.add_user_ap_i
    - user_and_roles.UserandRoles.update_user_ap_i
    - user_and_roles.UserandRoles.delete_user_ap_i
  - Paths used
    - get /dna/system/api/v1/user
    - post /dna/system/api/v1/user
    - put /dna/system/api/v1/user
    - delete /dna/system/api/v1/user/{userId}
"""

EXAMPLES = r"""
---
- name: Create a user
  cisco.dnac.user_role_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    dnac_log_level: DEBUG
    config_verify: True
    dnac_api_task_timeout: 1000
    dnac_task_poll_interval: 1
    state: merged
    config:
      - user_details:
          - username: "ajithandrewj"
            first_name: "ajith"
            last_name: "andrew"
            email: "ajith.andrew@example.com"
            password: "Ajith@123"
            role_list: ["SUPER-ADMIN-ROLE"]

- name: Update a user for first name, last name, email, and role list
  cisco.dnac.user_role_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    dnac_log_level: DEBUG
    config_verify: True
    dnac_api_task_timeout: 1000
    dnac_task_poll_interval: 1
    state: merged
    config:
      - user_details:
          - username: "ajithandrewj"
            first_name: "ajith"
            last_name: "andrew"
            email: "ajith.andrew@example.com"
            role_list: ["SUPER-ADMIN-ROLE"]

- name: Update a user for role list
  cisco.dnac.user_role_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    dnac_log_level: DEBUG
    config_verify: True
    dnac_api_task_timeout: 1000
    dnac_task_poll_interval: 1
    state: merged
    config:
      - user_details:
          - username: "ajithandrewj"
            role_list: ["NETWORK-ADMIN-ROLE"]

- name: Delete a user
  cisco.dnac.user_role_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    dnac_log_level: DEBUG
    config_verify: True
    dnac_api_task_timeout: 1000
    dnac_task_poll_interval: 1
    state: merged
    config:
      - user_details:
          username: "ajithandrewj"
          email: "ajith.andrew@example.com"

- name: Create a role with all params
  cisco.dnac.user_role_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    dnac_log_level: DEBUG
    config_verify: True
    role_based_access_control:
      - role_name: "role_name"
        description: "role_description"
        assurance:
          - monitoring_and_troubleshooting: "write"
            monitoring_settings: "read"
            troubleshooting_tools: "deny"
        network_analytics:
          data_access: "write"
        network_design:
          - advanced_network_settings: "deny"
            image_repository: "deny"
            network_hierarchy: "deny"
            network_profiles: "write"
            network_settings: "write"
            virtual_network: "read"
        network_provision:
          - compliance: "deny"
            image_update: "write"
            inventory_management:
              - device_configuration: "write"
                discovery: "deny"
                network_device: "read"
                port_management: "write"
                topology: "write"
            license: "write"
            network_telemetry: "write"
            pnp: "deny"
            provision: "read"
        network_services:
          - app_hosting: "deny"
            bonjour: "write"
            stealthwatch: "read"
            umbrella: "deny"
        platform:
          - apis: "write"
            bundles: "write"
            events: "write"
            reports: "read"
        security:
          - group_based_policy: "read"
            ip_based_access_control: "write"
            security_advisories: "write"
        system:
          - machine_reasoning: "read"
            system_management: "write"
        utilities:
          - audit_log: "read"
            event_viewer: "deny"
            network_reasoner: "write"
            scheduler: "read"
            search: "write"

- name: Create a role for assurance
  cisco.dnac.user_role_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    dnac_log_level: DEBUG
    config_verify: True
    role_based_access_control:
      - role_name: "role_name"
        description: "role_description"
        assurance:
          - overall: "write"
            monitoring_and_troubleshooting: "read"

- name: Create a role for network provision
  cisco.dnac.user_role_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    dnac_log_level: DEBUG
    config_verify: True
    role_based_access_control:
      - role_name: "role_name"
        description: "role_description"
        network_provision:
          - compliance: "deny"
            image_update: "write"
            inventory_management:
              - overall: "read"
                device_configuration: "write"
            license: "write"
            network_telemetry: "write"
            pnp: "deny"
            provision: "read"

- name: Update a role for assurance and platform
  cisco.dnac.user_role_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    dnac_log_level: DEBUG
    config_verify: True
    config:
      role_details:
        - role_name: "role_name"
          assurance:
            - overall: "deny"
          platform:
            - apis: "write"
              bundles: "write"
              events: "write"
              reports: "read"

- name: Delete a role
  cisco.dnac.user_role_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    dnac_log_level: DEBUG
    config_verify: True
    dnac_api_task_timeout: 1000
    dnac_task_poll_interval: 1
    state: merged
    config:
      - role_details:
          rolename: "role_name"
"""

RETURN = r"""
# Case 1: Successful creation of user
response_1:
  description: A dictionary with details of the API execution from Cisco Catalyst Center.
  returned: always
  type: dict
  sample:
    {
        "response": {
            "message": "string",
            "userId": "string"
        }
    }

# Case 2: Successful updation of user
response_2:
  description: A dictionary with details of the API execution from Cisco Catalyst Center.
  returned: always
  type: dict
  sample:
    {
        "response": {
            "message": "string"
        }
    }

# Case 3: Successful deletion of user
response_3:
  description: A dictionary with details of the API execution from Cisco Catalyst Center.
  returned: always
  type: dict
  sample:
    {
        "response": {
            "message": "string"
        }
    }

# Case 4: User exists and no action needed (for update)
response_4:
  description: A dictionary with existing user details indicating no update needed.
  returned: always
  type: dict
  sample:
    {
        "response": {
            "user": {
                "email": "user@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "username": "johndoe",
                "role_list": ["NETWORK-ADMIN-ROLE"]
            },
            "userId": "string",  # User ID from Cisco Catalyst Center
            "type": "string"
        },
        "msg": "User already exists and no update needed."
    }

# Case 5: Error during user operation (create/update/delete)
response_5:
  description: A dictionary with details of the API execution and error information.
  returned: always
  type: dict
  sample:
    {
        "response": {
            "msg": "Error during creating, updating or deleting the user."
        }
    }

# Case 6: User not found (during delete operation)
response_6:
  description: A dictionary indicating user not found during delete operation.
  returned: always
  type: dict
  sample:
    {
        "response": {
            "msg": "User not found."
        }
    }

# Case 7: Successful creation of role
response_7:
  description: A dictionary with details of the API execution from Cisco Catalyst Center.
  returned: always
  type: dict
  sample:
    {
        "response": {
            "roleid": "string",
            "message": "string"
        }
    }

# Case 8: Successful updation of role
response_8:
  description: A dictionary with details of the API execution from Cisco Catalyst Center.
  returned: always
  type: dict
  sample:
    {
        "response": {
            "roleId": "string",
            "message": "string"
        }
    }

# Case 9: Successful deletion of role
response_9:
  description: A dictionary with details of the API execution from Cisco Catalyst Center.
  returned: always
  type: dict
  sample:
    {
        "response": {
            "message": "string"
        }
    }

# Case 10: Error during role operation (create/update/delete)
response_10:
  description: A dictionary with details of the API execution and error information.
  returned: always
  type: dict
  sample:
    {
        "response": {
            "msg": "Error during creating, updating or deleting the role."
        }
    }

# Case 11: Role not found (during delete operation)
response_11:
  description: A dictionary indicating role not found during delete operation.
  returned: always
  type: dict
  sample:
    {
        "response": {
            "msg": "Role not found."
        }
    }
"""

import re
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    validate_str,
    validate_list
)
from ansible.module_utils.basic import AnsibleModule


class UserandRole(DnacBase):
    """Class containing member attributes for user workflow_manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.result["response"] = []
        self.supported_states = ["merged", "deleted"]
        self.payload = module.params
        self.keymap = {}

    def validate_input_yml(self, user_role_details):
        """
        Validate the fields provided in the yml files.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types based on input.
        Parameters:
          - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Returns:
          The method returns an instance of the class with updated attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either "success" or "failed").
                - self.validated_config: If successful, a validated version of the "config" parameter.
        Description:
          - To use this method, create an instance of the class and call "validate_input_yml" on it.
          - If the validation succeeds, "self.status" will be "success" and "self.validated_config" will contain the validated
            configuration. If it fails, "self.status" will be "failed", and "self.msg" will describe the validation issues.
          - If the validation succeeds, this will allow to go next step, unless this will stop execution based on the fields.
        """

        self.log("Validating the Playbook Yaml File..", "INFO")
        self.log(user_role_details)

        if user_role_details is None or isinstance(user_role_details, dict):
            self.msg = "Configuration is not available in the playbook for validation or user/role details are not type list"
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self

        try:
            if "role_name" in user_role_details[0] and user_role_details[0].get("role_name") is not None:
                rolelist = user_role_details
                rolelist = self.camel_to_snake_case(rolelist)
                role_details = dict(role_name=dict(required=True, type="str"),
                                    description=dict(required=False, type="str"),
                                    assurance=dict(required=False, type="list", elements="dict"),
                                    network_analytics=dict(required=False, type="list", elements="dict"),
                                    network_design=dict(required=False, type="list", elements="dict"),
                                    network_provision=dict(required=False, type="list", elements="dict"),
                                    network_services=dict(required=False, type="list", elements="dict"),
                                    platform=dict(required=False, type="list", elements="dict"),
                                    security=dict(required=False, type="list", elements="dict"),
                                    system=dict(required=False, type="list", elements="dict"),
                                    utilities=dict(required=False, type="list", elements="dict")
                                    )
                valid_param, invalid_param = validate_list_of_dicts(rolelist, role_details)

                if invalid_param:
                    self.msg("Invalid param found in playbook: {0}".format(", ".join(invalid_param)))
                    self.log(self.msg, "ERROR")
                    self.status = "failed"
                    return self

                self.validated_config = valid_param
                self.msg = "Successfully validated playbook config params: {0}".format(str(valid_param[0]))
                self.log(self.msg, "INFO")
                self.status = "success"
                return self

            elif "username" in user_role_details[0] or "email" in user_role_details[0]:
                userlist = user_role_details
                userlist = self.camel_to_snake_case(userlist)
                user_details = dict(first_name=dict(required=False, type="str"),
                                    last_name=dict(required=False, type="str"),
                                    email=dict(required=False, type="str"),
                                    password=dict(required=False, type="str"),
                                    username=dict(required=False, type="str"),
                                    role_list=dict(required=False, type="list", elements="str"),
                                    )

                valid_param, invalid_param = validate_list_of_dicts(userlist, user_details)

                if invalid_param:
                    self.msg("Invalid param found in playbook: {0}".format(", ".join(invalid_param)))
                    self.log(self.msg, "ERROR")
                    self.status = "failed"
                    return self

                self.validated_config = valid_param
                self.msg = "Successfully validated playbook config params:{0}".format(str(valid_param[0]))
                self.log(self.msg, "INFO")
                self.status = "success"
                return self

            else:
                self.msg = "Configuration params like username or email or role_name is not available in the playbook"
                self.log(self.msg, "ERROR")
                self.status = "failed"
                return self

        except Exception:
            self.msg = "Any of the role parameters like assurance, network_analytics, network_design, etc.. are not type list"
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self

    def valid_role_config_parameters(self, role_config):
        """
        Addtional validation for the create role configuration payload.
        Parameters:
          - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
          - ap_config (dict): A dictionary containing the input configuration details.
        Returns:
          The method returns an instance of the class with updated attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either "success" or "failed").
        Description:
            - To use this method, create an instance of the class and call "valid_role_config_parameters" on it.
            - If the validation succeeds it return "success".
            - If it fails, "self.status" will be "failed", and "self.msg" will describe the validation issues.
            - To use this method, create an instance of the class and call "valid_role_config_parameters" on it.
            - If the validation succeeds, this will allow to go next step, unless this will stop execution based on the fields.
        """

        errormsg = []

        if role_config.get("role_name"):
            role_name_regex = re.compile(r"^[A-Za-z0-9_-]+$")
            if not role_name_regex.match(role_config["role_name"]):
                errormsg.append("""Role name: role_name must only contain letters, numbers, underscores,
                                and hyphens and should not contain spaces or other special characters""")

        if role_config.get("description"):
            param_spec = dict(type="str", length_max=255)
            validate_str(role_config["description"], param_spec, "description", errormsg)

        assurance_list = role_config.get("assurance", [])

        if assurance_list:
            for assurance_dict in assurance_list:
                if assurance_dict.get("overall"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(assurance_dict["overall"], param_spec, "overall", errormsg)

                if assurance_dict.get("monitoring_and_troubleshooting"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(assurance_dict["monitoring_and_troubleshooting"], param_spec, "monitoring_and_troubleshooting", errormsg)

                if assurance_dict.get("monitoring_settings"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(assurance_dict["monitoring_settings"], param_spec, "monitoring_settings", errormsg)

                if assurance_dict.get("troubleshooting_tools"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(assurance_dict["troubleshooting_tools"], param_spec, "troubleshooting_tools", errormsg)

        network_analytics_list = role_config.get("network_analytics", [])

        if network_analytics_list:
            for network_analytics_dect in network_analytics_list:
                if network_analytics_dect.get("overall"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(network_analytics_dect["overall"], param_spec, "overall", errormsg)

                if network_analytics_dect.get("data_access"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(network_analytics_dect["data_access"], param_spec, "data_access", errormsg)

        network_design_list = role_config.get("network_design", [])

        if network_design_list:
            for network_design_dict in network_design_list:
                if network_design_dict.get("overall"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(network_design_dict["overall"], param_spec, "overall", errormsg)

                if network_design_dict.get("advanced_network_settings"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(network_design_dict["advanced_network_settings"], param_spec, "advanced_network_settings", errormsg)

                if network_design_dict.get("image_repository"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(network_design_dict["image_repository"], param_spec, "image_repository", errormsg)

                if network_design_dict.get("network_hierarchy"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(network_design_dict["network_hierarchy"], param_spec, "network_hierarchy", errormsg)

                if network_design_dict.get("network_profiles"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(network_design_dict["network_profiles"], param_spec, "network_profiles", errormsg)

                if network_design_dict.get("network_settings"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(network_design_dict["network_settings"], param_spec, "network_settings", errormsg)

                if network_design_dict.get("virtual_network"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(network_design_dict["virtual_network"], param_spec, "virtual_network", errormsg)

        network_provision_list = role_config.get("network_provision", [])

        if network_provision_list:
            for network_provision_dict in network_provision_list:
                if network_provision_dict.get("overall"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(network_provision_dict["overall"], param_spec, "overall", errormsg)

                if network_provision_dict.get("compliance"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(network_provision_dict["compliance"], param_spec, "compliance", errormsg)

                if network_provision_dict.get("image_update"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(network_provision_dict["image_update"], param_spec, "image_update", errormsg)

                if network_provision_dict.get("inventory_management"):
                    inventory_management_list = network_provision_dict.get("inventory_management", [])

                    for inventory_management_dict in inventory_management_list:
                        if inventory_management_dict.get("overall"):
                            param_spec = dict(type="str", length_max=255)
                            validate_str(inventory_management_dict["overall"], param_spec, "overall", errormsg)

                        if inventory_management_dict.get("device_configuration"):
                            param_spec = dict(type="str", length_max=255)
                            validate_str(inventory_management_dict["device_configuration"], param_spec, "device_configuration", errormsg)

                        if inventory_management_dict.get("discovery"):
                            param_spec = dict(type="str", length_max=255)
                            validate_str(inventory_management_dict["discovery"], param_spec, "discovery", errormsg)

                        if inventory_management_dict.get("network_device"):
                            param_spec = dict(type="str", length_max=255)
                            validate_str(inventory_management_dict["network_device"], param_spec, "network_device", errormsg)

                        if inventory_management_dict.get("port_management"):
                            param_spec = dict(type="str", length_max=255)
                            validate_str(inventory_management_dict["port_management"], param_spec, "port_management", errormsg)

                        if inventory_management_dict.get("topology"):
                            param_spec = dict(type="str", length_max=255)
                            validate_str(inventory_management_dict["topology"], param_spec, "topology", errormsg)

                if network_provision_dict.get("license"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(network_provision_dict["license"], param_spec, "license", errormsg)

                if network_provision_dict.get("network_telemetry"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(network_provision_dict["network_telemetry"], param_spec, "network_telemetry", errormsg)

                if network_provision_dict.get("pnp"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(network_provision_dict["pnp"], param_spec, "pnp", errormsg)

                if network_provision_dict.get("provision"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(network_provision_dict["provision"], param_spec, "provision", errormsg)

        network_services_list = role_config.get("network_services", [])

        if network_services_list:
            for network_services_dict in network_services_list:
                if network_services_dict.get("overall"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(network_services_dict["overall"], param_spec, "overall", errormsg)

                if network_services_dict.get("app_hosting"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(network_services_dict["app_hosting"], param_spec, "app_hosting", errormsg)

                if network_services_dict.get("bonjour"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(network_services_dict["bonjour"], param_spec, "bonjour", errormsg)

                if network_services_dict.get("stealthwatch"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(network_services_dict["stealthwatch"], param_spec, "stealthwatch", errormsg)

                if network_services_dict.get("umbrella"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(network_services_dict["umbrella"], param_spec, "umbrella", errormsg)

        platform_list = role_config.get("platform", [])

        if platform_list:
            for platform_dict in platform_list:
                if platform_dict.get("overall"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(platform_dict["overall"], param_spec, "overall", errormsg)

                if platform_dict.get("apis"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(platform_dict["apis"], param_spec, "apis", errormsg)

                if platform_dict.get("bundles"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(platform_dict["bundles"], param_spec, "bundles", errormsg)

                if platform_dict.get("events"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(platform_dict["events"], param_spec, "events", errormsg)

                if platform_dict.get("reports"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(platform_dict["reports"], param_spec, "reports", errormsg)

        security_list = role_config.get("security", [])

        if security_list:
            for security_dict in security_list:
                if security_dict.get("overall"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(security_dict["overall"], param_spec, "overall", errormsg)

                if security_dict.get("group_based_policy"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(security_dict["group_based_policy"], param_spec, "group_based_policy", errormsg)

                if security_dict.get("ip_based_access_control"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(security_dict["ip_based_access_control"], param_spec, "ip_based_access_control", errormsg)

                if security_dict.get("security_advisories"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(security_dict["security_advisories"], param_spec, "security_advisories", errormsg)

        system_list = role_config.get("system", [])

        if system_list:
            for system_dict in system_list:
                if system_dict.get("overall"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(system_dict["overall"], param_spec, "overall", errormsg)

                if system_dict.get("machine_reasoning"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(system_dict["machine_reasoning"], param_spec, "machine_reasoning", errormsg)

                if system_dict.get("system_management"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(system_dict["system_management"], param_spec, "system_management", errormsg)

        utilities_list = role_config.get("utilities", [])

        if utilities_list:
            for utilities_dict in utilities_list:
                if utilities_dict.get("overall"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(utilities_dict["overall"], param_spec, "overall", errormsg)

                if utilities_dict.get("audit_log"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(utilities_dict["audit_log"], param_spec, "audit_log", errormsg)

                if utilities_dict.get("event_viewer"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(utilities_dict["event_viewer"], param_spec, "event_viewer", errormsg)

                if utilities_dict.get("network_reasoner"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(utilities_dict["network_reasoner"], param_spec, "network_reasoner", errormsg)

                if utilities_dict.get("scheduler"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(utilities_dict["scheduler"], param_spec, "scheduler", errormsg)

                if utilities_dict.get("search"):
                    param_spec = dict(type="str", length_max=255)
                    validate_str(utilities_dict["search"], param_spec, "search", errormsg)

        if len(errormsg) > 0:
            self.msg = "Invalid parameters in playbook config: {0}".format(str("\n".join(errormsg)))
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self

        self.msg = "Successfully validated config params:{0}".format(str(role_config))
        self.log(self.msg, "INFO")
        self.status = "success"
        return self

    def valid_user_config_parameters(self, user_config):
        """
        Addtional validation for the create user configuration payload.
        Parameters:
          - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
          - ap_config (dict): A dictionary containing the input configuration details.
        Returns:
          The method returns an instance of the class with updated attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either "success" or "failed").
        Description:
            - To use this method, create an instance of the class and call "valid_user_config_parameters" on it.
            - If the validation succeeds it return "success".
            - If it fails, "self.status" will be "failed", and "self.msg" will describe the validation issues.
            - To use this method, create an instance of the class and call "valid_user_config_parameters" on it.
            - If the validation succeeds, this will allow to go next step, unless this will stop execution based on the fields.
        """

        errormsg = []

        if user_config.get("first_name"):
            first_name_regex = re.compile(r"^[A-Za-z0-9_-]+$")
            if not first_name_regex.match(user_config["first_name"]):
                errormsg.append("""first_name: first_name must only contain letters, numbers, underscores, and hyphens and
                should not contain spaces or other special characters""")

        if user_config.get("last_name"):
            last_name_regex = re.compile(r"^[A-Za-z0-9_-]+$")
            if not last_name_regex.match(user_config["last_name"]):
                errormsg.append("""last_name: last_name must only contain letters, numbers, underscores, and hyphens and
                should not contain spaces or other special characters""")

        if user_config.get("email"):
            email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
            if not email_regex.match(user_config["email"]):
                errormsg.append("email: Invalid email format for email: {0}".format(user_config["email"]))

        if user_config.get("password"):
            password_regex = re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
            if not password_regex.match(user_config["password"]):
                errormsg.append("password: Password does not meet complexity requirements for password: {0}".format(user_config["password"]))

        if user_config.get("username"):
            username_regex = re.compile(r"^[A-Za-z0-9_-]+$")
            if not username_regex.match(user_config["username"]):
                errormsg.append("""username: Username must only contain letters, numbers, underscores, and hyphens and
                should not contain spaces or other special characters""")

        if user_config.get("role_list"):
            param_spec = dict(type="list", elements="str")
            validate_list(user_config["role_list"], param_spec, "role_list", errormsg)

        if len(errormsg) > 0:
            self.msg = "Invalid parameters in playbook config: {0}".format(str("\n".join(errormsg)))
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self

        self.msg = "Successfully validated config params:{0}".format(str(user_config))
        self.log(self.msg, "INFO")
        self.status = "success"
        return self

    def get_want(self, config):
        """
        Retrieve all user or role-related information from the playbook needed for creation/updation in Cisco Catalyst Center.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - config (dict): A dictionary containing user or role information.
        Returns:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            - Retrieves all user or role-related information from the playbook required for creating or updating in Cisco Catalyst Center.
            - Includes parameters such as "username", "email", "role_list" and "role_name" as applicable.
            - Stores the gathered information in the "want" attribute for later reference.
            - Logs the desired state configuration for debugging and informational purposes.
        """

        want = {}
        for key, value in config.items():
            want[key] = value

        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
        return self

    def get_have(self, input_config):
        """
        Retrieve and store current user or role details from Cisco Catalyst Center based on input configuration.
        Parameters:
            - self (object): An instance for interacting with Cisco Catalyst Center.
            - input_config (dict): Configuration details specifying user or role.
        Returns:
            - self (object): An instance for interacting with Cisco Catalyst Center.
        Description:
            - Queries Cisco Catalyst Center to check if specified user or role exists.
            - If the input specifies a role name, checks and retrieves current role configuration.
            - If the input specifies a username or email, checks and retrieves current user configuration.
            - Stores retrieved user or role details in the "have" attribute for later reference.
        """

        user_exists = False
        role_exists = False
        current_user_config = None
        current_role_config = None
        current_role_id_config = None
        have = {}

        if "role_name" in input_config and input_config["role_name"] is not None:
            (role_exists, current_role_config) = self.get_current_config(input_config)

            if not role_exists:
                self.log("The provided role {0} is not present in the Cisco Catalyst Center. Role_exists = \
                         {1}".format(str(input_config.get("role_name")), str(role_exists)), "INFO")

            self.log("Current role config details (have): {0}".format(str(current_role_config)), "DEBUG")

            if role_exists:
                have["role_name"] = current_role_config.get("name")
                have["role_exists"] = role_exists
                have["current_role_config"] = current_role_config
            else:
                have["role_exists"] = role_exists

        elif input_config["username"] is not None or input_config["email"] is not None:
            (user_exists, role_exists, current_user_config, current_role_id_config) = self.get_current_config(input_config)

            if not user_exists:
                self.log("The provided user {0} is not present in the Cisco Catalyst Center. User_exists = \
                         {1}".format(str(input_config.get("username")), str(user_exists)), "INFO")

            self.log("Current user config details (have): {0}".format(str(current_user_config)), "DEBUG")

            if user_exists:
                have["username"] = current_user_config.get("username")
                have["user_exists"] = user_exists
                have["current_user_config"] = current_user_config
                have["current_role_id_config"] = current_role_id_config
            else:
                have["user_exists"] = user_exists
                have["current_role_id_config"] = current_role_id_config

            if role_exists:
                have["current_role_id_config"] = current_role_id_config

        self.have = have
        self.log("Current State (have): {0}".format(str(self.have)), "INFO")
        return self

    def get_diff_merged(self, config):
        """
        Update or create users and roles in Cisco Catalyst Center based on playbook configurations.
        Parameters:
            - self (object): Instance for interacting with Cisco Catalyst Center.
            - config (dict): Configuration data for user or role updates.
        Returns:
            - self (object): Instance for interacting with Cisco Catalyst Center.
        Description:
            - Determines whether to update or create a user or role in Cisco Catalyst Center based on the provided configuration.
            - Determines update or creation needs based on "role_name", "username", or "email" in config.
            - Updates roles if "role_name" exists, creates if absent using "create_role" or "update_role".
            - Updates users if "username" or "email" exists, creates if absent using "create_user" or "update_user".
            - Returns the instance of the class used for interacting with Cisco Catalyst Center after updating or
              creating the user or role.
        """

        config_updated = False
        config_created = False
        task_response = None
        responses = {}
        # check if the given user or role config exists and decided on updated/created operation need to be done.

        if "role_name" in config and config["role_name"] is not None:

            if self.have.get("role_exists"):
                # update the role
                self.valid_role_config_parameters(config).check_return_status()
                desired_role = self.generate_role_payload(self.want, "update")
                self.log("desired role with config {0}".format(str(desired_role)), "INFO")
                if "error" not in desired_role:
                    consolidated_data, update_required_param = self.role_requires_update(self.have["current_role_config"], desired_role)
                    if not consolidated_data:
                        # role does not need update
                        self.msg = "Role does not need any update"
                        self.log(self.msg, "INFO")
                        responses["role_operation"] = {"response": config}
                        self.result["response"] = self.msg
                        self.status = "success"
                        return self

                    task_response = self.update_role(update_required_param)
                else:
                    task_response = desired_role

            else:
                # Create the role
                self.valid_role_config_parameters(config).check_return_status()
                self.log("Creating role with config {0}".format(str(config)), "INFO")
                role_info_params = self.generate_role_payload(self.want, "create")
                if "error" not in role_info_params:
                    filtered_data, overall_update_required = self.get_permissions(self.want, role_info_params, "create")
                    denied_permissions = self.find_denied_permissions(self.want)
                    denied_required, create_role_params = self.remove_denied_operations(filtered_data, denied_permissions)
                    if denied_required or overall_update_required:
                        task_response = self.create_role(create_role_params)
                    else:
                        task_response = self.create_role(role_info_params)
                else:
                    task_response = role_info_params

        elif config["username"] is not None or config["email"] is not None:
            if self.have.get("user_exists"):
                # update the user
                self.valid_user_config_parameters(config).check_return_status()
                (consolidated_data, update_required_param) = self.user_requires_update(self.have["current_user_config"], self.have["current_role_id_config"])
                self.log(update_required_param)
                if not consolidated_data:
                    # user does not need update
                    self.msg = "User does not need any update"
                    self.log(self.msg, "INFO")
                    responses["role_operation"] = {"response": config}
                    self.result["response"] = self.msg
                    self.status = "success"
                    return self

                if update_required_param.get("role_list"):
                    user_in_have = self.have["current_user_config"]
                    update_param = update_required_param
                    update_param["username"] = user_in_have.get("username")
                    update_param["user_id"] = user_in_have.get("user_id")
                    user_info_params = self.snake_to_camel_case(update_param)
                    task_response = self.update_user(user_info_params)
                else:
                    task_response = {"error": "Role name is not present in the Cisco Catalyst Center: Please provide a valid role name"}
            else:
                # Create the user
                self.valid_user_config_parameters(config).check_return_status()
                self.log("Creating user with config {0}".format(str(config)), "INFO")
                user_params = self.want

                user_details = {}
                for key, value in user_params.items():
                    if value is not None:
                        if key != "role_list":
                            user_details[key] = value
                        else:
                            current_role = self.have.get("current_role_id_config")
                            user_details[key] = []
                            for role_name in user_params["role_list"]:
                                role_id = current_role.get(role_name.lower())
                                if role_id:
                                    user_details[key].append(role_id)
                                else:
                                    self.log("Role ID for {0} not found in current_role_id_config".format(str(role_name)))

                if "role_list" not in user_details:
                    user_details["role_list"] = ["6486ce98ff1f0d0c8be622fb"]

                if user_details.get("role_list"):
                    user_info_params = self.snake_to_camel_case(user_details)
                    task_response = self.create_user(user_info_params)
                else:
                    task_response = {"error": "Role name is not present in the Cisco Catalyst Center: Please provide a valid role name"}

        if "error" in task_response:
            config_created = False
        else:
            config_created = True

        if config_updated:
            self.log("Task response {0}".format(str(task_response)), "INFO")
            responses["users_operation"] = {"response": task_response}
            self.msg = responses
            self.result["response"] = self.msg
            self.status = "success"
            self.log(self.msg, "INFO")
            return self

        if config_created:
            self.log("Task respoonse {0}".format(str(task_response)), "INFO")
            responses["users_operation"] = {"response": task_response}
            self.msg = responses
            self.result["response"] = self.msg
            self.status = "success"
            self.log(self.msg, "INFO")
            return self

        self.msg = "Task response: {0}".format(str(task_response.get("error")))
        self.log(self.msg, "ERROR")
        self.status = "failed"
        return self

    def get_current_config(self, input_config):
        """
        Retrieve user and role details from Cisco Catalyst Center based on input parameters.

        Parameters:
            - self (object): An instance of the class used for interacting with Cisco Catalyst Center.
            - input_config (dict): A dictionary containing input parameters for retrieving user or role details.

        Returns:
            - user containing:
                - user_exists (bool): True if the user exists, False otherwise.
                - current_user_configuration (dict): Dictionary containing current user details.
                - current_role_id (dict): Dictionary containing current role IDs.
                - role_exists (bool): True if the role exists, False otherwise.
            - role containing:
                - role_exists (bool): True if the role exists, False otherwise.
                - current_role_configuration (dict): Dictionary containing current role details.

        Description:
            - Checks the existence of a user and retrieves user details in Cisco Catalyst Center
              by querying the "get_users_ap_i" function in the "user_and_roles" family.
            - Checks the existence of a role and retrieves role details in Cisco Catalyst Center
              by querying the "get_roles_ap_i" function in the "user_and_roles" family.
            - Logs errors if required parameters are missing in the playbook config.
        """

        user_exists = False
        role_exists = False
        current_user_configuration = {}
        current_role_configuration = {}
        current_role_id = {}
        response_user = None
        response_role = None

        response_user = self.get_user()

        response_role = self.get_role()

        if response_user and response_role:
            response_user = self.camel_to_snake_case(response_user)
            response_role = self.camel_to_snake_case(response_role)

            users = response_user.get("response", {0}).get("users", [])
            roles = response_role.get("response", {0}).get("roles", [])

            if "role_name" in input_config and input_config["role_name"] is not None:
                for role in roles:
                    if role.get("name") == input_config.get("role_name"):
                        current_role_configuration = role
                        role_exists = True

                return role_exists, current_role_configuration

            elif input_config["username"] is not None or input_config["email"] is not None:
                for user in users:
                    if user.get("username") == input_config.get("username"):
                        current_user_configuration = user
                        user_exists = True
                    elif input_config.get("email") is not None:
                        if user.get("email") == input_config.get("email"):
                            current_user_configuration = user
                            user_exists = True

                if input_config.get("role_list") is not None and input_config.get("role_list"):
                    for role in roles:
                        if role.get("name").lower() == input_config.get("role_list")[0].lower():
                            current_role_id[role.get("name").lower()] = role.get("role_id")
                            role_exists = True
                return user_exists, role_exists, current_user_configuration, current_role_id

    def create_user(self, user_params):
        """
        Create a new user in Cisco Catalyst Center with the provided parameters.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - user_params (dict): A dictionary containing user information.
        Returns:
            - response (dict): The API response from the "create_user" function.
        Description:
            - Sends a request to create a new user in Cisco Catalyst Center using the provided user parameters.
            - Uses the "user_and_roles" family and "add_user_ap_i" function for the API call.
            - Logs the provided user parameters and the received API response.
            - Returns the API response from the "create_user" function.
        """

        try:
            self.log("Create user with user_info_params: {0}".format(str(user_params)), "DEBUG")
            response = self.dnac._exec(
                family="user_and_roles",
                function="add_user_ap_i",
                op_modifies=True,
                params=user_params,
            )
            self.log("Received API response from create_user: {0}".format(str(response)), "DEBUG")
            return response

        except Exception as e:
            error_message = "Mandatory field not present: An error occurred while creating the user: {0}".format(str(e))
            return {"error": error_message}

    def create_role(self, role_params):
        """
        Create a new role in Cisco Catalyst Center with the provided parameters.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - role_params (dict): A dictionary containing role information.
        Returns:
            - response (dict): The API response from the "create_role" function.
        Description:
            - Sends a request to create a new role in Cisco Catalyst Center using the provided role parameters.
            - Utilizes the "user_and_roles" family and "add_role_ap_i" function for the API request.
            - Logs the provided role parameters and the received API response.
            - Returns the API response from the "create_role" function.
        """

        try:
            self.log("Create role with role_info_params: {0}".format(str(role_params)), "DEBUG")
            response = self.dnac._exec(
                family="user_and_roles",
                function="add_role_ap_i",
                op_modifies=True,
                params=role_params,
            )
            self.log("Received API response from create_role: {0}".format(str(response)), "DEBUG")
            return response

        except Exception as e:
            error_message = "An error occurred while creating the role without access-level parameters and permissions: {0}".format(str(e))
            return {"error": error_message}

    def get_user(self):
        """
        Retrieve users from Cisco Catalyst Center.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Returns:
            - response (dict): The API response from the "get_users_api" function.
        Description:
            - Sends a request to retrieve users from Cisco Catalyst Center using the "user_and_roles" family
              and "get_users_ap_i" function.
            - Logs the received API response and returns it.
        """

        response = self.dnac._exec(
            family="user_and_roles",
            function="get_users_ap_i",
            op_modifies=True,
            params={"invoke_source": "external"},
        )
        self.log("Received API response from get_users_api: {0}".format(str(response)), "DEBUG")
        return response

    def get_role(self):
        """
        Retrieve roles from Cisco Catalyst Center.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Returns:
            - response (dict): The API response from the "get_roles" function.
        Description:
            - Sends a request to retrieve roles from Cisco Catalyst Center using the "user_and_roles" family
              and "get_roles_ap_i" function.
            - Logs the received API response and returns it.
        """

        response = self.dnac._exec(
            family="user_and_roles",
            function="get_roles_ap_i",
            op_modifies=True,
        )
        self.log("Received API response from get_roles_api: {0}".format(str(response)), "DEBUG")
        return response

    def generate_role_payload(self, role_config, role_operation):
        """
        Generate a role payload for Cisco Catalyst Center.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - role_config (dict): A dictionary containing the configuration for the role.
        Returns:
            - payload (dict): A dictionary containing the payload for the role with processed resource types and operations.
        Description:
            - Generates a payload for a role based on the given role configuration.
            - Processes various sections of the role configuration, such as assurance, network analytics,
              network design, network provision, network services, platform, security, system, and utilities.
            - Validates permissions and converts them to corresponding operations using the convert_permission_to_operations method.
            - If the permission is valid and not set to "deny", constructs a resource type entry with operations and appends it to resource_types.
            - The final payload includes the role name, description, and the list of resource types with operations.
        """

        if not role_config:
            return None

        role_name = role_config.get("role_name", "")
        description = role_config.get("description", "")

        resource_types = []
        unique_types = {}

        # Process assurance rules
        if "assurance" in role_config and role_config.get("assurance") is not None:
            if role_operation != "update":
                default_entries = [
                    "Assurance.Monitoring and Troubleshooting",
                    "Assurance.Monitoring Settings",
                    "Assurance.Troubleshooting Tools"
                ]
                for entry in default_entries:
                    new_entry = {
                        "type": entry,
                        "operations": ["gRead"]
                    }
                    unique_types[new_entry["type"]] = new_entry
            for assurance in role_config["assurance"]:
                for resource, permission in assurance.items():
                    if permission is None:
                        continue
                    else:
                        permission = permission.lower()

                    if permission not in ["read", "write", "deny", None]:
                        return {"error": "Invalid permission {0} for assurance resource {1}".format(permission, resource)}

                    if permission != "deny" and permission is not None:
                        operations = self.convert_permission_to_operations(permission)

                        if resource == "overall":
                            new_entries = [
                                "Assurance.Monitoring and Troubleshooting",
                                "Assurance.Monitoring Settings",
                                "Assurance.Troubleshooting Tools"
                            ]
                            for entry in new_entries:
                                new_entry = {
                                    "type": entry,
                                    "operations": operations
                                }
                                unique_types[new_entry["type"]] = new_entry

                        elif resource == "monitoring_and_troubleshooting":
                            new_entry = {
                                "type": "Assurance.Monitoring and Troubleshooting",
                                "operations": operations
                            }
                            unique_types[new_entry["type"]] = new_entry

                        else:
                            new_entry = {
                                "type": "Assurance.{0}".format(resource.replace("_", " ").title()),
                                "operations": operations
                            }
                            unique_types[new_entry["type"]] = new_entry

            resource_types = list(unique_types.values())

        else:
            if role_operation != "update":
                default_entries = [
                    "Assurance.Monitoring and Troubleshooting",
                    "Assurance.Monitoring Settings",
                    "Assurance.Troubleshooting Tools"
                ]
                for entry in default_entries:
                    new_entry = {
                        "type": entry,
                        "operations": ["gRead"]
                    }
                    unique_types[new_entry["type"]] = new_entry

                resource_types = list(unique_types.values())

        # Process network analytics rules
        if "network_analytics" in role_config and role_config.get("network_analytics") is not None:
            if role_operation != "update":
                new_entry = {
                    "type": "Network Analytics.Data Access",
                    "operations": ["gRead"]
                }
                unique_types[new_entry["type"]] = new_entry

            for network_analytics in role_config["network_analytics"]:
                for resource, permission in network_analytics.items():
                    if permission is None:
                        continue
                    else:
                        permission = permission.lower()

                    if permission not in ["read", "write", "deny", None]:
                        return {"error": "Invalid permission {0} for network analytics resource {1}".format(permission, resource)}

                    if permission != "deny" and permission is not None:
                        operations = self.convert_permission_to_operations(permission)

                        if resource == "overall":
                            new_entry = {
                                "type": "Network Analytics.Data Access",
                                "operations": operations
                            }
                            unique_types[new_entry["type"]] = new_entry

                        else:
                            new_entry = {
                                "type": "Network Analytics.{0}".format(resource.replace("_", " ").title()),
                                "operations": operations
                            }
                            unique_types[new_entry["type"]] = new_entry

            resource_types = list(unique_types.values())

        else:
            if role_operation != "update":
                new_entry = {
                    "type": "Network Analytics.Data Access",
                    "operations": ["gRead"]
                }
                unique_types[new_entry["type"]] = new_entry

                resource_types = list(unique_types.values())

        # Process network design rules
        if "network_design" in role_config and role_config.get("network_design") is not None:
            if role_operation != "update":
                default_entries = [
                    "Network Design.Advanced Network Settings",
                    "Network Design.Image Repository",
                    "Network Design.Network Hierarchy",
                    "Network Design.Network Profiles",
                    "Network Design.Network Settings",
                    "Network Design.Virtual Network"
                ]
                for entry in default_entries:
                    new_entry = {
                        "type": entry,
                        "operations": ["gRead"]
                    }
                    unique_types[new_entry["type"]] = new_entry

            for network_design in role_config["network_design"]:
                for resource, permission in network_design.items():
                    if permission is None:
                        continue
                    else:
                        permission = permission.lower()

                    if permission not in ["read", "write", "deny", None]:
                        return {"error": "Invalid permission {0} for network design resource {1}".format(permission, resource)}

                    if permission != "deny" and permission is not None:
                        operations = self.convert_permission_to_operations(permission)

                        if resource == "overall":
                            new_entries = [
                                "Network Design.Advanced Network Settings",
                                "Network Design.Image Repository",
                                "Network Design.Network Hierarchy",
                                "Network Design.Network Profiles",
                                "Network Design.Network Settings",
                                "Network Design.Virtual Network"
                            ]
                            for entry in new_entries:
                                new_entry = {
                                    "type": entry,
                                    "operations": operations
                                }
                                unique_types[new_entry["type"]] = new_entry

                        else:
                            new_entry = {
                                "type": "Network Design.{0}".format(resource.replace("_", " ").title()),
                                "operations": operations
                            }
                            unique_types[new_entry["type"]] = new_entry

            resource_types = list(unique_types.values())

        else:
            if role_operation != "update":
                default_entries = [
                    "Network Design.Advanced Network Settings",
                    "Network Design.Image Repository",
                    "Network Design.Network Hierarchy",
                    "Network Design.Network Profiles",
                    "Network Design.Network Settings",
                    "Network Design.Virtual Network"
                ]
                for entry in default_entries:
                    new_entry = {
                        "type": entry,
                        "operations": ["gRead"]
                    }
                    unique_types[new_entry["type"]] = new_entry

                resource_types = list(unique_types.values())

        # Process network provision rules
        if "network_provision" in role_config and role_config.get("network_provision") is not None:
            if role_operation != "update":
                default_entries = [
                    "Network Provision.Compliance",
                    "Network Provision.EoX",
                    "Network Provision.Image Update",
                    "Network Provision.Inventory Management.Device Configuration",
                    "Network Provision.Inventory Management.Discovery",
                    "Network Provision.Inventory Management.Network Device",
                    "Network Provision.Inventory Management.Port Management",
                    "Network Provision.Inventory Management.Topology",
                    "Network Provision.License",
                    "Network Provision.Network Telemetry",
                    "Network Provision.PnP",
                    "Network Provision.Provision"
                ]
                for entry in default_entries:
                    new_entry = {
                        "type": entry,
                        "operations": ["gRead"]
                    }
                    unique_types[new_entry["type"]] = new_entry

            if not isinstance(role_config["network_provision"], list):
                return {"error": "The given network_provision is not in type: list"}

            for provision in role_config["network_provision"]:
                for resource, permission in provision.items():
                    if isinstance(permission, list):
                        # Handle nested inventory_management
                        for sub_resource, sub_permission in permission[0].items():
                            if sub_permission is None:
                                continue
                            else:
                                sub_permission = sub_permission.lower()

                            if sub_permission not in ["read", "write", "deny", None]:
                                return {"error": "Invalid permission {0} for sub-resource {1}".format(str(sub_permission), str(sub_resource))}
                            if sub_permission != "deny" and sub_permission is not None:
                                operations = self.convert_permission_to_operations(sub_permission)

                                if sub_resource == "overall":
                                    new_entries = [
                                        "Network Provision.Inventory Management.Device Configuration",
                                        "Network Provision.Inventory Management.Discovery",
                                        "Network Provision.Inventory Management.Network Device",
                                        "Network Provision.Inventory Management.Port Management",
                                        "Network Provision.Inventory Management.Topology"
                                    ]
                                    for entry in new_entries:
                                        new_entry = {
                                            "type": entry,
                                            "operations": operations
                                        }
                                        unique_types[new_entry["type"]] = new_entry

                                else:
                                    new_entry = {
                                        "type": "Network Provision.{0}.{1}".format(resource.replace("_", " ").title(), sub_resource.replace("_", " ").title()),
                                        "operations": operations
                                    }
                                    unique_types[new_entry["type"]] = new_entry

                        resource_types = list(unique_types.values())

                    else:
                        if permission is None:
                            continue
                        else:
                            permission = permission.lower()

                        if permission not in ["read", "write", "deny", None]:
                            return {"error": "Invalid permission {0} for resource {1}".format(str(permission), str(resource))}
                        if permission != "deny" and permission is not None:
                            operations = self.convert_permission_to_operations(permission)

                            if resource == "overall":
                                new_entries = [
                                    "Network Provision.Compliance",
                                    "Network Provision.EoX",
                                    "Network Provision.Image Update",
                                    "Network Provision.Inventory Management.Device Configuration",
                                    "Network Provision.Inventory Management.Discovery",
                                    "Network Provision.Inventory Management.Network Device",
                                    "Network Provision.Inventory Management.Port Management",
                                    "Network Provision.Inventory Management.Topology",
                                    "Network Provision.License",
                                    "Network Provision.Network Telemetry",
                                    "Network Provision.PnP",
                                    "Network Provision.Provision"
                                ]
                                for entry in new_entries:
                                    new_entry = {
                                        "type": entry,
                                        "operations": operations
                                    }
                                    unique_types[new_entry["type"]] = new_entry

                            elif resource == "eox":
                                new_entry = {
                                    "type": "Network Provision.EoX",
                                    "operations": operations
                                }
                                unique_types[new_entry["type"]] = new_entry

                            elif resource == "pnp":
                                new_entry = {
                                    "type": "Network Provision.PnP",
                                    "operations": operations
                                }
                                unique_types[new_entry["type"]] = new_entry

                            else:
                                new_entry = {
                                    "type": "Network Provision.{0}".format(resource.replace("_", " ").title()),
                                    "operations": operations
                                }
                                unique_types[new_entry["type"]] = new_entry

            resource_types = list(unique_types.values())

        else:
            if role_operation != "update":
                default_entries = [
                    "Network Provision.Compliance",
                    "Network Provision.EoX",
                    "Network Provision.Image Update",
                    "Network Provision.Inventory Management.Device Configuration",
                    "Network Provision.Inventory Management.Discovery",
                    "Network Provision.Inventory Management.Network Device",
                    "Network Provision.Inventory Management.Port Management",
                    "Network Provision.Inventory Management.Topology",
                    "Network Provision.License",
                    "Network Provision.Network Telemetry",
                    "Network Provision.PnP",
                    "Network Provision.Provision"
                ]
                for entry in default_entries:
                    new_entry = {
                        "type": entry,
                        "operations": ["gRead"]
                    }
                    unique_types[new_entry["type"]] = new_entry

                resource_types = list(unique_types.values())

        # Process network services rules
        if "network_services" in role_config and role_config.get("network_services") is not None:
            if role_operation != "update":
                default_entries = [
                    "Network Services.App Hosting",
                    "Network Services.Bonjour",
                    "Network Services.Stealthwatch",
                    "Network Services.Umbrella"
                ]
                for entry in default_entries:
                    new_entry = {
                        "type": entry,
                        "operations": ["gRead"]
                    }
                    unique_types[new_entry["type"]] = new_entry

            for services in role_config["network_services"]:
                for resource, permission in services.items():
                    if permission is None:
                        continue
                    else:
                        permission = permission.lower()

                    if permission not in ["read", "write", "deny", None]:
                        return {"error": "Invalid permission {0} for network services resource {1}".format(permission, resource)}
                    if permission != "deny" and permission is not None:
                        operations = self.convert_permission_to_operations(permission)

                        if resource == "overall":
                            new_entries = [
                                "Network Services.App Hosting",
                                "Network Services.Bonjour",
                                "Network Services.Stealthwatch",
                                "Network Services.Umbrella"
                            ]
                            for entry in new_entries:
                                new_entry = {
                                    "type": entry,
                                    "operations": operations
                                }
                                unique_types[new_entry["type"]] = new_entry

                        else:
                            new_entry = {
                                "type": "Network Services.{0}".format(resource.replace("_", " ").title()),
                                "operations": operations
                            }
                            unique_types[new_entry["type"]] = new_entry

            resource_types = list(unique_types.values())

        else:
            if role_operation != "update":
                default_entries = [
                    "Network Services.App Hosting",
                    "Network Services.Bonjour",
                    "Network Services.Stealthwatch",
                    "Network Services.Umbrella"
                ]
                for entry in default_entries:
                    new_entry = {
                        "type": entry,
                        "operations": ["gRead"]
                    }
                    unique_types[new_entry["type"]] = new_entry

                resource_types = list(unique_types.values())

        # Process platform rules
        if "platform" in role_config and role_config.get("platform") is not None:
            for platform in role_config["platform"]:
                for resource, permission in platform.items():
                    if permission is None:
                        continue
                    else:
                        permission = permission.lower()

                    if permission not in ["read", "write", "deny", None]:
                        return {"error": "Invalid permission {0} for platform resource {1}".format(permission, resource)}
                    if permission != "deny" and permission is not None:
                        operations = self.convert_permission_to_operations(permission)
                        if resource == "overall":
                            new_entries = [
                                "Platform.APIs",
                                "Platform.Bundles",
                                "Platform.Events",
                                "Platform.Reports"
                            ]
                            for entry in new_entries:
                                new_entry = {
                                    "type": entry,
                                    "operations": operations
                                }
                                unique_types[new_entry["type"]] = new_entry

                        elif resource == "apis":
                            new_entry = {
                                "type": "Platform.APIs",
                                "operations": operations
                            }
                            unique_types[new_entry["type"]] = new_entry

                        else:
                            new_entry = {
                                "type": "Platform.{0}".format(resource.replace("_", " ").title()),
                                "operations": operations
                            }
                            unique_types[new_entry["type"]] = new_entry

            resource_types = list(unique_types.values())

        # Process security rules
        if "security" in role_config and role_config.get("security") is not None:
            if role_operation != "update":
                default_entries = [
                    "Security.Group-Based Policy",
                    "Security.IP Based Access Control",
                    "Security.Security Advisories"
                ]
                for entry in default_entries:
                    new_entry = {
                        "type": entry,
                        "operations": ["gRead"]
                    }
                    unique_types[new_entry["type"]] = new_entry

            for security in role_config["security"]:
                for resource, permission in security.items():
                    if permission is None:
                        continue
                    else:
                        permission = permission.lower()

                    if permission not in ["read", "write", "deny", None]:
                        return {"error": "Invalid permission {0} for security resource {1}".format(permission, resource)}
                    if permission != "deny" and permission is not None:
                        operations = self.convert_permission_to_operations(permission)

                        if resource == "overall":
                            new_entries = [
                                "Security.Group-Based Policy",
                                "Security.IP Based Access Control",
                                "Security.Security Advisories"
                            ]
                            for entry in new_entries:
                                new_entry = {
                                    "type": entry,
                                    "operations": operations
                                }
                                unique_types[new_entry["type"]] = new_entry

                        elif resource == "ip_based_access_control":
                            new_entry = {
                                "type": "Security.IP Based Access Control",
                                "operations": operations
                            }
                            unique_types[new_entry["type"]] = new_entry

                        elif resource == "group_based_policy":
                            new_entry = {
                                "type": "Security.Group-Based Policy",
                                "operations": operations
                            }
                            unique_types[new_entry["type"]] = new_entry

                        else:
                            new_entry = {
                                "type": "Security.{0}".format(resource.replace("_", " ").title()),
                                "operations": operations
                            }
                            unique_types[new_entry["type"]] = new_entry

            resource_types = list(unique_types.values())

        else:
            if role_operation != "update":
                default_entries = [
                    "Security.Group-Based Policy",
                    "Security.IP Based Access Control",
                    "Security.Security Advisories"
                ]
                for entry in default_entries:
                    new_entry = {
                        "type": entry,
                        "operations": ["gRead"]
                    }
                    unique_types[new_entry["type"]] = new_entry

                resource_types = list(unique_types.values())

        # Process system rules
        if "system" in role_config and role_config.get("system") is not None:
            if role_operation != "update":
                default_entries = [
                    "System.Machine Reasoning",
                    "System.System Management"
                ]
                for entry in default_entries:
                    new_entry = {
                        "type": entry,
                        "operations": ["gRead"]
                    }
                    unique_types[new_entry["type"]] = new_entry

            for system in role_config["system"]:
                for resource, permission in system.items():
                    if permission is None:
                        continue
                    else:
                        permission = permission.lower()

                    if permission not in ["read", "write", "deny", None]:
                        return {"error": "Invalid permission {0} for system resource {1}".format(permission, resource)}
                    if permission != "deny" and permission is not None:
                        operations = self.convert_permission_to_operations(permission)

                        if resource == "overall":
                            new_entries = [
                                "System.Machine Reasoning",
                                "System.System Management"
                            ]
                            for entry in new_entries:
                                new_entry = {
                                    "type": entry,
                                    "operations": operations
                                }
                                unique_types[new_entry["type"]] = new_entry

                        else:
                            new_entry = {
                                "type": "System.{0}".format(resource.replace("_", " ").title()),
                                "operations": operations
                            }
                            unique_types[new_entry["type"]] = new_entry

            resource_types = list(unique_types.values())

        else:
            if role_operation != "update":
                default_entries = [
                    "System.Machine Reasoning",
                    "System.System Management"
                ]
                for entry in default_entries:
                    new_entry = {
                        "type": entry,
                        "operations": ["gRead"]
                    }
                    unique_types[new_entry["type"]] = new_entry

                resource_types = list(unique_types.values())

        # Process utilities rules
        if "utilities" in role_config and role_config.get("utilities") is not None:
            if role_operation != "update":
                default_entries = [
                    "Utilities.Event Viewer",
                    "Utilities.Network Reasoner",
                    "Utilities.Search"
                ]
                new_entry1 = {
                    "type": "Utilities.Scheduler",
                    "operations": ["gRead", "gUpdate", "gCreate", "gRemove"]
                }
                unique_types[new_entry1["type"]] = new_entry1

                for entry in default_entries:
                    new_entry = {
                        "type": entry,
                        "operations": ["gRead"]
                    }
                    unique_types[new_entry["type"]] = new_entry

            for utilities in role_config["utilities"]:
                for resource, permission in utilities.items():
                    if permission is None:
                        continue
                    else:
                        permission = permission.lower()

                    if permission not in ["read", "write", "deny", None]:
                        return {"error": "Invalid permission {0} for utilities resource {1}".format(permission, resource)}
                    if permission != "deny" and permission is not None:
                        operations = self.convert_permission_to_operations(permission)

                        if resource == "overall":
                            new_entries = [
                                "Utilities.Event Viewer",
                                "Utilities.Network Reasoner",
                                "Utilities.Search",
                                "Utilities.Audit Log",
                                "Utilities.Remote Device Support",
                                "Utilities.Scheduler"
                            ]
                            for entry in new_entries:
                                new_entry = {
                                    "type": entry,
                                    "operations": operations
                                }
                                unique_types[new_entry["type"]] = new_entry

                        else:
                            new_entry = {
                                "type": "Utilities.{0}".format(resource.replace("_", " ").title()),
                                "operations": operations
                            }
                            unique_types[new_entry["type"]] = new_entry

            resource_types = list(unique_types.values())

        else:
            if role_operation != "update":
                default_entries = [
                    "Utilities.Event Viewer",
                    "Utilities.Network Reasoner",
                    "Utilities.Search"
                ]
                new_entry1 = {
                    "type": "Utilities.Scheduler",
                    "operations": ["gRead", "gUpdate", "gCreate", "gRemove"]
                }
                unique_types[new_entry1["type"]] = new_entry1

                for entry in default_entries:
                    new_entry = {
                        "type": entry,
                        "operations": ["gRead"]
                    }
                    unique_types[new_entry["type"]] = new_entry

                resource_types = list(unique_types.values())

        # Construct the final payload
        payload = {
            "role": role_name,
            "description": description,
            "resourceTypes": resource_types
        }

        return payload

    def convert_permission_to_operations(self, permission):
        """
        Convert a permission string to a list of operations.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - permission (str): A string representing the permission level (e.g., "read" or "write").
        Returns:
            - list: A list of strings representing operations associated with the given permission level.
                    Returns None if the permission level is not recognized.
        Description:
            - This method converts a permission string to a corresponding list of operations.
            - For "read" or "Read" permissions, it returns a list containing "gRead".
            - For "write" or "Write" permissions, it returns a list containing "gRead", "gUpdate", "gCreate", and "gRemove".
            - If the permission level is not recognized, it returns None.
        """

        if permission == "read":
            return ["gRead"]
        elif permission == "write":
            return ["gRead", "gUpdate", "gCreate", "gRemove"]
        else:
            return None

    def role_requires_update(self, current_role, desired_role):
        """
        Check if the role requires updates and save parameters to update.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - current_role (dict): Dictionary containing current role information.
            - desired_role (dict): Dictionary containing desired role information.
        Returns:
            - bool: True if the role requires updates, False otherwise.
            - updated_get_have (dict): Updated dictionary with parameters that need to be updated.
        Description:
            - This method checks if the current role information needs to be updated based on the desired role information.
            - It compares the resource types and operations between current_role and desired_role.
            - If any resource type is not found in current_role but exists in desired_role, it adds it to current_role.
            - Removes denied operations based on denied permissions found in self.want.
            - Returns values indicating whether updates are required and the updated role information.
        """

        update_required = False

        for want_resource in desired_role["resourceTypes"]:
            found = False
            for have_resource in current_role["resource_types"]:
                if have_resource["type"] == want_resource["type"]:
                    found = True
                    if have_resource["operations"] != want_resource["operations"]:
                        have_resource["operations"] = want_resource["operations"]
                        update_required = True
                    break
            if not found:
                current_role["resource_types"].append(want_resource)
                update_required = True

        update_role_param = {}
        if desired_role.get("description") is not None:
            if current_role.get("description") != desired_role.get("description"):
                update_role_param["description"] = desired_role["description"]
                update_required = True
            elif "description" not in update_role_param:
                update_role_param["description"] = current_role["description"]
        else:
            update_role_param["description"] = current_role["description"]

        # Create the updated dictionary
        updated_get_have = {
            "roleId": current_role["role_id"],
            "description": update_role_param["description"],
            "resourceTypes": current_role["resource_types"]
        }

        filtered_data, overall_update_required = self.get_permissions(self.want, updated_get_have, "update")

        denied_permissions = self.find_denied_permissions(self.want)
        denied_update_required, updated_get_have = self.remove_denied_operations(filtered_data, denied_permissions)

        if update_required or denied_update_required or overall_update_required:
            role_update_required = True
            return role_update_required, updated_get_have
        else:
            role_update_required = False
            return role_update_required, updated_get_have

    def user_requires_update(self, current_user, current_role):
        """
        Check if the user requires updates and save parameters to update.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - current_user (dict): Dictionary containing current user information.
            - current_role (dict): Dictionary containing role mappings.
        Returns:
            - bool: True if the user requires updates, False otherwise.
            - update_user_param (dict): Dictionary containing parameters that need to be updated.
        Description:
            - This method checks if the current user information needs to be updated based on the desired user information.
            - It compares specific fields such as "first_name", "last_name", "email", "username", and "role_list".
            - If any of these fields differ between current_user and self.want, update_user_param is populated with the desired values.
            - Returns values indicating whether updates are required and the parameters to update if so.
        """

        update_required = False
        update_user_param = {}

        if self.want.get("first_name") is not None:
            if current_user.get("first_name") != self.want.get("first_name"):
                update_user_param["first_name"] = self.want["first_name"]
                update_required = True
            elif "first_name" not in update_user_param:
                update_user_param["first_name"] = current_user["first_name"]
        else:
            update_user_param["first_name"] = current_user["first_name"]

        if self.want.get("last_name") is not None:
            if current_user.get("last_name") != self.want.get("last_name"):
                update_user_param["last_name"] = self.want["last_name"]
                update_required = True
            elif "last_name" not in update_user_param:
                update_user_param["last_name"] = current_user["last_name"]
        else:
            update_user_param["last_name"] = current_user["last_name"]

        if self.want.get("email") is not None:
            if current_user.get("email") != self.want.get("email"):
                update_user_param["email"] = self.want["email"]
                update_required = True
            elif "email" not in update_user_param:
                update_user_param["email"] = current_user["email"]
        else:
            update_user_param["email"] = current_user["email"]

        if self.want.get("role_list") is not None:
            role_name = self.want.get("role_list")[0].lower()
            if role_name in current_role:
                role_id = current_role[role_name]
                if current_user.get("role_list")[0] != role_id:
                    update_user_param["role_list"] = [role_id]
                    update_required = True
                else:
                    update_user_param["role_list"] = current_user["role_list"]
            else:
                update_user_param["role_list"] = []
                update_required = True
        else:
            update_user_param["role_list"] = current_user["role_list"]

        return update_required, update_user_param

    def update_user(self, user_params):
        """
        Update a user in Cisco Catalyst Center with the provided parameters.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - user_params (dict): A dictionary containing user information.
        Returns:
            - response (dict): The API response from the "update_user" function.
        Description:
            - This method sends a request to update a user in Cisco Catalyst Center using the provided
            - user parameters. It logs the response and returns it.
        """

        try:
            self.log("Update user with user_info_params: {0}".format(str(user_params)), "DEBUG")
            response = self.dnac._exec(
                family="user_and_roles",
                function="update_user_ap_i",
                op_modifies=True,
                params=user_params,
            )
            self.log("Received API response from update_user: {0}".format(str(response)), "DEBUG")
            return response

        except Exception as e:
            error_message = "Mandatory field not present: An error occurred while updating the user: {0}".format(str(e))
            return {"error": error_message}

    def update_role(self, role_params):
        """
        Update a role in Cisco Catalyst Center with the provided parameters.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - role_params (dict): A dictionary containing role information.
        Returns:
            - response (dict): The API response from the "update_role" function.
        Description:
            - This method sends a request to update a role in Cisco Catalyst Center using the provided
              role parameters. It first logs the role parameters at the "DEBUG" level. Then it calls the"_exec" method
              of the "dnac" object to perform the API request. The API request is specified with the "user_and_roles" family
              and the "update_role_ap_i" function. The method logs the received API response at the "DEBUG" level and
              finally returns the response.
        """

        self.log("Update role with role_info_params: {0}".format(str(role_params)), "DEBUG")
        response = self.dnac._exec(
            family="user_and_roles",
            function="update_role_ap_i",
            op_modifies=True,
            params=role_params,
        )
        self.log("Received API response from update_role: {0}".format(str(response)), "DEBUG")

        return response

    def find_denied_permissions(self, config, parent_key=""):
        """
        Find all permissions set to "deny" in a configuration structure.
        Parameters:
            - config (dict or list): The configuration structure to search, which can be a nested dictionary or list.
            - parent_key (str): The key path leading to the current position in the configuration (used for nested structures).
        Returns:
            - denied_permissions (list): A list of keys representing paths in the configuration that have "deny" as their value.
        Description:
            - This function recursively searches through a given configuration structure, which can be a dictionary or a list,
              to find all occurrences of the string "deny". It constructs and returns a list of key paths where "deny" is found.
              The key paths are formed by combining parent keys with the current keys or indices, providing a clear path
              to the denied permissions within the nested structure.
        """

        denied_permissions = []

        if isinstance(config, dict):
            for key, value in config.items():
                if parent_key:
                    full_key = "{0}.{1}".format(parent_key, key)
                else:
                    full_key = key

                if isinstance(value, dict) or isinstance(value, list):
                    denied_permissions.extend(self.find_denied_permissions(value, full_key))
                elif isinstance(value, str) and value.lower() == "deny":
                    denied_permissions.append(full_key)

        elif isinstance(config, list):
            for index, item in enumerate(config):
                full_key = "{0}[{1}]".format(parent_key, index)

                if isinstance(item, dict):
                    denied_permissions.extend(self.find_denied_permissions(item, full_key))
                elif isinstance(item, str) and item.lower() == "deny":
                    denied_permissions.append(full_key)

        return denied_permissions

    def remove_denied_operations(self, input_data, denied_permissions):
        """
        Remove denied operations from the input data based on the provided denied permissions.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - input_data (dict): Input data containing resource types that may include denied operations.
            - denied_permissions (list): A list of denied permissions to be removed from input_data.
        Returns:
            - update_required (bool): True if any denied operations were removed, otherwise False.
            - updated_input_data (dict): Input data with denied operations removed.
        Description:
            - This method filters out denied operations from the resource types in the input_data based on the provided denied_permissions.
            - It checks each resource type against the denied permissions to determine if it should be kept or removed.
            - If a resource type matches any of the denied permissions, it is excluded from the updated input_data.
            - The method returns values indicating whether any updates were made (update_required) and the updated input_data.
        """

        resource_types = input_data["resourceTypes"]
        remaining_resource_types = []
        update_required = False

        for resource in resource_types:
            keep_resource = True
            resource_type_lower = resource["type"].lower()
            for denied in denied_permissions:
                denied_type_lower = denied.split(".")[-1].replace("_", " ").replace("[0]", "").lower()

                if denied_type_lower == "network settings":
                    denied_type_lower = "network design.network settings"
                    if denied_type_lower in resource_type_lower:
                        keep_resource = False
                        update_required = True
                        break

                elif denied_type_lower == "provision":
                    denied_type_lower = "network provision.provision"
                    if denied_type_lower in resource_type_lower:
                        keep_resource = False
                        update_required = True
                        break

                elif denied_type_lower == "group based policy":
                    denied_type_lower = "security.group-based policy"
                    if denied_type_lower in resource_type_lower:
                        keep_resource = False
                        update_required = True
                        break

                else:
                    if denied_type_lower in resource_type_lower:
                        keep_resource = False
                        update_required = True
                        break

            if keep_resource:
                remaining_resource_types.append(resource)

        input_data["resourceTypes"] = remaining_resource_types
        return update_required, input_data

    def parse_config(self, config_section):
        """
        Parse the given configuration section into a structured dictionary.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - config_section (dict): A dictionary containing a section of the configuration to be parsed.
        Returns:
            - parsed_config (dict): A dictionary containing the parsed configuration details.
        Description:
            - This method iterates through the provided configuration section and processes each key-value pair.
            - If the value is None, it assigns an empty dictionary to the corresponding key in the parsed configuration.
            - If the value is a non-empty list, it recursively parses the first element of the list.
            - Otherwise, it directly assigns the value to the corresponding key in the parsed configuration.
            - The resulting dictionary represents the structured configuration details.
        """

        parsed_config = {}
        for key, value in config_section.items():
            if value is None:
                parsed_config[key] = {}
            elif isinstance(value, list) and value:
                parsed_config[key] = self.parse_config(value[0])
            else:
                parsed_config[key] = value
        return parsed_config

    def check_permission(self, permissions, resource_type):
        """
        Check if a given resource type has permissions denied or allowed based on the provided permissions.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - permissions (dict): A dictionary containing permission details for various resource types.
            - resource_type (str): A string specifying the resource type for which permissions are being checked.
        Returns:
            - check_deny_update (bool): A boolean indicating if the overall permission is denied.
            - check_permission (bool): A boolean indicating if the permission is allowed.
        Description:
            - This method processes the resource type string to generate a list of keys for navigating through the permissions dictionary.
            - It traverses the permissions dictionary based on the generated keys to find the relevant permission level.
            - If an "overall" permission of "deny" is found at any level, it returns (True, False).
            - If the keys do not match any entry in the permissions dictionary, it returns (False, True).
            - If the keys match and there is no "overall" permission of "deny", it returns (False, True).
        """

        keys = resource_type.lower().replace(" ", "_").split(".")
        current_level = permissions
        for key in keys:
            if key in current_level:
                current_level = current_level[key]
            elif "overall" in current_level and current_level["overall"].lower() == "deny":
                return True, False
            else:
                return False, True

        return False, "overall" not in current_level or current_level["overall"].lower() != "deny"

    def get_operations(self, permissions, resource_type):
        """
        Retrieve specific operations allowed for a given resource type based on the provided permissions.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - permissions (dict): A dictionary containing permission details for various resource types.
            - resource_type (str): A string specifying the resource type for which operations are being retrieved.
        Returns:
            - list: A list of specific operations allowed for the given resource type. If no specific operations are found, an empty list is returned.
        Description:
            - This method processes the resource type string to generate a list of keys for navigating through the permissions dictionary.
            - It traverses the permissions dictionary based on the generated keys to find the relevant permission level.
            - If an "overall" permission of "deny" is found, it collects and returns specific permissions that are not denied.
            - If no specific operations are found or if the "overall" permission is not "deny", it returns an empty list.
        """

        keys = resource_type.lower().replace(" ", "_").split(".")
        current_level = permissions

        for key in keys:
            if key in current_level:
                current_level = current_level[key]

        if "overall" in current_level and current_level["overall"].lower() == "deny":
            specific_permissions = {}
            for k, v in current_level.items():
                if k != "overall" and v.lower() != "deny":
                    specific_permissions[k] = v

            return list(specific_permissions.values())

        return []

    def get_permissions(self, config, input_data, role_operation):
        """
        Retrieve and configure permissions for a role based on the provided configuration and input data.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - config (dict): A dictionary containing configuration details.
            - input_data (dict): A dictionary containing the role details, including "role", "description", and "resourceTypes".
            - role_operation (str): A string indicating the operation type (e.g., "update").
        Returns:
            - result (dict): A dictionary containing the configured role permissions.
            - is_denied (bool): A boolean indicating if any operation is denied.
        Description:
            - This method parses the provided configuration to retrieve permissions for the specified resources in the input data.
              It checks permissions for each resource type and determines the allowed operations.
            - If the role_operation is not "update", it includes the role name in the result. Otherwise, it includes the role ID.
            - It logs the final permissions configuration and returns the result along with a boolean indicating if any operations
            are denied.
        """

        permissions = self.parse_config(config)
        allowed_operations = []
        check_deny = []

        for resource in input_data["resourceTypes"]:
            res_type = resource["type"]
            operations = resource["operations"]

            check_deny_update, check_permission = self.check_permission(permissions, res_type)
            check_deny.append(str(check_deny_update))

            if check_permission:
                specific_operations = self.get_operations(permissions, res_type)
                allowed_operations.append({
                    "type": res_type,
                    "operations": operations if not specific_operations else specific_operations
                })

        if role_operation != "update":
            result = {
                "role": input_data["role"],
                "description": input_data["description"],
                "resourceTypes": allowed_operations
            }
        else:
            result = {
                "roleId": input_data["roleId"],
                "description": input_data["description"],
                "resourceTypes": allowed_operations
            }

        if "True" in check_deny:
            return result, True
        else:
            return result, False

    def get_diff_deleted(self, config):
        """
        Delete a user or role from Cisco Catalyst Center based on the provided parameters.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - config (dict): A dictionary containing configuration details, such as "role_name", "username", and "email".
        Returns:
            - self (object): An instance of the class after the deletion operation is performed.
        Description:
            - This method checks the provided configuration to determine whether a role or user needs to be deleted from
              Cisco Catalyst Center. It verifies if the role or user exists, logs the current state, and then proceeds to delete
              the specified role or user. It logs the response from the deletion operation and updates the status and result
              accordingly.
        """

        config_delete = False

        if "role_name" in config and config["role_name"] is not None:

            if self.have.get("role_exists"):
                self.valid_role_config_parameters(config).check_return_status()
                self.log("Deleting role with config {0}".format(str(config)), "INFO")

                # Check if the role exists in self.have
                current_role = self.have.get("current_role_config")
                role_id_to_delete = {}
                role_id_to_delete["role_id"] = current_role.get("role_id")
                task_response = self.delete_role(role_id_to_delete)
                self.log("Task response {0}".format(str(task_response)), "INFO")
                if "error" in task_response:
                    config_delete = False
                else:
                    config_delete = True

                if config_delete:
                    responses = {}
                    responses["role_operation"] = {"response": task_response}
                    self.msg = responses
                    self.result["response"] = self.msg
                    self.status = "success"
                    self.log(self.msg, "INFO")
                    return self
                else:
                    self.msg = task_response
                    self.log(self.msg, "ERROR")
                    self.status = "failed"
                    return self
            else:
                self.msg = "Please provide a valid role_name for role deletion"
                self.log(self.msg, "ERROR")
                self.status = "failed"
                return self

        elif config["username"] is not None or config["email"] is not None:

            if self.have.get("user_exists"):
                self.valid_user_config_parameters(config).check_return_status()
                self.log("Deleting user with config {0}".format(str(config)), "INFO")

                # Check if the username exists in self.have
                current_user = self.have.get("current_user_config")
                user_id_to_delete = {}
                user_id_to_delete["user_id"] = current_user.get("user_id")
                task_response = self.delete_user(user_id_to_delete)
                self.log("Task response {0}".format(str(task_response)), "INFO")
                config_delete = True

                if config_delete:
                    responses = {}
                    responses["users_operation"] = {"response": task_response}
                    self.msg = responses
                    self.result["response"] = self.msg
                    self.status = "success"
                    self.log(self.msg, "INFO")
                    return self

            else:
                self.msg = "Please provide a valid username or email for user deletion"
                self.log(self.msg, "ERROR")
                self.status = "failed"
                return self

    def delete_user(self, user_params):
        """
        Delete a user in Cisco Catalyst Center with the provided parameters.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - user_params (dict): A dictionary containing user information.
        Returns:
            - response (dict): The API response from the "delete_user" function.
        Description:
            - This method sends a request to delete a user in Cisco Catalyst Center using the provided user parameters.
            - It logs the response and returns it.
            - The function uses the "user_and_roles" family and the "delete_user_ap_i" function from the Cisco Catalyst Center API.
        """

        self.log("delete user with user_params: {0}".format(str(user_params)), "DEBUG")
        response = self.dnac._exec(
            family="user_and_roles",
            function="delete_user_ap_i",
            op_modifies=True,
            params=user_params,
        )
        self.log("Received API response from delete_user: {0}".format(str(response)), "DEBUG")
        return response

    def delete_role(self, role_params):
        """
        Delete a role in Cisco Catalyst Center with the provided parameters
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - role_params (dict): A dictionary containing role information.
        Returns:
            - response (dict): The API response from the "delete_role" function.
        Description:
            - This method sends a request to delete a role in Cisco Catalyst Center using the provided role parameters.
            - It logs the response and returns it.
            - The function uses the "user_and_roles" family and the "delete_role_ap_i" function from the Cisco Catalyst Center API.
        """

        try:
            self.log("delete role with role_params: {0}".format(str(role_params)), "DEBUG")
            response = self.dnac._exec(
                family="user_and_roles",
                function="delete_role_ap_i",
                op_modifies=True,
                params=role_params,
            )
            self.log("Received API response from delete_role: {0}".format(str(response)), "DEBUG")
        except Exception:
            error_message = "An error occurred while deleting the role. Check whether user are assigned to this role: \
                {0}".format(str(self.have.get("role_name")))

            return {"error": error_message}

        return response

    def verify_diff_merged(self, config):
        """
        Verify the merged status (Creation/Updation) of user or role details in Cisco Catalyst Center.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - config (dict): The configuration details to be verified, containing keys like "role_name", "username", and "email".
        Returns:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            - This method checks the merged status of a user or role configuration in Cisco Catalyst Center by retrieving the current state
              (have) and desired state (want) of the configuration. It logs the current and desired states, and validates whether the specified
              user or role exists in the Catalyst Center configuration.
            - The method verifies if the role or user creation or update has been executed successfully by comparing the current state with
              the desired state and checking if any updates are required.
            - If the specified role or user exists, it logs a success message. If the role or user needs to be updated, it checks if the update
              has been successfully verified. In case of any mismatch between the playbook input and the Catalyst Center configuration, it logs
              an appropriate message indicating that the merge task may not have executed successfully.
        """

        if "role_name" in config and config["role_name"] is not None:
            self.get_have(config)
            self.log("Current State (have): {0}".format(str(self.have)), "INFO")
            self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

            # Code to validate ccc config for merged state
            role_exist = self.have.get("role_exists")
            role_name = self.want.get("role_name")

            if role_exist:
                self.status = "success"
                self.msg = "The requested role {0} is present in the Cisco Catalyst Center and its creation has been verified.".format(role_name)
                self.log(self.msg, "INFO")

            desired_role = self.generate_role_payload(self.want, "update")
            (require_update, updated_role_info) = self.role_requires_update(self.have["current_role_config"], desired_role)
            if not require_update:
                self.log("The update for role {0} has been successfully verified. The updated info - {1}".format(role_name, updated_role_info), "INFO")
                self. status = "success"

            if not role_exist:
                self.log("""The playbook input for role {0} does not align with the Cisco Catalyst Center, indicating that the \
                         merge task may not have executed successfully.""".format(role_name), "INFO")

        elif config["username"] is not None or config["email"] is not None:
            self.get_have(config)
            self.log("Current State (have): {0}".format(str(self.have)), "INFO")
            self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

            # Code to validate ccc config for merged state
            user_exist = self.have.get("user_exists")
            user_name = self.have.get("username")

            if user_exist:
                self.status = "success"
                self.msg = "The requested user {0} is present in the Cisco Catalyst Center and its creation has been verified.".format(user_name)
                self.log(self.msg, "INFO")

            (require_update, updated_user_info) = self.user_requires_update(self.have["current_user_config"], self.have["current_role_id_config"])
            if not require_update:
                self.log("The update for user {0} has been successfully verified. The updated info - {1}".format(user_name, updated_user_info), "INFO")
                self. status = "success"

            if not user_exist:
                self.log("""The playbook input for user {0} does not align with the Cisco Catalyst Center, indicating that \
                         the merge task may not have executed successfully.""".format(user_name), "INFO")

        return self

    def verify_diff_deleted(self, config):
        """
        Verify the deletion status of user or role details in Cisco Catalyst Center.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - config (dict): The configuration details to be verified, containing keys like "role_name", "username", and "email".
        Returns:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            - This method checks the deletion status of a user or role configuration in Cisco Catalyst Center.
            - It validates whether the specified site (user or role) exists in the Catalyst Center configuration.
            - If the specified role or user does not exist, it sets the status to "success" and logs a confirmation message.
            - If the role or user still exists, it logs a mismatch message indicating the deletion was not executed successfully.
        """

        if "role_name" in config and config["role_name"] is not None:
            self.get_have(config)
            self.log("Current State (have): {0}".format(str(self.have)), "INFO")
            self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

            role_exist = self.have.get("role_exists")

            if not role_exist:
                self.status = "success"
                msg = """The requested role {0} has already been deleted from the Cisco Catalyst Center and this has been
                    successfully verified.""".format(str(self.want.get("role_name")))
                self.log(msg, "INFO")
                return self

            self.log("""Mismatch between the playbook input for role {0} and the Cisco Catalyst Center indicates that the deletion was \
                     not executed successfully.""".format(str(self.want.get("role_name"))), "INFO")

        elif config["username"] is not None or config["email"] is not None:
            self.get_have(config)
            self.log("Current State (have): {0}".format(str(self.have)), "INFO")
            self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

            user_exist = self.have.get("user_exists")

            if not user_exist:
                self.status = "success"
                msg = """The requested user {0} has already been deleted from the Cisco Catalyst Center and this has been \
                    successfully verified.""".format(str(self.want.get("username")))
                self.log(msg, "INFO")
                return self

            self.log("""Mismatch between the playbook input for user {0} and the Cisco Catalyst Center indicates that the deletion \
                     was not executed successfully.""".format(str(self.want.get("username"))), "INFO")

        return self

    def snake_to_camel_case(self, data):
        """
        Convert keys from snake_case to camelCase in a given dictionary or list of dictionaries recursively.
        Parameters:
            - data (dict or list): A dictionary with keys in snake_case or a list containing such dictionaries.
        Returns:
            - dict or list: A new dictionary with keys converted to camelCase, or a list of dictionaries
              with keys converted to camelCase.
        Description:
            - This function recursively converts keys from snake_case to camelCase in a given dictionary or list of dictionaries.
            - It handles nested dictionaries and lists, converting all keys in each dictionary found. Lists containing dictionaries
              are recursively processed to ensure all contained dictionaries have their keys converted.
        """

        def to_camel_case(snake_str):
            components = snake_str.split("_")
            camel_case_str = components[0]
            for component in components[1:]:
                camel_case_str += component.title()
            return camel_case_str

        if isinstance(data, dict):
            camel_case_data = {}
            for key, value in data.items():
                new_key = to_camel_case(key)

                if isinstance(value, dict):
                    camel_case_data[new_key] = self.snake_to_camel_case(value)
                elif isinstance(value, list):
                    camel_case_list = []
                    for item in value:
                        if isinstance(item, dict):
                            camel_case_list.append(self.snake_to_camel_case(item))
                        else:
                            camel_case_list.append(item)
                    camel_case_data[new_key] = camel_case_list
                else:
                    camel_case_data[new_key] = value

            return camel_case_data
        elif isinstance(data, list):
            camel_case_list = []
            for item in data:
                if isinstance(item, dict):
                    camel_case_list.append(self.snake_to_camel_case(item))
                else:
                    camel_case_list.append(item)
            return camel_case_list
        else:
            return data


def main():
    """ main entry point for module execution
    """
    # Basic Ansible type check or assign default.
    user_role_details = {"dnac_host": {"required": True, "type": "str"},
                         "dnac_port": {"type": "str", "default": "443"},
                         "dnac_username": {"type": "str", "default": "admin", 'aliases': ['user']},
                         "dnac_password": {"type": "str", "no_log": True},
                         "dnac_verify": {"type": "bool", "default": "True"},
                         "dnac_version": {"type": "str", "default": "2.2.3.3"},
                         "dnac_debug": {"type": "bool", "default": False},
                         "dnac_log": {"type": "bool", "default": False},
                         "dnac_log_level": {"type": "str", "default": "WARNING"},
                         "dnac_log_file_path": {"type": "str", "default": "dnac.log"},
                         "config_verify": {"type": "bool", "default": False},
                         "dnac_log_append": {"type": "bool", "default": True},
                         "dnac_api_task_timeout": {"type": "int", "default": 1200},
                         "dnac_task_poll_interval": {"type": "int", "default": 2},
                         "config": {"required": True, "type": "dict"},
                         "validate_response_schema": {"type": "bool", "default": True},
                         "state": {"default": "merged", "choices": ["merged", "deleted"]},
                         }

    module = AnsibleModule(
        argument_spec=user_role_details,
        supports_check_mode=True
    )

    ccc_user_role = UserandRole(module)
    state = ccc_user_role.params.get("state")

    if state not in ccc_user_role.supported_states:
        ccc_user_role.status = "invalid"
        ccc_user_role.msg = "State {0} is invalid".format(state)
        ccc_user_role.check_return_status()

    if "role_details" in ccc_user_role.params.get("config"):
        ccc_user_role.validate_input_yml(ccc_user_role.params.get("config").get("role_details")).check_return_status()
        config_verify = ccc_user_role.params.get("config_verify")

        for config in ccc_user_role.validated_config:
            ccc_user_role.reset_values()
            ccc_user_role.get_want(config).check_return_status()
            ccc_user_role.get_have(config).check_return_status()
            ccc_user_role.get_diff_state_apply[state](config).check_return_status()

            if config_verify:
                ccc_user_role.verify_diff_state_apply[state](config).check_return_status()

    if "user_details" in ccc_user_role.params.get("config"):
        ccc_user_role.validate_input_yml(ccc_user_role.params.get("config").get("user_details")).check_return_status()
        config_verify = ccc_user_role.params.get("config_verify")

        for config in ccc_user_role.validated_config:
            ccc_user_role.reset_values()
            ccc_user_role.get_want(config).check_return_status()
            ccc_user_role.get_have(config).check_return_status()
            ccc_user_role.get_diff_state_apply[state](config).check_return_status()

            if config_verify:
                ccc_user_role.verify_diff_state_apply[state](config).check_return_status()

    module.exit_json(**ccc_user_role.result)


if __name__ == "__main__":
    main()
