from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ObjectExistenceCriteria

module_definition = {
  "family": "tag",
  "name": "tag",
  "operations": {
    "delete": [
      "delete_tag"
    ],
    "get": [
      "get_tag",
      "get_tag_by_id",
      "get_tag_count"
    ],
    "post": [
      "create_tag"
    ],
    "put": [
      "update_tag"
    ]
  },
  "parameters": {
    "create_tag": [
      {
        "name": "description",
        "type": "string"
      },
      {
        "name": "dynamic_rules",
        "type": "array"
      },
      {
        "name": "id",
        "type": "string"
      },
      {
        "name": "instanceTenantId",
        "type": "string"
      },
      {
        "name": "name",
        "type": "string"
      },
      {
        "name": "systemTag",
        "type": "boolean"
      }
    ],
    "delete_tag": [
      {
        "name": "id",
        "required": True,
        "type": "string"
      }
    ],
    "get_tag": [
      {
        "name": "additional_info_attributes",
        "required": False,
        "type": "string"
      },
      {
        "name": "additional_info_name_space",
        "required": False,
        "type": "string"
      },
      {
        "name": "field",
        "required": False,
        "type": "string"
      },
      {
        "name": "level",
        "required": False,
        "type": "string"
      },
      {
        "name": "limit",
        "required": False,
        "type": "string"
      },
      {
        "name": "name",
        "required": False,
        "type": "string"
      },
      {
        "name": "offset",
        "required": False,
        "type": "string"
      },
      {
        "name": "order",
        "required": False,
        "type": "string"
      },
      {
        "name": "size",
        "required": False,
        "type": "string"
      },
      {
        "name": "sort_by",
        "required": False,
        "type": "string"
      },
      {
        "name": "system_tag",
        "required": False,
        "type": "string"
      }
    ],
    "get_tag_by_id": [
      {
        "name": "id",
        "required": True,
        "type": "string"
      }
    ],
    "get_tag_count": [
      {
        "name": "attribute_name",
        "required": False,
        "type": "string"
      },
      {
        "name": "level",
        "required": False,
        "type": "string"
      },
      {
        "name": "name",
        "required": False,
        "type": "string"
      },
      {
        "name": "name_space",
        "required": False,
        "type": "string"
      },
      {
        "name": "size",
        "required": False,
        "type": "string"
      },
      {
        "name": "system_tag",
        "required": False,
        "type": "string"
      },
      {
        "name": "count",
        "required": True,
        "type": "boolean"
      }
    ],
    "update_tag": [
      {
        "name": "description",
        "type": "string"
      },
      {
        "name": "dynamicRules",
        "type": "array"
      },
      {
        "name": "id",
        "type": "string"
      },
      {
        "name": "instanceTenantId",
        "type": "string"
      },
      {
        "name": "name",
        "type": "string"
      },
      {
        "name": "systemTag",
        "type": "boolean"
      }
    ]
  },
  "response": {
    "create_tag": [
        "response",
        "version"
    ],
    "delete_tag": [
        "response",
        "version"
    ],
    "get_tag": [
        "response",
        "version"
    ],
    "get_tag_by_id": [
        "response",
        "version"
    ],
    "get_tag_count": [
        "response",
        "version"
    ],
    "update_tag": [
        "response",
        "version"
    ],
  }
}

class TagExistenceCriteria(ObjectExistenceCriteria):
    def __init__(self, dnac):
        super(TagExistenceCriteria, self).__init__(
            dnac = dnac,
            get_function = "get_tag",
            get_params = {},
            list_field = "response"
        )
        self.WARN_OBJECT_EXISTS = "Tag already existed and was updated."
        self.ERR_MISSING_PARAM = "Missing 'name' parameter"

    def _object_is_equal(self, existing_object, candidate_params):
        if "name" in candidate_params.keys():
            return existing_object["name"] == candidate_params["name"]
        else:
            self.dnac.fail_json(msg=self.ERR_MISSING_PARAM)
            
        
