.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.cisco.dnac.smart_virtual_account_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.dnac.smart_virtual_account -- Manage SmartVirtualAccount objects of DeviceOnboardingPnp
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `cisco.dnac collection <https://galaxy.ansible.com/cisco/dnac>`_ (version 2.0.7).

    To install it use: :code:`ansible-galaxy collection install cisco.dnac`.

    To use it in a playbook, specify: :code:`cisco.dnac.smart_virtual_account`.

.. version_added

.. versionadded:: 1.0.0 of cisco.dnac

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Returns the list of Smart Account domains.
- Returns list of virtual accounts associated with the specified smart account.
- Registers a Smart Account, Virtual Account and the relevant server profile info with the PnP System & database. The devices present in the registered virtual account are synced with the PnP database as well. The response payload returns the new profile.

- Updates the PnP Server profile in a registered Virtual Account in the PnP database. The response payload returns the updated smart & virtual account info.

- Deregisters the specified smart account & virtual account info and the associated device information from the PnP System & database. The devices associated with the deregistered virtual account are removed from the PnP database as well. The response payload contains the deregistered smart & virtual account information.


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
            <th colspan="3">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-autoSyncPeriod"></div>
                    <b>autoSyncPeriod</b>
                    <a class="ansibleOptionLink" href="#parameter-autoSyncPeriod" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SAVAMapping&#x27;s autoSyncPeriod.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ccoUser"></div>
                    <b>ccoUser</b>
                    <a class="ansibleOptionLink" href="#parameter-ccoUser" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SAVAMapping&#x27;s ccoUser.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-domain"></div>
                    <b>domain</b>
                    <a class="ansibleOptionLink" href="#parameter-domain" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Smart Account Domain.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-expiry"></div>
                    <b>expiry</b>
                    <a class="ansibleOptionLink" href="#parameter-expiry" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SAVAMapping&#x27;s expiry.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-lastSync"></div>
                    <b>lastSync</b>
                    <a class="ansibleOptionLink" href="#parameter-lastSync" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SAVAMapping&#x27;s lastSync.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
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
                                            <div>Virtual Account Name.</div>
                                            <div>Required for state delete.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-profile"></div>
                    <b>profile</b>
                    <a class="ansibleOptionLink" href="#parameter-profile" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SAVAMapping&#x27;s profile.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-profile/addressFqdn"></div>
                    <b>addressFqdn</b>
                    <a class="ansibleOptionLink" href="#parameter-profile/addressFqdn" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the smart virtual account&#x27;s addressFqdn.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-profile/addressIpV4"></div>
                    <b>addressIpV4</b>
                    <a class="ansibleOptionLink" href="#parameter-profile/addressIpV4" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the smart virtual account&#x27;s addressIpV4.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-profile/cert"></div>
                    <b>cert</b>
                    <a class="ansibleOptionLink" href="#parameter-profile/cert" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the smart virtual account&#x27;s cert.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-profile/makeDefault"></div>
                    <b>makeDefault</b>
                    <a class="ansibleOptionLink" href="#parameter-profile/makeDefault" title="Permalink to this option"></a>
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
                                            <div>It is the smart virtual account&#x27;s makeDefault.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-profile/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-profile/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the smart virtual account&#x27;s name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-profile/port"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#parameter-profile/port" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the smart virtual account&#x27;s port.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-profile/profileId"></div>
                    <b>profileId</b>
                    <a class="ansibleOptionLink" href="#parameter-profile/profileId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the smart virtual account&#x27;s profileId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-profile/proxy"></div>
                    <b>proxy</b>
                    <a class="ansibleOptionLink" href="#parameter-profile/proxy" title="Permalink to this option"></a>
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
                                            <div>It is the smart virtual account&#x27;s proxy.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-smartAccountId"></div>
                    <b>smartAccountId</b>
                    <a class="ansibleOptionLink" href="#parameter-smartAccountId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SAVAMapping&#x27;s smartAccountId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-syncResult"></div>
                    <b>syncResult</b>
                    <a class="ansibleOptionLink" href="#parameter-syncResult" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SAVAMapping&#x27;s syncResult.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-syncResult/syncList"></div>
                    <b>syncList</b>
                    <a class="ansibleOptionLink" href="#parameter-syncResult/syncList" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the smart virtual account&#x27;s syncList.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-syncResult/syncList/deviceSnList"></div>
                    <b>deviceSnList</b>
                    <a class="ansibleOptionLink" href="#parameter-syncResult/syncList/deviceSnList" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the smart virtual account&#x27;s deviceSnList.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-syncResult/syncList/syncType"></div>
                    <b>syncType</b>
                    <a class="ansibleOptionLink" href="#parameter-syncResult/syncList/syncType" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the smart virtual account&#x27;s syncType.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-syncResult/syncMsg"></div>
                    <b>syncMsg</b>
                    <a class="ansibleOptionLink" href="#parameter-syncResult/syncMsg" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the smart virtual account&#x27;s syncMsg.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-syncResultStr"></div>
                    <b>syncResultStr</b>
                    <a class="ansibleOptionLink" href="#parameter-syncResultStr" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SAVAMapping&#x27;s syncResultStr.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-syncStartTime"></div>
                    <b>syncStartTime</b>
                    <a class="ansibleOptionLink" href="#parameter-syncStartTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SAVAMapping&#x27;s syncStartTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-syncStatus"></div>
                    <b>syncStatus</b>
                    <a class="ansibleOptionLink" href="#parameter-syncStatus" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SAVAMapping&#x27;s syncStatus.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-tenantId"></div>
                    <b>tenantId</b>
                    <a class="ansibleOptionLink" href="#parameter-tenantId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SAVAMapping&#x27;s tenantId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-token"></div>
                    <b>token</b>
                    <a class="ansibleOptionLink" href="#parameter-token" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SAVAMapping&#x27;s token.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-virtualAccountId"></div>
                    <b>virtualAccountId</b>
                    <a class="ansibleOptionLink" href="#parameter-virtualAccountId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SAVAMapping&#x27;s virtualAccountId.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes


.. Seealso

See Also
--------

.. seealso::

   :ref:`cisco.dnac.plugins.module_utils.definitions.smart_virtual_account <ansible_collections.cisco.dnac.plugins.module_utils.definitions.smart_virtual_account_module>`
      The official documentation on the **cisco.dnac.plugins.module_utils.definitions.smart_virtual_account** module.
   `SmartVirtualAccount reference <https://developer.cisco.com/docs/dna-center/api/1-3-3-x>`_
       Complete reference of the SmartVirtualAccount object model.
   `SmartVirtualAccount reference <https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary>`_
       SDK reference.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: get_smart_account_list
      cisco.dnac.smart_virtual_account:
        state: query  # required
      register: nm_get_smart_account_list

    - name: get_virtual_account_list
      cisco.dnac.smart_virtual_account:
        state: query  # required
        domain: SomeValue  # string, required
      register: nm_get_virtual_account_list

    - name: add_virtual_account
      cisco.dnac.smart_virtual_account:
        state: create  # required
        profile:  # required
          addressFqdn: SomeValue  # string
          addressIpV4: SomeValue  # string
          cert: SomeValue  # string
          makeDefault: True  # boolean
          name: SomeValue  # string
          port: 1  #  integer
          profileId: SomeValue  # string
          proxy: True  # boolean
        smartAccountId: SomeValue  # string, required
        syncStatus: # valid values are 'NOT_SYNCED',
          # 'SYNCING',
          # 'SUCCESS',
          # 'FAILURE'.
          SomeValue  # string, required
        virtualAccountId: SomeValue  # string, required
        autoSyncPeriod: 1  #  integer
        ccoUser: SomeValue  # string
        expiry: 1  #  integer
        lastSync: 1  #  integer
        syncResult:
          syncList:
          - deviceSnList:
            - SomeValue  # string
            syncType: SomeValue  # string
          syncMsg: SomeValue  # string
        syncResultStr: SomeValue  # string
        syncStartTime: 1  #  integer
        tenantId: SomeValue  # string
        token: SomeValue  # string

    - name: update_pnp_server_profile
      cisco.dnac.smart_virtual_account:
        state: update  # required
        profile:  # required
          addressFqdn: SomeValue  # string
          addressIpV4: SomeValue  # string
          cert: SomeValue  # string
          makeDefault: True  # boolean
          name: SomeValue  # string
          port: 1  #  integer
          profileId: SomeValue  # string
          proxy: True  # boolean
        smartAccountId: SomeValue  # string, required
        syncStatus: # valid values are 'NOT_SYNCED',
          # 'SYNCING',
          # 'SUCCESS',
          # 'FAILURE'.
          SomeValue  # string, required
        virtualAccountId: SomeValue  # string, required
        autoSyncPeriod: 1  #  integer
        ccoUser: SomeValue  # string
        expiry: 1  #  integer
        lastSync: 1  #  integer
        syncResult:
          syncList:
          - deviceSnList:
            - SomeValue  # string
            syncType: SomeValue  # string
          syncMsg: SomeValue  # string
        syncResultStr: SomeValue  # string
        syncStartTime: 1  #  integer
        tenantId: SomeValue  # string
        token: SomeValue  # string

    - name: deregister_virtual_account
      cisco.dnac.smart_virtual_account:
        state: delete  # required
        domain: SomeValue  # string, required
        name: SomeValue  # string, required





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
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">device_onboarding_pnp.add_virtual_account</div>
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

