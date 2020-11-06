import json

module_definition = json.loads('''{
    "family": "task",
    "name": "task",
    "operations": {
        "get": [
            "get_tasks",
            "get_task_by_id",
            "get_task_count",
            "get_task_by_operationid",
            "get_task_tree"
        ]
    },
    "parameters": {
        "get_task_by_id": [
            {
                "name": "task_id",
                "required": true,
                "type": "string"
            }
        ],
        "get_task_by_operationid": [
            {
                "name": "limit",
                "required": true,
                "type": "integer"
            },
            {
                "name": "offset",
                "required": true,
                "type": "integer"
            },
            {
                "name": "operation_id",
                "required": true,
                "type": "string"
            }
        ],
        "get_task_count": [
            {
                "name": "data",
                "required": false,
                "type": "string"
            },
            {
                "name": "end_time",
                "required": false,
                "type": "string"
            },
            {
                "name": "error_code",
                "required": false,
                "type": "string"
            },
            {
                "name": "failure_reason",
                "required": false,
                "type": "string"
            },
            {
                "name": "is_error",
                "required": false,
                "type": "string"
            },
            {
                "name": "parent_id",
                "required": false,
                "type": "string"
            },
            {
                "name": "progress",
                "required": false,
                "type": "string"
            },
            {
                "name": "service_type",
                "required": false,
                "type": "string"
            },
            {
                "name": "start_time",
                "required": false,
                "type": "string"
            },
            {
                "name": "username",
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
        "get_task_tree": [
            {
                "name": "task_id",
                "required": true,
                "type": "string"
            },
            {
                "artificial": true,
                "name": "tree",
                "required": true,
                "type": "boolean"
            }
        ],
        "get_tasks": [
            {
                "name": "data",
                "required": false,
                "type": "string"
            },
            {
                "name": "end_time",
                "required": false,
                "type": "string"
            },
            {
                "name": "error_code",
                "required": false,
                "type": "string"
            },
            {
                "name": "failure_reason",
                "required": false,
                "type": "string"
            },
            {
                "name": "is_error",
                "required": false,
                "type": "string"
            },
            {
                "name": "limit",
                "required": false,
                "type": "string"
            },
            {
                "name": "offset",
                "required": false,
                "type": "string"
            },
            {
                "name": "order",
                "required": false,
                "type": "string"
            },
            {
                "name": "parent_id",
                "required": false,
                "type": "string"
            },
            {
                "name": "progress",
                "required": false,
                "type": "string"
            },
            {
                "name": "service_type",
                "required": false,
                "type": "string"
            },
            {
                "name": "sort_by",
                "required": false,
                "type": "string"
            },
            {
                "name": "start_time",
                "required": false,
                "type": "string"
            },
            {
                "name": "username",
                "required": false,
                "type": "string"
            }
        ]
    },
    "responses": {
        "get_task_by_id": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_task_by_operationid": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_task_count": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_task_tree": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_tasks": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}''')