.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.cisco.dnac.discovery_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.dnac.discovery -- Manage Discovery objects of Discovery
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `cisco.dnac collection <https://galaxy.ansible.com/cisco/dnac>`_ (version 2.0.7).

    To install it use: :code:`ansible-galaxy collection install cisco.dnac`.

    To use it in a playbook, specify: :code:`cisco.dnac.discovery`.

.. version_added

.. versionadded:: 1.0.0 of cisco.dnac

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Stops all the discoveries and removes them.
- Initiates Discovery with the given parameters.
- Stops or starts an existing Discovery.
- Returns the count of all available Discovery jobs.
- Stops the Discovery for the given Discovery ID and removes it. Discovery ID can be obtained using the "Get Discoveries by range" API.

- Returns Discovery by Discovery ID. Discovery ID can be obtained using the "Get Discoveries by range" API.
- Stops Discovery for the given range and removes them.
- Returns the Discovery by specified range.

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
                    <div class="ansibleOptionAnchor" id="parameter-attributeInfo"></div>
                    <b>attributeInfo</b>
                    <a class="ansibleOptionLink" href="#parameter-attributeInfo" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>DiscoveryNIO&#x27;s attributeInfo.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-cdpLevel"></div>
                    <b>cdpLevel</b>
                    <a class="ansibleOptionLink" href="#parameter-cdpLevel" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s cdpLevel.</div>
                                            <div>DiscoveryNIO&#x27;s cdpLevel.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-deviceIds"></div>
                    <b>deviceIds</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceIds" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>DiscoveryNIO&#x27;s deviceIds.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-discoveryCondition"></div>
                    <b>discoveryCondition</b>
                    <a class="ansibleOptionLink" href="#parameter-discoveryCondition" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>DiscoveryNIO&#x27;s DiscoveryCondition.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-discoveryStatus"></div>
                    <b>discoveryStatus</b>
                    <a class="ansibleOptionLink" href="#parameter-discoveryStatus" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>DiscoveryNIO&#x27;s DiscoveryStatus.</div>
                                            <div>Required for state update.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-discoveryType"></div>
                    <b>discoveryType</b>
                    <a class="ansibleOptionLink" href="#parameter-discoveryType" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s DiscoveryType.</div>
                                            <div>DiscoveryNIO&#x27;s DiscoveryType.</div>
                                            <div>Required for state create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-enablePasswordList"></div>
                    <b>enablePasswordList</b>
                    <a class="ansibleOptionLink" href="#parameter-enablePasswordList" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s enablePasswordList (list of strings).</div>
                                            <div>DiscoveryNIO&#x27;s enablePasswordList.</div>
                                            <div>Type list for state create.</div>
                                            <div>Type str for state update.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-globalCredentialIdList"></div>
                    <b>globalCredentialIdList</b>
                    <a class="ansibleOptionLink" href="#parameter-globalCredentialIdList" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s globalCredentialIdList (list of strings).</div>
                                            <div>DiscoveryNIO&#x27;s globalCredentialIdList (list of strings).</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-httpReadCredential"></div>
                    <b>httpReadCredential</b>
                    <a class="ansibleOptionLink" href="#parameter-httpReadCredential" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s httpReadCredential.</div>
                                            <div>DiscoveryNIO&#x27;s httpReadCredential.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-httpReadCredential/comments"></div>
                    <b>comments</b>
                    <a class="ansibleOptionLink" href="#parameter-httpReadCredential/comments" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the Discovery&#x27;s comments.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-httpReadCredential/credentialType"></div>
                    <b>credentialType</b>
                    <a class="ansibleOptionLink" href="#parameter-httpReadCredential/credentialType" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the Discovery&#x27;s credentialType.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-httpReadCredential/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-httpReadCredential/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the Discovery&#x27;s description.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-httpReadCredential/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#parameter-httpReadCredential/id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the Discovery&#x27;s id.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-httpReadCredential/instanceTenantId"></div>
                    <b>instanceTenantId</b>
                    <a class="ansibleOptionLink" href="#parameter-httpReadCredential/instanceTenantId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the Discovery&#x27;s instanceTenantId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-httpReadCredential/instanceUuid"></div>
                    <b>instanceUuid</b>
                    <a class="ansibleOptionLink" href="#parameter-httpReadCredential/instanceUuid" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the Discovery&#x27;s instanceUuid.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-httpReadCredential/password"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-httpReadCredential/password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the Discovery&#x27;s password.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-httpReadCredential/port"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#parameter-httpReadCredential/port" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the Discovery&#x27;s port.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-httpReadCredential/secure"></div>
                    <b>secure</b>
                    <a class="ansibleOptionLink" href="#parameter-httpReadCredential/secure" title="Permalink to this option"></a>
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
                                            <div>It is the Discovery&#x27;s secure.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-httpReadCredential/username"></div>
                    <b>username</b>
                    <a class="ansibleOptionLink" href="#parameter-httpReadCredential/username" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the Discovery&#x27;s username.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-httpWriteCredential"></div>
                    <b>httpWriteCredential</b>
                    <a class="ansibleOptionLink" href="#parameter-httpWriteCredential" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s httpWriteCredential.</div>
                                            <div>DiscoveryNIO&#x27;s httpWriteCredential.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-httpWriteCredential/comments"></div>
                    <b>comments</b>
                    <a class="ansibleOptionLink" href="#parameter-httpWriteCredential/comments" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the Discovery&#x27;s comments.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-httpWriteCredential/credentialType"></div>
                    <b>credentialType</b>
                    <a class="ansibleOptionLink" href="#parameter-httpWriteCredential/credentialType" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the Discovery&#x27;s credentialType.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-httpWriteCredential/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-httpWriteCredential/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the Discovery&#x27;s description.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-httpWriteCredential/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#parameter-httpWriteCredential/id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the Discovery&#x27;s id.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-httpWriteCredential/instanceTenantId"></div>
                    <b>instanceTenantId</b>
                    <a class="ansibleOptionLink" href="#parameter-httpWriteCredential/instanceTenantId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the Discovery&#x27;s instanceTenantId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-httpWriteCredential/instanceUuid"></div>
                    <b>instanceUuid</b>
                    <a class="ansibleOptionLink" href="#parameter-httpWriteCredential/instanceUuid" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the Discovery&#x27;s instanceUuid.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-httpWriteCredential/password"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-httpWriteCredential/password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the Discovery&#x27;s password.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-httpWriteCredential/port"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#parameter-httpWriteCredential/port" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the Discovery&#x27;s port.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-httpWriteCredential/secure"></div>
                    <b>secure</b>
                    <a class="ansibleOptionLink" href="#parameter-httpWriteCredential/secure" title="Permalink to this option"></a>
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
                                            <div>It is the Discovery&#x27;s secure.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-httpWriteCredential/username"></div>
                    <b>username</b>
                    <a class="ansibleOptionLink" href="#parameter-httpWriteCredential/username" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the Discovery&#x27;s username.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
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
                                            <div>DiscoveryNIO&#x27;s id.</div>
                                            <div>Discovery ID.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-ipAddressList"></div>
                    <b>ipAddressList</b>
                    <a class="ansibleOptionLink" href="#parameter-ipAddressList" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s ipAddressList.</div>
                                            <div>DiscoveryNIO&#x27;s ipAddressList.</div>
                                            <div>Required for state create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-ipFilterList"></div>
                    <b>ipFilterList</b>
                    <a class="ansibleOptionLink" href="#parameter-ipFilterList" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s ipFilterList (list of strings).</div>
                                            <div>DiscoveryNIO&#x27;s ipFilterList.</div>
                                            <div>Type list for state create.</div>
                                            <div>Type str for state update.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-isAutoCdp"></div>
                    <b>isAutoCdp</b>
                    <a class="ansibleOptionLink" href="#parameter-isAutoCdp" title="Permalink to this option"></a>
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
                                            <div>DiscoveryNIO&#x27;s isAutoCdp.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-lldpLevel"></div>
                    <b>lldpLevel</b>
                    <a class="ansibleOptionLink" href="#parameter-lldpLevel" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s lldpLevel.</div>
                                            <div>DiscoveryNIO&#x27;s lldpLevel.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s name.</div>
                                            <div>DiscoveryNIO&#x27;s name.</div>
                                            <div>Required for state create.</div>
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
                                            <div>InventoryRequest&#x27;s netconfPort.</div>
                                            <div>DiscoveryNIO&#x27;s netconfPort.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-noAddNewDevice"></div>
                    <b>noAddNewDevice</b>
                    <a class="ansibleOptionLink" href="#parameter-noAddNewDevice" title="Permalink to this option"></a>
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
                                            <div>InventoryRequest&#x27;s noAddNewDevice.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-numDevices"></div>
                    <b>numDevices</b>
                    <a class="ansibleOptionLink" href="#parameter-numDevices" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>DiscoveryNIO&#x27;s numDevices.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-parentDiscoveryId"></div>
                    <b>parentDiscoveryId</b>
                    <a class="ansibleOptionLink" href="#parameter-parentDiscoveryId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s parentDiscoveryId.</div>
                                            <div>DiscoveryNIO&#x27;s parentDiscoveryId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-passwordList"></div>
                    <b>passwordList</b>
                    <a class="ansibleOptionLink" href="#parameter-passwordList" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s passwordList (list of strings).</div>
                                            <div>DiscoveryNIO&#x27;s passwordList.</div>
                                            <div>Type list for state create.</div>
                                            <div>Type str for state update.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-preferredMgmtIPMethod"></div>
                    <b>preferredMgmtIPMethod</b>
                    <a class="ansibleOptionLink" href="#parameter-preferredMgmtIPMethod" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s preferredMgmtIPMethod.</div>
                                            <div>DiscoveryNIO&#x27;s preferredMgmtIPMethod.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-protocolOrder"></div>
                    <b>protocolOrder</b>
                    <a class="ansibleOptionLink" href="#parameter-protocolOrder" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s protocolOrder.</div>
                                            <div>DiscoveryNIO&#x27;s protocolOrder.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-records_to_delete"></div>
                    <b>records_to_delete</b>
                    <a class="ansibleOptionLink" href="#parameter-records_to_delete" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of records to delete.</div>
                                            <div>Required for state delete.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-reDiscovery"></div>
                    <b>reDiscovery</b>
                    <a class="ansibleOptionLink" href="#parameter-reDiscovery" title="Permalink to this option"></a>
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
                                            <div>InventoryRequest&#x27;s reDiscovery.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-retry"></div>
                    <b>retry</b>
                    <a class="ansibleOptionLink" href="#parameter-retry" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s retry.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-retryCount"></div>
                    <b>retryCount</b>
                    <a class="ansibleOptionLink" href="#parameter-retryCount" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>DiscoveryNIO&#x27;s retryCount.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpAuthPassphrase"></div>
                    <b>snmpAuthPassphrase</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpAuthPassphrase" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s snmpAuthPassphrase.</div>
                                            <div>DiscoveryNIO&#x27;s snmpAuthPassphrase.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpAuthProtocol"></div>
                    <b>snmpAuthProtocol</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpAuthProtocol" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s snmpAuthProtocol.</div>
                                            <div>DiscoveryNIO&#x27;s snmpAuthProtocol.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpMode"></div>
                    <b>snmpMode</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpMode" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s snmpMode.</div>
                                            <div>DiscoveryNIO&#x27;s snmpMode.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpPrivPassphrase"></div>
                    <b>snmpPrivPassphrase</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpPrivPassphrase" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s snmpPrivPassphrase.</div>
                                            <div>DiscoveryNIO&#x27;s snmpPrivPassphrase.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpPrivProtocol"></div>
                    <b>snmpPrivProtocol</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpPrivProtocol" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s snmpPrivProtocol.</div>
                                            <div>DiscoveryNIO&#x27;s snmpPrivProtocol.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpROCommunity"></div>
                    <b>snmpROCommunity</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpROCommunity" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s snmpROCommunity.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpRoCommunity"></div>
                    <b>snmpRoCommunity</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpRoCommunity" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>DiscoveryNIO&#x27;s snmpRoCommunity.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpROCommunityDesc"></div>
                    <b>snmpROCommunityDesc</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpROCommunityDesc" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s snmpROCommunityDesc.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpRoCommunityDesc"></div>
                    <b>snmpRoCommunityDesc</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpRoCommunityDesc" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>DiscoveryNIO&#x27;s snmpRoCommunityDesc.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpRWCommunity"></div>
                    <b>snmpRWCommunity</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpRWCommunity" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s snmpRWCommunity.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpRwCommunity"></div>
                    <b>snmpRwCommunity</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpRwCommunity" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>DiscoveryNIO&#x27;s snmpRwCommunity.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpRWCommunityDesc"></div>
                    <b>snmpRWCommunityDesc</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpRWCommunityDesc" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s snmpRWCommunityDesc.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpRwCommunityDesc"></div>
                    <b>snmpRwCommunityDesc</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpRwCommunityDesc" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>DiscoveryNIO&#x27;s snmpRwCommunityDesc.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpUserName"></div>
                    <b>snmpUserName</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpUserName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s snmpUserName.</div>
                                            <div>DiscoveryNIO&#x27;s snmpUserName.</div>
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
                                            <div>InventoryRequest&#x27;s snmpVersion.</div>
                                            <div>Required for state create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-start_index"></div>
                    <b>start_index</b>
                    <a class="ansibleOptionLink" href="#parameter-start_index" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Start index.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-timeOut"></div>
                    <b>timeOut</b>
                    <a class="ansibleOptionLink" href="#parameter-timeOut" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>DiscoveryNIO&#x27;s timeOut.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-timeout"></div>
                    <b>timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-timeout" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s timeout.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-updateMgmtIp"></div>
                    <b>updateMgmtIp</b>
                    <a class="ansibleOptionLink" href="#parameter-updateMgmtIp" title="Permalink to this option"></a>
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
                                            <div>InventoryRequest&#x27;s updateMgmtIp.</div>
                                            <div>DiscoveryNIO&#x27;s updateMgmtIp.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-userNameList"></div>
                    <b>userNameList</b>
                    <a class="ansibleOptionLink" href="#parameter-userNameList" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>InventoryRequest&#x27;s userNameList (list of strings).</div>
                                            <div>DiscoveryNIO&#x27;s userNameList.</div>
                                            <div>Type list for state create.</div>
                                            <div>Type str for state update.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes


.. Seealso

See Also
--------

.. seealso::

   :ref:`cisco.dnac.plugins.module_utils.definitions.discovery <ansible_collections.cisco.dnac.plugins.module_utils.definitions.discovery_module>`
      The official documentation on the **cisco.dnac.plugins.module_utils.definitions.discovery** module.
   `Discovery reference <https://developer.cisco.com/docs/dna-center/api/1-3-3-x>`_
       Complete reference of the Discovery object model.
   `Discovery reference <https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary>`_
       SDK reference.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: delete_all_discovery
      cisco.dnac.discovery:
        state: delete  # required

    - name: start_discovery
      cisco.dnac.discovery:
        state: create  # required
        discoveryType: SomeValue  # string, required
        ipAddressList: SomeValue  # string, required
        name: SomeValue  # string, required
        snmpVersion: SomeValue  # string, required
        cdpLevel: 1  #  integer
        enablePasswordList:
        - SomeValue  # string
        globalCredentialIdList:
        - SomeValue  # string
        httpReadCredential:
          comments: SomeValue  # string
          credentialType: SomeValue  # string
          description: SomeValue  # string
          id: SomeValue  # string
          instanceTenantId: SomeValue  # string
          instanceUuid: SomeValue  # string
          password: SomeValue  # string
          port: 1  #  integer
          secure: True  # boolean
          username: SomeValue  # string
        httpWriteCredential:
          comments: SomeValue  # string
          credentialType: SomeValue  # string
          description: SomeValue  # string
          id: SomeValue  # string
          instanceTenantId: SomeValue  # string
          instanceUuid: SomeValue  # string
          password: SomeValue  # string
          port: 1  #  integer
          secure: True  # boolean
          username: SomeValue  # string
        ipFilterList:
        - SomeValue  # string
        lldpLevel: 1  #  integer
        netconfPort: SomeValue  # string
        noAddNewDevice: True  # boolean
        parentDiscoveryId: SomeValue  # string
        passwordList:
        - SomeValue  # string
        preferredMgmtIPMethod: SomeValue  # string
        protocolOrder: SomeValue  # string
        reDiscovery: True  # boolean
        retry: 1  #  integer
        snmpAuthPassphrase: SomeValue  # string
        snmpAuthProtocol: SomeValue  # string
        snmpMode: SomeValue  # string
        snmpPrivPassphrase: SomeValue  # string
        snmpPrivProtocol: SomeValue  # string
        snmpROCommunity: SomeValue  # string
        snmpROCommunityDesc: SomeValue  # string
        snmpRWCommunity: SomeValue  # string
        snmpRWCommunityDesc: SomeValue  # string
        snmpUserName: SomeValue  # string
        timeout: 1  #  integer
        updateMgmtIp: True  # boolean
        userNameList:
        - SomeValue  # string

    - name: updates_discovery_by_id
      cisco.dnac.discovery:
        state: update  # required
        discoveryStatus: SomeValue  # string, required
        id: SomeValue  # string, required
        attributeInfo:
        cdpLevel: 1  #  integer
        deviceIds: SomeValue  # string
        discoveryCondition: SomeValue  # string
        discoveryType: SomeValue  # string
        enablePasswordList: SomeValue  # string
        globalCredentialIdList:
        - SomeValue  # string
        httpReadCredential:
          comments: SomeValue  # string
          credentialType: SomeValue  # string
          description: SomeValue  # string
          id: SomeValue  # string
          instanceTenantId: SomeValue  # string
          instanceUuid: SomeValue  # string
          password: SomeValue  # string
          port: 1  #  integer
          secure: True  # boolean
          username: SomeValue  # string
        httpWriteCredential:
          comments: SomeValue  # string
          credentialType: SomeValue  # string
          description: SomeValue  # string
          id: SomeValue  # string
          instanceTenantId: SomeValue  # string
          instanceUuid: SomeValue  # string
          password: SomeValue  # string
          port: 1  #  integer
          secure: True  # boolean
          username: SomeValue  # string
        ipAddressList: SomeValue  # string
        ipFilterList: SomeValue  # string
        isAutoCdp: True  # boolean
        lldpLevel: 1  #  integer
        name: SomeValue  # string
        netconfPort: SomeValue  # string
        numDevices: 1  #  integer
        parentDiscoveryId: SomeValue  # string
        passwordList: SomeValue  # string
        preferredMgmtIPMethod: SomeValue  # string
        protocolOrder: SomeValue  # string
        retryCount: 1  #  integer
        snmpAuthPassphrase: SomeValue  # string
        snmpAuthProtocol: SomeValue  # string
        snmpMode: SomeValue  # string
        snmpPrivPassphrase: SomeValue  # string
        snmpPrivProtocol: SomeValue  # string
        snmpRoCommunity: SomeValue  # string
        snmpRoCommunityDesc: SomeValue  # string
        snmpRwCommunity: SomeValue  # string
        snmpRwCommunityDesc: SomeValue  # string
        snmpUserName: SomeValue  # string
        timeOut: 1  #  integer
        updateMgmtIp: True  # boolean
        userNameList: SomeValue  # string

    - name: get_count_of_all_discovery_jobs
      cisco.dnac.discovery:
        state: query  # required
        count: True  # boolean, required
      register: nm_get_count_of_all_discovery_jobs

    - name: delete_discovery_by_id
      cisco.dnac.discovery:
        state: delete  # required
        id: SomeValue  # string, required

    - name: get_discovery_by_id
      cisco.dnac.discovery:
        state: query  # required
        id: SomeValue  # string, required
      register: nm_get_discovery_by_id

    - name: delete_discovery_by_specified_range
      cisco.dnac.discovery:
        state: delete  # required
        records_to_delete: 1  #  integer, required
        start_index: 1  #  integer, required

    - name: get_discoveries_by_range
      cisco.dnac.discovery:
        state: query  # required
        records_to_return: 1  #  integer, required
        start_index: 1  #  integer, required
      register: nm_get_discoveries_by_range





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
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">discovery.delete_all_discovery</div>
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

