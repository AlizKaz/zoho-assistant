import json


def func_to_string(func):
    func['api_address'] = "invoices"
    function_name = func['name'].lower().replace(" ", "_")
    definition_line = f"def {function_name}(self, **kwargs):"
    argument_descriptions = ""
    for argument in func['arguments']:
        argument_description = f'name:{argument["name"]}, type:{argument["data_type"]}, ' \
                               f'required:{argument["required"]}. description:{argument["description"]}'

        argument_descriptions += "\t\t" + argument_description + "\n"
        if "sub_attributes" in argument:
            argument_descriptions += "\t\t\tsub attributes:" + "\n"
            for sub in argument['sub_attributes']:
                sub_attr_description = f'name:{sub["name"]}, type:{sub["data_type"]}, ' \
                                       f'required:{sub["required"]}. description:{sub["description"]}'

                argument_descriptions += f'\t\t\t{sub_attr_description}' + "\n"

    docs = f'\t\t"""{func["description"]}\n{argument_descriptions}\t\t"""'
    func_body = f"\t\tapi_url = self.zoho_books_api + \'/{func['api_address']}\'\n" \
                "\t\tdefault_params = {\n" \
                "\t\t}\n" \
                "\n" \
                "\t\tdefault_params.update(kwargs)\n" \
                "\t\theaders = {\n" \
                "\t\t\t'Authorization': f'Zoho-oauthtoken {self.access_token}'\n" \
                "\t\t}\n" \
                "\n" \
                "\t\treturn self.zoho_get_api_call(api_url, default_params, headers, 'invoices')\n"
    func = f"{definition_line}\n{docs}\n{func_body}"
    return func


def generate_func():
    init_method = "def __init__(self, zoho_books_api, access_token, session):\n" \
                  "\t\tself.access_token = access_token\n" \
                  "\t\tself.zoho_books_api = zoho_books_api\n" \
                  "\t\tself.session = session"

    zoho_post_api_call_method = "def zoho_post_api_call(self, api_url, payload, headers, data_key_name_in_response):\n" \
                                "\t\tprint(api_url)\n" \
                                "\t\tr = self.session.post(api_url, json=payload, headers=headers)\n" \
                                "\t\tif r.json()['code'] == 0:\n" \
                                "\t\t\treturn True, r.json()[data_key_name_in_response], None\n" \
                                "\t\telse:\n" \
                                "\t\t\treturn False, None, r.json()"

    zoho_get_api_call_method = "def zoho_get_api_call(self, api_url, params, headers, data_key_name_in_response):\n" \
                               "\t\tprint(api_url)\n" \
                               "\t\tr = self.session.get(api_url, params=params, headers=headers)\n" \
                               "\t\tif r.json()['code'] == 0:\n" \
                               "\t\t\treturn True, r.json()[data_key_name_in_response], None\n" \
                               "\t\telse:\n" \
                               "\t\t\treturn False, None, r.json()"

    class_methods = [init_method, zoho_get_api_call_method, zoho_post_api_call_method]

    f = open("./apis.json")

    funcs = json.load(f)

    for func in funcs:
        func['name'] = func['name'].replace('&', 'and').replace('.', '')

    print(f"function count: {len(funcs)}")
    for func in funcs:
        func_string = func_to_string(func)
        class_methods.append(func_string)
        print(func_string)
        print("\n")

    class_string = f"class InvoiceApi:\n"
    for method in class_methods:
        class_string += f"\t{method}\n\n"

    with open("invoice_api.py", "w") as text_file:
        text_file.write(class_string)


def get_json_schema_type(data_type, **kwargs):
    if data_type == "string":
        return "string"
    elif data_type == "integer" or data_type == "long":
        return "integer"
    elif data_type == "float" or data_type == "double":
        return "number"
    elif data_type == "array":
        return "array"
    elif data_type == "boolean":
        return "boolean"
    elif data_type == "object":
        return "object"
    else:
        raise Exception(f"unknown datatype: {data_type}, name:{kwargs.get('name')}")


def func_to_tool(func):
    properties = {}
    required = []

    for argument in func['arguments']:
        property = get_property(argument)
        properties.update(property)

        if argument['required'].lower() == 'required':
            required.append(argument['name'])

    parameters = {'type': 'object', 'properties': properties, 'required': required}

    function_name = func['name']
    # openai requires this
    function_name = clean_function_name(function_name)
    import re
    if not re.match(r"^[a-zA-Z0-9_-]+$", function_name):
        raise ValueError(f"Invalid characters in function_name: {function_name}")

    json_schema_for_function = {
        "name": function_name,
        "description": func['description'] if 'description' in func else "no description provided",
        "parameters": parameters,
        "required": required,
    }
    from jsonschema import Draft7Validator, exceptions

    try:
        Draft7Validator.check_schema(json_schema_for_function)
        print("Schema is valid!")
    except exceptions.SchemaError as e:
        print(f"Schema is invalid: {e.message}")

    return {"type": "function",
            "function": json_schema_for_function}
    pass


def clean_function_name(function_name):
    return (function_name
            .strip()
            .replace(" ", "_")
            .replace("'", "_")
            .replace(".", "_")
            .replace("&", "and")
            .lower())


def get_property(argument):
    json_schema_type = get_json_schema_type(argument['data_type'], name=argument['name'])
    property = {argument['name']: {'type': json_schema_type, 'description': None}}
    property_dict = property[argument['name']]
    property_dict['type'] = json_schema_type
    property_dict['description'] = argument["description"] if argument['description'] is not None \
        else 'no description provided'
    if json_schema_type == "array":
        property_dict["items"] = {
            "type": "string"
        }

        if "sub_attributes" in argument:
            property_dict["items"] = {
                "type": "object"
            }
            sub_property_dict = {}
            for sub_attr in argument["sub_attributes"]:
                sub_property = get_property(sub_attr)
                sub_property_dict.update(sub_property)
            property_dict["items"]["properties"] = sub_property_dict

    elif json_schema_type == "object":
        sub_property_dict = {}

        if "sub_attributes" in argument:
            for sub_attr in argument["sub_attributes"]:
                sub_property = get_property(sub_attr)
                sub_property_dict.update(sub_property)
        property_dict["properties"] = sub_property_dict
    return property


def generate_tools():
    f = open("./apis.json")

    funcs = json.load(f)

    print(f"function count: {len(funcs)}")
    tools = []
    for func in funcs:
        tool = func_to_tool(func)
        tools.append(tool)
        # print(tool)
        # print("\n")
    # print(tools)
    print(json.dumps(tools, indent=4))

    with open("invoice_tools.py", "w") as text_file:
        text_file.write("tools = ")
        json.dump(tools, text_file, indent=4)
        text_file.write("\n")

    return tools


generate_func()

generate_tools()
