# https://www.zoho.com/accounts/protocol/oauth/self-client/authorization-code-flow.html
import os
import requests
from dotenv import load_dotenv

load_dotenv()

accounts_server_url = os.environ.get('zoho_accounts_server_url')


def get_access_and_refresh_token(client_id, client_secret, authorization_code):
    api_url = f'{accounts_server_url}/oauth/v2/token'
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'authorization_code',
        'code': authorization_code,
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


def refresh_access_token(client_id, client_secret, refresh_token):
    api_url = f'{accounts_server_url}/oauth/v2/token'
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
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


def load_access_token(auth_store_filepath):
    import json

    # Opening JSON file
    f = open(auth_store_filepath)

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


def store_access_token(auth_store_filepath, data):
    import json
    with open(auth_store_filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_access_token_if_not_exists():
    try:
        data = load_access_token(os.environ.get('auth_store_filepath'))
    except Exception as e:
        print(f"an exception occurred during loading access token {e}")
        data = None

    if data is None:
        success, data = get_access_and_refresh_token(client_id=os.environ.get('zoho_client_id'),
                                                     client_secret=os.environ.get('zoho_client_secret'),
                                                     authorization_code=os.environ.get('zoho_grant_token'))
        if success:
            store_access_token(os.environ.get('auth_store_filepath'), data)
        else:
            raise Exception(f"unable to get access token. error: {data}")

    return data


def refresh_and_save_access_token():
    current_auth_data = load_access_token(os.environ.get('auth_store_filepath'))
    refresh_token = current_auth_data['refresh_token']

    success, data = refresh_access_token(client_id=os.environ.get('zoho_client_id'),
                                         client_secret=os.environ.get('zoho_client_secret'),
                                         refresh_token=refresh_token)
    if success:
        current_auth_data['access_token'] = data['access_token']
        store_access_token(os.environ.get('auth_store_filepath'), current_auth_data)
        new_auth_data = load_access_token(os.environ.get('auth_store_filepath'))
        return new_auth_data['access_token']
    else:
        raise Exception(f"unable to refresh access token due to {data}")


import json

auth_data = get_access_token_if_not_exists()
# print(json.dumps(data, indent=4))
# refresh_and_save_access_token()
