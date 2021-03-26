from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "discovery",
    "name": "discovery_network_device",
    "operations": {
        "get": [
            "get_discovered_network_devices_by_discovery_id",
            "get_discovered_devices_by_range",
            "get_devices_discovered_by_id",
            "get_network_devices_from_discovery"
        ]
    },
    "parameters": {
        "get_devices_discovered_by_id": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            },
            {
                "name": "task_id",
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
        "get_discovered_devices_by_range": [
            {
                "name": "id",
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
            },
            {
                "name": "task_id",
                "required": false,
                "type": "string"
            }
        ],
        "get_discovered_network_devices_by_discovery_id": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            },
            {
                "name": "task_id",
                "required": false,
                "type": "string"
            }
        ],
        "get_network_devices_from_discovery": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            },
            {
                "name": "cli_status",
                "required": false,
                "type": "string"
            },
            {
                "name": "http_status",
                "required": false,
                "type": "string"
            },
            {
                "name": "ip_address",
                "required": false,
                "type": "string"
            },
            {
                "name": "netconf_status",
                "required": false,
                "type": "string"
            },
            {
                "name": "ping_status",
                "required": false,
                "type": "string"
            },
            {
                "name": "snmp_status",
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
            },
            {
                "name": "task_id",
                "required": false,
                "type": "string"
            },
            {
                "artificial": true,
                "name": "summary",
                "required": true,
                "type": "boolean"
            }
        ]
    },
    "responses": {
        "get_devices_discovered_by_id": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_discovered_devices_by_range": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_discovered_network_devices_by_discovery_id": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_network_devices_from_discovery": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
