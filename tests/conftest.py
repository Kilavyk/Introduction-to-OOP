import pytest

from src.category_class import Category
from src.product_class import Product, Smartphone, LawnGrass


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


@pytest.fixture
def sample_json_data():
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации...",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5
                }
            ]
        }
    ]

@pytest.fixture
def sample_products_for_add():
    """Фикстура для тестирования сложения продуктов (__add__)."""
    product1 = Product("Product 1", "Description 1", 1000.0, 3)
    product2 = Product("Product 2", "Description 2", 2000.0, 2)
    return product1, product2

@pytest.fixture
def smartphone():
    smartphone = Smartphone("iPhone 15", "512GB", 210000.0, 8, efficiency=98.2, model="15", memory=512, color="Gray")
    return smartphone

@pytest.fixture
def lawn_grass():
    lawn_grass = LawnGrass("Трава", "Элитная", 500.0, 20, country="Россия", germination_period="7 дней", color="Зеленый")
    return lawn_grass

@pytest.fixture
def another_smartphone():
    another_smartphone = Smartphone("Samsung S24", "256GB", 180000.0, 5, efficiency=95.0, model="S24", memory=256, color="Black")
    return another_smartphone

@pytest.fixture
def another_lawn_grass():
    another_lawn_grass = LawnGrass("Трава Premium", "Устойчивая", 700.0, 15, country="USA", germination_period="10 дней", color="Dark Green")
    return another_lawn_grass

