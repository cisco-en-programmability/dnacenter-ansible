import json

module_definition = json.loads('''{
    "family": "itsm",
    "name": "integration_event",
    "operations": {
        "get": [
            "get_failed_itsm_events"
        ],
        "post": [
            "retry_integration_events"
        ]
    },
    "parameters": {
        "get_failed_itsm_events": [
            {
                "name": "instance_id",
                "required": false,
                "type": "string"
            }
        ],
        "retry_integration_events": [
            {
                "array_type": "string",
                "name": "payload",
                "required": true,
                "schema": [],
                "type": "array"
            }
        ]
    },
    "responses": {
        "get_failed_itsm_events": {
            "array_type": "object",
            "properties": [
                "instanceId",
                "eventId",
                "name",
                "type",
                "category",
                "domain",
                "subDomain",
                "severity",
                "source",
                "timestamp",
                "enrichmentInfo",
                "description"
            ],
            "type": "array"
        },
        "retry_integration_events": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        }
    }
}''')