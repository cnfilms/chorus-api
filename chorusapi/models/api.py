import datetime

import requests

from chorusapi.utils.chorus_utils import base_64_encode
from chorusapi.constants.api_constant import AUTH_SANDBOX_URL, AUTH_PRODUCTION_URL, API_SANDBOX_URL, API_PRODUCTION_URL
from chorusapi.exceptions.exception import ChorusApiException


class API:
    def __init__(self, client_id, client_secret, tech_username=None, tech_password=None, sandbox=True):
        """
        :param client_id:
        :param client_secret:
        :param tech_username:
        :param tech_password:
        :param sandbox:
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.tech_username = tech_username
        self.tech_password = tech_password
        self.sandbox = sandbox
        self.auth_url = AUTH_SANDBOX_URL if self.sandbox else AUTH_PRODUCTION_URL
        self.api_url = API_SANDBOX_URL if self.sandbox else API_PRODUCTION_URL
        self.grant_type = "client_credentials"
        self.scope = "openid"
        self.token = None
        self._token_date_expiration = None

    def _token_has_expire(self):
        if self.token and self._token_date_expiration:
            return self._token_date_expiration < datetime.datetime.now()

        return True

    def auth(self):
        """
        :return: {API}
        """
        if self._token_has_expire():
            headers = {
                'content-type': 'application/x-www-form-urlencoded',
            }

            data = f'grant_type={self.grant_type}&client_id={self.client_id}&client_secret={self.client_secret}&scope={self.scope}'
            req = requests.post(self.auth_url, headers=headers, data=data)
            if req.status_code != 200:
                raise ChorusApiException(req.text)

            json_response = req.json()

            self.token = json_response['access_token']
            self._token_date_expiration = datetime.datetime.now() + datetime.timedelta(
                seconds=json_response.get('expires_in', 0))
        return self

    def _make_headers(self):
        cpro_account = base_64_encode(f"{self.tech_username}:{self.tech_password}")

        if not self.token:
            raise ChorusApiException("Pas de jeton token, veuillez appeler la méthode auth() pour générer un token")

        return {
            'cpro-account': f"{cpro_account}",
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

    def _make_error_msg(self, req):
        return f"Code: {req.status_code} Reason: {req.reason}  Message: {req.text}"

    def get_token(self):
        return self.token
