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
    argument_spec = dnac_argument_spec()
    moddef = ModuleDefinition("network_device")
    argument_spec.update(moddef.get_argument_spec_dict())
    
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False
    )


    result = dict(
        changed=False,
        original_message='',
        message='')


    dnac = DNACModule(module)

    state = module.params["state"]
    family = moddef.family

    


    if state == "absent":
        function, message = moddef.get_function("delete", module.params)
        res = dnac.exec(function, family) if function else None
    elif state == "query":
        function, message = moddef.get_function("get", module.params)
        res = dnac.exec(function, family) if function else None
        if res:
            result.update(res)
            module.exit_json(**result)
        else:
            module.fail_json(msg=message) # Make this message more specific
    elif state == "present":
        # check whether the object exists or not
        # and decide between put and post
        function = moddef.get_function("post", module.params)["function"]
        res = dnac.exec(function, family) if function else None
    

if __name__ == "__main__":
    main()

