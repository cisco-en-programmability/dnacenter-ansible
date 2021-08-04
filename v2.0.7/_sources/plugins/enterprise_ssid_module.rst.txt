.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.cisco.dnac.enterprise_ssid_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.dnac.enterprise_ssid -- Manage EnterpriseSsid objects of Wireless
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `cisco.dnac collection <https://galaxy.ansible.com/cisco/dnac>`_ (version 2.0.7).

    To install it use: :code:`ansible-galaxy collection install cisco.dnac`.

    To use it in a playbook, specify: :code:`cisco.dnac.enterprise_ssid`.

.. version_added

.. versionadded:: 1.0.0 of cisco.dnac

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Gets either one or all the enterprise SSID.
- Creates enterprise SSID.
- Deletes given enterprise SSID.

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
                    <div class="ansibleOptionAnchor" id="parameter-enableBroadcastSSID"></div>
                    <b>enableBroadcastSSID</b>
                    <a class="ansibleOptionLink" href="#parameter-enableBroadcastSSID" title="Permalink to this option"></a>
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
                                            <div>EnableBroadcastSSID, property of the request body.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-enableFastLane"></div>
                    <b>enableFastLane</b>
                    <a class="ansibleOptionLink" href="#parameter-enableFastLane" title="Permalink to this option"></a>
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
                                            <div>EnableFastLane, property of the request body.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-enableMACFiltering"></div>
                    <b>enableMACFiltering</b>
                    <a class="ansibleOptionLink" href="#parameter-enableMACFiltering" title="Permalink to this option"></a>
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
                                            <div>EnableMACFiltering, property of the request body.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-fastTransition"></div>
                    <b>fastTransition</b>
                    <a class="ansibleOptionLink" href="#parameter-fastTransition" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Fast Transition, property of the request body.</div>
                                            <div>Available values are &#x27;Adaptive&#x27;, &#x27;Enable&#x27; and &#x27;Disable&#x27;.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Enter SSID Name, property of the request body. Constraint is maxLength set to 32.</div>
                                            <div>Required for state create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-passphrase"></div>
                    <b>passphrase</b>
                    <a class="ansibleOptionLink" href="#parameter-passphrase" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Pass Phrase (Only applicable for SSID with PERSONAL security level), property of the request body. Constraints are maxLength set to 63 and minLength set to 8.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-radioPolicy"></div>
                    <b>radioPolicy</b>
                    <a class="ansibleOptionLink" href="#parameter-radioPolicy" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Radio Policy, property of the request body.</div>
                                            <div>Available values are &#x27;Dual band operation (2.4GHz and 5GHz)&#x27;, &#x27;Dual band operation with band select&#x27;, &#x27;5GHz only&#x27; and &#x27;2.4GHz only&#x27;.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-securityLevel"></div>
                    <b>securityLevel</b>
                    <a class="ansibleOptionLink" href="#parameter-securityLevel" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Security Level, property of the request body.</div>
                                            <div>Available values are &#x27;WPA2_ENTERPRISE&#x27;, &#x27;WPA2_PERSONAL&#x27; and &#x27;OPEN&#x27;.</div>
                                            <div>Required for state create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-ssid_name"></div>
                    <b>ssid_name</b>
                    <a class="ansibleOptionLink" href="#parameter-ssid_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Enter the enterprise SSID name that needs to be retrieved. If not entered, all the enterprise SSIDs will be retrieved.</div>
                                            <div>Enter the SSID name to be deleted.</div>
                                            <div>Required for state delete.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-trafficType"></div>
                    <b>trafficType</b>
                    <a class="ansibleOptionLink" href="#parameter-trafficType" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Traffic Type, property of the request body.</div>
                                            <div>Available values are &#x27;voicedata&#x27; and &#x27;data&#x27;.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes


.. Seealso

See Also
--------

.. seealso::

   :ref:`cisco.dnac.plugins.module_utils.definitions.enterprise_ssid <ansible_collections.cisco.dnac.plugins.module_utils.definitions.enterprise_ssid_module>`
      The official documentation on the **cisco.dnac.plugins.module_utils.definitions.enterprise_ssid** module.
   `EnterpriseSsid reference <https://developer.cisco.com/docs/dna-center/api/1-3-3-x>`_
       Complete reference of the EnterpriseSsid object model.
   `EnterpriseSsid reference <https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary>`_
       SDK reference.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: get_enterprise_ssid
      cisco.dnac.enterprise_ssid:
        state: query  # required
        ssid_name: SomeValue  # string
      register: nm_get_enterprise_ssid

    - name: create_enterprise_ssid
      cisco.dnac.enterprise_ssid:
        state: create  # required
        name: SomeValue  # string, required
        securityLevel: # valid values are 'WPA2_ENTERPRISE',
          # 'WPA2_PERSONAL',
          # 'OPEN'.
          SomeValue  # string, required
        enableBroadcastSSID: True  # boolean
        enableFastLane: True  # boolean
        enableMACFiltering: True  # boolean
        fastTransition: # valid values are 'Adaptive',
          # 'Enable',
          # 'Disable'.
          SomeValue  # string
        passphrase: SomeValue  # string
        radioPolicy: # valid values are 'Dual band operation (2.4GHz and 5GHz)',
          # 'Dual band operation with band select',
          # '5GHz only',
          # '2.4GHz only'.
          SomeValue  # string
        trafficType: # valid values are 'voicedata',
          # 'data'.
          SomeValue  # string

    - name: delete_enterprise_ssid
      cisco.dnac.enterprise_ssid:
        state: delete  # required
        ssid_name: SomeValue  # string, required





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
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">wireless.create_enterprise_ssid</div>
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

