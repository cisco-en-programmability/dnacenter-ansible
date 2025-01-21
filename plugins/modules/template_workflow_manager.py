#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
"""Ansible module to perform operations on project and templates in Cisco Catalyst Center."""

from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ['Madhan Sankaranarayanan, Rishita Chowdhary, Akash Bhaskaran, Muthu Rakesh, Abhishek Maheshwari']

DOCUMENTATION = r"""
---
module: template_workflow_manager
short_description: Resource module for Template functions
description:
  - Manages operations for creating, updating, and deleting configuration templates.
  - Creates templates by project and template names.
  - Updates templates by project and template names.
  - Deletes templates by project and template names.
  - Exports projects and templates based on specified parameters.
  - Handles the creation of resources for importing configuration templates and projects.
version_added: '6.6.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author: Madhan Sankaranarayanan (@madhansansel)
        Rishita Chowdhary (@rishitachowdhary)
        Akash Bhaskaran (@akabhask)
        Muthu Rakesh (@MUTHU-RAKESH-27)
        Abhishek Maheshwari (@abmahesh)
options:
  config_verify:
    description: If set to True, verifies the Cisco Catalyst Center configuration after applying the playbook.
    type: bool
    default: false
  state:
    description: Desired state of the Cisco Catalyst Center after module execution.
    type: str
    choices: [merged, deleted]
    default: merged
  config:
    description: Details of templates to manage.
    type: list
    elements: dict
    required: true
    suboptions:
      configuration_templates:
        description: Operations for Create/Update/Delete on a template.
        type: dict
        suboptions:
          author:
            description: Creator of the template.
            type: str
          composite:
            description: Specifies if the template is composite.
            type: bool
          containing_templates:
            description:
              - Set of templates within the main template to define more complex or modular configurations.
              - This is particularly useful in systems that support hierarchical or nested templates.
              - Here parent templates may contain child templates to form a complete configuration.
            suboptions:
              composite:
                description: Specifies if the template is composite.
                type: bool
              description:
                description: Provides a description of the template.
                type: str
              device_types:
                description: List of dictionaries details the types of devices that the templates can be applied to.
                type: list
                elements: dict
                suboptions:
                  product_family:
                    description: Denotes the family to which the device belongs.
                    choices:
                      - Cisco Cloud Services Platform
                      - Cisco Interfaces and Modules
                      - Content Networking
                      - Network Management
                      - NFV-ThirdParty Devices
                      - NFVIS
                      - Routers
                      - Security and VPN
                      - Storage Networking
                      - Switches and Hubs
                      - Voice and Telephony
                      - Wireless Controller
                    type: str
                  product_series:
                    description: Specifies the series classification of the device.
                    type: str
                  product_type:
                    description: Describes the exact type of the device.
                    type: str
              id:
                description: Unique identifier for the template, represented as a UUID.
                type: str
              language:
                description: Programming language used for templating. Options are 'JINJA' for Jinja templating or 'VELOCITY' for Apache Velocity.
                choices:
                  - JINJA
                  - VELOCITY
                type: str
              name:
                description: Designation of the template, serving as its unique name.
                type: str
              project_name:
                description: Title of the project within which the template is categorized and managed.
                type: str
              project_description:
                description: Narrative that elaborates on the purpose and scope of the project.
                type: str
              tags:
                description: A list of dictionaries representing tags associated with the Configuration Template during creation.
                suboptions:
                  id:
                    description: The unique identifier for each tag, presented as a UUID.
                    type: str
                  name:
                    description: The descriptive label or name assigned to the tag.
                    type: str
                type: list
                elements: dict
              template_content:
                description: The actual script or code constituting the body of the template.
                type: str
              template_params:
                description: The customization of the contents within the template.
                elements: dict
                suboptions:
                  binding:
                    description: Associates the parameter with its source.
                    type: str
                  custom_order:
                    description: Specifies a user-defined ordering for the parameter.
                    type: int
                  data_type:
                    description: Identifies the data type of the parameter (e.g., string, integer, boolean).
                    type: str
                  default_value:
                    description: Establishes a default value for the parameter, used if no other value is provided.
                    type: str
                  description:
                    description: Provides a descriptive explanation of the parameter's purpose.
                    type: str
                  display_name:
                    description: The name of the parameter as displayed to users.
                    type: str
                  group:
                    description: Categorizes the parameter into a named group for organizational purposes.
                    type: str
                  id:
                    description: A unique identifier for the parameter, formatted as a UUID.
                    type: str
                  instruction_text:
                    description: Gives guidance or instructions regarding the parameter's use.
                    type: str
                  key:
                    description: A unique key that identifies the parameter within the template.
                    type: str
                  not_param:
                    description: Indicates whether the entry is not to be treated as a parameter.
                    type: bool
                  order:
                    description: Determines the sequence in which the parameter appears relative to others.
                    type: int
                  param_array:
                    description: Specifies if the parameter should be treated as an array.
                    type: bool
                  parameter_name:
                    description: The name of the parameter.
                    type: str
                  provider:
                    description: Denotes the provider associated with the parameter.
                    type: str
                  range:
                    description: Defines the permissible range for the parameter's value.
                    suboptions:
                      id:
                        description: Unique identifier for the range, represented as a UUID.
                        type: str
                      max_value:
                        description: Specifies the maximum allowable value for the parameter.
                        type: int
                      min_value:
                        description: Specifies the minimum allowable value for the parameter.
                        type: int
                    type: list
                    elements: dict
                  required:
                    description: Dictates whether the parameter is required for template operations.
                    type: bool
                  selection:
                    description: Contains options for parameter selection when a choice is available.
                    suboptions:
                      default_selected_values:
                        description: Lists the default values that are preselected.
                        elements: str
                        type: list
                      id:
                        description: A unique identifier for the selection entity, represented as a UUID.
                        type: str
                      selection_type:
                        description: Specifies the type of selection, such as 'SINGLE_SELECT' or 'MULTI_SELECT'.
                        type: str
                      selection_values:
                        description: A dictionary of available values for selection.
                        type: dict
                    type: dict
                type: list
              version:
                description: The current version of template.
                type: str
            type: list
            elements: dict
          custom_params_order:
            description: Specifies the sequence in which custom parameters or variables should be arranged within the template.
            type: bool
          template_description:
            description: Provides a overview  of the template.
            type: str
          device_types:
            description: List of dictionaries details the types of devices that the templates can be applied to.
            type: list
            elements: dict
            suboptions:
              product_family:
                description: Denotes the family to which the device belongs.
                choices:
                  - Cisco Cloud Services Platform
                  - Cisco Interfaces and Modules
                  - Content Networking
                  - Network Management
                  - NFV-ThirdParty Devices
                  - NFVIS
                  - Routers
                  - Security and VPN
                  - Storage Networking
                  - Switches and Hubs
                  - Voice and Telephony
                  - Wireless Controller
                type: str
              product_series:
                description: Specifies the series classification of the device.
                type: str
              product_type:
                description: Describes the exact type of the device.
                type: str
          failure_policy:
            description:
              - Define failure policy if template provisioning fails.
              - failure_policy will be enabled only when the composite is set to True.
            choices:
              - ABORT_TARGET_ON_ERROR
            type: str
          id:
            description: A unique identifier, represented as a UUID.
            type: str
          language:
            description: Programming language used for templating. Options are 'JINJA' for Jinja templating or 'VELOCITY' for Apache Velocity.
            choices:
              - JINJA
              - VELOCITY
            type: str
          template_name:
            description: Name of template. This field is required to create a new template.
            type: str
          project_name:
            description: Title of the project within which the template is categorized and managed.
            type: str
          project_description:
            description: Narrative that elaborates on the purpose and scope of the project.
            type: str
          software_type:
            description: Applicable device software type. This field is required to create a new template.
            choices:
              - IOS
              - IOS-XE
              - IOS-XR
              - NX-OS
              - Cisco Controller
              - Wide Area Application Services
              - Adaptive Security Appliance
              - NFV-OS
              - Others
            type: str
          software_version:
            description: Applicable device software version.
            type: str
          template_tag:
            description: Refers to a keyword, label, or metadata assigned to a template.
            suboptions:
              id:
                description: A unique identifier for the tag, represented as a UUID.
                type: str
              name:
                description: The name of the tag.
                type: str
            type: list
            elements: dict
          template_content:
            description: The actual script or code constituting the body of the template.
            type: str
          template_params:
            description: The customization of the contents within the template.
            suboptions:
              binding:
                description: Associates the parameter with its source.
                type: str
              custom_order:
                description: Specifies a user-defined ordering for the parameter.
                type: int
              data_type:
                description: Identifies the data type of the parameter (e.g., string, integer, boolean).
                type: str
              default_value:
                description: Establishes a default value for the parameter, used if no other value is provided.
                type: str
              description:
                description: Provides a descriptive explanation of the parameter's purpose.
                type: str
              display_name:
                description: The name of the parameter as displayed to users.
                type: str
              group:
                description: Categorizes the parameter into a named group for organizational purposes.
                type: str
              id:
                description: A unique identifier for the parameter, formatted as a UUID.
                type: str
              instruction_text:
                description: Gives guidance or instructions regarding the parameter's use.
                type: str
              key:
                description: A unique key that identifies the parameter within the template.
                type: str
              not_param:
                description: Indicates whether the entry is not to be treated as a parameter.
                type: bool
              order:
                description: Determines the sequence in which the parameter appears relative to others.
                type: int
              param_array:
                description: Specifies if the parameter should be treated as an array.
                type: bool
              parameter_name:
                description: The name of the parameter.
                type: str
              provider:
                description: Denotes the provider associated with the parameter.
                type: str
              range:
                description: Defines the permissible range for the parameter's value.
                suboptions:
                  id:
                    description: Unique identifier for the range, represented as a UUID.
                    type: str
                  max_value:
                    description: Specifies the maximum allowable value for the parameter.
                    type: int
                  min_value:
                    description: Specifies the minimum allowable value for the parameter.
                    type: int
                type: list
                elements: dict
              required:
                description: Dictates whether the parameter is required for template operations.
                type: bool
              selection:
                description: Contains options for parameter selection when a choice is available.
                suboptions:
                  default_selected_values:
                    description: Lists the default values that are preselected.
                    elements: str
                    type: list
                  id:
                    description: A unique identifier for the selection entity, represented as a UUID.
                    type: str
                  selection_type:
                    description: Specifies the type of selection, such as 'SINGLE_SELECT' or 'MULTI_SELECT'.
                    type: str
                  selection_values:
                    description: A dictionary of available values for selection.
                    type: dict
                type: dict
            type: list
            elements: dict
          version:
            description: The current version of template.
            type: str
          version_description:
            description: Template version comments.
            type: str
      export:
        description: Perform export on the projects and templates.
        type: dict
        suboptions:
          project:
            description: Export the project(s) details.
            type: list
            elements: str
          template:
            description: Export the template(s) details.
            type: list
            elements: dict
            suboptions:
              project_name:
                description: Name of the project under the template available.
                type: str
              template_name:
                description: Name of the template which we need to be exported.
                type: str
      import:
        description: Perform import on the projects and templates.
        type: dict
        suboptions:
          project:
            description: Import the projects.
            type: dict
            suboptions:
              do_version:
                description:
                  - Determines whether to create a new version of the project with the imported contents.
                  - If set to true and the project already exists, a new version will be created.
                  - If false, the operation will fail with a 'Project already exists' error if the project already exists.
                type: bool
              project_file:
                description:
                  - Specifies the path to a JSON file that contains the import project configuration.
                  - If both 'project_file' and 'payload' are provided, the 'project_file' will be given priority.
                type: str
                version_added: 6.17.0
              payload:
                description:
                  - Directly imports configuration data into the system using the provided payload.
                  - Offers an alternative to 'project_file' for importing configurations without referencing an external file.
                  - Ignored if 'project_file' is also provided.
                type: list
                elements: dict
                suboptions:
                  name:
                    description: Name of the project to be imported.
                    type: str
          template:
            description: Import the templates.
            type: dict
            suboptions:
              do_version:
                description: DoVersion query parameter. If this flag is true, creates a new
                  version of the template with the imported contents, if the templates already
                  exists. " If false and if template already exists, then operation
                  fails with 'Template already exists' error.
                type: bool
              template_file:
                description:
                  - Specifies the path to a JSON file that contains an import template.
                  - If both 'template_file' and 'payload' are provided, the 'template_file' will be given priority.
                type: str
              payload:
                description:
                  - The payload parameter is used to directly import configuration data into the system.
                  - The payload provides an alternative way to import configurations without the need to reference an external file.
                  - If both 'template_file' and 'payload' are provided, the 'template_file' will be given priority.
                type: list
                elements: dict
                suboptions:
                  author:
                    description: Identifies the creator of the template.
                    type: str
                  composite:
                    description: Specifies if the template is composite.
                    type: bool
                  containing_templates:
                    description:
                      - Refer to a set of templates within the main template to define more complex or modular configurations.
                      - This is particularly useful in systems that support hierarchical or nested templates.
                      - Here parent templates may contain child templates to form a complete configuration.
                    suboptions:
                      composite:
                        description: Specifies if the template is composite.
                        type: bool
                      description:
                        description: Provides a description of the template.
                        type: str
                      device_types:
                        description: List of dictionaries details the types of devices that the templates can be applied to.
                        type: list
                        elements: dict
                        suboptions:
                          product_family:
                            description: Denotes the family to which the device belongs.
                            choices:
                              - Cisco Cloud Services Platform
                              - Cisco Interfaces and Modules
                              - Content Networking
                              - Network Management
                              - NFV-ThirdParty Devices
                              - NFVIS
                              - Routers
                              - Security and VPN
                              - Storage Networking
                              - Switches and Hubs
                              - Voice and Telephony
                              - Wireless Controller
                            type: str
                          product_series:
                            description: Specifies the series classification of the device.
                            type: str
                          product_type:
                            description: Describes the exact type of the device.
                            type: str
                      id:
                        description: Unique identifier for the template, represented as a UUID.
                        type: str
                      language:
                        description: Programming language used for templating. Options are 'JINJA' for Jinja templating or 'VELOCITY' for Apache Velocity.
                        choices:
                          - JINJA
                          - VELOCITY
                        type: str
                      name:
                        description: Designation of the template, serving as its unique name.
                        type: str
                      project_name:
                        description: Title of the project within which the template is categorized and managed.
                        type: str
                      tags:
                        description: A list of dictionaries representing tags associated with the Configuration Template during creation.
                        suboptions:
                          id:
                            description: The unique identifier for each tag, presented as a UUID.
                            type: str
                          name:
                            description: The descriptive label or name assigned to the tag.
                            type: str
                        type: list
                        elements: dict
                      template_content:
                        description: The actual script or code constituting the body of the template.
                        type: str
                      template_params:
                        description: The customization of the contents within the template.
                        elements: dict
                        suboptions:
                          binding:
                            description: Associates the parameter with its source.
                            type: str
                          custom_order:
                            description: Specifies a user-defined ordering for the parameter.
                            type: int
                          data_type:
                            description: Identifies the data type of the parameter (e.g., string, integer, boolean).
                            type: str
                          default_value:
                            description: Establishes a default value for the parameter, used if no other value is provided.
                            type: str
                          description:
                            description: Provides a descriptive explanation of the parameter's purpose.
                            type: str
                          display_name:
                            description: The name of the parameter as displayed to users.
                            type: str
                          group:
                            description: Categorizes the parameter into a named group for organizational purposes.
                            type: str
                          id:
                            description: A unique identifier for the parameter, formatted as a UUID.
                            type: str
                          instruction_text:
                            description: Gives guidance or instructions regarding the parameter's use.
                            type: str
                          key:
                            description: A unique key that identifies the parameter within the template.
                            type: str
                          not_param:
                            description: Indicates whether the entry is not to be treated as a parameter.
                            type: bool
                          order:
                            description: Determines the sequence in which the parameter appears relative to others.
                            type: int
                          param_array:
                            description: Specifies if the parameter should be treated as an array.
                            type: bool
                          parameter_name:
                            description: The name of the parameter.
                            type: str
                          provider:
                            description: Denotes the provider associated with the parameter.
                            type: str
                          range:
                            description: Defines the permissible range for the parameter's value.
                            suboptions:
                              id:
                                description: Unique identifier for the range, represented as a UUID.
                                type: str
                              max_value:
                                description: Specifies the maximum allowable value for the parameter.
                                type: int
                              min_value:
                                description: Specifies the minimum allowable value for the parameter.
                                type: int
                            type: list
                            elements: dict
                          required:
                            description: Dictates whether the parameter is required for template operations.
                            type: bool
                          selection:
                            description: Contains options for parameter selection when a choice is available.
                            suboptions:
                              default_selected_values:
                                description: Lists the default values that are preselected.
                                elements: str
                                type: list
                              id:
                                description: A unique identifier for the selection entity, represented as a UUID.
                                type: str
                              selection_type:
                                description: Specifies the type of selection, such as 'SINGLE_SELECT' or 'MULTI_SELECT'.
                                type: str
                              selection_values:
                                description: A dictionary of available values for selection.
                                type: dict
                            type: dict
                        type: list
                      version:
                        description: The current version of template.
                        type: str
                    type: list
                    elements: dict
                  custom_params_order:
                    description: Specifies the sequence in which custom parameters or variables should be arranged within the template.
                    type: bool
                  template_description:
                    description: Provides a overview  of the template.
                    type: str
                  device_types:
                    description: List of dictionaries details the types of devices that the templates can be applied to.
                    type: list
                    elements: dict
                    suboptions:
                      product_family:
                        description: Denotes the family to which the device belongs.
                        choices:
                          - Cisco Cloud Services Platform
                          - Cisco Interfaces and Modules
                          - Content Networking
                          - Network Management
                          - NFV-ThirdParty Devices
                          - NFVIS
                          - Routers
                          - Security and VPN
                          - Storage Networking
                          - Switches and Hubs
                          - Voice and Telephony
                          - Wireless Controller
                        type: str
                      product_series:
                        description: Specifies the series classification of the device.
                        type: str
                      product_type:
                        description: Describes the exact type of the device.
                        type: str
                  failure_policy:
                    description:
                      - Define failure policy if template provisioning fails.
                      - failure_policy will be enabled only when the composite is set to True.
                    choices:
                      - ABORT_TARGET_ON_ERROR
                    type: str
                  id:
                    description: A unique identifier, represented as a UUID.
                    type: str
                  language:
                    description: Programming language used for templating. Options are 'JINJA' for Jinja templating or 'VELOCITY' for Apache Velocity.
                    choices:
                      - JINJA
                      - VELOCITY
                    type: str
                  template_name:
                    description: Name of template. This field is required to create a new template.
                    type: str
                  project_name:
                    description: Title of the project within which the template is categorized and managed.
                    type: str
                  project_description:
                    description: Narrative that elaborates on the purpose and scope of the project.
                    type: str
                  software_type:
                    description: Applicable device software type. This field is required to create a new template.
                    choices:
                      - IOS
                      - IOS-XE
                      - IOS-XR
                      - NX-OS
                      - Cisco Controller
                      - Wide Area Application Services
                      - Adaptive Security Appliance
                      - NFV-OS
                      - Others
                    type: str
                  software_version:
                    description: Applicable device software version.
                    type: str
                  template_tag:
                    description: Refers to a keyword, label, or metadata assigned to a template.
                    suboptions:
                      id:
                        description: A unique identifier for the tag, represented as a UUID.
                        type: str
                      name:
                        description: The name of the tag.
                        type: str
                    type: list
                    elements: dict
                  template_content:
                    description: The actual script or code constituting the body of the template.
                    type: str
                  template_params:
                    description: The customization of the contents within the template.
                    suboptions:
                      binding:
                        description: Associates the parameter with its source.
                        type: str
                      custom_order:
                        description: Specifies a user-defined ordering for the parameter.
                        type: int
                      data_type:
                        description: Identifies the data type of the parameter (e.g., string, integer, boolean).
                        type: str
                      default_value:
                        description: Establishes a default value for the parameter, used if no other value is provided.
                        type: str
                      description:
                        description: Provides a descriptive explanation of the parameter's purpose.
                        type: str
                      display_name:
                        description: The name of the parameter as displayed to users.
                        type: str
                      group:
                        description: Categorizes the parameter into a named group for organizational purposes.
                        type: str
                      id:
                        description: A unique identifier for the parameter, formatted as a UUID.
                        type: str
                      instruction_text:
                        description: Gives guidance or instructions regarding the parameter's use.
                        type: str
                      key:
                        description: A unique key that identifies the parameter within the template.
                        type: str
                      not_param:
                        description: Indicates whether the entry is not to be treated as a parameter.
                        type: bool
                      order:
                        description: Determines the sequence in which the parameter appears relative to others.
                        type: int
                      param_array:
                        description: Specifies if the parameter should be treated as an array.
                        type: bool
                      parameter_name:
                        description: The name of the parameter.
                        type: str
                      provider:
                        description: Denotes the provider associated with the parameter.
                        type: str
                      range:
                        description: Defines the permissible range for the parameter's value.
                        suboptions:
                          id:
                            description: Unique identifier for the range, represented as a UUID.
                            type: str
                          max_value:
                            description: Specifies the maximum allowable value for the parameter.
                            type: int
                          min_value:
                            description: Specifies the minimum allowable value for the parameter.
                            type: int
                        type: list
                        elements: dict
                      required:
                        description: Dictates whether the parameter is required for template operations.
                        type: bool
                      selection:
                        description: Contains options for parameter selection when a choice is available.
                        suboptions:
                          default_selected_values:
                            description: Lists the default values that are preselected.
                            elements: str
                            type: list
                          id:
                            description: A unique identifier for the selection entity, represented as a UUID.
                            type: str
                          selection_type:
                            description: Specifies the type of selection, such as 'SINGLE_SELECT' or 'MULTI_SELECT'.
                            type: str
                          selection_values:
                            description: A dictionary of available values for selection.
                            type: dict
                        type: dict
                    type: list
                    elements: dict
                  version:
                    description: The current version of template.
                    type: str
              project_name:
                description: ProjectName path parameter. Project name to create template under the
                  project.
                type: str
      deploy_template:
        description: To deploy the template to the devices based on either list of site provisionig details with further filtering
            criteria like device family, device role, device tag or by providing the device specific details which includes device_ips,
            device_hostnames, serial_numbers or mac_addresses.
        type: dict
        suboptions:
          project_name:
            description: Provide the name of project under which the template is available.
            type: str
          template_name:
            description: Name of the template to be deployed.
            type: str
          force_push:
            description: Boolean flag to indicate whether the template should be forcefully pushed to the devices, overriding any existing
                configuration.
            type: bool
          is_composite:
            description: Boolean flag indicating whether the template is composite, which means the template is built using multiple smaller
                templates.
            type: bool
          template_parameters:
            description: A list of parameter name-value pairs used for customizing the template with specific values for each device.
            type: list
            elements: dict
            suboptions:
              param_name:
                description: Name of the parameter in the template that needs to be replaced with a specific value.
                type: str
              param_value:
                description: Value assigned to the parameter for deployment to devices.
                type: str
          device_details:
            description: Details specific to devices where the template will be deployed, including lists of device IPs, hostnames,
                serial numbers, or MAC addresses.
            type: dict
            suboptions:
              device_ips:
                description: A list of IP addresses of the devices where the template will be deployed.
                type: list
                elements: str
              device_hostnames:
                description: A list of hostnames of the devices where the template will be deployed.
                type: list
                elements: str
              serial_numbers:
                description: A list of serial numbers of the devices where the template will be deployed.
                type: list
                elements: str
              mac_addresses:
                description: A list of MAC addresses of the devices where the template will be deployed.
                type: list
                elements: str
          site_provisioning_details:
            description: Parameters related to site-based provisioning, allowing the deployment of templates to devices associated with specific sites, with
                optional filtering by device family, role, or tag.
            type: list
            elements: dict
            suboptions:
              site_name:
                description: Name of the site where the devices are associated for provisioning.
                type: list
                elements: str
              device_family:
                description: Family of the devices (e.g., switches, routers) used to filter devices for template deployment.
                type: str
              device_role:
                description: Role of the devices (e.g., access, core, edge) used to filter devices for template deployment.
                type: str
              device_tag:
                description: Specific device tag used to filter devices for template deployment.
                type: str


requirements:
  - dnacentersdk >= 2.7.2
  - python >= 3.9
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.create_template,
    configuration_templates.ConfigurationTemplates.deletes_the_template,
    configuration_templates.ConfigurationTemplates.update_template,
    configuration_templates.ConfigurationTemplates.export_projects,
    configuration_templates.ConfigurationTemplates.export_templates,
    configuration_templates.ConfigurationTemplates.imports_the_projects_provided,
    configuration_templates.ConfigurationTemplates.imports_the_templates_provided,

  - Paths used are
    post /dna/intent/api/v1/template-programmer/project/{projectId}/template,
    delete /dna/intent/api/v1/template-programmer/template/{templateId},
    put /dna/intent/api/v1/template-programmer/template,
    post /dna/intent/api/v1/template-programmer/project/name/exportprojects,
    post /dna/intent/api/v1/template-programmer/template/exporttemplates,
    post /dna/intent/api/v1/template-programmer/project/importprojects,
    post /dna/intent/api/v1/template-programmer/project/name/{projectName}/template/importtemplates,

"""

EXAMPLES = r"""
- name: Create a new template.
  cisco.dnac.template_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config_verify: True
    config:
    - configuration_templates:
        author: string
        composite: true
        custom_params_order: true
        description: string
        device_types:
        - product_family: string
          product_series: string
          product_type: string
        failure_policy: string
        id: string
        language: string
        name: string
        project_name: string
        project_description: string
        software_type: string
        software_version: string
        tags:
        - id: string
          name: string
        template_content: string
        version: string

- name: Export the projects.
  cisco.dnac.template_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config_verify: True
    config:
      export:
        project:
          - string
          - string

- name: Export the templates.
  cisco.dnac.template_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config_verify: True
    config:
      export:
        template:
          - project_name : string
            template_name: string
          - project_name: string
            template_name: string

- name: Import the Projects.
  cisco.dnac.template_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config_verify: True
    config:
      import:
        project:
          do_version: false
          payload:
          - name: string
          - name: string

- name: Import the Templates.
  cisco.dnac.template_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config_verify: True
    config:
      import:
        template:
          do_version: false
          project_name: string
          template_file: string

- name: Deploy the given template to the devices based on site specific details and other filtering mode
  cisco.dnac.template_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config_verify: True
    config:
      deploy_template:
        project_name: "Sample_Project"
        template_name: "Sample Template"
        force_push: true
        template_parameters:
        - param_name: "vlan_id"
          param_value: "1431"
        - param_name: "vlan_name"
          param_value: "testvlan31"
        site_provisioning_details:
        - site_name: "Global/Bangalore/Building14/Floor1"
          device_family: "Switches and Hubs"

- name: Deploy the given template to the devices based on device specific details
  cisco.dnac.template_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config_verify: True
    config:
      deploy_template:
        project_name: "Sample_Project"
        template_name: "Sample Template"
        force_push: true
        template_parameters:
        - param_name: "vlan_id"
          param_value: "1431"
        - param_name: "vlan_name"
          param_value: "testvlan31"
        device_details:
          device_ips: ["10.1.2.1", "10.2.3.4"]

- name: Delete the given project or template from the Cisco Catalyst Center
  cisco.dnac.template_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{dnac_log_level}}"
    state: deleted
    config_verify: True
    config:
      configuration_templates:
        project_name: "Sample_Project"
        template_name: "Sample Template"
        language: "velocity"
        software_type: "IOS-XE"
        device_types:
        - product_family: "Switches and Hubs"

"""

RETURN = r"""
# Case_1: Successful creation/updation/deletion of template/project
response_1:
  description: A dictionary with versioning details of the template as returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
                        "endTime": 0,
                        "version": 0,
                        "data": String,
                        "startTime": 0,
                        "username": String,
                        "progress": String,
                        "serviceType": String, "rootId": String,
                        "isError": bool,
                        "instanceTenantId": String,
                        "id": String
                        "version": 0
                  },
      "msg": String
    }

# Case_2: Error while deleting a template or when given project is not found
response_2:
  description: A list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: list
  sample: >
    {
      "response": [],
      "msg": String
    }

# Case_3: Given template already exists and requires no update
response_3:
  description: A dictionary with the exisiting template deatails as returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {},
      "msg": String
    }

# Case_4: Given template list that needs to be exported
response_4:
  description: Details of the templates in the list as returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {},
      "msg": String
    }

# Case_5: Given project list that needs to be exported
response_5:
  description: Details of the projects in the list as returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {},
      "msg": String
    }

"""

import copy
import json
import time
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    get_dict_result,
    dnac_compare_equality,
)


class Template(DnacBase):
    """Class containing member attributes for template_workflow_manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.have_project = {}
        self.have_template = {}
        self.supported_states = ["merged", "deleted"]
        self.accepted_languages = ["JINJA", "VELOCITY"]
        self.export_template = []
        self.max_timeout = self.params.get('dnac_api_task_timeout')
        self.result['response'] = [
            {"configurationTemplate": {"response": {}, "msg": {}}},
            {"export": {"response": {}}},
            {"import": {"response": {}}}
        ]

    def validate_input(self):
        """
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.
        Parameters:
            self: The instance of the class containing the 'config' attribute to be validated.
        Returns:
            The method returns an instance of the class with updated attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either 'success' or 'failed').
                - self.validated_config: If successful, a validated version of 'config' parameter.
        Example:
            To use this method, create an instance of the class and call 'validate_input' on it.
            If the validation succeeds, 'self.status' will be 'success' and 'self.validated_config'
            will contain the validated configuration. If it fails, 'self.status' will be 'failed',
            'self.msg' will describe the validation issues.

        """

        if not self.config:
            self.msg = "config not available in playbook for validattion"
            self.status = "success"
            return self

        temp_spec = {
            "configuration_templates": {
                'type': 'dict',
                'tags': {'type': 'list'},
                'author': {'type': 'str'},
                'composite': {'type': 'bool'},
                'containing_templates': {'type': 'list'},
                'custom_params_order': {'type': 'bool'},
                'template_description': {'type': 'str'},
                'device_types': {
                    'type': 'list',
                    'elements': 'dict',
                    'product_family': {'type': 'str'},
                    'product_series': {'type': 'str'},
                    'product_type': {'type': 'str'},
                },
                'failure_policy': {'type': 'str'},
                'id': {'type': 'str'},
                'language': {'type': 'str'},
                'name': {'type': 'str'},
                'project_name': {'type': 'str'},
                'project_description': {'type': 'str'},
                'software_type': {'type': 'str'},
                'software_version': {'type': 'str'},
                'template_content': {'type': 'str'},
                'template_params': {'type': 'list'},
                'template_name': {'type': 'str'},
                'version': {'type': 'str'}
            },
            'deploy_template': {
                'type': 'dict',
                'project_name': {'type': 'str'},
                'template_name': {'type': 'str'},
                'force_push': {'type': 'bool'},
                'is_composite': {'type': 'bool'},
                'template_parameters': {
                    'type': 'list',
                    'elements': 'dict',
                    'param_name': {'type': 'str'},
                    'param_value': {'type': 'str'},
                },
                'device_details': {
                    'type': 'dict',
                    'device_ips': {'type': 'list', 'elements': 'str'},
                    'device_hostnames': {'type': 'list', 'elements': 'str'},
                    'serial_numbers': {'type': 'list', 'elements': 'str'},
                    'mac_addresses': {'type': 'list', 'elements': 'str'},
                },
                'site_provisioning_details': {
                    'type': 'list',
                    'elements': 'dict',
                    'site_name': {'type': 'str'},
                    'device_family': {'type': 'str'},
                    'device_role': {'type': 'str'},
                    'device_tag': {'type': 'str'},
                }
            },
            'export': {
                'type': 'dict',
                'project': {'type': 'list', 'elements': 'str'},
                'template': {
                    'type': 'list',
                    'elements': 'dict',
                    'project_name': {'type': 'str'},
                    'template_name': {'type': 'str'}
                }
            },
            'import': {
                'type': 'dict',
                'project': {
                    'type': 'dict',
                    'project_file': {'type': 'str'},
                    'do_version': {'type': 'str', 'default': 'False'},
                },
                'template': {
                    'type': 'dict',
                    'do_version': {'type': 'str', 'default': 'False'},
                    'template_file': {'type': 'str'},
                    'payload': {
                        'type': 'list',
                        'elements': 'dict',
                        'tags': {'type': 'list'},
                        'author': {'type': 'str'},
                        'composite': {'type': 'bool'},
                        'containing_templates': {'type': 'list'},
                        'custom_params_order': {'type': 'bool'},
                        'template_description': {'type': 'str'},
                        'device_types': {
                            'type': 'list',
                            'elements': 'dict',
                            'product_family': {'type': 'str'},
                            'product_series': {'type': 'str'},
                            'product_type': {'type': 'str'},
                        },
                        'failure_policy': {'type': 'str'},
                        'id': {'type': 'str'},
                        'language': {'type': 'str'},
                        'name': {'type': 'str'},
                        'project_name': {'type': 'str'},
                        'project_description': {'type': 'str'},
                        'software_type': {'type': 'str'},
                        'software_version': {'type': 'str'},
                        'template_content': {'type': 'str'},
                        'template_params': {'type': 'list'},
                        'template_name': {'type': 'str'},
                        'version': {'type': 'str'}
                    }
                }
            }
        }
        # Validate template params
        self.config = self.camel_to_snake_case(self.config)
        valid_temp, invalid_params = validate_list_of_dicts(
            self.config, temp_spec
        )
        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(
                "\n".join(invalid_params))
            self.status = "failed"
            return self

        self.validated_config = valid_temp
        self.log("Successfully validated playbook config params: {0}".format(valid_temp), "INFO")
        self.msg = "Successfully validated input"
        self.status = "success"
        return self

    def get_project_params(self, params):
        """
        Store project parameters from the playbook for template processing in Cisco Catalyst Center.

        Parameters:
            params (dict) - Playbook details containing Project information.

        Returns:
            project_params (dict) - Organized Project parameters.
        """

        project_params = {"name": params.get("project_name"),
                          "description": params.get("project_description")
                          }
        return project_params

    def get_tags(self, _tags):
        """
        Store tags from the playbook for template processing in Cisco Catalyst Center.
        Check using check_return_status()

        Parameters:
            tags (dict) - Tags details containing Template information.

        Returns:
            tags (dict) - Organized tags parameters.
        """

        if _tags is None:
            return None

        tags = []
        i = 0
        for item in _tags:
            tags.append({})
            id = item.get("id")
            if id is not None:
                tags[i].update({"id": id})

            name = item.get("name")
            if name is not None:
                tags[i].update({"name": name})
            else:
                self.msg = "name is required in tags in location " + str(i)
                self.status = "failed"
                return self.check_return_status()

        return tags

    def get_device_types(self, device_types):
        """
        Store device types parameters from the playbook for template processing in Cisco Catalyst Center.
        Check using check_return_status()

        Parameters:
            device_types (dict) - Device types details containing Template information.

        Returns:
            deviceTypes (dict) - Organized device types parameters.
        """

        if device_types is None:
            self.msg = "The parameter 'device_types' is required but not provided."
            self.status = "failed"
            return self.check_return_status()

        deviceTypes = []
        i = 0
        for item in device_types:
            deviceTypes.append({})
            product_family = item.get("product_family")
            if product_family is not None:
                deviceTypes[i].update({"productFamily": product_family})
            else:
                self.msg = "The parameter 'product_family' is required for 'device_types' but not provided."
                self.status = "failed"
                return self.check_return_status()

            product_families_list = ["Cisco Cloud Services Platform", "Cisco Interfaces and Modules",
                                     "Content Networking", "Network Management", "NFV-ThirdParty Devices",
                                     "NFVIS", "Routers", "Security and VPN", "Storage Networking",
                                     "Switches and Hubs", "Voice and Telephony", "Wireless Controller"]
            if product_family not in product_families_list:
                self.msg = "The 'product_family should be in the following list {0}.".format(product_families_list)
                self.status = "failed"
                return self.check_return_status()

            product_series = item.get("product_series")
            if product_series is not None:
                deviceTypes[i].update({"productSeries": product_series})
            product_type = item.get("product_type")
            if product_type is not None:
                deviceTypes[i].update({"productType": product_type})
            i = i + 1

        return deviceTypes

    def get_template_info(self, template_params):
        """
        Store template params from the playbook for template processing in Cisco Catalyst Center.
        Check using check_return_status()

        Parameters:
            template_params (dict) - Playbook details containing template params information.

        Returns:
            templateParams (dict) - Organized template params parameters.
        """

        if template_params is None:
            return None

        templateParams = []
        i = 0
        self.log("Template params details: {0}".format(template_params), "DEBUG")
        for item in template_params:
            self.log("Template params items: {0}".format(item), "DEBUG")
            templateParams.append({})
            binding = item.get("binding")
            if binding is not None:
                templateParams[i].update({"binding": binding})

            custom_order = item.get("custom_order")
            if custom_order is not None:
                templateParams[i].update({"customOrder": custom_order})

            default_value = item.get("default_value")
            if default_value is not None:
                templateParams[i].update({"defaultValue": default_value})

            description = item.get("description")
            if description is not None:
                templateParams[i].update({"description": description})

            display_name = item.get("display_name")
            if display_name is not None:
                templateParams[i].update({"displayName": display_name})

            group = item.get("group")
            if group is not None:
                templateParams[i].update({"group": group})

            id = item.get("id")
            if id is not None:
                templateParams[i].update({"id": id})

            instruction_text = item.get("instruction_text")
            if instruction_text is not None:
                templateParams[i].update({"instructionText": instruction_text})

            key = item.get("key")
            if key is not None:
                templateParams[i].update({"key": key})

            not_param = item.get("not_param")
            if not_param is not None:
                templateParams[i].update({"notParam": not_param})

            order = item.get("order")
            if order is not None:
                templateParams[i].update({"order": order})

            param_array = item.get("param_array")
            if param_array is not None:
                templateParams[i].update({"paramArray": param_array})

            provider = item.get("provider")
            if provider is not None:
                templateParams[i].update({"provider": provider})

            parameter_name = item.get("parameter_name")
            if parameter_name is not None:
                templateParams[i].update({"parameterName": parameter_name})
            else:
                self.msg = "The parameter 'parameter_name' is required for 'template_params' but not provided."
                self.status = "failed"
                return self.check_return_status()

            data_type = item.get("data_type")
            datatypes = ["STRING", "INTEGER", "IPADDRESS", "MACADDRESS", "SECTIONDIVIDER"]
            if data_type is not None:
                templateParams[i].update({"dataType": data_type})
            else:
                self.msg = "dataType is required for the template_params."
                self.status = "failed"
                return self.check_return_status()
            if data_type not in datatypes:
                self.msg = "data_type under template_params should be in " + str(datatypes)
                self.status = "failed"
                return self.check_return_status()

            required = item.get("required")
            if required is not None:
                templateParams[i].update({"required": required})

            range = item.get("range")
            self.log("Template params range list: {0}".format(range), "DEBUG")
            if range is not None:
                templateParams[i].update({"range": []})
                _range = templateParams[i].get("range")
                self.log("Template params range: {0}".format(_range), "DEBUG")
                j = 0
                for value in range:
                    _range.append({})
                    id = value.get("id")
                    if id is not None:
                        _range[j].update({"id": id})
                    max_value = value.get("max_value")
                    if max_value is not None:
                        _range[j].update({"maxValue": max_value})
                    else:
                        self.msg = "The parameter 'max_value' is required for range under 'template_params' but not provided."
                        self.status = "failed"
                        return self.check_return_status()
                    min_value = value.get("min_value")
                    if min_value is not None:
                        _range[j].update({"minValue": min_value})
                    else:
                        self.msg = "The parameter 'min_value' is required for range under 'template_params' but not provided."
                        self.status = "failed"
                        return self.check_return_status()
                    j = j + 1

            self.log("Template params details: {0}".format(templateParams), "DEBUG")
            selection = item.get("selection")
            self.log("Template params selection: {0}".format(selection), "DEBUG")
            if selection is not None:
                templateParams[i].update({"selection": {}})
                _selection = templateParams[i].get("selection")
                id = selection.get("id")
                if id is not None:
                    _selection.update({"id": id})
                default_selected_values = selection.get("default_selected_values")
                if default_selected_values is not None:
                    _selection.update({"defaultSelectedValues": default_selected_values})
                selection_values = selection.get("selection_values")
                if selection_values is not None:
                    _selection.update({"selectionValues": selection_values})
                selection_type = selection.get("selection_type")
                if selection_type is not None:
                    _selection.update({"selectionType": selection_type})
            i = i + 1

        return templateParams

    def get_templates_details(self, name):
        """
        Get the template details from the template name provided in the playbook.

        Parameters:
            name (str) - Name of the template provided in the playbook.

        Returns:
            result (dict) - Template details for the given template name.
        """

        result = None
        items = self.dnac_apply['exec'](
            family="configuration_templates",
            function="get_templates_details",
            op_modifies=True,
            params={"name": name}
        )
        if items:
            result = items

        self.log("Received API response from 'get_templates_details': {0}".format(items), "DEBUG")
        return result

    def get_project_defined_template_details(self, project_name, template_name):
        """
        Get the template details from the template name provided in the playbook.
        Parameters:
            project_name (str) - Name of the project under which templates are associated.
            template_name (str) - Name of the template provided in the playbook.
        Returns:
            template_details (dict) - Template details for the given template name.
        """

        self.log("Starting to retrieve template details for project '{0}' and template '{1}'.".format(project_name, template_name), "INFO")
        template_details = None
        try:
            items = self.dnac_apply['exec'](
                family="configuration_templates",
                function="get_templates_details",
                op_modifies=True,
                params={
                    "project_name": project_name,
                    "name": template_name
                }
            )
            if items:
                template_details = items
                self.log("Received template details for '{0}': {1}".format(template_name, template_details), "DEBUG")
            else:
                self.log("No template details found for project '{0}' and template '{1}'.".format(project_name, template_name), "WARNING")

            self.log("Received API response from 'get_templates_details': {0}".format(template_details), "DEBUG")
        except Exception as e:
            self.log("Exception occurred while retrieving template details for '{0}': {1}".format(template_name, str(e)), "ERROR")

        return template_details

    def get_containing_templates(self, containing_templates):
        """
        Store tags from the playbook for template processing in Cisco Catalyst Center.
        Check using check_return_status()

        Parameters:
            containing_templates (dict) - Containing templates details
            containing Template information.

        Returns:
            containingTemplates (dict) - Organized containing templates parameters.
        """

        if containing_templates is None:
            return None

        containingTemplates = []
        i = 0
        for item in containing_templates:
            containingTemplates.append({})
            _tags = item.get("tags")
            if _tags is not None:
                containingTemplates[i].update({"tags": self.get_tags(_tags)})

            composite = item.get("composite")
            if composite is not None:
                containingTemplates[i].update({"composite": composite})

            description = item.get("description")
            if description is not None:
                containingTemplates[i].update({"description": description})

            device_types = item.get("device_types")
            if device_types is not None:
                containingTemplates[i].update({
                    "deviceTypes": self.get_device_types(device_types)
                })

            name = item.get("name")
            if name is None:
                self.msg = "The parameter 'name' is required under 'containing_templates' but not provided."
                self.status = "failed"
                return self.check_return_status()

            containingTemplates[i].update({"name": name})

            template_details = self.get_templates_details(name).get("response")
            if not template_details:
                self.msg = "No template with the template name '{0}' or it is not versioned".format(name)
                self.status = "failed"
                return self.check_return_status()

            id = template_details[0].get("id")
            if id is not None:
                containingTemplates[i].update({"id": id})

            language = item.get("language")
            if language is None:
                self.msg = "The parameter 'language' is required under 'containing_templates' but not provided."
                self.status = "failed"
                return self.check_return_status()

            language_list = ["JINJA", "VELOCITY"]
            if language not in language_list:
                self.msg = "language under containing templates should be in " + str(language_list)
                self.status = "failed"
                return self.check_return_status()

            containingTemplates[i].update({"language": language})

            project_name = item.get("project_name")
            if project_name is None:
                self.msg = "The parameter 'project_name' is required under 'containing_templates' but not provided."
                self.status = "failed"
                return self.check_return_status()

            containingTemplates[i].update({"projectName": project_name})
            template_content = item.get("template_content")
            if template_content is not None:
                containingTemplates[i].update({"templateContent": template_content})

            template_params = item.get("template_params")
            if template_params is not None:
                containingTemplates[i].update({
                    "templateParams": self.get_template_info(template_params)
                })

            version = item.get("version")
            if version is not None:
                containingTemplates[i].update({"version": version})

            i += 1

        return containingTemplates

    def get_template_params(self, params):
        """
        Store template parameters from the playbook for template processing in Cisco Catalyst Center.

        Parameters:
            params (dict) - Playbook details containing Template information.

        Returns:
            temp_params (dict) - Organized template parameters.
        """

        self.log("Template params playbook details: {0}".format(params), "DEBUG")
        temp_params = {
            "tags": self.get_tags(params.get("template_tag")),
            "author": params.get("author"),
            "composite": params.get("composite"),
            "containingTemplates":
                self.get_containing_templates(params.get("containing_templates")),
            "customParamsOrder": params.get("custom_params_order"),
            "description": params.get("template_description"),
            "deviceTypes":
                self.get_device_types(params.get("device_types")),
            "id": params.get("id"),
            "softwareVersion": params.get("software_version"),
            "templateContent": params.get("template_content"),
            "templateParams":
                self.get_template_info(params.get("template_params")),
            "version": params.get("version"),
        }
        language = params.get("language")
        if not language:
            self.msg = "The parameter 'language' is required but not provided."
            self.status = "failed"
            return self.check_return_status()

        language = language.upper()
        language_list = ["JINJA", "VELOCITY"]
        if language not in language_list:
            self.msg = "language should be in '{0}'".format(language_list)
            self.status = "failed"
            return self.check_return_status()

        temp_params.update({"language": language})

        name = params.get("template_name")
        if not name:
            self.msg = "The parameter 'template_name' is required but not provided."
            self.status = "failed"
            return self.check_return_status()

        temp_params.update({"name": name})

        projectName = params.get("project_name")
        if not projectName:
            self.msg = "The parameter 'project_name' is required but not provided."
            self.status = "failed"
            return self.check_return_status()

        temp_params.update({"projectName": projectName})

        softwareType = params.get("software_type")
        if not softwareType:
            self.msg = "The parameter 'software_type' is required but not provided."
            self.status = "failed"
            return self.check_return_status()

        software_types_list = ["IOS", "IOS-XE", "IOS-XR", "NX-OS",
                               "Cisco Controller", "Wide Area Application Services",
                               "Adaptive Security Appliance", "NFV-OS", "Others"]
        if softwareType not in software_types_list:
            self.msg = "The 'software_type' should be in the following list {0}.".format(software_types_list)
            self.status = "failed"
            return self.check_return_status()

        temp_params.update({"softwareType": softwareType})

        if temp_params.get("composite") is True:
            failure_policy = params.get("failure_policy")
            failure_policy_list = ["ABORT_TARGET_ON_ERROR", None]
            if failure_policy not in failure_policy_list:
                self.msg = "The 'failure_policy' should be in the following list {0}.".format(failure_policy)
                self.status = "failed"
                return self

            temp_params.update({"failurePolicy": failure_policy})

        self.log("Formatted template params details: {0}".format(temp_params), "DEBUG")
        copy_temp_params = copy.deepcopy(temp_params)
        for item in copy_temp_params:
            if temp_params[item] is None:
                del temp_params[item]
        return temp_params

    def get_template(self, config):
        """
        Get the template needed for updation or creation.

        Parameters:
            config (dict) - Playbook details containing Template information.

        Returns:
            result (dict) - Template details for the given template ID.
        """

        result = None
        items = self.dnac_apply['exec'](
            family="configuration_templates",
            function="get_template_details",
            op_modifies=True,
            params={"template_id": config.get("templateId")}
        )
        if items:
            result = items

        self.log("Received API response from 'get_template_details': {0}".format(items), "DEBUG")
        self.result['response'][0].get("configurationTemplate").update({"items": items})
        return result

    def get_uncommitted_template_id(self, project_name, template_name):
        """
        Retrieves the ID of an uncommitted template from a specified project in the Cisco Catalyst Center.

        Args:
            self (object): An instance of the class used for interacting with Cisco Catalyst Center.
            project_name (str): The name of the project under which the template is located.
            template_name (str): The name of the template whose uncommitted ID is to be retrieved.
        Returns:
            str or None: The template ID if found, otherwise `None` if the template is not available or uncommitted.
        Description:
            This function queries the Cisco Catalyst Center for uncommitted templates within a specified project.
            It checks if the template list contains the specified `template_name` and if found, returns the associated
            `templateId`. If the template is not found, the function logs a warning message and returns `None`.
            The function is useful for identifying templates that are not yet committed, which can then be versioned
            or deployed. If the template is unavailable, an appropriate log message is recorded and the function
            exits early with `None`.
        """
        self.log("Retrieving uncommitted template ID for project '{0}' and template "
                 "'{1}'.".format(project_name, template_name), "INFO"
                 )
        template_id = None
        try:
            template_list = self.dnac_apply['exec'](
                family="configuration_templates",
                function="gets_the_templates_available",
                op_modifies=False,
                params={
                    "projectNames": project_name,
                    "un_committed": True
                },
            )
            if not template_list:
                msg = (
                    "No uncommitted templates available under the project '{0}'. "
                    "Cannot commit or deploy the template '{1}' in device(s)."
                ).format(project_name, template_name)
                self.log(msg, "WARNING")
                return template_id

            for template in template_list:
                if template.get("name") == template_name:
                    template_id = template.get("templateId")
                    self.log("Found uncommitted template '{0}' with ID: '{1}'.".format(template_name, template_id), "INFO")
                    return template_id
            self.log("Template '{0}' not found in the uncommitted templates for project '{1}'.".format(template_name, project_name), "WARNING")
        except Exception as e:
            error_msg = (
                "Exception occurred while retrieving uncommitted template ID for project '{0}' and "
                "template '{1}': {2}."
            ).format(project_name, template_name, str(e))
            self.log(error_msg, "ERROR")
            self.msg = error_msg

        return template_id

    def versioned_given_template(self, project_name, template_name, template_id):
        """
        Versions (commits) a specified template in the Cisco Catalyst Center.

        Args:
            self (object): An instance of the class used for interacting with Cisco Catalyst Center.
            project_name (str): The name of the project under which the template resides.
            template_name (str): The name of the template to be versioned.
            template_id (str): The unique identifier of the template to be versioned.
        Returns:
            self (object): The instance of the class itself, with the operation result (success/failure) set accordingly.
        Description:
            This function handles the process of versioning or committing a template in the Cisco Catalyst Center.
            It constructs a request payload with versioning comments and template ID, and then calls the API to
            initiate the versioning task.
            The function returns the class instance for further chaining of operations.
        """

        self.log("Starting the versioning process for template '{0}' in project '{1}'.".format(template_name, project_name), "INFO")
        try:
            comments = (
                "Given template '{0}' under the project '{1}' versioned successfully."
            ).format(template_name, project_name)

            version_params = {
                "comments": comments,
                "templateId": template_id
            }
            self.log("Preparing to version template with parameters: {0}".format(version_params), "DEBUG")
            task_name = "version_template"
            task_id = self.get_taskid_post_api_call("configuration_templates", task_name, version_params)

            if not task_id:
                self.msg = "Unable to retrieve the task_id for the task '{0}'.".format(task_name)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            success_msg = "Given template '{0}' versioned/committed successfully in the Cisco Catalyst Center.".format(template_name)
            self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg)

        except Exception as e:
            self.msg = (
                "An exception occured while versioning the template '{0}' in the Cisco Catalyst "
                "Center: {1}"
            ).format(template_name, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")

        return self

    def get_have_project(self, config):
        """
        Get the current project related information from Cisco Catalyst Center.

        Parameters:
            config (dict) - Playbook details containing Project information.

        Returns:
            template_available (list) - Current project information.
        """

        have_project = {}
        given_projectName = config.get("configuration_templates").get("project_name")
        template_available = None

        # Check if project exists.
        project_details = self.get_project_details(given_projectName)
        # Cisco Catalyst Center returns project details even if the substring matches.
        # Hence check the projectName retrieved from Cisco Catalyst Center.
        if not (project_details and isinstance(project_details, list)):
            self.log("Project: {0} not found, need to create new project in Cisco Catalyst Center"
                     .format(given_projectName), "INFO")
            return None

        fetched_projectName = project_details[0].get('name')
        if fetched_projectName != given_projectName:
            self.log("Project {0} provided is not exact match in Cisco Catalyst Center DB"
                     .format(given_projectName), "INFO")
            return None

        template_available = project_details[0].get('templates')
        have_project["project_found"] = True
        have_project["id"] = project_details[0].get("id")
        have_project["isDeletable"] = project_details[0].get("isDeletable")

        self.have_project = have_project
        return template_available

    def get_have_template(self, config, template_available):
        """
        Get the current template related information from Cisco Catalyst Center.

        Parameters:
            config (dict) - Playbook details containing Template information.
            template_available (list) -  Current project information.

        Returns:
            self
        """

        projectName = config.get("configuration_templates").get("project_name")
        templateName = config.get("configuration_templates").get("template_name")
        template = None
        have_template = {}

        have_template["isCommitPending"] = False
        have_template["template_found"] = False

        template_details = get_dict_result(template_available,
                                           "name",
                                           templateName)
        # Check if specified template in playbook is available
        if not template_details:
            self.log("Template {0} not found in project {1}"
                     .format(templateName, projectName), "INFO")
            self.msg = "Template : {0} missing, new template to be created".format(templateName)
            self.status = "success"
            return self

        config["templateId"] = template_details.get("id")
        have_template["id"] = template_details.get("id")
        # Get available templates which are committed under the project
        template_list = self.dnac_apply['exec'](
            family="configuration_templates",
            function="gets_the_templates_available",
            op_modifies=True,
            params={"projectNames": config.get("projectName")},
        )
        have_template["isCommitPending"] = True
        # This check will fail if specified template is there not committed in Cisco Catalyst Center
        if template_list and isinstance(template_list, list):
            template_info = get_dict_result(template_list,
                                            "name",
                                            templateName)
            if template_info:
                template = self.get_template(config)
                have_template["template"] = template
                have_template["isCommitPending"] = False
                have_template["template_found"] = template is not None \
                    and isinstance(template, dict)
                self.log("Template {0} is found and template "
                         "details are :{1}".format(templateName, str(template)), "INFO")

        # There are committed templates in the project but the
        # one specified in the playbook may not be committed
        self.log("Commit pending for template name {0}"
                 " is {1}".format(templateName, have_template.get('isCommitPending')), "INFO")

        self.have_template = have_template
        self.msg = "Successfully collected all template parameters from Cisco Catalyst Center for comparison"
        self.status = "success"
        return self

    def get_have(self, config):
        """
        Get the current project and template details from Cisco Catalyst Center.

        Parameters:
            config (dict) - Playbook details containing Project/Template information.

        Returns:
            self
        """
        have = {}
        configuration_templates = config.get("configuration_templates")
        if configuration_templates:
            if not configuration_templates.get("project_name"):
                self.msg = "The parameter 'project_name' is required but not provided."
                self.status = "failed"
                return self
            template_available = self.get_have_project(config)
            if template_available:
                self.get_have_template(config, template_available)

        deploy_temp_details = config.get("deploy_template")
        if deploy_temp_details:
            template_name = deploy_temp_details.get("template_name")
            project_name = deploy_temp_details.get("project_name")
            self.log("Fetching template details for '{0}' under project '{1}'.".format(template_name, project_name), "INFO")
            temp_details = self.get_project_defined_template_details(project_name, template_name).get("response")

            if temp_details:
                self.log("Given template '{0}' is already committed in the Catalyst Center.".format(template_name), "INFO")
                have["temp_id"] = temp_details[0].get("id")

                self.log("Successfully collected the details for the template '{0}' from the "
                         "Cisco Catalyst Center.".format(template_name), "INFO"
                         )
            else:
                self.log("No details found for template '{0}' under project '{1}'.".format(template_name, project_name), "WARNING")

            self.have = have

        self.msg = "Successfully collected all project and template \
                    parameters from Cisco Catalyst Center for comparison"
        self.status = "success"
        return self

    def get_project_details(self, projectName):
        """
        Get the details of specific project name provided.

        Parameters:
            projectName (str) - Project Name

        Returns:
            items (dict) - Project details with given project name.
        """

        items = self.dnac_apply['exec'](
            family="configuration_templates",
            function='get_projects',
            op_modifies=True,
            params={"name": projectName},
        )
        return items

    def get_want(self, config):
        """
        Get all the template and project related information from playbook
        that is needed to be created in Cisco Catalyst Center.

        Parameters:
            config (dict) - Playbook details.

        Returns:
            self
        """

        want = {}
        configuration_templates = config.get("configuration_templates")
        self.log("Playbook details: {0}".format(config), "INFO")
        if configuration_templates:
            template_params = self.get_template_params(configuration_templates)
            project_params = self.get_project_params(configuration_templates)
            version_comments = configuration_templates.get("version_description")

            if self.params.get("state") == "merged":
                self.update_mandatory_parameters(template_params)

            want["template_params"] = template_params
            want["project_params"] = project_params
            want["comments"] = version_comments

        deploy_temp_details = config.get("deploy_template")
        if deploy_temp_details:
            project_name = deploy_temp_details.get("project_name")
            if not project_name:
                self.msg = (
                    "To Deploy the template in the devices, parameter 'project_name' "
                    "must be given in the playboook."
                )
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            self.log("Project name '{0}' found in the playbook.".format(project_name), "INFO")
            template_name = deploy_temp_details.get("template_name")
            if not template_name:
                self.msg = (
                    "To Deploy the template in the devices, parameter 'template_name' "
                    "must be given in the playboook."
                )
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            self.log("Template name '{0}' found in the playbook.".format(template_name), "INFO")
            device_details = deploy_temp_details.get("device_details")
            site_provisioning_details = deploy_temp_details.get("site_provisioning_details")

            if not (device_details or site_provisioning_details):
                self.msg = (
                    "Either give the parameter 'device_details' or 'site_provisioning_details' "
                    "in the playbook to fetch the device ids and proceed for the deployment of template {0}."
                ).format(template_name)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            self.log("Proceeding with deployment details for template '{0}'.".format(template_name), "INFO")
            want["deploy_tempate"] = deploy_temp_details

        self.want = want
        self.msg = "Successfully collected all parameters from playbook " + \
                   "for comparison"
        self.status = "success"
        return self

    def create_project_or_template(self, is_create_project=False):
        """
        Call Cisco Catalyst Center API to create project or template based on the input provided.

        Parameters:
            is_create_project (bool) - Default value is False.

        Returns:
            creation_id (str) - Project Id.
            created (str) - True if Project created, else False.
        """

        creation_id = None
        created = False
        self.log("Desired State (want): {0}".format(self.want), "INFO")
        template_params = self.want.get("template_params")
        project_params = self.want.get("project_params")

        if is_create_project:
            params_key = project_params
            name = "project: {0}".format(project_params.get('name'))
            validation_string = "Successfully created project"
            creation_value = "create_project"
        else:
            params_key = template_params
            name = "template: {0}".format(template_params.get('name'))
            validation_string = "Successfully created template"
            creation_value = "create_template"

        response = self.dnac_apply['exec'](
            family="configuration_templates",
            function=creation_value,
            op_modifies=True,
            params=params_key,
        )
        if not isinstance(response, dict):
            self.log("Response of '{0}' is not in dictionary format."
                     .format(creation_value), "CRITICAL")
            return creation_id, created

        task_id = response.get("response").get("taskId")
        if not task_id:
            self.log("Task id {0} not found for '{1}'.".format(task_id, creation_value), "CRITICAL")
            return creation_id, created

        while not created:
            task_details = self.get_task_details(task_id)
            if not task_details:
                self.log("Failed to get task details of '{0}' for taskid: {1}"
                         .format(creation_value, task_id), "CRITICAL")
                return creation_id, created

            self.log("Task details for {0}: {1}".format(creation_value, task_details), "DEBUG")
            if task_details.get("isError"):
                self.log("Error occurred for '{0}' with taskid: {1}"
                         .format(creation_value, task_id), "ERROR")
                return task_id, created

            if validation_string not in task_details.get("progress"):
                self.log("'{0}' progress set to {1} for taskid: {2}"
                         .format(creation_value, task_details.get('progress'), task_id), "DEBUG")
                continue

            task_details_data = task_details.get("data")
            value = self.check_string_dictionary(task_details_data)
            if value is None:
                creation_id = task_details.get("data")
            else:
                creation_id = value.get("templateId")
            if not creation_id:
                self.log("Export data is not found for '{0}' with taskid : {1}"
                         .format(creation_value, task_id), "DEBUG")
                continue

            created = True
            if is_create_project:
                # ProjectId is required for creating a new template.
                # Store it with other template parameters.
                template_params["projectId"] = creation_id
                template_params["project_id"] = creation_id

        self.log("New {0} created with id {1}".format(name, creation_id), "DEBUG")
        return creation_id, created

    def requires_update(self):
        """
        Check if the template config given requires update.

        Parameters:
            self - Current object.

        Returns:
            bool - True if any parameter specified in obj_params differs between
            current_obj and requested_obj, indicating that an update is required.
            False if all specified parameters are equal.
        """

        if self.have_template.get("isCommitPending"):
            self.log("Template '{0}' is in saved state and needs to be updated and committed."
                     .format(self.have_template.get("template").get("name")), "DEBUG")
            return True

        current_obj = self.have_template.get("template")
        requested_obj = self.want.get("template_params")
        self.log("Current State (have): {0}".format(current_obj), "INFO")
        self.log("Desired State (want): {0}".format(requested_obj), "INFO")
        obj_params = [
            ("tags", "tags", ""),
            ("author", "author", ""),
            ("composite", "composite", False),
            ("containingTemplates", "containingTemplates", []),
            ("customParamsOrder", "customParamsOrder", False),
            ("description", "description", ""),
            ("deviceTypes", "deviceTypes", []),
            ("failurePolicy", "failurePolicy", ""),
            ("id", "id", ""),
            ("language", "language", "VELOCITY"),
            ("name", "name", ""),
            ("projectName", "projectName", ""),
            ("softwareType", "softwareType", ""),
            ("softwareVersion", "softwareVersion", ""),
            ("templateContent", "templateContent", ""),
            ("templateParams", "templateParams", []),
            ("version", "version", ""),
        ]

        return any(not dnac_compare_equality(current_obj.get(dnac_param, default),
                                             requested_obj.get(ansible_param))
                   for (dnac_param, ansible_param, default) in obj_params)

    def update_mandatory_parameters(self, template_params):
        """
        Update parameters which are required for creating a template.

        Parameters:
            template_params (dict) - Template information.

        Returns:
            None
        """

        # Mandate fields required for creating a new template.
        # Store it with other template parameters.
        template_params["projectId"] = self.have_project.get("id")
        template_params["project_id"] = self.have_project.get("id")
        # Update language,deviceTypes and softwareType if not provided for existing template.
        if not template_params.get("language"):
            template_params["language"] = self.have_template.get('template') \
                .get('language')
        if not template_params.get("deviceTypes"):
            template_params["deviceTypes"] = self.have_template.get('template') \
                .get('deviceTypes')
        if not template_params.get("softwareType"):
            template_params["softwareType"] = self.have_template.get('template') \
                .get('softwareType')

    def validate_input_merge(self, template_exists):
        """
        Validate input after getting all the parameters from Cisco Catalyst Center.
        "If mandate like deviceTypes, softwareType and language "
        "already present in Cisco Catalyst Center for a template."
        "It is not required to be provided in playbook, "
        "but if it is new creation error will be thrown to provide these fields.

        Parameters:
            template_exists (bool) - True if template exists, else False.

        Returns:
            None
        """

        template_params = self.want.get("template_params")
        language = template_params.get("language").upper()
        if language:
            if language not in self.accepted_languages:
                self.msg = "Invalid value language {0} ." \
                           "Accepted language values are {1}" \
                           .format(self.accepted_languages, language)
                self.status = "failed"
                return self
        else:
            template_params["language"] = "JINJA"

        if not template_exists:
            if not template_params.get("deviceTypes") \
               or not template_params.get("softwareType"):
                self.msg = "DeviceTypes and SoftwareType are required arguments to create Templates"
                self.status = "failed"
                return self

        self.msg = "Input validated for merging"
        self.status = "success"
        return self

    def get_export_template_values(self, export_values):
        """
        Get the export template values from the details provided by the playbook.

        Parameters:
            export_values (bool) - All the template available under the project.

        Returns:
            self
        """

        all_project_details = self.dnac._exec(
            family="configuration_templates",
            function='get_projects_details_v2'
        )
        all_project_details = all_project_details.get("response")
        for values in export_values:
            project_name = values.get("project_name")
            self.log("Project name for export template: {0}".format(project_name), "DEBUG")
            self.log("Template details: {0}".format(all_project_details), "DEBUG")
            project_details = get_dict_result(all_project_details,
                                              "name",
                                              project_name)
            if not project_details:
                self.msg = (
                    "There are no projects with the given project name '{project_name}'."
                    .format(project_name=project_name)
                )
                self.status = "failed"
                return self

            all_template_details = project_details.get("templates")
            if not all_template_details:
                self.msg = (
                    "There are no templates associated with the given project name '{project_name}'."
                    .format(project_name=project_name)
                )
                self.status = "failed"
                return self

            self.log("Template details under the project name {0}: {1}"
                     .format(project_name, all_template_details), "DEBUG")
            template_name = values.get("template_name")
            template_details = get_dict_result(all_template_details,
                                               "name",
                                               template_name)
            self.log("Template details with template name {0}: {1}"
                     .format(template_name, template_details), "DEBUG")
            if template_details is None:
                self.msg = "Invalid 'project_name' and 'template_name' in export templates."
                self.status = "failed"
                return self
            self.export_template.append(template_details.get("id"))

        self.msg = "Successfully collected the export template IDs"
        self.status = "success"
        return self

    def update_configuration_templates(self, configuration_templates):
        """
        Update/Create templates and projects in CCC with fields provided in Cisco Catalyst Center.

        Parameters:
            configuration_templates (dict) - Playbook details containing template information.

        Returns:
            self
        """

        is_project_found = self.have_project.get("project_found")
        if not is_project_found:
            project_id, project_created = \
                self.create_project_or_template(is_create_project=True)
            if not project_created:
                self.status = "failed"
                self.msg = "Project creation failed"
                return self

            self.log("project created with projectId: {0}".format(project_id), "DEBUG")

        is_template_found = self.have_template.get("template_found")
        template_params = self.want.get("template_params")
        self.log("Desired template details: {0}".format(template_params), "DEBUG")
        self.log("Current template details: {0}".format(self.have_template), "DEBUG")
        template_id = None
        template_updated = False
        self.validate_input_merge(is_template_found).check_return_status()
        if is_template_found:
            if not self.requires_update():
                # Template does not need update
                self.result['response'][0].get("configurationTemplate").update({
                    'response': self.have_template.get("template"),
                    'msg': "Template does not need update"
                })
                self.status = "exited"
                return self

            template_id = self.have_template.get("id")
            template_params.update({"id": template_id})
            self.log("Current State (have): {0}".format(self.have_template), "INFO")
            self.log("Desired State (want): {0}".format(self.want), "INFO")
            response = self.dnac_apply['exec'](
                family="configuration_templates",
                function="update_template",
                op_modifies=True,
                params=template_params,
            )
            template_updated = True
            self.log("Updating existing template '{0}'."
                     .format(self.have_template.get("template").get("name")), "INFO")

        else:
            if not template_params.get("name"):
                self.msg = "missing required arguments: template_name"
                self.status = "failed"
                return self
            template_id, template_updated = self.create_project_or_template()

        if template_updated:
            # Template needs to be versioned
            version_params = {
                "comments": self.want.get("comments"),
                "templateId": template_id
            }
            response = self.dnac_apply['exec'](
                family="configuration_templates",
                function="version_template",
                op_modifies=True,
                params=version_params
            )
            task_id = response.get("response").get("taskId")
            if not task_id:
                self.msg = "Task id: {0} not found".format(task_id)
                self.status = "failed"
                return self
            task_details = self.get_task_details(task_id)
            self.result['changed'] = True
            self.result['response'][0].get("configurationTemplate")['msg'] = task_details.get('progress')
            self.result['response'][0].get("configurationTemplate")['diff'] = configuration_templates
            self.log("Task details for 'version_template': {0}".format(task_details), "DEBUG")
            self.result['response'][0].get("configurationTemplate")['response'] = task_details if task_details else response

            if not self.result['response'][0].get("configurationTemplate").get('msg'):
                self.msg = "Error while versioning the template"
                self.status = "failed"
                return self
        else:
            task_details = self.get_task_details(template_id)
            self.log('Getting task details from task ID {0}: {1}'.format(template_id, task_details), "DEBUG")
            if task_details.get("failureReason"):
                self.msg = str(task_details.get("failureReason"))
            else:
                self.msg = str(task_details.get("progress"))
            self.status = "failed"

        return self

    def handle_export(self, export):
        """
        Export templates and projects in CCC with fields provided in Cisco Catalyst Center.

        Parameters:
            export (dict) - Playbook details containing export project/template information.

        Returns:
            self
        """

        export_project = export.get("project")
        self.log("Export project playbook details: {0}"
                 .format(export_project), "DEBUG")
        if export_project:
            response = self.dnac._exec(
                family="configuration_templates",
                function='export_projects',
                op_modifies=True,
                params={
                    "payload": export_project,
                },
            )
            validation_string = "successfully exported project"
            self.check_task_response_status(response,
                                            validation_string,
                                            "export_projects",
                                            True).check_return_status()
            self.result['response'][1].get("export").get("response").update({"exportProject": self.msg})

        export_values = export.get("template")
        if export_values:
            self.get_export_template_values(export_values).check_return_status()
            self.log("Exporting template playbook details: {0}"
                     .format(self.export_template), "DEBUG")
            response = self.dnac._exec(
                family="configuration_templates",
                function='export_templates',
                op_modifies=True,
                params={
                    "payload": self.export_template,
                },
            )
            validation_string = "successfully exported template"
            self.check_task_response_status(response,
                                            validation_string,
                                            "export_templates",
                                            True).check_return_status()
            self.result['response'][1].get("export").get("response").update({"exportTemplate": self.msg})

        return self

    def handle_import(self, _import):
        """
        Import templates and projects in CCC with fields provided in Cisco Catalyst Center.

        Parameters:
            _import (dict) - Playbook details containing import project/template information.

        Returns:
            self
        """

        _import_project = _import.get("project")
        if _import_project:
            do_version = _import_project.get("do_version")
            if not do_version:
                do_version = False

            payload = _import.get("project").get("payload")
            project_file = _import.get("project").get("project_file")
            if not (payload or project_file):
                self.msg = "Required parameter 'payload' or 'project_file' is not found under import project"
                self.status = "failed"
                return self

            final_payload = []
            if project_file:
                is_path_exists = self.is_path_exists(project_file)
                if not is_path_exists:
                    self.msg = "Import project file path '{0}' does not exist.".format(project_file)
                    self.status = "failed"
                    return self

                is_json = self.is_json(project_file)
                if not is_json:
                    self.msg = "Import project file '{0}' is not in JSON format".format(project_file)
                    self.status = "failed"
                    return self
                try:
                    with open(project_file, 'r') as file:
                        json_data = file.read()
                    json_project = json.loads(json_data)
                    final_payload = json_project
                except Exception as msg:
                    self.msg = "An unexpected error occurred while processing the file '{0}': {1}".format(project_file, msg)
                    self.status = "failed"
                    return self
            elif payload:
                for item in payload:
                    response = self.get_project_details(item.get("name"))
                    if response == []:
                        final_payload.append(item)

            if final_payload != []:
                _import_project = {
                    "do_version": do_version,
                    "payload": final_payload,
                }
                self.log("Importing project details from the playbook: {0}"
                         .format(_import_project), "DEBUG")
                if _import_project:
                    response = self.dnac._exec(
                        family="configuration_templates",
                        function='imports_the_projects_provided',
                        op_modifies=True,
                        params=_import_project,
                    )
                    validation_string = "successfully imported project"
                    self.check_task_response_status(response, validation_string, "imports_the_projects_provided").check_return_status()
                    self.result['response'][2].get("import").get("response").update({"importProject": "Successfully imported the project(s)."})
            else:
                self.msg = "Projects '{0}' already available.".format(payload)
                self.result['response'][2].get("import").get("response").update({
                    "importProject": "Projects '{0}' already available.".format(payload)
                })

        _import_template = _import.get("template")
        if _import_template:
            do_version = _import_template.get("do_version")
            if not do_version:
                do_version = False

            project_name = _import_template.get("project_name")
            if not _import_template.get("project_name"):
                self.msg = "Required parameter project_name is not found under import template"
                self.status = "failed"
                return self

            is_project_exists = self.get_project_details(project_name)
            if not is_project_exists:
                self.msg = "Project '{0}' is not found.".format(project_name)
                self.status = "failed"
                return self

            payload = _import_template.get("payload")
            template_file = _import_template.get("template_file")
            if not (payload or template_file):
                self.msg = "Required parameter 'payload' or 'template_file' is not found under import template"
                self.status = "failed"
                return self

            final_payload = None
            if template_file:
                is_path_exists = self.is_path_exists(template_file)
                if not is_path_exists:
                    self.msg = "Import template file path '{0}' does not exist.".format(template_file)
                    self.status = "failed"
                    return self

                is_json = self.is_json(template_file)
                if not is_json:
                    self.msg = "Import template file '{0}' is not in JSON format".format(template_file)
                    self.status = "failed"
                    return self
                try:
                    with open(template_file, 'r') as file:
                        json_data = file.read()
                    json_template = json.loads(json_data)
                    final_payload = json_template
                except Exception as msg:
                    self.msg = "An unexpected error occurred while processing the file '{0}': {1}".format(template_file, msg)
                    self.status = "failed"
                    return self

            elif payload:
                final_payload = []
                for item in payload:
                    final_payload.append(self.get_template_params(item))
            import_template = {
                "do_version": do_version,
                "project_name": project_name,
                "payload": final_payload,
            }
            self.log("Import template details from the playbook: {0}"
                     .format(import_template), "DEBUG")
            global_project_name = import_template.get("project_name")
            for item in import_template.get("payload"):
                template_project_name = item.get("projectName")
                if template_project_name is not None and \
                        global_project_name != template_project_name:
                    self.msg = "Template '{0}' under the the 'Import Template' should have project_name as {1}" \
                               .format(item.get("name"), global_project_name)
                    self.log(str(self.msg), "ERROR")
                    self.status = "failed"
                    return self

            if _import_template:
                response = self.dnac._exec(
                    family="configuration_templates",
                    function='imports_the_templates_provided',
                    op_modifies=True,
                    params=import_template
                )
                validation_string = "successfully imported template"
                self.check_task_response_status(response, validation_string, "imports_the_templates_provided").check_return_status()
                self.result['response'][2].get("import").get("response") \
                    .update({"importTemplate": "Successfully imported the templates"})

        return self

    def filter_devices_with_family_role(self, site_assign_device_ids, device_family=None, device_role=None):
        """
        Filters devices based on their family and role from a list of site-assigned device IDs.

        Args:
            self (object): An instance of the class interacting with Cisco Catalyst Center.
            site_assign_device_ids (list): A list of device IDs (strings) assigned to a site that need to be filtered.
            device_family (str, optional): The family of devices to filter by (e.g., 'Switches and Hubs'). If None,
                this filter is not applied. Defaults to None.
            device_role (str, optional): The role of the devices to filter by (e.g., 'ACCESS', 'CORE'). If None,
                this filter is not applied. Defaults to None.
        Returns:
            list (str): A list of filtered device IDs (strings) that belong to the specified device family and role.
            If no matching devices are found, the list will be empty.
        Description:
            This function filters a list of device IDs based on the specified `device_family` and `device_role` by querying
            the Cisco Catalyst Center API. It iterates over each device ID, checking if the device belongs to the specified
            family and has the desired role. Devices that match the criteria are added to the `filtered_device_list`.
            If a device does not match the criteria or no response is received from the API, the function logs an
            informational message and skips that device. In the event of an error during the API call, it logs the error
            message and continues processing the remaining devices.
            The function returns the list of devices that meet the filtering criteria.
        """

        filtered_device_list = []
        self.log("Filtering devices from the provided site-assigned device IDs: {0},  device_family='{1}', "
                 "and device_role='{2}'".format(site_assign_device_ids, device_family, device_role), "DEBUG"
                 )

        for device_id in site_assign_device_ids:
            try:
                self.log("Processing device ID: {0}".format(device_id), "DEBUG")
                response = self.dnac._exec(
                    family="devices",
                    function='get_device_list',
                    op_modifies=True,
                    params={
                        "family": device_family,
                        "id": device_id,
                        "role": device_role
                    }
                )
                if response and "response" in response:
                    response_data = response.get("response")
                else:
                    self.log("No valid response for device with ID '{0}'.".format(device_id), "INFO")
                    continue

                if not response_data:
                    self.log(
                        "Device with ID '{0}' does not match family '{1}' or role '{2}'.".format(device_id, device_family, device_role),
                        "INFO"
                    )
                    continue

                self.log("Device with ID '{0}' matches the criteria.".format(device_id), "DEBUG")
                filtered_device_list.append(device_id)

            except Exception as e:
                error_message = "Error while getting the response of device from Cisco Catalyst Center: {0}".format(str(e))
                self.log(error_message, "CRITICAL")
                continue
        self.log("Completed filtering. Filtered devices: {0}".format(filtered_device_list), "DEBUG")

        return filtered_device_list

    def get_latest_template_version_id(self, template_id, template_name):
        """
        Fetches the latest version ID of a specified template from the Cisco Catalyst Center.

        Args:
            self (object): An instance of the class interacting with Cisco Catalyst Center.
            template_id (str): The unique identifier of the template to retrieve its versions.
            template_name (str): The name of the template for logging and reference purposes.
        Returns:
            str: The ID of the latest version of the template if available; otherwise, returns None.
        Description:
            This method calls the Cisco Catalyst Center API to fetch all versions of the specified template.
            It selects the version with the most recent timestamp and retrieves its version ID.
            If no versions are available or an error occurs during the API call, appropriate logs are generated.
        """
        version_temp_id = None
        self.log(
            "Fetching the latest version ID for template '{0}' using template_id '{1}'.".format(
                template_name, template_id), "DEBUG"
        )

        try:
            response = self.dnac._exec(
                family="configuration_templates",
                function='get_template_versions',
                op_modifies=True,
                params={
                    "template_id": template_id,
                }
            )

            if not response or not isinstance(response, list) or not response[0].get("versionsInfo"):
                self.log(
                    "No version information found for template '{0}' in Cisco Catalyst Center.".format(template_name), "INFO"
                )
                return version_temp_id

            self.log(
                "Successfully retrieved version information for template '{0}'.".format(template_name), "DEBUG"
            )
            versions_info = response[0].get("versionsInfo")
            self.log(
                "Processing version details for template '{0}': {1}".format(template_name, str(versions_info)), "DEBUG"
            )
            latest_version = max(versions_info, key=lambda x: x["versionTime"])
            version_temp_id = latest_version.get("id")
            self.log(
                "Identified the latest version for template '{0}'. Version ID: {1}".format(
                    template_name, version_temp_id), "DEBUG"
            )

        except Exception as e:
            error_message = "Error while getting the latest version id for the template '{0}': '{1}'".format(template_name, str(e))
            self.log(error_message, "CRITICAL")
        self.log(
            "Returning latest version ID '{0}' for template '{1}'.".format(version_temp_id, template_name), "DEBUG"
        )

        return version_temp_id

    def create_payload_for_template_deploy(self, deploy_temp_details, device_ids):
        """
        Creates a payload for deploying a template to specified devices in the Cisco Catalyst Center.

        Args:
            self (object): An instance of the class interacting with Cisco Catalyst Center.
            deploy_temp_details (dict): A dictionary containing details about the template to be deployed.
            device_ids (list): A list of device UUIDs to which the template should be deployed.
        Returns:
            dict: A dictionary representing the payload required to deploy the template.
        Description:
            This function generates the necessary payload for deploying a template to devices in the Cisco Catalyst Center.
            It first checks if the given template is already committed. If not, it fetches its uncommitted version, commits it,
            and uses its template ID for deployment. The payload includes information about target devices and their respective
            template parameters.
            The function logs appropriate messages during the process, including if a template is already committed, if
            parameters are updated, and when the payload is successfully collected.
        """

        project_name = deploy_temp_details.get("project_name")
        template_name = deploy_temp_details.get("template_name")
        self.log(
            "Starting to create deployment payload for template '{0}' in project '{1}'."
            .format(template_name, project_name), "DEBUG"
        )
        # Check if the template is available but not yet committed
        if self.have.get("temp_id"):
            self.log(
                "Template '{0}' is already committed in Cisco Catalyst Center. Using the committed template ID."
                .format(template_name), "INFO"
            )
            template_id = self.have.get("temp_id")
        else:
            self.log(
                "Fetching uncommitted template ID for template '{0}' in project '{1}'.".format(template_name, project_name),
                "DEBUG"
            )
            template_id = self.get_uncommitted_template_id(project_name, template_name)

            if not template_id:
                self.msg = (
                    "Unable to fetch the details for the template '{0}' from the Cisco "
                    "Catalyst Center."
                ).format(template_name)
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            self.log(
                "Template '{0}' is available but not committed yet. Committing template...".format(template_name),
                "INFO"
            )

            # Commit or versioned the given template in the Catalyst Center
            self.versioned_given_template(project_name, template_name, template_id).check_return_status()

        deploy_payload = {
            "forcePushTemplate": deploy_temp_details.get("force_push", False),
            "isComposite": deploy_temp_details.get("is_composite", False),
            "templateId": template_id,
        }
        self.log(
            "Handling template parameters for the deployment of template '{0}'.".format(template_name),
            "DEBUG"
        )
        target_info_list = []
        template_dict = {}
        template_parameters = deploy_temp_details.get("template_parameters")
        if not template_parameters:
            self.msg = (
                "It appears that no template parameters were provided in the playbook. Unfortunately, this "
                "means we cannot proceed with deploying template '{0}' to the devices."
            ).format(template_name)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        for param in template_parameters:
            name = param["param_name"]
            value = param["param_value"]
            self.log("Update the template placeholder for the name '{0}' with value {1}".format(name, value), "DEBUG")
            template_dict[name] = value

        # Get the latest version template ID
        version_template_id = self.get_latest_template_version_id(template_id, template_name)
        if not version_template_id:
            self.log("No versioning found for the template: {0}".format(template_name), "INFO")
            version_template_id = template_id

        self.log("Preparing to deploy template '{0}' to the following device IDs: '{1}'".format(template_name, device_ids), "DEBUG")
        for device_id in device_ids:
            self.log("Adding device '{0}' to the deployment payload.".format(device_id), "DEBUG")
            target_device_dict = {
                "id": device_id,
                "type": "MANAGED_DEVICE_UUID",
                "versionedTemplateId": version_template_id,
                "params": template_dict,
            }
            target_info_list.append(target_device_dict)
            del target_device_dict

        deploy_payload["targetInfo"] = target_info_list
        self.log("Successfully generated deployment payload for template '{0}'.".format(template_name), "INFO")

        return deploy_payload

    def deploy_template_to_devices(self, deploy_temp_payload, template_name, device_ips):
        """
        Deploys a specified template to devices associated with a site in the Cisco Catalyst Center.

        Args:
            self (object): An instance of the class used for interacting with Cisco Catalyst Center.
            deploy_temp_payload (dict): The payload containing the details required to deploy the template.
                This includes the template ID, device details, and template parameters.
            template_name (str): The name of the template to be deployed.
            device_ips (list): The management ip address of the devices to which template will be deployed.
        Returns:
            self (object): The instance of the class itself, with the operation result (success or failure)
            set accordingly.
        Description:
            This function handles the deployment of a template to a set of devices managed in the Cisco Catalyst Center.
            It sends a POST request with the deployment payload and retrieves the task ID associated with the deployment task.
            It then monitors the status of the task using the task ID and logs the result.
            If the task ID is not retrieved or an exception occurs during deployment, the function logs an error message,
            sets the operation result to "failed," and returns the instance.
            The success message indicates that the template has been successfully deployed to all the devices in the specified
            site, while any exceptions are caught and logged with appropriate details.
        """

        try:
            self.log("Deploying the given template {0} to the device(s) {1}.".format(template_name, device_ips))
            payload = {"payload": deploy_temp_payload}
            task_name = "deploy_template_v2"
            task_id = self.get_taskid_post_api_call("configuration_templates", task_name, payload)

            if not task_id:
                self.msg = "Unable to retrieve the task_id for the task '{0}'.".format(task_name)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            loop_start_time = time.time()
            sleep_duration = self.params.get('dnac_task_poll_interval')
            self.log("Starting task monitoring for '{0}' with task ID '{1}'.".format(task_name, task_id), "DEBUG")

            while True:
                task_details = self.get_task_details_by_id(task_id)
                if not task_details:
                    self.msg = "Error retrieving task status for '{0}' with task ID '{1}'".format(task_name, task_id)
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                # Check if the elapsed time exceeds the timeout
                elapsed_time = time.time() - loop_start_time
                if self.check_timeout_and_exit(loop_start_time, task_id, task_name):
                    self.log(
                        "Timeout exceeded after {0:.2f} seconds while monitoring task '{1}' with task ID '{2}'.".format(
                            elapsed_time, task_name, task_id), "DEBUG"
                    )
                    return self

                progress = task_details.get("progress")
                self.log("Task ID '{0}' details for the API '{1}': {2}".format(task_id, task_name, progress), "DEBUG")

                if "not deploying" in progress:
                    self.log("Deployment of the template {0} gets failed because of: {1}".format(template_name, progress), "WARNING")
                    self.msg = progress
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                if "ApplicableTargets" in progress:
                    self.msg = (
                        "Given template '{0}' deployed successfully to all the device(s) '{1}' "
                        " in the Cisco Catalyst Center."
                    ).format(template_name, device_ips)
                    self.set_operation_result("success", True, self.msg, "INFO")
                    return self

                self.log("Waiting for {0} seconds before checking the task status again.".format(sleep_duration), "DEBUG")
                time.sleep(sleep_duration)

        except Exception as e:
            self.msg = (
                "An exception occured while deploying the template '{0}' to the device(s) {1} "
                " in the Cisco Catalyst Center: {2}."
            ).format(template_name, device_ips, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")

        return self

    def get_device_ips_from_config_priority(self, device_details):
        """
        Retrieve device IPs based on the configuration.
        Parameters:
            -  self (object): An instance of a class used for interacting with Cisco Cisco Catalyst Center.
        Returns:
            list: A list containing device IPs.
        Description:
            This method retrieves device IPs based on the priority order specified in the configuration.
            It first checks if device IPs are available. If not, it checks hostnames, serial numbers,
            and MAC addresses in order and retrieves IPs based on availability.
            If none of the information is available, an empty list is returned.
        """
        # Retrieve device IPs from the configuration
        self.log("Retrieving device IPs based on the configuration priority with details: {0}".format(device_details), "INFO")
        try:
            device_ips = device_details.get("device_ips")

            if device_ips:
                self.log("Found device IPs: {0}".format(device_ips), "INFO")
                return device_ips

            # If device IPs are not available, check hostnames
            device_hostnames = device_details.get("device_hostnames")
            if device_hostnames:
                self.log("No device IPs found. Checking hostnames: {0}".format(device_hostnames), "INFO")
                device_ip_dict = self.get_device_ips_from_hostnames(device_hostnames)
                return self.get_list_from_dict_values(device_ip_dict)

            # If hostnames are not available, check serial numbers
            device_serial_numbers = device_details.get("serial_numbers")
            if device_serial_numbers:
                self.log("No device IPs or hostnames found. Checking serial numbers: {0}".format(device_serial_numbers), "INFO")
                device_ip_dict = self.get_device_ips_from_serial_numbers(device_serial_numbers)
                return self.get_list_from_dict_values(device_ip_dict)

            # If serial numbers are not available, check MAC addresses
            device_mac_addresses = device_details.get("mac_addresses")
            if device_mac_addresses:
                self.log("No device IPs, hostnames, or serial numbers found. Checking MAC addresses: {0}".format(device_mac_addresses), "INFO")
                device_ip_dict = self.get_device_ips_from_mac_addresses(device_mac_addresses)
                return self.get_list_from_dict_values(device_ip_dict)

            # If no information is available, return an empty list
            self.log("No device information available to retrieve IPs.", "WARNING")
            return []

        except Exception as e:
            self.log("No device information available to retrieve IPs.", "WARNING")
            return []

    def get_device_ids_from_tag(self, tag_name, tag_id):
        """
        Retrieves the device IDs associated with a specific tag from the Cisco Catalyst Center.

        Args:
            self (object): An instance of the class used for interacting with Cisco Catalyst Center.
            tag_name (str): The name of the tag, used for logging purposes.
            tag_id (str): The unique identifier of the tag from which to retrieve associated device IDs.
        Returns:
            list (str): A list of device IDs (strings) associated with the specified tag. If no devices are found or
            an error occurs, the function returns an empty list.
        Description:
            This function queries the Cisco Catalyst Center API to retrieve a list of devices associated with a given tag.
            It calls the `get_tag_members_by_id` function using the tag's ID, specifying that the tag members should be of
            type "networkdevice". If the API response contains device data, the function extracts and returns the device IDs.
            The function logs whether the tag has associated devices and details about the API response. In the event of an
            exception, it logs an error message, sets the operation result to "failed," and returns an empty list.
        """

        device_ids = []
        self.log("Fetching device IDs associated with the tag '{0}' (ID: {1}).".format(tag_name, tag_id), "INFO")

        try:
            response = self.dnac._exec(
                family="tag",
                function='get_tag_members_by_id',
                op_modifies=False,
                params={
                    "id": tag_id,
                    "member_type": "networkdevice",
                }
            )
            if response and "response" in response:
                response_data = response.get("response")
            else:
                self.log("No valid response for device with tag ID '{0}'.".format(tag_id), "INFO")
                return device_ids

            if not response_data:
                self.log("No device(s) are associated with the tag '{0}'.".format(tag_name), "WARNING")
                return device_ids

            self.log("Received API response from 'get_tag_members_by_id' for the tag {0}: {1}".format(tag_name, response_data), "DEBUG")
            for tag in response_data:
                device_id = tag.get("id")
                self.log("Device ID '{0}' found for tag '{1}'.".format(device_id, tag_name), "DEBUG")
                device_ids.append(device_id)

        except Exception as e:
            self.msg = (
                "Exception occurred while fetching tag id for the tag '{0} 'from "
                "Cisco Catalyst Center: {1}"
            ).format(tag_name, str(e))
            self.set_operation_result("failed", False, self.msg, "INFO").check_return_status()

        return device_ids

    def get_diff_merged(self, config):
        """
        Update/Create templates and projects in CCC with fields provided in Cisco Catalyst Center.
        Export the tempaltes and projects.
        Import the templates and projects.
        Deploy the template to the devices based on device specific details or by fetching the device
        details from site using other filtering parameters like device tag, device family, device role.
        Check using check_return_status().

        Parameters:
            config (dict) - Playbook details containing template information.

        Returns:
            self
        """

        configuration_templates = config.get("configuration_templates")
        if configuration_templates:
            self.update_configuration_templates(configuration_templates).check_return_status()

        _import = config.get("import")
        if _import:
            self.handle_import(_import).check_return_status()

        export = config.get("export")
        if export:
            self.log("Found export configuration: {0}".format(export), "DEBUG")
            self.handle_export(export).check_return_status()

        deploy_temp_details = config.get("deploy_template")
        if deploy_temp_details:
            template_name = deploy_temp_details.get("template_name")
            device_details = deploy_temp_details.get("device_details")
            site_specific_details = deploy_temp_details.get("site_provisioning_details")
            self.log("Deploy template details found for template '{0}'".format(template_name), "DEBUG")
            self.log("Device specific details: {0}".format(device_details), "DEBUG")
            self.log("Site associated provisioning details: {0}".format(site_specific_details), "DEBUG")

            if device_details:
                self.log("Attempting to retrieve device IPs based on priority from device specific details.", "DEBUG")
                device_ips = self.get_device_ips_from_config_priority(device_details)
                if not device_ips:
                    self.msg = (
                        "No matching device management IP addresses found for the "
                        "deployment of template '{0}'."
                    ).format(template_name)
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                self.log("Successfully retrieved device IPs for template '{0}': '{1}'".format(template_name, device_ips), "INFO")
                device_id_dict = self.get_device_ids_from_device_ips(device_ips)
                device_ids = self.get_list_from_dict_values(device_id_dict)

                device_missing_msg = (
                    "There are no device id found for the device(s) '{0}' in the "
                    "Cisco Catalyst Center so cannot deploy the given template '{1}'."
                ).format(device_ips, template_name)
            elif site_specific_details:
                device_ids, site_name_list = [], []

                for site in site_specific_details:
                    site_name = site.get("site_name")
                    site_exists, site_id = self.get_site_id(site_name)
                    self.log("Checking if the site '{0}' exists in Cisco Catalyst Center.".format(site_name), "DEBUG")
                    if not site_exists:
                        self.msg = (
                            "To Deploy the template in the devices, given site '{0}' must be "
                            "present in the Cisco Catalyst Center and it's not there currently."
                        ).format(site_name)
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return self

                    self.log("Retrieving devices associated with site ID '{0}' for site '{1}'.".format(site_id, site_name), "DEBUG")
                    site_response, site_assign_device_ids = self.get_device_ids_from_site(site_name, site_id)
                    site_name_list.append(site_name)

                    if not site_assign_device_ids:
                        device_missing_msg = (
                            "There is no device currently associated with the site '{0}' in the "
                            "Cisco Catalyst Center so cannot deploy the given template '{1}'."
                        ).format(site_name, template_name)
                        self.msg = device_missing_msg
                        self.log(device_missing_msg, "WARNING")
                        continue

                    device_family = site.get("device_family")
                    device_role = site.get("device_role")

                    # Filter devices based on the device family or device role
                    if device_family or device_role:
                        self.log(
                            "Filtering devices based on the device family '{0}' or role '{1}' for the site '{2}'.".format(
                                device_family, device_role, site_name), "DEBUG"
                        )
                        self.log("Filtering devices based on the given family/role for the site {0}.".format(site_name), "INFO")
                        site_assign_device_ids = self.filter_devices_with_family_role(site_assign_device_ids, device_family, device_role)

                    # Filter devices based on the device tag given to the devices
                    tag_name = site.get("device_tag")
                    tag_device_ids = None
                    if tag_name:
                        self.log("Filtering out the devices based on the given device tag: '{0}'".format(tag_name), "INFO")
                        tag_id = self.get_network_device_tag_id(tag_name)
                        self.log("Successfully collected the tag id '{0}' for the tag '{1}'".format(tag_id, tag_name), "INFO")
                        # Get the device ids associated with the given tag for given site
                        tag_device_ids = self.get_device_ids_from_tag(tag_name, tag_id)
                        self.log("Successfully collected the device ids {0} associated with the tag {1}".format(tag_device_ids, tag_name), "INFO")

                    self.log("Getting the device ids based on device assoicated with tag or site or both.", "DEBUG")

                    if tag_device_ids and site_assign_device_ids:
                        self.log("Determining device IDs from site and tag criteria.", "DEBUG")
                        common_device_ids = list(set(tag_device_ids).intersection(set(site_assign_device_ids)))
                        device_ids.extend(common_device_ids)
                    elif site_assign_device_ids and not tag_device_ids:
                        self.log("Getting the device ids based on devices fetched from site.", "DEBUG")
                        device_ids.extend(site_assign_device_ids)
                    elif tag_device_ids and not site_assign_device_ids:
                        self.log("Getting the device ids based on devices fetched with the tag {0}.".format(tag_name), "DEBUG")
                        device_ids.extend(tag_device_ids)
                    else:
                        self.log(
                            "There is no matching device ids found for the deployment of template {0} "
                            "for the given site {1}".format(template_name, site_name), "WARNING"
                        )
                        continue

                device_missing_msg = (
                    "There is no device id found for the given site(s) '{0}' in the "
                    "Cisco Catalyst Center so cannot deploy the template '{1}'."
                ).format(site_name_list, template_name)
            else:
                self.msg = (
                    "Unable to provision the template '{0}' as device related details are "
                    "not given in the playboook. Please provide it either via the parameter "
                    "device_details or with site_provisioning_details."
                ).format(self.msg)
                self.set_operation_result("failed", False, self.msg, "INFO").check_return_status()

            if not device_ids:
                self.msg = device_missing_msg
                self.set_operation_result("failed", False, self.msg, "INFO")
                return self

            device_ip_dict = self.get_device_ips_from_device_ids(device_ids)
            device_ips = self.get_list_from_dict_values(device_ip_dict)
            self.log("Successfully collect the device ips {0} for the device ids {1}.".format(device_ips, device_ids), "INFO")
            deploy_temp_payload = self.create_payload_for_template_deploy(deploy_temp_details, device_ids)
            self.log("Deployment payload created successfully for template '{0}'.".format(template_name), "INFO")
            self.deploy_template_to_devices(deploy_temp_payload, template_name, device_ips).check_return_status()
            self.log("Successfully deployed template '{0}'.".format(template_name), "INFO")

        self.msg = "Successfully completed merged state execution"
        self.status = "success"

        return self

    def delete_project_or_template(self, config, is_delete_project=False):
        """
        Call Cisco Catalyst Center API to delete project or template with provided inputs.

        Parameters:
            config (dict) - Playbook details containing template information.
            is_delete_project (bool) - True if we need to delete project, else False.

        Returns:
            self
        """

        if is_delete_project:
            params_key = {"project_id": self.have_project.get("id")}
            deletion_value = "deletes_the_project"
            name = "project: {0}".format(config.get("configuration_templates").get('project_name'))
        else:
            template_params = self.want.get("template_params")
            params_key = {"template_id": self.have_template.get("id")}
            deletion_value = "deletes_the_template"
            name = "templateName: {0}".format(template_params.get('name'))

        response = self.dnac_apply['exec'](
            family="configuration_templates",
            function=deletion_value,
            op_modifies=True,
            params=params_key,
        )
        task_id = response.get("response").get("taskId")
        sleep_duration = self.params.get('dnac_task_poll_interval')
        if not task_id:
            self.msg = "Unable to retrieve the task ID for the task '{0}'.".format(deletion_value)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        while True:
            task_details = self.get_task_details_by_id(task_id)
            self.log("Printing task details: {0}".format(task_details), "DEBUG")
            if not task_details:
                self.msg = "Unable to delete {0} as task details is empty.".format(deletion_value)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            progress = task_details.get("progress")
            self.log("Task details for the API {0}: {1}".format(deletion_value, progress), "DEBUG")

            if "deleted" in progress:
                self.log("Successfully perform the operation of {0} for {1}".format(deletion_value, name), "INFO")
                self.msg = "Successfully deleted {0} ".format(name)
                self.set_operation_result("success", True, self.msg, "INFO")
                break

            if task_details.get("isError"):
                failure_reason = task_details.get("failureReason")
                if failure_reason:
                    self.msg = (
                        "Failed to perform the operation of {0} for {1} because of: {2}"
                    ).format(deletion_value, name, failure_reason)
                else:
                    self.msg = "Failed to perform the operation of {0} for {1}.".format(deletion_value, name)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                break

            self.log("Waiting for {0} seconds before checking the task status again.".format(sleep_duration), "DEBUG")
            time.sleep(sleep_duration)

        return self

    def get_diff_deleted(self, config):
        """
        Delete projects or templates in Cisco Catalyst Center with fields provided in playbook.

        Parameters:
            config (dict) - Playbook details containing template information.

        Returns:
            self
        """

        configuration_templates = config.get("configuration_templates")
        if configuration_templates:
            is_project_found = self.have_project.get("project_found")
            projectName = config.get("configuration_templates").get("project_name")

            if not is_project_found:
                self.msg = "Project {0} is not found".format(projectName)
                self.status = "failed"
                return self

            is_template_found = self.have_template.get("template_found")
            template_params = self.want.get("template_params")
            templateName = config.get("configuration_templates").get("template_name")
            if template_params.get("name"):
                if is_template_found:
                    self.delete_project_or_template(config)
                else:
                    self.result['response'][0].get("configurationTemplate").update({
                        "msg": "Template with template_name '{0}' already deleted".format(templateName)
                    })
                    self.msg = "Invalid template {0} under project".format(templateName)
                    self.status = "success"
                    return self
            else:
                self.log("Template name is empty, deleting the project '{0}' and "
                         "associated templates"
                         .format(config.get("configuration_templates").get("project_name")), "INFO")
                is_project_deletable = self.have_project.get("isDeletable")
                if is_project_deletable:
                    self.delete_project_or_template(config, is_delete_project=True)
                else:
                    self.msg = "Project is not deletable"
                    self.status = "failed"
                    return self
            self.log("Successfully completed the delete operation for the template {0}".format(templateName), "DEBUG")

        deploy_temp_details = config.get("deploy_template")
        if deploy_temp_details:
            template_name = deploy_temp_details.get("template_name")
            self.msg = (
                "Deleting or removing the device configuration using deployment of template is not supported "
                "for the template {0} in the Cisco Catalyst Center."
            ).format(template_name)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        return self

    def verify_diff_merged(self, config):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is merged (Create/Update).

        Parameters:
            config (dict) - Playbook details containing Global Pool,
            Reserved Pool, and Network Management configuration.

        Returns:
            self
        """

        if config.get("configuration_templates") is not None:
            is_template_available = self.get_have_project(config)
            self.log("Template availability: {0}".format(is_template_available), "INFO")
            if not is_template_available:
                self.msg = "Configuration Template config is not applied to the Cisco Catalyst Center."
                self.status = "failed"
                return self

            self.get_have_template(config, is_template_available)
            self.log("Desired State (have): {0}".format(self.want.get("template_params")), "INFO")
            self.log("Current State (want): {0}".format(self.have_template.get("template")), "INFO")
            if not self.have_template.get("template"):
                self.msg = "No template created with the name '{0}'".format(self.want.get("template_params").get("name"))
                self.status = "failed"
                return self

            template_params = ["language", "name", "projectName",
                               "softwareType", "templateContent"]
            have_template = self.have_template.get("template")
            want_template = self.want.get("template_params")
            for item in template_params:
                if have_template.get(item) != want_template.get(item):
                    self.msg = "Configuration Template config with template_name {0}'s '{1}' is not applied to the Cisco Catalyst Center." \
                               .format(want_template.get("name"), item)
                    self.status = "failed"
                    return self

            want_template_containing_template = want_template.get("containingTemplates")
            if want_template_containing_template:
                for item in want_template_containing_template:
                    name = item.get("name")
                    response = get_dict_result(have_template.get("containingTemplates"), "name", name)
                    if response is None:
                        self.msg = "Configuration Template config with template_name '{0}' under ".format(name) + \
                                   "'containing_templates' is not available in the Cisco Catalyst Center."
                        self.status = "failed"
                        return self
                    for value in item:
                        if item.get(value) != response.get(value):
                            self.msg = "Configuration Template config with template_name " + \
                                       "{0}'s '{1}' is not applied to the Cisco Catalyst Center.".format(name, value)
                            self.status = "failed"
                            return self

            self.log("Successfully validated the Template in the Catalyst Center.", "INFO")
            self.result['response'][0].get("configurationTemplate").get("response").update({"Validation": "Success"})

        self.msg = "Successfully validated the Configuration Templates."
        self.status = "success"
        return self

    def verify_diff_deleted(self, config):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is deleted (delete).

        Parameters:
            config (dict) - Playbook details containing Global Pool,
            Reserved Pool, and Network Management configuration.

        Returns:
            self
        """

        if config.get("configuration_templates") is not None:
            self.log("Current State (have): {0}".format(self.have), "INFO")
            self.log("Desired State (want): {0}".format(self.want), "INFO")
            template_list = self.dnac_apply['exec'](
                family="configuration_templates",
                function="gets_the_templates_available",
                op_modifies=True,
                params={"projectNames": config.get("configuration_templates").get("project_name")},
            )
            if template_list and isinstance(template_list, list):
                templateName = config.get("configuration_templates").get("template_name")
                template_info = get_dict_result(template_list,
                                                "name",
                                                templateName)
                if template_info:
                    self.log("Configuration Template config is not applied to the Cisco Catalyst Center.", "WARNING")
                    return self

                self.log("Successfully validated the absence of Template {0} in the Cisco Catalyst Center.".format(templateName), "INFO")

        return self

    def reset_values(self):
        """
        Reset all neccessary attributes to default values.

        Parameters:
            self - The current object.

        Returns:
            None
        """

        self.have_project.clear()
        self.have_template.clear()
        self.want.clear()


def main():
    """ main entry point for module execution"""

    element_spec = {
        'dnac_host': {'required': True, 'type': 'str'},
        'dnac_port': {'type': 'str', 'default': '443'},
        'dnac_username': {'type': 'str', 'default': 'admin', 'aliases': ['user']},
        'dnac_password': {'type': 'str', 'no_log': True},
        'dnac_verify': {'type': 'bool', 'default': 'True'},
        'dnac_version': {'type': 'str', 'default': '2.2.3.3'},
        'dnac_debug': {'type': 'bool', 'default': False},
        'dnac_log': {'type': 'bool', 'default': False},
        "dnac_log_level": {"type": 'str', "default": 'WARNING'},
        "dnac_log_file_path": {"type": 'str', "default": 'dnac.log'},
        "dnac_log_append": {"type": 'bool', "default": True},
        'validate_response_schema': {'type': 'bool', 'default': True},
        "config_verify": {"type": 'bool', "default": False},
        'dnac_api_task_timeout': {'type': 'int', "default": 1200},
        'dnac_task_poll_interval': {'type': 'int', "default": 2},
        'config': {'required': True, 'type': 'list', 'elements': 'dict'},
        'state': {'default': 'merged', 'choices': ['merged', 'deleted']}
    }
    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)
    ccc_template = Template(module)
    ccc_template.validate_input().check_return_status()
    state = ccc_template.params.get("state")
    config_verify = ccc_template.params.get("config_verify")
    if state not in ccc_template.supported_states:
        ccc_template.status = "invalid"
        ccc_template.msg = "State {0} is invalid".format(state)
        ccc_template.check_return_status()

    for config in ccc_template.validated_config:
        ccc_template.reset_values()
        ccc_template.get_have(config).check_return_status()
        ccc_template.get_want(config).check_return_status()
        ccc_template.get_diff_state_apply[state](config).check_return_status()
        if config_verify:
            ccc_template.verify_diff_state_apply[state](config).check_return_status()

    module.exit_json(**ccc_template.result)


if __name__ == '__main__':
    main()
