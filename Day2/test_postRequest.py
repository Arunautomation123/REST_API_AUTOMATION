import requests
import json
import pytest
from dataclasses import dataclass

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
    "id": "1014",
    "name": "Tarun",
    "active": True,
    "grades": [
      2.3,
      4.3,
      5.5
    ],
    "yearsOld": 29,
    "color": "green"}

    # resp = requests.post('http://localhost:3000/students', json=payload)

    resp = requests.post('http://localhost:3000/students', data=json.dumps(payload), headers=HEADERS)

    assert resp.status_code == 201, 'Wrong status code'
    assert resp.elapsed.total_seconds() < 2, 'Too slow response'
    resp_1 = resp.json()
    assert resp_1['name'] == 'Tarun', 'Wrong Name'
    student_ID = resp_1['id']

@pytest.fixture(autouse=True)
def delete_student():
    yield
    resp1 = requests.delete(f'http://localhost:3000/students/{student_ID}')
    assert resp1.status_code == 200, 'Wrong status code'
    # print(resp1.json())
    print("Deleted student")

def test_create_using_class():
    global student_ID
    class Student():
        def __init__(self, id, name, grades, active, color, yearsOld):
            self.id = id
            self.name = name
            self.grades = grades
            self.active = active
            self.color = color
            self.yearsOld = yearsOld

    student = Student(1015, 'Teja', [2.2, 3.3, 4.4], True, 'green', 29)

    resp_body = student.__dict__
    resp = requests.post('http://localhost:3000/students', data=json.dumps(resp_body), headers=HEADERS)

    assert resp.status_code == 201, 'Wrong status code'
    assert resp.elapsed.total_seconds() < 2, 'Too slow response'
    resp_1 = resp.json()
    assert resp_1['name'] == 'Teja', 'Wrong Name'
    student_ID = resp_1['id']


def test_create_using_dataclass():
    global student_ID
    @dataclass
    class Student:
        id: int
        name: str
        grades: list
        active: bool
        color: str
        age: int

    student = Student(1016, 'Tejas', [2.2, 3.3, 4.4], True, 'green', 32)
    resp_body = student.__dict__
    resp = requests.post('http://localhost:3000/students', data=json.dumps(resp_body), headers=HEADERS)

    assert resp.status_code == 201, 'Wrong status code'
    assert resp.elapsed.total_seconds() < 2, 'Too slow response'
    resp_1 = resp.json()
    assert resp_1['name'] == 'Tejas', 'Wrong Name'
    student_ID = resp_1['id']

def test_create_using_ext_file():
    global student_ID
    with open("./body.json", 'r') as f:
        resp_body = json.load(f)
    resp = requests.post('http://localhost:3000/students', data=json.dumps(resp_body), headers=HEADERS)

    assert resp.status_code == 201, 'Wrong status code'
    assert resp.elapsed.total_seconds() < 2, 'Too slow response'
    resp_1 = resp.json()
    assert resp_1['name'] == 'Carlos sainz', 'Wrong Name'
    student_ID = resp_1['id']
