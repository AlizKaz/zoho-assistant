# https://www.zoho.com/accounts/protocol/oauth/self-client/authorization-code-flow.html
import requests


class ZohoAuth:
    def __init__(self, client_id, client_secret, authorization_code, auth_store_filepath, accounts_server_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.authorization_code = authorization_code
        self.auth_store_filepath = auth_store_filepath
        self.accounts_server_url = accounts_server_url

    def get_access_and_refresh_token(self):
        api_url = f'{self.accounts_server_url}/oauth/v2/token'
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'authorization_code',
            'code': self.authorization_code,
        }

        # {
        # "access_token": "1000.8560a8d88bad047db58a2a2d4fbb7d55.0ca0b45142cef408de78d33d23fc6abc",
        # "refresh_token": "1000.c62f4a4a6f64c05730ba8266ff9e465a.456ae9c16d99a8b5d1d65cc16a923368",
        # "scope": "ZohoBooks.fullaccess.all",
        # "api_domain": "https://www.zohoapis.com",
        # "token_type": "Bearer",
        # "expires_in": 3600
        # }

        r = requests.post(api_url, data=params)
        if r.json().get('error'):
            error = r.json()['error']
            return False, error
        else:
            return True, r.json()

    def refresh_access_token(self, refresh_token):
        api_url = f'{self.accounts_server_url}/oauth/v2/token'
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
        }

        # {
        #     "access_token": "1000.875cf8ea310ae70c6fb26e25a5a48df0.be3bc88ab282cd58c6fd32f110c53c61",
        #     "api_domain": "https://www.zohoapis.in",
        #     "token_type": "Bearer",
        #     "expires_in": 3600
        # }

        r = requests.post(api_url, data=params)
        if r.json().get('error'):
            error = r.json()['error']
            return False, error
        else:
            return True, r.json()

    def load_access_token(self):
        import json

        # Opening JSON file
        f = open(self.auth_store_filepath)

        # returns JSON object as
        # a dictionary
        data = json.load(f)

        # Iterating through the json
        # list
        # for i in data['emp_details']:
        #     print(i)

        # Closing file
        f.close()

        return data

    def store_access_token(self, data):
        import json
        with open(self.auth_store_filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def refresh_and_save_access_token(self):
        current_auth_data = self.load_access_token()
        refresh_token = current_auth_data['refresh_token']

        success, data = self.refresh_access_token(refresh_token=refresh_token)
        if success:
            current_auth_data['access_token'] = data['access_token']
            self.store_access_token(current_auth_data)
            new_auth_data = self.load_access_token()
            return new_auth_data['access_token']
        else:
            raise Exception(f"unable to refresh access token due to {data}")

    def get_access_token_if_not_exists(self):
        try:
            data = self.load_access_token()
        except Exception as e:
            print(f"an exception occurred during loading access token {e}")
            data = None

        if data is None:
            success, data = self.get_access_and_refresh_token()
            if success:
                self.store_access_token(data)
            elif data == "invalid code":
                raise Exception(f"Unable to get access token. "
                                f"\nYou might need to [Generate a new authorization code]("
                                f"https://www.zoho.com/accounts/protocol/oauth/self-client/authorization-code-flow"
                                f".html) in Zoho API Console: https://api-console.zoho.com/"
                                f"\nerror: {data}")
            else:
                raise Exception(f"Unable to get access token. error: {data}")

        return data
