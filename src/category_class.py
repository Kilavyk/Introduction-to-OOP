from src.product_class import Product


class Category:
    """Класс для категорий товаров в магазине."""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None) -> None:
        """Инициализация категории."""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        """Возвращает строковое представление категории"""
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    def add_product(self, product) -> None:
        """Добавляет товар (или его наследника) в категорию."""
        if not isinstance(product, Product):
            raise TypeError(f"Ожидается Product, получен {type(product).__name__}")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> list:
        """Геттер для получения форматированного списка товаров."""
        return [str(product) for product in self.__products]

    def middle_price(self) -> float:
        """Подсчитывает средний ценник всех товаров в категории."""

        if not self.__products:
            return 0.0

        total_price = 0.0
        for product in self.__products:
            total_price += product.price

        average_price = total_price / len(self.__products)

        return average_price
