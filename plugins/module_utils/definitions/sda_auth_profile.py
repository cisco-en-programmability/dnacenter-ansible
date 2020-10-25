module_definition = {
  "name": "sda_auth_profile",
  "family": "sda",
  "operations": {
      "post": ["add_default_authentication_profile"],
      "put": ["update_default_authentication_profile"],
      "delete": ["delete_default_authentication_profile"],
      "get": ["get_default_authentication_profile"]
  },
  "parameters": {
  "add_default_authentication_profile": [
    {
      "name": "headers",
      "type": "object"
    },
    {
      "name": "payload",
      "type": "array"
    }
  ],
  "delete_default_authentication_profile": [
    {
      "required": True,
      "name": "site_name_hierarchy",
      "type": "string"
    },
    {
      "name": "headers",
      "type": "object"
    }
  ],
  "get_default_authentication_profile": [
    {
      "required": True,
      "name": "site_name_hierarchy",
      "type": "string"
    },
    {
      "name": "headers",
      "type": "object"
    }
  ],
  "update_default_authentication_profile": [
    {
      "name": "headers",
      "type": "object"
    },
    {
      "name": "payload",
      "type": "array"
    }
  ]
}
}