import os

import requests

from app.backend import zoho_auth

auth_data = zoho_auth.auth_data
access_token = auth_data['access_token']


def auth_hook(response, *args, **kwargs):
    if response.status_code == 401:
        print(f'getting 401 response code. trying to refresh access token')
        # Refresh token
        new_access_token = zoho_auth.refresh_and_save_access_token()
        # Update session headers with new token
        response.request.headers['Authorization'] = f'Zoho-oauthtoken {new_access_token}'
        # Retry original request
        return session.send(response.request)


session = requests.Session()
session.hooks['response'].append(auth_hook)


def list_invoices(access_token, params):
    api_url = os.environ.get('zoho_books_api') + "/invoices"

    default_params = {
    }

    default_params.update(params)

    headers = {
        'Authorization': f'Zoho-oauthtoken {access_token}'
    }

    return zoho_get_api_call(api_url, default_params, headers)


def zoho_get_api_call(api_url, params, headers):
    r = session.get(api_url, params=params, headers=headers)
    if r.json()['message'] == 'success':
        return True, r.json()['invoices'], None
    else:
        return False, None, r.json()
