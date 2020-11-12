import json

module_definition = json.loads(
    """{
    "family": "devices",
    "name": "network_device_wireless_info",
    "operations": {
        "get": [
            "get_wireless_lan_controller_details_by_id"
        ]
    },
    "parameters": {
        "get_wireless_lan_controller_details_by_id": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "get_wireless_lan_controller_details_by_id": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
