import json

module_definition = json.loads(
    """{
    "family": "site_design",
    "name": "nfv_provision",
    "operations": {
        "get": [
            "get_device_details_by_ip"
        ],
        "post": [
            "provision_nfv"
        ]
    },
    "parameters": {
        "get_device_details_by_ip": [
            {
                "name": "device_ip",
                "required": true,
                "type": "string"
            }
        ],
        "provision_nfv": [
            {
                "array_type": "object",
                "name": "provisioning",
                "required": true,
                "schema": [
                    {
                        "name": "site",
                        "required": true,
                        "schema": [
                            {
                                "name": "siteProfileName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "area",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "name",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "parentName",
                                        "required": false,
                                        "type": "string"
                                    }
                                ],
                                "type": "object"
                            },
                            {
                                "name": "building",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "name",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "address",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "latitude",
                                        "required": false,
                                        "type": "number"
                                    },
                                    {
                                        "name": "longitude",
                                        "required": false,
                                        "type": "number"
                                    },
                                    {
                                        "name": "parentName",
                                        "required": false,
                                        "type": "string"
                                    }
                                ],
                                "type": "object"
                            },
                            {
                                "name": "floor",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "name",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "parentName",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "rfModel",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "width",
                                        "required": false,
                                        "type": "number"
                                    },
                                    {
                                        "name": "length",
                                        "required": false,
                                        "type": "number"
                                    },
                                    {
                                        "name": "height",
                                        "required": false,
                                        "type": "number"
                                    }
                                ],
                                "type": "object"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "array_type": "object",
                        "name": "device",
                        "required": true,
                        "schema": [
                            {
                                "name": "ip",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "deviceSerialNumber",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "tagName",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "array_type": "object",
                                "name": "serviceProviders",
                                "required": true,
                                "schema": [
                                    {
                                        "name": "serviceProvider",
                                        "required": true,
                                        "type": "string"
                                    },
                                    {
                                        "name": "wanInterface",
                                        "required": false,
                                        "schema": [
                                            {
                                                "name": "ipAddress",
                                                "required": false,
                                                "type": "string"
                                            },
                                            {
                                                "name": "interfaceName",
                                                "required": false,
                                                "type": "string"
                                            },
                                            {
                                                "name": "subnetmask",
                                                "required": false,
                                                "type": "string"
                                            },
                                            {
                                                "name": "bandwidth",
                                                "required": false,
                                                "type": "string"
                                            },
                                            {
                                                "name": "gateway",
                                                "required": false,
                                                "type": "string"
                                            }
                                        ],
                                        "type": "object"
                                    }
                                ],
                                "type": "array"
                            },
                            {
                                "array_type": "object",
                                "name": "services",
                                "required": true,
                                "schema": [
                                    {
                                        "name": "type",
                                        "required": true,
                                        "type": "string"
                                    },
                                    {
                                        "name": "mode",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "systemIp",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "centralManagerIP",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "centralRegistrationKey",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "commonKey",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "adminPasswordHash",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "disk",
                                        "required": false,
                                        "type": "string"
                                    }
                                ],
                                "type": "array"
                            },
                            {
                                "array_type": "object",
                                "name": "vlan",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "type",
                                        "required": true,
                                        "type": "string"
                                    },
                                    {
                                        "name": "id",
                                        "required": true,
                                        "type": "string"
                                    },
                                    {
                                        "name": "interfaces",
                                        "required": true,
                                        "type": "string"
                                    },
                                    {
                                        "name": "network",
                                        "required": false,
                                        "type": "string"
                                    }
                                ],
                                "type": "array"
                            },
                            {
                                "array_type": "object",
                                "name": "subPools",
                                "required": true,
                                "schema": [
                                    {
                                        "name": "type",
                                        "required": true,
                                        "type": "string"
                                    },
                                    {
                                        "name": "name",
                                        "required": true,
                                        "type": "string"
                                    },
                                    {
                                        "name": "ipSubnet",
                                        "required": true,
                                        "type": "string"
                                    },
                                    {
                                        "name": "gateway",
                                        "required": true,
                                        "type": "string"
                                    },
                                    {
                                        "name": "parentPoolName",
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
                                        "name": "name",
                                        "required": true,
                                        "type": "string"
                                    },
                                    {
                                        "name": "port",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "ipAddressPool",
                                        "required": false,
                                        "type": "string"
                                    }
                                ],
                                "type": "array"
                            },
                            {
                                "name": "templateParam",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "nfvis",
                                        "required": false,
                                        "schema": [
                                            {
                                                "name": "var1",
                                                "required": false,
                                                "type": "string"
                                            }
                                        ],
                                        "type": "object"
                                    },
                                    {
                                        "name": "asav",
                                        "required": false,
                                        "schema": [
                                            {
                                                "name": "var1",
                                                "required": false,
                                                "type": "string"
                                            }
                                        ],
                                        "type": "object"
                                    }
                                ],
                                "type": "object"
                            }
                        ],
                        "type": "array"
                    }
                ],
                "type": "array"
            },
            {
                "array_type": "object",
                "name": "siteProfile",
                "required": true,
                "schema": [
                    {
                        "name": "siteProfileName",
                        "required": true,
                        "type": "string"
                    },
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
                                "name": "tagName",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "array_type": "object",
                                "name": "serviceProviders",
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
                                        "name": "defaultGateway",
                                        "required": true,
                                        "type": "boolean"
                                    }
                                ],
                                "type": "array"
                            },
                            {
                                "name": "dia",
                                "required": true,
                                "type": "boolean"
                            },
                            {
                                "array_type": "object",
                                "name": "services",
                                "required": true,
                                "schema": [
                                    {
                                        "name": "type",
                                        "required": true,
                                        "type": "string"
                                    },
                                    {
                                        "name": "profile",
                                        "required": true,
                                        "type": "string"
                                    },
                                    {
                                        "name": "mode",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "name",
                                        "required": true,
                                        "type": "string"
                                    },
                                    {
                                        "name": "imageName",
                                        "required": true,
                                        "type": "string"
                                    },
                                    {
                                        "name": "topology",
                                        "required": true,
                                        "schema": [
                                            {
                                                "name": "type",
                                                "required": false,
                                                "type": "string"
                                            },
                                            {
                                                "name": "name",
                                                "required": false,
                                                "type": "string"
                                            },
                                            {
                                                "name": "assignIp",
                                                "required": false,
                                                "type": "string"
                                            }
                                        ],
                                        "type": "object"
                                    }
                                ],
                                "type": "array"
                            },
                            {
                                "array_type": "object",
                                "name": "customServices",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "name",
                                        "required": true,
                                        "type": "string"
                                    },
                                    {
                                        "name": "applicationType",
                                        "required": true,
                                        "type": "string"
                                    },
                                    {
                                        "name": "profile",
                                        "required": true,
                                        "type": "string"
                                    },
                                    {
                                        "name": "topology",
                                        "required": true,
                                        "schema": [
                                            {
                                                "name": "type",
                                                "required": false,
                                                "type": "string"
                                            },
                                            {
                                                "name": "name",
                                                "required": false,
                                                "type": "string"
                                            },
                                            {
                                                "name": "assignIp",
                                                "required": false,
                                                "type": "string"
                                            }
                                        ],
                                        "type": "object"
                                    },
                                    {
                                        "name": "imageName",
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
                                        "name": "name",
                                        "required": true,
                                        "type": "string"
                                    },
                                    {
                                        "array_type": "object",
                                        "name": "servicesToConnect",
                                        "required": true,
                                        "schema": [
                                            {
                                                "name": "service",
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
                                        "name": "networkMode",
                                        "required": true,
                                        "type": "string"
                                    },
                                    {
                                        "name": "vlan",
                                        "required": false,
                                        "type": "string"
                                    }
                                ],
                                "type": "array"
                            },
                            {
                                "array_type": "object",
                                "name": "vlan",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "type",
                                        "required": true,
                                        "type": "string"
                                    },
                                    {
                                        "name": "id",
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
                                    }
                                ],
                                "type": "array"
                            }
                        ],
                        "type": "array"
                    }
                ],
                "type": "array"
            }
        ]
    },
    "responses": {
        "get_device_details_by_ip": {
            "properties": [
                "provisionDetails"
            ],
            "type": "object"
        },
        "provision_nfv": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        }
    }
}"""
)
