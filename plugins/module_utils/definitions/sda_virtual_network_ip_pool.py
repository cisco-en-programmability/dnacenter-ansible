import json

module_definition = json.loads(
    """{
    "family": "sda",
    "name": "sda_virtual_network_ip_pool",
    "operations": {
        "delete": [
            "delete_ip_pool_from_sda_virtual_network"
        ],
        "get": [
            "get_ip_pool_from_sda_virtual_network"
        ],
        "post": [
            "add_ip_pool_in_sda_virtual_network"
        ]
    },
    "parameters": {
        "add_ip_pool_in_sda_virtual_network": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "virtualNetworkName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "ipPoolName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "trafficType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "authenticationPolicyName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "scalableGroupName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "isL2FloodingEnabled",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "isThisCriticalPool",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "poolType",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "array"
            }
        ],
        "delete_ip_pool_from_sda_virtual_network": [
            {
                "name": "ip_pool_name",
                "required": true,
                "type": "string"
            },
            {
                "name": "virtual_network_name",
                "required": true,
                "type": "string"
            }
        ],
        "get_ip_pool_from_sda_virtual_network": [
            {
                "name": "ip_pool_name",
                "required": true,
                "type": "string"
            },
            {
                "name": "virtual_network_name",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "add_ip_pool_in_sda_virtual_network": {
            "properties": [
                "status",
                "description",
                "executionStatusUrl"
            ],
            "type": "object"
        },
        "delete_ip_pool_from_sda_virtual_network": {
            "properties": [
                "status",
                "description",
                "executionStatusUrl"
            ],
            "type": "object"
        },
        "get_ip_pool_from_sda_virtual_network": {
            "properties": [
                "status",
                "description",
                "virtualNetworkName",
                "ipPoolName",
                "authenticationPolicyName",
                "trafficType",
                "scalableGroupName",
                "isL2FloodingEnabled",
                "isThisCriticalPool"
            ],
            "type": "object"
        }
    }
}"""
)
