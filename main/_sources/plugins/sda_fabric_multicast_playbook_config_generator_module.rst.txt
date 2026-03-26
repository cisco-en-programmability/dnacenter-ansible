
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

.. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.dnac.sda_fabric_multicast_playbook_config_generator module -- Generate YAML configurations playbook for 'sda\_fabric\_multicast\_workflow\_manager' module.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `cisco.dnac collection <https://galaxy.ansible.com/cisco/dnac>`_ (version 6.49.0).

    To install it, use: :code:`ansible-galaxy collection install cisco.dnac`.
    You need further requirements to be able to use this module,
    see :ref:`Requirements <ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module_requirements>` for details.

    To use it in a playbook, specify: :code:`cisco.dnac.sda_fabric_multicast_playbook_config_generator`.

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

- Automates YAML playbook generation from existing SDA fabric multicast deployments in Cisco Catalyst Center.
- Creates playbooks compatible with the \ :literal:`sda\_fabric\_multicast\_workflow\_manager`\  module for infrastructure configuration management and documentation.
- Reduces manual effort by programmatically extracting current multicast configurations including replication modes, SSM ranges, and ASM RPs.
- Supports selective filtering to generate playbooks for specific fabric sites or Layer 3 virtual networks.
- Enables complete infrastructure discovery with auto-generation mode when \ :literal:`generate\_all\_configurations`\  is enabled.
- Requires Cisco Catalyst Center version 2.3.7.9 or higher.


.. Aliases


.. Requirements

.. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module_requirements:

Requirements
------------
The below requirements are needed on the host that executes this module.

- dnacentersdk \>= 2.9.2
- python \>= 3.9
- Cisco Catalyst Center \>= 2.3.7.9






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

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-config:

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

      A dictionary of filters for generating YAML playbook compatible with the \ :literal:`sda\_fabric\_multicast\_workflow\_manager`\  module.

      Filters specify which components to include in the YAML configuration file.

      If "components\_list" is specified, only those components are included, regardless of the filters.

      If config is not provided or is empty, all configurations for all fabric sites will be generated.

      This is useful for complete brownfield infrastructure discovery and documentation.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters"></div>

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-config/component_specific_filters:

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

      Filters to specify which components to include in the YAML configuration file.

      If "components\_list" is specified, only those components are included, regardless of other filters.

      If filters for specific components (e.g., fabric\_multicast) are provided without explicitly including them in components\_list, those components will be automatically added to components\_list.

      At least one of components\_list or component filters must be provided when config is specified.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/components_list"></div>

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-config/component_specific_filters/components_list:

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

      List of component types to include in the generated YAML playbook.

      Currently supports \ :literal:`fabric\_multicast`\  for SDA fabric multicast configurations.

      If omitted, all supported components are included by default.

      If specified, only the listed components will be processed.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"fabric\_multicast"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/fabric_multicast"></div>

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-config/component_specific_filters/fabric_multicast:

      .. rst-class:: ansible-option-title

      **fabric_multicast**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/fabric_multicast" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Each filter entry can specify \ :literal:`fabric\_name`\  and/or \ :literal:`layer3\_virtual\_network`\  to narrow results.

      Retrieved configurations include replication mode, SSM ranges, ASM RP details, and IP pool assignments.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/fabric_multicast/fabric_name"></div>

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-config/component_specific_filters/fabric_multicast/fabric_name:

      .. rst-class:: ansible-option-title

      **fabric_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/fabric_multicast/fabric_name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The hierarchical name of the fabric site from which to retrieve multicast configurations.

      Must match the exact site hierarchy as configured in Cisco Catalyst Center.

      Site can be either a fabric site or fabric zone.

      If the specified site is not configured as a fabric site or fabric zone, the filter entry is skipped with a warning.

      Example hierarchical path: \ :literal:`Global/USA/San Jose/Building1`\ 

      Case-sensitive matching is performed against cached site mappings.

      For detailed parameter usage and configuration examples, refer to the \ :literal:`sda\_fabric\_multicast\_workflow\_manager`\  module documentation.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/fabric_multicast/layer3_virtual_network"></div>

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-config/component_specific_filters/fabric_multicast/layer3_virtual_network:

      .. rst-class:: ansible-option-title

      **layer3_virtual_network**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/fabric_multicast/layer3_virtual_network" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The name of the Layer 3 virtual network (VN) associated with the fabric multicast configuration.

      Used to filter multicast configurations for a specific virtual network within the fabric site.

      Can be combined with \ :literal:`fabric\_name`\  to retrieve multicast settings for a specific VN in a specific fabric.

      If specified alone without \ :literal:`fabric\_name`\ , retrieves configurations for the VN across all fabric sites.

      Example VN names: \ :literal:`GUEST\_VN`\ , \ :literal:`EMPLOYEE\_VN`\ , \ :literal:`IOT\_VN`\ 

      For detailed parameter usage and configuration examples, refer to the \ :literal:`sda\_fabric\_multicast\_workflow\_manager`\  module documentation.


      .. raw:: html

        </div>




  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_api_task_timeout"></div>

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-dnac_api_task_timeout:

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

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-dnac_debug:

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

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-dnac_host:

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

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-dnac_log:

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

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-dnac_log_append:

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

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-dnac_log_file_path:

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

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-dnac_log_level:

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

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-dnac_password:

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

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-dnac_port:

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

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-dnac_task_poll_interval:

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

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-dnac_username:
      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-user:

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

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-dnac_verify:

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

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-dnac_version:

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

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-file_mode:

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

      Controls how config is written to the YAML file.

      \ :literal:`overwrite`\  replaces existing file content.

      \ :literal:`append`\  appends generated YAML content to the existing file.

      This parameter is only relevant when \ :literal:`file\_path`\  is specified. Defaults to \ :literal:`overwrite`\ .


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"overwrite"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"append"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-file_path"></div>

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-file_path:

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

      Path where the YAML configuration file will be saved.

      If not provided, the file will be saved in the current working directory with a default file name \ :literal:`sda\_fabric\_multicast\_playbook\_config\_\<YYYY-MM-DD\_HH-MM-SS\>.yml`\ .

      For example, \ :literal:`sda\_fabric\_multicast\_playbook\_config\_2026-01-30\_19-16-01.yml`\ .


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-state:

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

      The desired state for the module operation.

      \ :literal:`gathered`\  generates YAML playbooks from existing configurations.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"gathered"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-validate_response_schema"></div>

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__parameter-validate_response_schema:

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
   - Requires minimum Cisco Catalyst Center version 2.3.7.9 for SDA fabric multicast API support.
   - Module will fail with an error if connected to an unsupported version.
   - Generated playbooks are compatible with the \ :literal:`sda\_fabric\_multicast\_workflow\_manager`\  module for configuration deployment.
   - Device IDs in RP configurations are automatically converted to management IP addresses in the generated playbook.
   - Replication modes are retrieved from cached fabric configurations to ensure accurate playbook generation.
   - For FABRIC location RPs, external IP address fields are automatically excluded from the generated playbook.
   - Site hierarchies must exist in Cisco Catalyst Center and be configured as fabric sites or zones to be included in results.
   - Use \ :literal:`dnac\_log`\  and \ :literal:`dnac\_log\_level`\  parameters for detailed operation logging and troubleshooting.
   - The module operates in check mode but does not make any changes to Cisco Catalyst Center.
   - Does not support \ :literal:`check\_mode`\ 
   - The plugin runs on the control node and does not use any ansible connection plugins instead embedded connection manager from Cisco Catalyst Center SDK
   - The parameters starting with dnac\_ are used by the Cisco Catalyst Center Python SDK to establish the connection

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    # Example 1: Generate all configurations (default behavior when config is omitted)
    - name: Generate YAML playbook for all SDA fabric multicast configurations
      cisco.dnac.sda_fabric_multicast_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: INFO
        state: gathered
        # No config provided - generates all configurations

    # Example 2: Generate all configurations with custom file path
    - name: Generate complete SDA fabric multicast configuration with custom filename
      cisco.dnac.sda_fabric_multicast_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: INFO
        state: gathered
        file_path: "/tmp/complete_sda_fabric_multicast_config.yaml"
        file_mode: "overwrite"
        # No config provided - generates all configurations

    # Example 3: Generate fabric multicast configurations for a specific fabric site
    - name: Generate YAML playbook for specific fabric site
      cisco.dnac.sda_fabric_multicast_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        state: gathered
        file_path: "/tmp/site_specific_multicast.yaml"
        file_mode: "overwrite"
        config:
          component_specific_filters:
            components_list:
              - fabric_multicast
            fabric_multicast:
              - fabric_name: "Global/USA/San Jose/Building1"

    # Example 4: Generate configuration for specific fabric and virtual network
    - name: Generate YAML playbook for specific fabric and virtual network
      cisco.dnac.sda_fabric_multicast_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        state: gathered
        file_path: "/tmp/fabric_vn_specific_multicast.yaml"
        file_mode: "overwrite"
        config:
          component_specific_filters:
            fabric_multicast:
              - fabric_name: "Global/USA/San Jose/Building1"
                layer3_virtual_network: "GUEST_VN"

    # Example 5: Auto-populate components_list from component filters
    - name: Generate configuration with auto-populated components_list
      cisco.dnac.sda_fabric_multicast_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        state: gathered
        file_path: "/tmp/san_jose_fabric.yaml"
        file_mode: "overwrite"
        config:
          component_specific_filters:
            # No components_list specified, but fabric_multicast filters are provided
            # The 'fabric_multicast' component will be automatically added to components_list
            fabric_multicast:
              - fabric_name: "Global/USA/San Jose/Building1"

    # Example 6: Generate configuration with append mode
    - name: Generate and append SDA fabric multicast configuration
      cisco.dnac.sda_fabric_multicast_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        state: gathered
        file_path: "/tmp/all_fabric_multicast.yaml"
        file_mode: "append"
        config:
          component_specific_filters:
            components_list:
              - fabric_multicast
            fabric_multicast:
              - fabric_name: "Global/Europe/London/DataCenter1"

    # Example 7: Generate playbook for multiple fabric sites
    - name: Generate playbook for multiple fabric sites
      cisco.dnac.sda_fabric_multicast_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        state: gathered
        file_path: "/tmp/multiple_sites_multicast.yaml"
        file_mode: "overwrite"
        config:
          component_specific_filters:
            fabric_multicast:
              - fabric_name: "Global/USA/San Jose/Building1"
              - fabric_name: "Global/USA/San Jose/Building2"
              - fabric_name: "Global/Europe/London/DataCenter1"




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
        <div class="ansibleOptionAnchor" id="return-changed"></div>

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__return-changed:

      .. rst-class:: ansible-option-title

      **changed**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Indicates whether any changes were made.

      Always \ :literal:`false`\  for this module as it only reads configurations and generates playbooks.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`false`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__return-msg:

      .. rst-class:: ansible-option-title

      **msg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-msg" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Status message providing additional context about the operation.

      Includes details about configurations processed, files generated, or errors encountered.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"Successfully collected all parameters from the playbook for SDA Fabric Multicast playbook generation operations."`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-response"></div>

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__return-response:

      .. rst-class:: ansible-option-title

      **response**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-response" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Details of the YAML playbook generation operation.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"response": {"YAML config generation Task succeeded for module 'sda\_fabric\_multicast\_workflow\_manager'.": {"file\_path": "/tmp/sda\_fabric\_multicast\_playbook\_config\_2025-04-22\_21-43-26.yml"}}, "version": "2.3.7.9"}`


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-response/response"></div>

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__return-response/response:

      .. rst-class:: ansible-option-title

      **response**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-response/response" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Success or failure message indicating the result of the playbook generation operation.

      For successful operations, includes the file path where the YAML playbook was saved.

      For failed operations, includes error details and failure reason.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"YAML config generation Task succeeded for module 'sda\_fabric\_multicast\_workflow\_manager'.": {"file\_path": "/path/to/output/playbook.yml"}}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-response/version"></div>

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__return-response/version:

      .. rst-class:: ansible-option-title

      **version**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-response/version" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Cisco Catalyst Center version used during the operation.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"2.3.7.9"`


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-response_error"></div>

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__return-response_error:

      .. rst-class:: ansible-option-title

      **response_error**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-response_error" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Error response when playbook generation fails.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on failure

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"msg": "The specified version '2.3.5.3' does not support the YAML Playbook generation for SDA FABRIC MULTICAST Module. Supported versions start from '2.3.7.9' onwards.", "response": [], "version": "2.3.5.3"}`


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-response_error/msg"></div>

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__return-response_error/msg:

      .. rst-class:: ansible-option-title

      **msg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-response_error/msg" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Detailed error message explaining the failure reason.

      May include validation errors, API call failures, or file write errors.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"Invalid parameters in playbook: ['unknown\_parameter']"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-response_error/response"></div>

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__return-response_error/response:

      .. rst-class:: ansible-option-title

      **response**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-response_error/response" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Empty list or error details.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`[]`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-response_error/version"></div>

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__return-response_error/version:

      .. rst-class:: ansible-option-title

      **version**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-response_error/version" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Cisco Catalyst Center version.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"2.3.7.9"`


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-status"></div>

      .. _ansible_collections.cisco.dnac.sda_fabric_multicast_playbook_config_generator_module__return-status:

      .. rst-class:: ansible-option-title

      **status**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-status" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Current status of the operation (success, failed, invalid).


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"success"`


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Archit Soni (@koderchit)
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

