module_definition = {
  "name": "task",
  "family": "task",
  "operations": {
      "get": [
        "get_task_by_id",
        "get_task_by_operationid",
        "get_task_count",
        "get_tasks",
        "get_task_tree"
        ]
  },
  "parameters": {
  "get_task_by_id": [
    {
      "name": "task_id",
      "required": True,
      "type": "TaskId"
    },
    {
      "name": "headers",
      "type": "object"
    }
  ],
  "get_task_by_operationid": [
    {
      "name": "limit",
      "required": True,
      "sdk_name": "limit",
      "type": "integer"
    },
    {
      "name": "offset",
      "required": True,
      "sdk_name": "offset",
      "type": "integer"
    },
    {
      "name": "operationId",
      "required": True,
      "sdk_name": "operation_id",
      "type": "string"
    },
    {
      "name": "headers",
      "type": "object"
    }
  ],
  "get_task_count": [
    {
      "name": "data",
      "required": False,
      "sdk_name": "data",
      "type": "string"
    },
    {
      "name": "endTime",
      "required": False,
      "sdk_name": "end_time",
      "type": "string"
    },
    {
      "name": "errorCode",
      "required": False,
      "sdk_name": "error_code",
      "type": "string"
    },
    {
      "name": "failureReason",
      "required": False,
      "sdk_name": "failure_reason",
      "type": "string"
    },
    {
      "name": "isError",
      "required": False,
      "sdk_name": "is_error",
      "type": "string"
    },
    {
      "name": "parentId",
      "required": False,
      "sdk_name": "parent_id",
      "type": "string"
    },
    {
      "name": "progress",
      "required": False,
      "sdk_name": "progress",
      "type": "string"
    },
    {
      "name": "serviceType",
      "required": False,
      "sdk_name": "service_type",
      "type": "string"
    },
    {
      "name": "startTime",
      "required": False,
      "sdk_name": "start_time",
      "type": "string"
    },
    {
      "name": "username",
      "required": False,
      "sdk_name": "username",
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
  "get_tasks": [
    {
      "name": "data",
      "required": False,
      "sdk_name": "data",
      "type": "string"
    },
    {
      "name": "endTime",
      "required": False,
      "sdk_name": "end_time",
      "type": "string"
    },
    {
      "name": "errorCode",
      "required": False,
      "sdk_name": "error_code",
      "type": "string"
    },
    {
      "name": "failureReason",
      "required": False,
      "sdk_name": "failure_reason",
      "type": "string"
    },
    {
      "name": "isError",
      "required": False,
      "sdk_name": "is_error",
      "type": "string"
    },
    {
      "name": "limit",
      "required": False,
      "sdk_name": "limit",
      "type": "string"
    },
    {
      "name": "offset",
      "required": False,
      "sdk_name": "offset",
      "type": "string"
    },
    {
      "name": "order",
      "required": False,
      "sdk_name": "order",
      "type": "string"
    },
    {
      "name": "parentId",
      "required": False,
      "sdk_name": "parent_id",
      "type": "string"
    },
    {
      "name": "progress",
      "required": False,
      "sdk_name": "progress",
      "type": "string"
    },
    {
      "name": "serviceType",
      "required": False,
      "sdk_name": "service_type",
      "type": "string"
    },
    {
      "name": "sortBy",
      "required": False,
      "sdk_name": "sort_by",
      "type": "string"
    },
    {
      "name": "startTime",
      "required": False,
      "sdk_name": "start_time",
      "type": "string"
    },
    {
      "name": "username",
      "required": False,
      "sdk_name": "username",
      "type": "string"
    },
    {
      "name": "headers",
      "type": "object"
    }
  ],
  "get_task_tree": [
    {
      "name": "task_id",
      "required": True,
      "type": "string"
    },
      {
        "name": "tree",
        "type": "boolean",
        "required": True
      },
    {
      "name": "headers",
      "type": "object"
    }
  ]
}
}