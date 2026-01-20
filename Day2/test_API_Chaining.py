import pytest
import requests
import json
from faker import Faker

base_url = 'https://gorest.co.in/public/v2/users'
token = 'd226f283c4a96d9c3a6d19f871d4c7cfc0894bd78febee7e4dc856acc9215b2d'
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
fake = Faker()
user_id = None

class Test_API_Chaining:
    def test_API_Chaining(self, create_fixture):
        global user_id
        # data = {
        #     'name': fake.name(),
        #     'gender': "Male",
        #     "email": fake.email(),
        #     "status": "inactive"
        #
        # }
        # resp = requests.post(base_url, headers=headers, json=data)
        # assert resp.status_code == 201, 'Wrong status code'
        # user_data = resp.json()
        # user_id = user_data['id']
        # print(resp.json())

        # OR create a fixture function that will create the user and return the ID in conftest.py
        user_id = create_fixture
        resp1 = requests.get(base_url + '/' + str(user_id), headers=headers)
        assert resp1.status_code == 200, 'Wrong status code'
        print(resp1.json())

        data2 = {
            'name': fake.name(),
            'gender': "Male",
            "email": fake.email(),
            "status": "inactive"

        }

        resp2 = requests.put(base_url + '/' + str(user_id), headers=headers, json=data2)
        assert resp2.status_code == 200, 'Wrong status code'
        print(resp2.json())

        requests.delete(base_url + '/' + str(user_id), headers=headers)

