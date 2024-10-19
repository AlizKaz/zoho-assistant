import logging
import os
from http.client import HTTPConnection

import requests
from dotenv import load_dotenv
from openai import OpenAI

import zoho_auth
from app.backend import zoho


def debug_requests_on():
    """Switches on logging of the requests' module."""
    HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


def auth_hook_factory(*factory_args, **factory_kwargs):
    def auth_hook(response, *args, **kwargs):
        if response.status_code == 401:
            zoho_auth_obj = factory_kwargs.get('zoho_auth')
            session = factory_kwargs.get('session')
            print(f'getting 401 response code. trying to refresh access token')
            # Refresh token
            new_access_token = zoho_auth_obj.refresh_and_save_access_token()
            # Update session headers with new token
            response.request.headers['Authorization'] = f'Zoho-oauthtoken {new_access_token}'
            # Retry original request
            return session.send(response.request)
    return auth_hook


class AppInit:

    def __init__(self):
        self.config = None

    def init_app(self):
        load_dotenv()
        if os.environ.get("debug_request") == 'on':
            debug_requests_on()

        self.config = Config()
        self.config.init_zoho_auth()
        self.config.init_openai_client()


class Config:
    def __init__(self):
        self.openai_client = None
        self.invoice = None
        self.accounts_server_url = None
        self.zoho_auth = None

    def init_zoho_auth(self):
        self.zoho_auth = zoho_auth.ZohoAuth(
            client_id=os.environ.get("zoho_client_id"),
            client_secret=os.environ.get("zoho_client_secret"),
            authorization_code=os.environ.get("zoho_authorization_code"),
            auth_store_filepath=os.environ.get("auth_store_filepath"),
            accounts_server_url=os.environ.get('zoho_accounts_server_url'))

        session = requests.session()
        session.hooks['response'].append(auth_hook_factory(zoho_auth=self.zoho_auth, session=session))

        access_token = self.zoho_auth.get_access_token_if_not_exists()['access_token']

        self.invoice = zoho.Invoice(os.environ.get("zoho_books_api_server_url"), access_token, session)

    def init_openai_client(self):
        if self.openai_client is None:
            # Define OpenAI api_key
            api_key = os.environ.get('OPENAI_API_KEY_ZOHO_ASSISTANT_PROJECT')
            client = OpenAI(api_key=api_key)
            self.openai_client = client
            return self.openai_client
        else:
            return self.openai_client

