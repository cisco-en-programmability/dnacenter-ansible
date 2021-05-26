.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.cisco.dnac.wireless_rf_profile_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.dnac.wireless_rf_profile -- Manage WirelessRfProfile objects of Wireless
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `cisco.dnac collection <https://galaxy.ansible.com/cisco/dnac>`_ (version 2.0.7).

    To install it use: :code:`ansible-galaxy collection install cisco.dnac`.

    To use it in a playbook, specify: :code:`cisco.dnac.wireless_rf_profile`.

.. version_added

.. versionadded:: 1.0.0 of cisco.dnac

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Retrieve all RF profiles.
- Create or Update RF profile.
- Delete RF profile(s).

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
                    <div class="ansibleOptionAnchor" id="parameter-channelWidth"></div>
                    <b>channelWidth</b>
                    <a class="ansibleOptionLink" href="#parameter-channelWidth" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Channel Width, property of the request body.</div>
                                            <div>Required for state create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-defaultRfProfile"></div>
                    <b>defaultRfProfile</b>
                    <a class="ansibleOptionLink" href="#parameter-defaultRfProfile" title="Permalink to this option"></a>
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
                                            <div>DefaultRfProfile, property of the request body.</div>
                                            <div>Required for state create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-enableBrownField"></div>
                    <b>enableBrownField</b>
                    <a class="ansibleOptionLink" href="#parameter-enableBrownField" title="Permalink to this option"></a>
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
                                            <div>EnableBrownField, property of the request body.</div>
                                            <div>Required for state create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-enableCustom"></div>
                    <b>enableCustom</b>
                    <a class="ansibleOptionLink" href="#parameter-enableCustom" title="Permalink to this option"></a>
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
                                            <div>EnableCustom, property of the request body.</div>
                                            <div>Required for state create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-enableRadioTypeA"></div>
                    <b>enableRadioTypeA</b>
                    <a class="ansibleOptionLink" href="#parameter-enableRadioTypeA" title="Permalink to this option"></a>
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
                                            <div>EnableRadioTypeA, property of the request body.</div>
                                            <div>Required for state create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-enableRadioTypeB"></div>
                    <b>enableRadioTypeB</b>
                    <a class="ansibleOptionLink" href="#parameter-enableRadioTypeB" title="Permalink to this option"></a>
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
                                            <div>EnableRadioTypeB, property of the request body.</div>
                                            <div>Required for state create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                            <div>Name, property of the request body.</div>
                                            <div>Required for state create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-radioTypeAProperties"></div>
                    <b>radioTypeAProperties</b>
                    <a class="ansibleOptionLink" href="#parameter-radioTypeAProperties" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Radio Type AProperties, property of the request body.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-radioTypeAProperties/dataRates"></div>
                    <b>dataRates</b>
                    <a class="ansibleOptionLink" href="#parameter-radioTypeAProperties/dataRates" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the wireless rf profile&#x27;s dataRates.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-radioTypeAProperties/mandatoryDataRates"></div>
                    <b>mandatoryDataRates</b>
                    <a class="ansibleOptionLink" href="#parameter-radioTypeAProperties/mandatoryDataRates" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the wireless rf profile&#x27;s mandatoryDataRates.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-radioTypeAProperties/maxPowerLevel"></div>
                    <b>maxPowerLevel</b>
                    <a class="ansibleOptionLink" href="#parameter-radioTypeAProperties/maxPowerLevel" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the wireless rf profile&#x27;s maxPowerLevel.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-radioTypeAProperties/minPowerLevel"></div>
                    <b>minPowerLevel</b>
                    <a class="ansibleOptionLink" href="#parameter-radioTypeAProperties/minPowerLevel" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the wireless rf profile&#x27;s minPowerLevel.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-radioTypeAProperties/parentProfile"></div>
                    <b>parentProfile</b>
                    <a class="ansibleOptionLink" href="#parameter-radioTypeAProperties/parentProfile" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the wireless rf profile&#x27;s parentProfile.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-radioTypeAProperties/powerThresholdV1"></div>
                    <b>powerThresholdV1</b>
                    <a class="ansibleOptionLink" href="#parameter-radioTypeAProperties/powerThresholdV1" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the wireless rf profile&#x27;s powerThresholdV1.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-radioTypeAProperties/radioChannels"></div>
                    <b>radioChannels</b>
                    <a class="ansibleOptionLink" href="#parameter-radioTypeAProperties/radioChannels" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the wireless rf profile&#x27;s radioChannels.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-radioTypeAProperties/rxSopThreshold"></div>
                    <b>rxSopThreshold</b>
                    <a class="ansibleOptionLink" href="#parameter-radioTypeAProperties/rxSopThreshold" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the wireless rf profile&#x27;s rxSopThreshold.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-radioTypeBProperties"></div>
                    <b>radioTypeBProperties</b>
                    <a class="ansibleOptionLink" href="#parameter-radioTypeBProperties" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Radio Type BProperties, property of the request body.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-radioTypeBProperties/dataRates"></div>
                    <b>dataRates</b>
                    <a class="ansibleOptionLink" href="#parameter-radioTypeBProperties/dataRates" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the wireless rf profile&#x27;s dataRates.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-radioTypeBProperties/mandatoryDataRates"></div>
                    <b>mandatoryDataRates</b>
                    <a class="ansibleOptionLink" href="#parameter-radioTypeBProperties/mandatoryDataRates" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the wireless rf profile&#x27;s mandatoryDataRates.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-radioTypeBProperties/maxPowerLevel"></div>
                    <b>maxPowerLevel</b>
                    <a class="ansibleOptionLink" href="#parameter-radioTypeBProperties/maxPowerLevel" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the wireless rf profile&#x27;s maxPowerLevel.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-radioTypeBProperties/minPowerLevel"></div>
                    <b>minPowerLevel</b>
                    <a class="ansibleOptionLink" href="#parameter-radioTypeBProperties/minPowerLevel" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the wireless rf profile&#x27;s minPowerLevel.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-radioTypeBProperties/parentProfile"></div>
                    <b>parentProfile</b>
                    <a class="ansibleOptionLink" href="#parameter-radioTypeBProperties/parentProfile" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the wireless rf profile&#x27;s parentProfile.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-radioTypeBProperties/powerThresholdV1"></div>
                    <b>powerThresholdV1</b>
                    <a class="ansibleOptionLink" href="#parameter-radioTypeBProperties/powerThresholdV1" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the wireless rf profile&#x27;s powerThresholdV1.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-radioTypeBProperties/radioChannels"></div>
                    <b>radioChannels</b>
                    <a class="ansibleOptionLink" href="#parameter-radioTypeBProperties/radioChannels" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the wireless rf profile&#x27;s radioChannels.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-radioTypeBProperties/rxSopThreshold"></div>
                    <b>rxSopThreshold</b>
                    <a class="ansibleOptionLink" href="#parameter-radioTypeBProperties/rxSopThreshold" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It is the wireless rf profile&#x27;s rxSopThreshold.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-rf_profile_name"></div>
                    <b>rf_profile_name</b>
                    <a class="ansibleOptionLink" href="#parameter-rf_profile_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Rf-profile-name query parameter.</div>
                                            <div>Rf-profile-name path parameter.</div>
                                            <div>Required for state delete.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes


.. Seealso

See Also
--------

.. seealso::

   :ref:`cisco.dnac.plugins.module_utils.definitions.wireless_rf_profile <ansible_collections.cisco.dnac.plugins.module_utils.definitions.wireless_rf_profile_module>`
      The official documentation on the **cisco.dnac.plugins.module_utils.definitions.wireless_rf_profile** module.
   `WirelessRfProfile reference <https://developer.cisco.com/docs/dna-center/api/1-3-3-x>`_
       Complete reference of the WirelessRfProfile object model.
   `WirelessRfProfile reference <https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary>`_
       SDK reference.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: retrieve_rf_profiles
      cisco.dnac.wireless_rf_profile:
        state: query  # required
        rf_profile_name: SomeValue  # string
      register: nm_retrieve_rf_profiles

    - name: create_or_update_rf_profile
      cisco.dnac.wireless_rf_profile:
        state: create  # required
        channelWidth: SomeValue  # string, required
        defaultRfProfile: True  # boolean, required
        enableBrownField: True  # boolean, required
        enableCustom: True  # boolean, required
        enableRadioTypeA: True  # boolean, required
        enableRadioTypeB: True  # boolean, required
        name: SomeValue  # string, required
        radioTypeAProperties:
          parentProfile: SomeValue  # string
          radioChannels: SomeValue  # string
          dataRates: SomeValue  # string
          mandatoryDataRates: SomeValue  # string
          powerThresholdV1: 1  #  number
          rxSopThreshold: SomeValue  # string
          minPowerLevel: 1  #  number
          maxPowerLevel: 1  #  number
        radioTypeBProperties:
          parentProfile: SomeValue  # string
          radioChannels: SomeValue  # string
          dataRates: SomeValue  # string
          mandatoryDataRates: SomeValue  # string
          powerThresholdV1: 1  #  number
          rxSopThreshold: SomeValue  # string
          minPowerLevel: 1  #  number
          maxPowerLevel: 1  #  number

    - name: delete_rf_profiles
      cisco.dnac.wireless_rf_profile:
        state: delete  # required
        rf_profile_name: SomeValue  # string, required





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
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">wireless.create_or_update_rf_profile</div>
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

