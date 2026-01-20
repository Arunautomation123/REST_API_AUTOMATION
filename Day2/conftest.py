import pytest
import requests
from faker import Faker
fake = Faker()

base_url = 'https://gorest.co.in/public/v2/users'
token = 'd226f283c4a96d9c3a6d19f871d4c7cfc0894bd78febee7e4dc856acc9215b2d'
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

@pytest.fixture(scope='session', autouse=True)
def create_fixture():
    data = {
        'name': fake.name(),
        'gender': "Male",
        "email": fake.email(),
        "status": "inactive"

    }
    resp = requests.post(base_url, headers=headers, json=data)
    assert resp.status_code == 201, 'Wrong status code'
    user_data = resp.json()
    user_id = user_data['id']

    return user_id