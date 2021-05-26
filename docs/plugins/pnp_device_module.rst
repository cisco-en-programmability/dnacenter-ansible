.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.cisco.dnac.pnp_device_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.dnac.pnp_device -- Manage PnpDevice objects of DeviceOnboardingPnp
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `cisco.dnac collection <https://galaxy.ansible.com/cisco/dnac>`_ (version 2.0.7).

    To install it use: :code:`ansible-galaxy collection install cisco.dnac`.

    To use it in a playbook, specify: :code:`cisco.dnac.pnp_device`.

.. version_added

.. versionadded:: 1.0.0 of cisco.dnac

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Returns list of devices based on filter crieteria. If a limit is not specified, it will default to return 50 devices. Pagination and sorting are also supported by this endpoint.

- Adds a device to the PnP database.
- Returns device details specified by device id.
- Deletes specified device from PnP database.
- Updates device details specified by device id in PnP database.
- Returns the device count based on filter criteria. This is useful for pagination.
- Returns history for a specific device. Serial number is a required parameter.

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
            <th colspan="4">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-_id"></div>
                    <b>_id</b>
                    <a class="ansibleOptionLink" href="#parameter-_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device&#x27;s _id.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-_state"></div>
                    <b>_state</b>
                    <a class="ansibleOptionLink" href="#parameter-_state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device State.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-cm_state"></div>
                    <b>cm_state</b>
                    <a class="ansibleOptionLink" href="#parameter-cm_state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device Connection Manager State.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
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
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo"></div>
                    <b>deviceInfo</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device&#x27;s deviceInfo.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/aaaCredentials"></div>
                    <b>aaaCredentials</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/aaaCredentials" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s aaaCredentials.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/aaaCredentials/password"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/aaaCredentials/password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s password.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/aaaCredentials/username"></div>
                    <b>username</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/aaaCredentials/username" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s username.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/addedOn"></div>
                    <b>addedOn</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/addedOn" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s addedOn.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/addnMacAddrs"></div>
                    <b>addnMacAddrs</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/addnMacAddrs" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s addnMacAddrs.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/agentType"></div>
                    <b>agentType</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/agentType" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s agentType.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/authenticatedSudiSerialNo"></div>
                    <b>authenticatedSudiSerialNo</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/authenticatedSudiSerialNo" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s authenticatedSudiSerialNo.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/authStatus"></div>
                    <b>authStatus</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/authStatus" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s authStatus.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/capabilitiesSupported"></div>
                    <b>capabilitiesSupported</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/capabilitiesSupported" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s capabilitiesSupported.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/cmState"></div>
                    <b>cmState</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/cmState" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s cmState.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s description.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/deviceSudiSerialNos"></div>
                    <b>deviceSudiSerialNos</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/deviceSudiSerialNos" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s deviceSudiSerialNos.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/deviceType"></div>
                    <b>deviceType</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/deviceType" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s deviceType.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/featuresSupported"></div>
                    <b>featuresSupported</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/featuresSupported" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s featuresSupported.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/fileSystemList"></div>
                    <b>fileSystemList</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/fileSystemList" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s fileSystemList.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/fileSystemList/freespace"></div>
                    <b>freespace</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/fileSystemList/freespace" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s freespace.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/fileSystemList/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/fileSystemList/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/fileSystemList/readable"></div>
                    <b>readable</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/fileSystemList/readable" title="Permalink to this option"></a>
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
                                            <div>It is the pnp device&#x27;s readable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/fileSystemList/size"></div>
                    <b>size</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/fileSystemList/size" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s size.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/fileSystemList/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/fileSystemList/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/fileSystemList/writeable"></div>
                    <b>writeable</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/fileSystemList/writeable" title="Permalink to this option"></a>
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
                                            <div>It is the pnp device&#x27;s writeable.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/firstContact"></div>
                    <b>firstContact</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/firstContact" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s firstContact.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/hostname"></div>
                    <b>hostname</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/hostname" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s hostname.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/httpHeaders"></div>
                    <b>httpHeaders</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/httpHeaders" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s httpHeaders.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/httpHeaders/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/httpHeaders/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s key.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/httpHeaders/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/httpHeaders/value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s value.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/imageFile"></div>
                    <b>imageFile</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/imageFile" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s imageFile.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/imageVersion"></div>
                    <b>imageVersion</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/imageVersion" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s imageVersion.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/ipInterfaces"></div>
                    <b>ipInterfaces</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/ipInterfaces" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s ipInterfaces.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/ipInterfaces/ipv4Address"></div>
                    <b>ipv4Address</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/ipInterfaces/ipv4Address" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s ipv4Address.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/ipInterfaces/ipv6AddressList"></div>
                    <b>ipv6AddressList</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/ipInterfaces/ipv6AddressList" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s ipv6AddressList.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/ipInterfaces/macAddress"></div>
                    <b>macAddress</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/ipInterfaces/macAddress" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s macAddress.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/ipInterfaces/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/ipInterfaces/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/ipInterfaces/status"></div>
                    <b>status</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/ipInterfaces/status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s status.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/lastContact"></div>
                    <b>lastContact</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/lastContact" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s lastContact.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/lastSyncTime"></div>
                    <b>lastSyncTime</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/lastSyncTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s lastSyncTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/lastUpdateOn"></div>
                    <b>lastUpdateOn</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/lastUpdateOn" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s lastUpdateOn.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/location"></div>
                    <b>location</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/location" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s location.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/location/address"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/location/address" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s address.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/location/altitude"></div>
                    <b>altitude</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/location/altitude" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s altitude.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/location/latitude"></div>
                    <b>latitude</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/location/latitude" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s latitude.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/location/longitude"></div>
                    <b>longitude</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/location/longitude" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s longitude.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/location/siteId"></div>
                    <b>siteId</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/location/siteId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s siteId.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/macAddress"></div>
                    <b>macAddress</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/macAddress" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s macAddress.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/mode"></div>
                    <b>mode</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/mode" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s mode.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/neighborLinks"></div>
                    <b>neighborLinks</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/neighborLinks" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s neighborLinks.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/neighborLinks/localInterfaceName"></div>
                    <b>localInterfaceName</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/neighborLinks/localInterfaceName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s localInterfaceName.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/neighborLinks/localMacAddress"></div>
                    <b>localMacAddress</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/neighborLinks/localMacAddress" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s localMacAddress.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/neighborLinks/localShortInterfaceName"></div>
                    <b>localShortInterfaceName</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/neighborLinks/localShortInterfaceName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s localShortInterfaceName.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/neighborLinks/remoteDeviceName"></div>
                    <b>remoteDeviceName</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/neighborLinks/remoteDeviceName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s remoteDeviceName.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/neighborLinks/remoteInterfaceName"></div>
                    <b>remoteInterfaceName</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/neighborLinks/remoteInterfaceName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s remoteInterfaceName.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/neighborLinks/remoteMacAddress"></div>
                    <b>remoteMacAddress</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/neighborLinks/remoteMacAddress" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s remoteMacAddress.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/neighborLinks/remotePlatform"></div>
                    <b>remotePlatform</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/neighborLinks/remotePlatform" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s remotePlatform.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/neighborLinks/remoteShortInterfaceName"></div>
                    <b>remoteShortInterfaceName</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/neighborLinks/remoteShortInterfaceName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s remoteShortInterfaceName.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/neighborLinks/remoteVersion"></div>
                    <b>remoteVersion</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/neighborLinks/remoteVersion" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s remoteVersion.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/onbState"></div>
                    <b>onbState</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/onbState" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s onbState.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/pid"></div>
                    <b>pid</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/pid" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s pid.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/pnpProfileList"></div>
                    <b>pnpProfileList</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/pnpProfileList" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s pnpProfileList.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/pnpProfileList/createdBy"></div>
                    <b>createdBy</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/pnpProfileList/createdBy" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s createdBy.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/pnpProfileList/discoveryCreated"></div>
                    <b>discoveryCreated</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/pnpProfileList/discoveryCreated" title="Permalink to this option"></a>
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
                                            <div>It is the pnp device&#x27;s discoveryCreated.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/pnpProfileList/primaryEndpoint"></div>
                    <b>primaryEndpoint</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/pnpProfileList/primaryEndpoint" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s primaryEndpoint.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/pnpProfileList/primaryEndpoint/certificate"></div>
                    <b>certificate</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/pnpProfileList/primaryEndpoint/certificate" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s certificate.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/pnpProfileList/primaryEndpoint/fqdn"></div>
                    <b>fqdn</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/pnpProfileList/primaryEndpoint/fqdn" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s fqdn.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/pnpProfileList/primaryEndpoint/ipv4Address"></div>
                    <b>ipv4Address</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/pnpProfileList/primaryEndpoint/ipv4Address" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s ipv4Address.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/pnpProfileList/primaryEndpoint/ipv6Address"></div>
                    <b>ipv6Address</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/pnpProfileList/primaryEndpoint/ipv6Address" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s ipv6Address.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/pnpProfileList/primaryEndpoint/port"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/pnpProfileList/primaryEndpoint/port" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s port.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/pnpProfileList/primaryEndpoint/protocol"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/pnpProfileList/primaryEndpoint/protocol" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s protocol.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/pnpProfileList/profileName"></div>
                    <b>profileName</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/pnpProfileList/profileName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s profileName.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/pnpProfileList/secondaryEndpoint"></div>
                    <b>secondaryEndpoint</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/pnpProfileList/secondaryEndpoint" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s secondaryEndpoint.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/pnpProfileList/secondaryEndpoint/certificate"></div>
                    <b>certificate</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/pnpProfileList/secondaryEndpoint/certificate" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s certificate.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/pnpProfileList/secondaryEndpoint/fqdn"></div>
                    <b>fqdn</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/pnpProfileList/secondaryEndpoint/fqdn" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s fqdn.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/pnpProfileList/secondaryEndpoint/ipv4Address"></div>
                    <b>ipv4Address</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/pnpProfileList/secondaryEndpoint/ipv4Address" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s ipv4Address.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/pnpProfileList/secondaryEndpoint/ipv6Address"></div>
                    <b>ipv6Address</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/pnpProfileList/secondaryEndpoint/ipv6Address" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s ipv6Address.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/pnpProfileList/secondaryEndpoint/port"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/pnpProfileList/secondaryEndpoint/port" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s port.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/pnpProfileList/secondaryEndpoint/protocol"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/pnpProfileList/secondaryEndpoint/protocol" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s protocol.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/populateInventory"></div>
                    <b>populateInventory</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/populateInventory" title="Permalink to this option"></a>
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
                                            <div>It is the pnp device&#x27;s populateInventory.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/preWorkflowCliOuputs"></div>
                    <b>preWorkflowCliOuputs</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/preWorkflowCliOuputs" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s preWorkflowCliOuputs.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/preWorkflowCliOuputs/cli"></div>
                    <b>cli</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/preWorkflowCliOuputs/cli" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s cli.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/preWorkflowCliOuputs/cliOutput"></div>
                    <b>cliOutput</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/preWorkflowCliOuputs/cliOutput" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s cliOutput.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/projectId"></div>
                    <b>projectId</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/projectId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s projectId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/projectName"></div>
                    <b>projectName</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/projectName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s projectName.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/reloadRequested"></div>
                    <b>reloadRequested</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/reloadRequested" title="Permalink to this option"></a>
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
                                            <div>It is the pnp device&#x27;s reloadRequested.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/serialNumber"></div>
                    <b>serialNumber</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/serialNumber" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s serialNumber.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/smartAccountId"></div>
                    <b>smartAccountId</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/smartAccountId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s smartAccountId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/source"></div>
                    <b>source</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/source" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s source.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/stack"></div>
                    <b>stack</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/stack" title="Permalink to this option"></a>
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
                                            <div>It is the pnp device&#x27;s stack.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/stackInfo"></div>
                    <b>stackInfo</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/stackInfo" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s stackInfo.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/stackInfo/isFullRing"></div>
                    <b>isFullRing</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/stackInfo/isFullRing" title="Permalink to this option"></a>
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
                                            <div>It is the pnp device&#x27;s isFullRing.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/stackInfo/stackMemberList"></div>
                    <b>stackMemberList</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/stackInfo/stackMemberList" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s stackMemberList.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/stackInfo/stackMemberList/hardwareVersion"></div>
                    <b>hardwareVersion</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/stackInfo/stackMemberList/hardwareVersion" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s hardwareVersion.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/stackInfo/stackMemberList/licenseLevel"></div>
                    <b>licenseLevel</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/stackInfo/stackMemberList/licenseLevel" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s licenseLevel.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/stackInfo/stackMemberList/licenseType"></div>
                    <b>licenseType</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/stackInfo/stackMemberList/licenseType" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s licenseType.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/stackInfo/stackMemberList/macAddress"></div>
                    <b>macAddress</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/stackInfo/stackMemberList/macAddress" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s macAddress.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/stackInfo/stackMemberList/pid"></div>
                    <b>pid</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/stackInfo/stackMemberList/pid" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s pid.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/stackInfo/stackMemberList/priority"></div>
                    <b>priority</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/stackInfo/stackMemberList/priority" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s priority.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/stackInfo/stackMemberList/role"></div>
                    <b>role</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/stackInfo/stackMemberList/role" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s role.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/stackInfo/stackMemberList/serialNumber"></div>
                    <b>serialNumber</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/stackInfo/stackMemberList/serialNumber" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s serialNumber.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/stackInfo/stackMemberList/softwareVersion"></div>
                    <b>softwareVersion</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/stackInfo/stackMemberList/softwareVersion" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s softwareVersion.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/stackInfo/stackMemberList/stackNumber"></div>
                    <b>stackNumber</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/stackInfo/stackMemberList/stackNumber" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s stackNumber.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/stackInfo/stackMemberList/state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/stackInfo/stackMemberList/state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s state.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/stackInfo/stackMemberList/sudiSerialNumber"></div>
                    <b>sudiSerialNumber</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/stackInfo/stackMemberList/sudiSerialNumber" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s sudiSerialNumber.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/stackInfo/stackRingProtocol"></div>
                    <b>stackRingProtocol</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/stackInfo/stackRingProtocol" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s stackRingProtocol.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/stackInfo/supportsStackWorkflows"></div>
                    <b>supportsStackWorkflows</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/stackInfo/supportsStackWorkflows" title="Permalink to this option"></a>
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
                                            <div>It is the pnp device&#x27;s supportsStackWorkflows.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/stackInfo/totalMemberCount"></div>
                    <b>totalMemberCount</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/stackInfo/totalMemberCount" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s totalMemberCount.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/stackInfo/validLicenseLevels"></div>
                    <b>validLicenseLevels</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/stackInfo/validLicenseLevels" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s validLicenseLevels.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s state.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/sudiRequired"></div>
                    <b>sudiRequired</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/sudiRequired" title="Permalink to this option"></a>
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
                                            <div>It is the pnp device&#x27;s sudiRequired.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/tags"></div>
                    <b>tags</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s tags.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/userSudiSerialNos"></div>
                    <b>userSudiSerialNos</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/userSudiSerialNos" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s userSudiSerialNos.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/virtualAccountId"></div>
                    <b>virtualAccountId</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/virtualAccountId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s virtualAccountId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/workflowId"></div>
                    <b>workflowId</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/workflowId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s workflowId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deviceInfo/workflowName"></div>
                    <b>workflowName</b>
                    <a class="ansibleOptionLink" href="#parameter-deviceInfo/workflowName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s workflowName.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="4">
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
                                            <div>Id path parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-last_contact"></div>
                    <b>last_contact</b>
                    <a class="ansibleOptionLink" href="#parameter-last_contact" title="Permalink to this option"></a>
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
                                            <div>Device Has Contacted lastContact &gt; 0.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-limit"></div>
                    <b>limit</b>
                    <a class="ansibleOptionLink" href="#parameter-limit" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Limits number of results.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
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
                                            <div>Device Name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-offset"></div>
                    <b>offset</b>
                    <a class="ansibleOptionLink" href="#parameter-offset" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Index of first result.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-onb_state"></div>
                    <b>onb_state</b>
                    <a class="ansibleOptionLink" href="#parameter-onb_state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device Onboarding State.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-pid"></div>
                    <b>pid</b>
                    <a class="ansibleOptionLink" href="#parameter-pid" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device ProductId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-project_id"></div>
                    <b>project_id</b>
                    <a class="ansibleOptionLink" href="#parameter-project_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device Project Id.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-project_name"></div>
                    <b>project_name</b>
                    <a class="ansibleOptionLink" href="#parameter-project_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device Project Name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-runSummaryList"></div>
                    <b>runSummaryList</b>
                    <a class="ansibleOptionLink" href="#parameter-runSummaryList" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device&#x27;s runSummaryList (list of objects).</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-runSummaryList/details"></div>
                    <b>details</b>
                    <a class="ansibleOptionLink" href="#parameter-runSummaryList/details" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s details.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-runSummaryList/errorFlag"></div>
                    <b>errorFlag</b>
                    <a class="ansibleOptionLink" href="#parameter-runSummaryList/errorFlag" title="Permalink to this option"></a>
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
                                            <div>It is the pnp device&#x27;s errorFlag.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-runSummaryList/historyTaskInfo"></div>
                    <b>historyTaskInfo</b>
                    <a class="ansibleOptionLink" href="#parameter-runSummaryList/historyTaskInfo" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s historyTaskInfo.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-runSummaryList/historyTaskInfo/addnDetails"></div>
                    <b>addnDetails</b>
                    <a class="ansibleOptionLink" href="#parameter-runSummaryList/historyTaskInfo/addnDetails" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s addnDetails.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-runSummaryList/historyTaskInfo/addnDetails/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-runSummaryList/historyTaskInfo/addnDetails/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s key.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-runSummaryList/historyTaskInfo/addnDetails/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-runSummaryList/historyTaskInfo/addnDetails/value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s value.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-runSummaryList/historyTaskInfo/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-runSummaryList/historyTaskInfo/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-runSummaryList/historyTaskInfo/timeTaken"></div>
                    <b>timeTaken</b>
                    <a class="ansibleOptionLink" href="#parameter-runSummaryList/historyTaskInfo/timeTaken" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s timeTaken.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-runSummaryList/historyTaskInfo/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-runSummaryList/historyTaskInfo/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-runSummaryList/historyTaskInfo/workItemList"></div>
                    <b>workItemList</b>
                    <a class="ansibleOptionLink" href="#parameter-runSummaryList/historyTaskInfo/workItemList" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s workItemList.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-runSummaryList/historyTaskInfo/workItemList/command"></div>
                    <b>command</b>
                    <a class="ansibleOptionLink" href="#parameter-runSummaryList/historyTaskInfo/workItemList/command" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s command.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-runSummaryList/historyTaskInfo/workItemList/endTime"></div>
                    <b>endTime</b>
                    <a class="ansibleOptionLink" href="#parameter-runSummaryList/historyTaskInfo/workItemList/endTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s endTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-runSummaryList/historyTaskInfo/workItemList/outputStr"></div>
                    <b>outputStr</b>
                    <a class="ansibleOptionLink" href="#parameter-runSummaryList/historyTaskInfo/workItemList/outputStr" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s outputStr.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-runSummaryList/historyTaskInfo/workItemList/startTime"></div>
                    <b>startTime</b>
                    <a class="ansibleOptionLink" href="#parameter-runSummaryList/historyTaskInfo/workItemList/startTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s startTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-runSummaryList/historyTaskInfo/workItemList/state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-runSummaryList/historyTaskInfo/workItemList/state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s state.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-runSummaryList/historyTaskInfo/workItemList/timeTaken"></div>
                    <b>timeTaken</b>
                    <a class="ansibleOptionLink" href="#parameter-runSummaryList/historyTaskInfo/workItemList/timeTaken" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s timeTaken.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-runSummaryList/timestamp"></div>
                    <b>timestamp</b>
                    <a class="ansibleOptionLink" href="#parameter-runSummaryList/timestamp" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s timestamp.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="4">
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
                                            <div>Device Serial Number.</div>
                                            <div>Required for state query.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-smart_account_id"></div>
                    <b>smart_account_id</b>
                    <a class="ansibleOptionLink" href="#parameter-smart_account_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device Smart Account.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-sort"></div>
                    <b>sort</b>
                    <a class="ansibleOptionLink" href="#parameter-sort" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Comma seperated list of fields to sort on.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-sort_order"></div>
                    <b>sort_order</b>
                    <a class="ansibleOptionLink" href="#parameter-sort_order" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Sort Order Ascending (asc) or Descending (des).</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-source"></div>
                    <b>source</b>
                    <a class="ansibleOptionLink" href="#parameter-source" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device Source.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow"></div>
                    <b>systemResetWorkflow</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device&#x27;s systemResetWorkflow.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/_id"></div>
                    <b>_id</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s _id.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/addedOn"></div>
                    <b>addedOn</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/addedOn" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s addedOn.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/addToInventory"></div>
                    <b>addToInventory</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/addToInventory" title="Permalink to this option"></a>
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
                                            <div>It is the pnp device&#x27;s addToInventory.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/configId"></div>
                    <b>configId</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/configId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s configId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/currTaskIdx"></div>
                    <b>currTaskIdx</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/currTaskIdx" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s currTaskIdx.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s description.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/endTime"></div>
                    <b>endTime</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/endTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s endTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/execTime"></div>
                    <b>execTime</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/execTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s execTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/imageId"></div>
                    <b>imageId</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/imageId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s imageId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/instanceType"></div>
                    <b>instanceType</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/instanceType" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s instanceType.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/lastupdateOn"></div>
                    <b>lastupdateOn</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/lastupdateOn" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s lastupdateOn.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/startTime"></div>
                    <b>startTime</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/startTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s startTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s state.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/tasks"></div>
                    <b>tasks</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/tasks" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s tasks.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/tasks/currWorkItemIdx"></div>
                    <b>currWorkItemIdx</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/tasks/currWorkItemIdx" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s currWorkItemIdx.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/tasks/endTime"></div>
                    <b>endTime</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/tasks/endTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s endTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/tasks/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/tasks/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/tasks/startTime"></div>
                    <b>startTime</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/tasks/startTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s startTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/tasks/state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/tasks/state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s state.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/tasks/taskSeqNo"></div>
                    <b>taskSeqNo</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/tasks/taskSeqNo" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s taskSeqNo.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/tasks/timeTaken"></div>
                    <b>timeTaken</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/tasks/timeTaken" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s timeTaken.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/tasks/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/tasks/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/tasks/workItemList"></div>
                    <b>workItemList</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/tasks/workItemList" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s workItemList.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/tasks/workItemList/command"></div>
                    <b>command</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/tasks/workItemList/command" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s command.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/tasks/workItemList/endTime"></div>
                    <b>endTime</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/tasks/workItemList/endTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s endTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/tasks/workItemList/outputStr"></div>
                    <b>outputStr</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/tasks/workItemList/outputStr" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s outputStr.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/tasks/workItemList/startTime"></div>
                    <b>startTime</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/tasks/workItemList/startTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s startTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/tasks/workItemList/state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/tasks/workItemList/state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s state.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/tasks/workItemList/timeTaken"></div>
                    <b>timeTaken</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/tasks/workItemList/timeTaken" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s timeTaken.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/tenantId"></div>
                    <b>tenantId</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/tenantId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s tenantId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/useState"></div>
                    <b>useState</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/useState" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s useState.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemResetWorkflow/version"></div>
                    <b>version</b>
                    <a class="ansibleOptionLink" href="#parameter-systemResetWorkflow/version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s version.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow"></div>
                    <b>systemWorkflow</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device&#x27;s systemWorkflow.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/_id"></div>
                    <b>_id</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s _id.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/addedOn"></div>
                    <b>addedOn</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/addedOn" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s addedOn.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/addToInventory"></div>
                    <b>addToInventory</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/addToInventory" title="Permalink to this option"></a>
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
                                            <div>It is the pnp device&#x27;s addToInventory.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/configId"></div>
                    <b>configId</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/configId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s configId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/currTaskIdx"></div>
                    <b>currTaskIdx</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/currTaskIdx" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s currTaskIdx.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s description.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/endTime"></div>
                    <b>endTime</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/endTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s endTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/execTime"></div>
                    <b>execTime</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/execTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s execTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/imageId"></div>
                    <b>imageId</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/imageId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s imageId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/instanceType"></div>
                    <b>instanceType</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/instanceType" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s instanceType.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/lastupdateOn"></div>
                    <b>lastupdateOn</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/lastupdateOn" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s lastupdateOn.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/startTime"></div>
                    <b>startTime</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/startTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s startTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s state.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/tasks"></div>
                    <b>tasks</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/tasks" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s tasks.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/tasks/currWorkItemIdx"></div>
                    <b>currWorkItemIdx</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/tasks/currWorkItemIdx" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s currWorkItemIdx.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/tasks/endTime"></div>
                    <b>endTime</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/tasks/endTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s endTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/tasks/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/tasks/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/tasks/startTime"></div>
                    <b>startTime</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/tasks/startTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s startTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/tasks/state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/tasks/state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s state.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/tasks/taskSeqNo"></div>
                    <b>taskSeqNo</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/tasks/taskSeqNo" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s taskSeqNo.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/tasks/timeTaken"></div>
                    <b>timeTaken</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/tasks/timeTaken" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s timeTaken.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/tasks/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/tasks/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/tasks/workItemList"></div>
                    <b>workItemList</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/tasks/workItemList" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s workItemList.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/tasks/workItemList/command"></div>
                    <b>command</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/tasks/workItemList/command" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s command.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/tasks/workItemList/endTime"></div>
                    <b>endTime</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/tasks/workItemList/endTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s endTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/tasks/workItemList/outputStr"></div>
                    <b>outputStr</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/tasks/workItemList/outputStr" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s outputStr.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/tasks/workItemList/startTime"></div>
                    <b>startTime</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/tasks/workItemList/startTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s startTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/tasks/workItemList/state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/tasks/workItemList/state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s state.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/tasks/workItemList/timeTaken"></div>
                    <b>timeTaken</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/tasks/workItemList/timeTaken" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s timeTaken.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/tenantId"></div>
                    <b>tenantId</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/tenantId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s tenantId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/useState"></div>
                    <b>useState</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/useState" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s useState.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-systemWorkflow/version"></div>
                    <b>version</b>
                    <a class="ansibleOptionLink" href="#parameter-systemWorkflow/version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s version.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="4">
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
                                            <div>Device&#x27;s tenantId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-version"></div>
                    <b>version</b>
                    <a class="ansibleOptionLink" href="#parameter-version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device&#x27;s version.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-virtual_account_id"></div>
                    <b>virtual_account_id</b>
                    <a class="ansibleOptionLink" href="#parameter-virtual_account_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device Virtual Account.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-workflow"></div>
                    <b>workflow</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device&#x27;s workflow.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/_id"></div>
                    <b>_id</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s _id.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/addedOn"></div>
                    <b>addedOn</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/addedOn" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s addedOn.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/addToInventory"></div>
                    <b>addToInventory</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/addToInventory" title="Permalink to this option"></a>
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
                                            <div>It is the pnp device&#x27;s addToInventory.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/configId"></div>
                    <b>configId</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/configId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s configId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/currTaskIdx"></div>
                    <b>currTaskIdx</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/currTaskIdx" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s currTaskIdx.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s description.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/endTime"></div>
                    <b>endTime</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/endTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s endTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/execTime"></div>
                    <b>execTime</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/execTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s execTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/imageId"></div>
                    <b>imageId</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/imageId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s imageId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/instanceType"></div>
                    <b>instanceType</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/instanceType" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s instanceType.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/lastupdateOn"></div>
                    <b>lastupdateOn</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/lastupdateOn" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s lastupdateOn.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/startTime"></div>
                    <b>startTime</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/startTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s startTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s state.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/tasks"></div>
                    <b>tasks</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/tasks" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s tasks.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/tasks/currWorkItemIdx"></div>
                    <b>currWorkItemIdx</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/tasks/currWorkItemIdx" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s currWorkItemIdx.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/tasks/endTime"></div>
                    <b>endTime</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/tasks/endTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s endTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/tasks/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/tasks/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/tasks/startTime"></div>
                    <b>startTime</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/tasks/startTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s startTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/tasks/state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/tasks/state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s state.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/tasks/taskSeqNo"></div>
                    <b>taskSeqNo</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/tasks/taskSeqNo" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s taskSeqNo.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/tasks/timeTaken"></div>
                    <b>timeTaken</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/tasks/timeTaken" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s timeTaken.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/tasks/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/tasks/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/tasks/workItemList"></div>
                    <b>workItemList</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/tasks/workItemList" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s workItemList.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/tasks/workItemList/command"></div>
                    <b>command</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/tasks/workItemList/command" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s command.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/tasks/workItemList/endTime"></div>
                    <b>endTime</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/tasks/workItemList/endTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s endTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/tasks/workItemList/outputStr"></div>
                    <b>outputStr</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/tasks/workItemList/outputStr" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s outputStr.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/tasks/workItemList/startTime"></div>
                    <b>startTime</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/tasks/workItemList/startTime" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s startTime.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/tasks/workItemList/state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/tasks/workItemList/state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s state.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/tasks/workItemList/timeTaken"></div>
                    <b>timeTaken</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/tasks/workItemList/timeTaken" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s timeTaken.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/tenantId"></div>
                    <b>tenantId</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/tenantId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s tenantId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/useState"></div>
                    <b>useState</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/useState" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s useState.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflow/version"></div>
                    <b>version</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow/version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s version.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-workflow_id"></div>
                    <b>workflow_id</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device Workflow Id.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-workflow_name"></div>
                    <b>workflow_name</b>
                    <a class="ansibleOptionLink" href="#parameter-workflow_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device Workflow Name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-workflowParameters"></div>
                    <b>workflowParameters</b>
                    <a class="ansibleOptionLink" href="#parameter-workflowParameters" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device&#x27;s workflowParameters.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflowParameters/configList"></div>
                    <b>configList</b>
                    <a class="ansibleOptionLink" href="#parameter-workflowParameters/configList" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s configList.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-workflowParameters/configList/configId"></div>
                    <b>configId</b>
                    <a class="ansibleOptionLink" href="#parameter-workflowParameters/configList/configId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s configId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-workflowParameters/configList/configParameters"></div>
                    <b>configParameters</b>
                    <a class="ansibleOptionLink" href="#parameter-workflowParameters/configList/configParameters" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s configParameters.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-workflowParameters/configList/configParameters/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-workflowParameters/configList/configParameters/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s key.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-workflowParameters/configList/configParameters/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-workflowParameters/configList/configParameters/value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s value.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflowParameters/licenseLevel"></div>
                    <b>licenseLevel</b>
                    <a class="ansibleOptionLink" href="#parameter-workflowParameters/licenseLevel" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s licenseLevel.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflowParameters/licenseType"></div>
                    <b>licenseType</b>
                    <a class="ansibleOptionLink" href="#parameter-workflowParameters/licenseType" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s licenseType.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-workflowParameters/topOfStackSerialNumber"></div>
                    <b>topOfStackSerialNumber</b>
                    <a class="ansibleOptionLink" href="#parameter-workflowParameters/topOfStackSerialNumber" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the pnp device&#x27;s topOfStackSerialNumber.</div>
                                                        </td>
            </tr>
                    
                        </table>
    <br/>

.. Notes


.. Seealso

See Also
--------

.. seealso::

   :ref:`cisco.dnac.plugins.module_utils.definitions.pnp_device <ansible_collections.cisco.dnac.plugins.module_utils.definitions.pnp_device_module>`
      The official documentation on the **cisco.dnac.plugins.module_utils.definitions.pnp_device** module.
   `PnpDevice reference <https://developer.cisco.com/docs/dna-center/api/1-3-3-x>`_
       Complete reference of the PnpDevice object model.
   `PnpDevice reference <https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary>`_
       SDK reference.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: get_device_list
      cisco.dnac.pnp_device:
        state: query  # required
        cm_state: SomeValue  # string
        last_contact: True  # boolean
        limit: 1  #  integer
        name: SomeValue  # string
        offset: 1  #  integer
        onb_state: SomeValue  # string
        pid: SomeValue  # string
        project_id: SomeValue  # string
        project_name: SomeValue  # string
        serial_number: SomeValue  # string
        smart_account_id: SomeValue  # string
        sort: SomeValue  # string
        sort_order: SomeValue  # string
        source: SomeValue  # string
        _state: SomeValue  # string
        virtual_account_id: SomeValue  # string
        workflow_id: SomeValue  # string
        workflow_name: SomeValue  # string
      register: nm_get_device_list

    - name: add_device
      cisco.dnac.pnp_device:
        state: create  # required
        deviceInfo:  # required
          aaaCredentials:
            password: SomeValue  # string
            username: SomeValue  # string
          addedOn: 1  #  integer
          addnMacAddrs:
          - SomeValue  # string
          agentType: SomeValue  # string
          authStatus: SomeValue  # string
          authenticatedSudiSerialNo: SomeValue  # string
          capabilitiesSupported:
          - SomeValue  # string
          cmState: SomeValue  # string
          description: SomeValue  # string
          deviceSudiSerialNos:
          - SomeValue  # string
          deviceType: SomeValue  # string
          featuresSupported:
          - SomeValue  # string
          fileSystemList:
          - freespace: 1  #  integer
            name: SomeValue  # string
            readable: True  # boolean
            size: 1  #  integer
            type: SomeValue  # string
            writeable: True  # boolean
          firstContact: 1  #  integer
          hostname: SomeValue  # string
          httpHeaders:
          - key: SomeValue  # string
            value: SomeValue  # string
          imageFile: SomeValue  # string
          imageVersion: SomeValue  # string
          ipInterfaces:
          - ipv4Address: None
            ipv6AddressList:
            macAddress: SomeValue  # string
            name: SomeValue  # string
            status: SomeValue  # string
          lastContact: 1  #  integer
          lastSyncTime: 1  #  integer
          lastUpdateOn: 1  #  integer
          location:
            address: SomeValue  # string
            altitude: SomeValue  # string
            latitude: SomeValue  # string
            longitude: SomeValue  # string
            siteId: SomeValue  # string
          macAddress: SomeValue  # string
          mode: SomeValue  # string
          name: SomeValue  # string
          neighborLinks:
          - localInterfaceName: SomeValue  # string
            localMacAddress: SomeValue  # string
            localShortInterfaceName: SomeValue  # string
            remoteDeviceName: SomeValue  # string
            remoteInterfaceName: SomeValue  # string
            remoteMacAddress: SomeValue  # string
            remotePlatform: SomeValue  # string
            remoteShortInterfaceName: SomeValue  # string
            remoteVersion: SomeValue  # string
          onbState: SomeValue  # string
          pid: SomeValue  # string
          pnpProfileList:
          - createdBy: SomeValue  # string
            discoveryCreated: True  # boolean
            primaryEndpoint:
              certificate: SomeValue  # string
              fqdn: SomeValue  # string
              ipv4Address: None
              ipv6Address: None
              port: 1  #  integer
              protocol: SomeValue  # string
            profileName: SomeValue  # string
            secondaryEndpoint:
              certificate: SomeValue  # string
              fqdn: SomeValue  # string
              ipv4Address: None
              ipv6Address: None
              port: 1  #  integer
              protocol: SomeValue  # string
          populateInventory: True  # boolean
          preWorkflowCliOuputs:
          - cli: SomeValue  # string
            cliOutput: SomeValue  # string
          projectId: SomeValue  # string
          projectName: SomeValue  # string
          reloadRequested: True  # boolean
          serialNumber: SomeValue  # string
          smartAccountId: SomeValue  # string
          source: SomeValue  # string
          stack: True  # boolean
          stackInfo:
            isFullRing: True  # boolean
            stackMemberList:
            - hardwareVersion: SomeValue  # string
              licenseLevel: SomeValue  # string
              licenseType: SomeValue  # string
              macAddress: SomeValue  # string
              pid: SomeValue  # string
              priority: 1  #  integer
              role: SomeValue  # string
              serialNumber: SomeValue  # string
              softwareVersion: SomeValue  # string
              stackNumber: 1  #  integer
              state: SomeValue  # string
              sudiSerialNumber: SomeValue  # string
            stackRingProtocol: SomeValue  # string
            supportsStackWorkflows: True  # boolean
            totalMemberCount: 1  #  integer
            validLicenseLevels:
            - SomeValue  # string
          state: SomeValue  # string
          sudiRequired: True  # boolean
          tags: None
          userSudiSerialNos:
          - SomeValue  # string
          virtualAccountId: SomeValue  # string
          workflowId: SomeValue  # string
          workflowName: SomeValue  # string
        _id: SomeValue  # string
        runSummaryList:
        - details: SomeValue  # string
          errorFlag: True  # boolean
          historyTaskInfo:
            addnDetails:
            - key: SomeValue  # string
              value: SomeValue  # string
            name: SomeValue  # string
            timeTaken: 1  #  integer
            type: SomeValue  # string
            workItemList:
            - command: SomeValue  # string
              endTime: 1  #  integer
              outputStr: SomeValue  # string
              startTime: 1  #  integer
              state: SomeValue  # string
              timeTaken: 1  #  integer
          timestamp: 1  #  integer
        systemResetWorkflow:
          _id: SomeValue  # string
          addToInventory: True  # boolean
          addedOn: 1  #  integer
          configId: SomeValue  # string
          currTaskIdx: 1  #  integer
          description: SomeValue  # string
          endTime: 1  #  integer
          execTime: 1  #  integer
          imageId: SomeValue  # string
          instanceType: SomeValue  # string
          lastupdateOn: 1  #  integer
          name: SomeValue  # string
          startTime: 1  #  integer
          state: SomeValue  # string
          tasks:
          - currWorkItemIdx: 1  #  integer
            endTime: 1  #  integer
            name: SomeValue  # string
            startTime: 1  #  integer
            state: SomeValue  # string
            taskSeqNo: 1  #  integer
            timeTaken: 1  #  integer
            type: SomeValue  # string
            workItemList:
            - command: SomeValue  # string
              endTime: 1  #  integer
              outputStr: SomeValue  # string
              startTime: 1  #  integer
              state: SomeValue  # string
              timeTaken: 1  #  integer
          tenantId: SomeValue  # string
          type: SomeValue  # string
          useState: SomeValue  # string
          version: 1  #  integer
        systemWorkflow:
          _id: SomeValue  # string
          addToInventory: True  # boolean
          addedOn: 1  #  integer
          configId: SomeValue  # string
          currTaskIdx: 1  #  integer
          description: SomeValue  # string
          endTime: 1  #  integer
          execTime: 1  #  integer
          imageId: SomeValue  # string
          instanceType: SomeValue  # string
          lastupdateOn: 1  #  integer
          name: SomeValue  # string
          startTime: 1  #  integer
          state: SomeValue  # string
          tasks:
          - currWorkItemIdx: 1  #  integer
            endTime: 1  #  integer
            name: SomeValue  # string
            startTime: 1  #  integer
            state: SomeValue  # string
            taskSeqNo: 1  #  integer
            timeTaken: 1  #  integer
            type: SomeValue  # string
            workItemList:
            - command: SomeValue  # string
              endTime: 1  #  integer
              outputStr: SomeValue  # string
              startTime: 1  #  integer
              state: SomeValue  # string
              timeTaken: 1  #  integer
          tenantId: SomeValue  # string
          type: SomeValue  # string
          useState: SomeValue  # string
          version: 1  #  integer
        tenantId: SomeValue  # string
        version: 1  #  integer
        workflow:
          _id: SomeValue  # string
          addToInventory: True  # boolean
          addedOn: 1  #  integer
          configId: SomeValue  # string
          currTaskIdx: 1  #  integer
          description: SomeValue  # string
          endTime: 1  #  integer
          execTime: 1  #  integer
          imageId: SomeValue  # string
          instanceType: SomeValue  # string
          lastupdateOn: 1  #  integer
          name: SomeValue  # string
          startTime: 1  #  integer
          state: SomeValue  # string
          tasks:
          - currWorkItemIdx: 1  #  integer
            endTime: 1  #  integer
            name: SomeValue  # string
            startTime: 1  #  integer
            state: SomeValue  # string
            taskSeqNo: 1  #  integer
            timeTaken: 1  #  integer
            type: SomeValue  # string
            workItemList:
            - command: SomeValue  # string
              endTime: 1  #  integer
              outputStr: SomeValue  # string
              startTime: 1  #  integer
              state: SomeValue  # string
              timeTaken: 1  #  integer
          tenantId: SomeValue  # string
          type: SomeValue  # string
          useState: SomeValue  # string
          version: 1  #  integer
        workflowParameters:
          configList:
          - configId: SomeValue  # string
            configParameters:
            - key: SomeValue  # string
              value: SomeValue  # string
          licenseLevel: SomeValue  # string
          licenseType: SomeValue  # string
          topOfStackSerialNumber: SomeValue  # string

    - name: get_device_by_id
      cisco.dnac.pnp_device:
        state: query  # required
        id: SomeValue  # string, required
      register: nm_get_device_by_id

    - name: delete_device_by_id_from_pnp
      cisco.dnac.pnp_device:
        state: delete  # required
        id: SomeValue  # string, required

    - name: update_device
      cisco.dnac.pnp_device:
        state: update  # required
        id: SomeValue  # string, required
        deviceInfo:  # required
          aaaCredentials:
            password: SomeValue  # string
            username: SomeValue  # string
          addedOn: 1  #  integer
          addnMacAddrs:
          - SomeValue  # string
          agentType: SomeValue  # string
          authStatus: SomeValue  # string
          authenticatedSudiSerialNo: SomeValue  # string
          capabilitiesSupported:
          - SomeValue  # string
          cmState: SomeValue  # string
          description: SomeValue  # string
          deviceSudiSerialNos:
          - SomeValue  # string
          deviceType: SomeValue  # string
          featuresSupported:
          - SomeValue  # string
          fileSystemList:
          - freespace: 1  #  integer
            name: SomeValue  # string
            readable: True  # boolean
            size: 1  #  integer
            type: SomeValue  # string
            writeable: True  # boolean
          firstContact: 1  #  integer
          hostname: SomeValue  # string
          httpHeaders:
          - key: SomeValue  # string
            value: SomeValue  # string
          imageFile: SomeValue  # string
          imageVersion: SomeValue  # string
          ipInterfaces:
          - ipv4Address: None
            ipv6AddressList:
            macAddress: SomeValue  # string
            name: SomeValue  # string
            status: SomeValue  # string
          lastContact: 1  #  integer
          lastSyncTime: 1  #  integer
          lastUpdateOn: 1  #  integer
          location:
            address: SomeValue  # string
            altitude: SomeValue  # string
            latitude: SomeValue  # string
            longitude: SomeValue  # string
            siteId: SomeValue  # string
          macAddress: SomeValue  # string
          mode: SomeValue  # string
          name: SomeValue  # string
          neighborLinks:
          - localInterfaceName: SomeValue  # string
            localMacAddress: SomeValue  # string
            localShortInterfaceName: SomeValue  # string
            remoteDeviceName: SomeValue  # string
            remoteInterfaceName: SomeValue  # string
            remoteMacAddress: SomeValue  # string
            remotePlatform: SomeValue  # string
            remoteShortInterfaceName: SomeValue  # string
            remoteVersion: SomeValue  # string
          onbState: SomeValue  # string
          pid: SomeValue  # string
          pnpProfileList:
          - createdBy: SomeValue  # string
            discoveryCreated: True  # boolean
            primaryEndpoint:
              certificate: SomeValue  # string
              fqdn: SomeValue  # string
              ipv4Address: None
              ipv6Address: None
              port: 1  #  integer
              protocol: SomeValue  # string
            profileName: SomeValue  # string
            secondaryEndpoint:
              certificate: SomeValue  # string
              fqdn: SomeValue  # string
              ipv4Address: None
              ipv6Address: None
              port: 1  #  integer
              protocol: SomeValue  # string
          populateInventory: True  # boolean
          preWorkflowCliOuputs:
          - cli: SomeValue  # string
            cliOutput: SomeValue  # string
          projectId: SomeValue  # string
          projectName: SomeValue  # string
          reloadRequested: True  # boolean
          serialNumber: SomeValue  # string
          smartAccountId: SomeValue  # string
          source: SomeValue  # string
          stack: True  # boolean
          stackInfo:
            isFullRing: True  # boolean
            stackMemberList:
            - hardwareVersion: SomeValue  # string
              licenseLevel: SomeValue  # string
              licenseType: SomeValue  # string
              macAddress: SomeValue  # string
              pid: SomeValue  # string
              priority: 1  #  integer
              role: SomeValue  # string
              serialNumber: SomeValue  # string
              softwareVersion: SomeValue  # string
              stackNumber: 1  #  integer
              state: SomeValue  # string
              sudiSerialNumber: SomeValue  # string
            stackRingProtocol: SomeValue  # string
            supportsStackWorkflows: True  # boolean
            totalMemberCount: 1  #  integer
            validLicenseLevels:
            - SomeValue  # string
          state: SomeValue  # string
          sudiRequired: True  # boolean
          tags: None
          userSudiSerialNos:
          - SomeValue  # string
          virtualAccountId: SomeValue  # string
          workflowId: SomeValue  # string
          workflowName: SomeValue  # string
        _id: SomeValue  # string
        runSummaryList:
        - details: SomeValue  # string
          errorFlag: True  # boolean
          historyTaskInfo:
            addnDetails:
            - key: SomeValue  # string
              value: SomeValue  # string
            name: SomeValue  # string
            timeTaken: 1  #  integer
            type: SomeValue  # string
            workItemList:
            - command: SomeValue  # string
              endTime: 1  #  integer
              outputStr: SomeValue  # string
              startTime: 1  #  integer
              state: SomeValue  # string
              timeTaken: 1  #  integer
          timestamp: 1  #  integer
        systemResetWorkflow:
          _id: SomeValue  # string
          addToInventory: True  # boolean
          addedOn: 1  #  integer
          configId: SomeValue  # string
          currTaskIdx: 1  #  integer
          description: SomeValue  # string
          endTime: 1  #  integer
          execTime: 1  #  integer
          imageId: SomeValue  # string
          instanceType: SomeValue  # string
          lastupdateOn: 1  #  integer
          name: SomeValue  # string
          startTime: 1  #  integer
          state: SomeValue  # string
          tasks:
          - currWorkItemIdx: 1  #  integer
            endTime: 1  #  integer
            name: SomeValue  # string
            startTime: 1  #  integer
            state: SomeValue  # string
            taskSeqNo: 1  #  integer
            timeTaken: 1  #  integer
            type: SomeValue  # string
            workItemList:
            - command: SomeValue  # string
              endTime: 1  #  integer
              outputStr: SomeValue  # string
              startTime: 1  #  integer
              state: SomeValue  # string
              timeTaken: 1  #  integer
          tenantId: SomeValue  # string
          type: SomeValue  # string
          useState: SomeValue  # string
          version: 1  #  integer
        systemWorkflow:
          _id: SomeValue  # string
          addToInventory: True  # boolean
          addedOn: 1  #  integer
          configId: SomeValue  # string
          currTaskIdx: 1  #  integer
          description: SomeValue  # string
          endTime: 1  #  integer
          execTime: 1  #  integer
          imageId: SomeValue  # string
          instanceType: SomeValue  # string
          lastupdateOn: 1  #  integer
          name: SomeValue  # string
          startTime: 1  #  integer
          state: SomeValue  # string
          tasks:
          - currWorkItemIdx: 1  #  integer
            endTime: 1  #  integer
            name: SomeValue  # string
            startTime: 1  #  integer
            state: SomeValue  # string
            taskSeqNo: 1  #  integer
            timeTaken: 1  #  integer
            type: SomeValue  # string
            workItemList:
            - command: SomeValue  # string
              endTime: 1  #  integer
              outputStr: SomeValue  # string
              startTime: 1  #  integer
              state: SomeValue  # string
              timeTaken: 1  #  integer
          tenantId: SomeValue  # string
          type: SomeValue  # string
          useState: SomeValue  # string
          version: 1  #  integer
        tenantId: SomeValue  # string
        version: 1  #  integer
        workflow:
          _id: SomeValue  # string
          addToInventory: True  # boolean
          addedOn: 1  #  integer
          configId: SomeValue  # string
          currTaskIdx: 1  #  integer
          description: SomeValue  # string
          endTime: 1  #  integer
          execTime: 1  #  integer
          imageId: SomeValue  # string
          instanceType: SomeValue  # string
          lastupdateOn: 1  #  integer
          name: SomeValue  # string
          startTime: 1  #  integer
          state: SomeValue  # string
          tasks:
          - currWorkItemIdx: 1  #  integer
            endTime: 1  #  integer
            name: SomeValue  # string
            startTime: 1  #  integer
            state: SomeValue  # string
            taskSeqNo: 1  #  integer
            timeTaken: 1  #  integer
            type: SomeValue  # string
            workItemList:
            - command: SomeValue  # string
              endTime: 1  #  integer
              outputStr: SomeValue  # string
              startTime: 1  #  integer
              state: SomeValue  # string
              timeTaken: 1  #  integer
          tenantId: SomeValue  # string
          type: SomeValue  # string
          useState: SomeValue  # string
          version: 1  #  integer
        workflowParameters:
          configList:
          - configId: SomeValue  # string
            configParameters:
            - key: SomeValue  # string
              value: SomeValue  # string
          licenseLevel: SomeValue  # string
          licenseType: SomeValue  # string
          topOfStackSerialNumber: SomeValue  # string

    - name: get_device_count
      cisco.dnac.pnp_device:
        state: query  # required
        count: True  # boolean, required
        cm_state: SomeValue  # string
        last_contact: True  # boolean
        name: SomeValue  # string
        onb_state: SomeValue  # string
        pid: SomeValue  # string
        project_id: SomeValue  # string
        project_name: SomeValue  # string
        serial_number: SomeValue  # string
        smart_account_id: SomeValue  # string
        source: SomeValue  # string
        _state: SomeValue  # string
        virtual_account_id: SomeValue  # string
        workflow_id: SomeValue  # string
        workflow_name: SomeValue  # string
      register: nm_get_device_count

    - name: get_device_history
      cisco.dnac.pnp_device:
        state: query  # required
        serial_number: SomeValue  # string, required
        sort: SomeValue  # string
        sort_order: SomeValue  # string
      register: nm_get_device_history





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
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">device_onboarding_pnp.add_device</div>
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

