
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

.. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.dnac.sda_host_port_onboarding_playbook_config_generator module -- Generate YAML configurations playbook for 'sda\_host\_port\_onboarding\_workflow\_manager' module.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `cisco.dnac collection <https://galaxy.ansible.com/cisco/dnac>`_ (version 6.49.0).

    To install it, use: :code:`ansible-galaxy collection install cisco.dnac`.
    You need further requirements to be able to use this module,
    see :ref:`Requirements <ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module_requirements>` for details.

    To use it in a playbook, specify: :code:`cisco.dnac.sda_host_port_onboarding_playbook_config_generator`.

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

- Automates brownfield YAML playbook generation for SDA host port onboarding configurations deployed in Cisco Catalyst Center infrastructure.
- Extracts port assignments, port channels, and wireless SSID configurations via REST APIs for fabric sites managed in SDA environments.
- Generates YAML files compatible with sda\_host\_port\_onboarding\_workflow\_manager module for configuration documentation, port onboarding auditing, disaster recovery, and multi-fabric deployment standardization.
- Supports auto-discovery mode for complete fabric infrastructure extraction or component-based filtering for targeted extraction (port assignments, port channels, wireless SSIDs).
- Transforms camelCase API responses to snake\_case YAML format with comprehensive header comments and metadata.


.. Aliases


.. Requirements

.. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module_requirements:

Requirements
------------
The below requirements are needed on the host that executes this module.

- dnacentersdk \>= 2.3.7.9
- python \>= 3.9
- PyYAML \>= 5.1






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

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-config:

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

      A dictionary of filters for generating YAML playbook compatible with the \`sda\_host\_port\_onboarding\_workflow\_manager\` module.

      Filters specify which components to include in the YAML configuration file.

      If "components\_list" is specified, only those components are included, regardless of the filters.

      If config is not provided or is empty, all configurations for all port assignments, port channels and wireless SSIDs will be generated.

      This is useful for complete brownfield infrastructure discovery and documentation.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters"></div>

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-config/component_specific_filters:

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

      If filters for specific components (e.g., port\_assignments, port\_channels, or wireless\_ssids) are provided without explicitly including them in components\_list, those components will be automatically added to components\_list.

      At least one of components\_list or component filters must be provided.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/components_list"></div>

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-config/component_specific_filters/components_list:

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

      List of SDA host port onboarding components to include in YAML configuration.

      Valid values are 'port\_assignments' for interface port assignments, 'port\_channels' for port channel configurations, and 'wireless\_ssids' for wireless SSID mappings to VLANs within fabric sites.

      If specified, only the listed components will be included in the generated YAML file.

      If not specified but component filters (port\_assignments, port\_channels, or wireless\_ssids) are provided, those components are automatically added to this list.

      If neither components\_list nor any component filters are provided, an error will be raised.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"port\_assignments"`
      - :ansible-option-choices-entry:`"port\_channels"`
      - :ansible-option-choices-entry:`"wireless\_ssids"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/port_assignments"></div>

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-config/component_specific_filters/port_assignments:

      .. rst-class:: ansible-option-title

      **port_assignments**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/port_assignments" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filters for port channel configuration extraction.

      Each list entry targets one fabric site with optional device-level filtering by management IP address, serial number, or hostname.

      Extracts only port assignments for specified fabric site hierarchies and optionally only for devices matching the specified device\_ips, serial\_numbers, or hostnames within those sites.

      When multiple device filters (device\_ips, serial\_numbers, hostnames) are specified in the same list entry, they are combined using AND logic. A device must match ALL specified filters to be included.

      Each filter type is optional and independent. Omitting a filter type means no restriction on that attribute.

      Fabric site names must be full hierarchical paths (case-sensitive).

      If not specified when component included in components\_list, extracts all port assignments across all fabric sites and all devices.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/port_assignments/device_ips"></div>

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-config/component_specific_filters/port_assignments/device_ips:

      .. rst-class:: ansible-option-title

      **device_ips**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/port_assignments/device_ips" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of device management IP addresses to filter extraction within this fabric site.

      Each IP is matched against the managementIpAddress field resolved from Catalyst Center for each device in the fabric site.

      Devices whose management IP does not match any IP in this list are skipped.

      Combined with serial\_numbers and hostnames using AND logic when multiple filter types are specified in the same list entry. A device must satisfy all specified filters to be included.

      Scoped per list entry. Each fabric site entry can specify its own set of device IPs independently.

      If omitted, no IP-based filtering is applied and all devices in the fabric site are candidates (subject to other filters).

      For example, ["1.1.1.1", "1.1.1.2"]


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/port_assignments/fabric_site_name_hierarchy"></div>

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-config/component_specific_filters/port_assignments/fabric_site_name_hierarchy:

      .. rst-class:: ansible-option-title

      **fabric_site_name_hierarchy**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/port_assignments/fabric_site_name_hierarchy" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Fabric site hierarchical paths to extract port assignments.

      Site names must match exact hierarchical paths in Catalyst Center (case-sensitive).

      Extracts port assignments for all devices within specified fabric sites.

      For example, "Global/USA/San Jose/Building1"


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/port_assignments/hostnames"></div>

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-config/component_specific_filters/port_assignments/hostnames:

      .. rst-class:: ansible-option-title

      **hostnames**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/port_assignments/hostnames" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of device hostnames to filter extraction within this fabric site.

      Each hostname is matched against the hostname field resolved from Catalyst Center for each device in the fabric site.

      Devices whose hostname does not match any value in this list are skipped.

      Combined with device\_ips and serial\_numbers using AND logic when multiple filter types are specified in the same list entry. A device must satisfy all specified filters to be included.

      Scoped per list entry. Each fabric site entry can specify its own set of hostnames independently.

      If omitted, no hostname-based filtering is applied and all devices in the fabric site are candidates (subject to other filters).

      For example, ["switch1", "switch2"]


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/port_assignments/serial_numbers"></div>

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-config/component_specific_filters/port_assignments/serial_numbers:

      .. rst-class:: ansible-option-title

      **serial_numbers**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/port_assignments/serial_numbers" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of device serial numbers to filter extraction within this fabric site.

      Each serial number is matched against the serialNumber field resolved from Catalyst Center for each device in the fabric site.

      Devices whose serial number does not match any value in this list are skipped.

      Combined with device\_ips and hostnames using AND logic when multiple filter types are specified in the same list entry. A device must satisfy all specified filters to be included.

      Scoped per list entry. Each fabric site entry can specify its own set of serial numbers independently.

      If omitted, no serial number-based filtering is applied and all devices in the fabric site are candidates (subject to other filters).

      For example, ["FJC2327U0S2", "FJC2327U0S3"]


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/port_channels"></div>

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-config/component_specific_filters/port_channels:

      .. rst-class:: ansible-option-title

      **port_channels**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/port_channels" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filters for port channel configuration extraction.

      Each list entry targets one fabric site with optional device-level filtering by management IP address, serial number, or hostname.

      Extracts only port channels for specified fabric site hierarchies and optionally only for devices matching the specified device\_ips, serial\_numbers, or hostnames within those sites.

      When multiple device filters (device\_ips, serial\_numbers, hostnames) are specified in the same list entry, they are combined using AND logic. A device must match ALL specified filters to be included.

      Each filter type is optional and independent. Omitting a filter type means no restriction on that attribute.

      Fabric site names must be full hierarchical paths (case-sensitive).

      If not specified when component included in components\_list, extracts all port channels across all fabric sites and all devices.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/port_channels/device_ips"></div>

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-config/component_specific_filters/port_channels/device_ips:

      .. rst-class:: ansible-option-title

      **device_ips**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/port_channels/device_ips" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of device management IP addresses to filter extraction within this fabric site.

      Each IP is matched against the managementIpAddress field resolved from Catalyst Center for each device in the fabric site.

      Devices whose management IP does not match any IP in this list are skipped.

      Combined with serial\_numbers and hostnames using AND logic when multiple filter types are specified in the same list entry. A device must satisfy all specified filters to be included.

      Scoped per list entry. Each fabric site entry can specify its own set of device IPs independently.

      If omitted, no IP-based filtering is applied and all devices in the fabric site are candidates (subject to other filters).

      For example, ["1.1.1.1", "1.1.1.2"]


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/port_channels/fabric_site_name_hierarchy"></div>

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-config/component_specific_filters/port_channels/fabric_site_name_hierarchy:

      .. rst-class:: ansible-option-title

      **fabric_site_name_hierarchy**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/port_channels/fabric_site_name_hierarchy" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Fabric site hierarchical paths to extract port channels.

      Site names must match exact hierarchical paths in Catalyst Center (case-sensitive).

      Extracts port channel configurations for all devices within specified fabric sites.

      For example, "Global/USA/San Jose/Building1"


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/port_channels/hostnames"></div>

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-config/component_specific_filters/port_channels/hostnames:

      .. rst-class:: ansible-option-title

      **hostnames**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/port_channels/hostnames" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of device hostnames to filter extraction within this fabric site.

      Each hostname is matched against the hostname field resolved from Catalyst Center for each device in the fabric site.

      Devices whose hostname does not match any value in this list are skipped.

      Combined with device\_ips and serial\_numbers using AND logic when multiple filter types are specified in the same list entry. A device must satisfy all specified filters to be included.

      Scoped per list entry. Each fabric site entry can specify its own set of hostnames independently.

      If omitted, no hostname-based filtering is applied and all devices in the fabric site are candidates (subject to other filters).

      For example, ["switch1", "switch2"]


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/port_channels/serial_numbers"></div>

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-config/component_specific_filters/port_channels/serial_numbers:

      .. rst-class:: ansible-option-title

      **serial_numbers**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/port_channels/serial_numbers" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of device serial numbers to filter extraction within this fabric site.

      Each serial number is matched against the serialNumber field resolved from Catalyst Center for each device in the fabric site.

      Devices whose serial number does not match any value in this list are skipped.

      Combined with device\_ips and hostnames using AND logic when multiple filter types are specified in the same list entry. A device must satisfy all specified filters to be included.

      Scoped per list entry. Each fabric site entry can specify its own set of serial numbers independently.

      If omitted, no serial number-based filtering is applied and all devices in the fabric site are candidates (subject to other filters).

      For example, ["FJC2327U0S2", "FJC2327U0S3"]


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/wireless_ssids"></div>

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-config/component_specific_filters/wireless_ssids:

      .. rst-class:: ansible-option-title

      **wireless_ssids**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/wireless_ssids" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filters for wireless SSID configuration extraction.

      Extracts only wireless SSID to VLAN mappings for specified fabric site hierarchies.

      Fabric site names must be full hierarchical paths (case-sensitive).

      If not specified when component included in components\_list, extracts all wireless SSID mappings across all fabric sites.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/wireless_ssids/fabric_site_name_hierarchy"></div>

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-config/component_specific_filters/wireless_ssids/fabric_site_name_hierarchy:

      .. rst-class:: ansible-option-title

      **fabric_site_name_hierarchy**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/wireless_ssids/fabric_site_name_hierarchy" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of fabric site hierarchical paths to extract wireless SSID mappings.

      Site names must match exact hierarchical paths in Catalyst Center (case-sensitive).

      Extracts VLAN to SSID mappings for specified fabric sites.

      For example, ["Global/USA/San Jose/Building1", "Global/USA/RTP/Building2"]


      .. raw:: html

        </div>




  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_api_task_timeout"></div>

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-dnac_api_task_timeout:

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

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-dnac_debug:

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

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-dnac_host:

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

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-dnac_log:

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

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-dnac_log_append:

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

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-dnac_log_file_path:

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

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-dnac_log_level:

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

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-dnac_password:

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

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-dnac_port:

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

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-dnac_task_poll_interval:

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

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-dnac_username:
      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-user:

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

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-dnac_verify:

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

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-dnac_version:

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

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-file_mode:

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


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"overwrite"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"append"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-file_path"></div>

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-file_path:

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

      Absolute or relative path for YAML configuration file output.

      If not provided, generates default filename in current working directory with pattern 'sda\_host\_port\_onboarding\_playbook\_config\_\<YYYY-MM-DD\_HH-MM-SS\>.yml'

      Example default filename 'sda\_host\_port\_onboarding\_playbook\_config\_2026-02-27\_14-31-46.yml'

      Directory created automatically if path does not exist.

      Supports YAML file extension (.yml or .yaml).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-state:

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

      Desired state for YAML playbook generation workflow.

      Only 'gathered' state supported for brownfield SDA host port onboarding extraction.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"gathered"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-validate_response_schema"></div>

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__parameter-validate_response_schema:

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
   - SDK methods utilized - sda.get\_port\_assignments, sda.get\_port\_channels, fabric\_wireless.retrieve\_the\_vlans\_and\_ssids\_mapped\_to\_the\_vlan\_within\_a\_fabric\_site, devices.get\_device\_by\_id, sda.get\_fabric\_sites
   - API paths utilized - GET /dna/intent/api/v1/sda/portAssignments, GET /dna/intent/api/v1/sda/portChannels, GET /dna/intent/api/v1/sda/fabrics/{fabricId}/vlanToSsids GET /dna/intent/api/v1/network-device/{id} GET /dna/intent/api/v1/sda/fabricSites
   - Module is idempotent; multiple runs generate identical YAML content except timestamp in header comments.
   - Check mode supported; validates parameters without file generation.
   - Device management IP addresses are resolved from device IDs for all port configurations enabling device-specific port onboarding playbooks.
   - Generated YAML uses OrderedDumper for consistent key ordering enabling version control.
   - Fabric site hierarchical paths must match exact Catalyst Center fabric site structure.
   - Auto-population of components\_list: If component-specific filters (such as port\_assignments, port\_channels, or wireless\_ssids) are provided without explicitly including them in components\_list, those components will be automatically added to components\_list. This simplifies configuration by eliminating the need to redundantly specify components in both places.
   - Example of auto-population behavior: If you provide filters for port\_assignments without including port\_assignments in components\_list, the module will automatically add port\_assignments to components\_list before processing. This allows you to write more concise playbooks.
   - Validation requirements: If component\_specific\_filters is provided, at least one of the following must be true - (1) components\_list contains at least one component, OR (2) Component-specific filters (e.g., port\_assignments, port\_channels, wireless\_ssids) are provided. If neither condition is met, the module will fail with a validation error.
   - Does not support \ :literal:`check\_mode`\ 
   - The plugin runs on the control node and does not use any ansible connection plugins instead embedded connection manager from Cisco Catalyst Center SDK
   - The parameters starting with dnac\_ are used by the Cisco Catalyst Center Python SDK to establish the connection

.. Seealso

See Also
--------

.. seealso::

   \ :ref:`cisco.dnac.sda\_host\_port\_onboarding\_workflow\_manager <ansible_collections.cisco.dnac.sda_host_port_onboarding_workflow_manager_module>`\ 
       Module for managing SDA host port onboarding workflows in Cisco Catalyst Center.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Generate YAML playbook for host port onboarding workflow manager
        which includes all fabric sites's host port onboarding details
      cisco.dnac.sda_host_port_onboarding_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        state: gathered
        file_mode: "overwrite"

    - name: Generate YAML Configuration with File Path specified
      cisco.dnac.sda_host_port_onboarding_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        state: gathered
        file_path: "host_onboarding_playbook.yml"
        file_mode: "overwrite"

    - name: Generate YAML with multiple fabric sites and per-site device IP filtering
      cisco.dnac.sda_host_port_onboarding_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        state: gathered
        file_path: "host_onboarding_playbook.yml"
        file_mode: "overwrite"
        config:
          component_specific_filters:
            components_list: ["port_assignments", "port_channels"]
            port_assignments:
              - fabric_site_name_hierarchy: "Global/Site_India/Karnataka/Bangalore"
                device_ips:
                  - 1.1.1.1
              - fabric_site_name_hierarchy: "Global/USA/RTP/Building2"
            port_channels:
              - fabric_site_name_hierarchy: "Global/Site_India/Karnataka/Bangalore"
                device_ips:
                  - 1.1.1.1

    - name: Generate YAML Configuration with specific component port assignments filters
      cisco.dnac.sda_host_port_onboarding_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        state: gathered
        file_path: "host_onboarding_playbook.yml"
        file_mode: "overwrite"
        config:
          component_specific_filters:
            components_list: ["port_assignments"]
            port_assignments:
              - fabric_site_name_hierarchy: "Global/Site_India/Karnataka/Bangalore"
                device_ips:
                  - 1.1.1.1
                  - 1.1.1.2

    - name: Generate YAML Configuration with specific component port assignments filters
      cisco.dnac.sda_host_port_onboarding_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        state: gathered
        file_path: "host_onboarding_playbook.yml"
        file_mode: "overwrite"
        config:
          component_specific_filters:
            components_list: ["port_assignments"]
            port_assignments:
              - fabric_site_name_hierarchy: "Global/Site_India/Karnataka/Bangalore"
                serial_numbers:
                  - FJC27251Z8B
                  - FJC27251Z8C

    - name: Generate YAML Configuration with specific component port assignments filters
      cisco.dnac.sda_host_port_onboarding_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        state: gathered
        file_path: "host_onboarding_playbook.yml"
        file_mode: "overwrite"
        config:
          component_specific_filters:
            components_list: ["port_assignments"]
            port_assignments:
              - fabric_site_name_hierarchy: "Global/Site_India/Karnataka/Bangalore"
                hostnames:
                  - switch1
                  - switch2

    - name: Generate YAML Configuration with specific component port channels filters
      cisco.dnac.sda_host_port_onboarding_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        state: gathered
        file_path: "host_onboarding_playbook.yml"
        file_mode: "overwrite"
        config:
          component_specific_filters:
            components_list: ["port_channels"]
            port_channels:
              - fabric_site_name_hierarchy: "Global/Site_India/Karnataka/Bangalore"
                device_ips:
                  - 1.1.1.1
                  - 1.1.1.2

    - name: Generate YAML Configuration with specific component port channels filters
      cisco.dnac.sda_host_port_onboarding_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        state: gathered
        file_path: "host_onboarding_playbook.yml"
        file_mode: "overwrite"
        config:
          component_specific_filters:
            components_list: ["port_channels"]
            port_channels:
              - fabric_site_name_hierarchy: "Global/Site_India/Karnataka/Bangalore"
                serial_numbers:
                  - FJC27251Z8B
                  - FJC27251Z8C

    - name: Generate YAML Configuration with specific component port channels filters
      cisco.dnac.sda_host_port_onboarding_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        state: gathered
        file_path: "host_onboarding_playbook.yml"
        file_mode: "overwrite"
        config:
          component_specific_filters:
            components_list: ["port_channels"]
            port_channels:
              - fabric_site_name_hierarchy: "Global/Site_India/Karnataka/Bangalore"
                hostnames:
                  - switch1
                  - switch2

    - name: Generate YAML with AND-combined device filters per site
      cisco.dnac.sda_host_port_onboarding_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        state: gathered
        file_path: "host_onboarding_playbook.yml"
        file_mode: "overwrite"
        config:
          component_specific_filters:
            components_list:
              - "port_assignments"
              - "port_channels"
            port_assignments:
              # Site 1: AND filter — device must match IP AND hostname
              - fabric_site_name_hierarchy: "Global/USA/San Jose/Building1"
                device_ips:
                  - 1.1.1.1
                hostnames:
                  - switch1
              # Site 2: single filter — only serial number filtering
              - fabric_site_name_hierarchy: "Global/USA/RTP/Building2"
                serial_numbers:
                  - FJC2327U0S2
                  - FJC2327U0S3
              # Site 3: no device filter — extracts all devices
              - fabric_site_name_hierarchy: "Global/India/Bangalore/Building3"
            port_channels:
              - fabric_site_name_hierarchy: "Global/USA/San Jose/Building1"
                device_ips:
                  - 1.1.1.1

    - name: Generate YAML Configuration with specific component wireless ssids filters
      cisco.dnac.sda_host_port_onboarding_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        state: gathered
        file_path: "host_onboarding_playbook.yml"
        file_mode: "overwrite"
        config:
          component_specific_filters:
            components_list: ["wireless_ssids"]
            wireless_ssids:
              fabric_site_name_hierarchy:
                - "Global/Site_India/Karnataka/Bangalore"




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

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__return-response_1:

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

      A dictionary with  with the response returned by the Cisco Catalyst Center Python SDK


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"msg": {"components\_processed": 1, "components\_skipped": 0, "configurations\_count": 1, "file\_path": "host\_onboarding\_playbook.yml", "message": "YAML configuration file generated successfully for module 'sda\_host\_port\_onboarding\_workflow\_manager'", "status": "success"}, "response": {"components\_processed": 1, "components\_skipped": 0, "configurations\_count": 1, "file\_path": "host\_onboarding\_playbook.yml", "message": "YAML configuration file generated successfully for module 'sda\_host\_port\_onboarding\_workflow\_manager'", "status": "success"}, "status": "success"}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-response_2"></div>

      .. _ansible_collections.cisco.dnac.sda_host_port_onboarding_playbook_config_generator_module__return-response_2:

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

      A string with the response returned by the Cisco Catalyst Center Python SDK


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"{\\n    \\"msg\\":\\n        \\"Validation Error: 'component\_specific\_filters' must be provided with 'components\_list' key\\n         when 'generate\_all\_configurations' is set to False.\\",\\n    \\"response\\":\\n        \\"Validation Error: 'component\_specific\_filters' must be provided with 'components\_list' key\\n         when 'generate\_all\_configurations' is set to False.\\"\\n}\\n"`


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Vivek Raj (@vivekraj2000)
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

