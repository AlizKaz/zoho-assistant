import json
from domain import domains


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


def func_to_tool(func: json) -> domains.Function:
    from domain import domains
    properties: list[domains.Property] = []
    all_args = func['arguments'] + func['query_params']
    for argument in all_args:
        property_ = get_property(argument)
        properties.append(property_)

    domains.Parameters('object', properties)

    function_name = func['name']

    parameters = domains.Parameters("object", properties)

    return domains.Function(function_name, func['description'], parameters)


def get_property(argument) -> domains.Property:
    json_schema_type = get_json_schema_type(argument['data_type'], name=argument['name'])
    required = False
    if argument['required'].lower() == 'required':
        required = True

    property_ = domains.Property(argument['name'], json_schema_type, argument['description'], required)
    if json_schema_type in ("array", "object"):

        if "sub_attributes" in argument:
            for sub_attr in argument["sub_attributes"]:
                sub_property = get_property(sub_attr)
                property_.add_item(sub_property)

    return property_


def generate_tools():
    f = open("./apis.json")

    funcs = json.load(f)

    print(f"function count: {len(funcs)}")
    tools: domains.Tools = domains.Tools()
    for func in funcs:
        function: domains.Function = func_to_tool(func)
        tools.add_tool(domains.Tool("function", function))
        # print(tool)
        # print("\n")
    # print(tools)
    tools.validate()
    print(json.dumps(tools.to_json(), indent=4))

    with open("invoice_tools.py", "w") as text_file:
        text_file.write("tools = ")
        json.dump(tools.to_json(), text_file, indent=4)
        text_file.write("\n")

    return tools


generate_func()

generate_tools()
