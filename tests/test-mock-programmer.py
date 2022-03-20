import pytest
from unittest.mock import patch

from src.mock_programmer import Programmer


@pytest.fixture
def programmer():
    return Programmer().add_tech('python') \
            .add_tech('java') \
            .add_tech('sql') \
            .add_tech('aws') \
            .add_tech('django')


@patch.object(Programmer, "get_random_tech")
def test_get_random_tech_mock_py(mock_tech, programmer):
    mock_tech.return_value = "python"
    assert programmer.get_random_tech() == "python"


@patch.object(Programmer, "get_random_tech")
def test_get_random_tech_mock_cpp(mock_tech, programmer):
    mock_tech.return_value = "c++"
    assert programmer.get_random_tech() == "c++"


@patch.object(Programmer, "get_random_tech")
def test_display_random_tech_py(mock_display, programmer):
    mock_display.return_value = "python"
    assert programmer.display_random_tech() == "Technology name: python"


@patch.object(Programmer, "get_random_tech")
def test_display_random_tech_cpp(mock_display, programmer):
    mock_display.return_value = "c++"
    assert programmer.display_random_tech() == "Technology name: c++"