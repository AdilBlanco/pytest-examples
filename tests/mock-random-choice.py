import pytest
import random
from unittest.mock import Mock, patch


@pytest.fixture
def techs():
    return ['python', 'sql', 'java', 'aws', 'c++']


@patch("random.choice", return_value="aws")
def test_random_choice(choice_mock):
    assert choice_mock(techs) == "aws"


