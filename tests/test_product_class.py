from src.product_class import Product


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
