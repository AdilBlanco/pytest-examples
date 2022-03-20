import pytest

from src.tax_class import SimpleTaxCalculator


@pytest.fixture
def obj():
    return SimpleTaxCalculator()


def test_income_below_threshold(obj):
    assert obj.income_tax(60000) == 10200


def test_income_equal_threshold(obj):
    assert obj.income_tax(85528) == 14539.76


def test_income_above_threshold(obj):
    assert obj.income_tax(100000) == 19170.8


def test_vat_tax_with_default(obj):
    assert obj.vat_tax(100) == 23


def test_vat_tax_with_twenty_tax_rate(obj):
    assert obj.vat_tax(100, 20) == 20


def test_positive_profit(obj):
    assert obj.capital_gains_tax(1000) == 190


def test_zero_profit(obj):
    assert obj.capital_gains_tax(0) == 0


def test_negative_profit(obj):
    assert obj.capital_gains_tax(-1000) == 0
