import json
import os

from src.main_oop import Product, Category


def read_json() -> list:
    """Читает JSON-файл и возвращает данные виде списка словарей"""
    full_path = os.path.abspath("../data/products.json")
    with open(full_path, 'r', encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: list) -> list:
    """Создает объекты Category и Product из JSON-данных."""
    category = []
    for item in data:
        product = []
        for i in item["products"]:
            product.append(Product(**i))
        item["products"] = product
        category.append(Category(**item))
    return category



if __name__ == "__main__":
    # Чтение данных
    data = read_json()
    print(data)

    # Создание объектов
    class_data = create_objects_from_json(data)
    print(class_data)

    # Вывод полученных данных
    print(class_data[0].name)
    print(class_data[0].description)
    print(class_data[0].products[0].name)
    print(class_data[0].products[0].description)
    print(class_data[0].products[0].price)
    print(class_data[0].products[0].quantity)

    print(class_data[1].name)
    print(class_data[1].description)
    print(class_data[1])


