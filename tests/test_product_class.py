def test_product_init(product):
    assert product.name == "Samsung"
    assert product.description == "256GB"
    assert product.price == 180000.0
    assert product.quantity == 5