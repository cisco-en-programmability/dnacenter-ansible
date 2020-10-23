module_definition = {
  "name": "interface",
  "family": "devices",
  "operations": {
      "get": [
        "get_all_interfaces",
        "get_interface_by_id",
        "get_device_interface_count",
        "get_interface_by_ip",
        "get_isis_interfaces",
        "get_interface_info_by_id",
        "get_device_interfaces_by_specified_range",
        "get_device_interface_count_by_id",
        "get_interface_details",
        "get_ospf_interfaces"
      ]
  },
  "parameters": {
    "get_all_interfaces": [
        {
          "name": "limit",
          "required": False,
          "type": "number"
        },
        {
          "name": "offset",
          "required": False,
          "type": "number"
        }
    ],
    "get_interface_by_id": [
        {
          "name": "id",
          "required": True,
          "type": "string"
        }
    ],
    "get_device_interface_count": [
        {
          "name": "count",
          "required": True,
          "type": "boolean"
        }
    ],
    "get_interface_by_ip": [
        {
          "name": "ipAddress",
          "required": True,
          "type": "string"
        }
    ],
    "get_isis_interfaces": [
        {
          "name": "isis",
          "required": True,
          "type": "boolean"
        }
    ],
    "get_interface_info_by_id": [
        {
          "name": "deviceId",
          "required": True,
          "type": "string"
        }
    ],
    "get_device_interfaces_by_specified_range" : [
        {
          "name": "deviceId",
          "required": True,
          "sdk_name": "device_id",
          "type": "string"
        },
        {
          "name": "recordsToReturn",
          "required": True,
          "sdk_name": "records_to_return",
          "type": "integer"
        },
        {
          "name": "startIndex",
          "required": True,
          "sdk_name": "start_index",
          "type": "integer"
        }
    ],
    "get_device_interface_count_by_id": [
        {
          "name": "deviceId",
          "required": True,
          "type": "string"
        },
        {
            "name": "count",
            "required": True,
            "type": "boolean"
        }
    ],
    "get_interface_details": [
        {
          "name": "deviceId",
          "required": True,
          "type": "string"
        },
        {
          "name": "name",
          "required": True,
          "type": "string"
        }
    ],
    "get_ospf_interfaces": [
        {
            "name": "ospf",
            "required": True,
            "type": "boolean"
        }
    ]
  } 
}