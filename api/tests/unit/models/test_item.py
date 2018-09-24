from unittest import TestCase

from models.item import ItemModel


class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel('Test Name', 11.00)
        self.assertIsNotNone(item)
        self.assertEqual(item.name, 'Test Name')
        self.assertEqual(item.price, 11.00)

    def test_item_json(self):
        item = ItemModel('Test Name', 11.00)
        expected = {'name': 'Test Name', 'price': 11.00}
        self.assertEqual(expected, item.json())
