#!/usr/bin/env python

ANSIBLE_METADATA = {
    'metadata_version': '0.0.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''s
---
'''

EXAMPLES = r'''
---
'''

RETURN = r'''
---
#
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec



def main():

    moddef = ModuleDefinition("network_device")

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()
    
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
        required_if=required_if
    )

    dnac = DNACModule(module)

    state = module.params.get("state")
    family = moddef.family




    if state == "query":
        function, status = moddef.get_function("get", module.params)
        if function:
            dnac.exec(function, family)
        else:
            dnac.fail_json(msg=status.get("msg"))

    elif state == "absent":
        function, status = moddef.get_function("delete", module.params)

    elif state == "present":
        # check whether the object exists or not
        # and decide between put and post
        function, status = moddef.get_function("post", module.params)

    dnac.exit_json()


if __name__ == "__main__":
    main()

