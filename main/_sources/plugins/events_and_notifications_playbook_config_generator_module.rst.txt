
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. role:: ansible-attribute-support-label
.. role:: ansible-attribute-support-property
.. role:: ansible-attribute-support-full
.. role:: ansible-attribute-support-partial
.. role:: ansible-attribute-support-none
.. role:: ansible-attribute-support-na
.. role:: ansible-option-type
.. role:: ansible-option-elements
.. role:: ansible-option-required
.. role:: ansible-option-versionadded
.. role:: ansible-option-aliases
.. role:: ansible-option-choices
.. role:: ansible-option-choices-default-mark
.. role:: ansible-option-default-bold
.. role:: ansible-option-configuration
.. role:: ansible-option-returned-bold
.. role:: ansible-option-sample-bold

.. Anchors

.. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.dnac.events_and_notifications_playbook_config_generator module -- Generate YAML playbook for 'events\_and\_notifications\_workflow\_manager' module.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `cisco.dnac collection <https://galaxy.ansible.com/cisco/dnac>`_ (version 6.49.0).

    To install it, use: :code:`ansible-galaxy collection install cisco.dnac`.
    You need further requirements to be able to use this module,
    see :ref:`Requirements <ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module_requirements>` for details.

    To use it in a playbook, specify: :code:`cisco.dnac.events_and_notifications_playbook_config_generator`.

.. version_added

.. rst-class:: ansible-version-added

New in cisco.dnac 6.44.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Generates YAML configurations compatible with the events\_and\_notifications\_workflow\_manager module for brownfield infrastructure discovery and documentation.
- Retrieves existing events and notifications configurations from Cisco Catalyst Center including webhook destinations, email destinations, syslog destinations, SNMP destinations, ITSM integration settings, and event subscriptions.
- Transforms API responses to playbook-compatible YAML format with parameter name mapping, password redaction, and structure optimization for Ansible execution.
- Supports comprehensive filtering capabilities including component-specific filters, destination name filters, and notification subscription filters.
- Resolves site IDs to hierarchical site names and event IDs to event names for human-readable playbook generation.
- Creates structured playbook files ready for modification and redeployment through events\_and\_notifications\_workflow\_manager module.


.. Aliases


.. Requirements

.. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module_requirements:

Requirements
------------
The below requirements are needed on the host that executes this module.

- dnacentersdk \>= 2.7.2
- python \>= 3.9






.. Options

Parameters
----------

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-config:

      .. rst-class:: ansible-option-title

      **config**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A dictionary of filters for generating YAML playbook compatible with the \ :literal:`events\_and\_notifications\_workflow\_manager`\  module.

      If \ :literal:`config`\  is omitted, the module retrieves all supported components and generates configurations for every available component type.

      If \ :literal:`config`\  is provided, \ :literal:`component\_specific\_filters`\  is mandatory.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-config/component_specific_filters:

      .. rst-class:: ansible-option-title

      **component_specific_filters**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filter configuration controlling which components are included in generated YAML playbook.

      Mandatory when \ :literal:`config`\  is provided.

      When components\_list is specified, only listed components are retrieved regardless of other filters.

      Destination and notification filters provide name-based filtering within selected components.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/components_list"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-config/component_specific_filters/components_list:

      .. rst-class:: ansible-option-title

      **components_list**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/components_list" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of component types to include in generated YAML playbook file.

      Optional, but conditionally required when no other filter blocks are provided under \ :literal:`component\_specific\_filters`\ .

      Each component type corresponds to specific API endpoint and configuration structure.

      Valid component types - \ :literal:`webhook\_destinations`\  - REST webhook destination configurations - \ :literal:`email\_destinations`\  - Email destination with SMTP settings - \ :literal:`syslog\_destinations`\  - Syslog server configurations - \ :literal:`snmp\_destinations`\  - SNMP trap receiver configurations - \ :literal:`itsm\_settings`\  - ITSM integration connection settings - \ :literal:`webhook\_event\_notifications`\  - Webhook event subscription configurations - \ :literal:`email\_event\_notifications`\  - Email event subscription configurations - \ :literal:`syslog\_event\_notifications`\  - Syslog event subscription configurations


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"webhook\_destinations"`
      - :ansible-option-choices-entry:`"email\_destinations"`
      - :ansible-option-choices-entry:`"syslog\_destinations"`
      - :ansible-option-choices-entry:`"snmp\_destinations"`
      - :ansible-option-choices-entry:`"itsm\_settings"`
      - :ansible-option-choices-entry:`"webhook\_event\_notifications"`
      - :ansible-option-choices-entry:`"email\_event\_notifications"`
      - :ansible-option-choices-entry:`"syslog\_event\_notifications"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/destination_filters"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-config/component_specific_filters/destination_filters:

      .. rst-class:: ansible-option-title

      **destination_filters**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/destination_filters" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filters for destination configurations based on name or type matching.

      Applies to webhook\_destinations, email\_destinations, syslog\_destinations, and snmp\_destinations components.

      When \ :literal:`destination\_filters`\  is provided, the corresponding destination components are automatically added to \ :literal:`components\_list`\  if not already present. If \ :literal:`destination\_types`\  is specified, only those types are added. If \ :literal:`destination\_types`\  is omitted, all four destination component types are added.

      Filtering is applied independently per component type selected in components\_list.

      Each component type only retrieves destinations of its own type and applies destination\_names filter within that scope.

      When destination\_names provided and at least one name matches a destination within a component type, only matching destinations of that type are included.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/destination_filters/destination_names"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-config/component_specific_filters/destination_filters/destination_names:

      .. rst-class:: ansible-option-title

      **destination_names**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/destination_filters/destination_names" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of exact destination names to filter from retrieved configurations.

      Names must match exactly as configured in Catalyst Center (case-sensitive).

      Only components listed in components\_list are retrieved. The destination\_names filter is applied only within those selected component types. Names belonging to a component type that is not in components\_list are completely ignored.

      If a destination name matches a destination within a selected component type, only matching destinations of that type are included in the output.

      Empty list or not specified retrieves all destinations for selected component types.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/destination_filters/destination_types"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-config/component_specific_filters/destination_filters/destination_types:

      .. rst-class:: ansible-option-title

      **destination_types**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/destination_filters/destination_types" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Specifies which destination component types the \ :literal:`destination\_names`\  filter applies to.

      Components implied by \ :literal:`destination\_types`\  are automatically added to \ :literal:`components\_list`\  if not already present. For example \ :literal:`webhook`\  auto-adds \ :literal:`webhook\_destinations`\ .

      Use this when you want name-based filtering for some destination types but want to retrieve all destinations for other types in \ :literal:`components\_list`\ .

      For example, with \ :literal:`components\_list`\  set to \ :literal:`[webhook\_destinations, email\_destinations]`\  and \ :literal:`destination\_types`\  set to \ :literal:`[webhook]`\  and \ :literal:`destination\_names`\  set to \ :literal:`[my-webhook-1]`\ , only webhook destinations matching "my-webhook-1" are filtered while all email destinations are retrieved without any name filtering.

      Valid types are \ :literal:`webhook`\ , \ :literal:`email`\ , \ :literal:`syslog`\ , \ :literal:`snmp`\ .


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"webhook"`
      - :ansible-option-choices-entry:`"email"`
      - :ansible-option-choices-entry:`"syslog"`
      - :ansible-option-choices-entry:`"snmp"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/itsm_filters"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-config/component_specific_filters/itsm_filters:

      .. rst-class:: ansible-option-title

      **itsm_filters**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/itsm_filters" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filters for ITSM integration settings based on instance name matching.

      When \ :literal:`itsm\_filters`\  is provided, the \ :literal:`itsm\_settings`\  component is automatically added to \ :literal:`components\_list`\  if not already present.

      Filters ITSM integration instances by configured instance names.

      Empty list or not specified retrieves all configured ITSM integration instances.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/itsm_filters/instance_names"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-config/component_specific_filters/itsm_filters/instance_names:

      .. rst-class:: ansible-option-title

      **instance_names**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/itsm_filters/instance_names" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of exact ITSM instance names to filter from retrieved configurations.

      Names must match exactly as configured in Catalyst Center ITSM integration settings.

      Filters ServiceNow, BMC Remedy, or custom ITSM integration instances.

      Empty list or not specified retrieves all ITSM integration instances.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/notification_filters"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-config/component_specific_filters/notification_filters:

      .. rst-class:: ansible-option-title

      **notification_filters**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/notification_filters" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filters for event notification subscription configurations based on name or type.

      Applies to webhook\_event\_notifications, email\_event\_notifications, and syslog\_event\_notifications.

      When \ :literal:`notification\_filters`\  is provided, the corresponding notification components are automatically added to \ :literal:`components\_list`\  if not already present. If \ :literal:`notification\_types`\  is specified, only those types are added. If \ :literal:`notification\_types`\  is omitted, all three notification component types are added.

      When subscription\_names provided, filters notifications to include only matching subscriptions.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/notification_filters/notification_types"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-config/component_specific_filters/notification_filters/notification_types:

      .. rst-class:: ansible-option-title

      **notification_types**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/notification_filters/notification_types" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Specifies which notification component types the \ :literal:`subscription\_names`\  filter applies to.

      Components implied by \ :literal:`notification\_types`\  are automatically added to \ :literal:`components\_list`\  if not already present. For example \ :literal:`webhook`\  auto-adds \ :literal:`webhook\_event\_notifications`\ .

      Use this when you want name-based filtering for some notification types but want to retrieve all subscriptions for other types in \ :literal:`components\_list`\ .

      For example, with \ :literal:`components\_list`\  set to \ :literal:`[webhook\_event\_notifications, email\_event\_notifications]`\  and \ :literal:`notification\_types`\  set to \ :literal:`[webhook]`\  and \ :literal:`subscription\_names`\  set to \ :literal:`[Critical Alerts]`\ , only webhook event notifications matching "Critical Alerts" are filtered while all email event notifications are retrieved without name filtering.

      Valid types are \ :literal:`webhook`\ , \ :literal:`email`\ , \ :literal:`syslog`\ .


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"webhook"`
      - :ansible-option-choices-entry:`"email"`
      - :ansible-option-choices-entry:`"syslog"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/notification_filters/subscription_names"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-config/component_specific_filters/notification_filters/subscription_names:

      .. rst-class:: ansible-option-title

      **subscription_names**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/notification_filters/subscription_names" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of exact event subscription names to filter from retrieved configurations.

      Names must match exactly as configured in Catalyst Center event subscriptions.

      Filters webhook, email, and syslog event notifications based on subscription name.

      Empty list or not specified retrieves all event subscriptions for selected types.


      .. raw:: html

        </div>




  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_api_task_timeout"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-dnac_api_task_timeout:

      .. rst-class:: ansible-option-title

      **dnac_api_task_timeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dnac_api_task_timeout" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Defines the timeout in seconds for API calls to retrieve task details. If the task details are not received within this period, the process will end, and a timeout notification will be logged.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`1200`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_debug"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-dnac_debug:

      .. rst-class:: ansible-option-title

      **dnac_debug**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dnac_debug" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Indicates whether debugging is enabled in the Cisco Catalyst Center SDK.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_host"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-dnac_host:

      .. rst-class:: ansible-option-title

      **dnac_host**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dnac_host" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The hostname of the Cisco Catalyst Center.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_log"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-dnac_log:

      .. rst-class:: ansible-option-title

      **dnac_log**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dnac_log" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Flag to enable/disable playbook execution logging.

      When true and dnac\_log\_file\_path is provided, - Create the log file at the execution location with the specified name.

      When true and dnac\_log\_file\_path is not provided, - Create the log file at the execution location with the name 'dnac.log'.

      When false, - Logging is disabled.

      If the log file doesn't exist, - It is created in append or write mode based on the "dnac\_log\_append" flag.

      If the log file exists, - It is overwritten or appended based on the "dnac\_log\_append" flag.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_log_append"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-dnac_log_append:

      .. rst-class:: ansible-option-title

      **dnac_log_append**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dnac_log_append" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Determines the mode of the file. Set to True for 'append' mode. Set to False for 'write' mode.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_log_file_path"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-dnac_log_file_path:

      .. rst-class:: ansible-option-title

      **dnac_log_file_path**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dnac_log_file_path" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Governs logging. Logs are recorded if dnac\_log is True.

      If path is not specified, - When 'dnac\_log\_append' is True, 'dnac.log' is generated in the current Ansible directory; logs are appended. - When 'dnac\_log\_append' is False, 'dnac.log' is generated; logs are overwritten.

      If path is specified, - When 'dnac\_log\_append' is True, the file opens in append mode. - When 'dnac\_log\_append' is False, the file opens in write (w) mode. - In shared file scenarios, without append mode, content is overwritten after each module execution. - For a shared log file, set append to False for the 1st module (to overwrite); for subsequent modules, set append to True.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"dnac.log"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_log_level"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-dnac_log_level:

      .. rst-class:: ansible-option-title

      **dnac_log_level**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dnac_log_level" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Sets the threshold for log level. Messages with a level equal to or higher than this will be logged. Levels are listed in order of severity [CRITICAL, ERROR, WARNING, INFO, DEBUG].

      CRITICAL indicates serious errors halting the program. Displays only CRITICAL messages.

      ERROR indicates problems preventing a function. Displays ERROR and CRITICAL messages.

      WARNING indicates potential future issues. Displays WARNING, ERROR, CRITICAL messages.

      INFO tracks normal operation. Displays INFO, WARNING, ERROR, CRITICAL messages.

      DEBUG provides detailed diagnostic info. Displays all log messages.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"WARNING"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_password"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-dnac_password:

      .. rst-class:: ansible-option-title

      **dnac_password**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dnac_password" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The password for authentication at the Cisco Catalyst Center.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_port"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-dnac_port:

      .. rst-class:: ansible-option-title

      **dnac_port**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dnac_port" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specifies the port number associated with the Cisco Catalyst Center.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"443"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_task_poll_interval"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-dnac_task_poll_interval:

      .. rst-class:: ansible-option-title

      **dnac_task_poll_interval**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dnac_task_poll_interval" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specifies the interval in seconds between successive calls to the API to retrieve task details.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`2`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_username"></div>
        <div class="ansibleOptionAnchor" id="parameter-user"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-dnac_username:
      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-user:

      .. rst-class:: ansible-option-title

      **dnac_username**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dnac_username" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-aliases:`aliases: user`

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The username for authentication at the Cisco Catalyst Center.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"admin"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_verify"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-dnac_verify:

      .. rst-class:: ansible-option-title

      **dnac_verify**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dnac_verify" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Flag to enable or disable SSL certificate verification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_version"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-dnac_version:

      .. rst-class:: ansible-option-title

      **dnac_version**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dnac_version" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specifies the version of the Cisco Catalyst Center that the SDK should use.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"2.2.3.3"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-file_mode"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-file_mode:

      .. rst-class:: ansible-option-title

      **file_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-file_mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      File write mode for the generated YAML configuration file.

      The overwrite option replaces existing file content with new content.

      The append option adds new content to the end of existing file.

      Relevant only when \ :literal:`file\_path`\  is provided.

      Defaults to overwrite if not specified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"overwrite"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"append"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-file_path"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-file_path:

      .. rst-class:: ansible-option-title

      **file_path**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-file_path" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Absolute or relative path where generated YAML configuration file will be saved.

      If not provided, file is saved in current working directory with auto-generated filename.

      Filename format when auto-generated is \ :literal:`events\_and\_notifications\_playbook\_config\_\<YYYY-MM-DD\_HH-MM-SS\>.yml`\ .

      Example auto-generated filename "events\_and\_notifications\_playbook\_config\_2025-04-22\_21-43-26.yml".

      Parent directories are created automatically if they do not exist.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-state:

      .. rst-class:: ansible-option-title

      **state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Desired state for module execution controlling playbook generation workflow.

      Only 'gathered' state is supported for retrieving configurations from Catalyst Center.

      The 'gathered' state initiates configuration discovery, API calls, transformation, and YAML file generation.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"gathered"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-validate_response_schema"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__parameter-validate_response_schema:

      .. rst-class:: ansible-option-title

      **validate_response_schema**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-validate_response_schema" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Flag for Cisco Catalyst Center SDK to enable the validation of request bodies against a JSON schema.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>


.. Attributes


.. Notes

Notes
-----

.. note::
   - SDK Methods used are - event\_management.Events.get\_webhook\_destination - event\_management.Events.get\_email\_destination - event\_management.Events.get\_syslog\_destination - event\_management.Events.get\_snmp\_destination - event\_management.Events.get\_all\_itsm\_integration\_settings - event\_management.Events.get\_rest\_webhook\_event\_subscriptions - event\_management.Events.get\_email\_event\_subscriptions - event\_management.Events.get\_syslog\_event\_subscriptions - event\_management.Events.get\_event\_artifacts - sites.Sites.get\_site
   - Paths used are - GET /dna/system/api/v1/event/webhook - GET /dna/system/api/v1/event/email-config - GET /dna/system/api/v1/event/syslog-config - GET /dna/system/api/v1/event/snmp-config - GET /dna/system/api/v1/event/itsm-integration-setting - GET /dna/system/api/v1/event/subscription/rest - GET /dna/system/api/v1/event/subscription/email - GET /dna/system/api/v1/event/subscription/syslog - GET /dna/intent/api/v1/event-artifact - GET /dna/intent/api/v1/site
   - Minimum Catalyst Center version required is 2.3.5.3 for events and notifications APIs.
   - Module performs read-only operations and does not modify Catalyst Center configurations.
   - Generated YAML files contain password placeholders marked as "\*\*\*REDACTED\*\*\*" for security.
   - Site IDs are automatically resolved to hierarchical site names for readability.
   - Event IDs are automatically resolved to event names using Event Artifacts API.
   - Pagination is automatically handled for large datasets in webhook, SNMP, and event subscriptions.
   - Generated playbooks are compatible with events\_and\_notifications\_workflow\_manager module.
   - When filter blocks (\ :literal:`destination\_filters`\ , \ :literal:`notification\_filters`\ , \ :literal:`itsm\_filters`\ ) are provided, the corresponding components are automatically added to \ :literal:`components\_list`\  if not already present. This means \ :literal:`components\_list`\  is optional when filter blocks are provided.
   - If no filter blocks are provided, \ :literal:`components\_list`\  is mandatory and must be non-empty.
   - Destination name filtering in destination\_filters.destination\_names is applied only within component types present in the final components\_list (including auto-added components).
   - Does not support \ :literal:`check\_mode`\ 
   - The plugin runs on the control node and does not use any ansible connection plugins instead embedded connection manager from Cisco Catalyst Center SDK
   - The parameters starting with dnac\_ are used by the Cisco Catalyst Center Python SDK to establish the connection

.. Seealso

See Also
--------

.. seealso::

   \ :ref:`cisco.dnac.events\_and\_notifications\_workflow\_manager <ansible_collections.cisco.dnac.events_and_notifications_workflow_manager_module>`\ 
       Module to manage Events and Notifications configurations in Cisco Catalyst Center.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Generate YAML Configuration with all events and notifications components
      cisco.dnac.events_and_notifications_playbook_config_generator:
        dnac_host: "{{dnac_host}}"
        dnac_username: "{{dnac_username}}"
        dnac_password: "{{dnac_password}}"
        dnac_verify: "{{dnac_verify}}"
        dnac_port: "{{dnac_port}}"
        dnac_version: "{{dnac_version}}"
        dnac_debug: "{{dnac_debug}}"
        dnac_log: true
        dnac_log_level: "{{dnac_log_level}}"
        state: gathered
        file_path: "/tmp/catc_events_notifications_config.yaml"

    - name: Generate YAML Configuration for destinations only
      cisco.dnac.events_and_notifications_playbook_config_generator:
        dnac_host: "{{dnac_host}}"
        dnac_username: "{{dnac_username}}"
        dnac_password: "{{dnac_password}}"
        dnac_verify: "{{dnac_verify}}"
        dnac_port: "{{dnac_port}}"
        dnac_version: "{{dnac_version}}"
        dnac_debug: "{{dnac_debug}}"
        dnac_log: true
        dnac_log_level: "{{dnac_log_level}}"
        state: gathered
        file_path: "/tmp/catc_destinations_config.yaml"
        config:
          component_specific_filters:
            components_list: ["webhook_destinations", "email_destinations", "syslog_destinations"]

    - name: Generate YAML Configuration for specific webhook destinations
      cisco.dnac.events_and_notifications_playbook_config_generator:
        dnac_host: "{{dnac_host}}"
        dnac_username: "{{dnac_username}}"
        dnac_password: "{{dnac_password}}"
        dnac_verify: "{{dnac_verify}}"
        dnac_port: "{{dnac_port}}"
        dnac_version: "{{dnac_version}}"
        dnac_debug: "{{dnac_debug}}"
        dnac_log: true
        dnac_log_level: "{{dnac_log_level}}"
        state: gathered
        file_path: "/tmp/catc_webhook_config.yaml"
        config:
          component_specific_filters:
            components_list: ["webhook_destinations", "webhook_event_notifications"]
            destination_filters:
              destination_names: ["webhook-dest-1", "webhook-dest-2"]
              destination_types: ["webhook"]

    - name: Generate YAML Configuration with combined filters
      cisco.dnac.events_and_notifications_playbook_config_generator:
        dnac_host: "{{dnac_host}}"
        dnac_username: "{{dnac_username}}"
        dnac_password: "{{dnac_password}}"
        dnac_verify: "{{dnac_verify}}"
        dnac_port: "{{dnac_port}}"
        dnac_version: "{{dnac_version}}"
        dnac_debug: "{{dnac_debug}}"
        dnac_log: true
        dnac_log_level: "{{dnac_log_level}}"
        state: gathered
        file_path: "/tmp/combined_filters_config.yaml"
        file_mode: append
        config:
          component_specific_filters:
            components_list: ["webhook_destinations", "webhook_event_notifications", "email_destinations", "email_event_notifications"]
            destination_filters:
              destination_names: ["Production Webhook", "Alert Email Server"]
              destination_types: ["webhook", "email"]
            notification_filters:
              subscription_names: ["Critical System Alerts", "Network Health Monitoring"]
              notification_types: ["webhook", "email"]

    - name: Generate YAML Configuration for ITSM settings using filter block (auto-adds itsm_settings to components_list)
      cisco.dnac.events_and_notifications_playbook_config_generator:
        dnac_host: "{{dnac_host}}"
        dnac_username: "{{dnac_username}}"
        dnac_password: "{{dnac_password}}"
        dnac_verify: "{{dnac_verify}}"
        dnac_port: "{{dnac_port}}"
        dnac_version: "{{dnac_version}}"
        dnac_debug: "{{dnac_debug}}"
        dnac_log: true
        dnac_log_level: "{{dnac_log_level}}"
        state: gathered
        file_path: "/tmp/catc_itsm_config.yaml"
        config:
          component_specific_filters:
            itsm_filters:
              instance_names: ["ServiceNow Instance 1", "BMC Remedy Prod"]




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-response_1"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__return-response_1:

      .. rst-class:: ansible-option-title

      **response_1**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-response_1" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A dictionary with the response returned by the Cisco Catalyst Center


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"msg": "YAML configuration file generated successfully for module 'events\_and\_notifications\_workflow\_manager'", "response": {"components\_processed": 1, "components\_skipped": 0, "configurations\_count": 1, "file\_path": "/Users/priyadharshini/Downloads/events\_and\_notifications\_playbook", "message": "YAML configuration file generated successfully for module 'events\_and\_notifications\_workflow\_manager'", "status": "success"}, "status": "success"}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-response_2"></div>

      .. _ansible_collections.cisco.dnac.events_and_notifications_playbook_config_generator_module__return-response_2:

      .. rst-class:: ansible-option-title

      **response_2**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-response_2" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A string with the response returned by the Cisco Catalyst Center


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`["{\\n  \\"msg\\": \\"No configurations found to generate. Verify that the components exist and have data.\\"", "\\n  \\"response\\": {\\n      \\"components\_processed\\": 0", "\\n      \\"components\_skipped\\": 1", "\\n      \\"configurations\_count\\": 0", "\\n      \\"message\\": \\"No configurations found to generate. Verify that the components exist and have data.\\"", "\\n      \\"status\\": \\"success\\"\\n  }", "\\n  \\"status\\": \\"success\\"\\n}\\n"]`


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Priyadharshini B (@pbalaku2)
- Madhan Sankaranarayanan (@madhansansel)



.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. raw:: html

  <p class="ansible-links">
    <a href="https://github.com/cisco-en-programmability/dnacenter-ansible/issues" aria-role="button" target="_blank" rel="noopener external">Issue Tracker</a>
    <a href="https://github.com/cisco-en-programmability/dnacenter-ansible" aria-role="button" target="_blank" rel="noopener external">Repository (Sources)</a>
  </p>

.. Parsing errors

