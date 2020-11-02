import json

module_definition = json.loads('''{
    "family": "site_design",
    "name": "nfv_profile",
    "operations": {
        "delete": [
            "delete_nfv_profile"
        ],
        "get": [
            "get_nfv_profile"
        ],
        "post": [
            "create_nfv_profile"
        ],
        "put": [
            "update_nfv_profile"
        ]
    },
    "parameters": {
        "create_nfv_profile": [
            {
                "array_type": "object",
                "name": "device",
                "required": true,
                "schema": [
                    {
                        "name": "deviceType",
                        "required": true,
                        "type": "string"
                    },
                    {
                        "name": "deviceTag",
                        "required": true,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "serviceProviderProfile",
                        "required": true,
                        "schema": [
                            {
                                "name": "serviceProvider",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "linkType",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "connect",
                                "required": true,
                                "type": "boolean"
                            },
                            {
                                "name": "connectDefaultGatewayOnWan",
                                "required": true,
                                "type": "boolean"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "directInternetAccessForFirewall",
                        "required": true,
                        "type": "boolean"
                    },
                    {
                        "array_type": "object",
                        "name": "services",
                        "required": true,
                        "schema": [
                            {
                                "name": "serviceType",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "profileType",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "serviceName",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "imageName",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "array_type": "object",
                                "name": "vNicMapping",
                                "required": true,
                                "schema": [
                                    {
                                        "name": "networkType",
                                        "required": true,
                                        "type": "string"
                                    },
                                    {
                                        "name": "assignIpAddressToNetwork",
                                        "required": false,
                                        "type": "string"
                                    }
                                ],
                                "type": "array"
                            },
                            {
                                "name": "firewallMode",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "array_type": "object",
                        "name": "customNetworks",
                        "required": false,
                        "schema": [
                            {
                                "name": "networkName",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "array_type": "object",
                                "name": "servicesToConnect",
                                "required": true,
                                "schema": [
                                    {
                                        "name": "serviceName",
                                        "required": true,
                                        "type": "string"
                                    }
                                ],
                                "type": "array"
                            },
                            {
                                "name": "connectionType",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "vlanMode",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "vlanId",
                                "required": true,
                                "type": "number"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "array_type": "object",
                        "name": "vlanForL2",
                        "required": false,
                        "schema": [
                            {
                                "name": "vlanType",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "vlanId",
                                "required": true,
                                "type": "number"
                            },
                            {
                                "name": "vlanDescription",
                                "required": true,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "array_type": "object",
                        "name": "customTemplate",
                        "required": false,
                        "schema": [
                            {
                                "name": "deviceType",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "template",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "templateType",
                                "required": true,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    }
                ],
                "type": "array"
            },
            {
                "name": "profileName",
                "required": true,
                "type": "string"
            }
        ],
        "delete_nfv_profile": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            },
            {
                "name": "name",
                "required": false,
                "type": "string"
            }
        ],
        "get_nfv_profile": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            },
            {
                "name": "limit",
                "required": false,
                "type": "string"
            },
            {
                "name": "name",
                "required": false,
                "type": "string"
            },
            {
                "name": "offset",
                "required": false,
                "type": "string"
            }
        ],
        "update_nfv_profile": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            },
            {
                "array_type": "object",
                "name": "device",
                "required": true,
                "schema": [
                    {
                        "name": "deviceTag",
                        "required": true,
                        "type": "string"
                    },
                    {
                        "name": "directInternetAccessForFirewall",
                        "required": true,
                        "type": "boolean"
                    },
                    {
                        "array_type": "object",
                        "name": "services",
                        "required": false,
                        "schema": [
                            {
                                "name": "serviceType",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "profileType",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "serviceName",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "imageName",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "array_type": "object",
                                "name": "vNicMapping",
                                "required": true,
                                "schema": [
                                    {
                                        "name": "networkType",
                                        "required": true,
                                        "type": "string"
                                    },
                                    {
                                        "name": "assignIpAddressToNetwork",
                                        "required": false,
                                        "type": "string"
                                    }
                                ],
                                "type": "array"
                            },
                            {
                                "name": "firewallMode",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "array_type": "object",
                        "name": "customNetworks",
                        "required": false,
                        "schema": [
                            {
                                "name": "networkName",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "array_type": "object",
                                "name": "servicesToConnect",
                                "required": true,
                                "schema": [
                                    {
                                        "name": "serviceName",
                                        "required": true,
                                        "type": "string"
                                    }
                                ],
                                "type": "array"
                            },
                            {
                                "name": "connectionType",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "vlanMode",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "vlanId",
                                "required": true,
                                "type": "number"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "array_type": "object",
                        "name": "vlanForL2",
                        "required": false,
                        "schema": [
                            {
                                "name": "vlanType",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "vlanId",
                                "required": true,
                                "type": "number"
                            },
                            {
                                "name": "vlanDescription",
                                "required": true,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "array_type": "object",
                        "name": "customTemplate",
                        "required": false,
                        "schema": [
                            {
                                "name": "deviceType",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "template",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "templateType",
                                "required": true,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "currentDeviceTag",
                        "required": true,
                        "type": "string"
                    }
                ],
                "type": "array"
            },
            {
                "name": "name",
                "required": false,
                "type": "string"
            }
        ]
    },
    "responses": {
        "create_nfv_profile": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        },
        "delete_nfv_profile": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        },
        "get_nfv_profile": {
            "properties": [
                "response"
            ],
            "type": "object"
        },
        "update_nfv_profile": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        }
    }
}''')