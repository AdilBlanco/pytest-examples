import pytest
from typing import List
from src.slo import StringListOnly


def test_string_list_successful():
    slo = StringListOnly()  # ~ []
    slo.append("bb")
    assert slo == ["bb"]


def test_string_list_failed():
    slo = StringListOnly()
    with pytest.raises(TypeError):
        slo.append(1)


def test_slo_isinstance():
    slo = StringListOnly()
    assert isinstance(slo, list) == True
    assert isinstance(slo, StringListOnly) == True


def test_slo_issubclass():
    assert issubclass(StringListOnly, List) == True
