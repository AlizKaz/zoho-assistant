import json


def validate_function_json_schema(function_json_schema):
    from jsonschema import Draft7Validator, exceptions
    try:
        Draft7Validator.check_schema(function_json_schema)
        print("Schema is valid!")
    except exceptions.SchemaError as e:
        print(f"Schema is invalid: {e.message}")
        raise e


def clean_function_name(function_name):
    return (function_name
            .strip()
            .replace(" ", "_")
            .replace("'", "_")
            .replace(".", "_")
            .replace("&", "and")
            .lower())


class Property:
    def __init__(self, name: str, property_type: str, description: str or None, required: bool):
        self.name = name
        self.property_type = property_type
        self.description = description
        self.required = required
        self.items: list['Property'] = []

    def add_item(self, item: 'Property'):
        self.items.append(item)

    def to_json(self) -> json:
        description = self.get_clean_description()
        if self.property_type not in ("array", "object"):
            return {self.name: {"type": self.property_type, "description": description}}
        else:
            if len(self.items) <= 0:
                items_json = {self.name: {"type": self.property_type,
                                          "description": description,
                                          "items": {"type": "string"}
                                          }
                              }
                return items_json
            else:
                items_json = self.get_items_json()
                if self.property_type in "array":
                    return {self.name: {"type": self.property_type,
                                        "description": description,
                                        "items": items_json}
                            }
                elif self.property_type in "object":
                    properties = self.get_properties()
                    return {self.name: {"type": self.property_type,
                                        "description": description,
                                        "properties": properties}}

    def get_clean_description(self):
        return self.description if self.description is not None else "no description provided"

    def get_items_json(self) -> json:
        properties = self.get_properties()
        items: dict = {"type": "object", "properties": properties}
        return items

    def get_properties(self):
        properties = {}
        for _property in self.items:
            properties.update(_property.to_json())
        return properties


class Parameters:
    def __init__(self, parameters_type: str, properties: list[Property]):
        self.parameters_type = parameters_type
        self.properties = properties

    def get_required_parameters(self) -> list[str]:
        required = []
        for _property in self.properties:
            if _property.required:
                required.append(_property.name)
        return required

    def to_json(self):
        return {"type": self.parameters_type, "properties": self.properties_to_json()}

    def properties_to_json(self):
        properties_dict = {}
        for _property in self.properties:
            properties_dict.update(_property.to_json())
        return properties_dict


class Function:
    def __init__(self, name: str, description: str, parameters: Parameters):
        name = clean_function_name(name)
        import re
        if not re.match(r"^[a-zA-Z0-9_-]+$", name):
            raise ValueError(f"Invalid characters in function_name: {name}")
        self.name = name
        self.description = description
        self.parameters = parameters
        self.required_properties = []
        for _prop in self.parameters.properties:
            if _prop.required:
                self.required_properties.append(_prop.name)

    def to_json(self):
        json_ = {"name": self.name, "description": self.description, "parameters": self.parameters.to_json()}
        if len(self.required_properties) > 0:
            json_["required"] = self.required_properties
        return json_


class Tool:
    def __init__(self, tool_type: str, function: Function):
        valid_tool_types = "function"
        if tool_type not in valid_tool_types:
            raise Exception(f"invalid tool type: {tool_type}, valid types: {valid_tool_types}")
        self.tool_type = tool_type
        self.function = function

    def to_json(self):
        return {"type": self.tool_type, "function": self.function.to_json()}


class Tools:

    def __init__(self):
        self.tools: list[Tool] = []

    def add_tool(self, tool: Tool):
        self.tools.append(tool)

    def to_json(self) -> json:
        tools_list = []
        for tool in self.tools:
            tools_list.append(tool.to_json())

        return tools_list

    def validate(self):
        for tool in self.tools:
            print(f"validating function:{tool.function.name}")
            validate_function_json_schema(tool.function.to_json())
