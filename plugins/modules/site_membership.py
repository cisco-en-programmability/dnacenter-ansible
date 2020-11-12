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
module: site_membership
short_description: Manage SiteMembership objects of Sites
description:
- Getting the site children details and device details.
version_added: '1.0'
author: first last (@GitHubID)
options:
    site_id:
        description:
        - Site id to retrieve device associated with the site.
        type: str
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.site_membership
# Reference by Internet resource
- name: SiteMembership reference
  description: Complete reference of the SiteMembership object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SiteMembership reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
"""

RETURN = r"""
data_0:
    description: Getting the site children details and device details.
    returned: success,changed,always
    type: dict
    contains:
        site:
            description: Site, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                response:
                    description: It is the site membership's response.
                    returned: success,changed,always
                    type: list
                version:
                    description: It is the site membership's version.
                    returned: success,changed,always
                    type: str
                    sample: '1.0'

        device:
            description: Device, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                response:
                    description: It is the site membership's response.
                    returned: success,changed,always
                    type: list
                version:
                    description: It is the site membership's version.
                    returned: success,changed,always
                    type: str
                    sample: '1.0'
                siteId:
                    description: It is the site membership's siteId.
                    returned: success,changed,always
                    type: str
                    sample: '<siteid>'


"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    ModuleDefinition,
    DNACModule,
    dnac_argument_spec,
)
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.site_membership import (
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

    if state == "query":
        dnac.exec("get")

    dnac.exit_json()


if __name__ == "__main__":
    main()
