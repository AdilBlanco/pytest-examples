from unittest.mock import Mock, patch
from src.mock_msg_generator import get_message, get_code_with_day, get_code


@patch("src.mock_msg_generator.get_today_name")
def test_get_message_with_friday(mock_friday):
    mock_friday.return_value = "Friday"
    assert get_message() == "Hello Friday!"


@patch("src.mock_msg_generator.get_today_name")
def test_get_message_with_monday(mock_monday):
    mock_monday.return_value = "Monday"
    assert get_message() == "Hello Monday!"


@patch("random.randint")
@patch("src.mock_msg_generator.get_today_name")
def test_get_code_with_day_with_mocked_friday(
        mock_day, mock_int):

    mock_day.return_value = "FRIDAY"
    mock_int.return_value = 30

    assert get_code_with_day() == "CX-30-FRIDAY"
