import json

module_definition = json.loads(
    """{
    "family": "devices",
    "name": "network_device_module",
    "operations": {
        "get": [
            "get_modules",
            "get_module_info_by_id",
            "get_module_count"
        ]
    },
    "parameters": {
        "get_module_count": [
            {
                "name": "device_id",
                "required": true,
                "type": "string"
            },
            {
                "name": "name_list",
                "required": false,
                "type": "string"
            },
            {
                "name": "operational_state_code_list",
                "required": false,
                "type": "string"
            },
            {
                "name": "part_number_list",
                "required": false,
                "type": "string"
            },
            {
                "name": "vendor_equipment_type_list",
                "required": false,
                "type": "string"
            },
            {
                "artificial": true,
                "name": "count",
                "required": true,
                "type": "boolean"
            }
        ],
        "get_module_info_by_id": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            }
        ],
        "get_modules": [
            {
                "name": "device_id",
                "required": true,
                "type": "string"
            },
            {
                "name": "limit",
                "required": false,
                "type": "string"
            },
            {
                "name": "name_list",
                "required": false,
                "type": "string"
            },
            {
                "name": "offset",
                "required": false,
                "type": "string"
            },
            {
                "name": "operational_state_code_list",
                "required": false,
                "type": "string"
            },
            {
                "name": "part_number_list",
                "required": false,
                "type": "string"
            },
            {
                "name": "vendor_equipment_type_list",
                "required": false,
                "type": "string"
            }
        ]
    },
    "responses": {
        "get_module_count": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_module_info_by_id": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_modules": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
