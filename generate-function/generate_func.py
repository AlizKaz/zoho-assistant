import json


def func_to_string(func):
    function_name = func['name'].lower().replace(" ", "_")
    definition_line = f"def {function_name}(**kwargs):"
    description = f'"""{func["description"]}"""'
    argument_descriptions = ""
    for argument in func['arguments']:
        argument_description = f'\t"""name:{argument["name"]}, type:{argument["data_type"]}, ' \
                                f'required:{argument["required"]}. description:{argument["description"]}"""'
        argument_descriptions += argument_description + "\n"
    func = f"{definition_line}\n\t{description}\n{argument_descriptions}\n\tpass"
    return func


def generate_func():
    f = open("./apis.json")

    funcs = json.load(f)

    print(f"function count: {len(funcs)}")
    for func in funcs:
        func_string = func_to_string(func)
        print(func_string)
        print("\n")


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
                "name": func['name'],
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


# generate_func()

generate_tools()
