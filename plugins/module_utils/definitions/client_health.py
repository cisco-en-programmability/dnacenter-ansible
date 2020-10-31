import json

module_definition = json.loads('''{
    "family": "clients",
    "name": "client_health",
    "operations": {
        "get": [
            "get_overall_client_health"
        ]
    },
    "parameters": {
        "get_overall_client_health": [
            {
                "name": "timestamp",
                "required": false,
                "type": "integer"
            }
        ]
    },
    "responses": {
        "get_overall_client_health": {
            "properties": [
                "response"
            ],
            "type": "object"
        }
    }
}''')