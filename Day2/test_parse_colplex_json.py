import requests
import pytest
import json

@pytest.fixture
def load_json(request):
    with open('./complex.JSON', 'r') as file:
        request.cls.json_resp = json.load(file)


class TestPraseComplex:

    def test_user_details(self):
        assert self.json_resp['status'] == 'success', "Wrong code"