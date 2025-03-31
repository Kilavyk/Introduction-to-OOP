class Product:
    """Класс для описания товара в магазине."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализация товара."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """Строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity

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
