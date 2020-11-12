import json

module_definition = json.loads(
    """{
    "family": "command_runner",
    "name": "network_device_poller_legit_reads",
    "operations": {
        "get": [
            "get_all_keywords_of_clis_accepted"
        ]
    },
    "parameters": {
        "get_all_keywords_of_clis_accepted": []
    },
    "responses": {
        "get_all_keywords_of_clis_accepted": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
