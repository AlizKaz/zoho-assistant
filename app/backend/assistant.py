import json

from app.backend.gpt import gpt_service


def get_response(client, system_message, messages, tools, gpt_model):
    chat_response = gpt_service.chat_completion_request(
        client=client,
        system_message=system_message,
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in messages
        ], tools=tools, tool_choice="auto", model=gpt_model
    )
    response = chat_response.choices[0].message

    if response.content:
        result = response.content
        return result
    elif response.tool_calls:
        print_function(response)
        # return zoho_books_service.process_gpt_tool_call(response)
    else:
        return "unable to process the chat"


def print_function(response):
    function = response.tool_calls[0].function
    function_call = function.name
    function_call += "("
    arguments = json.loads(function.arguments)

    print(f"args: ${function.arguments}")

    for arg_name, arg_value in arguments.items():
        function_call += arg_name + "=" + str(arg_value) + ","

    function_call += ")"
    print(f"function_call : {function_call}")

