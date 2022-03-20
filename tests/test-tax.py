import pytest
from src.tax import calculate_tax


def test_tax_with_eighteen_age():
    assert calculate_tax(60000, 18) == 6000


def test_tax_with_nineteenteen():
    assert calculate_tax(60000, 19) == 10200


def test_tax_with_sixty_five():
    assert calculate_tax(60000, 65) == 10200


def test_tax_with_sixty_six_age():
    assert calculate_tax(60000, 66) == 9000
