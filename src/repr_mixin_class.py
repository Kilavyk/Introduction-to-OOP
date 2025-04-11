class ReprMixin:
    """Миксин для вывода информации о создании объекта."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"{self.__repr__()}")

    def __repr__(self):
        attrs = []
        for attr, value in self.__dict__.items():
            if not attr.startswith('_'):
                attrs.append(f"'{value}'")
        return f"{self.__class__.__name__}({', '.join(attrs)})"
