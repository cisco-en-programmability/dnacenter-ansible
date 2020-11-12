import json

module_definition = json.loads(
    """{
    "family": "devices",
    "name": "device_detail",
    "operations": {
        "get": [
            "get_device_detail"
        ]
    },
    "parameters": {
        "get_device_detail": [
            {
                "name": "identifier",
                "required": true,
                "type": "string"
            },
            {
                "name": "search_by",
                "required": true,
                "type": "string"
            },
            {
                "name": "timestamp",
                "required": false,
                "type": "integer"
            }
        ]
    },
    "responses": {
        "get_device_detail": {
            "properties": [
                "response"
            ],
            "type": "object"
        }
    }
}"""
)
