#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: template_preview
short_description: Manage TemplatePreview objects of ConfigurationTemplates
description:
- Previews an existing template.
version_added: '1.0'
author: first last (@GitHubID)
options:
    params:
        description:
        - TemplatePreviewRequestDTO's params.
        type: dict
    templateId:
        description:
        - TemplatePreviewRequestDTO's templateId.
        type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.template_preview
# Reference by Internet resource
- name: TemplatePreview reference
  description: Complete reference of the TemplatePreview object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: TemplatePreview reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
"""

RETURN = r"""
data_0:
    description: Previews an existing template.
    returned: success,changed,always
    type: dict
    contains:
        cliPreview:
            description: TemplatePreviewRequestDTO's cliPreview.
            returned: success,changed,always
            type: str
            sample: '<clipreview>'
        templateId:
            description: TemplatePreviewRequestDTO's templateId.
            returned: success,changed,always
            type: str
            sample: '<templateid>'
        validationErrors:
            description: TemplatePreviewRequestDTO's validationErrors.
            returned: success,changed,always
            type: dict

"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    ModuleDefinition,
    DNACModule,
    dnac_argument_spec,
)
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.template_preview import (
    module_definition,
)


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()

    module = AnsibleModule(
        argument_spec=argument_spec, supports_check_mode=False, required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "update":
        dnac.disable_validation()
        dnac.exec("put")

    dnac.exit_json()


if __name__ == "__main__":
    main()
