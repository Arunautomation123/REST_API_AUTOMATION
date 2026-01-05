import pytest
# class TestClass:
#     def testmethod1(self):
#         print("This is method1")
#
#     def testmethod2(self):
#         print("This is method2")

@pytest.mark.dependency()
@pytest.mark.order(1)
def test_func1():
    print("This is func1")
    assert False

@pytest.mark.dependency(depends=["test_func3"])
@pytest.mark.order(3)
def test_func2():
    print("This is func2")

@pytest.mark.dependency(depends=["test_func1"])
@pytest.mark.order(2)
def test_func3():
    print("This is func3")