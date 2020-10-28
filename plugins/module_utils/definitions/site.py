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
      "name": "site_id",
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
    ##### The schema for 'update_site' is incorrect in the specification
    "update_site": [
        "executionId",
        "executionStatusUrl",
        "message"
        ]
  }
}

from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ObjectExistenceCriteria

class SiteExistenceCriteria(ObjectExistenceCriteria):
    def __init__(self, dnac):
        super(SiteExistenceCriteria, self).__init__(
            dnac = dnac,
            get_function = "get_site",
            get_params = {},
            list_field = "response"
        )
        self.WARN_OBJECT_EXISTS = "Site already existed and was updated."

    def _object_is_equal(self, existing_object, candidate_params):

        if "site" in candidate_params.keys():
          site = candidate_params.get("site")
          if "area" in site.keys():
            name = site.get("area").get("name")
            parentName = site.get("area").get("parentName")
          elif "building" in site.keys():
            name = site.get("building").get("name")
            parentName = site.get("building").get("parentName")
          elif "floor" in site.keys():
            name = site.get("floor").get("name")
            parentName = site.get("floor").get("parentName")
          else:
            self.dnac.fail_json(msg="Missing 'area', 'building' or 'floor' param.")
          return existing_object["siteNameHierarchy"] == "{}/{}".format(parentName, name)
        else:
            self.dnac.fail_json(msg="Missing 'site' param.")

    def _transform_params(self, existing_object):

        existing_object["site_id"] = existing_object.get("id")
        del existing_object["id"]
        return existing_object
            
        