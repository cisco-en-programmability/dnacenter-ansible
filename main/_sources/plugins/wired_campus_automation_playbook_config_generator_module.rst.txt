
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

.. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.dnac.wired_campus_automation_playbook_config_generator module -- Generate YAML configurations playbook for 'wired\_campus\_automation\_workflow\_manager' module.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `cisco.dnac collection <https://galaxy.ansible.com/cisco/dnac>`_ (version 6.49.0).

    To install it, use: :code:`ansible-galaxy collection install cisco.dnac`.
    You need further requirements to be able to use this module,
    see :ref:`Requirements <ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module_requirements>` for details.

    To use it in a playbook, specify: :code:`cisco.dnac.wired_campus_automation_playbook_config_generator`.

.. version_added

.. rst-class:: ansible-version-added

New in cisco.dnac 6.40.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Generates YAML configurations compatible with the 'wired\_campus\_automation\_workflow\_manager' module, reducing the effort required to manually create Ansible playbooks and enabling programmatic modifications.
- The YAML configurations generated represent the layer 2 configurations deployed on network devices within the Cisco Catalyst Center.
- Supports extraction of VLANs, CDP, LLDP, STP, VTP, DHCP Snooping, IGMP Snooping, MLD Snooping, Authentication, Logical Ports, and Port Configuration settings.


.. Aliases


.. Requirements

.. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module_requirements:

Requirements
------------
The below requirements are needed on the host that executes this module.

- dnacentersdk \>= 2.10.10
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

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-config:

      .. rst-class:: ansible-option-title

      **config**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A list of filters for generating YAML playbook compatible with the 'wired\_campus\_automation\_workflow\_manager' module.

      Filters specify which components and devices to include in the YAML configuration file.

      Global filters identify target devices by IP address, hostname, or serial number.

      Component-specific filters allow selection of specific layer2 features and detailed filtering.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters"></div>

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-config/component_specific_filters:

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

      Filters to specify which layer2 components and features to include in the YAML configuration file.

      Allows granular selection of specific features and their parameters.

      If not specified, all supported layer2 features will be extracted.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/components_list"></div>

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-config/component_specific_filters/components_list:

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

      List of components to include in the YAML configuration file.

      Valid values are ["layer2\_configurations"]

      If not specified, all supported components are included.

      Future versions may support additional component types.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/layer2_features"></div>

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-config/component_specific_filters/layer2_features:

      .. rst-class:: ansible-option-title

      **layer2_features**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/layer2_features" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of specific layer2 features to extract from devices.

      Valid values are ["vlans", "cdp", "lldp", "stp", "vtp", "dhcp\_snooping", "igmp\_snooping", "mld\_snooping", "authentication", "logical\_ports", "port\_configuration"]

      If not specified, all supported layer2 features will be extracted.

      Example ["vlans", "stp", "cdp"] to extract only VLAN, STP, and CDP configurations.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"vlans"`
      - :ansible-option-choices-entry:`"cdp"`
      - :ansible-option-choices-entry:`"lldp"`
      - :ansible-option-choices-entry:`"stp"`
      - :ansible-option-choices-entry:`"vtp"`
      - :ansible-option-choices-entry:`"dhcp\_snooping"`
      - :ansible-option-choices-entry:`"igmp\_snooping"`
      - :ansible-option-choices-entry:`"mld\_snooping"`
      - :ansible-option-choices-entry:`"authentication"`
      - :ansible-option-choices-entry:`"logical\_ports"`
      - :ansible-option-choices-entry:`"port\_configuration"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/port_configuration"></div>

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-config/component_specific_filters/port_configuration:

      .. rst-class:: ansible-option-title

      **port_configuration**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/port_configuration" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Specific port configuration filtering options.

      Allows extraction of configurations for only specific interfaces.

      If not specified, all configured interfaces will be extracted.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/port_configuration/interface_names_list"></div>

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-config/component_specific_filters/port_configuration/interface_names_list:

      .. rst-class:: ansible-option-title

      **interface_names_list**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/port_configuration/interface_names_list" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of specific interface names to extract configurations from.

      Interface names must match the format used by the device.

      Example ["GigabitEthernet1/0/1", "GigabitEthernet1/0/2", "TenGigabitEthernet1/0/1"]

      Only interfaces in this list will have their configurations extracted.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/vlans"></div>

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-config/component_specific_filters/vlans:

      .. rst-class:: ansible-option-title

      **vlans**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/vlans" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Specific VLAN filtering options.

      Allows extraction of only specific VLANs based on VLAN IDs.

      If not specified, all VLANs configured on the device will be extracted.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/vlans/vlan_ids_list"></div>

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-config/component_specific_filters/vlans/vlan_ids_list:

      .. rst-class:: ansible-option-title

      **vlan_ids_list**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/vlans/vlan_ids_list" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of specific VLAN IDs to extract from devices.

      Each VLAN ID must be between 1 and 4094.

      Only VLANs in this list will be included in the generated configuration.

      Example ["10", "20", "100", "200"] to extract only these specific VLANs.


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/file_path"></div>

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-config/file_path:

      .. rst-class:: ansible-option-title

      **file_path**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/file_path" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Path where the YAML configuration file will be saved.

      If not provided, the file will be saved in the current working directory with a default file name \ :literal:`wired\_campus\_automation\_playbook\_config\_\<YYYY-MM-DD\_HH-MM-SS\>.yml`\ .

      For example, \ :literal:`wired\_campus\_automation\_playbook\_config\_2025-04-22\_21-43-26.yml`\ .


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/generate_all_configurations"></div>

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-config/generate_all_configurations:

      .. rst-class:: ansible-option-title

      **generate_all_configurations**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/generate_all_configurations" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      When set to True, automatically generates YAML configurations for all devices and all supported layer2 features.

      This mode discovers all managed devices in Cisco Catalyst Center and extracts all supported configurations.

      When enabled, the config parameter becomes optional and will use default values if not provided.

      A default filename will be generated automatically if file\_path is not specified.

      This is useful for complete brownfield infrastructure discovery and documentation.

      IMPORTANT NOTE - Currently, this module only supports layer2 configurations. When generate\_all\_configurations is enabled, it will attempt to retrieve layer2 configurations from ALL managed devices without filtering for layer2 capability. This may result in API errors for devices that do not support layer2 configuration features (such as older switch models, routers, wireless controllers, etc.). It is recommended to use specific device filters (ip\_address\_list, hostname\_list, or serial\_number\_list) to target only layer2-capable devices when not using generate\_all\_configurations mode.

      Supported layer2 devices include Catalyst 9000 series switches (9200/9300/9350/9400/9500/9600) and IE series switches (IE3400/IE3400H/IE3500/IE9300) running IOS-XE 17.3 or higher.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/global_filters"></div>

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-config/global_filters:

      .. rst-class:: ansible-option-title

      **global_filters**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/global_filters" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Global filters to apply when generating the YAML configuration file.

      These filters identify which network devices to extract configurations from.

      At least one filter type must be specified to identify target devices.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/global_filters/hostname_list"></div>

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-config/global_filters/hostname_list:

      .. rst-class:: ansible-option-title

      **hostname_list**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/global_filters/hostname_list" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of device hostnames to extract configurations from.

      LOWEST PRIORITY - Only used if neither ip\_address\_list nor serial\_number\_list are provided.

      Hostnames must match those registered in Catalyst Center.

      Case-sensitive and must be exact matches.

      Example ["switch01.lab.com", "core-switch-01", "access-sw-floor2"]


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/global_filters/ip_address_list"></div>

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-config/global_filters/ip_address_list:

      .. rst-class:: ansible-option-title

      **ip_address_list**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/global_filters/ip_address_list" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of device IP addresses to extract configurations from.

      HIGHEST PRIORITY - If provided, serial numbers and hostnames will be ignored.

      Each IP address must be a valid IPv4 address format.

      Devices must be managed by Cisco Catalyst Center.

      Example ["192.168.1.10", "192.168.1.11", "10.1.1.5"]


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/global_filters/serial_number_list"></div>

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-config/global_filters/serial_number_list:

      .. rst-class:: ansible-option-title

      **serial_number_list**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/global_filters/serial_number_list" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of device serial numbers to extract configurations from.

      MEDIUM PRIORITY - Only used if ip\_address\_list is not provided.

      Serial numbers must match those registered in Catalyst Center.

      Useful when IP addresses may change but serial numbers remain constant.

      If both serial\_number\_list and hostname\_list are provided, serial\_number\_list takes priority.

      Example ["FCW2140L05Y", "FCW2140L06Z", "9080V0I41J3"]


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config_verify"></div>

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-config_verify:

      .. rst-class:: ansible-option-title

      **config_verify**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config_verify" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set to True to verify the Cisco Catalyst Center after applying the playbook config.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_api_task_timeout"></div>

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-dnac_api_task_timeout:

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

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-dnac_debug:

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

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-dnac_host:

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

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-dnac_log:

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

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-dnac_log_append:

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

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-dnac_log_file_path:

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

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-dnac_log_level:

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

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-dnac_password:

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

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-dnac_port:

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

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-dnac_task_poll_interval:

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

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-dnac_username:
      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-user:

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

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-dnac_verify:

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

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-dnac_version:

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
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-state:

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

      The desired state of Cisco Catalyst Center after module execution.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"gathered"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-validate_response_schema"></div>

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__parameter-validate_response_schema:

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
   - SDK Methods used are - devices.Devices.get\_device\_list - wired.Wired.get\_configurations\_for\_a\_deployed\_layer2\_feature\_on\_a\_wired\_device
   - Paths used are - GET /dna/intent/api/v1/network-device - GET /dna/intent/api/v1/networkDevices/${id}/configFeatures/deployed/layer2/${feature}
   - Does not support \ :literal:`check\_mode`\ 
   - The plugin runs on the control node and does not use any ansible connection plugins instead embedded connection manager from Cisco Catalyst Center SDK
   - The parameters starting with dnac\_ are used by the Cisco Catalyst Center Python SDK to establish the connection

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    

    # NOT Recommended for actual use cases due to potential API errors on non-layer2 devices.
    # - name: Auto-generate YAML Configuration for all devices and features
    #   cisco.dnac.wired_campus_automation_playbook_config_generator:
    #     dnac_host: "{{dnac_host}}"
    #     dnac_username: "{{dnac_username}}"
    #     dnac_password: "{{dnac_password}}"
    #     dnac_verify: "{{dnac_verify}}"
    #     dnac_port: "{{dnac_port}}"
    #     dnac_version: "{{dnac_version}}"
    #     dnac_debug: "{{dnac_debug}}"
    #     dnac_log: true
    #     dnac_log_level: "{{dnac_log_level}}"
    #     state: gathered
    #     config:
    #       - generate_all_configurations: true

    # NOT Recommended for actual use cases due to potential API errors on non-layer2 devices.
    # - name: Auto-generate YAML Configuration with custom file path
    #   cisco.dnac.wired_campus_automation_playbook_config_generator:
    #     dnac_host: "{{dnac_host}}"
    #     dnac_username: "{{dnac_username}}"
    #     dnac_password: "{{dnac_password}}"
    #     dnac_verify: "{{dnac_verify}}"
    #     dnac_port: "{{dnac_port}}"
    #     dnac_version: "{{dnac_version}}"
    #     dnac_debug: "{{dnac_debug}}"
    #     dnac_log: true
    #     dnac_log_level: "{{dnac_log_level}}"
    #     state: gathered
    #     config:
    #       - file_path: "/tmp/complete_infrastructure_config.yml"

    - name: Generate YAML Configuration with default file path
      cisco.dnac.wired_campus_automation_playbook_config_generator:
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
        config:
          - global_filters:
              ip_address_list: ["192.168.1.10"]

    - name: Generate YAML Configuration with specific devices by IP address
      cisco.dnac.wired_campus_automation_playbook_config_generator:
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
        config:
          - file_path: "/tmp/wired_campus_automation_config.yml"
            global_filters:
              ip_address_list: ["192.168.1.10", "192.168.1.11", "192.168.1.12"]

    - name: Generate YAML Configuration with specific devices by hostname
      cisco.dnac.wired_campus_automation_playbook_config_generator:
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
        config:
          - file_path: "/tmp/wired_campus_automation_config.yml"
            global_filters:
              hostname_list: ["switch01.lab.com", "switch02.lab.com", "core-switch-01"]

    - name: Generate YAML Configuration with specific devices by serial number
      cisco.dnac.wired_campus_automation_playbook_config_generator:
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
        config:
          - file_path: "/tmp/wired_campus_automation_config.yml"
            global_filters:
              serial_number_list: ["FCW2140L05Y", "FCW2140L06Z", "9080V0I41J3"]

    - name: Generate YAML Configuration with specific devices by hostname
      cisco.dnac.wired_campus_automation_playbook_config_generator:
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
        config:
          - file_path: "/tmp/wired_campus_automation_config.yml"
            global_filters:
              hostname_list: ["switch01.lab.com", "switch02.lab.com", "core-switch-01"]

    - name: Generate YAML Configuration with specific devices by serial number
      cisco.dnac.wired_campus_automation_playbook_config_generator:
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
        config:
          - file_path: "/tmp/wired_campus_automation_config.yml"
            global_filters:
              serial_number_list: ["FCW2140L05Y", "FCW2140L06Z", "9080V0I41J3"]

    - name: Generate YAML Configuration using explicit components list
      cisco.dnac.wired_campus_automation_playbook_config_generator:
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
        config:
          - file_path: "/tmp/wired_campus_automation_config.yml"
            global_filters:
              ip_address_list: ["192.168.1.10", "192.168.1.11"]
            component_specific_filters:
              components_list: ["layer2_configurations"]

    - name: Generate YAML Configuration with components list and specific features
      cisco.dnac.wired_campus_automation_playbook_config_generator:
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
        config:
          - file_path: "/tmp/wired_campus_automation_config.yml"
            global_filters:
              ip_address_list: ["192.168.1.10"]
            component_specific_filters:
              components_list: ["layer2_configurations"]
              layer2_configurations:
                layer2_features: ["vlans", "stp", "cdp"]

    - name: Generate YAML Configuration for specific VLANs
      cisco.dnac.wired_campus_automation_playbook_config_generator:
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
        config:
          - file_path: "/tmp/wired_campus_automation_config.yml"
            global_filters:
              ip_address_list: ["192.168.1.10"]
            component_specific_filters:
              components_list: ["layer2_configurations"]
              layer2_configurations:
                layer2_features: ["vlans"]
                vlans:
                  vlan_ids_list: ["10", "20", "100", "200"]

    - name: Generate YAML Configuration for specific interfaces
      cisco.dnac.wired_campus_automation_playbook_config_generator:
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
        config:
          - file_path: "/tmp/wired_campus_automation_config.yml"
            global_filters:
              ip_address_list: ["192.168.1.10"]
            component_specific_filters:
              components_list: ["layer2_configurations"]
              layer2_configurations:
                layer2_features: ["port_configuration"]
                port_configuration:
                  interface_names_list:
                    - "GigabitEthernet1/0/1"
                    - "GigabitEthernet1/0/2"
                    - "TenGigabitEthernet1/0/1"

    - name: Generate YAML Configuration with comprehensive filtering
      cisco.dnac.wired_campus_automation_playbook_config_generator:
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
        config:
          - file_path: "/tmp/wired_campus_automation_config.yml"
            global_filters:
              ip_address_list: ["192.168.1.10", "192.168.1.11"]
            component_specific_filters:
              components_list: ["layer2_configurations"]
              layer2_configurations:
                layer2_features: ["vlans", "stp", "port_configuration"]
                vlans:
                  vlan_ids_list: ["10", "20", "100"]
                port_configuration:
                  interface_names_list:
                    - "GigabitEthernet1/0/1"
                    - "GigabitEthernet1/0/24"

    - name: Generate YAML Configuration for specific interfaces
      cisco.dnac.wired_campus_automation_playbook_config_generator:
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
        config:
          - file_path: "/tmp/wired_campus_automation_config.yml"
            global_filters:
              ip_address_list: ["192.168.1.10"]
            component_specific_filters:
              layer2_features: ["port_configuration"]
              port_configuration:
                interface_names_list:
                  - "GigabitEthernet1/0/1"
                  - "GigabitEthernet1/0/2"
                  - "TenGigabitEthernet1/0/1"

    - name: Generate YAML Configuration with comprehensive filtering
      cisco.dnac.wired_campus_automation_playbook_config_generator:
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
        config:
          - file_path: "/tmp/wired_campus_automation_config.yml"
            global_filters:
              ip_address_list: ["192.168.1.10", "192.168.1.11"]
            component_specific_filters:
              layer2_features: ["vlans", "stp", "port_configuration"]
              vlans:
                vlan_ids_list: ["10", "20", "100"]
              port_configuration:
                interface_names_list:
                  - "GigabitEthernet1/0/1"
                  - "GigabitEthernet1/0/24"

    - name: Generate YAML Configuration for all features (no component filters)
      cisco.dnac.wired_campus_automation_playbook_config_generator:
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
        config:
          - file_path: "/tmp/wired_campus_automation_config.yml"
            global_filters:
              ip_address_list: ["192.168.1.10"]

    - name: Generate YAML Configuration with default file path
      cisco.dnac.wired_campus_automation_playbook_config_generator:
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
        config:
          - global_filters:
              ip_address_list: ["192.168.1.10"]

    - name: Generate YAML Configuration for protocol features
      cisco.dnac.wired_campus_automation_playbook_config_generator:
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
        config:
          - file_path: "/tmp/protocol_features_config.yml"
            global_filters:
              hostname_list: ["switch01.lab.com", "switch02.lab.com"]
            component_specific_filters:
              layer2_features: ["cdp", "lldp", "stp", "vtp"]

    - name: Generate YAML Configuration for security features
      cisco.dnac.wired_campus_automation_playbook_config_generator:
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
        config:
          - file_path: "/tmp/security_features_config.yml"
            global_filters:
              serial_number_list: ["FCW2140L05Y", "FCW2140L06Z"]
            component_specific_filters:
              layer2_features: ["dhcp_snooping", "igmp_snooping", "authentication"]




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

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__return-response_1:

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

      A dictionary with the response returned by the Cisco Catalyst Center Python SDK


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"msg": "YAML config generation succeeded for module 'wired\_campus\_automation\_workflow\_manager'.", "response": {"configurations\_generated": 25, "file\_path": "/tmp/wired\_campus\_automation\_config.yml", "message": "YAML config generation succeeded for module 'wired\_campus\_automation\_workflow\_manager'.", "operation\_summary": {"devices\_with\_complete\_failure": [], "devices\_with\_complete\_success": ["192.168.1.10", "192.168.1.11"], "devices\_with\_partial\_success": ["192.168.1.12"], "failure\_details": [{"device\_id": "12345678-1234-1234-1234-123456789def", "device\_ip": "192.168.1.12", "error\_info": {"error\_code": "FEATURE\_NOT\_SUPPORTED", "error\_message": "Feature not supported on this device", "error\_type": "api\_error"}, "feature": "stp", "status": "failed"}], "success\_details": [{"api\_features\_processed": ["vlanConfig"], "device\_id": "12345678-1234-1234-1234-123456789abc", "device\_ip": "192.168.1.10", "feature": "vlans", "status": "success"}], "total\_devices\_processed": 3, "total\_failed\_operations": 3, "total\_features\_processed": 33, "total\_successful\_operations": 30}}}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-response_2"></div>

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__return-response_2:

      .. rst-class:: ansible-option-title

      **response_2**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-response_2" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A dictionary with the response when no configurations are found


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"msg": "No configurations or components to process for module 'wired\_campus\_automation\_workflow\_manager'. Verify input filters or configuration.", "response": {"message": "No configurations or components to process for module 'wired\_campus\_automation\_workflow\_manager'. Verify input filters or configuration.", "operation\_summary": {"devices\_with\_complete\_failure": [], "devices\_with\_complete\_success": [], "devices\_with\_partial\_success": [], "failure\_details": [], "success\_details": [], "total\_devices\_processed": 0, "total\_failed\_operations": 0, "total\_features\_processed": 0, "total\_successful\_operations": 0}}}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-response_3"></div>

      .. _ansible_collections.cisco.dnac.wired_campus_automation_playbook_config_generator_module__return-response_3:

      .. rst-class:: ansible-option-title

      **response_3**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-response_3" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A dictionary with error details when YAML generation fails


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"msg": "YAML config generation failed for module 'wired\_campus\_automation\_workflow\_manager'.", "response": {"file\_path": "/tmp/wired\_campus\_automation\_config.yml", "message": "YAML config generation failed for module 'wired\_campus\_automation\_workflow\_manager'.", "operation\_summary": {"devices\_with\_complete\_failure": ["192.168.1.11"], "devices\_with\_complete\_success": [], "devices\_with\_partial\_success": ["192.168.1.10"], "failure\_details": [{"device\_id": "12345678-1234-1234-1234-123456789ghi", "device\_ip": "192.168.1.11", "error\_info": {"error\_code": "DEVICE\_UNREACHABLE", "error\_message": "Device is not reachable or not managed", "error\_type": "device\_unreachable"}, "feature": "vlans", "status": "failed"}], "success\_details": [], "total\_devices\_processed": 2, "total\_failed\_operations": 10, "total\_features\_processed": 20, "total\_successful\_operations": 10}}}`


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Rugvedi Kapse (@rukapse)
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

