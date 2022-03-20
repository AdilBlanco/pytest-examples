import pytest

from src.note_class import Note, Notebook


@pytest.fixture
def obj():
    return Note('Simple note.')


@pytest.fixture
def nb():
    notebook = Notebook()
    notebook.new_note('Big Data')
    notebook.new_note('Data Science')
    notebook.new_note('Machine Learning')
    return notebook


def test_note_has_content_instance_attr(obj):
    msg = 'A Note instance does not have a content attribute.'
    assert hasattr(obj, 'content'), msg


def test_note_has_category_class_attr(obj):
    msg = 'A Note instance does not have a category attribute.'
    assert hasattr(obj, 'category'), msg


def test_notebook_search_method(nb):
    print(nb.search("data"))
    assert nb.search("data") == ["Big Data", "Data Science"]
