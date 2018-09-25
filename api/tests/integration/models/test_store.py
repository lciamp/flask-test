from models.item import ItemModel
from models.store import StoreModel
from api.tests.base_test import BaseTest


class StoreTest(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel('Test Store')

        self.assertListEqual(store.items.all(), [],
                             "Store items length was not zero even though no items were added.")

    def test_crud(self):
        with self.app_context():
            store = StoreModel('Test')

            self.assertIsNone(store.find_by_name('Test'),
                              "Found an store with name '{}', but expected not to.".format(store.name))

            store.save_to_db()

            self.assertIsNotNone(store.find_by_name('Test'),
                                 "Did not find an store with name '{}', but expected to.".format(store.name))

            store.delete_from_db()

            self.assertIsNone(store.find_by_name('Test'),
                              "Found an store with name '{}', but expected not to.".format(store.name))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('Test Store')
            item = ItemModel('Test', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, item.name)

    def test_store_json_with_item(self):
        with self.app_context():
            store = StoreModel('Test Store')
            item = ItemModel('Test', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            expected = {
                'name': 'Test Store',
                'items': [{'name': 'Test', 'price': 19.99}]
            }

            self.assertEqual(store.json(), expected)





