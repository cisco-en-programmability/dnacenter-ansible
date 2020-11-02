import json

module_definition = json.loads('''{
    "family": "network_settings",
    "name": "global_pool",
    "operations": {
        "delete": [
            "delete_global_ip_pool"
        ],
        "get": [
            "get_global_pool"
        ],
        "post": [
            "create_global_pool"
        ],
        "put": [
            "update_global_pool"
        ]
    },
    "parameters": {
        "create_global_pool": [
            {
                "name": "settings",
                "required": true,
                "schema": [
                    {
                        "array_type": "object",
                        "name": "ippool",
                        "required": false,
                        "schema": [
                            {
                                "name": "ipPoolName",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "type",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "ipPoolCidr",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "gateway",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "array_type": "string",
                                "name": "dhcpServerIps",
                                "required": false,
                                "schema": [],
                                "type": "array"
                            },
                            {
                                "array_type": "string",
                                "name": "dnsServerIps",
                                "required": false,
                                "schema": [],
                                "type": "array"
                            },
                            {
                                "name": "IpAddressSpace",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    }
                ],
                "type": "object"
            }
        ],
        "delete_global_ip_pool": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            }
        ],
        "get_global_pool": [
            {
                "name": "limit",
                "required": false,
                "type": "string"
            },
            {
                "name": "offset",
                "required": false,
                "type": "string"
            }
        ],
        "update_global_pool": [
            {
                "name": "settings",
                "required": true,
                "schema": [
                    {
                        "array_type": "object",
                        "name": "ippool",
                        "required": false,
                        "schema": [
                            {
                                "name": "ipPoolName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "gateway",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "array_type": "string",
                                "name": "dhcpServerIps",
                                "required": false,
                                "schema": [],
                                "type": "array"
                            },
                            {
                                "array_type": "string",
                                "name": "dnsServerIps",
                                "required": false,
                                "schema": [],
                                "type": "array"
                            },
                            {
                                "name": "id",
                                "required": true,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    }
                ],
                "type": "object"
            }
        ]
    },
    "responses": {
        "create_global_pool": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        },
        "delete_global_ip_pool": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        },
        "get_global_pool": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "update_global_pool": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        }
    }
}''')