import json

module_definition = json.loads('''{
    "family": "sda",
    "name": "sda_device",
    "operations": {
        "get": [
            "get_device_info"
        ]
    },
    "parameters": {
        "get_device_info": [
            {
                "name": "device_ipaddress",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "get_device_info": {
            "properties": [
                "status",
                "description",
                "name",
                "roles",
                "deviceManagementIpAddress",
                "siteHierarchy"
            ],
            "type": "object"
        }
    }
}''')