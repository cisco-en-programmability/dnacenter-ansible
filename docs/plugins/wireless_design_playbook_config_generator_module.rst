
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

.. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.dnac.wireless_design_playbook_config_generator module -- Generate YAML playbook for \ :literal:`wireless\_design\_workflow\_manager`\  module.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `cisco.dnac collection <https://galaxy.ansible.com/cisco/dnac>`_ (version 6.49.0).

    To install it, use: :code:`ansible-galaxy collection install cisco.dnac`.
    You need further requirements to be able to use this module,
    see :ref:`Requirements <ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module_requirements>` for details.

    To use it in a playbook, specify: :code:`cisco.dnac.wireless_design_playbook_config_generator`.

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

- Generates YAML configurations compatible with the \ :literal:`wireless\_design\_workflow\_manager`\  module, reducing the effort required to manually create Ansible playbooks and enabling programmatic modifications.
- The YAML configurations generated represent the wireless settings configured on the Cisco Catalyst Center.


.. Aliases


.. Requirements

.. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module_requirements:

Requirements
------------
The below requirements are needed on the host that executes this module.

- dnacentersdk \>= 2.3.7.9
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

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config:

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

      A dictionary of filters for generating YAML playbook compatible with the \`wireless\_design\_workflow\_manager\` module.

      Filters specify which components to include in the YAML configuration file.

      If config is not provided (omitted entirely), all configurations for wireless design and feature templates will be generated.

      This is useful for complete brownfield infrastructure discovery and documentation.

      Important - An empty dictionary {} is not valid. Either omit 'config' entirely to generate all configurations, or provide specific filters within 'config'.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters:

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

      If filters for specific components (e.g., ssids or feature\_template\_config) are provided without explicitly including them in components\_list, those components will be automatically added to components\_list.

      At least one of components\_list or component filters must be provided.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/802_11_be_profiles"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/802_11_be_profiles:

      .. rst-class:: ansible-option-title

      **802_11_be_profiles**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/802_11_be_profiles" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filters for 802.11be profile retrieval.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/802_11_be_profiles/profile_name"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/802_11_be_profiles/profile_name:

      .. rst-class:: ansible-option-title

      **profile_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/802_11_be_profiles/profile_name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filter 802.11be profiles by profile name.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/access_point_profiles"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/access_point_profiles:

      .. rst-class:: ansible-option-title

      **access_point_profiles**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/access_point_profiles" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filters for access point profile retrieval.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/access_point_profiles/ap_profile_name"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/access_point_profiles/ap_profile_name:

      .. rst-class:: ansible-option-title

      **ap_profile_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/access_point_profiles/ap_profile_name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filter AP profiles by AP profile name.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/anchor_groups"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/anchor_groups:

      .. rst-class:: ansible-option-title

      **anchor_groups**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/anchor_groups" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filters for anchor group retrieval.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/anchor_groups/anchor_group_name"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/anchor_groups/anchor_group_name:

      .. rst-class:: ansible-option-title

      **anchor_group_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/anchor_groups/anchor_group_name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filter anchor groups by anchor group name.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/components_list"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/components_list:

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

      Valid values are - Wireless SSIDs "ssids" - Interfaces "interfaces" - Power Profiles "power\_profiles" - Access Point Profiles "access\_point\_profiles" - Radio Frequency Profiles "radio\_frequency\_profiles" - Anchor Groups "anchor\_groups" - Feature Template Config "feature\_template\_config" - 802.11be Profiles "802\_11\_be\_profiles" - Flex Connect Configuration "flex\_connect\_configuration"

      If not specified but component specific filters (ssids or feature\_template\_config) are provided, those components are automatically added to this list.

      If neither components\_list nor any component filters are provided, an error will be raised.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ssids"`
      - :ansible-option-choices-entry:`"interfaces"`
      - :ansible-option-choices-entry:`"power\_profiles"`
      - :ansible-option-choices-entry:`"access\_point\_profiles"`
      - :ansible-option-choices-entry:`"radio\_frequency\_profiles"`
      - :ansible-option-choices-entry:`"anchor\_groups"`
      - :ansible-option-choices-entry:`"feature\_template\_config"`
      - :ansible-option-choices-entry:`"802\_11\_be\_profiles"`
      - :ansible-option-choices-entry:`"flex\_connect\_configuration"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/feature_template_config"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/feature_template_config:

      .. rst-class:: ansible-option-title

      **feature_template_config**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/feature_template_config" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filters for wireless feature template configuration retrieval.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/feature_template_config/design_name"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/feature_template_config/design_name:

      .. rst-class:: ansible-option-title

      **design_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/feature_template_config/design_name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filter by feature template design name.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/feature_template_config/feature_template_type"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/feature_template_config/feature_template_type:

      .. rst-class:: ansible-option-title

      **feature_template_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/feature_template_config/feature_template_type" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filter by feature template type.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"aaa\_radius\_attribute"`
      - :ansible-option-choices-entry:`"advanced\_ssid"`
      - :ansible-option-choices-entry:`"clean\_air\_configuration"`
      - :ansible-option-choices-entry:`"dot11ax\_configuration"`
      - :ansible-option-choices-entry:`"dot11be\_configuration"`
      - :ansible-option-choices-entry:`"event\_driven\_rrm\_configuration"`
      - :ansible-option-choices-entry:`"flexconnect\_configuration"`
      - :ansible-option-choices-entry:`"multicast\_configuration"`
      - :ansible-option-choices-entry:`"rrm\_fra\_configuration"`
      - :ansible-option-choices-entry:`"rrm\_general\_configuration"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/flex_connect_configuration"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/flex_connect_configuration:

      .. rst-class:: ansible-option-title

      **flex_connect_configuration**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/flex_connect_configuration" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filters for flex connect configuration retrieval.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/flex_connect_configuration/site_name_hierarchy"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/flex_connect_configuration/site_name_hierarchy:

      .. rst-class:: ansible-option-title

      **site_name_hierarchy**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/flex_connect_configuration/site_name_hierarchy" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filter flex connect configuration by site name hierarchy.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/interfaces"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/interfaces:

      .. rst-class:: ansible-option-title

      **interfaces**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/interfaces" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filters for wireless interface retrieval.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/interfaces/interface_name"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/interfaces/interface_name:

      .. rst-class:: ansible-option-title

      **interface_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/interfaces/interface_name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filter interfaces by interface name.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/interfaces/vlan_id"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/interfaces/vlan_id:

      .. rst-class:: ansible-option-title

      **vlan_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/interfaces/vlan_id" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filter interfaces by VLAN ID.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/power_profiles"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/power_profiles:

      .. rst-class:: ansible-option-title

      **power_profiles**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/power_profiles" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filters for wireless power profile retrieval.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/power_profiles/power_profile_name"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/power_profiles/power_profile_name:

      .. rst-class:: ansible-option-title

      **power_profile_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/power_profiles/power_profile_name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filter power profiles by power profile name.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/radio_frequency_profiles"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/radio_frequency_profiles:

      .. rst-class:: ansible-option-title

      **radio_frequency_profiles**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/radio_frequency_profiles" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filters for radio frequency profile retrieval.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/radio_frequency_profiles/rf_profile_name"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/radio_frequency_profiles/rf_profile_name:

      .. rst-class:: ansible-option-title

      **rf_profile_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/radio_frequency_profiles/rf_profile_name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filter radio frequency profiles by RF profile name.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/ssids"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/ssids:

      .. rst-class:: ansible-option-title

      **ssids**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/ssids" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filters for SSID retrieval.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/ssids/site_name_hierarchy"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/ssids/site_name_hierarchy:

      .. rst-class:: ansible-option-title

      **site_name_hierarchy**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/ssids/site_name_hierarchy" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filter SSIDs by site name hierarchy.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/ssids/ssid_name"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/ssids/ssid_name:

      .. rst-class:: ansible-option-title

      **ssid_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/ssids/ssid_name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filter SSIDs by SSID name.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/component_specific_filters/ssids/ssid_type"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-config/component_specific_filters/ssids/ssid_type:

      .. rst-class:: ansible-option-title

      **ssid_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/component_specific_filters/ssids/ssid_type" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filter SSIDs by SSID type.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"Enterprise"`
      - :ansible-option-choices-entry:`"Guest"`


      .. raw:: html

        </div>




  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnac_api_task_timeout"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-dnac_api_task_timeout:

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

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-dnac_debug:

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

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-dnac_host:

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

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-dnac_log:

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

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-dnac_log_append:

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

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-dnac_log_file_path:

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

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-dnac_log_level:

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

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-dnac_password:

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

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-dnac_port:

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

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-dnac_task_poll_interval:

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

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-dnac_username:
      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-user:

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

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-dnac_verify:

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

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-dnac_version:

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

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-file_mode:

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

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-file_path:

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

      If not provided, the file will be saved in the current working directory with a default file name  \ :literal:`wireless\_design\_playbook\_config\_\<YYYY-MM-DD\_HH-MM-SS\>.yml`\ .

      For example, \ :literal:`wireless\_design\_playbook\_config\_2026-02-20\_13-34-58.yml`\ .


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-state:

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

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__parameter-validate_response_schema:

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
   - Cisco Catalyst Center \>= 2.3.7.9
   - SDK Methods used are
     sites.Sites.get\_site
     site\_design.SiteDesigns.get\_sites
     wirelesss.Wireless.get\_ssid\_by\_site
     wirelesss.Wireless.get\_interfaces
     wirelesss.Wireless.get\_power\_profiles
     wirelesss.Wireless.get\_ap\_profiles
     wirelesss.Wireless.get\_rf\_profiles
     wirelesss.Wireless.get\_anchor\_groups
   - SDK Paths used are
     GET /dna/intent/api/v1/sites
     GET /dna/intent/api/v1/sites/${siteId}/wirelessSettings/ssids
     GET /dna/intent/api/v1/wirelessSettings/interfaces
     GET /dna/intent/api/v1/wirelessSettings/powerProfiles
     GET /dna/intent/api/v1/wirelessSettings/apProfiles
     GET /dna/intent/api/v1/wirelessSettings/rfProfiles
     GET /dna/intent/api/v1/wirelessSettings/anchorGroups
   - Auto-population of components\_list:
     If component-specific filters (such as 'ssids' or 'interfaces' or 'power\_profiles') are provided
     without explicitly including them in 'components\_list', those components will be
     automatically added to 'components\_list'. This simplifies configuration by eliminating
     the need to redundantly specify components in both places.

   - Example of auto-population behavior:
     If you provide filters for 'ssids' without including 'ssids' in 'components\_list',
     the module will automatically add 'ssids' to 'components\_list' before processing.
     This allows you to write more concise playbooks.

   - Validation requirements:
     If 'component\_specific\_filters' is provided, at least one of the following must be true:
     (1) 'components\_list' contains at least one component, OR
     (2) Component-specific filters (e.g., 'ssids', 'interfaces') are provided.
     If neither condition is met, the module will fail with a validation error.

   - Module result behavior (changed/ok/failed):
     The module result reflects local file state only, not Catalyst Center state.
     In overwrite mode, the full file content is compared (excluding volatile
     fields like timestamps and playbook path). In append mode, only the last
     YAML document in the file is compared against the newly generated
     configuration. If a file contains multiple config entries from previous
     appends, only the most recent entry is used for the idempotency check.
     - changed=true (status: success): The generated YAML configuration differs
       from the existing output file (or the file does not exist). The file was
       written and the configuration was updated.
     - changed=false (status: ok): The generated YAML configuration matches the
       existing output file content. The write was skipped as the file is
       already up-to-date.
     - failed=true (status: failed): The module encountered a validation error,
       API failure, or file write error. No file was written or modified.
     Note: Re-running with identical inputs and unchanged Catalyst Center state
     will produce changed=false, ensuring idempotent playbook behavior.
   - Does not support \ :literal:`check\_mode`\ 
   - The plugin runs on the control node and does not use any ansible connection plugins instead embedded connection manager from Cisco Catalyst Center SDK
   - The parameters starting with dnac\_ are used by the Cisco Catalyst Center Python SDK to establish the connection

.. Seealso

See Also
--------

.. seealso::

   \ :ref:`cisco.dnac.wireless\_design\_workflow\_manager <ansible_collections.cisco.dnac.wireless_design_workflow_manager_module>`\ 
       Module for managing wireless design and feature template config.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Auto-generate YAML Configuration for all components
      cisco.dnac.template_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: "{{ dnac_log_level }}"
        state: gathered
        # No config provided - generates all configurations

    - name: Generate YAML Configuration with File Path specified
      cisco.dnac.wireless_design_playbook_config_generator:
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
        file_path: "tmp/catc_wireless_config.yml"
        file_mode: "overwrite"
        # No config provided - generates all configurations

    - name: Generate YAML Configuration with specific wireless network components only
      cisco.dnac.wireless_design_playbook_config_generator:
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
        file_path: "tmp/catc_wireless_components_config.yml"
        file_mode: "overwrite"
        config:
          component_specific_filters:
            components_list: ["interfaces", "anchor_groups"]

    - name: Generate YAML Configuration for wireless SSIDs with site filter
      cisco.dnac.wireless_design_playbook_config_generator:
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
        file_path: "tmp/catc_wireless_components_config.yml"
        file_mode: "overwrite"
        config:
          component_specific_filters:
            components_list: ["ssids"]
            ssids:
              - site_name_hierarchy: "Global/USA/San Jose"

    - name: Generate YAML Configuration with multiple filters
      cisco.dnac.wireless_design_playbook_config_generator:
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
        file_path: "/tmp/catc_wireless_components_config.yaml"
        file_mode: "append"
        config:
          component_specific_filters:
            components_list: ["ssids", "feature_template_config"]
            ssids:
              - ssid_name: sample_ssid
                ssid_type: Guest
            feature_template_config:
              - feature_template_type: advanced_ssid




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

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__return-response_1:

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

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"msg": {"components\_processed": 9, "components\_skipped": 0, "configurations\_count": 9, "file\_path": "tmp/all\_configurations.yml", "message": "YAML configuration file generated successfully for module 'wireless\_design\_workflow\_manager'", "status": "success"}, "response": {"components\_processed": 9, "components\_skipped": 0, "configurations\_count": 9, "file\_path": "tmp/all\_configurations.yml", "message": "YAML configuration file generated successfully for module 'wireless\_design\_workflow\_manager'", "status": "success"}, "status": "success"}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-response_2"></div>

      .. _ansible_collections.cisco.dnac.wireless_design_playbook_config_generator_module__return-response_2:

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

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"{\\n    \\"msg\\":\\n        \\"Validation Error: component\_specific\_filters is provided but no components are specified.\\n         Either provide 'components\_list' with at least one component, or provide filters for specific components.\\",\\n    \\"response\\":\\n        \\"Validation Error: component\_specific\_filters is provided but no components are specified.\\n         Either provide 'components\_list' with at least one component, or provide filters for specific components.\\"\\n}\\n"`


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Rugvedi Kapse (@rukapse)
- Sunil Shatagopa (@shatagopasunil)
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

