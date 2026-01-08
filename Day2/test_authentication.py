import requests
from requests.auth import HTTPDigestAuth
import pytest
access_token = None

class TestAuthentication:
    def test_basic_auth(self):
        resp = requests.get("https://postman-echo.com/basic-auth", auth=("postman", "password"))
        assert resp.status_code == 200, "Wrong code"
        data = resp.json()
        print(data)
        assert data.get("authenticated") == True, "No authentication"

    def test_digest_auth(self):
        resp = requests.get("https://postman-echo.com/digest-auth", auth=HTTPDigestAuth("postman", "password"))
        assert resp.status_code == 200, "Wrong code"
        data = resp.json()
        print(data)
        assert data.get("authenticated") == True, "No authentication"

    def test_bearer_token_auth(self):
        # go to github --> settings --> developer settings --> create token --> generate token
        bearer_token = ''
        headers = {"Authorization": f"Bearer {bearer_token}"}
        resp = requests.get('https://api.github.com/user/repos', headers=headers)
        assert resp.status_code == 200, "Wrong code"
        data = resp.json()
        print(data)

    def test_api_key_auth(self):
        params = {'q': 'Delhi', 'appid': 'bc33c573ae0211318a9b383edb2340bd'}
        resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        assert resp.status_code == 200, "Wrong code"
        data = resp.json()
        print(data)

@pytest.fixture(scope='session', autouse=True)
def generate_token():
    global access_token
    client_id = ''
    client_secret = ''
    token_url = ''
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    form_data = {'grant_type': 'client_credentials',
                 "client_id": client_id,
                 "client_secret": client_secret}

    resp = requests.post(token_url, data=form_data, headers=headers)
    assert resp.status_code == 200, "Wrong code"
    data = resp.json()
    return data['access_token']

generate_token()
# get ID from spotify artist
# https://open.spotify.com/artist/4YRxDV8wJFPHPTeXepOstw?si=n2x9-uScRlypOxfP4aZIgA
class TestOauth2API:
    def get_singer_top_tracks(self):
        headers = {"Authorization": f"Bearer {access_token}"}
        resp = requests.get(f'https://api.spotify.com/v1/artists/4YRxDV8wJFPHPTeXepOstw/top-tracks', headers=headers, params={'market':'US'})
        assert resp.status_code == 200, "Wrong code"
        print(resp.json())