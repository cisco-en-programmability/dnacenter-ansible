from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "network_settings",
    "name": "device_credential",
    "operations": {
        "delete": [
            "delete_device_credential"
        ],
        "get": [
            "get_device_credential_details"
        ],
        "post": [
            "create_device_credentials"
        ],
        "put": [
            "update_device_credentials"
        ]
    },
    "parameters": {
        "create_device_credentials": [
            {
                "name": "settings",
                "required": true,
                "schema": [
                    {
                        "array_type": "object",
                        "name": "cliCredential",
                        "required": false,
                        "schema": [
                            {
                                "name": "description",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "username",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "password",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "enablePassword",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "array_type": "object",
                        "name": "snmpV2cRead",
                        "required": false,
                        "schema": [
                            {
                                "name": "description",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "readCommunity",
                                "required": true,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "array_type": "object",
                        "name": "snmpV2cWrite",
                        "required": false,
                        "schema": [
                            {
                                "name": "description",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "writeCommunity",
                                "required": true,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "array_type": "object",
                        "name": "snmpV3",
                        "required": false,
                        "schema": [
                            {
                                "name": "description",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "username",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "privacyType",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "privacyPassword",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "authType",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "authPassword",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "snmpMode",
                                "required": true,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "array_type": "object",
                        "name": "httpsRead",
                        "required": false,
                        "schema": [
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "username",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "password",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "port",
                                "required": false,
                                "type": "number"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "array_type": "object",
                        "name": "httpsWrite",
                        "required": false,
                        "schema": [
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "username",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "password",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "port",
                                "required": false,
                                "type": "number"
                            }
                        ],
                        "type": "array"
                    }
                ],
                "type": "object"
            }
        ],
        "delete_device_credential": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            }
        ],
        "get_device_credential_details": [
            {
                "name": "site_id",
                "required": false,
                "type": "string"
            }
        ],
        "update_device_credentials": [
            {
                "name": "settings",
                "required": true,
                "schema": [
                    {
                        "name": "cliCredential",
                        "required": false,
                        "schema": [
                            {
                                "name": "description",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "username",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "password",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "enablePassword",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "id",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "snmpV2cRead",
                        "required": false,
                        "schema": [
                            {
                                "name": "description",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "readCommunity",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "id",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "snmpV2cWrite",
                        "required": false,
                        "schema": [
                            {
                                "name": "description",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "writeCommunity",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "id",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "snmpV3",
                        "required": false,
                        "schema": [
                            {
                                "name": "authPassword",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "authType",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "snmpMode",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "privacyPassword",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "privacyType",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "username",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "description",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "id",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "httpsRead",
                        "required": false,
                        "schema": [
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "username",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "password",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "port",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "id",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "httpsWrite",
                        "required": false,
                        "schema": [
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "username",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "password",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "port",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "id",
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
        "create_device_credentials": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        },
        "delete_device_credential": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        },
        "get_device_credential_details": {
            "properties": [
                "snmp_v3",
                "http_read",
                "http_write",
                "snmp_v2_write",
                "snmp_v2_read",
                "cli"
            ],
            "type": "object"
        },
        "update_device_credentials": {
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
