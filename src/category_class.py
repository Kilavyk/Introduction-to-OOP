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

    def add_product(self, product) -> None:
        """Добавляет товар в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> list:
        """Геттер для получения форматированного списка товаров."""
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]
