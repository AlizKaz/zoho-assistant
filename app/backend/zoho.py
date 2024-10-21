class Invoice:
    def __init__(self, zoho_books_api, access_token, session):
        self.access_token = access_token
        self.zoho_books_api = zoho_books_api
        self.session = session

    def list_invoices(self, params):
        api_url = self.zoho_books_api + "/invoices"

        default_params = {
        }

        default_params.update(params)
        headers = {
            'Authorization': f'Zoho-oauthtoken {self.access_token}'
        }

        return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')

    def create_invoice(self, params):
        api_url = self.zoho_books_api + "/invoices"

        default_params = {

        }
        default_params.update(params)

        headers = {
            'Authorization': f'Zoho-oauthtoken {self.access_token}',
            'content-type': 'application/json',
        }

        return self.zoho_post_api_call(api_url, default_params, headers, 'invoice')

    def zoho_post_api_call(self, api_url, payload, headers, data_key_name_in_response):
        print(api_url)
        r = self.session.post(api_url, json=payload, headers=headers)
        if r.json()['code'] == 0:
            return True, r.json()[data_key_name_in_response], None
        else:
            return False, None, r.json()

    def zoho_get_api_call(self, api_url, params, headers, data_key_name_in_response):
        print(api_url)
        r = self.session.get(api_url, params=params, headers=headers)
        if r.json()['code'] == 0:
            return True, r.json()[data_key_name_in_response], None
        else:
            return False, None, r.json()
