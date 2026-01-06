import requests
import json
import pytest

student_ID = None

HEADERS = {'Content-Type': 'application/json'}
base_url = 'http://localhost:3000/'

# when json = is used then content type should be automatically taken as application/json,
# that is converted to json string
# data parameter - sends form data default

# dictionary

def test_create_dict():
    global student_ID
    payload = {
    "id": "1013",
    "name": "Vijay",
    "active": True,
    "grades": [
      2.3,
      4.3,
      5.5
    ],
    "yearsOld": 29,
    "color": "blue"}

    # resp = requests.post('http://localhost:3000/students', json=payload)

    resp = requests.post('http://localhost:3000/students', data=json.dumps(payload), headers=HEADERS)

    assert resp.status_code == 201, 'Wrong status code'
    assert resp.elapsed.total_seconds() < 2, 'Too slow response'
    resp_1 = resp.json()
    assert resp_1['name'] == 'Vijay', 'Wrong Name'
    student_ID = resp_1['id']

@pytest.fixture(autouse=True)
def delete_student():
    yield
    resp = requests.delete(f'http://localhost:3000/students/{student_ID}')
    assert resp.status_code == 200, 'Wrong status code'
    print(resp.json())
    print("Deleted student")

