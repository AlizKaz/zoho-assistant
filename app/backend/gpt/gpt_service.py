import os

from openai import OpenAI
from tenacity import retry, wait_random_exponential, stop_after_attempt


@retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(3))
def chat_completion_request(client, system_message, messages, model, tools=None, tool_choice=None):
    try:
        messages = [{"role": "system", "content": system_message}] + messages
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            tool_choice=tool_choice,
        )
        return response
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e


def init_client():
    # Define OpenAI api_key
    api_key = os.environ.get('OPENAI_API_KEY_BOOKING_PROJECT')
    client = OpenAI(api_key=api_key)
    return client
