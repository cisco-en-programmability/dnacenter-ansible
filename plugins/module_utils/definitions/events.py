import json

module_definition = json.loads(
    """{
    "family": "event_management",
    "name": "events",
    "operations": {
        "get": [
            "get_events",
            "count_of_events"
        ]
    },
    "parameters": {
        "count_of_events": [
            {
                "name": "tags",
                "required": true,
                "type": "string"
            },
            {
                "name": "event_id",
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
        "get_events": [
            {
                "name": "tags",
                "required": true,
                "type": "string"
            },
            {
                "name": "event_id",
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
                "name": "sort_by",
                "required": false,
                "type": "string"
            }
        ]
    },
    "responses": {
        "count_of_events": {
            "properties": [
                "response"
            ],
            "type": "object"
        },
        "get_events": {
            "array_type": "object",
            "properties": [
                "eventId",
                "nameSpace",
                "name",
                "description",
                "version",
                "category",
                "domain",
                "subDomain",
                "type",
                "tags",
                "severity",
                "details",
                "subscriptionTypes"
            ],
            "type": "array"
        }
    }
}"""
)
