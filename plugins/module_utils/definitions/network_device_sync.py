import json

module_definition = json.loads('''{
    "family": "devices",
    "name": "network_device_sync",
    "operations": {
        "put": [
            "sync_devices_using_forcesync"
        ]
    },
    "parameters": {
        "sync_devices_using_forcesync": [
            {
                "name": "force_sync",
                "required": false,
                "type": "boolean"
            },
            {
                "array_type": "any",
                "name": "payload",
                "required": true,
                "schema": [],
                "type": "array"
            }
        ]
    },
    "responses": {
        "sync_devices_using_forcesync": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}''')