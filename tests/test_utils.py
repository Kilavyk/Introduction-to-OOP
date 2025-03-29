from unittest.mock import mock_open, patch

from src.category_class import Category
from src.utils import create_objects_from_json, read_json


@patch("builtins.open", new_callable=mock_open)
@patch("json.load")
def test_read_json(mock_json_load, mock_file):
    mock_json_load.return_value = [{"id": 123}, {"id": 321}]
    result = read_json()
    assert result == [{"id": 123}, {"id": 321}]


def test_create_objects_from_json(sample_json_data):
    result = create_objects_from_json(sample_json_data)

    assert isinstance(result[0], Category)

    category = result[0]
    assert category.name == "Смартфоны"
    assert "Смартфоны, как средство не только коммуникации" in category.description
