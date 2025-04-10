import pytest

from src.category_class import Category
from src.product_class import Product


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


def test_add_product(first_category):
    assert len(first_category.products) == 2
    new_product = Product("Samsung Galaxy S22", "128GB, Black", 120000.0, 7)
    first_category.add_product(new_product)
    assert len(first_category.products) == 3

    # Тест на попытку добавления неподходящего объекта
    with pytest.raises(TypeError) as excinfo:
        first_category.add_product("string_product")
    assert "Ожидается Product, получен str" in str(excinfo.value)

def test_category_str(first_category):
    assert str(first_category) == "Samsung, количество продуктов: 2 шт."

def test_add_smartphone_to_category(first_category, smartphone):
    initial_count = len(first_category.products)
    first_category.add_product(smartphone)
    assert len(first_category.products) == initial_count + 1
    assert "iPhone 15" in str(first_category.products)

def test_add_lawn_grass_to_category(first_category, lawn_grass):
    initial_count = len(first_category.products)
    first_category.add_product(lawn_grass)
    assert len(first_category.products) == initial_count + 1
    assert "Трава" in str(first_category.products)

def test_add_invalid_type_to_category(first_category):
    with pytest.raises(TypeError) as excinfo:
        first_category.add_product({"name": "Not a product"})
    assert "Ожидается Product, получен dict" in str(excinfo.value)
