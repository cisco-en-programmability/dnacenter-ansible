import json

module_definition = json.loads('''{
    "family": "devices",
    "name": "network_device_meraki_org",
    "operations": {
        "get": [
            "get_organization_list_for_meraki"
        ]
    },
    "parameters": {
        "get_organization_list_for_meraki": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "get_organization_list_for_meraki": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}''')