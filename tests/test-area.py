import pytest
from numpy.testing import assert_almost_equal

from src.area import area, perimeter


def test_circle_area_with_radius_one():
    assert_almost_equal(area(1), 3.14, 2)


def test_circle_area_with_radius_three():
    assert_almost_equal(area(3), 28.27, 2)


def test_area_incorrect_type_should_raise_type_error():
    with pytest.raises(TypeError):
        area("ha")
        area(None)


def test_area_incorrect_value_should_raise_value_error():
    with pytest.raises(ValueError):
        area(0)
        area(-1)


def test_circle_perimeter_with_radius_one():
    assert_almost_equal(perimeter(1), 6.28, 2)


def test_circle_perimeter__with_radius_three():
    assert_almost_equal(perimeter(3), 18.84, 2)


def test_perimeter__incorrect_type_should_raise_type_error():
    with pytest.raises(TypeError):
        perimeter("ha")
        perimeter(None)


def test_perimeter__incorrect_value_should_raise_value_error():
    with pytest.raises(ValueError):
        perimeter(0)
        perimeter(-1)
