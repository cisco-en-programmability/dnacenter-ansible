from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "topology",
    "name": "topology",
    "operations": {
        "get": [
            "get_topology_details",
            "get_l3_topology_details",
            "get_physical_topology",
            "get_site_topology",
            "get_vlan_details"
        ]
    },
    "parameters": {
        "get_l3_topology_details": [
            {
                "name": "topology_type",
                "required": true,
                "type": "string"
            },
            {
                "artificial": true,
                "name": "layer3",
                "required": true,
                "type": "boolean"
            }
        ],
        "get_physical_topology": [
            {
                "name": "node_type",
                "required": false,
                "type": "string"
            },
            {
                "artificial": true,
                "name": "physical",
                "required": true,
                "type": "boolean"
            }
        ],
        "get_site_topology": [
            {
                "artificial": true,
                "name": "site",
                "required": true,
                "type": "boolean"
            }
        ],
        "get_topology_details": [
            {
                "name": "vlan_id",
                "required": true,
                "type": "string"
            },
            {
                "artificial": true,
                "name": "layer2",
                "required": true,
                "type": "boolean"
            }
        ],
        "get_vlan_details": [
            {
                "artificial": true,
                "name": "vlan",
                "required": true,
                "type": "boolean"
            }
        ]
    },
    "responses": {
        "get_l3_topology_details": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_physical_topology": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_site_topology": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_topology_details": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_vlan_details": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
