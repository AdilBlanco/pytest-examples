import pytest

from src.employee_class import Employee


@pytest.fixture
def obj():
    yield Employee(
        first_name="John",
        last_name="Smith",
        age=40,
        salary=80000)


def test_email(obj):
    assert hasattr(obj, "email") == True
    assert obj.email == "john.smith@mail.com"


def test_email_after_changing_first_name(obj):
    obj.first_name = "Mike"
    assert obj.email == "mike.smith@mail.com"


def test_email_after_changing_last_name(obj):
    obj.last_name = "Doe"
    assert obj.email == "john.doe@mail.com"


def test_get_salary(obj):
    assert obj.salary == 80000


def test_apply_bonus(obj):
    obj.apply_bonus()
    assert obj.salary == 88000
