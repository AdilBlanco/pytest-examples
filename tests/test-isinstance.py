import py
import pytest
from collections import Counter

# @pytest.fixture
# def result():
#     return True


def test_case_1():
    assert isinstance((), tuple) == True


def test_case_2():
    assert isinstance([], list) == True


def test_case_3():
    assert isinstance({}, dict) == True


def test_case_4():
    cnt = Counter()
    assert isinstance(cnt, Counter) == True


def test_case_5():
    var1 = 4
    assert isinstance(var1, int) == True
