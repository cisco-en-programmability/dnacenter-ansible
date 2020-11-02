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
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.application_set import module_definition, ApplicationSetExistenceCriteria



def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()
    
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
        required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "query":
        dnac.exec("get")
        
    elif state == "absent":
        dnac.exec("delete")

    elif state == "present":
        
        ec = ApplicationSetExistenceCriteria(dnac)

        if ec.object_exists():
            dnac.fail_json(ec.ERR_OBJECT_EXISTS)
            
        else:
            dnac.exec("post")

    else:
        dnac.fail_json("Unsupported state '{}'". format(state))

    dnac.exit_json()


if __name__ == "__main__":
    main()

