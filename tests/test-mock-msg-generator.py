from unittest.mock import Mock, patch
from src.mock_msg_generator import get_message


@patch("src.mock_msg_generator.get_today_name")
def test_get_message_with_friday(mock_friday):
    mock_friday.return_value = "Friday"
    assert get_message() == "Hello Friday!"
