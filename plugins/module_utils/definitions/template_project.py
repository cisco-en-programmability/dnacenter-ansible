import json

module_definition = json.loads(
    """{
    "family": "configuration_templates",
    "name": "template_project",
    "operations": {
        "delete": [
            "delete_project"
        ],
        "get": [
            "get_projects"
        ],
        "post": [
            "create_project"
        ],
        "put": [
            "update_project"
        ]
    },
    "parameters": {
        "create_project": [
            {
                "name": "createTime",
                "type": "integer"
            },
            {
                "name": "description",
                "type": "string"
            },
            {
                "name": "id",
                "type": "string"
            },
            {
                "name": "lastUpdateTime",
                "type": "integer"
            },
            {
                "name": "name",
                "type": "string"
            },
            {
                "array_type": "string",
                "name": "tags",
                "required": false,
                "schema": [],
                "type": "array"
            },
            {
                "name": "templates",
                "type": "any"
            }
        ],
        "delete_project": [
            {
                "name": "project_id",
                "required": true,
                "type": "string"
            }
        ],
        "get_projects": [
            {
                "name": "name",
                "required": false,
                "type": "string"
            }
        ],
        "update_project": [
            {
                "name": "createTime",
                "type": "integer"
            },
            {
                "name": "description",
                "type": "string"
            },
            {
                "name": "id",
                "type": "string"
            },
            {
                "name": "lastUpdateTime",
                "type": "integer"
            },
            {
                "name": "name",
                "type": "string"
            },
            {
                "array_type": "string",
                "name": "tags",
                "required": false,
                "schema": [],
                "type": "array"
            },
            {
                "name": "templates",
                "type": "any"
            }
        ]
    },
    "responses": {
        "create_project": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "delete_project": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_projects": {
            "array_type": "object",
            "properties": [
                "name",
                "id",
                "templates"
            ],
            "type": "array"
        },
        "update_project": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
