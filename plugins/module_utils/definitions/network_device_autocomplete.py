import json

module_definition = json.loads('''{
    "family": "devices",
    "name": "network_device_autocomplete",
    "operations": {
        "get": [
            "retrieves_all_network_devices"
        ]
    },
    "parameters": {
        "retrieves_all_network_devices": [
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
                "name": "limit",
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
                "name": "offset",
                "required": false,
                "type": "string"
            },
            {
                "name": "platform_id",
                "required": false,
                "type": "string"
            },
            {
                "name": "reachability_failure_reason",
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
                "name": "role_source",
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
            },
            {
                "name": "vrf_name",
                "required": false,
                "type": "string"
            }
        ]
    },
    "responses": {
        "retrieves_all_network_devices": {
            "properties": [],
            "type": "object"
        }
    }
}''')