from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "wireless",
    "name": "wireless_provision",
    "operations": {
        "post": [
            "provision"
        ],
        "put": [
            "provision_update"
        ]
    },
    "parameters": {
        "provision": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "deviceName",
                        "required": true,
                        "type": "string"
                    },
                    {
                        "name": "site",
                        "required": true,
                        "type": "string"
                    },
                    {
                        "array_type": "string",
                        "name": "managedAPLocations",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    },
                    {
                        "array_type": "object",
                        "name": "dynamicInterfaces",
                        "required": false,
                        "schema": [
                            {
                                "name": "interfaceIPAddress",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "interfaceNetmaskInCIDR",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "interfaceGateway",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "lagOrPortNumber",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "vlanId",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "interfaceName",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    }
                ],
                "type": "array"
            }
        ],
        "provision_update": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "deviceName",
                        "required": true,
                        "type": "string"
                    },
                    {
                        "array_type": "string",
                        "name": "managedAPLocations",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    },
                    {
                        "array_type": "object",
                        "name": "dynamicInterfaces",
                        "required": false,
                        "schema": [
                            {
                                "name": "interfaceIPAddress",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "interfaceNetmaskInCIDR",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "interfaceGateway",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "lagOrPortNumber",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "vlanId",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "interfaceName",
                                "required": false,
                                "type": "string"
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
        "provision": {
            "properties": [
                "executionId",
                "executionUrl",
                "provisioningTasks"
            ],
            "type": "object"
        },
        "provision_update": {
            "properties": [
                "executionId",
                "executionUrl",
                "provisioningTasks"
            ],
            "type": "object"
        }
    }
}"""
)
