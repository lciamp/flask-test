from api.models.item import ItemModel
from api.models.store import StoreModel
from api.tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        StoreModel('Test Store').save_to_db()
        item = ItemModel('Test', 19.99, 1)

        self.assertIsNone(ItemModel.find_by_name('Test'),
                          "Found an item with name '{}', but expected not to.".format(item.name))

        item.save_to_db()

        self.assertIsNotNone(ItemModel.find_by_name('Test'),
                             "Did not find an item with name '{}', but expected to.".format(item.name))

        item.delete_from_db()

        self.assertIsNone(ItemModel.find_by_name('Test'),
                          "Found an item with name '{}', but expected not to.".format(item.name))

    def test_store_relationship(self):
        store = StoreModel('Test Store')
        item = ItemModel('Test', 19.99, 1)

        store.save_to_db()
        item.save_to_db()

        self.assertEqual(item.store.name, 'Test Store')

