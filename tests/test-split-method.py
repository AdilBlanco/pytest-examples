import pytest


@pytest.fixture
def result():
    yield ["python", "testing"]


def test_split_by_default(result):
    assert "python testing".split() == result


def test_split_by_comma(result):
    assert "python;testing".split(";") == result


def test_split_by_hash(result):
    assert "python#testing".split("#") == result
