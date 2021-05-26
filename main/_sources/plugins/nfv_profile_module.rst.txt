.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.cisco.dnac.nfv_profile_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.dnac.nfv_profile -- Manage NfvProfile objects of SiteDesign
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `cisco.dnac collection <https://galaxy.ansible.com/cisco/dnac>`_ (version 2.0.7).

    To install it use: :code:`ansible-galaxy collection install cisco.dnac`.

    To use it in a playbook, specify: :code:`cisco.dnac.nfv_profile`.

.. version_added

.. versionadded:: 1.0.0 of cisco.dnac

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- API to create network profile for different NFV topologies.
- API to get NFV network profile.
- API to delete nfv network profile.
- API to update a NFV Network profile.

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
                    <div class="ansibleOptionAnchor" id="parameter-device"></div>
                    <b>device</b>
                    <a class="ansibleOptionLink" href="#parameter-device" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device, property of the request body (list of objects).</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-device/currentDeviceTag"></div>
                    <b>currentDeviceTag</b>
                    <a class="ansibleOptionLink" href="#parameter-device/currentDeviceTag" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s currentDeviceTag.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-device/customNetworks"></div>
                    <b>customNetworks</b>
                    <a class="ansibleOptionLink" href="#parameter-device/customNetworks" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s customNetworks.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-device/customNetworks/connectionType"></div>
                    <b>connectionType</b>
                    <a class="ansibleOptionLink" href="#parameter-device/customNetworks/connectionType" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s connectionType.</div>
                                            <div>Required for states update and create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-device/customNetworks/networkName"></div>
                    <b>networkName</b>
                    <a class="ansibleOptionLink" href="#parameter-device/customNetworks/networkName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s networkName.</div>
                                            <div>Required for states update and create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-device/customNetworks/servicesToConnect"></div>
                    <b>servicesToConnect</b>
                    <a class="ansibleOptionLink" href="#parameter-device/customNetworks/servicesToConnect" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s servicesToConnect.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-device/customNetworks/servicesToConnect/serviceName"></div>
                    <b>serviceName</b>
                    <a class="ansibleOptionLink" href="#parameter-device/customNetworks/servicesToConnect/serviceName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s serviceName.</div>
                                            <div>Required for states update and create.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-device/customNetworks/vlanId"></div>
                    <b>vlanId</b>
                    <a class="ansibleOptionLink" href="#parameter-device/customNetworks/vlanId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s vlanId.</div>
                                            <div>Required for states update and create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-device/customNetworks/vlanMode"></div>
                    <b>vlanMode</b>
                    <a class="ansibleOptionLink" href="#parameter-device/customNetworks/vlanMode" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s vlanMode.</div>
                                            <div>Required for states update and create.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-device/customTemplate"></div>
                    <b>customTemplate</b>
                    <a class="ansibleOptionLink" href="#parameter-device/customTemplate" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s customTemplate.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-device/customTemplate/deviceType"></div>
                    <b>deviceType</b>
                    <a class="ansibleOptionLink" href="#parameter-device/customTemplate/deviceType" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s deviceType.</div>
                                            <div>Required for states update and create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-device/customTemplate/template"></div>
                    <b>template</b>
                    <a class="ansibleOptionLink" href="#parameter-device/customTemplate/template" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s template.</div>
                                            <div>Required for states update and create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-device/customTemplate/templateType"></div>
                    <b>templateType</b>
                    <a class="ansibleOptionLink" href="#parameter-device/customTemplate/templateType" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s templateType.</div>
                                            <div>Required for states update and create.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-device/deviceTag"></div>
                    <b>deviceTag</b>
                    <a class="ansibleOptionLink" href="#parameter-device/deviceTag" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s deviceTag.</div>
                                            <div>Required for states update and create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-device/deviceType"></div>
                    <b>deviceType</b>
                    <a class="ansibleOptionLink" href="#parameter-device/deviceType" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s deviceType.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-device/directInternetAccessForFirewall"></div>
                    <b>directInternetAccessForFirewall</b>
                    <a class="ansibleOptionLink" href="#parameter-device/directInternetAccessForFirewall" title="Permalink to this option"></a>
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
                                            <div>It is the nfv profile&#x27;s directInternetAccessForFirewall.</div>
                                            <div>Required for states update and create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-device/serviceProviderProfile"></div>
                    <b>serviceProviderProfile</b>
                    <a class="ansibleOptionLink" href="#parameter-device/serviceProviderProfile" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s serviceProviderProfile.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-device/serviceProviderProfile/connect"></div>
                    <b>connect</b>
                    <a class="ansibleOptionLink" href="#parameter-device/serviceProviderProfile/connect" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s connect.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-device/serviceProviderProfile/connectDefaultGatewayOnWan"></div>
                    <b>connectDefaultGatewayOnWan</b>
                    <a class="ansibleOptionLink" href="#parameter-device/serviceProviderProfile/connectDefaultGatewayOnWan" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s connectDefaultGatewayOnWan.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-device/serviceProviderProfile/linkType"></div>
                    <b>linkType</b>
                    <a class="ansibleOptionLink" href="#parameter-device/serviceProviderProfile/linkType" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s linkType.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-device/serviceProviderProfile/serviceProvider"></div>
                    <b>serviceProvider</b>
                    <a class="ansibleOptionLink" href="#parameter-device/serviceProviderProfile/serviceProvider" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s serviceProvider.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-device/services"></div>
                    <b>services</b>
                    <a class="ansibleOptionLink" href="#parameter-device/services" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s services.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-device/services/firewallMode"></div>
                    <b>firewallMode</b>
                    <a class="ansibleOptionLink" href="#parameter-device/services/firewallMode" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s firewallMode.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-device/services/imageName"></div>
                    <b>imageName</b>
                    <a class="ansibleOptionLink" href="#parameter-device/services/imageName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s imageName.</div>
                                            <div>Required for states update and create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-device/services/profileType"></div>
                    <b>profileType</b>
                    <a class="ansibleOptionLink" href="#parameter-device/services/profileType" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s profileType.</div>
                                            <div>Required for states update and create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-device/services/serviceName"></div>
                    <b>serviceName</b>
                    <a class="ansibleOptionLink" href="#parameter-device/services/serviceName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s serviceName.</div>
                                            <div>Required for states update and create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-device/services/serviceType"></div>
                    <b>serviceType</b>
                    <a class="ansibleOptionLink" href="#parameter-device/services/serviceType" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s serviceType.</div>
                                            <div>Required for states update and create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-device/services/vNicMapping"></div>
                    <b>vNicMapping</b>
                    <a class="ansibleOptionLink" href="#parameter-device/services/vNicMapping" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s vNicMapping.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-device/services/vNicMapping/assignIpAddressToNetwork"></div>
                    <b>assignIpAddressToNetwork</b>
                    <a class="ansibleOptionLink" href="#parameter-device/services/vNicMapping/assignIpAddressToNetwork" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s assignIpAddressToNetwork.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-device/services/vNicMapping/networkType"></div>
                    <b>networkType</b>
                    <a class="ansibleOptionLink" href="#parameter-device/services/vNicMapping/networkType" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s networkType.</div>
                                            <div>Required for states update and create.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-device/vlanForL2"></div>
                    <b>vlanForL2</b>
                    <a class="ansibleOptionLink" href="#parameter-device/vlanForL2" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s vlanForL2.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-device/vlanForL2/vlanDescription"></div>
                    <b>vlanDescription</b>
                    <a class="ansibleOptionLink" href="#parameter-device/vlanForL2/vlanDescription" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s vlanDescription.</div>
                                            <div>Required for states update and create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-device/vlanForL2/vlanId"></div>
                    <b>vlanId</b>
                    <a class="ansibleOptionLink" href="#parameter-device/vlanForL2/vlanId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s vlanId.</div>
                                            <div>Required for states update and create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-device/vlanForL2/vlanType"></div>
                    <b>vlanType</b>
                    <a class="ansibleOptionLink" href="#parameter-device/vlanForL2/vlanType" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the nfv profile&#x27;s vlanType.</div>
                                            <div>Required for states update and create.</div>
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
                                            <div>ID of network profile to retrieve.</div>
                                            <div>Id of nfv network profile to delete. .</div>
                                            <div>Id of the NFV profile to be updated.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-limit"></div>
                    <b>limit</b>
                    <a class="ansibleOptionLink" href="#parameter-limit" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of profile to be retrieved.</div>
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
                                            <div>Name of network profile to be retrieved.</div>
                                            <div>Nameof nfv network profile to delete. .</div>
                                            <div>Name of the profile to be updated.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-offset"></div>
                    <b>offset</b>
                    <a class="ansibleOptionLink" href="#parameter-offset" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Offset/starting row.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-profileName"></div>
                    <b>profileName</b>
                    <a class="ansibleOptionLink" href="#parameter-profileName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Site Profile Name, property of the request body.</div>
                                            <div>Required for state create.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes


.. Seealso

See Also
--------

.. seealso::

   :ref:`cisco.dnac.plugins.module_utils.definitions.nfv_profile <ansible_collections.cisco.dnac.plugins.module_utils.definitions.nfv_profile_module>`
      The official documentation on the **cisco.dnac.plugins.module_utils.definitions.nfv_profile** module.
   `NfvProfile reference <https://developer.cisco.com/docs/dna-center/api/1-3-3-x>`_
       Complete reference of the NfvProfile object model.
   `NfvProfile reference <https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary>`_
       SDK reference.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: create_nfv_profile
      cisco.dnac.nfv_profile:
        state: create  # required
        device:  # required
        - deviceType: SomeValue  # string, required
          deviceTag: SomeValue  # string, required
          serviceProviderProfile:  # required
          - serviceProvider: SomeValue  # string, required
            linkType: SomeValue  # string, required
            connect: True  # boolean, required
            connectDefaultGatewayOnWan: True  # boolean, required
          directInternetAccessForFirewall: True  # boolean, required
          services:  # required
          - serviceType: SomeValue  # string, required
            profileType: SomeValue  # string, required
            serviceName: SomeValue  # string, required
            imageName: SomeValue  # string, required
            vNicMapping:  # required
            - networkType: SomeValue  # string, required
              assignIpAddressToNetwork: SomeValue  # string
            firewallMode: SomeValue  # string
          customNetworks:
          - networkName: SomeValue  # string, required
            servicesToConnect:  # required
            - serviceName: SomeValue  # string, required
            connectionType: SomeValue  # string, required
            vlanMode: SomeValue  # string, required
            vlanId: 1  #  number, required
          vlanForL2:
          - vlanType: SomeValue  # string, required
            vlanId: 1  #  number, required
            vlanDescription: SomeValue  # string, required
          customTemplate:
          - deviceType: SomeValue  # string, required
            template: SomeValue  # string, required
            templateType: SomeValue  # string, required
        profileName: SomeValue  # string, required

    - name: get_nfv_profile
      cisco.dnac.nfv_profile:
        state: query  # required
        id: SomeValue  # string, required
        limit: SomeValue  # string
        name: SomeValue  # string
        offset: SomeValue  # string
      register: nm_get_nfv_profile

    - name: delete_nfv_profile
      cisco.dnac.nfv_profile:
        state: delete  # required
        id: SomeValue  # string, required
        name: SomeValue  # string

    - name: update_nfv_profile
      cisco.dnac.nfv_profile:
        state: update  # required
        id: SomeValue  # string, required
        device:  # required
        - deviceTag: SomeValue  # string, required
          directInternetAccessForFirewall: True  # boolean, required
          currentDeviceTag: SomeValue  # string, required
          services:
          - serviceType: SomeValue  # string, required
            profileType: SomeValue  # string, required
            serviceName: SomeValue  # string, required
            imageName: SomeValue  # string, required
            vNicMapping:  # required
            - networkType: SomeValue  # string, required
              assignIpAddressToNetwork: SomeValue  # string
            firewallMode: SomeValue  # string
          customNetworks:
          - networkName: SomeValue  # string, required
            servicesToConnect:  # required
            - serviceName: SomeValue  # string, required
            connectionType: SomeValue  # string, required
            vlanMode: SomeValue  # string, required
            vlanId: 1  #  number, required
          vlanForL2:
          - vlanType: SomeValue  # string, required
            vlanId: 1  #  number, required
            vlanDescription: SomeValue  # string, required
          customTemplate:
          - deviceType: SomeValue  # string, required
            template: SomeValue  # string, required
            templateType: SomeValue  # string, required
        name: SomeValue  # string





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
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">site_design.create_nfv_profile</div>
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

