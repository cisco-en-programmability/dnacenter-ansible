import json

module_definition = json.loads('''{
    "family": "application_policy",
    "name": "application_set",
    "operations": {
        "delete": [
            "delete_application_set"
        ],
        "get": [
            "get_application_sets",
            "get_application_sets_count"
        ],
        "post": [
            "create_application_set"
        ]
    },
    "parameters": {
        "create_application_set": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "name",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "array"
            }
        ],
        "delete_application_set": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            }
        ],
        "get_application_sets": [
            {
                "name": "limit",
                "required": false,
                "type": "number"
            },
            {
                "name": "name",
                "required": false,
                "type": "string"
            },
            {
                "name": "offset",
                "required": false,
                "type": "number"
            }
        ],
        "get_application_sets_count": [
            {
                "artificial": true,
                "name": "count",
                "required": true,
                "type": "boolean"
            }
        ]
    },
    "responses": {
        "create_application_set": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "delete_application_set": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_application_sets": {
            "properties": [
                "response"
            ],
            "type": "object"
        },
        "get_application_sets_count": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}''')