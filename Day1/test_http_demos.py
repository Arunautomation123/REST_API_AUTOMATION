import requests
import pytest

# HEADER = {'Content-Type': 'application/json'}
# HEADER = {'Content-Type': 'application/json'}
HEADER = {}
user_id = None

@pytest.mark.order(1)
def test_get_users():
    resp = requests.get("https://reqres.in/api/users?page=2")
    print(resp.json())
    print(resp.status_code)
    assert resp.status_code == 200, resp.status_code
    assert resp.elapsed.total_seconds() < 2, "Too slow"
    assert "email" in resp.text, "Email not found"
    data = resp.json()
    print(data)
    assert data.get("data") is not None, "Data not found"
    assert data.get("page") == 2, 'Wrong Page'

@pytest.mark.order(2)
def test_create_user():
    global user_id
    payload = {'name': 'Arun', 'Job': 'Software Engineer'}
    resp = requests.post("https://reqres.in/api/users", json=payload)
    # print(resp.json())
    print(resp.status_code)
    assert resp.status_code == 201, resp.status_code
    assert resp.elapsed.total_seconds() < 2, "Too slow"
    assert "email" in resp.text, "Email not found"
    data = resp.json()
    print(data)
    assert data.get("name") == 'Arun', "Name incorrect"
    assert data.get("job") == 'trainer', 'Job mismatch'
    user_id = data.get("id")

@pytest.mark.order(3)
def test_update_user():
    payload = {'name': 'Arun', 'Job': 'Software Tester'}
    resp = requests.put(f"https://reqres.in/api/users/{user_id}", json=payload)
    # print(resp.json())
    print(resp.status_code)
    assert resp.status_code == 200, resp.status_code
    assert resp.elapsed.total_seconds() < 2, "Too slow"
    assert "email" in resp.text, "Email not found"
    data = resp.json()
    print(data)
    assert data.get("name") == 'Arun', "Name incorrect"
    assert data.get("job") == 'Software Tester', 'Job mismatch'


@pytest.mark.order(4)
def test_delete_user():
    resp = requests.delete(f"https://reqres.in/api/users/{user_id}")
    # print(resp.json())
    print(resp.status_code)
    assert resp.status_code == 200, resp.status_code
    assert resp.elapsed.total_seconds() < 2, "Too slow"
    print("User deleted successfully")
