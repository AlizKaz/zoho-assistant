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
    docs = f'\t\t"""{func["description"]}\n{argument_descriptions}\t\t"""'
    func_body = f"\t\tapi_url = self.zoho_books_api + \'/{func['api_address']}\'\n" \
        "\t\tdefault_params = {\n"\
        "\t\t}\n"\
        "\n"\
        "\t\tdefault_params.update(kwargs)\n" \
        "\t\theaders = {\n"\
        "\t\t\t'Authorization': f'Zoho-oauthtoken {self.access_token}'\n"\
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


def func_to_tool(func):
    """
    {
            "type": "function",
            "function": {
                "name": "book_tennis_court",
                "description": "book a tennis court with a partner at a specified data and time",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "partner_name": {
                            "type": "string",
                            "description": "Name of the partner",
                        },
                        "date": {
                            "type": "string",
                            # "enum": ["celsius", "fahrenheit"],
                            "description": "The date that we are going to play",
                        },
                        "time": {
                            "type": "string",
                            # "enum": ["6 AM", "7 AM", "8 AM", "9 AM", "10 AM", "11 AM", "12 PM", "1 PM", "2 PM", "3 PM",
                            #          "4 PM", "5 PM", "6 PM", "7 PM", "8 PM", "9 PM", "10 PM"],
                            "description": "The time that we are going to play. formatted as HH:MM:SS",
                        }
                    },
                    "required": ["partner_name", "date", "time"],
                },
            }
        }
    """

    parameters = {}
    required = []
    for argument in func['arguments']:
        parameters[argument['name']] = {'type': argument['data_type'], 'description': argument["description"]}
        if argument['required'].lower() == 'required':
            required.append(argument['name'])

    return {"type": "function",
            "function": {
                "name": func['name'].lower().replace(" ", "_"),
                "description": func['description'],
                "parameters": parameters,
                "required": required,
            }}
    pass


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
    return tools


generate_func()

# generate_tools()
