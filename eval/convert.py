from pydantic import BaseModel, create_model
from typing import Any, Dict, Type


def create_basemodel_from_function(function_def: Dict[str, Any], model_name: str) -> Type[BaseModel]:
    """
    Converts an OpenAI FunctionDefinition instance to a Pydantic BaseModel.

    Args:
        function_def (Dict[str, Any]): The function definition schema (inputs/outputs).
        model_name (str): The name of the BaseModel class to create.

    Returns:
        Type[BaseModel]: A dynamically created Pydantic BaseModel class.
    """
    # Extract properties and required fields from the schema
    schema = function_def.get("parameters", {})
    properties = schema.get("properties", {})
    required = schema.get("required", [])

    # Build the Pydantic model fields
    fields = {}
    for field_name, field_info in properties.items():
        field_type = map_openai_schema_to_pydantic(field_info)
        default = ... if field_name in required else None  # Required fields use `...`
        fields[field_name] = (field_type, default)

    # Create the Pydantic model dynamically
    return create_model(model_name, **fields)


def map_openai_schema_to_pydantic(field_info: Dict[str, Any]) -> Any:
    """
    Maps OpenAI's JSON schema types to Pydantic types.

    Args:
        field_info (Dict[str, Any]): Field definition in JSON Schema format.

    Returns:
        Any: Corresponding Pydantic type.
    """
    type_map = {
        "string": str,
        "integer": int,
        "number": float,
        "boolean": bool,
        "array": list,
        "object": dict,
    }

    field_type = field_info.get("type", "string")  # Default to string
    if field_type == "array":
        # Handle array types (e.g., List[str])
        items = field_info.get("items", {})
        item_type = map_openai_schema_to_pydantic(items)
        return list[item_type]
    elif field_type == "object":
        # Handle nested objects recursively
        properties = field_info.get("properties", {})
        nested_name = field_info.get("title", "NestedObject")
        return create_basemodel_from_function({"parameters": {"properties": properties}}, nested_name)

    return type_map.get(field_type, Any)


# Example usage
function_definition = {
    "parameters": {
        "type": "object",
        "properties": {
            "query": {"type": "string"},
            "limit": {"type": "integer", "default": 10},
        },
        "required": ["query"],
    }
}

import invoice_tools

function_definition = invoice_tools.tools[0]["function"]

GeneratedModel = create_basemodel_from_function(function_definition, "SearchRequest")

# Instantiate the generated BaseModel
example_instance = GeneratedModel(customer_id="CUST-100200")
print(example_instance)



