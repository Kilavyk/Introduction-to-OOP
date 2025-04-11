from src.base_product_class import BaseProduct
from src.repr_mixin_class import ReprMixin


class Product(ReprMixin, BaseProduct, ):
    """Класс для описания товара в магазине."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализация товара."""
        super().__init__(name, description, price, quantity)
        self.__price = price  # Приватный атрибут

    def __str__(self):
        """Строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение двух продуктов."""
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, new_product: dict) -> "Product":
        """Создает новый товар из словаря данных."""
        return cls(new_product["name"], new_product["description"], new_product["price"], new_product["quantity"])

    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price) -> None:
        """Сеттер для цены с проверкой"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:  # если цена понижается
                confirmation = input(f"Вы уверены, что хотите понизить цену с {self.__price} до {new_price}? (y/n): ")
                if confirmation.lower() == "y":
                    self.__price = new_price
            else:
                self.__price = new_price


class Smartphone(Product):
    """Класс для товаров категории 'Смартфоны'."""

    efficiency: str
    model: str
    memory: str
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Инициализация смартфона."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Сложение двух смартфонов."""
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError


class LawnGrass(Product):
    """Класс для товаров категории 'Газонная трава'."""

    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Сложение двух упаковок газонной травы."""
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
