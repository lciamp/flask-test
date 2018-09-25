from unittest import TestCase
from models.store import StoreModel
from models.item import ItemModel


class StoreTest(TestCase):
    def test_create_store(self):
        store = StoreModel('Test Name')
        self.assertIsNotNone(store)
        self.assertEqual(store.name, 'Test Name')
