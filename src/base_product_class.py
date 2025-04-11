from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов."""

    @abstractmethod
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass