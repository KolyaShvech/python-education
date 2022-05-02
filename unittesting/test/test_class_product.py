"""
Testing classes Product and Shop.
"""
from unittest.mock import patch

import pytest

from unittesting.unittesting.class_product import Product, Shop


@pytest.fixture
def some_product():
    """
    Create product with parameters.
    """
    return Product("airpods", 2499.99, quantity=200)


def test_init_param(some_product):
    """
    Check parameters initialisation.
    """
    assert some_product.title == 'airpods'
    assert some_product.price == 2499.99
    assert some_product.quantity == 200


def test_subtract_quantity(some_product):
    """
    Check method subtract_quantity.
    """
    some_product.subtract_quantity(50)
    assert some_product.quantity == 150


def test_add_quantity(some_product):
    """
    Check method add_quantity.
    """
    some_product.add_quantity(100)
    assert some_product.quantity == 300


def test_change_price(some_product):
    """
    Check method change_price with different parameters.
    """
    some_product.change_price(2399.99)
    assert some_product.price == 2399.99
    assert some_product.price == 2000
    assert some_product.price == 0
    assert some_product.price == -100


@pytest.fixture
def goods_shop(some_product):
    """
    Create fixture for shop.
    """
    return Shop(some_product)


def test_add_new_product(goods_shop, some_product):
    """
    Check method add_product.
    """
    new_product = Product('watch', 10001.50, 10)
    goods_shop.add_product(new_product)
    assert goods_shop.products == [some_product, new_product]


@pytest.mark.parametrize('product_title, expected_result', [
    ('airpods', 0),
    ('random_title', None)
], ids=[
    'product present in shop',
    'product does not'
])
def test_get_product_index(goods_shop, product_title, expected_result):
    """
    Check empty index product.
    """
    actual_result = goods_shop._get_product_index(product_title)
    assert actual_result == expected_result


def test_get_index_product(goods_shop):
    """
    Check index product 'Oppo'.
    """
    assert goods_shop._get_product_index("Oppo") == 3


@pytest.mark.parametrize('nokia', [('nokia', 100), ('nokia', 0), ('nokia', -20)])
def test_sell_product(goods_shop, nokia):
    """
    Check sell product.
    """
    assert goods_shop.sell_product(*nokia) == nokia[1]


@patch('class_product.Shop._get_product_index', return_value=0)
def test_sell_product_with_insufficient_amount(index_mock, goods_shop):
    """
    Testing sell product with insufficient index, raise error.
    """
    with pytest.raises(ValueError):
        goods_shop.sell_product('airpods', 201)


def test_sell_product_all_quantity(goods_shop):
    """
    Check sell product all quantity. Then sell all product output empty list.
    """
    goods_shop.sell_product('airpods', 200)
    assert goods_shop.products == []


def test_sell_product_changed_quantity(goods_shop):
    """
    Testing sell product changed quantity.
    """
    goods_shop.sell_product('airpods')
    assert goods_shop.products[0].quantity == 199


@pytest.mark.parametrize('product_title, expected_result', [
    ('airpods', 2499.99),
    ('somepods', None),
], ids=['product sell at shop.', 'have not product at shop.'])
def test_sell_product(goods_shop, product_title, expected_result):
    """
    Check sell product, where have product and have not.
    """
    actual_result = goods_shop.sell_product(product_title)
    assert actual_result == expected_result