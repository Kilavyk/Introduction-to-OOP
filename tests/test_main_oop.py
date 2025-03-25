from tests.conftest import product


def test_product_init(product):
    assert product.name == "Samsung"
    assert product.description == "256GB"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_init(first_category, second_category):
    assert first_category.name == "Samsung"
    assert first_category.description == "Смартфоны"
    assert len(first_category.products) == 2

    assert second_category.name == "Xiaomi"
    assert second_category.description == "Смартфоны"
    assert len(second_category.products) == 1

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 3
    assert second_category.product_count == 3

