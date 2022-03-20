from pydoc import doc
import pytest
from src.doc import Doc


@pytest.fixture
def doc1():
    return Doc("technology")


@pytest.fixture
def doc2():
    return Doc("Online")


@pytest.fixture
def doc3():
    return Doc("Nature")

# test_less_than()
# doc2 < doc1
# doc3 < doc1


def test_less_than(doc1, doc2, doc3):
    assert doc2 < doc1
    assert doc3 < doc1

# test_greater_than()
# doc1 > doc2
# doc1 > doc3


def test_greater_than(doc1, doc2, doc3):
    assert doc1 > doc2
    assert doc1 > doc3


@pytest.mark.skip
def test_equal(doc1, doc2, doc3):
    assert doc2 == doc3


def test_not_equal(doc1, doc2, doc3):
    assert doc1 != doc2
    assert doc2 != doc3
