import json

module_definition = json.loads(
    """{
    "family": "sda",
    "name": "sda_host_onboarding_user_device",
    "operations": {
        "delete": [
            "delete_port_assignment_for_user_device"
        ],
        "get": [
            "get_port_assignment_for_user_device"
        ],
        "post": [
            "add_port_assignment_for_user_device"
        ]
    },
    "parameters": {
        "add_port_assignment_for_user_device": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "siteNameHierarchy",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "deviceManagementIpAddress",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "interfaceName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "dataIpAddressPoolName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "voiceIpAddressPoolName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "authenticateTemplateName",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "array"
            }
        ],
        "delete_port_assignment_for_user_device": [
            {
                "name": "device_ip",
                "required": true,
                "type": "string"
            },
            {
                "name": "interface_name",
                "required": true,
                "type": "string"
            }
        ],
        "get_port_assignment_for_user_device": [
            {
                "name": "device_ip",
                "required": true,
                "type": "string"
            },
            {
                "name": "interface_name",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "add_port_assignment_for_user_device": {
            "properties": [
                "status",
                "description",
                "executionStatusUrl"
            ],
            "type": "object"
        },
        "delete_port_assignment_for_user_device": {
            "properties": [
                "status",
                "description",
                "executionStatusUrl"
            ],
            "type": "object"
        },
        "get_port_assignment_for_user_device": {
            "properties": [
                "status",
                "description",
                "siteNameHierarchy",
                "deviceManagementIpAddress",
                "interfaceName",
                "dataIpAddressPoolName",
                "voiceIpAddressPoolName",
                "scalableGroupName",
                "authenticateTemplateName"
            ],
            "type": "object"
        }
    }
}"""
)
