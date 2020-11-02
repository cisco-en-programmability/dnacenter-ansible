import json

module_definition = json.loads('''{
    "family": "path_trace",
    "name": "flow_analysis",
    "operations": {
        "delete": [
            "deletes_pathtrace_by_id"
        ],
        "get": [
            "retrives_all_previous_pathtraces_summary",
            "retrieves_previous_pathtrace"
        ],
        "post": [
            "initiate_a_new_pathtrace"
        ]
    },
    "parameters": {
        "deletes_pathtrace_by_id": [
            {
                "name": "flow_analysis_id",
                "required": true,
                "type": "string"
            }
        ],
        "initiate_a_new_pathtrace": [
            {
                "name": "controlPath",
                "type": "boolean"
            },
            {
                "name": "destIP",
                "required": true,
                "type": "string"
            },
            {
                "name": "destPort",
                "type": "string"
            },
            {
                "array_type": "string",
                "name": "inclusions",
                "required": false,
                "schema": [],
                "type": "array"
            },
            {
                "name": "periodicRefresh",
                "type": "boolean"
            },
            {
                "name": "protocol",
                "type": "string"
            },
            {
                "name": "sourceIP",
                "required": true,
                "type": "string"
            },
            {
                "name": "sourcePort",
                "type": "string"
            }
        ],
        "retrieves_previous_pathtrace": [
            {
                "name": "flow_analysis_id",
                "required": true,
                "type": "string"
            }
        ],
        "retrives_all_previous_pathtraces_summary": [
            {
                "name": "dest_ip",
                "required": false,
                "type": "string"
            },
            {
                "name": "dest_port",
                "required": false,
                "type": "string"
            },
            {
                "name": "gt_create_time",
                "required": false,
                "type": "string"
            },
            {
                "name": "last_update_time",
                "required": false,
                "type": "string"
            },
            {
                "name": "limit",
                "required": false,
                "type": "string"
            },
            {
                "name": "lt_create_time",
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
                "name": "periodic_refresh",
                "required": false,
                "type": "boolean"
            },
            {
                "name": "protocol",
                "required": false,
                "type": "string"
            },
            {
                "name": "sort_by",
                "required": false,
                "type": "string"
            },
            {
                "name": "source_ip",
                "required": false,
                "type": "string"
            },
            {
                "name": "source_port",
                "required": false,
                "type": "string"
            },
            {
                "name": "status",
                "required": false,
                "type": "string"
            },
            {
                "name": "task_id",
                "required": false,
                "type": "string"
            }
        ]
    },
    "responses": {
        "deletes_pathtrace_by_id": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "initiate_a_new_pathtrace": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "retrieves_previous_pathtrace": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "retrives_all_previous_pathtraces_summary": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}''')