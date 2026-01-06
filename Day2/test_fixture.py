import pytest

@pytest.fixture()
def setup():
    print("Launch the browser")
    yield
    print("Close the browser")

class TestClass:
    def test_login(self, setup):
        print("This is login test")

    def test_search(self, setup):
        print("This is search test")