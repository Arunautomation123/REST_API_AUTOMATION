import requests

HEADER = {'Content-Type': 'application/json',
          "x-api-key": "regres-free-v1"}

def test_path_params():
    country = 'India'
    resp = requests.get(f'https://restcountries.com/v2/name/{country}')
    assert resp.status_code == 200, 'Wrong code'
    print(resp.json())


def test_query_params():
    query_pms = {"page":2}
    resp = requests.get("https://reqres.in/api/users", params=query_pms, headers=HEADER)
    print(resp.json())
    print(resp.status_code)
    assert resp.status_code == 200, resp.status_code