from typing import Any, Dict, Callable
from pydantic import BaseModel, create_model
from langchain_core.tools.structured import StructuredTool


def create_structured_tool_from_function(
        function_def: Dict[str, Any],
        tool_logic: Callable,
) -> StructuredTool:
    """
    Converts an OpenAI FunctionDefinition into a langchain_core.tools.structured.StructuredTool.

    Args:
        function_def (Dict[str, Any]): The function definition schema (parameters).
        tool_logic (Callable): The function to be executed by the tool.
        tool_name (str): The name of the tool.

    Returns:
        StructuredTool: A LangChain StructuredTool instance.
    """
    tool_name = function_def.get("name")
    # Extract schema
    schema = function_def.get("parameters", {})

    # Dynamically create a Pydantic BaseModel to represent the input schema
    input_model = create_basemodel_from_schema(schema, f"{tool_name}Input")

    # Create the StructuredTool
    return StructuredTool(
        name=tool_name,
        description=function_def.get("description", "No description provided."),
        func=tool_logic,
        args_schema=input_model
    )


def create_basemodel_from_schema(schema: Dict[str, Any], model_name: str) -> BaseModel:
    """
    Creates a Pydantic BaseModel from a JSON schema.

    Args:
        schema (Dict[str, Any]): JSON schema defining the model.
        model_name (str): Name of the BaseModel.

    Returns:
        BaseModel: A dynamically generated Pydantic model.
    """
    properties = schema.get("properties", {})
    required = schema.get("required", [])

    fields = {}
    for field_name, field_info in properties.items():
        field_type = map_openai_schema_to_pydantic(field_info)
        default = ... if field_name in required else None
        fields[field_name] = (field_type, default)

    return create_model(model_name, **fields)


def map_openai_schema_to_pydantic(field_info: Dict[str, Any]) -> Any:
    """
    Maps OpenAI JSON schema types to Pydantic types.

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
        items = field_info.get("items", {})
        item_type = map_openai_schema_to_pydantic(items)
        return list[item_type]
    elif field_type == "object":
        properties = field_info.get("properties", {})
        nested_name = field_info.get("title", "NestedObject")
        return create_basemodel_from_schema({"properties": properties}, nested_name)

    return type_map.get(field_type, Any)


# Example usage
# function_definition = {
#     "name": "search_tool",
#     "description": "A tool for performing search operations.",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "query": {"type": "string"},
#             "limit": {"type": "integer", "default": 10},
#         },
#         "required": ["query"],
#     }
# }

import invoice_tools

function_definition = invoice_tools.tools[0]["function"]


# Example logic for the tool
def search_logic(query: str, limit: int = 10) -> str:
    return f"Searching for '{query}' with a limit of {limit} results."


def create_an_invoice(customer_id: str, currency_id: str):
    return f"Creating an invoice for customer:'{customer_id} with currency:{currency_id}"


# Generate the StructuredTool
structured_tool = create_structured_tool_from_function(function_definition, create_an_invoice)

# Output the tool's details
print(structured_tool.name)  # Output: SearchTool
print(structured_tool.to_json())
# print(structured_tool.args_schema.model_dump_json(indent=2))  # Output: JSON Schema of the input model
print(structured_tool.func(customer_id="Customer-100200", currency_id=5))  # Call the tool logic
