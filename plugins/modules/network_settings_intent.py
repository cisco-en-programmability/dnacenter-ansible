#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2023, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to perform operations on global pool, reserve pool and network in DNAC."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ['Muthu Rakesh, Madhan Sankaranarayanan']

DOCUMENTATION = r"""
---
module: network_settings_intent
short_description: Resource module for IP Address pools and network functions
description:
- Manage operations on Global Pool, Reserve Pool, Network resources.
- API to create/update/delete global pool.
- API to reserve/update/delete an ip subpool from the global pool.
- API to update network settings for DHCP, Syslog, SNMP, NTP, Network AAA, Client and Endpoint AAA,
  and/or DNS center server settings.
version_added: '6.6.0'
extends_documentation_fragment:
  - cisco.dnac.intent_params
author: Muthu Rakesh (@MUTHU-RAKESH-27)
        Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description: The state of Cisco DNA Center after module completion.
    type: str
    choices: [ merged, deleted ]
    default: merged
  config:
    description:
    - List of details of global pool, reserved pool, network being managed.
    type: list
    elements: dict
    required: true
    suboptions:
      GlobalPoolDetails:
        description: Global ip pool manages IPv4 and IPv6 IP pools.
        type: dict
        suboptions:
          settings:
            description: Global Pool's settings.
            type: dict
            suboptions:
              ippool:
                description: Global Pool's ippool.
                elements: dict
                type: list
                suboptions:
                  dhcpServerIps:
                    description: Dhcp Server Ips.
                    elements: str
                    type: list
                  dnsServerIps:
                    description: Dns Server Ips.
                    elements: str
                    type: list
                  gateway:
                    description: Gateway.
                    type: str
                  IpAddressSpace:
                    description: Ip address space.
                    type: str
                  ipPoolCidr:
                    description: Ip pool cidr.
                    type: str
                  prev_name:
                    description: previous name.
                    type: str
                  ipPoolName:
                    description: Ip Pool Name.
                    type: str
      ReservePoolDetails:
        description: Reserving IP subpool from the global pool
        type: dict
        suboptions:
          ipv4DhcpServers:
            description: IPv4 input for dhcp server ip example 1.1.1.1.
            elements: str
            type: list
          ipv4DnsServers:
            description: IPv4 input for dns server ip example 4.4.4.4.
            elements: str
            type: list
          ipv4GateWay:
            description: Gateway ip address details, example 175.175.0.1.
            type: str
            version_added: 4.0.0
          ipv4GlobalPool:
            description: IP v4 Global pool address with cidr, example 175.175.0.0/16.
            type: str
          ipv4Prefix:
            description: ip4 prefix length is enabled or ipv4 total Host input is enabled
            type: bool
          ipv4PrefixLength:
            description: The ipv4 prefix length is required when ipv4prefix value is true.
            type: int
          ipv4Subnet:
            description: IPv4 Subnet address, example 175.175.0.0.
            type: str
          ipv4TotalHost:
            description: IPv4 total host is required when ipv4prefix value is false.
            type: int
          ipv6AddressSpace:
            description: >
              If the value is false only ipv4 input are required, otherwise both
              ipv6 and ipv4 are required.
            type: bool
          ipv6DhcpServers:
            description: IPv6 format dhcp server as input example 2001 db8 1234.
            elements: str
            type: list
          ipv6DnsServers:
            description: IPv6 format dns server input example 2001 db8 1234.
            elements: str
            type: list
          ipv6GateWay:
            description: Gateway ip address details, example 2001 db8 85a3 0 100 1.
            type: str
          ipv6GlobalPool:
            description: >
              IPv6 Global pool address with cidr this is required when Ipv6AddressSpace
              value is true, example 2001 db8 85a3 /64.
            type: str
          ipv6Prefix:
            description: >
              Ipv6 prefix value is true, the ip6 prefix length input field is enabled,
              if it is false ipv6 total Host input is enable.
            type: bool
          ipv6PrefixLength:
            description: IPv6 prefix length is required when the ipv6prefix value is true.
            type: int
          ipv6Subnet:
            description: IPv6 Subnet address, example 2001 db8 85a3 0 100.
            type: str
          ipv6TotalHost:
            description: IPv6 total host is required when ipv6prefix value is false.
            type: int
          name:
            description: Name of the reserve ip sub pool.
            type: str
          prev_name:
            description: Previous name of the reserve ip sub pool.
            type: str
          siteName:
            description: Site name path parameter. Site name to reserve the ip sub pool.
            type: str
          slaacSupport:
            description: Slaac Support.
            type: bool
          type:
            description: Type of the reserve ip sub pool.
            type: str
      NetworkManagementDetails:
        description: Set default network settings for the site
        type: dict
        suboptions:
          settings:
            description: Network management details settings.
            type: dict
            suboptions:
              clientAndEndpoint_aaa:
                description: Network V2's clientAndEndpoint_aaa.
                suboptions:
                  ipAddress:
                    description: IP address for ISE serve (eg 1.1.1.4).
                    type: str
                  network:
                    description: IP address for AAA or ISE server (eg 2.2.2.1).
                    type: str
                  protocol:
                    description: Protocol for AAA or ISE serve (eg RADIUS).
                    type: str
                  servers:
                    description: Server type AAA or ISE server (eg AAA).
                    type: str
                  sharedSecret:
                    description: Shared secret for ISE server.
                    type: str
                type: dict
              dhcpServer:
                description: DHCP Server IP (eg 1.1.1.1).
                elements: str
                type: list
              dnsServer:
                description: Network V2's dnsServer.
                suboptions:
                  domainName:
                    description: Domain Name of DHCP (eg; cisco).
                    type: str
                  primaryIpAddress:
                    description: Primary IP Address for DHCP (eg 2.2.2.2).
                    type: str
                  secondaryIpAddress:
                    description: Secondary IP Address for DHCP (eg 3.3.3.3).
                    type: str
                type: dict
              messageOfTheday:
                description: Network V2's messageOfTheday.
                suboptions:
                  bannerMessage:
                    description: Massage for Banner message (eg; Good day).
                    type: str
                  retainExistingBanner:
                    description: Retain existing Banner Message (eg "true" or "false").
                    type: str
                type: dict
              netflowcollector:
                description: Network V2's netflowcollector.
                suboptions:
                  ipAddress:
                    description: IP Address for NetFlow collector (eg 3.3.3.1).
                    type: str
                  port:
                    description: Port for NetFlow Collector (eg; 443).
                    type: int
                type: dict
              network_aaa:
                description: Network V2's network_aaa.
                suboptions:
                  ipAddress:
                    description: IP address for AAA and ISE server (eg 1.1.1.1).
                    type: str
                  network:
                    description: IP Address for AAA or ISE server (eg 2.2.2.2).
                    type: str
                  protocol:
                    description: Protocol for AAA or ISE serve (eg RADIUS).
                    type: str
                  servers:
                    description: Server type for AAA Network (eg AAA).
                    type: str
                  sharedSecret:
                    description: Shared secret for ISE Server.
                    type: str
                type: dict
              ntpServer:
                description: IP address for NTP server (eg 1.1.1.2).
                elements: str
                type: list
              snmpServer:
                description: Network V2's snmpServer.
                suboptions:
                  configureDnacIP:
                    description: Configuration Cisco DNA Center IP for SNMP Server (eg true).
                    type: bool
                  ipAddresses:
                    description: IP Address for SNMP Server (eg 4.4.4.1).
                    elements: str
                    type: list
                type: dict
              syslogServer:
                description: Network V2's syslogServer.
                suboptions:
                  configureDnacIP:
                    description: Configuration Cisco DNA Center IP for syslog server (eg true).
                    type: bool
                  ipAddresses:
                    description: IP Address for syslog server (eg 4.4.4.4).
                    elements: str
                    type: list
                type: dict
              timezone:
                description: Input for time zone (eg Africa/Abidjan).
                type: str
          siteName:
            description: Site name path parameter.
            type: str
requirements:
- dnacentersdk == 2.4.5
- python >= 3.5
notes:
  - SDK Method used are
    network_settings.NetworkSettings.create_global_pool,
    network_settings.NetworkSettings.delete_global_ip_pool,
    network_settings.NetworkSettings.update_global_pool,
    network_settings.NetworkSettings.release_reserve_ip_subpool,
    network_settings.NetworkSettings.reserve_ip_subpool,
    network_settings.NetworkSettings.update_reserve_ip_subpool,
    network_settings.NetworkSettings.update_network_v2,

  - Paths used are
    post /dna/intent/api/v1/global-pool,
    delete /dna/intent/api/v1/global-pool/{id},
    put /dna/intent/api/v1/global-pool,
    post /dna/intent/api/v1/reserve-ip-subpool/{siteId},
    delete /dna/intent/api/v1/reserve-ip-subpool/{id},
    put /dna/intent/api/v1/reserve-ip-subpool/{siteId},
    put /dna/intent/api/v2/network/{siteId},

"""

EXAMPLES = r"""
- name: Create global pool, reserve an ip pool and network
  cisco.dnac.network_settings_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    state: merged
    config:
    - GlobalPoolDetails:
        settings:
          ippool:
          - ipPoolName: string
            gateway: string
            IpAddressSpace: string
            ipPoolCidr: string
            type: Generic
            dhcpServerIps: list
            dnsServerIps: list
      ReservePoolDetails:
        ipv6AddressSpace: True
        ipv4GlobalPool: string
        ipv4Prefix: True
        ipv4PrefixLength: 9
        ipv4Subnet: string
        name: string
        ipv6Prefix: True
        ipv6PrefixLength: 64
        ipv6GlobalPool: string
        ipv6Subnet: string
        siteName: string
        slaacSupport: True
        type: LAN
      NetworkManagementDetails:
        settings:
          dhcpServer: list
          dnsServer:
            domainName: string
            primaryIpAddress: string
            secondaryIpAddress: string
          clientAndEndpoint_aaa:
            network: string
            protocol: string
            servers: string
          messageOfTheday:
            bannerMessage: string
            retainExistingBanner: string
          netflowcollector:
            ipAddress: string
            port: 443
          network_aaa:
            network: string
            protocol: string
            servers: string
          ntpServer: list
          snmpServer:
            configureDnacIP: True
            ipAddresses: list
          syslogServer:
            configureDnacIP: True
            ipAddresses: list
        siteName: string
"""

RETURN = r"""
# Case_1: Successful creation/updation/deletion of global pool
response_1:
  description: A dictionary or list with the response returned by the Cisco DNA Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }

# Case_2: Successful creation/updation/deletion of reserve pool
response_2:
  description: A dictionary or list with the response returned by the Cisco DNA Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }

# Case_3: Successful creation/updation of network
response_3:
  description: A dictionary or list with the response returned by the Cisco DNA Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""

import copy
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    get_dict_result,
    dnac_compare_equality,
)


class DnacNetwork(DnacBase):
    """Class containing member attributes for network intent module"""

    def __init__(self, module):
        super().__init__(module)
        self.result["response"] = [
            {"globalPool": {"response": {}, "msg": {}}},
            {"reservePool": {"response": {}, "msg": {}}},
            {"network": {"response": {}, "msg": {}}}
        ]

    def validate_input(self):
        """
        Checks if the configuration parameters provided in the playbook
        meet the expected structure and data types,
        as defined in the 'temp_spec' dictionary.
        Parameters:
          - self: The instance of the class containing the 'config' attribute
        Returns:
          The method returns an instance of the class with updated attributes:
          - self.msg: A message describing the validation result.
          - self.status: The status of the validation (either 'success' or 'failed').
        """

        if not self.config:
            self.msg = "config not available in playbook for validation"
            self.status = "success"
            return self

        # temp_spec is the specification for the expected structure of configuration parameters
        temp_spec = {
            "GlobalPoolDetails": {
                "type": 'dict',
                "settings": {
                    "type": 'dict',
                    "ippool": {
                        "type": 'list',
                        "IpAddressSpace": {"type": 'string'},
                        "dhcpServerIps": {"type": 'list'},
                        "dnsServerIps": {"type": 'list'},
                        "gateway": {"type": 'string'},
                        "ipPoolCidr": {"type": 'string'},
                        "ipPoolName": {"type": 'string'},
                        "prevName": {"type": 'string'},
                    }
                }
            },
            "ReservePoolDetails": {
                "type": 'dict',
                "name": {"type": 'string'},
                "prevName": {"type": 'string'},
                "ipv6AddressSpace": {"type": 'bool'},
                "ipv4GlobalPool": {"type": 'string'},
                "ipv4Prefix": {"type": 'bool'},
                "ipv4PrefixLength": {"type": 'string'},
                "ipv4Subnet": {"type": 'string'},
                "ipv4GateWay": {"type": 'string'},
                "ipv4DhcpServers": {"type": 'list'},
                "ipv4DnsServers": {"type": 'list'},
                "ipv6GlobalPool": {"type": 'string'},
                "ipv6Prefix": {"type": 'bool'},
                "ipv6PrefixLength": {"type": 'integer'},
                "ipv6Subnet": {"type": 'string'},
                "ipv6GateWay": {"type": 'string'},
                "ipv6DhcpServers": {"type": 'list'},
                "ipv6DnsServers": {"type": 'list'},
                "ipv4TotalHost": {"type": 'integer'},
                "ipv6TotalHost": {"type": 'integer'},
                "slaacSupport": {"type": 'bool'},
                "siteName": {"type": 'string'},
            },
            "NetworkManagementDetails": {
                "type": 'dict',
                "settings": {
                    "type": 'dict',
                    "dhcpServer": {"type": 'list'},
                    "dnsServer": {
                        "type": 'dict',
                        "domainName": {"type": 'string'},
                        "primaryIpAddress": {"type": 'string'},
                        "secondaryIpAddress": {"type": 'string'}
                    },
                    "syslogServer": {
                        "type": 'dict',
                        "ipAddresses": {"type": 'list'},
                        "configureDnacIP": {"type": 'bool'}
                    },
                    "snmpServer": {
                        "type": 'dict',
                        "ipAddresses": {"type": 'list'},
                        "configureDnacIP": {"type": 'bool'}
                    },
                    "netflowcollector": {
                        "type": 'dict',
                        "ipAddress": {"type": 'string'},
                        "port": {"type": 'integer'},
                    },
                    "timezone": {"type": 'string'},
                    "ntpServer": {"type": 'list'},
                    "messageOfTheday": {
                        "type": 'dict',
                        "bannerMessage": {"type": 'string'},
                        "retainExistingBanner": {"type": 'bool'},
                    },
                    "network_aaa": {
                        "type": 'dict',
                        "servers": {"type": 'string', "choices": ["ISE", "AAA"]},
                        "ipAddress": {"type": 'string'},
                        "network": {"type": 'string'},
                        "protocol": {"type": 'string', "choices": ["RADIUS", "TACACS"]},
                        "sharedSecret": {"type": 'string'}

                    },
                    "clientAndEndpoint_aaa": {
                        "type": 'dict',
                        "servers": {"type": 'string', "choices": ["ISE", "AAA"]},
                        "ipAddress": {"type": 'string'},
                        "network": {"type": 'string'},
                        "protocol": {"type": 'string', "choices": ["RADIUS", "TACACS"]},
                        "sharedSecret": {"type": 'string'}
                    }
                },
                "siteName": {"type": 'string'},
            }
        }

        # Validate playbook params against the specification (temp_spec)
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)
        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format("\n".join(invalid_params))
            self.status = "failed"
            return self

        self.validated_config = valid_temp
        self.log(str(valid_temp))
        self.msg = "Successfully validated input from the playbook"
        self.status = "success"
        return self

    def requires_update(self, have, want, obj_params):
        """
        Check if the template config given requires update by comparing
        current information wih the requested information.

        This method compares the current global pool, reserve pool,
        or network details from Cisco DNA Center with the user-provided details
        from the playbook, using a specified schema for comparison.

        Parameters:
          - self: The instance of the class containing the 'config' attribute
          - have (dict): Current information from the Cisco DNA Center
                          (global pool, reserve pool, network details)
          - want (dict): Users provided information from the playbook
          - obj_params (list of tuples): A list of parameter mappings
                  specifying which Cisco DNA Center parameters (dnac_param)
                  correspond to the user-provided parameters (ansible_param).
        Returns:
          -  bool: True if any parameter specified in obj_params differs
                   between current_obj and requested_obj, indicating that an
                   update is required.
                   False if all specified parameters are equal.
        """

        current_obj = have
        requested_obj = want
        self.log(str(current_obj))
        self.log(str(requested_obj))

        return any(not dnac_compare_equality(current_obj.get(dnac_param),
                                             requested_obj.get(ansible_param))
                   for (dnac_param, ansible_param) in obj_params)

    def get_site_id(self, site_name):
        """
        Get the site id from the site name.
        Use check_return_status() to check for failure.

        Parameters:
          - site_name (str): Site name
        Returns:
          - str or None - The Site Id if found, or None if not found or error
        """

        try:
            response = self.dnac._exec(
                family="sites",
                function='get_site',
                params={"name": site_name},
            )
            self.log(str(response))
            if not response:
                self.log("Failed to get the site id from site name {0}".format(site_name))
                return None

            _id = response.get("response")[0].get("id")
            self.log(str(_id))
        except Exception as e:
            self.log("Error while getting site_id from the site_name")
            return None

        return _id

    def get_global_pool_params(self, pool_info):
        """
        Process Global Pool params from playbook data for Global Pool config
        in Cisco DNA Center

        Parameters:
          - pool_info (dict): Playbook data containing information about
                              the global pool
        Returns:
          - dict or None: Processed Global Pool data in a format suitable
                          for Cisco DNA Center configuration, or None
                          if pool_info is empty.
        """

        if not pool_info:
            self.log("Global Pool is empty")
            return None

        self.log(str(pool_info))
        global_pool = {
            "settings": {
                "ippool": [{
                    "dhcpServerIps": pool_info.get("dhcpServerIps"),
                    "dnsServerIps": pool_info.get("dnsServerIps"),
                    "ipPoolCidr": pool_info.get("ipPoolCidr"),
                    "ipPoolName": pool_info.get("ipPoolName"),
                    "type": pool_info.get("type")
                }]
            }
        }
        self.log(str(global_pool))
        global_ippool = global_pool.get("settings").get("ippool")[0]
        if pool_info.get("ipv6") is False:
            global_ippool.update({"IpAddressSpace": "IPv4"})
        else:
            global_ippool.update({"IpAddressSpace": "IPv6"})

        self.log(str(global_ippool.get("IpAddressSpace")))
        if not pool_info["gateways"]:
            global_ippool.update({"gateway": ""})
        else:
            global_ippool.update({"gateway": pool_info.get("gateways")[0]})

        return global_pool

    def get_reserve_pool_params(self, pool_info):
        """
        Process Reserved Pool parameters from playbook data
        for Reserved Pool configuration in Cisco DNA Center.

        Parameters:
          - pool_info (dict): Playbook data containing information about
                              the reserved pool.

        Returns:
          - reserve_pool (dict): Processed Reserved pool data in the format
                                 suitable for the Cisco DNA Center config.
        """

        reserve_pool = {
            "name": pool_info.get("groupName"),
            "site_id": pool_info.get("siteId"),
        }
        if len(pool_info.get("ipPools")) == 1:
            reserve_pool.update({
                "ipv4DhcpServers": pool_info.get("ipPools")[0].get("dhcpServerIps"),
                "ipv4DnsServers": pool_info.get("ipPools")[0].get("dnsServerIps"),
                "ipv6AddressSpace": "False"
            })
            if pool_info.get("ipPools")[0].get("gateways") != []:
                reserve_pool.update({"ipv4GateWay": pool_info.get("ipPools")[0].get("gateways")[0]})
            else:
                reserve_pool.update({"ipv4GateWay": ""})
            reserve_pool.update({"ipv6AddressSpace": "False"})
        elif len(pool_info.get("ipPools")) == 2:
            if not pool_info.get("ipPools")[0].get("ipv6"):
                reserve_pool.update({
                    "ipv4DhcpServers": pool_info.get("ipPools")[0].get("dhcpServerIps"),
                    "ipv4DnsServers": pool_info.get("ipPools")[0].get("dnsServerIps"),
                    "ipv6AddressSpace": "True",
                    "ipv6DhcpServers": pool_info.get("ipPools")[1].get("dhcpServerIps"),
                    "ipv6DnsServers": pool_info.get("ipPools")[1].get("dnsServerIps"),

                })

                if pool_info.get("ipPools")[0].get("gateways") != []:
                    reserve_pool.update({"ipv4GateWay":
                                        pool_info.get("ipPools")[0].get("gateways")[0]})
                else:
                    reserve_pool.update({"ipv4GateWay": ""})

                if pool_info.get("ipPools")[1].get("gateways") != []:
                    reserve_pool.update({"ipv6GateWay":
                                         pool_info.get("ipPools")[1].get("gateways")[0]})
                else:
                    reserve_pool.update({"ipv4GateWay": ""})

            elif not pool_info.get("ipPools")[1].get("ipv6"):
                reserve_pool.update({
                    "ipv4DhcpServers": pool_info.get("ipPools")[1].get("dhcpServerIps"),
                    "ipv4DnsServers": pool_info.get("ipPools")[1].get("dnsServerIps"),
                    "ipv6AddressSpace": "True",
                    "ipv6DnsServers": pool_info.get("ipPools")[0].get("dnsServerIps"),
                    "ipv6DhcpServers": pool_info.get("ipPools")[0].get("dhcpServerIps")
                })
                if pool_info.get("ipPools")[1].get("gateways") != []:
                    reserve_pool.update({"ipv4GateWay":
                                        pool_info.get("ipPools")[1].get("gateways")[0]})
                else:
                    reserve_pool.update({"ipv4GateWay": ""})

                if pool_info.get("ipPools")[0].get("gateways") != []:
                    reserve_pool.update({"ipv6GateWay":
                                         pool_info.get("ipPools")[0].get("gateways")[0]})
                else:
                    reserve_pool.update({"ipv4GateWay": ""})
        reserve_pool.update({"slaacSupport": True})
        self.log(str(reserve_pool))
        return reserve_pool

    def get_network_params(self, site_id):
        """
        Process the Network parameters from the playbook
        for Network configuration in Cisco DNA Center

        Parameters:
          - site_id (str): The Site ID for which network parameters
                           are requested.

        Returns:
          - dict or None: Processed Network data in a format suitable for
                          Cisco DNA Center configuration, or None if the
                          response is not a dictionary or there was an error.
        """

        response = self.dnac._exec(
            family="network_settings",
            function='get_network',
            params={"site_id": site_id}
        )
        self.log(str(response))
        if not isinstance(response, dict):
            self.log("Error in getting network details - Response is not a dictionary")
            return None

        # Extract various network-related details from the response
        all_network_details = response.get("response")
        dhcp_details = get_dict_result(all_network_details, "key", "dhcp.server")
        dns_details = get_dict_result(all_network_details, "key", "dns.server")
        snmp_details = get_dict_result(all_network_details, "key", "snmp.trap.receiver")
        syslog_details = get_dict_result(all_network_details, "key", "syslog.server")
        netflow_details = get_dict_result(all_network_details, "key", "netflow.collector")
        ntpserver_details = get_dict_result(all_network_details, "key", "ntp.server")
        timezone_details = get_dict_result(all_network_details, "key", "timezone.site")
        messageoftheday_details = get_dict_result(all_network_details, "key", "banner.setting")
        network_aaa = get_dict_result(all_network_details, "key", "aaa.network.server.1")
        network_aaa_pan = get_dict_result(all_network_details, "key", "aaa.server.pan.network")
        clientAndEndpoint_aaa = get_dict_result(all_network_details, "key", "aaa.endpoint.server.1")
        clientAndEndpoint_aaa_pan = \
            get_dict_result(all_network_details, "key", "aaa.server.pan.endpoint")

        # Prepare the network details for Cisco DNA Center configuration
        network_details = {
            "settings": {
                "snmpServer": {
                    "configureDnacIP": snmp_details.get("value")[0].get("configureDnacIP"),
                    "ipAddresses": snmp_details.get("value")[0].get("ipAddresses"),
                },
                "syslogServer": {
                    "configureDnacIP": syslog_details.get("value")[0].get("configureDnacIP"),
                    "ipAddresses": syslog_details.get("value")[0].get("ipAddresses"),
                },
                "netflowcollector": {
                    "ipAddress": netflow_details.get("value")[0].get("ipAddress"),
                    "port": netflow_details.get("value")[0].get("port"),
                    "configureDnacIP": netflow_details.get("value")[0].get("configureDnacIP"),
                },
                "timezone": timezone_details.get("value")[0],
            }
        }
        network_settings = network_details.get("settings")
        if dhcp_details is not None:
            network_settings.update({"dhcpServer": dhcp_details.get("value")})

        if dns_details is not None:
            network_settings.update({
                "dnsServer": {
                    "domainName": dns_details.get("value")[0].get("domainName"),
                    "primaryIpAddress": dns_details.get("value")[0].get("primaryIpAddress"),
                    "secondaryIpAddress": dns_details.get("value")[0].get("secondaryIpAddress")
                }
            })

        if ntpserver_details is not None:
            network_settings.update({"ntpServer": ntpserver_details.get("value")})

        if messageoftheday_details is not None:
            network_settings.update({
                "messageOfTheday": {
                    "bannerMessage": messageoftheday_details.get("value")[0].get("bannerMessage"),
                    "retainExistingBanner":
                    messageoftheday_details.get("value")[0].get("retainExistingBanner"),
                }
            })

        if network_aaa and network_aaa_pan:
            network_settings.update({
                "network_aaa": {
                    "network": network_aaa.get("value")[0].get("ipAddress"),
                    "protocol": network_aaa.get("value")[0].get("protocol"),
                    "ipAddress": network_aaa_pan.get("value")[0]
                }
            })

        if clientAndEndpoint_aaa and clientAndEndpoint_aaa_pan:
            network_settings.update({
                "clientAndEndpoint_aaa": {
                    "network": clientAndEndpoint_aaa.get("value")[0].get("ipAddress"),
                    "protocol": clientAndEndpoint_aaa.get("value")[0].get("protocol"),
                    "ipAddress": clientAndEndpoint_aaa_pan.get("value")[0],
                }
            })
        self.log(str(network_details))
        return network_details

    def global_pool_exists(self, name):
        """
        Check if the Global Pool with the given name exists

        Parameters:
          - name (str): The name of the Global Pool to check for existence
        Returns:
          dict: A dictionary containing information about the
                Global Pool's existence:
          - 'exists' (bool): True if Global Pool exists, otherwise False.
          - 'id' (str): ID of the Global Pool if exists, otherwise None
          - 'details' (dict): Details of Global Pool if exists, otherwise None.
        """

        global_pool = {
            "exists": False,
            "details": None,
            "id": None
        }
        response = self.dnac._exec(
            family="network_settings",
            function="get_global_pool",
        )
        if not isinstance(response, dict):
            self.log("Error in getting global pool - Response is not a dictionary")
            return global_pool

        all_global_pool_details = response.get("response")
        global_pool_details = get_dict_result(all_global_pool_details, "ipPoolName", name)
        self.log("Global Ippool Name : " + str(name))
        self.log(str(global_pool_details))
        if not global_pool_details:
            self.log("Global pool {0} does not exist".format(name))
            return global_pool
        global_pool.update({"exists": True})
        global_pool.update({"id": global_pool_details.get("id")})
        global_pool["details"] = self.get_global_pool_params(global_pool_details)

        self.log(str(global_pool))
        return global_pool

    def reserve_pool_exists(self, name, site_name):
        """
        Check if the Reserved pool with the given name exists in a specific site
        Use check_return_status() to check for failure

        Parameters:
          - name (str): Name of the Reserved pool to check for existence.
          - site_name (str): Name of the site where Reserved pool is located.

        Returns:
            dict - Dictionary containing information about the
                   Reserved pool's existence:
            - 'exists' (bool): True if the Reserved pool exists in the specified
                               site, otherwise False.
            - 'id' (str or None): ID of the Reserved pool if it exists, or
                                  None if it doesn't.
            - 'details' (dict or None): Details of the Reserved pool if exists,
                                  or else None.
        """

        reserve_pool = {
            "exists": False,
            "details": None,
            "id": None,
            "success": True
        }
        site_id = self.get_site_id(site_name)
        self.log(str(site_id))
        if not site_id:
            reserve_pool.update({"success": False})
            self.msg = "Failed to get the site id from the site name {0}".format(site_name)
            self.status = "failed"
            return reserve_pool

        response = self.dnac._exec(
            family="network_settings",
            function="get_reserve_ip_subpool",
            params={"siteId": site_id}
        )
        if not isinstance(response, dict):
            reserve_pool.update({"success": False})
            self.msg = "Error in getting reserve pool - Response is not a dictionary"
            self.status = "exited"
            return reserve_pool

        all_reserve_pool_details = response.get("response")
        reserve_pool_details = get_dict_result(all_reserve_pool_details, "groupName", name)
        if not reserve_pool_details:
            self.log("Reserve pool {0} does not exist in the site {1}".format(name, site_name))
            return reserve_pool

        reserve_pool.update({"exists": True})
        reserve_pool.update({"id": reserve_pool_details.get("id")})
        reserve_pool.update({"details": self.get_reserve_pool_params(reserve_pool_details)})

        self.log("Reserved Pool Details " + str(reserve_pool.get("details")))
        self.log("Reserved Pool Id " + str(reserve_pool.get("id")))
        return reserve_pool

    def get_have_global_pool(self, config):
        """
        Get the current Global Pool information from
        Cisco DNA Center based on the provided playbook details.
        check this API using check_return_status.

        Parameters:
          - config (dict): Playbook details containing Global Pool config.
        Returns:
            self - The current object with updated information.
        """

        global_pool = {
            "exists": False,
            "details": None,
            "id": None
        }
        global_pool_settings = config.get("GlobalPoolDetails").get("settings")
        if global_pool_settings is None:
            self.msg = "settings in GlobalPoolDetails is missing in the playbook"
            self.status = "failed"
            return self

        global_pool_ippool = global_pool_settings.get("ippool")
        if global_pool_ippool is None:
            self.msg = "ippool in GlobalPoolDetails is missing in the playbook"
            self.status = "failed"
            return self

        name = global_pool_ippool[0].get("ipPoolName")
        if name is None:
            self.msg = "Mandatory Parameter ipPoolName required"
            self.status = "failed"
            return self

        # If the Global Pool doesn't exist and a previous name is provided
        # Else try using the previous name
        global_pool = self.global_pool_exists(name)
        self.log(str(global_pool))
        prev_name = global_pool_ippool[0].get("prev_name")
        if global_pool.get("exists") is False and \
                prev_name is not None:
            global_pool = self.global_pool_exists(prev_name)
            if global_pool.get("exists") is False:
                self.msg = "Prev name {0} doesn't exist in GlobalPoolDetails".format(prev_name)
                self.status = "failed"
                return self

        self.log("pool Exists: " + str(global_pool.get("exists")) +
                 "\n Current Site: " + str(global_pool.get("details")))
        self.have.update({"globalPool": global_pool})
        self.msg = "Collecting the global pool details from the Cisco DNA Center"
        self.status = "success"
        return self

    def get_have_reserve_pool(self, config):
        """
        Get the current Reserved Pool information from Cisco DNA Center
        based on the provided playbook details.
        Check this API using check_return_status

        Parameters:
          - config (list of dict): Playbook details containing Reserved Pool
                                   configuration.
        Returns:
            self - The current object with updated information.
        """

        reserve_pool = {
            "exists": False,
            "details": None,
            "id": None
        }
        reserve_pool_details = config.get("ReservePoolDetails")
        name = reserve_pool_details.get("name")
        if name is None:
            self.msg = "Mandatory Parameter name required in ReservePoolDetails\n"
            self.status = "failed"
            return self

        site_name = reserve_pool_details.get("siteName")
        self.log(str(site_name))
        if site_name is None:
            self.msg = "Missing parameter 'siteName' in ReservePoolDetails"
            self.status = "failed"
            return self

        # Check if the Reserved Pool exists in Cisco DNA Center
        # based on the provided name and site name
        reserve_pool = self.reserve_pool_exists(name, site_name)
        if not reserve_pool.get("success"):
            return self.check_return_status()
        self.log(str(reserve_pool))

        # If the Reserved Pool doesn't exist and a previous name is provided
        # Else try using the previous name
        prev_name = reserve_pool_details.get("prev_name")
        if reserve_pool.get("exists") is False and \
                prev_name is not None:
            reserve_pool = self.reserve_pool_exists(prev_name, site_name)
            if not reserve_pool.get("success"):
                return self.check_return_status()

            # If the previous name doesn't exist in Cisco DNA Center, return with error
            if reserve_pool.get("exists") is False:
                self.msg = "Prev name {0} doesn't exist in ReservePoolDetails".format(prev_name)
                self.status = "failed"
                return self

        self.log("Reservation Exists: " + str(reserve_pool.get("exists")) +
                 "\n Reserved Pool: " + str(reserve_pool.get("details")))

        # If reserve pool exist, convert ipv6AddressSpace to the required format (boolean)
        if reserve_pool.get("exists"):
            reserve_pool_details = reserve_pool.get("details")
            if reserve_pool_details.get("ipv6AddressSpace") == "False":
                reserve_pool_details.update({"ipv6AddressSpace": False})
            else:
                reserve_pool_details.update({"ipv6AddressSpace": True})

        self.log(str(reserve_pool))
        self.have.update({"reservePool": reserve_pool})
        self.msg = "Collecting the reserve pool details from the Cisco DNA Center"
        self.status = "success"
        return self

    def get_have_network(self, config):
        """
        Get the current Network details from Cisco DNA
        Center based on the provided playbook details.

        Parameters:
            config (dict) - Playbook details containing Network Management
                            configuration.
        Returns:
            self - The current object with updated Network information.
        """
        network = {}
        site_name = config.get("NetworkManagementDetails").get("siteName")
        if site_name is None:
            self.msg = "Mandatory Parameter 'siteName' missing"
            self.status = "failed"
            return self

        site_id = self.get_site_id(site_name)
        if site_id is None:
            self.msg = "Failed to get site id from {0}".format(site_name)
            self.status = "failed"
            return self

        network["site_id"] = site_id
        network["net_details"] = self.get_network_params(site_id)
        self.log("Network Details from the Cisco DNA Center " + str(network))
        self.have.update({"network": network})
        self.msg = "Collecting the network details from the Cisco DNA Center"
        self.status = "success"
        return self

    def get_have(self, config):
        """
        Get the current Global Pool Reserved Pool and Network details
        from Cisco DNA Center

        Parameters:
          - config (dict): Playbook details containing Global Pool, Reserved
                           Pool, and Network Management configuration.

        Returns:
          - self: The current object with updated Global Pool,
                  Reserved Pool, and Network information.
        """

        if config.get("GlobalPoolDetails") is not None:
            self.get_have_global_pool(config).check_return_status()

        if config.get("ReservePoolDetails") is not None:
            self.get_have_reserve_pool(config).check_return_status()

        if config.get("NetworkManagementDetails") is not None:
            self.get_have_network(config).check_return_status()

        self.log("Global Pool, Reserve Pool, Network Details in Cisco DNA Center " + str(self.have))
        self.msg = "Successfully retrieved the details from the Cisco DNA Center"
        self.status = "success"
        return self

    def get_want_global_pool(self, global_ippool):
        """
        Get all the Global Pool information from playbook
        Set the status and the msg before returning from the API
        Check the return value of the API with check_return_status()

        Parameters:
          - global_ippool (dict): Playbook global pool details containing
                        IpAddressSpace, DHCP server IPs, DNS server IPs,
                        IP pool name, IP pool CIDR, gateway, and type.

        Returns:
          - self: Current object with updated desired Global Pool information.
        """

        # Initialize the desired Global Pool configuration
        want_global = {
            "settings": {
                "ippool": [{
                    "IpAddressSpace": global_ippool.get("IpAddressSpace"),
                    "dhcpServerIps": global_ippool.get("dhcpServerIps"),
                    "dnsServerIps": global_ippool.get("dnsServerIps"),
                    "ipPoolName": global_ippool.get("ipPoolName"),
                    "ipPoolCidr": global_ippool.get("ipPoolCidr"),
                    "gateway": global_ippool.get("gateway"),
                    "type": global_ippool.get("type"),
                }]
            }
        }
        want_ippool = want_global.get("settings").get("ippool")[0]

        # Converting to the required format based on the existing Global Pool
        if not self.have.get("globalPool").get("exists"):
            if want_ippool.get("dhcpServerIps") is None:
                want_ippool.update({"dhcpServerIps": []})
            if want_ippool.get("dnsServerIps") is None:
                want_ippool.update({"dnsServerIps": []})
            if want_ippool.get("IpAddressSpace") is None:
                want_ippool.update({"IpAddressSpace": ""})
            if want_ippool.get("gateway") is None:
                want_ippool.update({"gateway": ""})
            if want_ippool.get("type") is None:
                want_ippool.update({"type": "Generic"})
        else:
            have_ippool = self.have.get("globalPool").get("details") \
                .get("settings").get("ippool")[0]

            # Copy existing Global Pool information if the desired configuration is not provided
            want_ippool.update({
                "IpAddressSpace": have_ippool.get("IpAddressSpace"),
                "type": have_ippool.get("ipPoolType"),
                "ipPoolCidr": have_ippool.get("ipPoolCidr")
            })
            want_ippool.update({})
            want_ippool.update({})

            for key in ["dhcpServerIps", "dnsServerIps", "gateway"]:
                if want_ippool.get(key) is None and have_ippool.get(key) is not None:
                    want_ippool[key] = have_ippool[key]

        self.log("Global Pool Playbook Details " + str(want_global))
        self.want.update({"wantGlobal": want_global})
        self.msg = "Collecting the global pool details from the playbook"
        self.status = "success"
        return self

    def get_want_reserve_pool(self, reserve_pool):
        """
        Get all the Reserved Pool information from playbook
        Set the status and the msg before returning from the API
        Check the return value of the API with check_return_status()

        Parameters:
         - reserve_pool (dict) - Playbook reserved pool details
                     containing various properties.

        Returns:
          - self: The current object with updated desired Reserved
                  Pool information.
        """

        want_reserve = {
            "name": reserve_pool.get("name"),
            "type": reserve_pool.get("type"),
            "ipv6AddressSpace": reserve_pool.get("ipv6AddressSpace"),
            "ipv4GlobalPool": reserve_pool.get("ipv4GlobalPool"),
            "ipv4Prefix": reserve_pool.get("ipv4Prefix"),
            "ipv4PrefixLength": reserve_pool.get("ipv4PrefixLength"),
            "ipv4GateWay": reserve_pool.get("ipv4GateWay"),
            "ipv4DhcpServers": reserve_pool.get("ipv4DhcpServers"),
            "ipv4DnsServers": reserve_pool.get("ipv4DnsServers"),
            "ipv4Subnet": reserve_pool.get("ipv4Subnet"),
            "ipv6GlobalPool": reserve_pool.get("ipv6GlobalPool"),
            "ipv6Prefix": reserve_pool.get("ipv6Prefix"),
            "ipv6PrefixLength": reserve_pool.get("ipv6PrefixLength"),
            "ipv6GateWay": reserve_pool.get("ipv6GateWay"),
            "ipv6DhcpServers": reserve_pool.get("ipv6DhcpServers"),
            "ipv6Subnet": reserve_pool.get("ipv6Subnet"),
            "ipv6DnsServers": reserve_pool.get("ipv6DnsServers"),
            "ipv4TotalHost": reserve_pool.get("ipv4TotalHost"),
            "ipv6TotalHost": reserve_pool.get("ipv6TotalHost")
        }

        # Check for missing mandatory parameters in the playbook
        if not want_reserve.get("name"):
            self.msg = "Missing mandatory parameter 'name' in ReservePoolDetails"
            self.status = "failed"
            return self

        if want_reserve.get("ipv4Prefix") is True:
            if want_reserve.get("ipv4Subnet") is None and \
                    want_reserve.get("ipv4TotalHost") is None:
                self.msg = "missing parameter 'ipv4Subnet' or 'ipv4TotalHost' \
                    while adding the ipv4 in ReservePoolDetails"
                self.status = "failed"
                return self

        if want_reserve.get("ipv6Prefix") is True:
            if want_reserve.get("ipv6Subnet") is None and \
                    want_reserve.get("ipv6TotalHost") is None:
                self.msg = "missing parameter 'ipv6Subnet' or 'ipv6TotalHost' \
                    while adding the ipv6 in ReservePoolDetails"
                self.status = "failed"
                return self

        self.log("Reserve IP Pool Playbook Details " + str(want_reserve))

        # If there are no existing Reserved Pool details, validate and set defaults
        if not self.have.get("reservePool").get("details"):
            if not want_reserve.get("ipv4GlobalPool"):
                self.msg = "missing parameter 'ipv4GlobalPool' in ReservePoolDetails"
                self.status = "failed"
                return self

            if not want_reserve.get("ipv4PrefixLength"):
                self.msg = "missing parameter 'ipv4PrefixLength' in ReservePoolDetails"
                self.status = "failed"
                return self

            if want_reserve.get("type") is None:
                want_reserve.update({"type": "Generic"})
            if want_reserve.get("ipv4GateWay") is None:
                want_reserve.update({"ipv4GateWay": ""})
            if want_reserve.get("ipv4DhcpServers") is None:
                want_reserve.update({"ipv4DhcpServers": []})
            if want_reserve.get("ipv4DnsServers") is None:
                want_reserve.update({"ipv4DnsServers": []})
            if want_reserve.get("ipv6AddressSpace") is None:
                want_reserve.update({"ipv6AddressSpace": False})
            if want_reserve.get("slaacSupport") is None:
                want_reserve.update({"slaacSupport": True})
            if want_reserve.get("ipv4TotalHost") is None:
                del want_reserve['ipv4TotalHost']
            if want_reserve.get("ipv6AddressSpace") is True:
                want_reserve.update({"ipv6Prefix": True})
            else:
                del want_reserve['ipv6Prefix']

            if not want_reserve.get("ipv6AddressSpace"):
                keys_to_check = ['ipv6GlobalPool', 'ipv6PrefixLength',
                                 'ipv6GateWay', 'ipv6DhcpServers',
                                 'ipv6DnsServers', 'ipv6TotalHost']
                for key in keys_to_check:
                    if want_reserve.get(key) is None:
                        del want_reserve[key]
        else:
            keys_to_delete = ['type', 'ipv4GlobalPool',
                              'ipv4Prefix', 'ipv4PrefixLength',
                              'ipv4TotalHost', 'ipv4Subnet']
            for key in keys_to_delete:
                if key in want_reserve:
                    del want_reserve[key]

        self.want.update({"wantReserve": want_reserve})
        self.log(str(self.want))
        self.msg = "Collecting the reserve pool details from the playbook"
        self.status = "success"
        return self

    def get_want_network(self, network_management_details):
        """
        Get all the Network related information from playbook
        Set the status and the msg before returning from the API
        Check the return value of the API with check_return_status()

        Parameters:
          - network_management_details (dict): Playbook network
                      details containing various network settings.

        Returns:
          - self: Current object with updated desired Network-related info.
        """

        want_network = {
            "settings": {
                "dhcpServer": {},
                "dnsServer": {},
                "snmpServer": {},
                "syslogServer": {},
                "netflowcollector": {},
                "ntpServer": {},
                "timezone": "",
                "messageOfTheday": {},
                "network_aaa": {},
                "clientAndEndpoint_aaa": {}
            }
        }
        want_network_settings = want_network.get("settings")
        if network_management_details.get("dhcpServer"):
            want_network_settings.update({
                "dhcpServer": network_management_details.get("dhcpServer")
            })
        else:
            del want_network_settings["dhcpServer"]

        if network_management_details.get("ntpServer"):
            want_network_settings.update({
                "ntpServer": network_management_details.get("ntpServer")
            })
        else:
            del want_network_settings["ntpServer"]

        if network_management_details.get("timezone") is not None:
            want_network_settings["timezone"] = \
                network_management_details.get("timezone")
        else:
            self.msg = "missing parameter timezone in network"
            self.status = "failed"
            return self

        dnsServer = network_management_details.get("dnsServer")
        if dnsServer:
            if dnsServer.get("domainName"):
                want_network_settings.get("dnsServer").update({
                    "domainName":
                    dnsServer.get("domainName")
                })

            if dnsServer.get("primaryIpAddress"):
                want_network_settings.get("dnsServer").update({
                    "primaryIpAddress":
                    dnsServer.get("primaryIpAddress")
                })

            if dnsServer.get("secondaryIpAddress"):
                want_network_settings.get("dnsServer").update({
                    "secondaryIpAddress":
                    dnsServer.get("secondaryIpAddress")
                })
        else:
            del want_network_settings["dnsServer"]

        snmpServer = network_management_details.get("snmpServer")
        if snmpServer:
            if snmpServer.get("configureDnacIP"):
                want_network_settings.get("snmpServer").update({
                    "configureDnacIP": snmpServer.get("configureDnacIP")
                })
            if snmpServer.get("ipAddresses"):
                want_network_settings.get("snmpServer").update({
                    "ipAddresses": snmpServer.get("ipAddresses")
                })
        else:
            del want_network_settings["snmpServer"]

        syslogServer = network_management_details.get("syslogServer")
        if syslogServer:
            if syslogServer.get("configureDnacIP"):
                want_network_settings.get("syslogServer").update({
                    "configureDnacIP": syslogServer.get("configureDnacIP")
                })
            if syslogServer.get("ipAddresses"):
                want_network_settings.get("syslogServer").update({
                    "ipAddresses": syslogServer.get("ipAddresses")
                })
        else:
            del want_network_settings["syslogServer"]

        netflowcollector = network_management_details.get("netflowcollector")
        if netflowcollector:
            if netflowcollector.get("ipAddress"):
                want_network_settings.get("netflowcollector").update({
                    "ipAddress":
                    netflowcollector.get("ipAddress")
                })
            if netflowcollector.get("port"):
                want_network_settings.get("netflowcollector").update({
                    "port":
                    netflowcollector.get("port")
                })
            if netflowcollector.get("configureDnacIP"):
                want_network_settings.get("netflowcollector").update({
                    "configureDnacIP":
                    netflowcollector.get("configureDnacIP")
                })
        else:
            del want_network_settings["netflowcollector"]

        messageOfTheday = network_management_details.get("messageOfTheday")
        if messageOfTheday:
            if messageOfTheday.get("bannerMessage"):
                want_network_settings.get("messageOfTheday").update({
                    "bannerMessage":
                    messageOfTheday.get("bannerMessage")
                })
            if messageOfTheday.get("retainExistingBanner"):
                want_network_settings.get("messageOfTheday").update({
                    "retainExistingBanner":
                    messageOfTheday.get("retainExistingBanner")
                })
        else:
            del want_network_settings["messageOfTheday"]

        network_aaa = network_management_details.get("network_aaa")
        if network_aaa:
            if network_aaa.get("ipAddress"):
                want_network_settings.get("network_aaa").update({
                    "ipAddress":
                    network_aaa.get("ipAddress")
                })
            else:
                if network_aaa.get("servers") == "ISE":
                    self.msg = "missing parameter ipAddress in network_aaa, server ISE is set"
                    self.status = "failed"
                    return self

            if network_aaa.get("network"):
                want_network_settings.get("network_aaa").update({
                    "network": network_aaa.get("network")
                })
            else:
                self.msg = "missing parameter network in network_aaa"
                self.status = "failed"
                return self

            if network_aaa.get("protocol"):
                want_network_settings.get("network_aaa").update({
                    "protocol":
                    network_aaa.get("protocol")
                })
            else:
                self.msg = "missing parameter protocol in network_aaa"
                self.status = "failed"
                return self

            if network_aaa.get("servers"):
                want_network_settings.get("network_aaa").update({
                    "servers":
                    network_aaa.get("servers")
                })
            else:
                self.msg = "missing parameter servers in network_aaa"
                self.status = "failed"
                return self

            if network_aaa.get("sharedSecret"):
                want_network_settings.get("network_aaa").update({
                    "sharedSecret":
                    network_aaa.get("sharedSecret")
                })
        else:
            del want_network_settings["network_aaa"]

        clientAndEndpoint_aaa = network_management_details.get("clientAndEndpoint_aaa")
        if clientAndEndpoint_aaa:
            if clientAndEndpoint_aaa.get("ipAddress"):
                want_network_settings.get("clientAndEndpoint_aaa").update({
                    "ipAddress":
                    clientAndEndpoint_aaa.get("ipAddress")
                })
            else:
                if clientAndEndpoint_aaa.get("servers") == "ISE":
                    self.msg = "missing parameter ipAddress in clientAndEndpoint_aaa, \
                        server ISE is set"
                    self.status = "failed"
                    return self

            if clientAndEndpoint_aaa.get("network"):
                want_network_settings.get("clientAndEndpoint_aaa").update({
                    "network":
                    clientAndEndpoint_aaa.get("network")
                })
            else:
                self.msg = "missing parameter network in clientAndEndpoint_aaa"
                self.status = "failed"
                return self

            if clientAndEndpoint_aaa.get("protocol"):
                want_network_settings.get("clientAndEndpoint_aaa").update({
                    "protocol":
                    clientAndEndpoint_aaa.get("protocol")
                })
            else:
                self.msg = "missing parameter protocol in clientAndEndpoint_aaa"
                self.status = "failed"
                return self

            if clientAndEndpoint_aaa.get("servers"):
                want_network_settings.get("clientAndEndpoint_aaa").update({
                    "servers":
                    clientAndEndpoint_aaa.get("servers")
                })
            else:
                self.msg = "missing parameter servers in clientAndEndpoint_aaa"
                self.status = "failed"
                return self

            if clientAndEndpoint_aaa.get("sharedSecret"):
                want_network_settings.get("clientAndEndpoint_aaa").update({
                    "sharedSecret":
                    clientAndEndpoint_aaa.get("sharedSecret")
                })
        else:
            del want_network_settings["clientAndEndpoint_aaa"]

        self.log("Network Playbook Details " + str(want_network))
        self.want.update({"wantNetwork": want_network})
        self.msg = "Collecting the network details from the playbook"
        self.status = "success"
        return self

    def get_want(self, config):
        """
        Get all the Global Pool Reserved Pool and Network related information from playbook

        Parameters:
          - config (list of dict): Playbook details
        Returns:
          - self
        """

        if config.get("GlobalPoolDetails"):
            global_ippool = config.get("GlobalPoolDetails").get("settings").get("ippool")[0]
            self.get_want_global_pool(global_ippool).check_return_status()

        if config.get("ReservePoolDetails"):
            reserve_pool = config.get("ReservePoolDetails")
            self.get_want_reserve_pool(reserve_pool).check_return_status()

        if config.get("NetworkManagementDetails"):
            network_management_details = config.get("NetworkManagementDetails") \
                                               .get("settings")
            self.get_want_network(network_management_details).check_return_status()

        self.log("User details from the playbook " + str(self.want))
        self.msg = "Successfully retrieved details from the playbook"
        self.status = "success"
        return self

    def update_global_pool(self, config):
        """
        Update/Create Global Pool in Cisco DNA Center with fields provided in playbook

        Parameters:
          - config (list of dict): Playbook details

        Returns:
          - None
        """

        name = config.get("GlobalPoolDetails") \
            .get("settings").get("ippool")[0].get("ipPoolName")
        result_global_pool = self.result.get("response")[0].get("globalPool")
        result_global_pool.get("response").update({name: {}})

        # Check pool exist, if not create and return
        if not self.have.get("globalPool").get("exists"):
            pool_params = self.want.get("wantGlobal")
            self.log(str(pool_params))
            response = self.dnac._exec(
                family="network_settings",
                function="create_global_pool",
                params=pool_params,
            )
            self.check_execution_response_status(response).check_return_status()
            self.log("Global Pool Created Successfully")
            result_global_pool.get("response").get(name) \
                .update({"globalPool Details": self.want.get("wantGlobal")})
            result_global_pool.get("msg").update({name: "Global Pool Created Successfully"})
            return

        # Pool exists, check update is required
        obj_params = [
            ("settings", "settings"),
        ]
        if not self.requires_update(self.have.get("globalPool").get("details"),
                                    self.want.get("wantGlobal"), obj_params):
            self.log("Global pool doesn't requires an update")
            result_global_pool.get("response").get(name).update({
                "Cisco DNA Center params":
                self.have.get("globalPool").get("details").get("settings").get("ippool")[0]
            })
            result_global_pool.get("response").get(name).update({
                "Id": self.have.get("globalPool").get("id")
            })
            result_global_pool.get("msg").update({
                name: "Global pool doesn't require an update"
            })
            self.log(str(self.result))
            return

        self.log("Pool requires update")
        # Pool Exists
        pool_params = copy.deepcopy(self.want.get("wantGlobal"))
        pool_params_ippool = pool_params.get("settings").get("ippool")[0]
        pool_params_ippool.update({"id": self.have.get("globalPool").get("id")})
        self.log(str(pool_params))
        keys_to_remove = ["IpAddressSpace", "ipPoolCidr", "type"]
        for key in keys_to_remove:
            del pool_params["settings"]["ippool"][0][key]

        have_ippool = self.have.get("globalPool").get("details").get("settings").get("ippool")[0]
        keys_to_update = ["dhcpServerIps", "dnsServerIps", "gateway"]
        for key in keys_to_update:
            if pool_params_ippool.get(key) is None:
                pool_params_ippool[key] = have_ippool.get(key)

        self.log(str(pool_params))
        response = self.dnac._exec(
            family="network_settings",
            function="update_global_pool",
            params=pool_params,
        )

        self.check_execution_response_status(response).check_return_status()
        self.log("Global Pool Updated Successfully")
        result_global_pool.get("response").get(name) \
            .update({"Id": self.have.get("globalPool").get("details").get("id")})
        result_global_pool.get("msg").update({name: "Global Pool Updated Successfully"})
        return

    def update_reserve_pool(self, config):
        """
        Update or Create a Reserve Pool in Cisco DNA Center based on the provided configuration.
        This method checks if a reserve pool with the specified name exists in Cisco DNA Center.
        If it exists and requires an update, it updates the pool. If not, it creates a new pool.

        Parameters:
          - config (list of dict) - Playbook details containing Reserve
                                    Pool information.
        Returns:
          - None
        """

        name = config.get("ReservePoolDetails").get("name")
        result_reserve_pool = self.result.get("response")[1].get("reservePool")
        result_reserve_pool.get("response").update({name: {}})
        self.log("Reserve Pool Cisco DNA Center Details " +
                 str(self.have.get("reservePool").get("details")))
        self.log("Reserve Pool User Details " +
                 str(self.want.get("wantReserve")))

        # Check pool exist, if not create and return
        self.log(str(self.want.get("wantReserve").get("ipv4GlobalPool")))
        site_name = config.get("ReservePoolDetails").get("siteName")
        reserve_params = self.want.get("wantReserve")
        site_id = self.get_site_id(site_name)
        reserve_params.update({"site_id": site_id})
        if not self.have.get("reservePool").get("exists"):
            self.log(str(reserve_params))
            response = self.dnac._exec(
                family="network_settings",
                function="reserve_ip_subpool",
                params=reserve_params,
            )
            self.check_execution_response_status(response).check_return_status()
            self.log("Ip Subpool Reservation Created Successfully")
            result_reserve_pool.get("response").get(name) \
                .update({"reservePool Details": self.want.get("wantReserve")})
            result_reserve_pool.get("msg") \
                .update({name: "Ip Subpool Reservation Created Successfully"})
            return

        # Check update is required
        obj_params = [
            ("name", "name"),
            ("type", "type"),
            ("ipv6AddressSpace", "ipv6AddressSpace"),
            ("ipv4GlobalPool", "ipv4GlobalPool"),
            ("ipv4Prefix", "ipv4Prefix"),
            ("ipv4PrefixLength", "ipv4PrefixLength"),
            ("ipv4GateWay", "ipv4GateWay"),
            ("ipv4DhcpServers", "ipv4DhcpServers"),
            ("ipv4DnsServers", "ipv4DnsServers"),
            ("ipv6GateWay", "ipv6GateWay"),
            ("ipv6DhcpServers", "ipv6DhcpServers"),
            ("ipv6DnsServers", "ipv6DnsServers"),
            ("ipv4TotalHost", "ipv4TotalHost"),
            ("slaacSupport", "slaacSupport")
        ]
        if not self.requires_update(self.have.get("reservePool").get("details"),
                                    self.want.get("wantReserve"), obj_params):
            self.log("Reserved ip subpool doesn't require an update")
            result_reserve_pool.get("response").get(name) \
                .update({"Cisco DNA Center params": self.have.get("reservePool").get("details")})
            result_reserve_pool.get("response").get(name) \
                .update({"Id": self.have.get("reservePool").get("id")})
            result_reserve_pool.get("msg") \
                .update({name: "Reserve ip subpool doesn't require an update"})
            return

        self.log("Reserve ip pool requires an update")
        # Pool Exists
        self.log("Reserved Ip Pool Cisco DNA Center Details " + str(self.have.get("reservePool")))
        self.log("Reserved Ip Pool User Details" + str(self.want.get("wantReserve")))
        reserve_params.update({"id": self.have.get("reservePool").get("id")})
        response = self.dnac._exec(
            family="network_settings",
            function="update_reserve_ip_subpool",
            params=reserve_params,
        )
        self.check_execution_response_status(response).check_return_status()
        self.log("Reserved Ip Subpool Updated Successfully")
        result_reserve_pool['msg'] = "Reserved Ip Subpool Updated Successfully"
        result_reserve_pool.get("response").get(name) \
            .update({"Reservation details": self.have.get("reservePool").get("details")})
        return

    def update_network(self, config):
        """
        Update or create a network configuration in Cisco DNA
        Center based on the provided playbook details.

        Parameters:
          - config (list of dict) - Playbook details containing Network
                                    Management information.
        Returns:
          - None
        """

        siteName = config.get("NetworkManagementDetails").get("siteName")
        result_network = self.result.get("response")[2].get("network")
        result_network.get("response").update({siteName: {}})
        obj_params = [
            ("settings", "settings"),
            ("siteName", "siteName")
        ]

        # Check update is required or not
        if not self.requires_update(self.have.get("network").get("net_details"),
                                    self.want.get("wantNetwork"), obj_params):

            self.log("Network doesn't require an update")
            result_network.get("response").get(siteName).update({
                "Cisco DNA Center params": self.have.get("network")
                .get("net_details").get("settings")
            })
            result_network.get("msg").update({siteName: "Network doesn't require an update"})
            return

        self.log("Network requires update")
        self.log("Network Cisco DNA Center Details" + str(self.have.get("network")))
        self.log("Network User Details" + str(self.want.get("wantNetwork")))

        net_params = copy.deepcopy(self.want.get("wantNetwork"))
        net_params.update({"site_id": self.have.get("network").get("site_id")})
        response = self.dnac._exec(
            family="network_settings",
            function='update_network',
            params=net_params,
        )
        self.log(str(response))
        self.check_execution_response_status(response).check_return_status()
        self.log("Network has been changed Successfully")
        result_network.get("msg") \
            .update({siteName: "Network Updated successfully"})
        result_network.get("response").get(siteName) \
            .update({"Network Details": self.want.get("wantNetwork").get("settings")})
        return

    def get_diff_merged(self, config):
        """
        Update or create Global Pool, Reserve Pool, and
        Network configurations in Cisco DNA Center based on the playbook details

        Parameters:
          - config (list of dict) - Playbook details containing
                  Global Pool, Reserve Pool, and Network Management information.

        Returns:
          - self
        """

        if config.get("GlobalPoolDetails") is not None:
            self.update_global_pool(config)

        if config.get("ReservePoolDetails") is not None:
            self.update_reserve_pool(config)

        if config.get("NetworkManagementDetails") is not None:
            self.update_network(config)

        return self

    def delete_reserve_pool(self, name):
        """
        Delete a Reserve Pool by name in Cisco DNA Center

        Parameters:
          - name (str): The name of the Reserve Pool to be deleted.

        Returns:
          - self
        """

        reserve_pool_exists = self.have.get("reservePool").get("exists")
        self.log("Reserved Ip Pool to be deleted " +
                 str(self.want.get("wantReserve").get("name")))

        if not reserve_pool_exists:
            self.msg = "Reserved Ip Subpool Not Found"
            self.status = "failed"
            return self

        _id = self.have.get("reservePool").get("id")
        self.log("Reserve pool {0} id ".format(name) + str(_id))
        response = self.dnac._exec(
            family="network_settings",
            function="release_reserve_ip_subpool",
            params={"id": _id},
        )
        self.check_execution_response_status(response).check_return_status()
        executionid = response.get("executionId")
        result_reserve_pool = self.result.get("response")[1].get("reservePool")
        result_reserve_pool.get("response").update({name: {}})
        result_reserve_pool.get("response").get(name) \
            .update({"Execution Id": executionid})
        result_reserve_pool.get("msg") \
            .update({name: "Ip subpool reservation released successfully"})
        self.msg = "Reserve pool - {0} released successfully".format(name)
        self.status = "success"
        return self

    def delete_global_pool(self, name):
        """
        Delete a Global Pool by name in Cisco DNA Center

        Parameters:
          - name (str): The name of the Global Pool to be deleted.

        Returns:
          - self
        """

        global_pool_exists = self.have.get("globalPool").get("exists")
        if not global_pool_exists:
            self.msg = "Global pool Not Found"
            self.status = "failed"
            return self

        response = self.dnac._exec(
            family="network_settings",
            function="delete_global_ip_pool",
            params={"id": self.have.get("globalPool").get("id")},
        )

        # Check the execution status
        self.check_execution_response_status(response).check_return_status()
        executionid = response.get("executionId")

        # Update result information
        result_global_pool = self.result.get("response")[0].get("globalPool")
        result_global_pool.get("response").update({name: {}})
        result_global_pool.get("response").get(name).update({"Execution Id": executionid})
        result_global_pool.get("msg").update({name: "Pool deleted successfully"})
        self.msg = "Global pool - {0} deleted successfully".format(name)
        self.status = "success"
        return self

    def get_diff_deleted(self, config):
        """
        Delete Reserve Pool and Global Pool in Cisco DNA Center based
        on playbook details.

        Parameters:
          - config (list of dict): Playbook details

        Returns:
          - self
        """

        if config.get("ReservePoolDetails") is not None:
            name = config.get("ReservePoolDetails").get("name")
            self.delete_reserve_pool(name).check_return_status()

        if config.get("GlobalPoolDetails") is not None:
            name = config.get("GlobalPoolDetails") \
                .get("settings").get("ippool")[0].get("ipPoolName")
            self.delete_global_pool(name).check_return_status()

        return self

    def reset_values(self):
        """
        Reset all neccessary attributes to default values

        Parameters:
          - self

        Returns:
          - None
        """

        self.have.clear()
        self.want.clear()
        return


def main():
    """main entry point for module execution"""

    # Define the specification for module arguments
    element_spec = {
        "dnac_host": {"type": 'str', "required": True},
        "dnac_port": {"type": 'str', "default": '443'},
        "dnac_username": {"type": 'str', "default": 'admin', "aliases": ['user']},
        "dnac_password": {"type": 'str', "no_log": True},
        "dnac_verify": {"type": 'bool', "default": 'True'},
        "dnac_version": {"type": 'str', "default": '2.2.3.3'},
        "dnac_debug": {"type": 'bool', "default": False},
        "dnac_log": {"type": 'bool', "default": False},
        "config": {"type": 'list', "required": True, "elements": 'dict'},
        "state": {"default": 'merged', "choices": ['merged', 'deleted']},
        "validate_response_schema": {"type": 'bool', "default": True},
    }

    # Create an AnsibleModule object with argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=False)
    dnac_network = DnacNetwork(module)
    state = dnac_network.params.get("state")
    if state not in dnac_network.supported_states:
        dnac_network.status = "invalid"
        dnac_network.msg = "State {0} is invalid".format(state)
        dnac_network.check_return_status()

    dnac_network.validate_input().check_return_status()

    for config in dnac_network.config:
        dnac_network.reset_values()
        dnac_network.get_have(config).check_return_status()
        dnac_network.get_want(config).check_return_status()
        dnac_network.get_diff_state_apply[state](config).check_return_status()

    module.exit_json(**dnac_network.result)


if __name__ == "__main__":
    main()
