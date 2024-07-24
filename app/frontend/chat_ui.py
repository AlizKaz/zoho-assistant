import streamlit as st

import sys

type(sys.path)

print("all paths in sys.path")
for path in sys.path:
    print(path)
print("---------")


from backend import assistant
from backend.init import AppInit


def init_streamlit():
    st.title("Zoho Books Assistant")

    if "init_config" not in st.session_state:
        st.session_state.init_config = True
        app_init = AppInit()
        app_init.init_app()
        st.session_state.config = app_init.config
        st.session_state.messages = []


def start():
    init_streamlit()
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = assistant.get_response(
                client=st.session_state.config.openai_client,
                system_message=st.session_state.config.gpt['system_message'],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ], tools=st.session_state.config.gpt['tools'], model=st.session_state.config.gpt['gpt_model']
            )

            st.write(response)

            st.session_state.messages.append({"role": "assistant", "content": response})
