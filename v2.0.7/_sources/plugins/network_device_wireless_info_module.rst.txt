.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.cisco.dnac.network_device_wireless_info_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.dnac.network_device_wireless_info -- Manage NetworkDeviceWirelessInfo objects of Devices
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `cisco.dnac collection <https://galaxy.ansible.com/cisco/dnac>`_ (version 2.0.7).

    To install it use: :code:`ansible-galaxy collection install cisco.dnac`.

    To use it in a playbook, specify: :code:`cisco.dnac.network_device_wireless_info`.

.. version_added

.. versionadded:: 1.0.0 of cisco.dnac

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Returns the wireless lan controller info with given device ID.

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
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#parameter-id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device ID.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes


.. Seealso

See Also
--------

.. seealso::

   :ref:`cisco.dnac.plugins.module_utils.definitions.network_device_wireless_info <ansible_collections.cisco.dnac.plugins.module_utils.definitions.network_device_wireless_info_module>`
      The official documentation on the **cisco.dnac.plugins.module_utils.definitions.network_device_wireless_info** module.
   `NetworkDeviceWirelessInfo reference <https://developer.cisco.com/docs/dna-center/api/1-3-3-x>`_
       Complete reference of the NetworkDeviceWirelessInfo object model.
   `NetworkDeviceWirelessInfo reference <https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary>`_
       SDK reference.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: get_wireless_lan_controller_details_by_id
      cisco.dnac.network_device_wireless_info:
        state: query  # required
        id: SomeValue  # string, required
      register: nm_get_wireless_lan_controller_details_by_id





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
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">devices.get_wireless_lan_controller_details_by_id</div>
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

