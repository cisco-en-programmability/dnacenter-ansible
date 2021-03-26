from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "devices",
    "name": "interface",
    "operations": {
        "get": [
            "get_all_interfaces",
            "get_interface_by_id",
            "get_device_interface_count",
            "get_interface_by_ip",
            "get_interface_info_by_id",
            "get_device_interfaces_by_specified_range",
            "get_device_interface_count_by_id",
            "get_interface_details",
            "get_isis_interfaces",
            "get_ospf_interfaces"
        ]
    },
    "parameters": {
        "get_all_interfaces": [
            {
                "name": "limit",
                "required": false,
                "type": "number"
            },
            {
                "name": "offset",
                "required": false,
                "type": "number"
            }
        ],
        "get_device_interface_count": [
            {
                "artificial": true,
                "name": "count",
                "required": true,
                "type": "boolean"
            }
        ],
        "get_device_interface_count_by_id": [
            {
                "name": "device_id",
                "required": true,
                "type": "string"
            },
            {
                "artificial": true,
                "name": "count",
                "required": true,
                "type": "boolean"
            }
        ],
        "get_device_interfaces_by_specified_range": [
            {
                "name": "device_id",
                "required": true,
                "type": "string"
            },
            {
                "name": "records_to_return",
                "required": true,
                "type": "integer"
            },
            {
                "name": "start_index",
                "required": true,
                "type": "integer"
            }
        ],
        "get_interface_by_id": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            }
        ],
        "get_interface_by_ip": [
            {
                "name": "ip_address",
                "required": true,
                "type": "string"
            }
        ],
        "get_interface_details": [
            {
                "name": "device_id",
                "required": true,
                "type": "string"
            },
            {
                "name": "name",
                "required": true,
                "type": "string"
            }
        ],
        "get_interface_info_by_id": [
            {
                "name": "device_id",
                "required": true,
                "type": "string"
            }
        ],
        "get_isis_interfaces": [
            {
                "artificial": true,
                "name": "isis",
                "required": true,
                "type": "boolean"
            }
        ],
        "get_ospf_interfaces": [
            {
                "artificial": true,
                "name": "ospf",
                "required": true,
                "type": "boolean"
            }
        ]
    },
    "responses": {
        "get_all_interfaces": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_device_interface_count": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_device_interface_count_by_id": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_device_interfaces_by_specified_range": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_interface_by_id": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_interface_by_ip": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_interface_details": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_interface_info_by_id": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_isis_interfaces": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_ospf_interfaces": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
