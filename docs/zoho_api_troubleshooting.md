1. invalid_code
   - url: /oauth/v2/token
   - error: invalid_code 
   - solution: [Generate a new authorization code](https://www.zoho.com/accounts/protocol/oauth/self-client/authorization-code-flow.html) put in zoho_grant_token in .env 
     - Scope: 
2. JSON is not well formed
   - url: any url 
   - error: JSON is not well formed
   - code: 1038
   - solution: Zoho expects to see a json string in the body as opposed to string parameters separated by `&` character.
     - wrong: 
     ```python
     requests.post(api_url, data=payload, headers=headers)
     ```
     - correct: 
     ```python
     requests.post(api_url, json=payload, headers=headers)
     ```
     
