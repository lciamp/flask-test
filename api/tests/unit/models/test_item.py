from unittest import TestCase
from api.models.item import ItemModel
from api.models.store import StoreModel


class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel('Test Name', 11.00, 1)
        self.assertIsNotNone(item)
        self.assertEqual(item.name, 'Test Name')
        self.assertEqual(item.price, 11.00)

        self.assertEqual(item.store_id, 1)

        self.assertIsNone(item.store)

    def test_item_json(self):
        item = ItemModel('Test Name', 11.00, 1)
        expected = {'name': 'Test Name', 'price': 11.00}
        self.assertEqual(expected, item.json())
