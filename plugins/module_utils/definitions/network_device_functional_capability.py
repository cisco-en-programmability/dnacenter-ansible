import json

module_definition = json.loads('''{
    "family": "devices",
    "name": "network_device_functional_capability",
    "operations": {
        "get": [
            "get_functional_capability_for_devices",
            "get_functional_capability_by_id"
        ]
    },
    "parameters": {
        "get_functional_capability_by_id": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            }
        ],
        "get_functional_capability_for_devices": [
            {
                "name": "device_id",
                "required": true,
                "type": "string"
            },
            {
                "name": "function_name",
                "required": false,
                "type": "string"
            }
        ]
    },
    "responses": {
        "get_functional_capability_by_id": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_functional_capability_for_devices": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}''')