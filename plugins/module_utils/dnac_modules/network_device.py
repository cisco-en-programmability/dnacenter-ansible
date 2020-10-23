module_definition = {
  "name": "network_device",
  "family": "devices",
  "operations": {
      "post": ["add_device"],
      "put": ["sync_devices"],
      "delete": ["delete_device_by_id"],
      "get": [
        "get_device_list",
        "get_device_by_id",
        "get_device_summary",
        "get_network_device_by_pagination_range",
        "get_device_count",
        "get_network_device_by_ip",
        "get_device_by_serial_number"
      ]
  },
  "parameters": {
    "add_device": [
      {
        "name": "cliTransport",
        "required": True,
        "type": "string"
      },
      {
        "name": "computeDevice",
        "type": "boolean"
      },
      {
        "name": "enablePassword",
        "required": True,
        "type": "string"
      },
      {
        "name": "extendedDiscoveryInfo",
        "type": "string"
      },
      {
        "name": "httpPassword",
        "type": "string",
        "required": True
      },
      {
        "name": "httpPort",
        "type": "string",
        "required": False
      },
      {
        "name": "httpSecure",
        "type": "boolean"
      },
      {
        "name": "httpUserName",
        "type": "string",
        "required": True
      },
      {
        "name": "ipAddress",
        "required": True,
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
        "required": True,
        "type": "string"
      },
      {
        "name": "serialNumber",
        "type": "string"
      },
      {
        "name": "snmpAuthPassphrase",
        "required": True,
        "type": "string"
      },
      {
        "name": "snmpAuthProtocol",
        "required": True,
        "type": "string"
      },
      {
        "name": "snmpMode",
        "required": True,
        "type": "string"
      },
      {
        "name": "snmpPrivPassphrase",
        "required": True,
        "type": "string"
      },
      {
        "name": "snmpPrivProtocol",
        "required": True,
        "type": "string"
      },
      {
        "name": "snmpROCommunity",
        "required": True,
        "type": "string"
      },
      {
        "name": "snmpRWCommunity",
        "required": True,
        "type": "string"
      },
      {
        "name": "snmpRetry",
        "required": True,
        "type": "number"
      },
      {
        "name": "snmpTimeout",
        "required": True,
        "type": "number"
      },
      {
        "name": "snmpUserName",
        "required": True,
        "type": "string"
      },
      {
        "name": "snmpVersion",
        "type": "string",
        "required": True
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
        "required": True,
        "type": "string"
      },
      {
        "name": "headers",
        "type": "object"
      },
      {
        "name": "payload",
        "type": "object"
      }
    ],
    "delete_device_by_id": [
      {
        "name": "id",
        "required": True,
        "sdk_name": "id",
        "type": "string"
      },
      {
        "name": "isForceDelete",
        "required": False,
        "sdk_name": "is_force_delete",
        "type": "boolean"
      },
      {
        "name": "headers",
        "type": "object"
      }
    ],
    "get_device_by_id": [
      {
        "name": "id",
        "required": True,
        "sdk_name": "id",
        "type": "string"
      },
      {
        "name": "headers",
        "type": "object"
      }
    ],
    "get_device_by_serial_number": [
      {
        "name": "serial_number",
        "required": True,
        "type": "string"
      },
      {
        "name": "headers",
        "type": "object"
      }
    ],
    "get_device_count": [
      {
        "name": "headers",
        "type": "object"
      },
      {
        "name": "count",
        "type": "boolean",
        "required": True
      }
    ],
    "get_device_list": [
      {
        "name": "associatedWlcIp",
        "required": False,
        "sdk_name": "associated_wlc_ip",
        "type": "array"
      },
      {
        "name": "collectionInterval",
        "required": False,
        "sdk_name": "collection_interval",
        "type": "array"
      },
      {
        "name": "collectionStatus",
        "required": False,
        "sdk_name": "collection_status",
        "type": "array"
      },
      {
        "name": "errorCode",
        "required": False,
        "sdk_name": "error_code",
        "type": "array"
      },
      {
        "name": "errorDescription",
        "required": False,
        "sdk_name": "error_description",
        "type": "array"
      },
      {
        "name": "family",
        "required": False,
        "sdk_name": "family",
        "type": "array"
      },
      {
        "name": "hostname",
        "required": False,
        "sdk_name": "hostname",
        "type": "array"
      },
      {
        "name": "id",
        "required": False,
        "sdk_name": "id",
        "type": "string"
      },
      {
        "name": "license.name",
        "required": False,
        "sdk_name": "license_name",
        "type": "array"
      },
      {
        "name": "license.status",
        "required": False,
        "sdk_name": "license_status",
        "type": "array"
      },
      {
        "name": "license.type",
        "required": False,
        "sdk_name": "license_type",
        "type": "array"
      },
      {
        "name": "location",
        "required": False,
        "sdk_name": "location",
        "type": "array"
      },
      {
        "name": "locationName",
        "required": False,
        "sdk_name": "location_name",
        "type": "array"
      },
      {
        "name": "macAddress",
        "required": False,
        "sdk_name": "mac_address",
        "type": "array"
      },
      {
        "name": "managementIpAddress",
        "required": False,
        "sdk_name": "management_ip_address",
        "type": "array"
      },
      {
        "name": "module+equpimenttype",
        "required": False,
        "sdk_name": "module_equpimenttype",
        "type": "array"
      },
      {
        "name": "module+name",
        "required": False,
        "sdk_name": "module_name",
        "type": "array"
      },
      {
        "name": "module+operationstatecode",
        "required": False,
        "sdk_name": "module_operationstatecode",
        "type": "array"
      },
      {
        "name": "module+partnumber",
        "required": False,
        "sdk_name": "module_partnumber",
        "type": "array"
      },
      {
        "name": "module+servicestate",
        "required": False,
        "sdk_name": "module_servicestate",
        "type": "array"
      },
      {
        "name": "module+vendorequipmenttype",
        "required": False,
        "sdk_name": "module_vendorequipmenttype",
        "type": "array"
      },
      {
        "name": "notSyncedForMinutes",
        "required": False,
        "sdk_name": "not_synced_for_minutes",
        "type": "array"
      },
      {
        "name": "platformId",
        "required": False,
        "sdk_name": "platform_id",
        "type": "array"
      },
      {
        "name": "reachabilityStatus",
        "required": False,
        "sdk_name": "reachability_status",
        "type": "array"
      },
      {
        "name": "role",
        "required": False,
        "sdk_name": "role",
        "type": "array"
      },
      {
        "name": "serialNumber",
        "required": False,
        "sdk_name": "serial_number",
        "type": "array"
      },
      {
        "name": "series",
        "required": False,
        "sdk_name": "series",
        "type": "array"
      },
      {
        "name": "softwareType",
        "required": False,
        "sdk_name": "software_type",
        "type": "array"
      },
      {
        "name": "softwareVersion",
        "required": False,
        "sdk_name": "software_version",
        "type": "array"
      },
      {
        "name": "type",
        "required": False,
        "sdk_name": "type",
        "type": "array"
      },
      {
        "name": "upTime",
        "required": False,
        "sdk_name": "up_time",
        "type": "array"
      },
      {
        "name": "headers",
        "type": "object"
      }
    ],
    "get_device_summary": [
      {
        "name": "id",
        "required": True,
        "sdk_name": "id",
        "type": "string"
      },
      {
        "name": "headers",
        "type": "object"
      },
      {
        "name": "summary",
        "type": "boolean",
        "required": True
      }
    ],
    "get_network_device_by_ip": [
      {
        "name": "ip_address",
        "required": True,
        "sdk_name": "ip_address",
        "type": "string"
      },
      {
        "name": "headers",
        "type": "object"
      }
    ],
    "get_network_device_by_pagination_range": [
      {
        "name": "records_to_return",
        "required": True,
        "sdk_name": "records_to_return",
        "type": "integer"
      },
      {
        "name": "start_index",
        "required": True,
        "sdk_name": "start_index",
        "type": "integer"
      },
      {
        "name": "headers",
        "type": "object"
      }
    ],
    "sync_devices": [
      {
        "name": "cliTransport",
        "required": True,
        "type": "string"
      },
      {
        "name": "computeDevice",
        "type": "boolean"
      },
      {
        "name": "enablePassword",
        "required": True,
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
        "required": True,
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
        "required": True,
        "type": "string"
      },
      {
        "name": "serialNumber",
        "type": "string"
      },
      {
        "name": "snmpAuthPassphrase",
        "required": True,
        "type": "string"
      },
      {
        "name": "snmpAuthProtocol",
        "required": True,
        "type": "string"
      },
      {
        "name": "snmpMode",
        "required": True,
        "type": "string"
      },
      {
        "name": "snmpPrivPassphrase",
        "required": True,
        "type": "string"
      },
      {
        "name": "snmpPrivProtocol",
        "required": True,
        "type": "string"
      },
      {
        "name": "snmpROCommunity",
        "required": True,
        "type": "string"
      },
      {
        "name": "snmpRWCommunity",
        "required": True,
        "type": "string"
      },
      {
        "name": "snmpRetry",
        "required": True,
        "type": "number"
      },
      {
        "name": "snmpTimeout",
        "required": True,
        "type": "number"
      },
      {
        "name": "snmpUserName",
        "required": True,
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
        "required": True,
        "type": "string"
      },
      {
        "name": "headers",
        "type": "object"
      },
      {
        "name": "payload",
        "type": "object"
      }
    ]
  }
}