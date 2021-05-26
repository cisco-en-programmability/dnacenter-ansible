.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.cisco.dnac.network_device_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.dnac.network_device -- Manage NetworkDevice objects of Devices
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `cisco.dnac collection <https://galaxy.ansible.com/cisco/dnac>`_ (version 2.0.7).

    To install it use: :code:`ansible-galaxy collection install cisco.dnac`.

    To use it in a playbook, specify: :code:`cisco.dnac.network_device`.

.. version_added

.. versionadded:: 1.0.0 of cisco.dnac

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Returns list of network devices based on filter criteria such as management IP address, mac address, hostname, location name and a wide variety of additional criteria. You can also use the asterisk in any value to conduct a wildcard search. For example, to find all hostnames beginning with myhost in the IP address range 192.25.18.n, issue the following request GET fqdnoripofdnacenterplatform/dna/intent/api/v1/network-device? hostname=myhost* & managementIpAddress=192.25.18.* For a complete list of parameter names that you can use for filtering this request, see the DNA Center API Reference documentation. Note If id parameter is provided, it will return the list of network-devices for the given ids and ignores the other request parameters.

- Adds the device with given credential.
- Sync the devices provided as input.
- Deletes the network device for the given Id.
- Returns the network device details for the given device ID.
- Returns brief summary of device info such as hostname, management IP address for the given device Id.
- Returns the list of network devices for the given pagination range.
- Returns the count of network devices based on the filter criteria by management IP address, mac address, hostname and location name.

- Returns the network device by specified IP address.
- Returns the network device with given serial number.

.. note::
    This module has a corresponding :ref:`action plugin <action_plugins>`.

.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- dnacentersdk


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-associated_wlc_ip"></div>
                    <b>associated_wlc_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-associated_wlc_ip" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>AssociatedWlcIp query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-cliTransport"></div>
                    <b>cliTransport</b>
                    <a class="ansibleOptionLink" href="#parameter-cliTransport" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s cliTransport.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-collection_interval"></div>
                    <b>collection_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-collection_interval" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>CollectionInterval query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-collection_status"></div>
                    <b>collection_status</b>
                    <a class="ansibleOptionLink" href="#parameter-collection_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>CollectionStatus query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-computeDevice"></div>
                    <b>computeDevice</b>
                    <a class="ansibleOptionLink" href="#parameter-computeDevice" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s computeDevice.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-count"></div>
                    <b>count</b>
                    <a class="ansibleOptionLink" href="#parameter-count" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>If true gets the number of objects.</div>
                                            <div>Required for state query.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-enablePassword"></div>
                    <b>enablePassword</b>
                    <a class="ansibleOptionLink" href="#parameter-enablePassword" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s enablePassword.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-error_code"></div>
                    <b>error_code</b>
                    <a class="ansibleOptionLink" href="#parameter-error_code" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>ErrorCode query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-error_description"></div>
                    <b>error_description</b>
                    <a class="ansibleOptionLink" href="#parameter-error_description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>ErrorDescription query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-extendedDiscoveryInfo"></div>
                    <b>extendedDiscoveryInfo</b>
                    <a class="ansibleOptionLink" href="#parameter-extendedDiscoveryInfo" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s extendedDiscoveryInfo.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-family"></div>
                    <b>family</b>
                    <a class="ansibleOptionLink" href="#parameter-family" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Family query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-hostname"></div>
                    <b>hostname</b>
                    <a class="ansibleOptionLink" href="#parameter-hostname" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Hostname query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-httpPassword"></div>
                    <b>httpPassword</b>
                    <a class="ansibleOptionLink" href="#parameter-httpPassword" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s httpPassword.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-httpPort"></div>
                    <b>httpPort</b>
                    <a class="ansibleOptionLink" href="#parameter-httpPort" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s httpPort.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-httpSecure"></div>
                    <b>httpSecure</b>
                    <a class="ansibleOptionLink" href="#parameter-httpSecure" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s httpSecure.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-httpUserName"></div>
                    <b>httpUserName</b>
                    <a class="ansibleOptionLink" href="#parameter-httpUserName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s httpUserName.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#parameter-id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Accepts comma separated id&#x27;s and return list of network-devices for the given id&#x27;s. If invalid or not- found id&#x27;s are provided, null entry will be returned in the list.</div>
                                            <div>Device ID.</div>
                                            <div>Required for states query and delete.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-ip_address"></div>
                    <b>ip_address</b>
                    <a class="ansibleOptionLink" href="#parameter-ip_address" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device IP address.</div>
                                            <div>Required for state query.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-ipAddress"></div>
                    <b>ipAddress</b>
                    <a class="ansibleOptionLink" href="#parameter-ipAddress" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s ipAddress (list of strings).</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-is_force_delete"></div>
                    <b>is_force_delete</b>
                    <a class="ansibleOptionLink" href="#parameter-is_force_delete" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>IsForceDelete query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-license_name"></div>
                    <b>license_name</b>
                    <a class="ansibleOptionLink" href="#parameter-license_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>License.name query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-license_status"></div>
                    <b>license_status</b>
                    <a class="ansibleOptionLink" href="#parameter-license_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>License.status query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-license_type"></div>
                    <b>license_type</b>
                    <a class="ansibleOptionLink" href="#parameter-license_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>License.type query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-location"></div>
                    <b>location</b>
                    <a class="ansibleOptionLink" href="#parameter-location" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Location query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-location_name"></div>
                    <b>location_name</b>
                    <a class="ansibleOptionLink" href="#parameter-location_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>LocationName query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-mac_address"></div>
                    <b>mac_address</b>
                    <a class="ansibleOptionLink" href="#parameter-mac_address" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>MacAddress query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-management_ip_address"></div>
                    <b>management_ip_address</b>
                    <a class="ansibleOptionLink" href="#parameter-management_ip_address" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>ManagementIpAddress query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-merakiOrgId"></div>
                    <b>merakiOrgId</b>
                    <a class="ansibleOptionLink" href="#parameter-merakiOrgId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s merakiOrgId (list of strings).</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-module_equpimenttype"></div>
                    <b>module_equpimenttype</b>
                    <a class="ansibleOptionLink" href="#parameter-module_equpimenttype" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Module+equpimenttype query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-module_name"></div>
                    <b>module_name</b>
                    <a class="ansibleOptionLink" href="#parameter-module_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Module+name query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-module_operationstatecode"></div>
                    <b>module_operationstatecode</b>
                    <a class="ansibleOptionLink" href="#parameter-module_operationstatecode" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Module+operationstatecode query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-module_partnumber"></div>
                    <b>module_partnumber</b>
                    <a class="ansibleOptionLink" href="#parameter-module_partnumber" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Module+partnumber query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-module_servicestate"></div>
                    <b>module_servicestate</b>
                    <a class="ansibleOptionLink" href="#parameter-module_servicestate" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Module+servicestate query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-module_vendorequipmenttype"></div>
                    <b>module_vendorequipmenttype</b>
                    <a class="ansibleOptionLink" href="#parameter-module_vendorequipmenttype" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Module+vendorequipmenttype query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-netconfPort"></div>
                    <b>netconfPort</b>
                    <a class="ansibleOptionLink" href="#parameter-netconfPort" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s netconfPort.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-not_synced_for_minutes"></div>
                    <b>not_synced_for_minutes</b>
                    <a class="ansibleOptionLink" href="#parameter-not_synced_for_minutes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>NotSyncedForMinutes query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-password"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s password.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-platform_id"></div>
                    <b>platform_id</b>
                    <a class="ansibleOptionLink" href="#parameter-platform_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>PlatformId query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-reachability_status"></div>
                    <b>reachability_status</b>
                    <a class="ansibleOptionLink" href="#parameter-reachability_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>ReachabilityStatus query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-records_to_return"></div>
                    <b>records_to_return</b>
                    <a class="ansibleOptionLink" href="#parameter-records_to_return" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of records to return.</div>
                                            <div>Required for state query.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-role"></div>
                    <b>role</b>
                    <a class="ansibleOptionLink" href="#parameter-role" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Role query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-serial_number"></div>
                    <b>serial_number</b>
                    <a class="ansibleOptionLink" href="#parameter-serial_number" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SerialNumber query parameter.</div>
                                            <div>Device serial number.</div>
                                            <div>Required for state query.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-serialNumber"></div>
                    <b>serialNumber</b>
                    <a class="ansibleOptionLink" href="#parameter-serialNumber" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s serialNumber.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-series"></div>
                    <b>series</b>
                    <a class="ansibleOptionLink" href="#parameter-series" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Series query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpAuthPassphrase"></div>
                    <b>snmpAuthPassphrase</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpAuthPassphrase" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s snmpAuthPassphrase.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpAuthProtocol"></div>
                    <b>snmpAuthProtocol</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpAuthProtocol" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s snmpAuthProtocol.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpMode"></div>
                    <b>snmpMode</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpMode" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s snmpMode.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpPrivPassphrase"></div>
                    <b>snmpPrivPassphrase</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpPrivPassphrase" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s snmpPrivPassphrase.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpPrivProtocol"></div>
                    <b>snmpPrivProtocol</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpPrivProtocol" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s snmpPrivProtocol.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpRetry"></div>
                    <b>snmpRetry</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpRetry" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s snmpRetry.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpROCommunity"></div>
                    <b>snmpROCommunity</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpROCommunity" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s snmpROCommunity.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpRWCommunity"></div>
                    <b>snmpRWCommunity</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpRWCommunity" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s snmpRWCommunity.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpTimeout"></div>
                    <b>snmpTimeout</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpTimeout" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s snmpTimeout.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpUserName"></div>
                    <b>snmpUserName</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpUserName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s snmpUserName.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpVersion"></div>
                    <b>snmpVersion</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpVersion" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s snmpVersion.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-software_type"></div>
                    <b>software_type</b>
                    <a class="ansibleOptionLink" href="#parameter-software_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SoftwareType query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-software_version"></div>
                    <b>software_version</b>
                    <a class="ansibleOptionLink" href="#parameter-software_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SoftwareVersion query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-start_index"></div>
                    <b>start_index</b>
                    <a class="ansibleOptionLink" href="#parameter-start_index" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Start index.</div>
                                            <div>Required for state query.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-summary"></div>
                    <b>summary</b>
                    <a class="ansibleOptionLink" href="#parameter-summary" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>If true gets the summary.</div>
                                            <div>Required for state query.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Type query parameter.</div>
                                            <div>InventoryDeviceInfo&#x27;s type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-up_time"></div>
                    <b>up_time</b>
                    <a class="ansibleOptionLink" href="#parameter-up_time" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>UpTime query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-updateMgmtIPaddressList"></div>
                    <b>updateMgmtIPaddressList</b>
                    <a class="ansibleOptionLink" href="#parameter-updateMgmtIPaddressList" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s updateMgmtIPaddressList (list of objects).</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-updateMgmtIPaddressList/existMgmtIpAddress"></div>
                    <b>existMgmtIpAddress</b>
                    <a class="ansibleOptionLink" href="#parameter-updateMgmtIPaddressList/existMgmtIpAddress" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the network device&#x27;s existMgmtIpAddress.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-updateMgmtIPaddressList/newMgmtIpAddress"></div>
                    <b>newMgmtIpAddress</b>
                    <a class="ansibleOptionLink" href="#parameter-updateMgmtIPaddressList/newMgmtIpAddress" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the network device&#x27;s newMgmtIpAddress.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-userName"></div>
                    <b>userName</b>
                    <a class="ansibleOptionLink" href="#parameter-userName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryDeviceInfo&#x27;s userName.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes


.. Seealso

See Also
--------

.. seealso::

   :ref:`cisco.dnac.plugins.module_utils.definitions.network_device <ansible_collections.cisco.dnac.plugins.module_utils.definitions.network_device_module>`
      The official documentation on the **cisco.dnac.plugins.module_utils.definitions.network_device** module.
   `NetworkDevice reference <https://developer.cisco.com/docs/dna-center/api/1-3-3-x>`_
       Complete reference of the NetworkDevice object model.
   `NetworkDevice reference <https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary>`_
       SDK reference.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: get_device_list
      cisco.dnac.network_device:
        state: query  # required
        associated_wlc_ip: SomeValue  # string
        collection_interval: SomeValue  # string
        collection_status: SomeValue  # string
        error_code: SomeValue  # string
        error_description: SomeValue  # string
        family: SomeValue  # string
        hostname: SomeValue  # string
        id: SomeValue  # string
        license_name: SomeValue  # string
        license_status: SomeValue  # string
        license_type: SomeValue  # string
        location: SomeValue  # string
        location_name: SomeValue  # string
        mac_address: SomeValue  # string
        management_ip_address: SomeValue  # string
        module_equpimenttype: SomeValue  # string
        module_name: SomeValue  # string
        module_operationstatecode: SomeValue  # string
        module_partnumber: SomeValue  # string
        module_servicestate: SomeValue  # string
        module_vendorequipmenttype: SomeValue  # string
        not_synced_for_minutes: SomeValue  # string
        platform_id: SomeValue  # string
        reachability_status: SomeValue  # string
        role: SomeValue  # string
        serial_number: SomeValue  # string
        series: SomeValue  # string
        software_type: SomeValue  # string
        software_version: SomeValue  # string
        type: SomeValue  # string
        up_time: SomeValue  # string
      register: nm_get_device_list

    - name: add_device
      cisco.dnac.network_device:
        state: create  # required
        cliTransport: SomeValue  # string, required
        enablePassword: SomeValue  # string, required
        ipAddress:  # required
        - SomeValue  # string
        password: SomeValue  # string, required
        snmpAuthPassphrase: SomeValue  # string, required
        snmpAuthProtocol: SomeValue  # string, required
        snmpMode: SomeValue  # string, required
        snmpPrivPassphrase: SomeValue  # string, required
        snmpPrivProtocol: SomeValue  # string, required
        snmpROCommunity: SomeValue  # string, required
        snmpRWCommunity: SomeValue  # string, required
        snmpRetry: 1  #  integer, required
        snmpTimeout: 1  #  integer, required
        snmpUserName: SomeValue  # string, required
        userName: SomeValue  # string, required
        computeDevice: True  # boolean
        extendedDiscoveryInfo: SomeValue  # string
        httpPassword: SomeValue  # string
        httpPort: SomeValue  # string
        httpSecure: True  # boolean
        httpUserName: SomeValue  # string
        merakiOrgId:
        - SomeValue  # string
        netconfPort: SomeValue  # string
        serialNumber: SomeValue  # string
        snmpVersion: SomeValue  # string
        type: # valid values are 'COMPUTE_DEVICE',
          # 'MERAKI_DASHBOARD',
          # 'NETWORK_DEVICE',
          # 'NODATACHANGE'.
          SomeValue  # string
        updateMgmtIPaddressList:
        - existMgmtIpAddress: SomeValue  # string
          newMgmtIpAddress: SomeValue  # string

    - name: sync_devices
      cisco.dnac.network_device:
        state: update  # required
        cliTransport: SomeValue  # string, required
        enablePassword: SomeValue  # string, required
        ipAddress:  # required
        - SomeValue  # string
        password: SomeValue  # string, required
        snmpAuthPassphrase: SomeValue  # string, required
        snmpAuthProtocol: SomeValue  # string, required
        snmpMode: SomeValue  # string, required
        snmpPrivPassphrase: SomeValue  # string, required
        snmpPrivProtocol: SomeValue  # string, required
        snmpROCommunity: SomeValue  # string, required
        snmpRWCommunity: SomeValue  # string, required
        snmpRetry: 1  #  integer, required
        snmpTimeout: 1  #  integer, required
        snmpUserName: SomeValue  # string, required
        userName: SomeValue  # string, required
        computeDevice: True  # boolean
        extendedDiscoveryInfo: SomeValue  # string
        httpPassword: SomeValue  # string
        httpPort: SomeValue  # string
        httpSecure: True  # boolean
        httpUserName: SomeValue  # string
        merakiOrgId:
        - SomeValue  # string
        netconfPort: SomeValue  # string
        serialNumber: SomeValue  # string
        snmpVersion: SomeValue  # string
        type: # valid values are 'COMPUTE_DEVICE',
          # 'MERAKI_DASHBOARD',
          # 'NETWORK_DEVICE',
          # 'NODATACHANGE'.
          SomeValue  # string
        updateMgmtIPaddressList:
        - existMgmtIpAddress: SomeValue  # string
          newMgmtIpAddress: SomeValue  # string

    - name: delete_device_by_id
      cisco.dnac.network_device:
        state: delete  # required
        id: SomeValue  # string, required
        is_force_delete: True  # boolean

    - name: get_device_by_id
      cisco.dnac.network_device:
        state: query  # required
        id: SomeValue  # string, required
      register: nm_get_device_by_id

    - name: get_device_summary
      cisco.dnac.network_device:
        state: query  # required
        id: SomeValue  # string, required
        summary: True  # boolean, required
      register: nm_get_device_summary

    - name: get_network_device_by_pagination_range
      cisco.dnac.network_device:
        state: query  # required
        records_to_return: 1  #  integer, required
        start_index: 1  #  integer, required
      register: nm_get_network_device_by_pagination_range

    - name: get_device_count
      cisco.dnac.network_device:
        state: query  # required
        count: True  # boolean, required
      register: nm_get_device_count

    - name: get_network_device_by_ip
      cisco.dnac.network_device:
        state: query  # required
        ip_address: SomeValue  # string, required
      register: nm_get_network_device_by_ip

    - name: get_device_by_serial_number
      cisco.dnac.network_device:
        state: query  # required
        serial_number: SomeValue  # string, required
      register: nm_get_device_by_serial_number





.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-dnac_response"></div>
                    <b>dnac_response</b>
                    <a class="ansibleOptionLink" href="#return-dnac_response" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>A dictionary with the response returned by the DNA Center Python SDK</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;response&#x27;: 29, &#x27;version&#x27;: &#x27;1.0&#x27;}</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-missing_params"></div>
                    <b>missing_params</b>
                    <a class="ansibleOptionLink" href="#return-missing_params" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>when the function request schema is not satisfied</td>
                <td>
                                            <div>Provided arguments do not comply with the schema of the DNA Center Python SDK function</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-sdk_function"></div>
                    <b>sdk_function</b>
                    <a class="ansibleOptionLink" href="#return-sdk_function" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The DNA Center SDK function used to execute the task</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">devices.add_device</div>
                                    </td>
            </tr>
                        </table>
    <br/><br/>

..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Rafael Campos (@racampos)



.. Parsing errors

