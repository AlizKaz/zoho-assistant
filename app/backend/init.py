import logging
import os
from http.client import HTTPConnection

import requests
from openai import OpenAI

from backend import zoho_auth
from backend import zoho
from backend.zoho_tools import invoice_tools


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
        # load_dotenv()
        if os.environ.get("debug_request") == 'on':
            debug_requests_on()
            print_system_path()

        self.config = Config()
        self.config.init_zoho_auth()
        self.config.init_openai_client()
        self.config.init_gpt_properties()

    @staticmethod
    def print_system_path(self):
        import sys
        type(sys.path)

        print("all paths in sys.path")
        for path in sys.path:
            print(path)
        print("---------")


class Config:
    def __init__(self):
        self.openai_client = None
        self.gpt = None
        self.invoice = None
        self.accounts_server_url = None
        self.zoho_auth = None

    def init_zoho_auth(self):
        auth_store_location = os.environ.get("auth_store_location")
        auth_store_filename_prefix = os.environ.get("auth_store_filename_prefix")
        zoho_oauth_app_client_type = os.environ.get('zoho_app_client_type')
        auth_store_filepath = f"{auth_store_location}/{auth_store_filename_prefix}_{zoho_oauth_app_client_type}.txt"
        self.zoho_auth = zoho_auth.ZohoAuth(
            client_id=os.environ.get("zoho_client_id"),
            client_secret=os.environ.get("zoho_client_secret"),
            auth_store_filepath=auth_store_filepath,
            accounts_server_url=os.environ.get('zoho_accounts_server_url'),
            client_type=zoho_oauth_app_client_type)

    def get_access_token(self, authorization_code):
        if self.zoho_auth.client_type == "Self-Client":
            authorization_code = os.environ.get("zoho_authorization_code")
            print(f"trying to get access token with auth_code:{authorization_code}")
            access_token = self.zoho_auth.get_access_token_if_not_exists(authorization_code)['access_token']
            return access_token
        else:
            access_token = self.zoho_auth.get_access_token_if_not_exists(authorization_code)['access_token']
            return access_token

    def init_zoho_services(self, access_token):
        if access_token is None:
            raise Exception("please login first")

        session = requests.session()
        session.hooks['response'].append(auth_hook_factory(zoho_auth=self.zoho_auth, session=session))

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

    def init_gpt_properties(self):
        if self.gpt is None:
            self.gpt = {'system_message': "", 'tools': self.get_tools(),
                        'gpt_model': os.environ.get('zoho_assistant_openai_model')}
        else:
            return self.gpt

    @staticmethod
    def get_tools():
        tools = [
            invoice_tools.search_invoices,
            invoice_tools.create_an_invoice
        ]

        return tools
