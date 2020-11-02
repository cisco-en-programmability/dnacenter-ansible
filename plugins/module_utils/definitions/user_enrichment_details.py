import json

module_definition = json.loads('''{
    "family": "users",
    "name": "user_enrichment_details",
    "operations": {
        "get": [
            "get_user_enrichment_details"
        ]
    },
    "parameters": {
        "get_user_enrichment_details": [
            {
                "name": "headers",
                "required": true,
                "schema": [],
                "type": "object"
            }
        ]
    },
    "responses": {
        "get_user_enrichment_details": {
            "array_type": "object",
            "properties": [
                "userDetails",
                "connectedDevice"
            ],
            "type": "array"
        }
    }
}''')