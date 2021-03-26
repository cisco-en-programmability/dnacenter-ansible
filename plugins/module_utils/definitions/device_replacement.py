from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "device_replacement",
    "name": "device_replacement",
    "operations": {
        "get": [
            "return_replacement_devices_with_details",
            "return_replacement_devices_count"
        ],
        "post": [
            "mark_device_for_replacement"
        ],
        "put": [
            "unmark_device_for_replacement"
        ]
    },
    "parameters": {
        "mark_device_for_replacement": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "creationTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "family",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "faultyDeviceId",
                        "required": true,
                        "type": "string"
                    },
                    {
                        "name": "faultyDeviceName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "faultyDevicePlatform",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "faultyDeviceSerialNumber",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "id",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "neighbourDeviceId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "networkReadinessTaskId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "replacementDevicePlatform",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "replacementDeviceSerialNumber",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "replacementStatus",
                        "required": true,
                        "type": "string"
                    },
                    {
                        "name": "replacementTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "workflowId",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "array"
            }
        ],
        "return_replacement_devices_count": [
            {
                "name": "replacement_status",
                "required": false,
                "type": "string"
            },
            {
                "artificial": true,
                "name": "count",
                "required": true,
                "type": "boolean"
            }
        ],
        "return_replacement_devices_with_details": [
            {
                "name": "family",
                "required": false,
                "type": "string"
            },
            {
                "name": "faulty_device_name",
                "required": false,
                "type": "string"
            },
            {
                "name": "faulty_device_platform",
                "required": false,
                "type": "string"
            },
            {
                "name": "faulty_device_serial_number",
                "required": false,
                "type": "string"
            },
            {
                "name": "limit",
                "required": false,
                "type": "integer"
            },
            {
                "name": "offset",
                "required": false,
                "type": "integer"
            },
            {
                "name": "replacement_device_platform",
                "required": false,
                "type": "string"
            },
            {
                "name": "replacement_device_serial_number",
                "required": false,
                "type": "string"
            },
            {
                "name": "replacement_status",
                "required": false,
                "type": "string"
            },
            {
                "name": "sort_by",
                "required": false,
                "type": "string"
            },
            {
                "name": "sort_order",
                "required": false,
                "type": "string"
            }
        ],
        "unmark_device_for_replacement": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "creationTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "family",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "faultyDeviceId",
                        "required": true,
                        "type": "string"
                    },
                    {
                        "name": "faultyDeviceName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "faultyDevicePlatform",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "faultyDeviceSerialNumber",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "id",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "neighbourDeviceId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "networkReadinessTaskId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "replacementDevicePlatform",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "replacementDeviceSerialNumber",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "replacementStatus",
                        "required": true,
                        "type": "string"
                    },
                    {
                        "name": "replacementTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "workflowId",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "array"
            }
        ]
    },
    "responses": {
        "mark_device_for_replacement": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "return_replacement_devices_count": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "return_replacement_devices_with_details": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "unmark_device_for_replacement": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
