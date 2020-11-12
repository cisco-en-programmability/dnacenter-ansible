import json

module_definition = json.loads(
    """{
    "family": "event_management",
    "name": "event_series",
    "operations": {
        "get": [
            "get_notifications",
            "count_of_notifications"
        ]
    },
    "parameters": {
        "count_of_notifications": [
            {
                "name": "category",
                "required": false,
                "type": "string"
            },
            {
                "name": "domain",
                "required": false,
                "type": "string"
            },
            {
                "name": "end_time",
                "required": false,
                "type": "string"
            },
            {
                "name": "event_ids",
                "required": false,
                "type": "string"
            },
            {
                "name": "severity",
                "required": false,
                "type": "string"
            },
            {
                "name": "source",
                "required": false,
                "type": "string"
            },
            {
                "name": "start_time",
                "required": false,
                "type": "string"
            },
            {
                "name": "sub_domain",
                "required": false,
                "type": "string"
            },
            {
                "name": "type",
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
        "get_notifications": [
            {
                "name": "category",
                "required": false,
                "type": "string"
            },
            {
                "name": "domain",
                "required": false,
                "type": "string"
            },
            {
                "name": "end_time",
                "required": false,
                "type": "string"
            },
            {
                "name": "event_ids",
                "required": false,
                "type": "string"
            },
            {
                "name": "limit",
                "required": false,
                "type": "number"
            },
            {
                "name": "offset",
                "required": false,
                "type": "number"
            },
            {
                "name": "order",
                "required": false,
                "type": "string"
            },
            {
                "name": "severity",
                "required": false,
                "type": "string"
            },
            {
                "name": "sort_by",
                "required": false,
                "type": "string"
            },
            {
                "name": "source",
                "required": false,
                "type": "string"
            },
            {
                "name": "start_time",
                "required": false,
                "type": "string"
            },
            {
                "name": "sub_domain",
                "required": false,
                "type": "string"
            },
            {
                "name": "type",
                "required": false,
                "type": "string"
            }
        ]
    },
    "responses": {
        "count_of_notifications": {
            "properties": [
                "response"
            ],
            "type": "object"
        },
        "get_notifications": {
            "properties": [
                "instanceId",
                "eventId",
                "name",
                "namespace",
                "description",
                "type",
                "category",
                "severity",
                "timestamp",
                "domain",
                "subDomain",
                "source",
                "context",
                "details",
                "tenantId"
            ],
            "type": "object"
        }
    }
}"""
)
