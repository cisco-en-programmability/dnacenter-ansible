.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.cisco.dnac.sda_host_onboarding_user_device_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.dnac.sda_host_onboarding_user_device -- Manage SdaHostOnboardingUserDevice objects of Sda
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `cisco.dnac collection <https://galaxy.ansible.com/cisco/dnac>`_ (version 2.0.7).

    To install it use: :code:`ansible-galaxy collection install cisco.dnac`.

    To use it in a playbook, specify: :code:`cisco.dnac.sda_host_onboarding_user_device`.

.. version_added

.. versionadded:: 1.0.0 of cisco.dnac

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Get Port assignment for user device in SDA Fabric.
- Delete Port assignment for user device in SDA Fabric.
- Add Port assignment for user device in SDA Fabric.

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
                    <div class="ansibleOptionAnchor" id="parameter-device_ip"></div>
                    <b>device_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-device_ip" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device-ip query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-interface_name"></div>
                    <b>interface_name</b>
                    <a class="ansibleOptionLink" href="#parameter-interface_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InterfaceName query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-payload"></div>
                    <b>payload</b>
                    <a class="ansibleOptionLink" href="#parameter-payload" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An object to send in the Request body.</div>
                                            <div>Required for state create.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-payload/authenticateTemplateName"></div>
                    <b>authenticateTemplateName</b>
                    <a class="ansibleOptionLink" href="#parameter-payload/authenticateTemplateName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the sda host onboarding user device&#x27;s authenticateTemplateName.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-payload/dataIpAddressPoolName"></div>
                    <b>dataIpAddressPoolName</b>
                    <a class="ansibleOptionLink" href="#parameter-payload/dataIpAddressPoolName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the sda host onboarding user device&#x27;s dataIpAddressPoolName.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-payload/deviceManagementIpAddress"></div>
                    <b>deviceManagementIpAddress</b>
                    <a class="ansibleOptionLink" href="#parameter-payload/deviceManagementIpAddress" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the sda host onboarding user device&#x27;s deviceManagementIpAddress.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-payload/interfaceName"></div>
                    <b>interfaceName</b>
                    <a class="ansibleOptionLink" href="#parameter-payload/interfaceName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the sda host onboarding user device&#x27;s interfaceName.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-payload/siteNameHierarchy"></div>
                    <b>siteNameHierarchy</b>
                    <a class="ansibleOptionLink" href="#parameter-payload/siteNameHierarchy" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the sda host onboarding user device&#x27;s siteNameHierarchy.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-payload/voiceIpAddressPoolName"></div>
                    <b>voiceIpAddressPoolName</b>
                    <a class="ansibleOptionLink" href="#parameter-payload/voiceIpAddressPoolName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the sda host onboarding user device&#x27;s voiceIpAddressPoolName.</div>
                                                        </td>
            </tr>
                    
                        </table>
    <br/>

.. Notes


.. Seealso

See Also
--------

.. seealso::

   :ref:`cisco.dnac.plugins.module_utils.definitions.sda_host_onboarding_user_device <ansible_collections.cisco.dnac.plugins.module_utils.definitions.sda_host_onboarding_user_device_module>`
      The official documentation on the **cisco.dnac.plugins.module_utils.definitions.sda_host_onboarding_user_device** module.
   `SdaHostOnboardingUserDevice reference <https://developer.cisco.com/docs/dna-center/api/1-3-3-x>`_
       Complete reference of the SdaHostOnboardingUserDevice object model.
   `SdaHostOnboardingUserDevice reference <https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary>`_
       SDK reference.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: get_port_assignment_for_user_device
      cisco.dnac.sda_host_onboarding_user_device:
        state: query  # required
        device_ip: SomeValue  # string, required
        interface_name: SomeValue  # string, required
      register: nm_get_port_assignment_for_user_device

    - name: delete_port_assignment_for_user_device
      cisco.dnac.sda_host_onboarding_user_device:
        state: delete  # required
        device_ip: SomeValue  # string, required
        interface_name: SomeValue  # string, required

    - name: add_port_assignment_for_user_device
      cisco.dnac.sda_host_onboarding_user_device:
        state: create  # required
        payload:  # required
        - siteNameHierarchy: SomeValue  # string
          deviceManagementIpAddress: SomeValue  # string
          interfaceName: SomeValue  # string
          dataIpAddressPoolName: SomeValue  # string
          voiceIpAddressPoolName: SomeValue  # string
          authenticateTemplateName: SomeValue  # string





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
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">sda.add_port_assignment_for_user_device</div>
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

