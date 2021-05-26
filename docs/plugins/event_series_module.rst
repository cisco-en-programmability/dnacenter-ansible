.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.cisco.dnac.event_series_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.dnac.event_series -- Manage EventSeries objects of EventManagement
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `cisco.dnac collection <https://galaxy.ansible.com/cisco/dnac>`_ (version 2.0.7).

    To install it use: :code:`ansible-galaxy collection install cisco.dnac`.

    To use it in a playbook, specify: :code:`cisco.dnac.event_series`.

.. version_added

.. versionadded:: 1.0.0 of cisco.dnac

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Get the list of Published Notifications.
- Get the Count of Published Notifications.

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
                    <div class="ansibleOptionAnchor" id="parameter-category"></div>
                    <b>category</b>
                    <a class="ansibleOptionLink" href="#parameter-category" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Category .</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-count"></div>
                    <b>count</b>
                    <a class="ansibleOptionLink" href="#parameter-count" title="Permalink to this option"></a>
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
                                            <div>If true gets the number of objects.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-domain"></div>
                    <b>domain</b>
                    <a class="ansibleOptionLink" href="#parameter-domain" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Domain .</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-end_time"></div>
                    <b>end_time</b>
                    <a class="ansibleOptionLink" href="#parameter-end_time" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>EndTime .</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-event_ids"></div>
                    <b>event_ids</b>
                    <a class="ansibleOptionLink" href="#parameter-event_ids" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The registered EventIds should be provided.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
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
                                            <div>Limit whose default value 10.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
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
                                            <div>Offset whose default value 0.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-order"></div>
                    <b>order</b>
                    <a class="ansibleOptionLink" href="#parameter-order" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Order query parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-severity"></div>
                    <b>severity</b>
                    <a class="ansibleOptionLink" href="#parameter-severity" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Severity .</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-sort_by"></div>
                    <b>sort_by</b>
                    <a class="ansibleOptionLink" href="#parameter-sort_by" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SortBy field name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
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
                                            <div>Source .</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-start_time"></div>
                    <b>start_time</b>
                    <a class="ansibleOptionLink" href="#parameter-start_time" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>StartTime .</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-sub_domain"></div>
                    <b>sub_domain</b>
                    <a class="ansibleOptionLink" href="#parameter-sub_domain" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SubDomain .</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
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
                                            <div>Type .</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes


.. Seealso

See Also
--------

.. seealso::

   :ref:`cisco.dnac.plugins.module_utils.definitions.event_series <ansible_collections.cisco.dnac.plugins.module_utils.definitions.event_series_module>`
      The official documentation on the **cisco.dnac.plugins.module_utils.definitions.event_series** module.
   `EventSeries reference <https://developer.cisco.com/docs/dna-center/api/1-3-3-x>`_
       Complete reference of the EventSeries object model.
   `EventSeries reference <https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary>`_
       SDK reference.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: get_notifications
      cisco.dnac.event_series:
        state: query  # required
        category: SomeValue  # string
        domain: SomeValue  # string
        end_time: SomeValue  # string
        event_ids: SomeValue  # string
        limit: 1  #  number
        offset: 1  #  number
        order: SomeValue  # string
        severity: SomeValue  # string
        sort_by: SomeValue  # string
        source: SomeValue  # string
        start_time: SomeValue  # string
        sub_domain: SomeValue  # string
        type: SomeValue  # string
      register: nm_get_notifications

    - name: count_of_notifications
      cisco.dnac.event_series:
        state: query  # required
        count: True  # boolean, required
        category: SomeValue  # string
        domain: SomeValue  # string
        end_time: SomeValue  # string
        event_ids: SomeValue  # string
        severity: SomeValue  # string
        source: SomeValue  # string
        start_time: SomeValue  # string
        sub_domain: SomeValue  # string
        type: SomeValue  # string
      register: nm_count_of_notifications





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
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">event_management.count_of_notifications</div>
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

