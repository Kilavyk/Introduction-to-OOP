import pytest

from src.main_oop import Category, Product


@pytest.fixture
def first_category():
    return Category(
        name="Samsung",
        description="Смартфоны",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Samsung Galaxy Z Fold 5", "512GB, Черный, складной экран", 250000.0, 3),
        ],
    )

@pytest.fixture
def second_category():
    return Category(
        name="Xiaomi",
        description="Смартфоны",
        products=[
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        ],
    )

@pytest.fixture
def product():
    return Product("Samsung", "256GB", 180000.0, 5)