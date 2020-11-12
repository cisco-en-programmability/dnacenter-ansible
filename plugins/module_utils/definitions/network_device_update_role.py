import json

module_definition = json.loads(
    """{
    "family": "devices",
    "name": "network_device_update_role",
    "operations": {
        "put": [
            "update_device_role"
        ]
    },
    "parameters": {
        "update_device_role": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            },
            {
                "name": "role",
                "required": true,
                "type": "string"
            },
            {
                "name": "roleSource",
                "required": true,
                "type": "string"
            },
            {
                "artificial": true,
                "name": "summary",
                "required": true,
                "type": "boolean"
            }
        ]
    },
    "responses": {
        "update_device_role": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
