import pytest




def test_equal_or_not_equal():
    assert 3 == 3
    assert 3 == 3

def test_is_instance():
    assert isinstance(3, int)


def test_boolean():
    validated = True
    assert validated is True
    assert ('hello' == 'world') is False


def test_type():
    assert type('hello' is str)
    assert type('World' is not int) 

def test_list():
    num_list = [1,2,3,4,5]
    any_list = [False, False]
    assert 1 in num_list
    assert 7 in num_list
    assert all(num_list)
    assert not any(any_list)

class Student:
    def __init__(self,first_name:str,last_name:str,major:str,years:int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years


#This function will be called when we run the test test_person_initilaization
@pytest.fixture
def default_employee():
    return Student('Jhon','Doe','Computer Science',4)

def test_person_initialization(default_employee):
    # no need for the below code
    # p= Student('Jhon','Doe','Computer Science',4)
    assert default_employee.first_name == 'Jhon','First name should be jhon'
    assert default_employee.last_name == 'Doe','Last name should be Doe'
    assert default_employee.major == 'Computer Science','Major will be CS'
    assert default_employee.years == 4
