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
      "required": True,
      "schema": [
        {
          "type": "object",
          "schema": [
            {
              "type": "string",
              "enum": [],
              "sensitive": False,
              "default": "",
              "constraints": [],
              "required": True,
              "name": "name",
              "displayText": "Name"
            },
            {
              "type": "string",
              "enum": [],
              "sensitive": False,
              "default": "",
              "constraints": [],
              "required": True,
              "name": "parentName",
              "displayText": "Parent Name"
            }
          ],
          "name": "area",
          "displayText": "Area"
        },
        {
          "type": "object",
          "schema": [
            {
              "type": "string",
              "enum": [],
              "sensitive": False,
              "default": "",
              "constraints": [],
              "required": True,
              "name": "name",
              "displayText": "Name"
            },
            {
              "type": "string",
              "enum": [],
              "sensitive": False,
              "default": "",
              "constraints": [],
              "required": False,
              "name": "address",
              "displayText": "Address"
            },
            {
              "type": "string",
              "enum": [],
              "sensitive": False,
              "default": "",
              "constraints": [],
              "required": True,
              "name": "parentName",
              "displayText": "Parent Name"
            },
            {
              "type": "number",
              "constraints": [],
              "required": True,
              "name": "latitude",
              "displayText": "Latitude"
            },
            {
              "type": "number",
              "constraints": [],
              "required": True,
              "name": "longitude",
              "displayText": "Longitude"
            }
          ],
          "name": "building",
          "displayText": "Building"
        },
        {
          "type": "object",
          "schema": [
            {
              "type": "string",
              "enum": [],
              "sensitive": False,
              "default": "",
              "constraints": [],
              "required": True,
              "name": "name",
              "displayText": "Name"
            },
            {
              "type": "string",
              "enum": [],
              "sensitive": False,
              "default": "",
              "constraints": [],
              "required": True,
              "name": "parentName",
              "displayText": "Parent Name"
            },
            {
              "type": "string",
              "enum": [
                "Cubes And Walled Offices",
                "Drywall Office Only",
                "Indoor High Ceiling",
                "Outdoor Open Space"
              ],
              "sensitive": False,
              "default": "",
              "constraints": [],
              "required": True,
              "name": "rfModel",
              "displayText": "Rf Model"
            },
            {
              "type": "number",
              "constraints": [],
              "required": True,
              "name": "width",
              "displayText": "Width"
            },
            {
              "type": "number",
              "constraints": [],
              "required": True,
              "name": "length",
              "displayText": "Length"
            },
            {
              "type": "number",
              "constraints": [],
              "required": True,
              "name": "height",
              "displayText": "Height"
            }
          ],
          "required": False,
          "name": "floor",
          "displayText": "Floor"
        }
      ]
    }
  ],
  "delete_site": [
    {
      "name": "site_id",
      "required": True,
      "type": "string"
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
      }
  ],
  "update_site": [
    {
      "name": "siteId",
      "required": True,
      "type": "string"
    },
    {
      "name": "site",
      "required": True,
      "type": "object",
      "schema": [
        {
          "type": "object",
          "schema": [
            {
              "type": "string",
              "enum": [],
              "sensitive": False,
              "default": "",
              "constraints": [],
              "required": True,
              "name": "name",
              "displayText": "Name"
            },
            {
              "type": "string",
              "enum": [],
              "sensitive": False,
              "default": "",
              "constraints": [],
              "required": True,
              "name": "parentName",
              "displayText": "Parent Name"
            }
          ],
          "name": "area",
          "displayText": "Area"
        },
        {
          "type": "object",
          "schema": [
            {
              "type": "string",
              "enum": [],
              "sensitive": False,
              "default": "",
              "constraints": [],
              "required": True,
              "name": "name",
              "displayText": "Name"
            },
            {
              "type": "string",
              "enum": [],
              "sensitive": False,
              "default": "",
              "constraints": [],
              "required": False,
              "name": "address",
              "displayText": "Address"
            },
            {
              "type": "string",
              "enum": [],
              "sensitive": False,
              "default": "",
              "constraints": [],
              "required": True,
              "name": "parentName",
              "displayText": "Parent Name"
            },
            {
              "type": "number",
              "constraints": [],
              "required": True,
              "name": "latitude",
              "displayText": "Latitude"
            },
            {
              "type": "number",
              "constraints": [],
              "required": True,
              "name": "longitude",
              "displayText": "Longitude"
            }
          ],
          "name": "building",
          "displayText": "Building"
        },
        {
          "type": "object",
          "schema": [
            {
              "type": "string",
              "enum": [],
              "sensitive": False,
              "default": "",
              "constraints": [],
              "required": True,
              "name": "name",
              "displayText": "Name"
            },
            {
              "type": "string",
              "enum": [],
              "sensitive": False,
              "default": "",
              "constraints": [],
              "required": True,
              "name": "parentName",
              "displayText": "Parent Name"
            },
            {
              "type": "string",
              "enum": [
                "Cubes And Walled Offices",
                "Drywall Office Only",
                "Indoor High Ceiling",
                "Outdoor Open Space"
              ],
              "sensitive": False,
              "default": "",
              "constraints": [],
              "required": True,
              "name": "rfModel",
              "displayText": "Rf Model"
            },
            {
              "type": "number",
              "constraints": [],
              "required": True,
              "name": "width",
              "displayText": "Width"
            },
            {
              "type": "number",
              "constraints": [],
              "required": True,
              "name": "length",
              "displayText": "Length"
            },
            {
              "type": "number",
              "constraints": [],
              "required": True,
              "name": "height",
              "displayText": "Height"
            }
          ],
          "required": False,
          "name": "floor",
          "displayText": "Floor"
        }
      ]
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
    }
  ]
},
  "response": {
    "create_site": [
        "executionId",
        "executionStatusUrl",
        "message"
        ],
    "delete_site": [
        "status",
        "message"
        ],
    "get_site": [
        "response"
        ],
    "get_site_count": [
        "response",
        "version"
    ],
    "update_site": [
        "result",
        "response",
        "status"
        ]
  }
}