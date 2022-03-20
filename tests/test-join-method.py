import pytest


def test_join_with_space():
    assert " ".join(["Python", "3.8"]) == "Python 3.8"


def test_join_with_comma():
    assert ";".join(["Python", "3.8"]) == "Python;3.8"


def test_join_with_new_line_char():
    assert "\n".join(["Python", "3.8"]) == "Python\n3.8"
