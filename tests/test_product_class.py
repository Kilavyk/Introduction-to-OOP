from src.product_class import Product, Smartphone, LawnGrass


def test_product_init(product):
    assert product.name == "Samsung"
    assert product.description == "256GB"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_new_product_classmethod():
    product_data = {
        "name": "Test Product",
        "description": "Test Description",
        "price": 1000.0,
        "quantity": 10
    }
    product = Product.new_product(product_data)

    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 1000.0
    assert product.quantity == 10


def test_price_setter_valid(product):
    product.price = 200000.0
    assert product.price == 200000.0


def test_price_setter_invalid(capsys, product):
    initial_price = product.price
    product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == initial_price  # Цена не изменилась
    assert product.price == 180000.0


def test_price_decrease_confirmation(product, monkeypatch):
    initial_price = product.price

    # Ввод 'n'
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    product.price = initial_price - 1000
    assert product.price == initial_price  # Цена не изменилась

    # Ввод 'y'
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    product.price = initial_price - 1000
    assert product.price == initial_price - 1000

def test_product_str(product):
    assert str(product) == "Samsung, 180000.0 руб. Остаток: 5 шт."


def test_product_add(sample_products_for_add):
    product1, product2 = sample_products_for_add
    total_value = product1 + product2
    expected_value = (1000.0 * 3) + (2000.0 * 2)
    assert total_value == expected_value

def test_smartphone_init(smartphone):
    assert smartphone.name == "iPhone 15"
    assert smartphone.memory == 512
    assert smartphone.color == "Gray"
    assert isinstance(smartphone, Product)

def test_lawn_grass_init(lawn_grass):
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "7 дней"
    assert isinstance(lawn_grass, Product)

def test_add_smartphones(smartphone, another_smartphone):
    total = smartphone + another_smartphone
    assert total == (210000.0 * 8) + (180000.0 * 5)

def test_add_lawn_grass(lawn_grass, another_lawn_grass):
    total = lawn_grass + another_lawn_grass
    assert total == (500.0 * 20) + (700.0 * 15)

def test_repr_mixin_functionality(capsys):
    """Тестируем вывод информации при создании объекта"""
    p = Product("Test", "Desc", 100, 5)
    captured = capsys.readouterr()
    assert "Product('Test', 'Desc', '5')" in captured.out

    s = Smartphone("iPhone 15", "512GB", 210000.0, 8, efficiency=98.2, model="15", memory=512, color="Gray")
    captured = capsys.readouterr()
    assert "Smartphone('iPhone 15', '512GB', '8')" in captured.out

    LawnGrass("Трава", "Элитная", 500.0, 20, country="Россия", germination_period="7 дней", color="Зеленый")
    captured = capsys.readouterr()
    assert "LawnGrass('Трава', 'Элитная', '20')" in captured.out