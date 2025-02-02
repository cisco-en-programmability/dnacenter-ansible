# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("Madhan Sankaranarayanan, Syed Khadeer Ahmed")

DOCUMENTATION = r"""
---
module: application_policy_workflow_manager
short_description: Resource module for managing application policies in Cisco Catalyst Center.
description:
  - Manages operations to create, update, and delete application, application set, queuing profile and application policies in Cisco Catalyst Center.
  - API to create application, application set, queuing profile and application policies.
  - API to update application, queuing profile and application policies.
  - API to delete application, application set, queuing profile and application policies.

version_added: "6.17.0"
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - Syed Khadeer Ahmed (@syed-khadeerahmed)
  - Madhan Sankaranarayanan (@madhansansel)

options:
  config_verify:
    description: Set to True to verify the Cisco Catalyst Center after applying the playbook config.
    type: bool
    default: False
  state:
    description: The state of Cisco Catalyst Center after module completion.
    type: str
    choices: ["merged", "deleted"]
    default: merged
  config:
    description: A dictionary containing the details for application queuing profile.
    type: list
    elements: dict
    required: true
    suboptions:
      application_queuing_details:
        description: Manages the details for application queuing profile.
        type: list
        elements: dict
        suboptions:
          profile_name:
            description:
              - This represents a name for the queuing profile.
              - Required for queuing profile create, update and delete operations.
            type: str
          new_profile_name:
            description:
              - This represents to update new name for the queuing profile.
            type: str
          profile_description:
            description: The description for queuing profile.
            type: str
          bandwidth_settings:
            description: The "bandwidth_settings" will include specific details related to bandwidth allocation
            type: dict
            suboptions:
              is_common_between_all_interface_speeds:
                description:
                  - The field indicates that the bandwidth allocation settings defined in the configuration are
                    uniform across all interface speeds or not.
                type: bool
              interface_speed_bandwidth_clauses:
                description:
                  - Define the specific bandwidth allocation for different types of network traffic based on the interface speed.
                  - This clause allows you to specify how bandwidth should be distributed across various traffic categories
                type: list
                elements: dict
                suboptions:
                  interface_speed:
                    description: |
                      - The "interface_speed" refers to the specific data transfer rate (or bandwidth capacity) of a network interface.
                      - It defines how much data the interface can handle within a given period, typically measured in bits per second (bps)
                      - Permissible values:
                        - "ALL": Refers to the total bandwidth applicable across all interface speeds, without specifying a particular speed.
                        - "HUNDRED_GBPS": Represents a bandwidth of 100 gigabits per second (Gbps).
                        - "TEN_GBPS": Represents a bandwidth of 10 gigabits per second (Gbps).
                        - "ONE_GBPS": Represents a bandwidth of 1 gigabit per second (Gbps).
                        - "HUNDRED_MBPS": Represents a bandwidth of 100 megabits per second (Mbps).
                        - "TEN_MBPS": Represents a bandwidth of 10 megabits per second (Mbps).
                        - "ONE_MBPS": Represents a bandwidth of 1 megabit per second (Mbps).
                    type: str
                  bandwidth_percentages:
                    description:
                      - The field specifies the percentage of total available bandwidth that should be allocated to different types of network traffic.
                      - This allocation is used to prioritize specific traffic categories based on their importance or application requirements.
                    type: dict
                    suboptions:
                      transactional_data:
                        description: Refers to a category of network traffic that involves data transactions between systems.
                        type: str
                      best_effort:
                        description:
                          - Refers to a type of network traffic that does not require specific guarantees for quality or priority.
                          - It is typically used for non-critical or general-purpose data transmission.
                        type: str
                      voip_telephony:
                        description:
                          - Refers to network traffic for the voice and video calls transmitted over the internet rather
                            than traditional telephone lines.
                        type: str
                      multimedia_streaming:
                        description: Refers to network traffic for the transmission of audio and video content over the internet in real time.
                        type: str
                      real_time_interactive:
                        description: Refers to network traffic generated by applications that require low latency and immediate responsiveness.
                        type: str
                      multimedia_conferencing:
                        description: Refers to network traffic that involve both audio and video communication.
                        type: str
                      signaling:
                        description: Refers to network traffic that control messages and protocols used to manage communication sessions in a network.
                        type: str
                      scavenger:
                        description:
                          - Refers to low-priority network traffic that can be delayed or dropped in times of congestion
                            without significant impact on application performance.
                        type: str
                      ops_admin_mgmt:
                        description: Refers to network traffic associated with operations and administration management.
                        type: str
                      broadcast_video:
                        description:
                          - Refers to video content that is broadcasted or streamed to a large audience,
                            typically in a one-to-many distribution model.
                        type: str
                      network_control:
                        description: Refers to traffic related to the management and operation of the network itself.
                        type: str
                      bulk_data:
                        description: Refers to large-volume data transfers that are typically non-time-sensitive and can tolerate delays or interruptions.
                        type: str
          dscp_settings:
            description: The 'dscp_settings' will include specific details related to dscp allocation.
            type: list
            elements: dict
            suboptions:
              transactional_data:
                description: Refers to a category of network traffic that involves data transactions between systems.
                type: str
              best_effort:
                description:
                  - Refers to a type of network traffic that does not require specific guarantees for quality or priority.
                  - It is typically used for non-critical or general-purpose data transmission.
                type: str
              voip_telephony:
                description:
                  - Refers to network traffic for the voice and video calls transmitted over the internet or private networks
                    rather than traditional telephone lines.
                type: str
              multimedia_streaming:
                description: Refers to network traffic for the transmission of audio and video content over the internet in real time.
                type: str
              real_time_interactive:
                description: Refers to network traffic generated by applications that require low latency and immediate responsiveness.
                type: str
              multimedia_conferencing:
                description: Refers to network traffic that involve both audio and video communication.
                type: str
              signaling:
                description:
                  - Refers to network traffic that control messages and protocols used to establish, manage,
                    and terminate communication sessions in a network.
                type: str
              scavenger:
                description:
                  - Refers to low-priority network traffic that can be delayed or dropped in times of congestion
                    without significant impact on application performance.
                type: str
              ops_admin_mgmt:
                description: Refers to network traffic associated with operations and administration management.
                type: str
              broadcast_video:
                description: Refers to video content that is broadcasted or streamed to a large audience, typically in a one-to-many distribution model.
                type: str
              network_control:
                description: Refers to traffic related to the management and operation of the network itself.
                type: str
              bulk_data:
                description: Refers to large-volume data transfers that are typically non-time-sensitive and can tolerate delays or interruptions.
                type: str
      application_set_details:
        description:
          - An Application Set is a logical grouping of network applications that share common policies and configuration settings.
          - Application sets allow network administrators to manage and apply policies to multiple applications simultaneously,
            streamlining the process of policy enforcement, monitoring, and optimization.
        type: list
        elements: dict
        suboptions:
          name:
            description:
              - This field represents name for the application set.
              - Required for application set delete operations.
            type: str
      application_details:
        description:
          - Each application inside an Application Set share a common purpose or function.
          - Group of similar applications inside an application set are classified in a way that allows network administrators to
            apply uniform policies to the entire set.
        type: list
        elements: dict
        suboptions:
          name:
            description:
              - This field represent a name for the application.
              - Required for application create, update and delete operations.
            type: str
          description:
            description:
              - This field represent a short description for the application.
            type: str
          helpString:
            description:
              - This field helps the purpose for what the application is created.
            type: str
          type:
            description: |
              - The type field in a Network Application refers to the way the application is identified or categorized within the network.
              - Permissible values:
              - _servername: Specifies a custom application is based on the server name for identifying the application.
              - _url: Specifies a custom application is based on a URL for identifying the application.
              - _server-ip: Specifies a custom application is based on the server IP address for identifying the application.
            type: str
          server_name:
            description:
              - If the type mentioned is servername then a name for the server has to be mentioned.
            type: str
          dscp:
            description:
              - If the type mentioned is serverip then a value for dscp or network_identity details has to be mentioned to create an application.
              - The value for dscp should range between 0 - 63.
            type: str
          network_identity:
            description:
              - If the type mentioned is server-ip then a value for dscp or network_identity details has to be mentioned to create an application.
            type: list
            elements: dict
            suboptions:
              protocol:
                description:
                  - This field represent The network protocol used by the application.
                type: str
              port:
                description:
                  - This field represent the port number for the application to communicate on.
                type: str
              ip_subnet:
                description:
                  - This field represent list of IP addresses or subnets associated with the application.
                type: list
                elements: str
              lower_port:
                description:
                  - This field represent the lower range of ports for network communication.
                type: str
              upper_port:
                description:
                  - This field represent the upper range of ports for network communication.
                type: str
          app_protocol:
            description: |
              - If the type mentioned is url or serverip then the protocol used by the application has to be mentioned to create an application.
              - If the type is url then the app_protocol should be tcp.
              - Permissible values:
                - 'TCP': Specifies the Transmission Control Protocol, used for reliable, connection-oriented communication.
                - 'UDP': Specifies the User Datagram Protocol, used for connectionless, faster communication without guaranteed delivery.
                - 'TCP/UDP': Indicates both TCP and UDP protocols are used, allowing flexibility in communication.
                - 'IP': Refers to the Internet Protocol, used for addressing and routing packets in a network.
            type: str
          url:
            description:
              - If the type mentioned is url then url has to be mentioned to create an application.
            type: str
          traffic_class:
            description: |
              - Traffic classes help enforce network policies by determining how to prioritize different types of data, ensuring that critical
                applications receive the necessary bandwidth while less critical traffic can be deprioritized or handled with lower resources.
              - Permissible values:
                - "BROADCAST_VIDEO": Video traffic broadcasted to multiple recipients.
                - "BULK_DATA": Large data transfers like file uploads or backups.
                - "MULTIMEDIA_CONFERENCING": Audio and video traffic for conferencing.
                - "MULTIMEDIA_STREAMING": Streaming video or audio content.
                - "NETWORK_CONTROL": Traffic for managing and controlling network infrastructure.
                - "OPS_ADMIN_MGMT": Traffic for network operational and administrative tasks.
                - "REAL_TIME_INTERACTIVE": Low-latency traffic for real-time interactive applications.
                - "SIGNALING": Control traffic for setting up and managing sessions (e.g., VoIP).
                - "TRANSACTIONAL_DATA": Data related to transactions, like financial or retail operations.
                - "VOIP_TELEPHONY": Voice traffic over IP networks.
                - "BEST_EFFORT": Non-critical traffic delivered on a best-effort basis.
                - "SCAVENGER": Low-priority traffic, often background tasks.
            type: str
          ignore_conflict:
            description:
              - Flag indicating whether conflicts should be ignored.
            type: str
          rank:
            description:
              - The rank or priority of the application.
            type: str
          engine_id:
            description:
              - Identifier for the engine that manages the application.
            type: str
          application_set_name:
            description: This represents under which appliction set we are going to create the application
            type: str
      application_policy_details:
        description: Define how an application's traffic is managed and prioritized within a network.
        type: list
        elements: dict
        suboptions:
          name:
            description:
              - This field represent a name for the application policy.
            type: str
          application_set_name:
            description:
              - This represents the application sets to be removed from the application policy.
              - Only the sets mentioned here will be removed.
              - This parameter will be applicable only in the deleted state.
            type: str
          policy_details:
            description: |
              - Indicates the current status of the application policy. It helps track whether the policy is active, deleted, or restored.
              - Permissible values:
                - "NONE": The policy is active and in its original, operational state.
                - "DELETED": The policy has been removed and is no longer active.
                - "RESTORED": The policy has been reactivated after being deleted.
            type: str
          site_name:
            description:
              -  It typically represents the specific site or area within the network where the policy should be enforced.
            type: str
          device_type:
            description:
              -  It typically represents whether the device is wired or wireless.
            type: list
            elements: dict
            suboptions:
              device_ip:
                description:
                  - If device type is wireless, specify the device ip.
                  - Indicates is the IP address assigned to the device, used for network communication.
                type: str
              wlan_id:
                description:
                  - If device type is wireless, specify the wlan id.
                  - The wlan ID associated with the device, used to segment network traffic.
                type: str
          application_queuing_profile_name:
            description:
              - The application_queuing_profile_name determines how the application policy prioritizes network traffic by defining
                rules for traffic management
            type: str
          clause:
            description:
              - The clause is used to define specific rules or conditions under which an application set is added to the application policy
            type: list
            elements: dict
            suboptions:
              clause_type:
                description: |
                  - Specifies the type of clause for the application policy.
                  - Permissible values:
                    - "BUSINESS_RELEVANCE": Defines the importance of the application to business operations, affecting its priority and
                    handling in the network policy.
                    - "APPLICATION_POLICY_KNOBS": Refers to configurable settings that manage the application's network behavior,
                    such as traffic prioritization and resource allocation.
                type: str
              relevance_details:
                description: |
                  - Indicates details about how relevant the application is to business operations.
                type: list
                elements: dict
                suboptions:
                  relevance:
                    description: |
                      - Indicates whether the set is relevant, irrelevant or default to the application policy
                      - Permissible values:
                        - "BUSINESS_RELEVANT": The application is critical for business functions.
                        - "BUSINESS_IRRELEVANT": The application is not essential for business operations.
                        - "DEFAULT": A default setting when no specific relevance is assigned.
                    type: str
                  application_set_name:
                    description: |
                      - Include all the application sets for which the application policy has to be created
                    type: str
requirements:
- dnacentersdk >= 2.9.3
- python >= 3.9.19
notes:
- SDK Methods used are
  - application_policy.ApplicationPolicy.get_application_policy
  - application_policy.ApplicationPolicy.application_policy_intent
  - application_policy.ApplicationPolicy.get_application_policy_queuing_profile
  - application_policy.ApplicationPolicy.update_application_policy_queuing_profile
  - application_policy.ApplicationPolicy.create_application_policy_queuing_profile
  - application_policy.ApplicationPolicy.delete_application_policy_queuing_profile
  - application_policy.ApplicationPolicy.get_application_sets
  - application_policy.ApplicationPolicy.create_application_set
  - application_policy.ApplicationPolicy.delete_application_set
  - application_policy.ApplicationPolicy.get_applications
  - application_policy.ApplicationPolicy.create_application
  - application_policy.ApplicationPolicy.update_application
  - application_policy.ApplicationPolicy.delete_application

- Paths used are
  - GET/dna/intent/api/v1/app-policy
  - POST/dna/intent/api/v1/app-policy-intent
  - GET/dna/intent/api/v1/app-policy-queuing-profile
  - POST/dna/intent/api/v1/app-policy-queuing-profile
  - PUT/dna/intent/api/v1/app-policy-queuing-profile
  - DELETE/dna/intent/api/v1/app-policy-queuing-profile/{id}
  - GET/dna/intent/api/v1/application-policy-application-set
  - POST//dna/intent/api/v1/application-policy-application-set
  - DELETE/dna/intent/api/v2/application-policy-application-set/{id}
  - GET/dna/intent/api/v2/applications
  - POST/dna/intent/api/v2/applications
  - PUT/dna/intent/api/v1/applications
  - DELETE/dna/intent/api/v2/applications/{id}
"""

EXAMPLES = r"""
---
#Playbook 1 - application queuing profile - type both ("bandwidth", "dscp")

- name: Application Queuing Profile Creation in Cisco Catalyst Center
  hosts: localhost
  connection: local
  gather_facts: no
  vars_files:
    - "credentials.yml"

  tasks:
    - name: Create a application Queuing Profile in Cisco Catalyst Center
      cisco.dnac.application_policy_workflow_manager:
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
          - application_queuing_details:
              - profile_name: "Asampleq9"
                profile_description: "sample 12234567876543q"
                bandwidth_settings:
                  is_common_between_all_interface_speeds: true
                  interface_speed: "ALL"
                  bandwidth_percentages:
                    transactional_data: "5"
                    best_effort: "10"
                    voip_telephony: "15"
                    multimedia_streaming: "10"
                    real_time_interactive: "20"
                    multimedia_conferencing: "10"
                    signaling: "10"
                    scavenger: "5"
                    ops_admin_mgmt: "5"
                    broadcast_video: "2"
                    network_control: "3"
                    bulk_data: "5"
                dscp_settings:
                  multimedia_conferencing: "20"
                  ops_admin_mgmt: "23"
                  transactional_data: "28"
                  voip_telephony: "45"
                  multimedia_streaming: "27"
                  broadcast_video: "46"
                  network_control: "48"
                  best_effort: "0"
                  signaling: "4"
                  bulk_data: "10"
                  scavenger: "2"
                  real_time_interactive: "34"

#Playbook type 2 - for is_common_between_all_interface_speeds: true

- name: Application Queueing Profile Creation in Cisco Catalyst Center
  hosts: localhost
  connection: local
  gather_facts: no
  vars_files:
    - "credentials.yml"

  tasks:
    - name: Create a application Queueing Profile in Cisco Catalyst Center
      cisco.dnac.application_policy_workflow_manager:
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
          - application_queuing_details:
            - profile_name: "sample4"
              profile_description: "sample1"
              bandwidth_settings:
                is_common_between_all_interface_speeds: true
                interface_speed: "ALL"
                bandwidth_percentages:
                  transactional_data: "5"
                  best_effort: "10"
                  voip_telephony: "15"
                  multimedia_streaming: "10"
                  real_time_interactive: "20"
                  multimedia_conferencing: "10"
                  signaling: "10"
                  scavenger: "5"
                  ops_admin_mgmt: "5"
                  broadcast_video: "2"
                  network_control: "3"
                  bulk_data: "5"

# Playbook-3 for different interface speeds

- name: Application Queueing Profile Creation in Cisco Catalyst Center
  hosts: localhost
  connection: local
  gather_facts: no
  vars_files:
    - "credentials.yml"

  tasks:
    - name: Create a application Queueing Profile in Cisco Catalyst Center
      cisco.dnac.application_policy_workflow_manager:
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
          - application_queuing_details:
            - profile_name: "newprofile20"
              profile_description: "sample desc"
              bandwidth_settings:
                is_common_between_all_interface_speeds: false
                interface_speed_settings:
                  - interface_speed: "HUNDRED_GBPS"
                    bandwidth_percentages:
                      transactional_data: "5"
                      best_effort: "10"
                      voip_telephony: "20"
                      multimedia_streaming: "5"
                      real_time_interactive: "20"
                      multimedia_conferencing: "10"
                      signaling: "10"
                      scavenger: "5"
                      ops_admin_mgmt: "5"
                      broadcast_video: "2"
                      network_control: "3"
                      bulk_data: "5"
                  - interface_speed: "TEN_GBPS"
                    bandwidth_percentages:
                      transactional_data: "5"
                      best_effort: "5"
                      voip_telephony: "25"
                      multimedia_streaming: "5"
                      real_time_interactive: "20"
                      multimedia_conferencing: "5"
                      signaling: "6"
                      scavenger: "5"
                      ops_admin_mgmt: "5"
                      broadcast_video: "2"
                      network_control: "3"
                      bulk_data: "15"
                  - interface_speed: "ONE_GBPS"
                    bandwidth_percentages:
                      transactional_data: "5"
                      best_effort: "10"
                      voip_telephony: "15"
                      multimedia_streaming: "10"
                      real_time_interactive: "20"
                      multimedia_conferencing: "10"
                      signaling: "10"
                      scavenger: "5"
                      ops_admin_mgmt: "5"
                      broadcast_video: "2"
                      network_control: "3"
                      bulk_data: "5"
                  - interface_speed: "HUNDRED_MBPS"
                    bandwidth_percentages:
                      transactional_data: "5"
                      best_effort: "10"
                      voip_telephony: "5"
                      multimedia_streaming: "15"
                      real_time_interactive: "25"
                      multimedia_conferencing: "10"
                      signaling: "10"
                      scavenger: "5"
                      ops_admin_mgmt: "5"
                      broadcast_video: "2"
                      network_control: "3"
                      bulk_data: "5"
                  - interface_speed: "TEN_MBPS"
                    bandwidth_percentages:
                      transactional_data: "5"
                      best_effort: "10"
                      voip_telephony: "15"
                      multimedia_streaming: "10"
                      real_time_interactive: "20"
                      multimedia_conferencing: "10"
                      signaling: "10"
                      scavenger: "5"
                      ops_admin_mgmt: "5"
                      broadcast_video: "2"
                      network_control: "3"
                      bulk_data: "5"
                  - interface_speed: "ONE_MBPS"
                    bandwidth_percentages:
                      transactional_data: "5"
                      best_effort: "5"
                      voip_telephony: "25"
                      multimedia_streaming: "10"
                      real_time_interactive: "20"
                      multimedia_conferencing: "5"
                      signaling: "10"
                      scavenger: "5"
                      ops_admin_mgmt: "5"
                      broadcast_video: "2"
                      network_control: "3"
                      bulk_data: "5"

# Playbook-4 for some interface speeds having common bandwidth percentage

- name: Application Queueing Profile Creation in Cisco Catalyst Center
  hosts: localhost
  connection: local
  gather_facts: no
  vars_files:
    - "credentials.yml"

  tasks:
    - name: Create a application Queueing Profile in Cisco Catalyst Center
      cisco.dnac.application_policy_workflow_manager:
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
          - application_queuing_details:
            - profile_name: "newprofile21"
              profile_description: "sample desc"
              bandwidth_settings:
                is_common_between_all_interface_speeds: false
                interface_speed_settings:
                  - interface_speed: "HUNDRED_GBPS"
                    bandwidth_percentages:
                      transactional_data: "5"
                      best_effort: "10"
                      voip_telephony: "20"
                      multimedia_streaming: "5"
                      real_time_interactive: "20"
                      multimedia_conferencing: "10"
                      signaling: "10"
                      scavenger: "5"
                      ops_admin_mgmt: "5"
                      broadcast_video: "2"
                      network_control: "3"
                      bulk_data: "5"
                  - interface_speed: "TEN_GBPS"
                    bandwidth_percentages:
                      transactional_data: "5"
                      best_effort: "5"
                      voip_telephony: "25"
                      multimedia_streaming: "5"
                      real_time_interactive: "20"
                      multimedia_conferencing: "5"
                      signaling: "6"
                      scavenger: "5"
                      ops_admin_mgmt: "4"
                      broadcast_video: "2"
                      network_control: "3"
                      bulk_data: "15"
                  - interface_speed: "HUNDRED_MBPS"
                    bandwidth_percentages:
                      transactional_data: "5"
                      best_effort: "10"
                      voip_telephony: "5"
                      multimedia_streaming: "15"
                      real_time_interactive: "25"
                      multimedia_conferencing: "10"
                      signaling: "10"
                      scavenger: "5"
                      ops_admin_mgmt: "5"
                      broadcast_video: "2"
                      network_control: "3"
                      bulk_data: "5"
                  - interface_speed: TEN_MBPS, ONE_MBPS, ONE_GBPS
                    bandwidth_percentages:
                      transactional_data: "5"
                      best_effort: "10"
                      voip_telephony: "15"
                      multimedia_streaming: "10"
                      real_time_interactive: "20"
                      multimedia_conferencing: "10"
                      signaling: "10"
                      scavenger: "5"
                      ops_admin_mgmt: "5"
                      broadcast_video: "2"
                      network_control: "3"
                      bulk_data: "5"

# Playbook 5 - application queuing profile - type dscp

- name: Application Queuing Profile Creation in Cisco Catalyst Center
  hosts: localhost
  connection: local
  gather_facts: no
  vars_files:
    - "credentials.yml"
  tasks:
    - name: Create a application Queuing Profile in Cisco Catalyst Center
      cisco.dnac.application_policy_workflow_manager:
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
          - application_queuing_details:
              - profile_name: "Asampleq9"
                profile_description: "sample 12234567876543q"
                dscp_settings:
                  multimedia_conferencing: "20"
                  ops_admin_mgmt: "23"
                  transactional_data: "28"
                  voip_telephony: "45"
                  multimedia_streaming: "27"
                  broadcast_video: "46"
                  network_control: "48"
                  best_effort: "0"
                  signaling: "4"
                  bulk_data: "10"
                  scavenger: "2"
                  real_time_interactive: "34"

# Playbook 6 – update application queuing profile

- name: Application Queuing Profile update in Cisco Catalyst Center
  hosts: localhost
  connection: local
  gather_facts: no
  vars_files:
    - "credentials.yml"

  tasks:
    - name: update application Queuing Profile in Cisco Catalyst Center
      cisco.dnac.application_policy_workflow_manager:
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
          - application_queuing_details:
              - profile_name: "Asampleq9"
                new_profile_name: "Asampleq99"
                profile_description: "sample 12234567876543q"
                new_profile_description: "sample"
                bandwidth_settings:
                  is_common_between_all_interface_speeds: true
                  interface_speed: "ALL"
                  bandwidth_percentages:
                    transactional_data: "5"
                    best_effort: "10"
                    voip_telephony: "15"
                    multimedia_streaming: "10"
                    real_time_interactive: "20"
                    multimedia_conferencing: "10"
                    signaling: "10"
                    scavenger: "5"
                    ops_admin_mgmt: "5"
                    broadcast_video: "2"
                    network_control: "3"
                    bulk_data: "5"
                dscp_settings:
                  multimedia_conferencing: "20"
                  ops_admin_mgmt: "23"
                  transactional_data: "28"
                  voip_telephony: "45"
                  multimedia_streaming: "27"
                  broadcast_video: "46"
                  network_control: "48"
                  best_effort: "0"
                  signaling: "4"
                  bulk_data: "10"
                  scavenger: "2"
                  real_time_interactive: "34"

# Playbook 7 - delete application queuing profile

- name: Delete application queuing profile from Cisco Catalyst Center
  hosts: localhost
  connection: local
  vars_files:
    - "credentials.yml"

  tasks:
    - name: Delete application queuing profile from Cisco Catalyst Center
      cisco.dnac.application_policy_workflow_manager:
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
        config:
          - application_queuing_details:
            - profile_name: "sample_queuing_profile"

# Playbook 8 - delete application set

- name: Application Set deletion from Cisco Catalyst Center
  hosts: localhost
  connection: local
  vars_files:
    - "credentials.yml"

  tasks:
    - name: Delete application set from Cisco Catalyst Center
      cisco.dnac.application_policy_workflow_manager:
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
        config:
          - application_set_details:
            - name: "sample_application_set"

# Playbook 9 - create application - type server_name

- name: Create application on Cisco Catalyst Center
  hosts: localhost
  connection: local
  vars_files:
    - "credentials.yml"

  tasks:
    - name: Create application on Cisco Catalyst Center
      cisco.dnac.application_policy_workflow_manager:
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
        config:
          - application_details:
              name: "sample"
              description: "sample"
              helpstring: "sample"
              type: "server_name"
              server_name: "www.sampleserverapp.com"
              traffic_class: "BROADCAST_VIDEO"
              ignore_conflict: true
              rank: "1"
              engine_id: "100"
              application_set_name: "authentication_services"

# Playbook 10 - create application - type server_ip

- name: Create application on Cisco Catalyst Center
  hosts: localhost
  connection: local
  vars_files:
    - "credentials.yml"

  tasks:
    - name: Create application on Cisco Catalyst Center
      cisco.dnac.application_policy_workflow_manager:
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
        config:
          - application_details:
              - name: "app30"
                helpstring: "sample"
                description: "sample"
                type: "server_ip"
                app_protocol: "UDP"
                network_identity_setting:
                  protocol: "UDP"
                  port: "2000"
                  ip_subnet: ["1.1.1.1","2.2.2.2","3.3.3.3"]
                  lower_port: "10"
                  upper_port: "100"
                dscp: "2"
                traffic_class: "BROADCAST_VIDEO"
                ignore_conflict: true
                rank: "23"
                engine_id: "4"
                application_set_name: "sampleapplset"

# Playbook 11 - create application - type url

- name: Create application on Cisco Catalyst Center
  hosts: localhost
  connection: local
  vars_files:
    - "credentials.yml"

  tasks:
    - name: Create application on Cisco Catalyst Center
      cisco.dnac.application_policy_workflow_manager:
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
        config:
          - application_details:
            - name: "app8"
              helpstring: "sample"
              description: "sample"
              type: "url"
              app_protocol: "TCP"
              url: "www.sample.com"
              traffic_class: "BROADCAST_VIDEO"
              ignore_conflict: true
              rank: "23"
              engine_id: "4"
              application_set_name: "sampleapplset"

# Playbook 12 - delete application

- name: Delete application from Cisco Catalyst Center
  hosts: localhost
  connection: local
  vars_files:
    - "credentials.yml"

  tasks:
    - name: Delete application from Cisco Catalyst Center
      cisco.dnac.sample_workflow_manager:
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
        config:
          - application_details:
              - name: "sample_application"

# Playbook 13 - create application policy - wireless

- name: Application Policy Creation in Cisco Catalyst Center
  hosts: localhost
  connection: local
  gather_facts: no
  vars_files:
    - "credentials.yml"

  tasks:
    - name: Create a application Policy in Cisco Catalyst Center
      cisco.dnac.application_policy_workflow_manager:
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
          - application_policy_details:
              name: "sample_application_policy"
              policy_status: "deployed"
              site_name: "global/Chennai/FLOOR1"
              device_type: "wireless"
              device:
                - device_ip: "204.1.2.3"
                  wlan_id: "18"
              application_queuing_profile_name: "sample_queuing_profile"
              clause:
                - clause_type: "BUSINESS_RELEVANCE"
                  relevance_details:
                    - relevance: "BUSINESS_RELEVANT"
                      application_set_name: ["sample_application_set", "sample_application_set"]
                    - relevance: "BUSINESS_IRRELEVANT"
                      application_set_name: ["sample_application_set", "sample_application_set"]
                    - relevance: "DEFAULT"
                      application_set_name: ["sample_application_set", "sample_application_set"]

# Playbook 14 - create application policy - wired

- name: Application Policy Creation in Cisco Catalyst Center
  hosts: localhost
  connection: local
  gather_facts: no
  vars_files:
    - "credentials.yml"

  tasks:
    - name: Create a application Policy in Cisco Catalyst Center
      cisco.dnac.application_policy_workflow_manager:
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
            - application_policy_details:
                name: "sample_application_policy"
                policy_status: "deployed"
                site_name: "global/Chennai/FLOOR1"
                device_type: "wireless"
                application_queuing_profile_name: "sample_queuing_profile"
                clause:
                - clause_type: "BUSINESS_RELEVANCE"
                  relevance_details:
                    - relevance: "BUSINESS_RELEVANT"
                      application_set_name: ["sample_application_set", "sample_application_set"]
                    - relevance: "BUSINESS_IRRELEVANT"
                      application_set_name: ["sample_application_set", "sample_application_set"]
                    - relevance: "DEFAULT"
                      application_set_name: ["sample_application_set", "sample_application_set"]

#  Playbook 15 - delete application policy

- name: Application Policy Deletion from Cisco Catalyst Center
  hosts: localhost
  connection: local
  vars_files:
    - "credentials.yml"

  tasks:
  - name: Delete application policy from Cisco Catalyst Center
    cisco.dnac.application_policy_workflow_manager:
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
      state: deleted
      config:
        - application_policy_details:
          - name: "sample_application_policy"

"""

RETURN = r"""

# Case 1: Successful creation of application queuing profile

creation_of_application_queuing_profile_response_task_tracking:
  description: A dictionary containing task tracking details such as task ID and URL from the Cisco Catalyst Center.
  returned: always
  type: dict
  sample:
    {
      "response": {
          "taskId": "str",
          "url": "str"
      },
      "version": "str"
    }

creation _of_application_queuing_profile_response_task_execution:
  description: A dictionary with additional details for successful task execution, including progress and data.
  returned: always
  type: dict
  sample:
    {
      "response": {
          "data": "str",
          "progress": "str"
      },
      "version": "str"
    }


# Case 2: Successful updation of application queuing profile

updation_of_application_queuing_profile_response_task_tracking:
  description: A dictionary with details of the API execution from Cisco Catalyst Center.
  returned: always
  type: dict
  sample:
    {
      "response": {
          "taskId": "str",
          "url": "str"
      },
      "version": "str"
    }

updation_of_application_queuing_profile_response_task_execution:
  description: With task id get details for successfull updation
  returned: always
  type: dict
  sample:
    {
      "response": {
          "data": "str",
          "progress": "str",
      },
      "version": "str"
    }

# Case 3: Successful deletion of application queuing profile

deletion_of_application_queuing_profile_response_task_tracking:
  description: A dictionary with details of the API execution from Cisco Catalyst Center.
  returned: always
  type: dict
  sample:
    {
      "response": {
          "taskId": "str",
          "url": "str"
      },
      "version": "str"
    }
deletion_of_application_queuing_profile_response_task_execution:
  description: With task id get details for successfull deletion
  returned: always
  type: dict
  sample:
    {
      "response": {
          "data": "str",
          "progress": "str",
      },
      "version": "str"
    }

# Case 4: Error during application queuing profile (create/update/delete)

error_during_application_queuing_profile_response_task_tracking:
  description: A dictionary with details of the API execution and error information.
  returned: always
  type: dict
  sample:
    {
      "response": {
          "taskId": "str",
          "url": "str"
      },
      "version": "str"
    }
error_during_application_queuing_profile_response_task_execution:
  description: With task id get details for error during application queuing profile (create/update/delete)
  returned: always
  type: dict
  sample:
    {
      "response": {
          "data": "str",
          "progress": "str",
          "errorCode": "str",
          "failureReason": "str"
      },
      "version": "str"
    }

# Case 5: Application queuing profile not found (during delete operation)

application_queuing_profile_not_found_response_task_tracking:
  description: A dictionary with details of the API execution and error information.
  returned: always
  type: dict
  sample:
    {
      "response": {
          "taskId": "str",
          "url": "str"
      },
      "version": "str"
    }
application_queuing_profile_not_found_response_task_execution:
  description: With task id get details for error message
  returned: always
  type: dict
  sample:
    {
      "response": {
          "data": "str",
          "progress": "str",
          "errorCode": "str",
          "failureReason": "str"
      },
      "version": "str"
    }


# Case 6: Successful creation of application set

successful_creation_of_application_set_response_task_tracking:
  description: A dictionary with details of the API execution from Cisco Catalyst Center.
  returned: always
  type: dict
  sample:
    {
      "response": {
          "taskId": "str",
          "url": "str"
      },
      "version": "str"
    }
successful_creation_of_application_set_response_task_execution:
  description: With task id get details for successfull creation
  returned: always
  type: dict
  sample:
    {
      "response": {
          "data": "str",
          "progress": "str",
      },
      "version": "str"
    }

# Case 7: Successful deletion of application set

successful_deletion_of_application set_response_task_tracking:
  description: A dictionary with details of the API execution from Cisco Catalyst Center.
  returned: always
  type: dict
  sample:
    {
      "response": {
          "taskId": "str",
          "url": "str"
      },
      "version": "str"
    }
successful_deletion_of_application_set_response_task_execution:
  description: With task id get details for successfull deletion
  returned: always
  type: dict
  sample:
    {
      "response": {
          "data": "str",
          "progress": "str",
      },
      "version": "str"
    }

# Case 8: Error during application set operation (create/delete)

error_during_application_set_operation_response_task_tracking:
  description: A dictionary with details of the API execution and error information.
  returned: always
  type: dict
  sample:
    {
      "response": {
          "taskId": "str",
          "url": "str"
      },
      "version": "str"
    }
error_during_application_set_operation_response_task_execution:
  description: With task id get details for error during application set (create/delete)
  returned: always
  type: dict
  sample:
    {
      "response": {
          "data": "str",
          "progress": "str",
          "errorCode": "str",
          "failureReason": "str"
      },
      "version": "str"
    }

# Case 9: Application set not found (during delete operation)

application_set_not_found_response_task_tracking:
  description: A dictionary with details of the API execution and error information.
  returned: always
  type: dict
  sample:
    {
      "response": {
          "taskId": "str",
          "url": "str"
      },
      "version": "str"
    }
application_set_not_found_response_task_execution:
  description: With task id get details for error message
  returned: always
  type: dict
  sample:
    {
      "response": {
          "data": "str",
          "progress": "str",
          "errorCode": "str",
          "failureReason": "str"
      },
      "version": "str"
    }

# Case 10: Successful creation of application

successful_creation_of_application_response_task_tracking:
  description: A dictionary with details of the API execution from Cisco Catalyst Center.
  returned: always
  type: dict
  sample:
    {
      "response": {
          "taskId": "str",
          "url": "str"
      },
      "version": "str"
    }
successful_creation_of_application_response_task_execution:
  description: With task id get details for successfull creation
  returned: always
  type: dict
  sample:
    {
      "response": {
          "data": "str",
          "progress": "str",
      },
      "version": "str"
    }

# Case 11: Successful updation of application

successful updation_of_application_response_task_tracking:
  description: A dictionary with details of the API execution from Cisco Catalyst Center.
  returned: always
  type: dict
  sample:
    {
      "response": {
          "taskId": "str",
          "url": "str"
      },
      "version": "str"
    }
successful_updation_of_application_response_task_execution:
  description: With task id get details for successfull updation
  returned: always
  type: dict
  sample:
    {
      "response": {
          "data": "str",
          "progress": "str",
      },
      "version": "str"
    }

# Case 12: Successful deletion of application

deletion_of_application_response_task_tracking:
  description: A dictionary with details of the API execution from Cisco Catalyst Center.
  returned: always
  type: dict
  sample:
    {
      "response": {
          "taskId": "str",
          "url": "str"
      },
      "version": "str"
    }

deletion_of_application_response_task_execution:
  description: With task id get details for successfull deletion
  returned: always
  type: dict
  sample:
    {
      "response": {
          "data": "str",
          "progress": "str",
      },
      "version": "str"
    }

# Case 13: Error during application operation (create/update/delete)

error_during_application_operation_response_task_tracking:
  description: A dictionary with details of the API execution and error information.
  returned: always
  type: dict
  sample:
    {
      "response": {
          "taskId": "str",
          "url": "str"
      },
      "version": "str"
    }
error_during_application_operation_response_task_execution:
  description: With task id get details for error during application (create/update/delete)
  returned: always
  type: dict
  sample:
    {
      "response": {
          "data": "str",
          "progress": "str",
          "errorCode": "str",
          "failureReason": "str"
      },
      "version": "str"
    }

# Case 14: Application not found (during delete operation)

application_not_found_response_task_tracking:
  description: A dictionary with details of the API execution and error information.
  returned: always
  type: dict
  sample:
    {
      "response": {
          "taskId": "str",
          "url": "str"
      },
      "version": "str"
    }
application_not_found_response_task_execution:
  description: With task id get details for error message
  returned: always
  type: dict
  sample:
    {
      "response": {
          "data": "str",
          "progress": "str",
          "errorCode": "str",
          "failureReason": "str"
      },
      "version": "str"
    }

# Case 15: Successful creation of application policy

successful_creation_of_application_policy_response_task_tracking:
  description: A dictionary with details of the API execution from Cisco Catalyst Center.
  returned: always
  type: dict
  sample:
    {
      "response": {
          "taskId": "str",
          "url": "str"
      },
      "version": "str"
    }
successful_creation_of_application_policy_response_task_execution:
  description: With task id get details for successfull creation
  returned: always
  type: dict
  sample:
    {
      "response": {
          "data": "str",
          "progress": "str",
      },
      "version": "str"
    }

#Case 16: Successful updation of application policy

successful_updation_of_application_policy_response_task_tracking:
  description: A dictionary with details of the API execution from Cisco Catalyst Center.
  returned: always
  type: dict
  sample:
    {
      "response": {
          "taskId": "str",
          "url": "str"
      },
      "version": "str"
    }
successful_updation_of_application_policy_response_task_execution:
  description: With task id get details for successfull updation
  returned: always
  type: dict
  sample:
    {
      "response": {
          "data": "str",
          "progress": "str",
      },
      "version": "str"
    }

# Case 17: Successful deletion of application policy

successful_deletion_of_application_policy_response_task_tracking:
  description: A dictionary with details of the API execution from Cisco Catalyst Center.
  returned: always
  type: dict
  sample:
    {
      "response": {
          "taskId": "str",
          "url": "str"
      },
      "version": "str"
    }
successful_deletion_of_application_policy_response_task_execution:
  description: With task id get details for successfull deletion
  returned: always
  type: dict
  sample:
    {
      "response": {
          "data": "str",
          "progress": "str",
      },
      "version": "str"
    }

# Case 18: Error during application policy operation(create/update/delete)

error_during_application_policy_operation_response_task_tracking:
  description: A dictionary with details of the API execution and error information.
  returned: always
  type: dict
  sample:
    {
      "response": {
          "taskId": "str",
          "url": "str"
      },
      "version": "str"
    }
error_during_application_policy_operation_response_task_execution:
  description: With task id get details for error during application policy(create/update/delete)
  returned: always
  type: dict
  sample:
    {
      "response": {
          "data": "str",
          "progress": "str",
          "errorCode": "str",
          "failureReason": "str"
      },
      "version": "str"
    }

# Case 19: Application policy not found (during delete operation)

application_policy_not_found_response_task_tracking:
  description: A dictionary with details of the API execution and error information.
  returned: always
  type: dict
  sample:
    {
      "response": {
          "taskId": "str",
          "url": "str"
      },
      "version": "str"
    }
application_policy_not_found_response_task_execution:
  description: With task id get details for error message
  returned: always
  type: dict
  sample:
    {
      "response": {
          "data": "str",
          "progress": "str",
          "errorCode": "str",
          "failureReason": "str"
      },
      "version": "str"
    }
"""

from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
)
from ansible.module_utils.basic import AnsibleModule
import json

# Defer this feature as API issue is there once it's fixed we will addresses it in upcoming release
support_for_application_set = False


class ApplicationPolicy(DnacBase):
    """Class containing member attributes for application_policy_workflow_manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged", "deleted"]

    def validate_input(self):
        """
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.
        Parameters:
        - self: The instance of the class containing the 'config' attribute to be validated.
        Returns:
        The method returns an instance of the class with updated attributes:
        - self.msg: A message describing the validation result.
        - self.status: The status of the validation (either 'success' or 'failed').
        - self.validated_config: If successful, a validated version of 'config' parameter.
        Example:
            To use this method, create an instance of the class and call 'validate_input' on it.
        If the validation succeeds, 'self.status' will be 'success' and 'self.validated_config'
        will contain the validated configuration. If it fails, 'self.status' will be 'failed',
        'self.msg' will describe the validation issues.
        """

        if not self.config:
            self.status = "success"
            self.msg = "Configuration is not available in the playbook for validation"
            self.log(self.msg, "ERROR")
            return self

        # Check if the config is a list, as expected
        if not isinstance(self.config, list):
            self.status = "failed"
            self.msg = "Config should be a list, found: {0}".format(type(self.config))
            self.log(self.msg, "ERROR")
            return self

        config_data = self.config[0] if self.config else {}

        # Ensure application_queuing_details is a list
        application_queuing_details = config_data.get('application_queuing_details', [])
        if not isinstance(application_queuing_details, list):
            self.status = "failed"
            self.msg = "'application_queuing_details' should be a list, found: {0}".format(type(application_queuing_details))
            self.log(self.msg, "ERROR")
            return self

        application_set_details = config_data.get('application_set_details', [])
        if not isinstance(application_set_details, list):
            self.status = "failed"
            self.msg = "'application_set_details' should be a list, found: {0}".format(type(application_set_details))
            self.log(self.msg, "ERROR")
            return self

        application_details = config_data.get('application_details', {})
        if not isinstance(application_details, dict):
            self.status = "failed"
            self.msg = "'application_details' should be a dict, found: {0}".format(type(application_details))
            self.log(self.msg, "ERROR")
            return self

        application_policy_details = config_data.get('application_policy_details', {})
        self.log(application_policy_details)
        if not isinstance(application_policy_details, dict):
            self.status = "failed"
            self.msg = "'application_policy_details' should be a dict, found: {0}".format(type(application_policy_details))
            self.log(self.msg, "ERROR")
            return self

        # Validate each item in the application_queuing_details list
        for item in application_queuing_details:
            if not isinstance(item, dict):
                self.status = "failed"
                self.msg = "Each item in 'application_queuing_details' should be a dictionary, found: {0}".format(type(item))
                self.log(self.msg, "ERROR")
                return self
        self.validated_config = self.config

        config_spec = {
            'application_details': {
                'type': 'dict',
                'elements': {
                    'name': {'type': 'str'},
                    'description': {'type': 'str'},
                    'helpstring': {'type': 'str'},
                    'type': {'type': 'str'},
                    'server_name': {'type': 'str'},
                    'traffic_class': {'type': 'str'},
                    'ignore_conflict': {'type': 'bool'},
                    'rank': {'type': 'str'},
                    'engine_id': {'type': 'str'},
                    'application_set_name': {'type': 'str'},
                },
            },
            'application_queuing_details': {
                'type': 'list',
                'elements': 'dict',
                'profile_name': {'type': 'str'},
                'new_profile_name': {'type': 'str'},
                'profile_description': {'type': 'str'},
                'bandwidth_settings': {
                    'type': 'dict',
                    'elements': 'dict',
                    'is_common_between_all_interface_speeds': {'type': 'bool'},
                    'interface_speed': {'type': 'str'},
                    'bandwidth_percentages': {
                        'type': 'dict',
                        'elements': 'dict',
                        'transactional_data': {'type': 'str'},
                        'best_effort': {'type': 'str'},
                        'voip_telephony': {'type': 'str'},
                        'multimedia_streaming': {'type': 'str'},
                        'real_time_interactive': {'type': 'str'},
                        'multimedia_conferencing': {'type': 'str'},
                        'signaling': {'type': 'str'},
                        'scavenger': {'type': 'str'},
                        'ops_admin_mgmt': {'type': 'str'},
                        'broadcast_video': {'type': 'str'},
                        'network_control': {'type': 'str'},
                        'bulk_data': {'type': 'str'},
                    },
                },
                'dscp_settings': {
                    'type': 'dict',
                    'elements': 'dict',
                    'multimedia_conferencing': {'type': 'str'},
                    'ops_admin_mgmt': {'type': 'str'},
                    'transactional_data': {'type': 'str'},
                    'voip_telephony': {'type': 'str'},
                    'multimedia_streaming': {'type': 'str'},
                    'broadcast_video': {'type': 'str'},
                    'network_control': {'type': 'str'},
                    'best_effort': {'type': 'str'},
                    'signaling': {'type': 'str'},
                    'bulk_data': {'type': 'str'},
                    'scavenger': {'type': 'str'},
                    'real_time_interactive': {'type': 'str'},
                },

            },
            'application_policy_details': {
                'type': 'dict',
                'element': 'dict',
                'name': {'type': 'str'},
                'policy_status': {'type': 'str'},
                'site_name': {'type': 'list', 'elements': 'str'},
                'device_type': {'type': 'str'},
                'device': {
                    'type': 'dict',
                    'element': 'dict',
                    'device_ip': {'type': 'str'},
                    'Wlan_id': {'type': 'str'},
                },
                'application_queuing_profile_name': {'type': 'str'},
                'clause': {
                    'type': 'list',
                    'element': 'dict',
                    'clause_type': {'type': 'str'},
                    'relevance_details': {
                        'type': 'list',
                        'element': 'dict',
                        'relevance': {'type': 'str'},
                        'application_set_name': {'type': 'list', 'elements': 'str'},
                    },
                },
            },
        }

        self.log(json.dumps(self.config, indent=4))

        # Validate the input configuration
        valid_config, invalid_params = validate_list_of_dicts(
            self.config, config_spec
        )

        if invalid_params:
            self.log(f"Invalid configuration parameters: {invalid_params}")
        else:
            self.log(f"Configuration validated successfully: {valid_config}")

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.log(self.msg, "ERROR")
            self.status = "failed"
            self.result['response'] = self.msg
            return self

        return self

    def get_want(self, config):
        """
        Retrieve and store import, tagging, distribution, and activation details from playbook configuration.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration dictionary containing image import and other details.
        Returns:
            self: The current instance of the class with updated 'want' attributes.
        Raises:
            AnsibleFailJson: If an incorrect import type is specified.
        Description:
            This function parses the playbook configuration to extract information related to image
            import, tagging, distribution, and activation. It stores these details in the 'want' dictionary
            for later use in the Ansible module.
        """

        want = {}
        want["application_queuing_details"] = config.get("application_queuing_details")
        want["application_set_details"] = config.get("application_set_details")
        want["application_details"] = config.get("application_details")
        want["application_policy_details"] = config.get("application_policy_details")

        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

        return self

    def get_queuing_profile_details(self, name):
        """
        Retrieves the details of an application queuing profile by its name.
        Description:
            This method queries the Cisco Catalyst Center API to check if a queuing profile with the specified name exists.
            It fetches the profile details if available. If the profile does not exist or an error occurs, the method logs
            the issue and returns default values indicating that the profile was not found.
        Parameters:
            name (str): The name of the queuing profile to retrieve.
        Returns:
            tuple: A tuple containing:
                - queuing_profile_exists (bool): Indicates whether the queuing profile exists.
                - current_queuing_profile (dict): A dictionary containing the details of the queuing profile, or an
                empty dictionary if the profile does not exist.
        Raises:
            Exception: Logs the error and updates the status if an API call fails or an unexpected issue occurs.
        """

        queuing_profile_exists = False
        current_queuing_profile = {}

        try:
            params = dict(name=name)
            response = self.dnac._exec(
                family="application_policy",
                function='get_application_policy_queuing_profile',
                params=params
            )
            self.log("Received API response from 'get_application_policy_queuing_profile': {0}".format(str(response)), "DEBUG")

            if not response:
                self.log("Unexpected response received:", "ERROR")
                raise Exception

            if not response.get("response"):
                self.log("empty response {0}".format(response))
                return queuing_profile_exists, current_queuing_profile

            current_queuing_profile = response.get("response")
            queuing_profile_exists = True
            self.log("got the details for queuing_profile_exists: {0} and current_queuing_profile: {1}".format(queuing_profile_exists, current_queuing_profile))
            return queuing_profile_exists, current_queuing_profile

        except Exception as e:
            self.status = "failed"
            self.msg = "error occured while getting queuing profile: {0}".format(e)
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

    def get_application_set_details(self, name):
        """
        Retrieves the details of an application set by its name.
        Description:
            This method queries the Cisco Catalyst Center API to determine if an application set with the specified
            name exists. It fetches the details of the application set if available. If the application set does not
            exist or an error occurs, the method logs the issue and either raises an exception or returns default values
            indicating that the application set was not found.
        Parameters:
            name (str): The name of the application set to retrieve.
        Returns:
            tuple: A tuple containing:
                - application_set_exists (bool): Indicates whether the application set exists.
                - current_application_set (dict): A dictionary containing the details of the application set, or an
                empty dictionary if the application set does not exist.
        Raises:
            Exception: If the API response is unexpected or indicates failure, an exception is raised, and the
            status is updated to "failed".
        """

        application_set_exists = False
        current_application_set = {}
        try:

            response = self.dnac._exec(
                family="application_policy",
                function='get_application_sets',
                params={"name": name}
            )
            self.log("Received API response from 'get_application_sets': {0}".format(str(response)), "DEBUG")

            if not response:
                self.log("Unexpected response received:", "ERROR")
                raise Exception

            if not response.get("response"):
                self.log("empty response {0}".format(response))
                return application_set_exists, current_application_set

            current_application_set = response.get("response")
            application_set_exists = True
            self.log("got the details for queuing_profile_exists: {0} and current_application_set: {1}".format(application_set_exists, current_application_set))
            return application_set_exists, current_application_set

        except Exception as e:
            self.status = "failed"
            self.msg = "An error occurred while retriving the application set details: {0}".format(e)
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

    def get_application_set_id(self, name):
        """
        Retrieves the details of an application set by its name.
        Description:
            This method queries the Cisco Catalyst Center API to determine if an application set with the specified
            name exists. It fetches the details of the application set if available. If the application set does not
            exist or an error occurs, the method logs the issue and either raises an exception or returns default values
            indicating that the application set was not found.
        Parameters:
            name (str): The name of the application set to retrieve.
        Returns:
            tuple: A tuple containing:
                - application_set_exists (bool): Indicates whether the application set exists.
                - current_application_set (dict): A dictionary containing the details of the application set, or an
                empty dictionary if the application set does not exist.
        Raises:
            Exception: If the API response is unexpected or indicates failure, an exception is raised, and the
            status is updated to "failed".
        """

        application_set_id = ''
        try:
            response = self.dnac._exec(
                family="application_policy",
                function='get_application_sets',
                params={"name": name}
            )
            self.log("Received API response from 'get_application_sets': {0}".format(str(response)), "DEBUG")

            if not response:
                self.log("Unexpected response received:", "ERROR")
                raise Exception

            if not response.get("response"):
                self.log("empty response {0}".format(response))
                raise Exception("No application set found in the Cisco Catalyst Center")

            current_application_set = response.get("response")
            application_set_id = current_application_set[0].get('id')

        except Exception as e:
            self.status = "failed"
            self.msg = "An error occurred while retriving the application set details: {0}".format(e)
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

        return application_set_id

    def get_application_details(self, name):
        """
        Retrieve the details of a specific application by its name.

        Parameters:
            self (object): An instance of the class used for interacting with Cisco Catalyst Center.
            name (str): The name of the application to retrieve.

        Returns:
            tuple: A tuple containing:
                - application_exists (bool): Indicates whether the application exists.
                - current_application (dict): The details of the application if found, otherwise an empty dictionary.

        Description:
            This function fetches the details of a specific application using the Cisco Catalyst Center API. It sends
            a request to retrieve the application data by specifying its name along with additional parameters for
            attributes, offset, and limit. If the response contains the application details, they are returned along
            with a flag indicating the existence of the application. In case of an error or unexpected response, the
            function logs the error, updates the status, and handles the exception gracefully.
        """
        application_exists = False
        current_application = {}
        try:

            response = self.dnac._exec(
                family="application_policy",
                function='get_applications',
                params={'attributes': "application", 'name': name, 'offset': 1, 'limit': 500}
            )
            self.log("Received API response from 'get_applications': {0}".format(str(response)), "DEBUG")

            if not response:
                self.log("Unexpected response received:", "ERROR")
                raise Exception

            if not response.get("response"):
                self.log("empty response {0}".format(response))
                return application_exists, current_application

            current_application = response.get("response")
            application_exists = True
            self.log("got the details for application_exists: {0} and current_application_set: {1}".format(application_exists, current_application))
            return application_exists, current_application

        except Exception as e:
            self.status = "failed"
            self.msg = "An error occurred while retriving the application details: {0}".format(e)
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

    def get_application_details_v1(self):
        """
        Retrieve the details of applications from Cisco Catalyst Center.

        Parameters:
            self (object): An instance of the class used for interacting with Cisco Catalyst Center.

        Returns:
            dict: A dictionary containing the details of the applications retrieved from Cisco Catalyst Center.

        Description:
            This function fetches the details of applications using the Cisco Catalyst Center API. It sends a request
            to retrieve application data with specified attributes, offset, and limit. If a response is received, it
            extracts the application details and logs the data. In case the response is empty, the function logs a
            message and returns an empty dictionary.
        """
        current_application = {}

        try:
            # Fetching application data
            response = self.dnac._exec(
                family="application_policy",
                function="get_applications",
                params={"attributes": "application", "offset": 1, "limit": 500}
            )

            self.log("Received API response from 'get_applications': {0}".format(response), "DEBUG")

            # Check if the response contains data
            if not response.get("response"):
                self.log("Empty response received: {0}".format(response))
                return current_application

            current_application = response.get("response")

            self.log(
                "Retrieved application details successfully. Application Data: {0}".format(current_application),
                "DEBUG"
            )
            return current_application

        except Exception as e:
            self.status = "failed"
            self.msg = "Error occurred while fetching application details: {0}".format(str(e))
            self.result["response"] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

    def get_application_policy_details(self, name):
        """
        Get application policy details for the specified policy name.

        Parameters:
            self (object): An instance of the class used for interacting with Cisco Catalyst Center.
            name (str): The name of the application policy to retrieve.

        Returns:
            tuple: A tuple containing:
                - application_policy_exists (bool): Indicates whether the application policy exists.
                - current_application_policy (dict): The details of the application policy if found, otherwise an empty dictionary.

        Description:
            This function interacts with the Cisco Catalyst Center API to retrieve the details of an application policy
            specified by its name. It sends an API request to fetch the policy details and processes the response.
            If the response contains the policy details, they are returned along with a flag indicating its existence.
            In case of an exception, the function updates the status and logs an appropriate error message.
        """
        application_policy_exists = False
        current_application_policy = {}
        try:

            response = self.dnac._exec(
                family="application_policy",
                function='get_application_policy',
                params={"policyScope": name}
            )
            self.log("Received API response from 'get_application_policy': {0}".format(str(response)), "DEBUG")

            if not response:
                self.log("Unexpected response received:", "ERROR")
                raise Exception

            if not response.get("response"):
                self.log("empty response {0}".format(response))
                return application_policy_exists, current_application_policy

            current_application_policy = response.get("response")
            application_policy_exists = True
            self.log(
                "got the details for queuing_profile_exists: {0} and current_application_policy: {1}"
                .format(application_policy_exists, current_application_policy)
            )
            return application_policy_exists, current_application_policy

        except Exception as e:
            self.status = "failed"
            self.msg = "{0}".format(e)
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

    def get_have(self):
        """
        Retrieve and store various software image and device details based on user-provided information.
        Returns:
            self: The current instance of the class with updated 'have' attributes.
        Raises:
            AnsibleFailJson: If required image or device details are not provided.
        Description:
            This function populates the 'have' dictionary with details related to software images, site information,
            device families, distribution devices, and activation devices based on user-provided data in the 'want' dictionary.
            It validates and retrieves the necessary information from Cisco Catalyst Center to support later actions.
        """
        have = {}
        if self.want.get("application_queuing_details"):
            application_queuing_details = self.want.get("application_queuing_details")
            for detail in application_queuing_details:
                if detail.get("profile_name"):
                    application_queuing_name = detail.get("profile_name")
                    if not application_queuing_name:
                        self.status = "failed"
                        self.msg = (
                            "The following parameter(s): 'profile_name' could not be found"
                            "and are mandatory to create or update application queuinig profile ."
                        )
                        self.log(self.msg, "ERROR")
                        self.result['response'] = self.msg
                        self.check_return_status()
                    queuing_profile_exists, current_queuing_profile = self.get_queuing_profile_details(application_queuing_name)
                    have["current_queuing_profile"] = current_queuing_profile
                    have["queuing_profile_exists"] = queuing_profile_exists

        if self.want.get("application_set_details"):
            application_set_details = self.want.get("application_set_details")[0]
            if application_set_details.get("application_set_name"):
                application_set_name = application_set_details.get("application_set_name")
                application_set_exists, current_application_set = self.get_application_set_details(application_set_name)
                have["current_application_set"] = current_application_set
                have["application_set_exists"] = application_set_exists

        if self.want.get("application_policy_details"):
            application_policy_details = self.want.get("application_policy_details")
            application_policy_name = self.want.get("application_policy_details", {}).get("name")

            if not application_policy_name:
                self.status = "failed"
                self.msg = (
                    "The following parameter(s): 'name' could not be found  and are mandatory to create or update application policy ."
                )
                self.log(self.msg, "ERROR")
                self.result['response'] = self.msg
                self.check_return_status()

            if application_policy_details.get("application_queuing_profile_name"):
                queuing_profile_name = application_policy_details.get("application_queuing_profile_name")
                queuing_profile_exists, current_queuing_profile = self.get_queuing_profile_details(queuing_profile_name)
                have["current_queuing_profile"] = current_queuing_profile
                have["queuing_profile_exists"] = queuing_profile_exists

                if not queuing_profile_exists:
                    self.status = "failed"
                    self.msg = (
                        "The application queuing profile does not exist - {0} ".format(queuing_profile_name)
                    )
                    self.log(self.msg, "ERROR")
                    self.result['response'] = self.msg
                    self.check_return_status()

            if application_policy_details.get("name"):
                application_policy_name = application_policy_details.get("name")
                application_policy_exists, current_application_policy = self.get_application_policy_details(application_policy_name)
                have["current_application_policy"] = current_application_policy
                have["application_policy_exists"] = application_policy_exists

        if self.want.get("application_details"):
            application_details = self.want.get("application_details")
            self.log(application_details)
            application_name = application_details.get("name")

            if not application_name:
                self.status = "failed"
                self.msg = (
                    "The following parameter(s): 'name' could not be found  and are mandatory to create or update application ."
                )
                self.log(self.msg, "ERROR")
                self.result['response'] = self.msg
                self.check_return_status()

            if application_details.get("name"):
                application_name = application_details.get("name")
                application_exists, current_application = self.get_application_details(application_name)
                have["current_application"] = current_application
                have["application_exists"] = application_exists

            if application_details.get("application_set_name"):
                application_set_name = application_details.get("application_set_name")
                application_set_exists, current_application_set = self.get_application_set_details(application_set_name)
                have["current_application_set"] = current_application_set
                have["application_set_exists"] = application_set_exists

        self.have = have
        self.log("Current State (have): {0}".format(str(self.have)), "INFO")

        return self

    def get_diff_merged(self, config):
        """
        Get application queuing details and then trigger xxxxxxxxxxx details followed by xxxxxxx details and xxxxxxxx details if specified in the playbook.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration dictionary containing tagging, distribution, and activation details.
        Returns:
            self: The current instance of the class with updated 'result' and 'have' attributes.
        Description:
            This function checks the provided playbook configuration for tagging, distribution, and activation details. It
            then triggers these operations in sequence if the corresponding details are found in the configuration.The
            function monitors the progress of each task and updates the 'result' dictionary accordingly. If any of the
            operations are successful, 'changed' is set to True.
        """

        self.config = config

        if config.get("application_queuing_details"):
            self.get_diff_queuing_profile().check_return_status()

        if support_for_application_set:
            if config.get("application_set_details"):
                self.get_diff_application_set().check_return_status()

        if config.get("application_details"):
            self.get_diff_application().check_return_status()

        if config.get("application_policy_details"):
            self.get_diff_application_policy().check_return_status()

        return self

    def is_update_required_for_application_policy(self):
        """
        Check if updates are required for the application policy and trigger necessary updates.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.

        Returns:
            bool:
                - True if updates are required for the application policy.
                - False if no updates are necessary.

        Description:
            This function evaluates whether updates are required for the application policy configuration in Cisco Catalyst Center
            based on the desired state provided in the configuration. It validates the existence of the application policy,
            identifies mismatches in queuing profiles and site mappings, and checks for missing application set names
            categorized as BUSINESS_RELEVANT, BUSINESS_IRRELEVANT, or DEFAULT.

            The function ensures the application policy aligns with the desired configuration while minimizing unnecessary updates.
        """

        application_policy_details = self.have

        # If application policy does not exist, create it and return
        if application_policy_details.get("application_policy_exists") is False:
            self.create_application_policy()
            return self

        req_application_policy_details = self.config.get("application_policy_details")
        application_queuing_profile_name = req_application_policy_details.get("application_queuing_profile_name")
        site_names = req_application_policy_details.get("site_name")
        site_ids = [self.get_site_id(site_name)[1] for site_name in site_names]
        current_application_policy = application_policy_details.get("current_application_policy")

        self.log(req_application_policy_details)

        # Flags to check if updates are required
        is_update_required_for_queuing_profile = any(
            application_queuing_profile_name not in contract.get("name")
            for contract in current_application_policy if contract.get('contract')
        )
        is_update_required_for_site = any(
            set(site_ids) != set(application_policy.get("advancedPolicyScope").get("advancedPolicyScopeElement")[0].get("groupId"))
            for application_policy in current_application_policy
        )

        # Logging the update status
        if is_update_required_for_queuing_profile:
            self.log("update required for queuing profile")
        else:
            self.log("no update required for queuing profile")

        if is_update_required_for_site:
            self.log("update required for site")
        else:
            self.log("no update required for site")

        other_check_names = ["application_queuing_profile", "site_name"]
        no_update_require = []
        if not is_update_required_for_queuing_profile:
            no_update_require.append("application_queuing_profile")
        if not is_update_required_for_site:
            no_update_require.append("site_name")

        update_not_required = True
        for check in other_check_names:
            if check not in no_update_require:
                update_not_required = False
                break

        # Final check: If no update is required for both queuing profile and site name
        if all(check in no_update_require for check in ["application_queuing_profile", "site_name"]):
            self.log("no update required for application policy")
            return False

        # Prepare application set names based on relevance
        want_business_relevant_set_name, want_business_irrelevant_set_name, want_default_set_name = [], [], []
        have_business_relevant_set_name, have_business_irrelevant_set_name, have_default_set_name = [], [], []

        application_set_names = req_application_policy_details.get("clause")
        for item in application_set_names:
            for relevance in item['relevance_details']:
                if relevance['relevance'] == 'BUSINESS_RELEVANT':
                    want_business_relevant_set_name.extend(relevance['application_set_name'])
                elif relevance['relevance'] == 'BUSINESS_IRRELEVANT':
                    want_business_irrelevant_set_name.extend(relevance['application_set_name'])
                elif relevance['relevance'] == 'DEFAULT':
                    want_default_set_name.extend(relevance['application_set_name'])

        # Process current application set names from existing policy
        for application_sets in current_application_policy:
            clause = application_sets.get("exclusiveContract", {}).get("clause")
            if clause and clause[0].get("relevanceLevel"):
                current_relevance_type = clause[0].get("relevanceLevel")
                app_set_name = application_sets.get("name").replace(application_sets.get("policyScope") + '_', "")

                if current_relevance_type == "BUSINESS_RELEVANT":
                    have_business_relevant_set_name.append(app_set_name)
                elif current_relevance_type == "BUSINESS_IRRELEVANT":
                    have_business_irrelevant_set_name.append(app_set_name)
                elif current_relevance_type == "DEFAULT":
                    have_default_set_name.append(app_set_name)

        # Compare and append missing items
        final_business_relevant_set_name, final_business_irrelevant_set_name, final_default_set_name = [], [], []
        for want_item, have_item, final_item in [
            (want_business_relevant_set_name, have_business_relevant_set_name, final_business_relevant_set_name),
            (want_business_irrelevant_set_name, have_business_irrelevant_set_name, final_business_irrelevant_set_name),
            (want_default_set_name, have_default_set_name, final_default_set_name)
        ]:
            final_item.extend(item for item in want_item if item not in have_item)

        # Ensure the default list is empty if no relevant/default values are there
        if not want_default_set_name:
            final_default_set_name = []
        if not want_business_relevant_set_name:
            final_business_relevant_set_name = []
        if not want_business_irrelevant_set_name:
            final_business_irrelevant_set_name = []

        if update_not_required :
            if not any([final_business_relevant_set_name, final_business_irrelevant_set_name, final_default_set_name]):
                self.log("no update required for application policy")
                return False

        return True

    def get_diff_application_policy(self):
        """
        Get the differences in application policy configuration and trigger necessary updates.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.

        Returns:
            self: The current instance of the class with updated 'result', 'status', and 'msg' attributes.

        Description:
            This function identifies differences between the current and desired application policy configurations in Cisco
            Catalyst Center. It validates the presence of mandatory parameters, checks for updates in queuing profiles and
            site mappings, and categorizes application sets based on relevance levels (BUSINESS_RELEVANT, BUSINESS_IRRELEVANT,
            and DEFAULT). The function generates a payload for required updates and ensures the application's compliance
            with the desired state.

            If discrepancies exist between the current and desired configurations, the function prepares and sends the
            appropriate API payloads to update the policy. Additionally, it ensures that no unexpected application sets
            are added. Errors or inconsistencies are logged, and the status, result, and message attributes are updated
            accordingly.

            This function also ensures the desired application policy reflects the latest configurations by performing
            detailed comparisons and triggering updates only when necessary.
        """

        application_policy_details = self.have
        application_policy_name = self.want.get("application_policy_details", {}).get("name")
        current_application_policy_details = self.config.get("application_policy_details")

        site_names = current_application_policy_details.get("site_name")
        application_queuing_profile_name = current_application_policy_details.get("application_queuing_profile_name")
        clause = current_application_policy_details.get("clause")

        missing_fields = []

        if not site_names:
            missing_fields.append("site_name")
        if not application_queuing_profile_name:
            missing_fields.append("application_queuing_profile_name")
        if not clause:
            missing_fields.append("clause")

        # Raise error if any field is missing
        if missing_fields:
            self.status = "failed"
            self.msg = "Application policy operation failed. The following mandatory parameters are missing or empty: {}.".format(", ".join(missing_fields))
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

        if application_policy_details.get("application_policy_exists") is False:
            self.create_application_policy()
            return self

        req_application_policy_details = self.config.get("application_policy_details")
        site_names = req_application_policy_details.get("site_name")
        site_ids = []
        for site_name in site_names:
            site_exists, site_id = self.get_site_id(site_name)
            site_ids.append(site_id)
        application_set_names = req_application_policy_details.get("clause")
        application_queuing_profile_name = req_application_policy_details.get("application_queuing_profile_name")
        queuing_profile_id = application_policy_details.get('current_queuing_profile', [])[0].get('id', None)
        current_application_policy = application_policy_details.get("current_application_policy")

        self.log(req_application_policy_details)

        is_update_required_for_queuing_profile = False
        is_update_required_for_site = False

        no_update_require = []
        other_check_names = ["application_queuing_profile", "site_name"]
        final_app_set_payload = []

        for contract in current_application_policy:
            if 'contract' in contract and contract['contract']:
                current_application_policy_queuing_id = contract.get("id")
                advanced_policy_scope_for_queuing_profile = contract.get("advancedPolicyScope").get("id")
                advanced_policy_scope_element_for_queuing_profile = contract.get("advancedPolicyScope").get("advancedPolicyScopeElement")[0].get("id")
                name = contract.get("name")
                if application_queuing_profile_name not in name:
                    is_update_required_for_queuing_profile = True
                    break

        # Check if the site IDs match
        for application_policy in current_application_policy:
            curent_site_ids = application_policy.get("advancedPolicyScope").get("advancedPolicyScopeElement")[0].get("groupId")
            # Compare the site_ids and curent_site_ids
            if set(site_ids) != set(curent_site_ids):
                is_update_required_for_site = True
                break

        if is_update_required_for_site or is_update_required_for_queuing_profile:
            self.log("update required for queuing profile" if is_update_required_for_queuing_profile else "update required for site")
            group_id = site_ids if is_update_required_for_site else curent_site_ids
            payload = {
                "id": current_application_policy_queuing_id,
                "name": "{}_{}".format(application_policy_name, application_queuing_profile_name),
                "deletePolicyStatus": current_application_policy[0].get("deletePolicyStatus"),
                "policyScope": current_application_policy[0].get("policyScope"),
                "priority": current_application_policy[0].get("priority"),
                "advancedPolicyScope": {
                    "id": advanced_policy_scope_for_queuing_profile,
                    "name": application_policy_name,
                    "advancedPolicyScopeElement": [
                        {
                            "id": advanced_policy_scope_element_for_queuing_profile,
                            "groupId": group_id,
                            "ssid": []
                        }
                    ]
                },
                "contract": {
                    "idRef": queuing_profile_id
                }
            }

            final_app_set_payload.append(payload)
            self.log(json.dumps(payload, indent=4))
        else:
            self.log("no update is required for queuing profile")
            no_update_require.append("application_queuing_profile")

        if is_update_required_for_site is True:
            self.log("update required for site")
        else:
            self.log("no update is required for site")
            no_update_require.append("site_name")

        update_not_required = True
        for check in other_check_names:
            if check not in no_update_require:
                update_not_required = False
                break

        want_business_relevant_set_name, want_business_irrelevant_set_name, want_default_set_name = [], [], []
        have_business_relevant_set_name, have_business_irrelevant_set_name, have_default_set_name = [], [], []
        final_business_relevant_set_name, final_business_irrelevant_set_name, final_default_set_name = [], [], []

        # Application data (replace with actual data or mock data)
        application_set_names = req_application_policy_details.get("clause")

        total_current_app_set = []
        total_want_app_set = []
        # Populate the lists based on relevance
        for item in application_set_names:
            for relevance in item['relevance_details']:
                if relevance['relevance'] == 'BUSINESS_RELEVANT':
                    want_business_relevant_set_name.extend(relevance['application_set_name'])
                    total_want_app_set.extend(relevance['application_set_name'])
                elif relevance['relevance'] == 'BUSINESS_IRRELEVANT':
                    want_business_irrelevant_set_name.extend(relevance['application_set_name'])
                    total_want_app_set.extend(relevance['application_set_name'])
                elif relevance['relevance'] == 'DEFAULT':
                    want_default_set_name.extend(relevance['application_set_name'])
                    total_want_app_set.extend(relevance['application_set_name'])

        self.log("Wanted Business Irrelevant Set: {}".format(want_business_irrelevant_set_name))
        self.log("Wanted Business Relevant Set: {}".format(want_business_relevant_set_name))
        self.log("Wanted Default Set: {}".format(want_default_set_name))

        # Populate current application set names
        for application_sets in current_application_policy:
            clause = application_sets.get("exclusiveContract", {}).get("clause")
            if clause and clause[0].get("relevanceLevel") is not None:
                current_relevance_type = clause[0].get("relevanceLevel")

                # Process Business Relevant
                if current_relevance_type == "BUSINESS_RELEVANT":
                    full_name = application_sets.get("name")
                    policy_name = application_sets.get("policyScope") + '_'
                    app_set_name = full_name.replace(policy_name, "")
                    have_business_relevant_set_name.append(app_set_name)
                    total_current_app_set.append(app_set_name)

                    for set_name in want_business_relevant_set_name:
                        if set_name in application_sets.get("name"):
                            self.log("No update required for: {}".format(set_name))

                # Process Business Irrelevant
                elif current_relevance_type == "BUSINESS_IRRELEVANT":
                    full_name = application_sets.get("name")
                    policy_name = application_sets.get("policyScope") + '_'
                    app_set_name = full_name.replace(policy_name, "")
                    have_business_irrelevant_set_name.append(app_set_name)
                    total_current_app_set.append(app_set_name)

                    for set_name in want_business_irrelevant_set_name:
                        if set_name in application_sets.get("name"):
                            self.log("No update required for: {}".format(set_name))

                # Process Default
                elif current_relevance_type == "DEFAULT":
                    full_name = application_sets.get("name")
                    policy_name = application_sets.get("policyScope") + '_'
                    app_set_name = full_name.replace(policy_name, "")
                    have_default_set_name.append(app_set_name)
                    total_current_app_set.append(app_set_name)

                    for set_name in want_default_set_name:
                        if set_name in application_sets.get("name"):
                            self.log("No update required for: {}".format(set_name))

        self.log("Total Current Application Set: {}".format(total_current_app_set))
        self.log("Total Want Application Set: {}".format(total_want_app_set))

        current_set = set(total_current_app_set)
        want_set = set(total_want_app_set)

        extra_in_want = want_set - current_set

        if extra_in_want:
            self.status = "failed"
            self.msg = "no extra application sets can be added to the application policy"
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

        else:
            self.log("Comparison passed. No extra items in want.")

        want_lists = [
            (want_business_relevant_set_name, have_business_relevant_set_name, final_business_relevant_set_name),
            (want_business_irrelevant_set_name, have_business_irrelevant_set_name, final_business_irrelevant_set_name),
            (want_default_set_name, have_default_set_name, final_default_set_name)
        ]

        for want_item, have_item, final_item in want_lists:
            for w in want_item:
                if w not in have_item:
                    final_item.append(w)
            if not want_item:
                final_item.extend([item for item in have_item if item not in final_item])

        if not want_default_set_name:
            final_default_set_name = []
        if not want_business_relevant_set_name:
            final_business_relevant_set_name = []
        if not want_business_irrelevant_set_name:
            final_business_irrelevant_set_name = []

        self.log("have Business Relevant: {}".format(have_business_relevant_set_name))
        self.log("have Business Irrelevant: {}".format(have_business_irrelevant_set_name))
        self.log("have Default: {}".format(have_default_set_name))

        self.log("Final Business Relevant: {}".format(final_business_relevant_set_name))
        self.log("Final Business Irrelevant: {}".format(final_business_irrelevant_set_name))
        self.log("Final Default: {}".format(final_default_set_name))

        final_want_business_relevant = []
        final_want_business_irrelevant = []
        final_want_default = []

        for item in have_business_relevant_set_name:
            if (item not in final_business_relevant_set_name and
                    item not in final_business_irrelevant_set_name and
                    item not in final_default_set_name):
                final_want_business_relevant.append(item)

        for item in have_business_irrelevant_set_name:
            if (item not in final_business_relevant_set_name and
                    item not in final_business_irrelevant_set_name and
                    item not in final_default_set_name):
                final_want_business_irrelevant.append(item)

        for item in have_default_set_name:
            if (item not in final_business_relevant_set_name and
                    item not in final_business_irrelevant_set_name and
                    item not in final_default_set_name):
                final_want_default.append(item)

        # Log the results
        self.log("Final want Business Relevant (Diff): {}".format(final_want_business_relevant))
        self.log("Final want Business Irrelevant (Diff): {}".format(final_want_business_irrelevant))
        self.log("Final want Default (Diff): {}".format(final_want_default))
        self.application_policy_updated = self.is_update_required_for_application_policy()
        self.log(self.application_policy_updated)
        if update_not_required :
            if not (final_business_irrelevant_set_name or final_business_relevant_set_name or final_default_set_name):
                self.log("no update required for application policy")
                self.status = "success"
                self.result['changed'] = False
                self.msg = "application policy '{0}' does not need any update. ".format(application_policy_name)
                self.result['msg'] = self.msg
                self.result['response'] = self.msg
                self.log(self.msg, "INFO")
                return self

        for application_sets in current_application_policy:
            group_id = site_ids if is_update_required_for_site else curent_site_ids
            for app_set in final_business_relevant_set_name + final_business_irrelevant_set_name + final_default_set_name:
                if app_set in final_business_relevant_set_name:
                    relevance_level = "BUSINESS_RELEVANT"
                elif app_set in final_business_irrelevant_set_name:
                    relevance_level = "BUSINESS_IRRELEVANT"
                elif app_set in final_default_set_name:
                    relevance_level = "DEFAULT"

                if relevance_level and app_set in application_sets.get("name"):
                    self.log(app_set)
                    app_set_payload = {
                        "id": application_sets.get("id"),
                        "name": "{}_{}".format(application_sets.get('policyScope'), app_set),
                        "deletePolicyStatus": application_sets.get("deletePolicyStatus"),
                        "policyScope": application_sets.get('policyScope'),
                        "priority": application_sets.get('priority'),
                        "advancedPolicyScope": {
                            "id": application_sets.get("advancedPolicyScope").get("id"),
                            "name": application_sets.get("advancedPolicyScope").get("name"),
                            "advancedPolicyScopeElement": [
                                {
                                    "id": application_sets.get("advancedPolicyScope").get("advancedPolicyScopeElement")[0].get("id"),
                                    "groupId": group_id,
                                    "ssid": []
                                }
                            ]
                        },
                        "exclusiveContract": {
                            "id": application_sets.get("exclusiveContract").get("id"),
                            "clause": [
                                {
                                    "id": application_sets.get("exclusiveContract").get("clause")[0].get("id"),
                                    "type": application_sets.get("exclusiveContract").get("clause")[0].get("type"),
                                    "relevanceLevel": relevance_level
                                }
                            ]
                        },
                        "producer": {
                            "id": application_sets.get("producer").get("id"),
                            "scalableGroup": [
                                {
                                    "idRef": application_sets.get("producer").get("scalableGroup")[0].get("idRef")
                                }
                            ]
                        }
                    }
                    final_app_set_payload.append(app_set_payload)

        for application_sets in current_application_policy:
            if is_update_required_for_site is True:
                group_id = site_ids if is_update_required_for_site else curent_site_ids
                for app_set in final_want_business_relevant + final_want_business_irrelevant + final_want_default:
                    if app_set in final_want_business_relevant:
                        relevance_level = "BUSINESS_RELEVANT"
                    elif app_set in final_want_business_irrelevant:
                        relevance_level = "BUSINESS_IRRELEVANT"
                    elif app_set in final_want_default:
                        relevance_level = "DEFAULT"

                    if relevance_level and app_set in application_sets.get("name"):
                        self.log(app_set)
                        app_set_payload = {
                            "id": application_sets.get("id"),
                            "name": "{}_{}".format(application_sets.get('policyScope'), app_set),
                            "deletePolicyStatus": application_sets.get("deletePolicyStatus"),
                            "policyScope": application_sets.get('policyScope'),
                            "priority": application_sets.get('priority'),
                            "advancedPolicyScope": {
                                "id": application_sets.get("advancedPolicyScope").get("id"),
                                "name": application_sets.get("advancedPolicyScope").get("name"),
                                "advancedPolicyScopeElement": [
                                    {
                                        "id": application_sets.get("advancedPolicyScope").get("advancedPolicyScopeElement")[0].get("id"),
                                        "groupId": group_id,
                                        "ssid": []
                                    }
                                ]
                            },
                            "exclusiveContract": {
                                "id": application_sets.get("exclusiveContract").get("id"),
                                "clause": [
                                    {
                                        "id": application_sets.get("exclusiveContract").get("clause")[0].get("id"),
                                        "type": application_sets.get("exclusiveContract").get("clause")[0].get("type"),
                                        "relevanceLevel": relevance_level
                                    }
                                ]
                            },
                            "producer": {
                                "id": application_sets.get("producer").get("id"),
                                "scalableGroup": [
                                    {
                                        "idRef": application_sets.get("producer").get("scalableGroup")[0].get("idRef")
                                    }
                                ]
                            }
                        }
                        final_app_set_payload.append(app_set_payload)

        self.log(json.dumps(final_app_set_payload, indent=4))
        try:
            response = self.dnac._exec(
                family="application_policy",
                function='application_policy_intent',
                op_modifies=True,
                params={'updateList': final_app_set_payload, }
            )

            self.log("Received API response from 'application_policy_intent' for Update: {}".format(response), "DEBUG")
            self.check_tasks_response_status(response, "application_policy_intent")

            if self.status not in ["failed", "exited"]:
                self.log("application policy '{0}' updated successfully.".format(application_policy_name), "INFO")
                self.status = "success"
                self.result['changed'] = True
                self.msg = ("application policy '{0}' updated successfully.".format(application_policy_name))
                self.result['response'] = self.msg
                return self

            if self.status == "failed":
                fail_reason = self.msg
                self.status = "failed"
                self.msg = "update of the application policy failed due to - {0}".format(fail_reason)
                self.result['response'] = self.msg
                self.log(self.msg, "ERROR")
                self.check_return_status()

        except Exception as e:
            self.status = "failed"
            self.msg = "{0}".format(e)
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

    def get_ssid_from_wc(self, device_id, wlan_id):
        try:
            response = self.dnac._exec(
                family="wireless",
                function='get_ssid_details_for_specific_wireless_controller',
                op_modifies=True,
                params={'network_device_id': device_id, }
            )

            self.log("Received API response from 'get_ssid_details_for_specific_wireless_controller' : {0}".format(response), "DEBUG")
            # Initialize the variable to store the SSID name
            ssid_name = None

            # Iterate through the list of dictionaries inside the 'response' key
            for item in response.get("response"):
                if item['wlanId'] == int(wlan_id):
                    # Assign the corresponding SSID name to the variable
                    ssid_name = item['ssidName']
                    break  # Exit the loop as we found the match

            # Print the result
            if ssid_name:
                self.log("The SSID name for WLAN ID {} is: {}".format(wlan_id, ssid_name))
            else:
                self.log("No SSID name found for WLAN ID {}.".format(wlan_id))

            return ssid_name

        except Exception as e:
            self.status = "failed"
            self.msg = "{0}".format(e)
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

    def create_application_policy(self):
        """
        Create an application policy and trigger its deployment details based on the configuration provided in the playbook.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.

        Returns:
            self: The current instance of the class with updated 'result', 'status', and 'msg' attributes.

        Description:
            This function creates an application policy in the Catalyst Center by processing the configuration details
            provided in the playbook. It retrieves site information, identifies application queuing profiles, and
            categorizes application sets based on relevance levels (BUSINESS_RELEVANT, BUSINESS_IRRELEVANT, and DEFAULT).
            The application sets are mapped to their IDs, and a payload is generated for API submission. The function
            then sends a request to create the application policy and validates the response.
            In case of an error or failure in creation, appropriate error messages are logged, and the function updates
            the status and result attributes.
        """

        new_application_policy_details = self.config.get("application_policy_details")
        application_policy_name = self.want.get("application_policy_details", {}).get("name")
        device_type = self.want.get("application_policy_details", {}).get("device_type")
        device = self.want.get("application_policy_details", {}).get("device", {})

        if device.get("device_ip"):
            device_ip = device.get("device_ip")
            Wlan_id = device.get("Wlan_id")

        else:
            device_ip = None
            Wlan_id = None
        site_names = new_application_policy_details.get("site_name")
        application_queuing_profile_name = new_application_policy_details.get("application_queuing_profile_name")
        clause = new_application_policy_details.get("clause")

        missing_fields = []

        if not site_names:
            missing_fields.append("site_name")
        if not application_queuing_profile_name:
            missing_fields.append("application_queuing_profile_name")
        if not clause:
            missing_fields.append("clause")

        # Raise error if any field is missing
        if missing_fields:
            self.status = "failed"
            self.msg = "Application policy operation failed. The following mandatory parameters are missing or empty: {}.".format(", ".join(missing_fields))
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

        site_ids = []
        for site_name in site_names:
            site_exists, site_id = self.get_site_id(site_name)
            site_ids.append(site_id)
        application_policy_details = self.have
        application_set_names = new_application_policy_details.get("clause")
        application_queuing_profile_name = new_application_policy_details.get("application_queuing_profile_name")
        queuing_profile_id = application_policy_details.get('current_queuing_profile', [])[0].get('id', None)

        if device_type == "wireless":
            wc_device_id = self.get_device_ids_from_device_ips([device_ip])
            ssid = self.get_ssid_from_wc(wc_device_id.get(device_ip), Wlan_id)
            self.log(ssid)
            if ssid:
                ssid = [ssid]
        else:
            ssid = []
        self.log(ssid)
        # Initialize empty lists for each relevance
        business_relevant_set_name, business_relevant_set_id = [], []
        business_irrelevant_set_name, business_irrelevant_set_id = [], []
        default_set_name, default_set_id = [], []

        # Populate the lists based on relevance
        for item in application_set_names:
            for relevance in item['relevance_details']:
                if relevance['relevance'] == 'BUSINESS_RELEVANT':
                    business_relevant_set_name.extend(relevance['application_set_name'])
                elif relevance['relevance'] == 'BUSINESS_IRRELEVANT':
                    business_irrelevant_set_name.extend(relevance['application_set_name'])
                elif relevance['relevance'] == 'DEFAULT':
                    default_set_name.extend(relevance['application_set_name'])

        # Get application set IDs for business_relevant
        for app_set_name in business_relevant_set_name:
            app_set_id = self.get_application_set_id(app_set_name)
            if app_set_id:
                business_relevant_set_id.append({"name": app_set_name, "id": app_set_id})
            else:
                self.log("No app set found for {}".format(app_set_name))

        # Get application set IDs for business_irrelevant
        for app_set_name in business_irrelevant_set_name:
            app_set_id = self.get_application_set_id(app_set_name)
            if app_set_id:
                business_irrelevant_set_id.append({"name": app_set_name, "id": app_set_id})
            else:
                self.log("No app set found for {}".format(app_set_name))

        # Get application set IDs for default
        for app_set_name in default_set_name:
            app_set_id = self.get_application_set_id(app_set_name)
            if app_set_id:
                default_set_id.append({"name": app_set_name, "id": app_set_id})
            else:
                self.log("No app set found for {}".format(app_set_name))

        # Log the final lists
        self.log("Business Relevant Set IDs: {}".format(business_relevant_set_id))
        self.log("Business Irrelevant Set IDs: {}".format(business_irrelevant_set_id))
        self.log("Default Set IDs: {}".format(default_set_id))

        # Determine the deletePolicyStatus
        policy_status = new_application_policy_details.get("policy_status")
        delete_policy_status = {
            "deployed": "NONE",
            "deleted": "DELETED",
            "restored": "RESTORED"
        }.get(policy_status, "NONE")

        # Map relevance to application set IDs
        relevance_map = {
            "BUSINESS_RELEVANT": business_relevant_set_id,
            "BUSINESS_IRRELEVANT": business_irrelevant_set_id,
            "DEFAULT": default_set_id
        }

        payload = []
        payload.append({
            "name": "{}_{}".format(application_policy_name, application_queuing_profile_name),
            "deletePolicyStatus": delete_policy_status,
            "policyScope": "{}".format(application_policy_name),
            "priority": "100",
            "advancedPolicyScope": {
                "name": "{}".format(application_policy_name),
                "advancedPolicyScopeElement": [
                    {
                        "groupId": site_ids,
                        "ssid": ssid
                    }
                ]
            },
            "contract": {
                "idRef": queuing_profile_id
            }
        })

        for relevance_detail in new_application_policy_details['clause'][0]['relevance_details']:
            relevance_level = relevance_detail['relevance']
            application_set_names = relevance_detail['application_set_name']

            for app_set_name in application_set_names:
                # Find the matching application set ID
                matching_set = next((item for item in relevance_map[relevance_level] if item['name'] == app_set_name), None)
                if not matching_set:
                    continue

                # Append the policy details to the payload
                payload.append({
                    "name": "{}_{}".format(application_policy_name, app_set_name),
                    "deletePolicyStatus": delete_policy_status,
                    "policyScope": "{}".format(application_policy_name),
                    "priority": "100",
                    "advancedPolicyScope": {
                        "name": "{}".format(application_policy_name),
                        "advancedPolicyScopeElement": [
                            {
                                "groupId": site_ids,
                                "ssid": ssid
                            }
                        ]
                    },
                    "exclusiveContract": {
                        "clause": [
                            {
                                "type": "BUSINESS_RELEVANCE",
                                "relevanceLevel": relevance_level
                            }
                        ]
                    },
                    "producer": {
                        "scalableGroup": [
                            {
                                "idRef": matching_set['id']
                            }
                        ]
                    }
                })

        self.log(json.dumps(payload, indent=4))

        try:
            response = self.dnac._exec(
                family="application_policy",
                function='application_policy_intent',
                op_modifies=True,
                params={'createList': payload}
            )

            self.log("Received API response from 'application_policy_intent' for creation: {}".format(response), "DEBUG")
            self.check_tasks_response_status(response, "application_policy_intent")

            if self.status not in ["failed", "exited"]:
                self.log("application policy '{0}' created successfully.".format(application_policy_name), "INFO")
                self.status = "success"
                self.result['changed'] = True
                self.msg = ("application policy '{0}' created successfully.".format(application_policy_name))
                self.result['response'] = self.msg
                return self

            if self.status == "failed":
                fail_reason = self.msg
                self.status = "failed"
                self.msg = "creation of the application policy failed due to - {0}".format(fail_reason)
                self.result['response'] = self.msg
                self.log(self.msg, "ERROR")
                self.check_return_status()

        except Exception as e:
            self.status = "failed"
            self.msg = "{0}".format(e)
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

    def is_update_required_for_application(self):
        """
        Determine if an update is required for the application based on differences between
        required and current application details.

        Returns:
            bool: True if an update is required, False otherwise.
        """

        required_application_details = self.want.get("application_details")
        current_application_details = self.have.get("current_application")[0]
        application_set_id = None

        current_application_set = self.have.get("current_application_set")
        if current_application_set and isinstance(current_application_set, list) and len(current_application_set) > 0:
            application_set_id = current_application_set[0].get("id")

        # Define the mappings for comparison
        fields_to_check = {
            "description": "longDescription",
            "helpstring": "helpString",
            "traffic_class": "trafficClass",
            "server_name": "serverName"
        }

        # Check if updates are required
        for required_key, current_key in fields_to_check.items():
            required_value = required_application_details.get(required_key)
            current_value = current_application_details.get("networkApplications")[0].get(current_key)

            if current_value is None and required_value is not None:
                self.log("Update required for {} as current value is None.".format(required_key))
                return True

            if required_value != current_value:
                self.log("Update required for {}".format(required_key))
                return True

        # Check for application_set_id
        if application_set_id != current_application_details.get("parentScalableGroup").get("idRef") and application_set_id is not None:
            self.log("Update required for application_set")
            return True

        self.log("No updates required.")
        return False

    def get_diff_application(self):
        """
        Retrieve and update differences between current and required application configurations.

        Parameters:
            self (object): An instance of the class for interacting with Cisco Catalyst Center.

        Returns:
            self: The updated instance with 'status', 'msg', and 'result' attributes.

        Description:
            Compares the existing application details ('have') with the desired configuration ('want') and updates
            the application if discrepancies are found. Handles mandatory field validation, constructs the update
            payload, logs required actions, and sends an API request to apply changes.
        """

        application_name = self.want.get("application_details", {}).get("name")
        application_set_name = self.want.get("application_details").get("application_set_name")

        if application_name is None:
            self.status = "failed"
            self.msg = "mandatory field 'application_name' is missing"
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

        application_details = self.have
        required_application_details = self.want.get("application_details")

        if application_details.get("application_set_exists") is False:
            self.status = "success"
            self.result['changed'] = False
            self.msg = (
                "The application set '{0}' is not available in the Cisco Catalyst Center. "
                "Only the default application sets can be used. "
                "Defer this feature as API issue is there. "
                "Once it's fixed, we will address it in the upcoming release.".format(application_set_name)
            )
            self.result['msg'] = self.msg
            self.result['response'] = self.msg
            self.log(self.msg, "INFO")
            return self

        if application_details.get("application_exists") is False:
            self.create_application()
            return self

        current_application_details = application_details.get("current_application")[0]

        current_application_set = application_details.get("current_application_set")

        application_set_id = None
        if current_application_set and isinstance(current_application_set, list) and len(current_application_set) > 0:
            application_set_id = current_application_set[0].get("id")

        application_name = current_application_details.get("name")
        self.log(current_application_details)
        if required_application_details.get("name") != current_application_details.get("name"):
            self.log("application name cant be updated")

        fields_to_check = {
            "description": "longDescription",
            "helpstring": "helpString",
            "traffic_class": "trafficClass",
            "server_name": "serverName"
        }

        update_required_keys = []

        for required_key, current_key in fields_to_check.items():
            required_value = required_application_details.get(required_key)
            current_value = current_application_details.get("networkApplications")[0].get(current_key)
            if current_value is None:
                if required_value is not None:
                    self.log("Update required for {} as current value is None.".format(required_key))
                    update_required_keys.append(required_key)
                else:
                    self.log("Skipping {} as both values are None.".format(required_key))
                continue

            if required_value == current_value or required_value is None:
                self.log("Update not required for {}".format(required_key))
            else:
                self.log("Update required for {}".format(required_key))
                update_required_keys.append(required_key)

        if application_set_id == current_application_details.get("parentScalableGroup").get("idRef") or application_set_id is None:
            self.log("update not required for application_set")
            application_set_id = current_application_details.get("parentScalableGroup").get("idRef")
        else:
            self.log("update required for application set")
            update_required_keys.append("application_set")

        self.application_updated = self.is_update_required_for_application()

        if not update_required_keys:
            self.status = "success"
            self.result['changed'] = False
            self.msg = "application '{0}' does not need any update. ".format(application_name)
            self.result['msg'] = self.msg
            self.result['response'] = self.msg
            self.log(self.msg, "INFO")
            return self

        network_application_payload = {
            "id": current_application_details.get("networkApplications")[0].get("id"),
            "applicationSubType": current_application_details.get("networkApplications")[0].get("applicationSubType"),
            "applicationType": current_application_details.get("networkApplications")[0].get("applicationType"),
            "categoryId": current_application_details.get("networkApplications")[0].get("categoryId"),
            "displayName": current_application_details.get("networkApplications")[0].get("displayName"),
            "helpString": (
                required_application_details.get("helpstring")
                if "helpstring" in update_required_keys
                else current_application_details.get("networkApplications")[0].get("helpString")
            ),
            "longDescription": (
                required_application_details.get("description")
                if "description" in update_required_keys
                else current_application_details.get("networkApplications")[0].get("longDescription")
            ),
            "name": current_application_details.get("networkApplications")[0].get("name"),
            "popularity": current_application_details.get("networkApplications")[0].get("popularity"),
            "rank": (
                required_application_details.get("rank")
                if "rank" in update_required_keys
                else current_application_details.get("networkApplications")[0].get("rank")
            ),
            "selectorId": current_application_details.get("networkApplications")[0].get("selectorId"),
            "trafficClass": (
                required_application_details.get("traffic_class")
                if "traffic_class" in update_required_keys
                else current_application_details.get("networkApplications")[0].get("trafficClass")
            ),
        }

        self.log(current_application_details.get("networkApplications")[0].get("trafficClass"))
        if "server_name" in required_application_details:
            network_application_payload["serverName"] = required_application_details.get("server_name")
            if "serverName" in current_application_details.get("networkApplications")[0]:
                network_application_payload["serverName"] = current_application_details.get("networkApplications")[0].get("serverName")
        else:
            if "url" in required_application_details:
                network_application_payload["url"] = required_application_details.get("url")
            if "url" in current_application_details.get("networkApplications")[0]:
                network_application_payload["url"] = current_application_details.get("networkApplications")[0].get("url")
            if "app_protocol" in required_application_details:
                network_application_payload["appProtocol"] = required_application_details.get("app_protocol")
            if "appProtocol" in current_application_details.get("networkApplications")[0]:
                network_application_payload["appProtocol"] = current_application_details.get("networkApplications")[0].get("appProtocol")

        network_identity_setting = {}

        if "network_identity_setting" in required_application_details:
            network_identity_details = required_application_details["network_identity_setting"]

            key_mapping = {
                "protocol": "protocol",
                "port": "ports",
                "ip_subnet": "ipv4Subnet",
                "lower_Port": "lowerPort",
                "upper_port": "upperPort"
            }

            for source_key, target_key in key_mapping.items():
                if source_key in network_identity_details:
                    network_identity_setting[target_key] = network_identity_details[source_key]

        self.log(network_identity_setting)

        # Construct the full payload
        param = [
            {
                "id": current_application_details.get("id"),
                "instanceId": current_application_details.get("instanceId"),
                "displayName": current_application_details.get("displayName"),
                "instanceVersion": current_application_details.get("instanceVersion"),
                "name": current_application_details.get("name"),
                "namespace": current_application_details.get("namespace"),
                "networkApplications": [network_application_payload],
                "parentScalableGroup": {
                    "idRef": application_set_id
                },
                **(
                    {"networkIdentity": [network_identity_setting]}
                    if "network_identity_setting" in required_application_details
                    else {}
                ),
                "qualifier": current_application_details.get("qualifier"),
                "scalableGroupExternalHandle": current_application_details.get("scalableGroupExternalHandle"),
                "scalableGroupType": current_application_details.get("scalableGroupType"),
                "type": current_application_details.get("type"),
            }
        ]

        self.log("Payload for update application: {}".format(json.dumps(param, indent=4)))

        try:
            response = self.dnac._exec(
                family="application_policy",
                function='edit_applications',
                op_modifies=True,
                params={"payload": param}
            )

            self.log("Received API response from 'edit_applications': {}".format(response), "DEBUG")
            self.check_tasks_response_status(response, "edit_applications")

            if self.status not in ["failed", "exited"]:
                self.log("application '{0}' updated successfully.".format(application_name), "INFO")
                self.status = "success"
                self.result['changed'] = True
                self.msg = ("application '{0}' updated successfully.".format(application_name))
                self.result['response'] = self.msg
                return self

            if self.status == "failed":
                fail_reason = self.msg
                self.status = "failed"
                self.msg = "updation of the application failed due to - {0}".format(fail_reason)
                self.result['response'] = self.msg
                self.log(self.msg, "ERROR")
                self.check_return_status()

        except Exception as e:
            self.status = "failed"
            self.msg = "updation of the application failed due to: {0}".format(e)
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

    def create_application(self):
        """
        Create a new application in Cisco DNA Center.

        Parameters:
            self (object): An instance of the class for interacting with Cisco DNA Center.

        Returns:
            self: The updated instance with 'status', 'msg', and 'result' attributes.

        Description:
            This method creates a new application by comparing the desired configuration ('want') with the existing
            application details ('have'). It checks for missing mandatory fields, validates the application type,
            and constructs the payload for the application creation request. The method sends an API request to
            Cisco DNA Center to create the application and logs success or failure. If any errors are encountered,
            they are handled and returned with appropriate messages.
        """

        new_application_set_details = self.want
        application_set_name = new_application_set_details.get('application_details', {}).get('application_set_name')
        application_set_id = self.get_application_set_id(application_set_name)
        application_details = self.want.get("application_details")
        application_name = application_details.get("name")
        application_traffic_class = application_details.get("traffic_class")
        application_type = application_details.get("type")
        application_details_set = self.have
        get_application_set = application_details.get("current_application_set")

        missing_fields = []

        if application_traffic_class is None:
            missing_fields.append("traffic_class")
        if application_name is None:
            missing_fields.append("application_name")
        if application_set_name is None:
            missing_fields.append("application_set_name")
        if application_type is None:
            missing_fields.append("type")

        if missing_fields:
            self.status = "failed"
            self.msg = "As we need to create a new application - mandatory field(s) missing: {}".format(', '.join(missing_fields))
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

        get_application_list = self.get_application_details_v1()

        category_id = None

        for app in get_application_list:
            if app.get("parentScalableGroup", {}).get("idRef") == application_set_id:
                network_applications = app.get("networkApplications")
                if network_applications and isinstance(network_applications, list):
                    category_id = network_applications[0].get("categoryId")
                break

        supported_types = ["server_name", "url", "server_ip"]

        if application_details.get("type") not in ["server_name", "url", "server_ip"]:
            self.status = "failed"
            self.msg = "Unsupported application type: '{0}'. Supported values are: {1}".format(application_type, ', '.join(supported_types))
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

        # Prepare common application data, ignoring optional fields if not provided
        network_application = {
            "applicationType": "CUSTOM",
            "trafficClass": application_details.get("traffic_class"),
            "categoryId": category_id,
            "type": "_server-ip" if application_details.get("type") == "server_ip" else
                    "_url" if application_details.get("type") == "url" else "_servername"
        }

        # Add optional fields if they exist in the application_details
        optional_fields = [
            ("ignore_conflict", "ignoreConflict"),
            ("rank", "rank"),
            ("engine_id", "engineId"),
            ("helpstring", "helpString"),
            ("description", "longDescription")
        ]

        for field, key in optional_fields:
            value = application_details.get(field)
            if value is not None:  # Only add to payload if the value exists
                network_application[key] = value if key not in ("rank", "engineId") else int(value)

        # Add specific fields for 'server_name', 'url', or 'server_ip'
        app_type = application_details.get("type")

        if app_type == "server_name":
            if application_details.get("server_name") is None:
                self.status = "failed"
                self.msg = ("server_name is required for the type - server_name")
                self.result['response'] = self.msg
                self.log(self.msg, "ERROR")
                self.check_return_status()

            network_application["serverName"] = application_details.get("server_name")

        elif app_type == "url":
            if application_details.get("app_protocol") is None or application_details.get("url") is None:
                self.status = "failed"
                self.msg = ("app_protocol and url are required for the type - url")
                self.result['response'] = self.msg
                self.log(self.msg, "ERROR")
                self.check_return_status()

            network_application["appProtocol"] = application_details.get("app_protocol")
            network_application["url"] = application_details.get("url")

        # Handle the conditional inclusion of `dscp` or `network_identity_setting` (or both)
        dscp = application_details.get("dscp")
        network_identity_setting = application_details.get("network_identity_setting", {})

        network_identity_list = None  # Default to None

        if app_type == "server_ip":
            if not dscp and not network_identity_setting:
                self.status = "failed"
                self.msg = ("Either 'dscp' or 'network_identity_setting' must be provided for the type - server_ip.")
                self.result['response'] = self.msg
                self.log(self.msg, "ERROR")
                self.check_return_status()

            # Add dscp if present
            if dscp:
                network_application["dscp"] = dscp

            # Add network_identity_setting if present
            if network_identity_setting:
                protocol = network_identity_setting.get("protocol")
                ports = network_identity_setting.get("port")

                # Raise an error if mandatory fields are missing
                if not protocol or not ports:
                    self.status = "failed"
                    self.msg = ("Both 'protocol' and 'ports' are required for the network identity in server_ip type.")
                    self.result['response'] = self.msg
                    self.log(self.msg, "ERROR")
                    self.check_return_status()

                # Prepare networkIdentity dictionary with mandatory and optional fields
                network_identity = {
                    "protocol": protocol,
                    "ports": str(ports)  # Ensure port is a string
                }

                # Optional fields for networkIdentity
                optional_network_identity_fields = [
                    ("ip_subnet", "ipv4Subnet"),
                    ("lower_port", "lowerPort"),
                    ("upper_port", "upperPort")
                ]

                for field, key in optional_network_identity_fields:
                    value = network_identity_setting.get(field)
                    if value is not None:
                        network_identity[key] = value

                # Include networkIdentity in the payload
                network_identity_list = [network_identity]

        # Prepare the rest of the payload
        param = {
            "name": application_details.get("name"),
            "parentScalableGroup": {
                "idRef": application_set_id
            },
            "scalableGroupType": "APPLICATION",
            "type": "scalablegroup",
            "networkApplications": [network_application],
        }

        # Add networkIdentity if it exists
        if network_identity_list:
            param["networkIdentity"] = network_identity_list
        self.log(param)
        try:
            response = self.dnac._exec(
                family="application_policy",
                function='create_applications',
                op_modifies=True,
                params={"payload": [param]}
            )

            self.log("Received API response from 'create_applications': {}".format(response), "DEBUG")
            self.check_tasks_response_status(response, "create_applications")

            if self.status not in ["failed", "exited"]:
                self.log("application '{0}' created successfully.".format(application_name), "INFO")
                self.status = "success"
                self.result['changed'] = True
                self.msg = ("application '{0}' created successfully.".format(application_name))
                self.result['response'] = self.msg
                return self

            if self.status == "failed":
                fail_reason = self.msg
                self.status = "failed"
                self.msg = "creation of the application failed due to - {0}".format(fail_reason)
                self.result['response'] = self.msg
                self.log(self.msg, "ERROR")
                self.check_return_status()

        except Exception as e:
            self.status = "failed"
            self.msg = "{0}".format(e)
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

    def get_diff_application_set(self):
        """
        Manages the creation of an application set by checking for its existence.

        Description:
            This method checks if an application set already exists using the `have` attribute.
            If the application set exists, it logs the status and skips creation. If it does not
            exist, the method calls `create_application_set` to create a new application set.

        Parameters:
            None: This method relies on the class instance's `have` attribute for determining the current state.

        Returns:
            self: The current instance of the class, updated with the result of the operation.

        Raises:
            None: All conditions and errors are handled internally.
        """

        application_set_details = self.have
        if application_set_details.get("application_set_exists") is True:
            self.status = "success"
            self.result['changed'] = False
            self.msg = "application set already exist and hence cannot be updated"
            self.result['msg'] = self.msg
            self.result['response'] = self.msg
            self.log(self.msg, "INFO")
            return self
        if application_set_details.get("application_set_exists") is False:
            self.status = "success"
            self.result['changed'] = False
            self.msg = "Defer this feature as API issue is there once it's fixed we will addresses it in upcoming release"
            self.result['msg'] = self.msg
            self.result['response'] = self.msg
            self.log(self.msg, "INFO")
            return self

        # self.create_application_set()
        return self

    def create_application_set(self):
        """
        Creates a new application set in Cisco Catalyst Center.
        Description:
            This method retrieves the application set details from the `config` attribute and constructs a payload
            required to create the application set. It then triggers the appropriate API call to create the application set
            and monitors the task's response status. If the creation is successful, the method updates the status and logs
            a success message.
        Parameters:
            None: The method uses the `config` attribute from the class instance to retrieve application set details.
        Returns:
            self: Returns the current instance of the class with updated attributes such as `status`, `result`, and `msg`.
        Raises:
            None: Any errors or unexpected behaviors are handled within the method and logged appropriately.
        """
        new_application_set_details = self.want
        application_set_name = new_application_set_details.get('application_details', {}).get('application_set_name')
        param = {"name": application_set_name}
        try:
            response = self.dnac._exec(
                family="application_policy",
                function='create_application_set',
                op_modifies=True,
                params={"payload": [param]}
            )
            self.log("Received API response from 'create_application_set': {}".format(response), "DEBUG")
            self.check_tasks_response_status(response, "create_application_set")

            if self.status not in ["failed", "exited"]:
                self.log("application set '{0}' created successfully.".format(application_set_name), "INFO")
                self.status = "success"
                self.result['changed'] = True
                self.msg = ("application set '{0}' created successfully.".format(application_set_name))
                self.result['response'] = self.msg
                return self

        except Exception as e:
            self.status = "failed"
            self.msg = "An error occured while creating application set: {0}".format(e)
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

    def get_diff_queuing_profile(self):
        """
        Creates a new application queuing profile based on the provided configuration.
        Description:
            This method retrieves queuing profile details from the `config` attribute and validates mandatory fields.
            It constructs the payload required for creating a queuing profile and triggers the appropriate API call
            to Cisco Catalyst Center. The response from the API is logged for debugging and tracking purposes.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Raises:
            ValueError: If any mandatory fields (`profile_name`, `type`, or `tc_bandwidth_settings`) are missing
            in the configuration.
        Returns:
            None: The method updates the system state by calling the API and logs the API response.
        """
        queuing_profile = self.have
        required_queuing_profile_details = self.want

        if queuing_profile.get("queuing_profile_exists") is False:
            self.create_queuing_profile()
            return self

        required_details = required_queuing_profile_details['application_queuing_details'][0]
        current_profiles = queuing_profile.get('current_queuing_profile', [])
        if required_details.get('bandwidth_settings', {}):
            is_common = required_details.get('bandwidth_settings', {}).get('is_common_between_all_interface_speeds')

        for item in current_profiles:
            for clause in item.get('clause', []):
                if clause.get('isCommonBetweenAllInterfaceSpeeds') is True:
                    is_common = True
                    break
                else:
                    is_common = False

        if 'new_profile_name' in required_details:
            profile_name = required_details['new_profile_name']
        else:
            profile_name = queuing_profile['current_queuing_profile'][0].get("name")
        if is_common:
            if required_details.get('bandwidth_settings', {}):
                want_bandwidth_settings = {
                    key.upper(): value for key, value in required_details['bandwidth_settings']['bandwidth_percentages'].items()
                }
            else:
                want_bandwidth_settings = {}

            if required_details.get('dscp_settings', {}):
                want_dscp_settings = {
                    key.upper(): value.upper() if isinstance(value, str) else value
                    for key, value in required_details['dscp_settings'].items()
                }

            else:
                want_dscp_settings = {}
            self.log(queuing_profile)
            # Current queuing profile bandwidth and DSCP settings
            have_bandwidth_settings = {}
            have_dscp_settings = {}

            # Loop through each clause to gather bandwidth and DSCP settings
            for clause in queuing_profile.get('current_queuing_profile', [])[0].get('clause', []):
                # If the clause has 'interfaceSpeedBandwidthClauses' field
                if 'interfaceSpeedBandwidthClauses' in clause:
                    for interface_speed_clause in clause['interfaceSpeedBandwidthClauses']:
                        for tc in interface_speed_clause.get('tcBandwidthSettings', []):
                            have_bandwidth_settings[tc['trafficClass']] = tc['bandwidthPercentage']

                # If the clause has 'tcDscpSettings' field
                if 'tcDscpSettings' in clause:
                    for tc in clause.get('tcDscpSettings', []):
                        have_dscp_settings[tc['trafficClass']] = tc['dscp']

            # Initialize final dictionary
            final_want_bandwidth_dict = {}
            self.log(want_bandwidth_settings)
            self.log(have_bandwidth_settings)
            for traffic_class, want_value in want_bandwidth_settings.items():
                # Convert want_value to int for comparison
                want_value = int(want_value)

                if traffic_class in have_bandwidth_settings:
                    have_value = have_bandwidth_settings[traffic_class]
                    # Use the value from want if it exists, otherwise use the one from have
                    final_want_bandwidth_dict[traffic_class] = want_value
                else:
                    # If the traffic class is only in want
                    final_want_bandwidth_dict[traffic_class] = want_value

            # Add the remaining values from have_bandwidth_settings that are not in want_bandwidth_settings
            for traffic_class, have_value in have_bandwidth_settings.items():
                if traffic_class not in final_want_bandwidth_dict:
                    final_want_bandwidth_dict[traffic_class] = have_value

            self.log(have_bandwidth_settings)
            self.log("Final Want bandwidth Dict:")
            self.log(final_want_bandwidth_dict)

            final_want_dscp_dict = {}
            for traffic_class, want_value in want_dscp_settings.items():
                # Convert want_value to int for comparison
                want_value = int(want_value)

                if traffic_class in have_dscp_settings:
                    have_value = have_dscp_settings[traffic_class]
                    # Use the value from want if it exists, otherwise use the one from have
                    final_want_dscp_dict[traffic_class] = want_value
                else:
                    # If the traffic class is only in want
                    final_want_dscp_dict[traffic_class] = want_value

            # Add the remaining values from have_dscp_settings that are not in want_dscp_settings
            for traffic_class, have_value in have_dscp_settings.items():
                if traffic_class not in final_want_dscp_dict:
                    final_want_dscp_dict[traffic_class] = have_value

            # Final result
            self.log("Final Want dscp Dict:")
            self.log(final_want_dscp_dict)

            id_bandwidth_mapping = {}
            id_dscp_mapping = {}

            # Navigate through the queuing profile structure
            current_profiles = queuing_profile.get('current_queuing_profile', [])
            self.log(current_profiles)
            for profile in current_profiles:
                for clause in profile.get('clause', []):
                    if clause.get('type') == 'BANDWIDTH':
                        for interface_clause in clause.get('interfaceSpeedBandwidthClauses', []):
                            for bandwidth_setting in interface_clause.get('tcBandwidthSettings', []):
                                traffic_class = bandwidth_setting.get('trafficClass')
                                instance_id = bandwidth_setting.get('instanceId')
                                if traffic_class and instance_id:
                                    id_bandwidth_mapping[traffic_class] = instance_id
                    elif clause.get('type') == 'DSCP_CUSTOMIZATION':
                        for dscp_setting in clause.get('tcDscpSettings', []):
                            dscp = dscp_setting.get('dscp')
                            traffic_class = dscp_setting.get('trafficClass')
                            instance_id = dscp_setting.get('instanceId')
                            if dscp and traffic_class and instance_id:
                                id_dscp_mapping[traffic_class] = instance_id

            update_required = False

            # Checking Bandwidth settings
            for key, value in final_want_bandwidth_dict.items():
                if key in have_bandwidth_settings:
                    if have_bandwidth_settings[key] != value:
                        update_required = True
                else:
                    update_required = True

            # Checking DSCP settings
            for key, value in final_want_dscp_dict.items():
                if key in have_dscp_settings:
                    if int(have_dscp_settings[key]) != value:
                        update_required = True
                else:
                    update_required = True

            if 'new_profile_name' in required_details:
                profile_name = required_details['new_profile_name']
                update_required = True
            else:
                profile_name = queuing_profile['current_queuing_profile'][0].get("name")

            if 'profile_description' in required_details:
                if queuing_profile['current_queuing_profile'][0].get("description") != required_details['profile_description']:
                    profile_desc = required_details['profile_description']
                    update_required = True
            else:
                profile_desc = queuing_profile['current_queuing_profile'][0].get("description")

            if not update_required:
                self.status = "success"
                self.result['changed'] = False
                self.msg = "application queuing profile '{0}' does not need any update".format(profile_name)
                self.result['msg'] = self.msg
                self.result['response'] = self.msg
                self.log(self.msg, "INFO")
                return self
            else:
                self.log("Update required.")

            instance_ids = {}
            for clause in queuing_profile['current_queuing_profile'][0]['clause']:
                if clause['type'] == 'BANDWIDTH':
                    instance_ids['bandwidth'] = clause['instanceId']
                elif clause['type'] == 'DSCP_CUSTOMIZATION':
                    instance_ids['dscp'] = clause['instanceId']
            self.log(queuing_profile)
            current_queuing_profile = queuing_profile.get('current_queuing_profile')
            if current_queuing_profile and len(current_queuing_profile) > 0:
                clause = current_queuing_profile[0].get('clause')
                if clause and len(clause) > 0:
                    interface_speed_bandwidth_clauses = clause[0].get('interfaceSpeedBandwidthClauses')
                    if interface_speed_bandwidth_clauses and len(interface_speed_bandwidth_clauses) > 0:
                        interface_speed_clause = interface_speed_bandwidth_clauses[0]
                    else:
                        self.log("interfaceSpeedBandwidthClauses is None or empty")
                else:
                    self.log("clause is None or empty")
            else:
                self.log("current_queuing_profile is None or empty")

            if interface_speed_clause['interfaceSpeed'] == 'ALL':
                interface_speed_all_instance_id = interface_speed_clause['instanceId']

            if 'profile_description' in required_details:
                profile_desc = required_details['profile_description']
            else:
                profile_desc = queuing_profile['current_queuing_profile'][0].get("description")

            # Construct the payload
            payload = [
                {
                    "id": queuing_profile['current_queuing_profile'][0].get("id"),
                    "name": profile_name,
                    "description": profile_desc,
                    "clause": [
                        {
                            "instanceId": instance_ids.get('bandwidth'),
                            "type": "BANDWIDTH",
                            "isCommonBetweenAllInterfaceSpeeds": True,
                            "interfaceSpeedBandwidthClauses": [
                                {
                                    "instanceId": interface_speed_all_instance_id,
                                    "interfaceSpeed": "ALL",
                                    "tcBandwidthSettings": [
                                        {
                                            "instanceId": id_bandwidth_mapping[traffic_class],
                                            "trafficClass": traffic_class,
                                            "bandwidthPercentage": final_want_bandwidth_dict[traffic_class]
                                        }
                                        for traffic_class in final_want_bandwidth_dict
                                    ]
                                }
                            ]
                        },
                        {
                            "instanceId": instance_ids.get('dscp'),
                            "type": "DSCP_CUSTOMIZATION",
                            "tcDscpSettings": [
                                {
                                    "instanceId": id_dscp_mapping[traffic_class],
                                    "trafficClass": traffic_class,
                                    "dscp": final_want_dscp_dict[traffic_class]
                                }
                                for traffic_class in final_want_dscp_dict
                            ]
                        }
                    ]
                }
            ]

            self.log(json.dumps(payload, indent=2))

        else:
            want_bandwidth_settings_100_GBPS = None
            want_bandwidth_settings_10_GBPS = None
            want_bandwidth_settings_1_GBPS = None
            want_bandwidth_settings_100_MBPS = None
            want_bandwidth_settings_10_MBPS = None
            want_bandwidth_settings_1_MBPS = None

            if required_details.get('bandwidth_settings', {}):
                for setting in required_details['bandwidth_settings']['interface_speed_settings']:
                    if "HUNDRED_GBPS" in setting['interface_speed']:
                        want_bandwidth_settings_100_GBPS = setting.get("bandwidth_percentages")
                    if "HUNDRED_MBPS" in setting['interface_speed']:
                        want_bandwidth_settings_100_MBPS = setting.get("bandwidth_percentages")
                    if "TEN_GBPS" in setting['interface_speed']:
                        want_bandwidth_settings_10_GBPS = setting.get("bandwidth_percentages")
                    if "TEN_MBPS" in setting['interface_speed']:
                        want_bandwidth_settings_10_MBPS = setting.get("bandwidth_percentages")
                    if "ONE_GBPS" in setting['interface_speed']:
                        want_bandwidth_settings_1_GBPS = setting.get("bandwidth_percentages")
                    if "ONE_MBPS" in setting['interface_speed']:
                        want_bandwidth_settings_1_MBPS = setting.get("bandwidth_percentages")

            have_bandwidth_settings_100_GBPS, have_bandwidth_settings_100_MBPS, have_bandwidth_settings_10_GBPS = {}, {}, {}
            have_bandwidth_settings_10_MBPS, have_bandwidth_settings_1_GBPS, have_bandwidth_settings_1_MBPS = {}, {}, {}

            instance_id_bandwidth_settings_100_GBPS, instance_id_bandwidth_settings_100_MBPS, instance_id_bandwidth_settings_10_GBPS = {}, {}, {}
            instance_id_bandwidth_settings_10_MBPS, instance_id_bandwidth_settings_1_GBPS, instance_id_bandwidth_settings_1_MBPS = {}, {}, {}

            for profile in current_profiles:
                for clause in profile.get('clause', []):
                    for interface_speed_bandwidth_clause in clause.get('interfaceSpeedBandwidthClauses', []):
                        if interface_speed_bandwidth_clause.get("interfaceSpeed") == "HUNDRED_GBPS":
                            for setting in interface_speed_bandwidth_clause['tcBandwidthSettings']:
                                traffic_class = setting['trafficClass'].upper().replace(' ', '_')
                                bandwidth_percentage = str(setting['bandwidthPercentage'])
                                instance_id = (setting['instanceId'])
                                have_bandwidth_settings_100_GBPS[traffic_class] = bandwidth_percentage
                                instance_id_bandwidth_settings_100_GBPS[traffic_class] = instance_id

                        if interface_speed_bandwidth_clause.get("interfaceSpeed") == "HUNDRED_MBPS":
                            for setting in interface_speed_bandwidth_clause['tcBandwidthSettings']:
                                traffic_class = setting['trafficClass'].upper().replace(' ', '_')
                                bandwidth_percentage = str(setting['bandwidthPercentage'])
                                instance_id = (setting['instanceId'])
                                have_bandwidth_settings_100_MBPS[traffic_class] = bandwidth_percentage
                                instance_id_bandwidth_settings_100_MBPS[traffic_class] = instance_id

                        if interface_speed_bandwidth_clause.get("interfaceSpeed") == "TEN_GBPS":
                            for setting in interface_speed_bandwidth_clause['tcBandwidthSettings']:
                                traffic_class = setting['trafficClass'].upper().replace(' ', '_')
                                bandwidth_percentage = str(setting['bandwidthPercentage'])
                                instance_id = (setting['instanceId'])
                                have_bandwidth_settings_10_GBPS[traffic_class] = bandwidth_percentage
                                instance_id_bandwidth_settings_10_GBPS[traffic_class] = instance_id

                        if interface_speed_bandwidth_clause.get("interfaceSpeed") == "TEN_MBPS":
                            for setting in interface_speed_bandwidth_clause['tcBandwidthSettings']:
                                traffic_class = setting['trafficClass'].upper().replace(' ', '_')
                                bandwidth_percentage = str(setting['bandwidthPercentage'])
                                instance_id = (setting['instanceId'])
                                have_bandwidth_settings_10_MBPS[traffic_class] = bandwidth_percentage
                                instance_id_bandwidth_settings_10_MBPS[traffic_class] = instance_id

                        if interface_speed_bandwidth_clause.get("interfaceSpeed") == "ONE_GBPS":
                            for setting in interface_speed_bandwidth_clause['tcBandwidthSettings']:
                                traffic_class = setting['trafficClass'].upper().replace(' ', '_')
                                bandwidth_percentage = str(setting['bandwidthPercentage'])
                                instance_id = (setting['instanceId'])
                                have_bandwidth_settings_1_GBPS[traffic_class] = bandwidth_percentage
                                instance_id_bandwidth_settings_1_GBPS[traffic_class] = instance_id
                        if interface_speed_bandwidth_clause.get("interfaceSpeed") == "ONE_MBPS":
                            for setting in interface_speed_bandwidth_clause['tcBandwidthSettings']:
                                traffic_class = setting['trafficClass'].upper().replace(' ', '_')
                                bandwidth_percentage = str(setting['bandwidthPercentage'])
                                instance_id = (setting['instanceId'])
                                have_bandwidth_settings_1_MBPS[traffic_class] = bandwidth_percentage
                                instance_id_bandwidth_settings_1_MBPS[traffic_class] = instance_id

            final_want_bandwidth_settings_100_GBPS = {}
            final_want_bandwidth_settings_100_MBPS = {}
            final_want_bandwidth_settings_10_GBPS = {}
            final_want_bandwidth_settings_10_MBPS = {}
            final_want_bandwidth_settings_1_GBPS = {}
            final_want_bandwidth_settings_1_MBPS = {}

            for speed, want_bandwidth_settings, have_bandwidth_settings, final_want_bandwidth_settings in [
                ("100_GBPS", want_bandwidth_settings_100_GBPS, have_bandwidth_settings_100_GBPS, final_want_bandwidth_settings_100_GBPS),
                ("100_MBPS", want_bandwidth_settings_100_MBPS, have_bandwidth_settings_100_MBPS, final_want_bandwidth_settings_100_MBPS),
                ("10_GBPS", want_bandwidth_settings_10_GBPS, have_bandwidth_settings_10_GBPS, final_want_bandwidth_settings_10_GBPS),
                ("10_MBPS", want_bandwidth_settings_10_MBPS, have_bandwidth_settings_10_MBPS, final_want_bandwidth_settings_10_MBPS),
                ("1_GBPS", want_bandwidth_settings_1_GBPS, have_bandwidth_settings_1_GBPS, final_want_bandwidth_settings_1_GBPS),
                ("1_MBPS", want_bandwidth_settings_1_MBPS, have_bandwidth_settings_1_MBPS, final_want_bandwidth_settings_1_MBPS)
            ]:
                # Compare and merge `want_bandwidth_settings` and `have_bandwidth_settings`
                want_bandwidth_settings = want_bandwidth_settings or {}
                have_bandwidth_settings = have_bandwidth_settings or {}
                for key, value in want_bandwidth_settings.items():
                    normalized_key = key.upper().replace(' ', '_')  # Normalize key to uppercase with underscores
                    if normalized_key in have_bandwidth_settings:
                        if have_bandwidth_settings[normalized_key] != value:
                            final_want_bandwidth_settings[normalized_key] = value
                        else:
                            final_want_bandwidth_settings[normalized_key] = have_bandwidth_settings[normalized_key]
                    else:
                        final_want_bandwidth_settings[normalized_key] = value

                for key, value in have_bandwidth_settings.items():
                    if key not in final_want_bandwidth_settings:
                        final_want_bandwidth_settings[key] = value

            normalized_have = {k.upper(): v for k, v in have_bandwidth_settings.items()}
            normalized_want = {k.upper(): v for k, v in want_bandwidth_settings.items()}

            self.log(want_bandwidth_settings)
            self.log(have_bandwidth_settings)
            instance_id_bandwidth_settings = {
                "HUNDRED_GBPS": {key: instance_id_bandwidth_settings_100_GBPS.get(key, None) for key in final_want_bandwidth_settings_100_GBPS},
                "HUNDRED_MBPS": {key: instance_id_bandwidth_settings_100_MBPS.get(key, None) for key in final_want_bandwidth_settings_100_MBPS},
                "TEN_GBPS": {key: instance_id_bandwidth_settings_10_GBPS.get(key, None) for key in final_want_bandwidth_settings_10_GBPS},
                "TEN_MBPS": {key: instance_id_bandwidth_settings_10_MBPS.get(key, None) for key in final_want_bandwidth_settings_10_MBPS},
                "ONE_GBPS": {key: instance_id_bandwidth_settings_1_GBPS.get(key, None) for key in final_want_bandwidth_settings_1_GBPS},
                "ONE_MBPS": {key: instance_id_bandwidth_settings_1_MBPS.get(key, None) for key in final_want_bandwidth_settings_1_MBPS}
            }

            final_bandwidth_settings = {
                "HUNDRED_GBPS": final_want_bandwidth_settings_100_GBPS,
                "HUNDRED_MBPS": final_want_bandwidth_settings_100_MBPS,
                "TEN_GBPS": final_want_bandwidth_settings_10_GBPS,
                "TEN_MBPS": final_want_bandwidth_settings_10_MBPS,
                "ONE_GBPS": final_want_bandwidth_settings_1_GBPS,
                "ONE_MBPS": final_want_bandwidth_settings_1_MBPS
            }

            want_dscp_settings = {
                key.upper(): value.upper() if isinstance(value, str) else value
                for key, value in required_details.get('dscp_settings', {}).items()
            }

            # Current DSCP settings from the current profiles
            have_dscp_settings = {
                tc['trafficClass']: tc['dscp']
                for profile in current_profiles
                for clause in profile.get('clause', [])
                if 'tcDscpSettings' in clause
                for tc in clause['tcDscpSettings']
            }
            final_want_dscp_dict = {}
            for traffic_class, want_value in want_dscp_settings.items():
                want_value = int(want_value)
                self.log(want_value)
                if traffic_class in have_dscp_settings:
                    have_value = have_dscp_settings[traffic_class]
                    if want_value == have_value:
                        final_want_dscp_dict[traffic_class] = have_value
                    else:
                        final_want_dscp_dict[traffic_class] = want_value
                else:
                    final_want_dscp_dict[traffic_class] = want_value

            if not want_dscp_settings:
                final_want_dscp_dict = have_dscp_settings

            id_dscp_mapping = {}

            for profile in current_profiles:
                for clause in profile.get('clause', []):
                    if clause.get('type') == 'DSCP_CUSTOMIZATION':
                        for dscp_setting in clause.get('tcDscpSettings', []):
                            dscp = dscp_setting.get('dscp')
                            traffic_class = dscp_setting.get('trafficClass')
                            instance_id = dscp_setting.get('instanceId')
                            if dscp and traffic_class and instance_id:
                                id_dscp_mapping[traffic_class] = instance_id

            dscp_update_required = False

            final_want_dscp_dict_normalized = {key: str(value) for key, value in final_want_dscp_dict.items()}
            have_dscp_settings_normalized = {key: str(value) for key, value in have_dscp_settings.items()}

            if not have_dscp_settings:
                dscp_update_required = False
            elif final_want_dscp_dict_normalized != have_dscp_settings_normalized:
                dscp_update_required = True
            else:
                dscp_update_required = False

            bandwidth_update_required = False

            for speed, final_bandwidth in final_bandwidth_settings.items():
                if speed == 'HUNDRED_GBPS':
                    have_bandwidth = have_bandwidth_settings_100_GBPS
                elif speed == 'HUNDRED_MBPS':
                    have_bandwidth = have_bandwidth_settings_100_MBPS
                elif speed == 'TEN_GBPS':
                    have_bandwidth = have_bandwidth_settings_10_GBPS
                elif speed == 'TEN_MBPS':
                    have_bandwidth = have_bandwidth_settings_10_MBPS
                elif speed == 'ONE_GBPS':
                    have_bandwidth = have_bandwidth_settings_1_GBPS
                elif speed == 'ONE_MBPS':
                    have_bandwidth = have_bandwidth_settings_1_MBPS

                for traffic_class, final_value in final_bandwidth.items():
                    have_value = have_bandwidth.get(traffic_class, None)
                    if have_value != final_value:
                        bandwidth_update_required = True

            update_required = False
            if 'new_profile_name' in required_details:
                profile_name = required_details['new_profile_name']
                update_required = True
            else:
                profile_name = queuing_profile['current_queuing_profile'][0].get("name")

            if 'profile_description' in required_details:
                profile_desc = required_details['profile_description']
                if profile_desc != queuing_profile['current_queuing_profile'][0].get("description"):
                    update_required = True
                    profile_desc = required_details['profile_description']
            else:
                profile_desc = queuing_profile['current_queuing_profile'][0].get("description")

            if not dscp_update_required and not bandwidth_update_required and not update_required:
                self.status = "success"
                self.result['changed'] = False
                self.msg = "application queuing profile '{0}' does not need any update".format(profile_name)
                self.result['msg'] = self.msg
                self.result['response'] = self.msg
                self.log(self.msg, "INFO")
                return self

            # Construct the payload for DSCP customization
            instance_ids = {}
            for profile in current_profiles:
                for clause in profile.get('clause', []):
                    if 'type' in clause and clause['type'] == 'DSCP_CUSTOMIZATION':
                        instance_ids['dscp'] = clause.get('instanceId')
                    if 'interfaceSpeedBandwidthClauses' in clause and clause['interfaceSpeedBandwidthClauses']:
                        instance_ids['bandwidth'] = clause.get('instanceId')

            speed_to_instance_id = {}

            # Loop through the current_profiles to extract the instanceId for each speed
            for profile in current_profiles:
                for clause in profile.get('clause', []):
                    if 'interfaceSpeedBandwidthClauses' in clause:
                        for speed_bandwidth_clause in clause['interfaceSpeedBandwidthClauses']:
                            speed = speed_bandwidth_clause.get('interfaceSpeed')
                            instance_id = speed_bandwidth_clause.get('instanceId')

                            # Store the instanceId in the dictionary with interfaceSpeed as the key
                            if speed and instance_id:
                                speed_to_instance_id[speed] = instance_id

            param = {
                "id": current_profiles[0].get("id"),
                "name": profile_name,
                "description": profile_desc,
                "clause": []
            }

            # Loop through the speeds and bandwidth settings to create the clauses dynamically
            for profile in current_profiles:
                for clause in profile.get('clause', []):
                    if 'interfaceSpeedBandwidthClauses' in clause and clause['interfaceSpeedBandwidthClauses']:

                        params = {
                            "instanceId": instance_ids.get("bandwidth"),
                            "type": "BANDWIDTH",
                            "isCommonBetweenAllInterfaceSpeeds": False,
                            "interfaceSpeedBandwidthClauses": []
                        }
                        param["clause"].append(params)

                        # Loop through the speeds and bandwidth settings for this profile
                        for speed, bandwidth_settings in instance_id_bandwidth_settings.items():
                            clause = {
                                "instanceId": speed_to_instance_id.get(speed) ,
                                "interfaceSpeed": speed,
                                "tcBandwidthSettings": []
                            }

                            for traffic_class, instance_id in bandwidth_settings.items():
                                clause["tcBandwidthSettings"].append({
                                    "trafficClass": traffic_class,
                                    "instanceId": instance_id,
                                    "bandwidthPercentage": final_bandwidth_settings[speed].get(traffic_class, 0)
                                })

                            params["interfaceSpeedBandwidthClauses"].append(clause)

                    if 'tcDscpSettings' in clause and clause['tcDscpSettings']:
                        dscp_clause = {
                            "instanceId": instance_ids.get("dscp"),
                            "type": "DSCP_CUSTOMIZATION",
                            "tcDscpSettings": []
                        }

                        for traffic_class, dscp_value in final_want_dscp_dict.items():
                            dscp_clause["tcDscpSettings"].append({
                                "instanceId": id_dscp_mapping[traffic_class],
                                "trafficClass": traffic_class,
                                "dscp": dscp_value
                            })

                        param["clause"].append(dscp_clause)

                    payload = [param]

            self.log(json.dumps(payload, indent=2))

        try:
            response = self.dnac._exec(
                family="application_policy",
                function='update_application_policy_queuing_profile',
                op_modifies=True,
                params={"payload": payload}
            )

            self.log("Received API response from 'update_application_policy_queuing_profile' for update: {}".format(response), "DEBUG")
            self.check_tasks_response_status(response, "update_application_policy_queuing_profile")

            if self.status not in ["failed", "exited"]:
                self.log("application policy queuing profile '{0}' updated successfully.".format(profile_name), "INFO")
                self.status = "success"
                self.result['changed'] = True
                self.msg = ("application policy queuing profile '{0}' updated successfully.".format(profile_name))
                self.result['response'] = self.msg
                return self

            if self.status == "failed":
                fail_reason = self.msg
                self.status = "failed"
                self.msg = "update of the application policy queuing profile failed due to - {0}".format(fail_reason)
                self.result['response'] = self.msg
                self.log(self.msg, "ERROR")
                self.check_return_status()

        except Exception as e:
            self.status = "failed"
            self.msg = "{0}".format(e)
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

    def create_queuing_profile(self):
        """
        Creates an application queuing profile in Cisco Catalyst Center.
        Description:
            This method validates the provided configuration for creating an application queuing profile. It ensures
            mandatory fields are present and verifies the total bandwidth percentage for different interface speeds.
            The method constructs a payload based on the provided bandwidth and DSCP settings, and invokes the
            appropriate API to create the queuing profile. The result is logged and stored in the instance attributes.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Returns:
            self: The current instance of the class, updated with the result of the create operation. Updates include:
        Raises:
            None: Any errors or unexpected behaviors are handled within the method and logged appropriately.
        """

        new_queuing_profile_details = self.config.get("application_queuing_details", [])[0]
        self.log("Queuing Profile Details: {}".format(new_queuing_profile_details))

        # Check for mandatory fields
        mandatory_fields = ["profile_name"]

        for field in mandatory_fields:
            if not new_queuing_profile_details.get(field):
                self.status = "failed"
                self.msg = (
                    "The following parameter(s): {0} could not be found  and are mandatory to create application queuing profile."
                ).format(field)
                self.log(self.msg, "ERROR")
                self.result['response'] = self.msg
                self.check_return_status()

        if new_queuing_profile_details['bandwidth_settings']['is_common_between_all_interface_speeds'] is False:
            if 'bandwidth_settings' in new_queuing_profile_details:
                for interface in new_queuing_profile_details['bandwidth_settings']['interface_speed_settings']:
                    total_percentage = sum(int(value) for value in interface['bandwidth_percentages'].values())

                    if total_percentage != 100:
                        msg = "Validation ERROR at interface speed:{0} (Total:{1}%) Should be total 100%".format(interface['interface_speed'], total_percentage)
                        self.status = "failed"
                        self.msg = msg
                        self.log(msg, "ERROR")
                        self.result['response'] = self.msg
                        self.check_return_status()

        # Construct payload
        if (
            new_queuing_profile_details.get('bandwidth_settings', {})
            .get('is_common_between_all_interface_speeds') is True
            or new_queuing_profile_details.get('type') == ['dscp']
        ):
            param = {
                "name": new_queuing_profile_details.get('profile_name', ''),
                "description": new_queuing_profile_details.get('profile_description', ''),
                "clause": []
            }

            if new_queuing_profile_details.get('bandwidth_settings'):
                self.log("As we are passing common traffic class bandwidth percentage for all the interface speeds")
                bandwidth_clause = {
                    "type": "BANDWIDTH",
                    "isCommonBetweenAllInterfaceSpeeds": new_queuing_profile_details['bandwidth_settings'].get(
                        'is_common_between_all_interface_speeds', False
                    ),
                    "interfaceSpeedBandwidthClauses": [
                        {
                            "interfaceSpeed": new_queuing_profile_details['bandwidth_settings'].get('interface_speed', ''),
                            "tcBandwidthSettings": [
                                {
                                    "trafficClass": key.upper(),
                                    "bandwidthPercentage": int(value)
                                }
                                for key, value in new_queuing_profile_details['bandwidth_settings']['bandwidth_percentages'].items()
                            ]
                        }
                    ]
                }
                param['clause'].append(bandwidth_clause)

            if new_queuing_profile_details.get('dscp_settings'):
                dscp_clause = {
                    "type": "DSCP_CUSTOMIZATION",
                    "tcDscpSettings": [
                        {
                            "trafficClass": key.upper(),
                            "dscp": value
                        }
                        for key, value in new_queuing_profile_details['dscp_settings'].items()
                    ]
                }
                param['clause'].append(dscp_clause)

        elif new_queuing_profile_details['bandwidth_settings']['is_common_between_all_interface_speeds'] is False:

            self.log("As we are passing different traffic class bandwidth percentage for six different interface speeds")
            param = {
                "name": new_queuing_profile_details['profile_name'],
                "description": new_queuing_profile_details['profile_description'],
                "clause": [
                    {
                        "isCommonBetweenAllInterfaceSpeeds": new_queuing_profile_details['bandwidth_settings']['is_common_between_all_interface_speeds'],
                        "interfaceSpeedBandwidthClauses": []
                    }
                ]
            }

            for interface in new_queuing_profile_details['bandwidth_settings']['interface_speed_settings']:
                # Split the comma-separated interface speeds
                interface_speeds = interface['interface_speed'].split(',')
                for speed in interface_speeds:
                    # Create the interface speed clause
                    interface_speed_clause = {
                        "interfaceSpeed": speed.strip(),
                        "tcBandwidthSettings": [
                            {
                                "trafficClass": key.upper(),
                                "bandwidthPercentage": int(value)
                            }
                            for key, value in interface['bandwidth_percentages'].items()
                        ]
                    }
                    # Append the clause to the main structure
                    param["clause"][0]["interfaceSpeedBandwidthClauses"].append(interface_speed_clause)

            # Add dscp settings if available
            if 'dscp_settings' in new_queuing_profile_details:
                dscp_clause = {
                    "type": "DSCP_CUSTOMIZATION",
                    "tcDscpSettings": [
                        {
                            "trafficClass": key.upper(),
                            "dscp": value
                        }
                        for key, value in new_queuing_profile_details['dscp_settings'].items()
                    ]
                }
                param['clause'].append(dscp_clause)

        self.log("Payload for Queuing Profile: {}".format(json.dumps(param, indent=4)))

        try:
            response = self.dnac._exec(
                family="application_policy",
                function='create_application_policy_queuing_profile',
                op_modifies=True,
                params={"payload": [param]}
            )

            self.log("Received API response from 'create_application_policy_queuing_profile': {}".format(response), "DEBUG")
            self.check_tasks_response_status(response, "create_application_policy_queuing_profile")

            if self.status not in ["failed", "exited"]:
                self.log("application queuing profile created successfully.", "INFO")
                self.status = "success"
                self.result['changed'] = True
                self.msg = ("application queuing profile created successfully.")
                self.result['response'] = self.msg
                return self

            if self.status == "failed":
                fail_reason = self.msg
                self.status = "failed"
                self.msg = (
                    "failed to create application queuing profile reason - {0}").format(fail_reason)
                self.log(self.msg, "ERROR")
                self.result['response'] = self.msg
                self.check_return_status()

        except Exception as e:
            self.status = "failed"
            self.msg = "error occured while creating queuing profile: {0}".format(e)
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

    def get_diff_deleted(self, config):
        """
        Manages the deletion of an application set based on the provided configuration.
        Description:
            This method checks the provided `config` for `application_set_details`. If the details are found, it triggers
            the `delete_application_set` method to delete the application set and subsequently checks the return status
            of the operation.
        Parameters:
            config (dict): A dictionary containing the configuration details, including `application_set_details`.
        Returns:
            None: The method performs the operation but does not return any value.
        Raises:
            None: Any errors or unexpected behaviors are handled internally by the called methods.
        """

        self.config = config

        if config.get("application_set_details"):
            self.delete_application_set().check_return_status()

        if config.get("application_queuing_details"):
            self.delete_application_queuing_profile().check_return_status()

        if config.get("application_details"):
            self.delete_application().check_return_status()

        if config.get("application_policy_details"):
            self.delete_application_policy().check_return_status()

        return self

    def delete_application_policy(self):
        """
        Delete an existing application policy in Cisco DNA Center.

        Parameters:
            self (object): An instance of the class for interacting with Cisco DNA Center.

        Returns:
            self: The updated instance with 'status', 'msg', and 'result' attributes.

        Description:
            This method deletes an application policy from Cisco DNA Center by first checking if the policy exists.
            If the policy is not found, it logs a message and returns. If the policy exists, it retrieves the
            policy ID and sends a delete request to Cisco DNA Center via the API. The response is processed,
            and the method logs success or failure. If an error occurs, it is caught and handled appropriately.
        """

        want_application_policy_details = self.config.get("application_policy_details")
        self.log("Queuing Profile Details: {0}".format(want_application_policy_details))
        application_policy_name = want_application_policy_details.get("name")
        application_policy_details = self.have

        if application_policy_details.get("application_policy_exists") is False:
            self.status = "success"
            self.result['changed'] = False
            self.msg = "application policy '{0}' does not present in the cisco catalyst center or its been already deleted".format(application_policy_name)
            self.result['msg'] = self.msg
            self.result['response'] = self.msg
            self.log(self.msg, "INFO")
            return self

        get_ids = self.have
        ids_list = []
        application_set_names = []
        if not want_application_policy_details.get("application_set_name"):
            if "current_application_policy" in get_ids:
                for policy in get_ids["current_application_policy"]:
                    if "id" in policy:
                        ids_list.append(policy["id"])
        else:
            if "current_application_policy" in get_ids:
                for policy in get_ids["current_application_policy"]:
                    application_set_name = want_application_policy_details.get("application_set_name", [])
                    for app_name in application_set_name:
                        if app_name in policy.get('name', ''):
                            application_set_names.append(app_name)
                            ids_list.append(policy.get('id'))
                            break

            application_set_name_not_available = [
                app_name for app_name in application_set_name
                if app_name not in [name.strip() for name in application_set_names]
            ]

        if want_application_policy_details.get("application_set_name"):
            if not application_set_names:
                self.status = "success"
                self.result['changed'] = False
                self.msg = (
                    "application set(s) '{0}' does not present in the application policy {1} "
                    "or it's been already removed.".format(application_set_name, application_policy_name)
                )
                self.result['msg'] = self.msg
                self.result['response'] = self.msg
                self.log(self.msg, "INFO")
                return self

        try:
            response = self.dnac._exec(
                family="application_policy",
                function='application_policy_intent',
                op_modifies=True,
                params={'deleteList': ids_list, }
            )

            self.log("Received API response from 'application_policy_intent' for deletion: {}".format(response), "DEBUG")
            self.check_tasks_response_status(response, "application_policy_intent")

            if not want_application_policy_details.get("application_set_name"):
                if self.status not in ["failed", "exited"]:
                    self.log("application policy '{0}' deleted successfully.".format(application_policy_name), "INFO")
                    self.status = "success"
                    self.result['changed'] = True
                    self.msg = ("application policy '{0}' deleted successfully.".format(application_policy_name))
                    self.result['response'] = self.msg
                    return self
            else:
                if self.status not in ["failed", "exited"]:
                    self.log(
                        "application set '{0}' has been removed from the application policy {1} successfully. "
                        "and application set - {2} are not present in the policy".format(
                            application_set_name, application_policy_name, application_set_name_not_available
                        ),
                        "INFO"
                    )
                    self.status = "success"
                    self.result['changed'] = True
                    if application_set_name_not_available:
                        self.msg = (
                            "application set '{0}' has been removed from the application policy {1} successfully. "
                            "and application set - {2} are not present in the policy.".format(
                                application_set_names, application_policy_name, application_set_name_not_available))
                    else:
                        self.msg = (
                            "application set '{0}' has been removed from the application policy {1} successfully.".format(
                                application_set_name, application_policy_name))

                    self.result['response'] = self.msg
                    return self

            if self.status == "failed":
                fail_reason = self.msg
                self.status = "failed"
                self.msg = "deletion of the application policy failed due to - {0}".format(fail_reason)
                self.result['response'] = self.msg
                self.log(self.msg, "ERROR")
                self.check_return_status()

        except Exception as e:
            self.status = "failed"
            self.msg = "{0}".format(e)
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

    def delete_application_queuing_profile(self):
        """
        Deletes an existing application set in Cisco Catalyst Center.
        Description:
            This method checks if the specified application set exists in Cisco Catalyst Center. If the application set does
            not exist or has already been deleted, it logs the status and exits without performing any operations. If the
            application set exists, the method retrieves its ID and triggers the appropriate API call to delete it. The
            method monitors the task's response status and logs the outcome.
        Parameters:
            None: The method uses the `config` attribute to retrieve application set details, such as `application_set_name`.
        Returns:
            self: The current instance of the class, updated with the result of the delete operation.
        Raises:
            None: Any errors or unexpected behaviors are handled within the method and logged appropriately.
        """

        application_queuing_profile_details = self.config.get("application_queuing_details", [])[0]
        self.log("Queuing Profile Details: {}".format(application_queuing_profile_details))
        application_queuing_profile_name = application_queuing_profile_details.get("profile_name")
        application_queuing_profile_details = self.have
        self.log(application_queuing_profile_details)

        if application_queuing_profile_details.get("queuing_profile_exists") is False:
            self.status = "success"
            self.result['changed'] = False
            self.msg = (
                "Application queuing profile '{0}' does not present in the Cisco Catalyst Center "
                "or it has already been deleted.".format(application_queuing_profile_name)
            )
            self.result['msg'] = self.msg
            self.result['response'] = self.msg
            self.log(self.msg, "INFO")
            return self

        queuing_profile_id = application_queuing_profile_details.get('current_queuing_profile', [])[0].get('id', None)
        self.log(queuing_profile_id)

        try:
            response = self.dnac._exec(
                family="application_policy",
                function='delete_application_policy_queuing_profile',
                op_modifies=True,
                params={'id': queuing_profile_id, }
            )

            self.log("Received API response from 'delete_application_policy_queuing_profile': {}".format(response), "DEBUG")
            self.check_tasks_response_status(response, "delete_application_policy_queuing_profile")

            if self.status not in ["failed", "exited"]:
                self.log("application policy queuing profile '{0}' deleted successfully.".format(application_queuing_profile_name), "INFO")
                self.status = "success"
                self.result['changed'] = True
                self.msg = ("application policy queuing profile '{0}' deleted successfully.".format(application_queuing_profile_name))
                self.result['response'] = self.msg
                return self

            if self.status == "failed":
                fail_reason = self.msg
                self.status = "failed"
                self.msg = "deletion of the application policy queuing profile failed due to - {0}".format(fail_reason)
                self.result['response'] = self.msg
                self.log(self.msg, "ERROR")
                self.check_return_status()

        except Exception as e:
            self.status = "failed"
            self.msg = "error occured while deleting queuing profile: {0}".format(e)
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

    def delete_application_set(self):
        """
        Deletes an existing application set in Cisco Catalyst Center.
        Description:
            This method checks if the specified application set exists in Cisco Catalyst Center. If the application set does
            not exist or has already been deleted, it logs the status and exits without performing any operations. If the
            application set exists, the method retrieves its ID and triggers the appropriate API call to delete it. The
            method monitors the task's response status and logs the outcome.
        Parameters:
            None: The method uses the `config` attribute to retrieve application set details, such as `application_set_name`.
        Returns:
            self: The current instance of the class, updated with the result of the delete operation.
        Raises:
            None: Any errors or unexpected behaviors are handled within the method and logged appropriately.
        """

        application_set_detail = self.config.get("application_set_details", [])[0]
        self.log("application set details : {0}".format(application_set_detail))
        application_set_name = application_set_detail.get("application_set_name")
        application_set_details = self.have

        if application_set_details.get("application_set_exists") is False:
            self.status = "success"
            self.result['changed'] = False
            self.msg = "application set '{0}' does not present in the cisco catalyst center or its been already deleted".format(application_set_name)
            self.result['msg'] = self.msg
            self.result['response'] = self.msg
            self.log(self.msg, "INFO")
            return self

        application_set_id = application_set_details['current_application_set'][0]['id'] if application_set_details['current_application_set'] else None
        self.log(application_set_id)

        try:
            response = self.dnac._exec(
                family="application_policy",
                function='delete_application_set',
                op_modifies=True,
                params={'id': application_set_id, }
            )

            self.log("Received API response from 'delete_application_set': {}".format(response), "DEBUG")
            self.check_tasks_response_status(response, "delete_application_set")

            if self.status not in ["failed", "exited"]:
                self.log("application set '{0}' deleted successfully.".format(application_set_name), "INFO")
                self.status = "success"
                self.result['changed'] = True
                self.msg = ("application set '{0}' deleted successfully.".format(application_set_name))
                self.result['response'] = self.msg
                return self

            if self.status == "failed":
                fail_reason = self.msg
                self.status = "failed"
                self.msg = "deletion of the application set failed due to - {0}".format(fail_reason)
                self.result['response'] = self.msg
                self.log(self.msg, "ERROR")
                self.check_return_status()

        except Exception as e:
            self.status = "failed"
            self.msg = "error occured while deleting application set: {0}".format(e)
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

    def delete_application(self):
        """
        Deletes an existing application in Cisco Catalyst Center.
        Description:
            This method checks if the specified application exists in Cisco Catalyst Center. If the application
            does not exist or has already been deleted, it logs the status and exits without performing any operations.
            If the application exists, the method retrieves its ID and triggers the appropriate API call to delete it.
            The method monitors the task's response status and logs the outcome.
        Parameters:
            None: The method uses the `config` attribute to retrieve application details, such as `application_name`.
        Returns:
            self: The current instance of the class, updated with the result of the delete operation. Updates include:
        Raises:
            None: Any errors or unexpected behaviors are handled within the method and logged appropriately.
        """

        application_details = self.config.get("application_details", [])
        self.log("application Details: {}".format(application_details))
        application_name = application_details.get("name")
        application_deatils = self.have

        if application_deatils.get("application_exists") is False:
            self.status = "success"
            self.result['changed'] = False
            self.msg = "application '{0}' does not present in the cisco catalyst center or its been already deleted".format(application_name)
            self.result['msg'] = self.msg
            self.result['response'] = self.msg
            self.log(self.msg, "INFO")
            return self

        application_id = application_deatils['current_application'][0]['id'] if application_deatils['current_application'] else None
        self.log(application_id)

        try:
            self.log("outter")
            response = self.dnac._exec(
                family="application_policy",
                function='delete_application_set2',
                op_modifies=True,
                params={'id': application_id, }
            )
            self.log("inner")
            self.log("Received API response from 'delete_application': {}".format(response), "DEBUG")
            self.check_tasks_response_status(response, "delete_application")

            if self.status not in ["failed", "exited"]:
                self.log("application '{0}' deleted successfully.".format(application_name), "INFO")
                self.status = "success"
                self.result['changed'] = True
                self.msg = ("application '{0}' deleted successfully.".format(application_name))
                self.result['response'] = self.msg
                return self

            if self.status == "failed":
                fail_reason = self.msg
                self.status = "failed"
                self.msg = "deletion of the application failed due to - {0}".format(fail_reason)
                self.result['response'] = self.msg
                self.log(self.msg, "ERROR")
                self.check_return_status()

        except Exception as e:
            self.status = "failed"
            self.msg = "error - {0}".format(e)
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

    def verify_diff_merged(self, config):
        """
        Verify the merged status(Addition/Updation) of Devices in Cisco Catalyst Center.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - config (dict): The configuration details to be verified.
        Return:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method checks the merged status of a configuration in Cisco Catalyst Center by retrieving the current state
            (have) and desired state (want) of the configuration, logs the states, and validates whether the specified
            site exists in the Catalyst Center configuration.

            The function performs the following verifications:
            - Checks for devices added to Cisco Catalyst Center and logs the status.
            - Verifies updated device roles and logs the status.
            - Verifies updated interface details and logs the status.
            - Verifies updated device credentials and logs the status.
            - Verifies the creation of a global User Defined Field (UDF) and logs the status.
            - Verifies the provisioning of wired devices and logs the status.
        """
        self.log("verify starts here verify diff merged")

        if self.want.get("application_queuing_details"):
            self.get_have()
            self.log("Current State (have): {0}".format(str(self.have)), "INFO")
            self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

            # Code to validate ccc config for merged state
            application_queuing_profile_exist = self.have.get("queuing_profile_exists")
            application_queuing_profile_name = self.want.get("application_queuing_details", [])[0].get("profile_name")

            if application_queuing_profile_exist:
                self.status = "success"
                self.msg = (
                    "The requested application queuing profile {0} is present in the Cisco Catalyst Center "
                    "and its creation has been verified.".format(application_queuing_profile_name)
                )
                self.log(self.msg, "INFO")
            else:
                self.log("The playbook input for application queuing profile {0} does not align with the Cisco Catalyst Center, indicating that the \
                         merge task may not have executed successfully.".format(application_queuing_profile_name), "INFO")

        if self.want.get("application_details"):
            self.get_have()
            self.log("Current State (have): {0}".format(str(self.have)), "INFO")
            self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

            # Code to validate ccc config for merged state
            application_exists = self.have.get("application_exists")
            application_name = self.want.get("application_details").get("name")

            if application_exists:
                self.status = "success"
                self.msg = "The requested application {0} is present in the Cisco Catalyst Center and its creation has been verified.".format(application_name)
                self.log(self.msg, "INFO")
            else:
                self.log("The playbook input for application {0} does not align with the Cisco Catalyst Center, indicating that the \
                         merge task may not have executed successfully.".format(application_name), "INFO")

            is_application_available = self.have.get("application_exists")

            if is_application_available:
                application_updated = self.is_update_required_for_application()

                if application_updated or self.application_updated:
                    self.log("The update for application {0} has been successfully verified.".format(application_name), "INFO")
                    self.status = "success"

        if self.want.get("application_policy_details"):
            self.get_have()
            self.log("Current State (have): {0}".format(str(self.have)), "INFO")
            self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

            # Code to validate ccc config for merged state
            application_policy_exist = self.have.get("application_policy_exists")
            application_policy_name = self.want.get("application_policy_details").get("name")

            if application_policy_exist:
                self.status = "success"
                self.msg = (
                    "The requested application policy {0} is present in the Cisco Catalyst Center "
                    "and its creation has been verified.".format(application_policy_name)
                )
                self.log(self.msg, "INFO")
            else:
                self.log("The playbook input for application policy {0} does not align with the Cisco Catalyst Center, indicating that the \
                         merge task may not have executed successfully.".format(application_policy_name), "INFO")

        return self

    def verify_diff_deleted(self, config):
        """
        Verify the merged status(Addition/Updation) of Devices in Cisco Catalyst Center.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - config (dict): The configuration details to be verified.
        Return:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method checks the merged status of a configuration in Cisco Catalyst Center by retrieving the current state
            (have) and desired state (want) of the configuration, logs the states, and validates whether the specified
            site exists in the Catalyst Center configuration.

            The function performs the following verifications:
            - Checks for devices added to Cisco Catalyst Center and logs the status.
            - Verifies updated device roles and logs the status.
            - Verifies updated interface details and logs the status.
            - Verifies updated device credentials and logs the status.
            - Verifies the creation of a global User Defined Field (UDF) and logs the status.
            - Verifies the provisioning of wired devices and logs the status.
        """
        self.log("verify starts here verify diff deleted")

        if self.want.get("application_queuing_details"):
            self.get_have()
            self.log("Current State (have): {0}".format(str(self.have)), "INFO")
            self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

            # Code to validate ccc config for merged state
            application_queuing_profile_exist = self.have.get("queuing_profile_exists")
            application_queuing_profile_name = self.want.get("application_queuing_details", [])[0].get("profile_name")

            if not application_queuing_profile_exist:
                self.status = "success"
                self.msg = (
                    "The requested application queuing profile {0} is not present in the Cisco Catalyst Center "
                    "and its deletion has been verified.".format(application_queuing_profile_name)
                )
                self.log(self.msg, "INFO")
            else:
                self.log("The playbook input for application queuing profile {0} does not align with the Cisco Catalyst Center, indicating that the \
                         merge task may not have executed successfully.".format(application_queuing_profile_name), "INFO")

        if self.want.get("application_details"):
            self.get_have()
            self.log("Current State (have): {0}".format(str(self.have)), "INFO")
            self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

            # Code to validate ccc config for merged state
            application_exists = self.have.get("application_exists")
            application_name = self.want.get("application_details").get("name")

            if not application_exists:
                self.status = "success"
                self.msg = (
                    "The requested application {0} is not present in the Cisco Catalyst Center "
                    "and its deletion has been verified.".format(application_name)
                )
                self.log(self.msg, "INFO")
            else:
                self.log("The playbook input for application {0} does not align with the Cisco Catalyst Center, indicating that the \
                         merge task may not have executed successfully.".format(application_name), "INFO")

        if self.want.get("application_policy_details"):
            self.get_have()
            self.log("Current State (have): {0}".format(str(self.have)), "INFO")
            self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

            # Code to validate ccc config for merged state
            application_policy_exist = self.have.get("application_policy_exists")
            application_policy_name = self.want.get("application_policy_details").get("name")

            if not application_policy_exist:
                self.status = "success"
                self.msg = (
                    "The requested application policy {0} is not present in the Cisco Catalyst Center "
                    "and its deletion has been verified.".format(application_policy_name)
                )
                self.log(self.msg, "INFO")
            else:
                self.log("The playbook input for application policy {0} does not align with the Cisco Catalyst Center, indicating that the \
                         merge task may not have executed successfully.".format(application_policy_name), "INFO")
        return self


def main():
    """ main entry point for module execution
    """
    element_spec = {'dnac_host': {'required': True, 'type': 'str'},
                    'dnac_port': {'type': 'str', 'default': '443'},
                    'dnac_username': {'type': 'str', 'default': 'admin', 'aliases': ['user']},
                    'dnac_password': {'type': 'str', 'no_log': True},
                    'dnac_verify': {'type': 'bool', 'default': 'True'},
                    'dnac_version': {'type': 'str', 'default': '2.2.3.3'},
                    'dnac_debug': {'type': 'bool', 'default': False},
                    'dnac_log_level': {'type': 'str', 'default': 'WARNING'},
                    "dnac_log_file_path": {"type": 'str', "default": 'dnac.log'},
                    "dnac_log_append": {"type": 'bool', "default": True},
                    'dnac_log': {'type': 'bool', 'default': False},
                    'validate_response_schema': {'type': 'bool', 'default': True},
                    'config_verify': {'type': 'bool', "default": False},
                    'dnac_api_task_timeout': {'type': 'int', "default": 1200},
                    'dnac_task_poll_interval': {'type': 'int', "default": 2},
                    'config': {'required': True, 'type': 'list', 'elements': 'dict'},
                    'state': {'default': 'merged', 'choices': ['merged', 'deleted']}
                    }

    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=False)
    ccc_application = ApplicationPolicy(module)
    state = ccc_application.params.get("state")

    if state not in ccc_application.supported_states:
        ccc_application.status = "invalid"
        ccc_application.msg = "State {0} is invalid".format(state)
        ccc_application.check_return_status()

    ccc_application.validate_input().check_return_status()
    config_verify = ccc_application.params.get("config_verify")

    for config in ccc_application.validated_config:
        ccc_application.reset_values()
        ccc_application.get_want(config).check_return_status()
        ccc_application.get_have().check_return_status()
        ccc_application.get_diff_state_apply[state](config).check_return_status()
        if config_verify:
            ccc_application.verify_diff_state_apply[state](config).check_return_status()

    module.exit_json(**ccc_application.result)


if __name__ == '__main__':
    main()
