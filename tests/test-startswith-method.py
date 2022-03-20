def test_startswith_one_letter():
    "unittest".startswith("u") == True
    "unittest".startswith("U") == False


def test_startswith_four_letters():
    "http://www.e-smartdata.org/".startswith("http") == True
    "www.e-smartdata.org/".startswith("http") == False


def test_endswith_three_letter():
    assert 'e-smartdata.org'.endswith('org') == True
    assert 'e-smartdata.org'.endswith('com') == False
