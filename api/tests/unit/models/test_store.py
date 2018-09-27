from unittest import TestCase
from api.models.store import StoreModel
from api.models.item import ItemModel


class StoreTest(TestCase):
    def test_create_store(self):
        store = StoreModel('Test Name')
        self.assertIsNotNone(store)
        self.assertEqual(store.name, 'Test Name')
