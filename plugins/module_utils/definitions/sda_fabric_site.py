import json

module_definition = json.loads(
    """{
    "family": "sda",
    "name": "sda_fabric_site",
    "operations": {
        "delete": [
            "delete_site"
        ],
        "get": [
            "get_site"
        ],
        "post": [
            "add_site"
        ]
    },
    "parameters": {
        "add_site": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "fabricName",
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
        "delete_site": [
            {
                "name": "site_name_hierarchy",
                "required": true,
                "type": "string"
            }
        ],
        "get_site": [
            {
                "name": "site_name_hierarchy",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "add_site": {
            "properties": [
                "status",
                "description",
                "executionStatusUrl"
            ],
            "type": "object"
        },
        "delete_site": {
            "properties": [
                "status",
                "description",
                "executionStatusUrl"
            ],
            "type": "object"
        },
        "get_site": {
            "properties": [
                "status",
                "description",
                "executionStatusUrl"
            ],
            "type": "object"
        }
    }
}"""
)
