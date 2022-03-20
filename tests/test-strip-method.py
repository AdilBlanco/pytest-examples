def test_strip():
    assert "pass ".strip() == "pass"
    assert " pass ".strip() == "pass"
    assert "  pass".strip() == "pass"


def test_lstrip():
    assert " pass".lstrip() == "pass"
    assert " pass ".lstrip() == "pass "
    assert "  pass".lstrip() == "pass"


def test_rstrip():
    assert "pass ".rstrip() == "pass"
    assert " pass".rstrip() == " pass"
    assert "pass    ".rstrip() == "pass"
