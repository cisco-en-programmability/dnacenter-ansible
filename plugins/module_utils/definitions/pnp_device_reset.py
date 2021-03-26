from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "device_onboarding_pnp",
    "name": "pnp_device_reset",
    "operations": {
        "post": [
            "reset_device"
        ]
    },
    "parameters": {
        "reset_device": [
            {
                "array_type": "object",
                "name": "deviceResetList",
                "required": false,
                "schema": [
                    {
                        "array_type": "object",
                        "name": "configList",
                        "required": false,
                        "schema": [
                            {
                                "name": "configId",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "array_type": "object",
                                "name": "configParameters",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "key",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "value",
                                        "required": false,
                                        "type": "string"
                                    }
                                ],
                                "type": "array"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "deviceId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "licenseLevel",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "licenseType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "topOfStackSerialNumber",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "array"
            },
            {
                "name": "projectId",
                "type": "string"
            },
            {
                "name": "workflowId",
                "type": "string"
            }
        ]
    },
    "responses": {
        "reset_device": {
            "properties": [
                "jsonArrayResponse",
                "jsonResponse",
                "message",
                "statusCode"
            ],
            "type": "object"
        }
    }
}"""
)
