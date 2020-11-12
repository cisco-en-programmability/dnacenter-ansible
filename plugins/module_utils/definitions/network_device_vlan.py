import json

module_definition = json.loads(
    """{
    "family": "devices",
    "name": "network_device_vlan",
    "operations": {
        "get": [
            "get_device_interface_vlans"
        ]
    },
    "parameters": {
        "get_device_interface_vlans": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            },
            {
                "name": "interface_type",
                "required": false,
                "type": "string"
            }
        ]
    },
    "responses": {
        "get_device_interface_vlans": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
