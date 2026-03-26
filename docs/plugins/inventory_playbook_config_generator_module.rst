
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

.. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.dnac.inventory_playbook_config_generator module -- Generate YAML playbook input for 'inventory\_workflow\_manager' module.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `cisco.dnac collection <https://galaxy.ansible.com/cisco/dnac>`_ (version 6.49.0).

    To install it, use: :code:`ansible-galaxy collection install cisco.dnac`.
    You need further requirements to be able to use this module,
    see :ref:`Requirements <ansible_collections.cisco.dnac.inventory_playbook_config_generator_module_requirements>` for details.

    To use it in a playbook, specify: :code:`cisco.dnac.inventory_playbook_config_generator`.

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

- Generates YAML input files for \ :literal:`cisco.dnac.inventory\_workflow\_manager`\ .
- Supports independent component generation for device details, SDA provisioning, interface details, and user-defined fields.
- Supports global device filters by IP, hostname, serial number, and MAC address.
- In non-auto mode, provide \ :literal:`component\_specific\_filters.components\_list`\  to control which component sections are generated.


.. Aliases


.. Requirements

.. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module_requirements:

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

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-config:

      .. rst-class:: ansible-option-title

      **config**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A list of filters for generating YAML playbook compatible with the 'inventory\_workflow\_manager' module.

      Filters specify which devices and credentials to include in the YAML configuration file.

      If "components\_list" is specified, only those components are included, regardless of the filters.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-config/component_specific_filters:

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

      Filters to specify which components and device attributes to include in the YAML configuration file.

      If "components\_list" is specified, only those components are included.

      Additional filters can be applied to narrow down device selection based on role, type, etc.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/components_list"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-config/component_specific_filters/components_list:

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

      Valid values are "device\_details", "provision\_device", "interface\_details", and "user\_defined\_fields".

      If not specified, all components are included.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"device\_details"`
      - :ansible-option-choices-entry:`"provision\_device"`
      - :ansible-option-choices-entry:`"interface\_details"`
      - :ansible-option-choices-entry:`"user\_defined\_fields"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/device_details"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-config/component_specific_filters/device_details:

      .. rst-class:: ansible-option-title

      **device_details**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/device_details" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`any`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filters for device configuration generation.

      Accepts a dict or a list of dicts.

      List behavior OR between dict entries.

      Dict behavior AND between filter keys.

      Supported keys include type, role, snmp\_version, and cli\_transport.

      Type options: NETWORK\_DEVICE, COMPUTE\_DEVICE, MERAKI\_DASHBOARD, THIRD\_PARTY\_DEVICE, FIREPOWER\_MANAGEMENT\_SYSTEM.

      Role options: ACCESS, CORE, DISTRIBUTION, BORDER ROUTER, UNKNOWN.

      SNMP version options: v2, v2c, v3.

      CLI transport options: ssh or telnet.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/device_details/role"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-config/component_specific_filters/device_details/role:

      .. rst-class:: ansible-option-title

      **role**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/device_details/role" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filter devices by network role.

      Can be a single role string or a list of roles (matches any in the list).

      Valid values are ACCESS, CORE, DISTRIBUTION, BORDER ROUTER, UNKNOWN.

      Example: role="ACCESS" for single role or role=["ACCESS", "CORE"] for multiple roles.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ACCESS"`
      - :ansible-option-choices-entry:`"CORE"`
      - :ansible-option-choices-entry:`"DISTRIBUTION"`
      - :ansible-option-choices-entry:`"BORDER ROUTER"`
      - :ansible-option-choices-entry:`"UNKNOWN"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/interface_details"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-config/component_specific_filters/interface_details:

      .. rst-class:: ansible-option-title

      **interface_details**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/interface_details" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Component selector for auto-generated interface\_details.

      Filters interface configurations based on device IP addresses and interface names.

      Interfaces are automatically discovered from matched devices using Catalyst Center API.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/interface_details/interface_name"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-config/component_specific_filters/interface_details/interface_name:

      .. rst-class:: ansible-option-title

      **interface_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/interface_details/interface_name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filter interfaces by name (optional).

      Can be a single interface name string or a list of interface names.

      When specified, only interfaces with matching names will be included.

      Matches use 'OR' logic; any interface matching any name in the list is included.

      Common interface names include Vlan100, Loopback0, GigabitEthernet1/0/1, or FortyGigabitEthernet1/1/1.

      If not specified, all discovered interfaces for matched devices are included.

      Example: interface\_name="Vlan100" for single or interface\_name=["Vlan100", "Loopback0"] for multiple.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/provision_device"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-config/component_specific_filters/provision_device:

      .. rst-class:: ansible-option-title

      **provision_device**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/provision_device" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Specific filters for provision\_device component.

      Filters the provision\_wired\_device configuration based on site assignment.

      No additional API calls are made; filtering is applied to existing provision data.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/provision_device/site_name"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-config/component_specific_filters/provision_device/site_name:

      .. rst-class:: ansible-option-title

      **site_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/provision_device/site_name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filter provision devices by site name (e.g., Global/India/Telangana/Hyderabad/BLD\_1).


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/user_defined_fields"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-config/component_specific_filters/user_defined_fields:

      .. rst-class:: ansible-option-title

      **user_defined_fields**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/user_defined_fields" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filters for user-defined fields (UDF) component generation.

      Supports filtering by UDF field name and/or UDF field value.

      Both \ :literal:`name`\  and \ :literal:`value`\  accept a single string or a list of strings.

      List behavior uses OR logic (match any item in the list).


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/user_defined_fields/name"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-config/component_specific_filters/user_defined_fields/name:

      .. rst-class:: ansible-option-title

      **name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/user_defined_fields/name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`any`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filter UDF output by field name.

      Accepts a single name string or a list of names.

      When specified, only matching UDF names are included.

      Example: name="Cisco Switches" or name=["Cisco Switches", "To\_test\_udf"].


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/user_defined_fields/value"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-config/component_specific_filters/user_defined_fields/value:

      .. rst-class:: ansible-option-title

      **value**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/user_defined_fields/value" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`any`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filter UDF output by field value.

      Accepts a single value string or a list of values.

      When specified, only UDFs with matching values are included.

      Example: value="2234" or value=["2234", "value12345"].


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/file_mode"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-config/file_mode:

      .. rst-class:: ansible-option-title

      **file_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/file_mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Controls how config is written to the YAML file.

      \ :literal:`overwrite`\  replaces existing file content.

      \ :literal:`append`\  appends generated YAML content to the existing file.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"overwrite"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"append"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/file_path"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-config/file_path:

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

      If not provided, the file will be saved in the current working directory with a default file name  \ :literal:`inventory\_playbook\_config\_\<YYYY-MM-DD\_HH-MM-SS\>.yml`\ .

      For example, \ :literal:`inventory\_playbook\_config\_2026-01-24\_12-33-20.yml`\ .


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/generate_all_configurations"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-config/generate_all_configurations:

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

      When set to True, automatically generates YAML configurations for all devices in Cisco Catalyst Center.

      This mode discovers all managed devices in Cisco Catalyst Center and extracts all device inventory configurations.

      When enabled, the config parameter becomes optional and will use default values if not provided.

      A default filename will be generated automatically if file\_path is not specified.

      This is useful for complete infrastructure discovery and documentation.

      Note - Only devices with manageable software versions are included in the output.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/global_filters"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-config/global_filters:

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

      These filters apply to all components unless overridden by component-specific filters.

      Supports filtering devices by IP address, hostname, serial number, or MAC address.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/global_filters/hostname_list"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-config/global_filters/hostname_list:

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

      List of device hostnames to include in the YAML configuration file.

      When specified, only devices with matching hostnames will be included.

      For example, ["switch-1", "router-1", "firewall-1"]


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/global_filters/ip_address_list"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-config/global_filters/ip_address_list:

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

      List of device IP addresses to include in the YAML configuration file.

      When specified, only devices with matching management IP addresses will be included.

      For example, ["192.168.1.1", "192.168.1.2", "192.168.1.3"]


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/global_filters/mac_address_list"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-config/global_filters/mac_address_list:

      .. rst-class:: ansible-option-title

      **mac_address_list**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/global_filters/mac_address_list" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of device MAC addresses to include in the YAML configuration file.

      When specified, only devices with matching MAC addresses will be included.

      For example, ["e4:1f:7b:d7:bd:00", "a1:b2:c3:d4:e5:f6"]


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/global_filters/serial_number_list"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-config/global_filters/serial_number_list:

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

      List of device serial numbers to include in the YAML configuration file.

      When specified, only devices with matching serial numbers will be included.

      For example, ["ABC123456789", "DEF987654321"]


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_api_task_timeout"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-dnac_api_task_timeout:

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

      API task timeout in seconds.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`1200`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_debug"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-dnac_debug:

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

      Enable debug logging.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_host"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-dnac_host:

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

      Cisco Catalyst Center hostname or IP address.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_log"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-dnac_log:

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

      Enable logging to file.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_log_append"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-dnac_log_append:

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

      Append to log file instead of overwriting.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_log_file_path"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-dnac_log_file_path:

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

      Path for debug log file.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"dnac.log"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_log_level"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-dnac_log_level:

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

      Log level for module execution.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"WARNING"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_password"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-dnac_password:

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

      Cisco Catalyst Center password.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_port"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-dnac_port:

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

      Cisco Catalyst Center port number.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"443"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_task_poll_interval"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-dnac_task_poll_interval:

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

      Task poll interval in seconds.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`2`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_username"></div>
        <div class="ansibleOptionAnchor" id="parameter-user"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-dnac_username:
      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-user:

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

      Cisco Catalyst Center username.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"admin"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_verify"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-dnac_verify:

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

      Verify SSL certificate for Cisco Catalyst Center.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_version"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-dnac_version:

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

      Cisco Catalyst Center version.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"2.2.3.3"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-state:

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

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__parameter-validate_response_schema:

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

      Validate response schema from API.


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
   - SDK Methods used are - devices.Devices.get\_device\_list - devices.Devices.get\_network\_device\_by\_ip - devices.Devices.get\_device\_by\_ip - licenses.Licenses.device\_license\_summary
   - API Endpoints used are GET /dna/intent/api/v2/devices (list all devices), GET /dna/intent/api/v2/network-device (get network device info), GET /dna/intent/api/v1/interface/ip-address/{ipAddress} (get interfaces for device IP), and GET /dna/intent/api/v1/licenses/device/summary (get device license and site info).
   - Device Consolidation: Devices are grouped and consolidated by their configuration hash. All interfaces from devices with identical configurations are grouped under a single device entry. This reduces redundancy when multiple physical devices share the same configuration.
   - Component Independence: Each component (device\_details, provision\_device, interface\_details) is filtered independently. Global filters apply to all components unless overridden by component-specific filters. Interface details are automatically fetched based on matched device IPs.
   - Interface Discovery: Interfaces are discovered using the IP-to-interface API endpoint. Interface names can be optionally filtered using the interface\_name parameter. When no interfaces match the filter criteria, no interface\_details output is generated.

.. Seealso

See Also
--------

.. seealso::

   \ :ref:`cisco.dnac.inventory\_workflow\_manager <ansible_collections.cisco.dnac.inventory_workflow_manager_module>`\ 
       Module for managing inventory configurations in Cisco Catalyst Center.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Generate inventory playbook for all devices
      cisco.dnac.inventory_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        state: gathered
        config:
          generate_all_configurations: true
          file_mode: "overwrite"
          file_path: "./inventory_devices_all.yml"

    - name: Generate inventory playbook for specific devices by IP address
      cisco.dnac.inventory_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        state: gathered
        config:
          global_filters:
            ip_address_list:
              - "10.195.225.40"
              - "10.195.225.42"
          file_mode: "overwrite"
          file_path: "./inventory_devices_by_ip.yml"

    - name: Generate inventory playbook for devices by hostname
      cisco.dnac.inventory_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        state: gathered
        config:
          global_filters:
            hostname_list:
              - "cat9k_1"
              - "cat9k_2"
              - "switch_1"
          file_mode: "overwrite"
          file_path: "./inventory_devices_by_hostname.yml"

    - name: Generate inventory playbook for devices by serial number
      cisco.dnac.inventory_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        state: gathered
        config:
          global_filters:
            serial_number_list:
              - "FCW2147L0AR1"
              - "FCW2147L0AR2"
          file_mode: "overwrite"
          file_path: "./inventory_devices_by_serial.yml"

    - name: Generate inventory playbook for mixed device filtering
      cisco.dnac.inventory_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        state: gathered
        config:
          global_filters:
            ip_address_list:
              - "10.195.225.40"
            hostname_list:
              - "cat9k_1"
          file_mode: "overwrite"
          file_path: "./inventory_devices_mixed_filter.yml"

    - name: Generate inventory playbook with default file path
      cisco.dnac.inventory_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        state: gathered
        config:
          global_filters:
            ip_address_list:
              - "10.195.225.40"
          file_mode: "overwrite"

    - name: Generate inventory playbook for multiple devices
      cisco.dnac.inventory_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        state: gathered
        config:
          global_filters:
            ip_address_list:
              - "10.195.225.40"
              - "10.195.225.41"
              - "10.195.225.42"
              - "10.195.225.43"
          file_mode: "overwrite"
          file_path: "./inventory_devices_multiple.yml"

    - name: Generate inventory playbook for ACCESS role devices only
      cisco.dnac.inventory_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        state: gathered
        config:
          component_specific_filters:
            components_list: ["device_details"]
            device_details:
              - role: "ACCESS"
            file_mode: "overwrite"
            file_path: "./inventory_access_role_devices.yml"

    - name: Generate inventory playbook with auto-populated provision_wired_device
      cisco.dnac.inventory_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        state: gathered
        config:
          generate_all_configurations: true
          file_mode: "overwrite"
          file_path: "./inventory_with_provisioning.yml"

    - name: Generate inventory playbook with interface filtering
      cisco.dnac.inventory_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        state: gathered
        config:
          global_filters:
            ip_address_list:
              - "10.195.225.40"
              - "10.195.225.42"
          component_specific_filters:
            interface_details:
              interface_name:
                - "Vlan100"
                - "GigabitEthernet1/0/1"
          file_mode: "overwrite"
          file_path: "./inventory_interface_filtered.yml"

    - name: Generate inventory playbook for specific interface on single device
      cisco.dnac.inventory_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        state: gathered
        config:
          global_filters:
            ip_address_list:
              - "10.195.225.40"
          component_specific_filters:
            interface_details:
              interface_name: "Loopback0"
          file_mode: "overwrite"
          file_path: "./inventory_loopback_interface.yml"

    - name: Generate complete inventory with all components and interface filter
      cisco.dnac.inventory_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        state: gathered
        config:
          component_specific_filters:
            components_list: ["device_details", "provision_device", "interface_details"]
            device_details:
              role: "ACCESS"
            interface_details:
              interface_name:
                - "GigabitEthernet1/0/1"
                - "GigabitEthernet1/0/2"
                - "GigabitEthernet1/0/3"
          file_mode: "overwrite"
          file_path: "./inventory_access_with_interfaces.yml"

    - name: Generate UDF output filtered by name (single string)
      cisco.dnac.inventory_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        state: gathered
        config:
          component_specific_filters:
            components_list: ["user_defined_fields"]
            user_defined_fields:
              name: "Cisco Switches"
          file_mode: "overwrite"
          file_path: "./inventory_udf_name_single.yml"

    - name: Generate UDF output filtered by name (list)
      cisco.dnac.inventory_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        state: gathered
        config:
          component_specific_filters:
            components_list: ["user_defined_fields"]
            user_defined_fields:
              name: ["Cisco Switches", "To_test_udf"]
          file_mode: "overwrite"
          file_path: "./inventory_udf_name_list.yml"

    - name: Generate UDF output filtered by value (single string)
      cisco.dnac.inventory_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        state: gathered
        config:
          component_specific_filters:
            components_list: ["user_defined_fields"]
            user_defined_fields:
              value: "2234"
          file_mode: "overwrite"
          file_path: "./inventory_udf_value_single.yml"

    - name: Generate UDF output filtered by value (list)
      cisco.dnac.inventory_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        state: gathered
        config:
          component_specific_filters:
            components_list: ["user_defined_fields"]
            user_defined_fields:
              value: ["2234", "value12345", "value321"]
          file_mode: "overwrite"
          file_path: "./inventory_udf_value_list.yml"




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

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__return-response_1:

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

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"msg": {"YAML config generation Task succeeded for module 'inventory\_workflow\_manager'.": {"file\_path": "inventory\_specific\_ips.yml"}}, "response": {"YAML config generation Task succeeded for module 'inventory\_workflow\_manager'.": {"file\_path": "inventory\_specific\_ips.yml"}}, "status": "success"}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-response_2"></div>

      .. _ansible_collections.cisco.dnac.inventory_playbook_config_generator_module__return-response_2:

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

      A string with the error message returned by the Cisco Catalyst Center Python SDK


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on failure

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"msg": "Invalid 'global\_filters' found for module 'inventory\_workflow\_manager': [\\"Filter 'ip\_address\_list' must be a list, got NoneType\\"]", "response": "Invalid 'global\_filters' found for module 'inventory\_workflow\_manager': [\\"Filter 'ip\_address\_list' must be a list, got NoneType\\"]"}`


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Mridul Saurabh (@msaurabh)
- Madhan Sankaranarayanan (@madsanka)



.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. raw:: html

  <p class="ansible-links">
    <a href="https://github.com/cisco-en-programmability/dnacenter-ansible/issues" aria-role="button" target="_blank" rel="noopener external">Issue Tracker</a>
    <a href="https://github.com/cisco-en-programmability/dnacenter-ansible" aria-role="button" target="_blank" rel="noopener external">Repository (Sources)</a>
  </p>

.. Parsing errors

