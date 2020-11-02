import json

module_definition = json.loads('''{
    "family": "sda",
    "name": "sda_virtual_network",
    "operations": {
        "delete": [
            "delete_vn"
        ],
        "get": [
            "get_vn"
        ],
        "post": [
            "add_vn"
        ]
    },
    "parameters": {
        "add_vn": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "virtualNetworkName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "siteNameHierarchy",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "array"
            }
        ],
        "delete_vn": [
            {
                "name": "site_name_hierarchy",
                "required": true,
                "type": "string"
            },
            {
                "name": "virtual_network_name",
                "required": true,
                "type": "string"
            }
        ],
        "get_vn": [
            {
                "name": "site_name_hierarchy",
                "required": true,
                "type": "string"
            },
            {
                "name": "virtual_network_name",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "add_vn": {
            "properties": [
                "status",
                "description",
                "name",
                "roles",
                "deviceManagementIpAddress",
                "siteHierarchy"
            ],
            "type": "object"
        },
        "delete_vn": {
            "properties": [
                "status",
                "description",
                "name",
                "roles",
                "deviceManagementIpAddress",
                "siteHierarchy"
            ],
            "type": "object"
        },
        "get_vn": {
            "properties": [
                "status",
                "description",
                "name",
                "roles",
                "deviceManagementIpAddress",
                "siteHierarchy"
            ],
            "type": "object"
        }
    }
}''')