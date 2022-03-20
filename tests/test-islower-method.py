def test_lower():
    assert "Joe.Smith@mail.com".lower() == "joe.smith@mail.com"


def test_is_lower():
    assert "joe.smith@mail.com".islower() == True
    assert "Joe.Smith@mail.com".islower() == False
