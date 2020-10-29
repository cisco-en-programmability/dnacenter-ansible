import json

module_definition = json.loads('''{
    "family": "devices",
    "name": "network_device",
    "operations": {
        "delete": [
            "delete_device_by_id"
        ],
        "get": [
            "get_device_list",
            "get_device_by_id",
            "get_device_summary",
            "get_network_device_by_pagination_range",
            "get_device_count",
            "get_network_device_by_ip",
            "get_device_by_serial_number"
        ],
        "post": [
            "add_device"
        ],
        "put": [
            "sync_devices"
        ]
    },
    "parameters": {
        "add_device": [
            {
                "name": "cliTransport",
                "required": true,
                "type": "string"
            },
            {
                "name": "computeDevice",
                "type": "boolean"
            },
            {
                "name": "enablePassword",
                "required": true,
                "type": "string"
            },
            {
                "name": "extendedDiscoveryInfo",
                "type": "string"
            },
            {
                "name": "httpPassword",
                "type": "string"
            },
            {
                "name": "httpPort",
                "type": "string"
            },
            {
                "name": "httpSecure",
                "type": "boolean"
            },
            {
                "name": "httpUserName",
                "type": "string"
            },
            {
                "name": "ipAddress",
                "required": true,
                "type": "array"
            },
            {
                "name": "merakiOrgId",
                "type": "array"
            },
            {
                "name": "netconfPort",
                "type": "string"
            },
            {
                "name": "password",
                "required": true,
                "type": "string"
            },
            {
                "name": "serialNumber",
                "type": "string"
            },
            {
                "name": "snmpAuthPassphrase",
                "required": true,
                "type": "string"
            },
            {
                "name": "snmpAuthProtocol",
                "required": true,
                "type": "string"
            },
            {
                "name": "snmpMode",
                "required": true,
                "type": "string"
            },
            {
                "name": "snmpPrivPassphrase",
                "required": true,
                "type": "string"
            },
            {
                "name": "snmpPrivProtocol",
                "required": true,
                "type": "string"
            },
            {
                "name": "snmpROCommunity",
                "required": true,
                "type": "string"
            },
            {
                "name": "snmpRWCommunity",
                "required": true,
                "type": "string"
            },
            {
                "name": "snmpRetry",
                "required": true,
                "type": "integer"
            },
            {
                "name": "snmpTimeout",
                "required": true,
                "type": "integer"
            },
            {
                "name": "snmpUserName",
                "required": true,
                "type": "string"
            },
            {
                "name": "snmpVersion",
                "type": "string"
            },
            {
                "enum": [
                    "COMPUTE_DEVICE",
                    "MERAKI_DASHBOARD",
                    "NETWORK_DEVICE",
                    "NODATACHANGE"
                ],
                "name": "type",
                "type": "string"
            },
            {
                "name": "updateMgmtIPaddressList",
                "type": "array"
            },
            {
                "name": "userName",
                "required": true,
                "type": "string"
            }
        ],
        "delete_device_by_id": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            },
            {
                "name": "is_force_delete",
                "required": false,
                "type": "boolean"
            }
        ],
        "get_device_by_id": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            }
        ],
        "get_device_by_serial_number": [
            {
                "name": "serial_number",
                "required": true,
                "type": "string"
            }
        ],
        "get_device_count": [
            {
                "name": "count",
                "required": true,
                "type": "boolean"
            }
        ],
        "get_device_list": [
            {
                "name": "associated_wlc_ip",
                "required": false,
                "type": "string"
            },
            {
                "name": "collection_interval",
                "required": false,
                "type": "string"
            },
            {
                "name": "collection_status",
                "required": false,
                "type": "string"
            },
            {
                "name": "error_code",
                "required": false,
                "type": "string"
            },
            {
                "name": "error_description",
                "required": false,
                "type": "string"
            },
            {
                "name": "family",
                "required": false,
                "type": "string"
            },
            {
                "name": "hostname",
                "required": false,
                "type": "string"
            },
            {
                "name": "id",
                "required": false,
                "type": "string"
            },
            {
                "name": "license_name",
                "required": false,
                "type": "string"
            },
            {
                "name": "license_status",
                "required": false,
                "type": "string"
            },
            {
                "name": "license_type",
                "required": false,
                "type": "string"
            },
            {
                "name": "location",
                "required": false,
                "type": "string"
            },
            {
                "name": "location_name",
                "required": false,
                "type": "string"
            },
            {
                "name": "mac_address",
                "required": false,
                "type": "string"
            },
            {
                "name": "management_ip_address",
                "required": false,
                "type": "string"
            },
            {
                "name": "module_equpimenttype",
                "required": false,
                "type": "string"
            },
            {
                "name": "module_name",
                "required": false,
                "type": "string"
            },
            {
                "name": "module_operationstatecode",
                "required": false,
                "type": "string"
            },
            {
                "name": "module_partnumber",
                "required": false,
                "type": "string"
            },
            {
                "name": "module_servicestate",
                "required": false,
                "type": "string"
            },
            {
                "name": "module_vendorequipmenttype",
                "required": false,
                "type": "string"
            },
            {
                "name": "not_synced_for_minutes",
                "required": false,
                "type": "string"
            },
            {
                "name": "platform_id",
                "required": false,
                "type": "string"
            },
            {
                "name": "reachability_status",
                "required": false,
                "type": "string"
            },
            {
                "name": "role",
                "required": false,
                "type": "string"
            },
            {
                "name": "serial_number",
                "required": false,
                "type": "string"
            },
            {
                "name": "series",
                "required": false,
                "type": "string"
            },
            {
                "name": "software_type",
                "required": false,
                "type": "string"
            },
            {
                "name": "software_version",
                "required": false,
                "type": "string"
            },
            {
                "name": "type",
                "required": false,
                "type": "string"
            },
            {
                "name": "up_time",
                "required": false,
                "type": "string"
            }
        ],
        "get_device_summary": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            },
            {
                "name": "summary",
                "required": true,
                "type": "boolean"
            }
        ],
        "get_network_device_by_ip": [
            {
                "name": "ip_address",
                "required": true,
                "type": "string"
            }
        ],
        "get_network_device_by_pagination_range": [
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
        "sync_devices": [
            {
                "name": "cliTransport",
                "required": true,
                "type": "string"
            },
            {
                "name": "computeDevice",
                "type": "boolean"
            },
            {
                "name": "enablePassword",
                "required": true,
                "type": "string"
            },
            {
                "name": "extendedDiscoveryInfo",
                "type": "string"
            },
            {
                "name": "httpPassword",
                "type": "string"
            },
            {
                "name": "httpPort",
                "type": "string"
            },
            {
                "name": "httpSecure",
                "type": "boolean"
            },
            {
                "name": "httpUserName",
                "type": "string"
            },
            {
                "name": "ipAddress",
                "required": true,
                "type": "array"
            },
            {
                "name": "merakiOrgId",
                "type": "array"
            },
            {
                "name": "netconfPort",
                "type": "string"
            },
            {
                "name": "password",
                "required": true,
                "type": "string"
            },
            {
                "name": "serialNumber",
                "type": "string"
            },
            {
                "name": "snmpAuthPassphrase",
                "required": true,
                "type": "string"
            },
            {
                "name": "snmpAuthProtocol",
                "required": true,
                "type": "string"
            },
            {
                "name": "snmpMode",
                "required": true,
                "type": "string"
            },
            {
                "name": "snmpPrivPassphrase",
                "required": true,
                "type": "string"
            },
            {
                "name": "snmpPrivProtocol",
                "required": true,
                "type": "string"
            },
            {
                "name": "snmpROCommunity",
                "required": true,
                "type": "string"
            },
            {
                "name": "snmpRWCommunity",
                "required": true,
                "type": "string"
            },
            {
                "name": "snmpRetry",
                "required": true,
                "type": "integer"
            },
            {
                "name": "snmpTimeout",
                "required": true,
                "type": "integer"
            },
            {
                "name": "snmpUserName",
                "required": true,
                "type": "string"
            },
            {
                "name": "snmpVersion",
                "type": "string"
            },
            {
                "enum": [
                    "COMPUTE_DEVICE",
                    "MERAKI_DASHBOARD",
                    "NETWORK_DEVICE",
                    "NODATACHANGE"
                ],
                "name": "type",
                "type": "string"
            },
            {
                "name": "updateMgmtIPaddressList",
                "type": "array"
            },
            {
                "name": "userName",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "add_device": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "delete_device_by_id": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_device_by_id": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_device_by_serial_number": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_device_count": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_device_list": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_device_summary": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_network_device_by_ip": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_network_device_by_pagination_range": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "sync_devices": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}''')