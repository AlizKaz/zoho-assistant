import time

from IPython.display import display


from app.backend.gpt import gpt_service


def eval(model: str, system_prompt: str, function_list, prompts_to_expected_tool_name):
    """
    Evaluate the performance of a model in selecting the correct function based on given prompts.

    Args:
        model (str): The name of the model to be evaluated.
        system_prompt (str): The system prompt to be used in the chat completion.
        function_list (list): A list of functions that the model can call.
        prompts_to_expected_tool_name (dict): A dictionary mapping prompts to their expected function names.

    Returns:
        None
    """

    prompts_to_actual = []
    latencies = []
    tokens_used = []

    for prompt, expected_function in prompts_to_expected_tool_name.items():
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ]

        start_time = time.time()
        completion, usage = gpt_service.get_chat_completion(
            model=model,
            messages=messages,
            seed=42,
            tools=function_list,
            temperature=0.0,
            tool_choice="required",
        )
        end_time = time.time()

        latency = (end_time - start_time) * 1000  # convert to milliseconds
        latencies.append(latency)

        prompts_to_actual.append(
            {prompt: completion.tool_calls[0].function.name})

        # Calculate tokens used
        tokens_used.append(usage.total_tokens)

    total_prompts = len(prompts_to_expected_tool_name)

    # Calculate the number of matches
    matches = sum(
        1
        for result in prompts_to_actual
        if list(result.values())[0]
        == prompts_to_expected_tool_name[list(result.keys())[0]]
    )
    match_percentage = (matches / total_prompts) * 100

    # Calculate average latency
    avg_latency = sum(latencies) / total_prompts
    # Calculate average tokens used
    avg_tokens_used = sum(tokens_used) / total_prompts

    # Create a DataFrame to store the results
    results_df = pd.DataFrame(columns=["Prompt", "Expected", "Match"])

    results_list = []
    for result in prompts_to_actual:
        prompt = list(result.keys())[0]
        actual_function = list(result.values())[0]
        expected_function = prompts_to_expected_tool_name[prompt]
        match = actual_function == expected_function
        results_list.append(
            {
                "Prompt": prompt,
                "Actual": actual_function,
                "Expected": expected_function,
                "Match": "Yes" if match else "No",
            }
        )
    results_df = pd.DataFrame(results_list)

    def style_rows(row):
        match = row["Match"]
        background_color = "red" if match == "No" else "white"
        return ["background-color: {}; color: black".format(background_color)] * len(
            row
        )

    styled_results_df = results_df.style.apply(style_rows, axis=1)

    # Display the DataFrame as a table
    display(styled_results_df)

    print(
        f"Number of matches: {matches} out of {total_prompts} ({match_percentage:.2f}%)"
    )
    print(f"Average latency per request: {avg_latency:.2f} ms")
    print(f"Average tokens used per request: {avg_tokens_used:.2f}")
