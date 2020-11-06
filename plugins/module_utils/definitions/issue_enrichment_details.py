import json

module_definition = json.loads('''{
    "family": "issues",
    "name": "issue_enrichment_details",
    "operations": {
        "get": [
            "get_issue_enrichment_details"
        ]
    },
    "parameters": {
        "get_issue_enrichment_details": [
            {
                "artificial": true,
                "name": "headers",
                "required": true,
                "schema": [],
                "type": "object"
            }
        ]
    },
    "responses": {
        "get_issue_enrichment_details": {
            "properties": [
                "issueDetails"
            ],
            "type": "object"
        }
    }
}''')