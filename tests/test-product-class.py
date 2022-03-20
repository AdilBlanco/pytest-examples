import pytest

from src.product_class import Product


@pytest.fixture
def product():
    return Product(
            product_name="p1",
            price=100)


def test_product_has_get_id_function_attribute(product):
    assert hasattr(product, "get_id") == True
    assert callable(product.get_id) == True
