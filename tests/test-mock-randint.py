import random
from unittest.mock import Mock, patch

from src.mock_randint import get_code


@patch("random.randint")
def test_get_code_mock_return_30(mock_randint):
    mock_randint.return_value = 30
    assert get_code() == "CX-30"
