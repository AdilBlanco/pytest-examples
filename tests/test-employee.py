from attr import has
import pytest
from src.employee import Employee


def test_has_email_attr():
    assert hasattr(
        Employee, "email") == True, "The Employee class does not have an email attribute."


def test_has_tax_attr():
    assert hasattr(
        Employee, "tax") == True, "The Employee class does not have a tax attribute."


def test_has_apply_bonus():
    assert hasattr(
        Employee, "apply_bonus") == True, "The Employee class does not have an apply_bonus attribute."


def test_has_email_property():
    assert isinstance(Employee.email, property) == True
