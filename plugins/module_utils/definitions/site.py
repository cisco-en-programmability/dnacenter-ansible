module_definition = {
  "name": "site",
  "family": "sites",
  "operations": {
      "post": ["create_site"],
      "put": ["update_site"],
      "delete": ["delete_site"],
      "get": [
        "get_site",
        "get_site_count"
        ]
  },
  "parameters": {
  "create_site": [
    {
      "enum": [
        "area",
        "building",
        "floor"
      ],
      "name": "type",
      "required": True,
      "type": "string"
    },
    {
      "name": "site",
      "type": "object",
      "required": True
    }
  ],
  "delete_site": [
    {
      "name": "siteId",
      "required": True,
      "sdk_name": "site_id",
      "type": "string"
    },
    {
      "name": "headers",
      "type": "object"
    }
  ],
  "get_site": [
    {
      "name": "limit",
      "required": False,
      "sdk_name": "limit",
      "type": "string"
    },
    {
      "name": "name",
      "required": False,
      "sdk_name": "name",
      "type": "string"
    },
    {
      "name": "offset",
      "required": False,
      "sdk_name": "offset",
      "type": "string"
    },
    {
      "name": "siteId",
      "required": False,
      "sdk_name": "site_id",
      "type": "string"
    },
    {
      "name": "type",
      "required": False,
      "sdk_name": "type",
      "type": "string"
    },
    {
      "name": "headers",
      "type": "object"
    }
  ],
  "get_site_count": [
    {
      "name": "siteId",
      "required": False,
      "sdk_name": "site_id",
      "type": "string"
    },
    {
        "name": "count",
        "type": "boolean",
        "required": True
      },
    {
      "name": "headers",
      "type": "object"
    }
  ],
  "update_site": [
    {
      "name": "siteId",
      "required": True,
      "sdk_name": "site_id",
      "type": "string"
    },
    {
      "name": "site",
      "required": True,
      "type": "object"
    },
    {
      "enum": [
        "area",
        "building",
        "floor"
      ],
      "name": "type",
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