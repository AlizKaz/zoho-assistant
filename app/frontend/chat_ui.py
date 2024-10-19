import streamlit as st

from backend import assistant, zoho_auth
from backend.init import AppInit
from dotenv import load_dotenv

st.title("Zoho Books Assistant")

if "init_config" not in st.session_state:
    load_dotenv()
    st.session_state.init_config = True
    app_init = AppInit()
    try:
        print("init app...")
        app_init.init_app()
        st.session_state.app_init = app_init
        st.session_state.config = app_init.config
        st.session_state.messages = []
    except Exception as e:
        del st.session_state["init_config"]
        print("unable to init app")
        print(e)


def write_authorization_url():
    print("getting auth url...")
    return st.session_state.config.zoho_auth.initiate_server_side_login_to_zoho()


def init_login():
    print("getting auth url...")
    authorization_url = write_authorization_url()
    print(f"auth url: {authorization_url}")
    # st.write(authorization_url)
    st.markdown(f'<a href="{authorization_url}" target="_self">Proceed to Zoho Books Login</a>', unsafe_allow_html=True)


def after_init(st):
    if "authorization_code" not in st.session_state:
        print("auth code not found in session_state")
        query_params = st.query_params
        if 'code' in query_params:
            print("auth code found in query params params")
            code = query_params['code']
            print(f"auth code: {code}")
            st.session_state.authorization_code = code
            access_token = st.session_state.config.get_access_token(st.session_state.authorization_code)
            print(f"access_token:{access_token}")
            st.session_state.access_token = access_token
            if 'access_token' in st.session_state and st.session_state.access_token is not None:
                st.subheader("You are successfully logged in Zoho Books")
            else:
                st.button("Login to Zoho Books", type="secondary", on_click=init_login)
                st.subheader("You need to login")
        else:
            st.button("Login to Zoho Books", type="secondary", on_click=init_login)

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


if "init_config" in st.session_state:
    after_init(st)
