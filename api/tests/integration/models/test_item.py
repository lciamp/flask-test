from models.item import ItemModel
from api.tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('Test', 19.99)

            self.assertIsNone(ItemModel.find_by_name('Test'),
                              "Found an item with name '{}', but expected not to.".format(item.name))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('Test'),
                                 "Did not find an item with name '{}', but expected to.".format(item.name))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('Test'),
                              "Found an item with name '{}', but expected not to.".format(item.name))
