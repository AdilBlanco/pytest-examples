def test_upper():
    assert "summer".upper() == "SUMMER"


def test_is_upper():
    assert "SUMMER".isupper() == True
    assert "summer".isupper() == False
