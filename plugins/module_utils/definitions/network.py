import json

module_definition = json.loads('''{
    "family": "network_settings",
    "name": "network",
    "operations": {
        "get": [
            "get_network"
        ],
        "post": [
            "create_network"
        ],
        "put": [
            "update_network"
        ]
    },
    "parameters": {
        "create_network": [
            {
                "name": "site_id",
                "required": true,
                "type": "string"
            },
            {
                "name": "settings",
                "required": true,
                "schema": [
                    {
                        "array_type": "string",
                        "name": "dhcpServer",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    },
                    {
                        "name": "dnsServer",
                        "required": false,
                        "schema": [
                            {
                                "name": "domainName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "primaryIpAddress",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "secondaryIpAddress",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "syslogServer",
                        "required": false,
                        "schema": [
                            {
                                "array_type": "string",
                                "name": "ipAddresses",
                                "required": false,
                                "schema": [],
                                "type": "array"
                            },
                            {
                                "name": "configureDnacIP",
                                "required": false,
                                "type": "boolean"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "snmpServer",
                        "required": false,
                        "schema": [
                            {
                                "array_type": "string",
                                "name": "ipAddresses",
                                "required": false,
                                "schema": [],
                                "type": "array"
                            },
                            {
                                "name": "configureDnacIP",
                                "required": false,
                                "type": "boolean"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "netflowcollector",
                        "required": false,
                        "schema": [
                            {
                                "name": "ipAddress",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "port",
                                "required": false,
                                "type": "number"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "array_type": "string",
                        "name": "ntpServer",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    },
                    {
                        "name": "timezone",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "messageOfTheday",
                        "required": false,
                        "schema": [
                            {
                                "name": "bannerMessage",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "retainExistingBanner",
                                "required": false,
                                "type": "boolean"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "network_aaa",
                        "required": false,
                        "schema": [
                            {
                                "name": "servers",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "ipAddress",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "network",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "protocol",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "sharedSecret",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "clientAndEndpoint_aaa",
                        "required": false,
                        "schema": [
                            {
                                "name": "servers",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "ipAddress",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "network",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "protocol",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "sharedSecret",
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
        "get_network": [
            {
                "name": "site_id",
                "required": false,
                "type": "string"
            }
        ],
        "update_network": [
            {
                "name": "site_id",
                "required": true,
                "type": "string"
            },
            {
                "name": "settings",
                "required": true,
                "schema": [
                    {
                        "array_type": "string",
                        "name": "dhcpServer",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    },
                    {
                        "name": "dnsServer",
                        "required": false,
                        "schema": [
                            {
                                "name": "domainName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "primaryIpAddress",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "secondaryIpAddress",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "syslogServer",
                        "required": false,
                        "schema": [
                            {
                                "array_type": "string",
                                "name": "ipAddresses",
                                "required": false,
                                "schema": [],
                                "type": "array"
                            },
                            {
                                "name": "configureDnacIP",
                                "required": false,
                                "type": "boolean"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "snmpServer",
                        "required": false,
                        "schema": [
                            {
                                "array_type": "string",
                                "name": "ipAddresses",
                                "required": false,
                                "schema": [],
                                "type": "array"
                            },
                            {
                                "name": "configureDnacIP",
                                "required": false,
                                "type": "boolean"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "netflowcollector",
                        "required": false,
                        "schema": [
                            {
                                "name": "ipAddress",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "port",
                                "required": false,
                                "type": "number"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "array_type": "string",
                        "name": "ntpServer",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    },
                    {
                        "name": "timezone",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "messageOfTheday",
                        "required": false,
                        "schema": [
                            {
                                "name": "bannerMessage",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "retainExistingBanner",
                                "required": false,
                                "type": "boolean"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "network_aaa",
                        "required": false,
                        "schema": [
                            {
                                "name": "servers",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "ipAddress",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "network",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "protocol",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "sharedSecret",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "clientAndEndpoint_aaa",
                        "required": false,
                        "schema": [
                            {
                                "name": "servers",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "ipAddress",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "network",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "protocol",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "sharedSecret",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "object"
                    }
                ],
                "type": "object"
            }
        ]
    },
    "responses": {
        "create_network": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        },
        "get_network": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "update_network": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        }
    }
}''')