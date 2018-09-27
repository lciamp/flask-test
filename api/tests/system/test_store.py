from api.models.store import StoreModel
from api.models.item import ItemModel
from api.tests.base_test import BaseTest
import json


class StoreTest(BaseTest):
    def test_create_store(self):
        response = self.client.post('/store/Test')
        self.assertEqual(response.status_code, 201)
        self.assertDictEqual(json.loads(response.data), StoreModel('Test').json())

    def test_create_duplicate_store(self):
        StoreModel('Test').save_to_db()
        response = self.client.post('/store/Test')
        self.assertEqual(response.status_code, 400)
        expected = {'message': "A store with name 'Test' already exists."}
        self.assertDictEqual(expected, json.loads(response.data))

    def test_delete_store(self):
        StoreModel('Test').save_to_db()
        response = self.client.delete('/store/Test')
        self.assertEqual(response.status_code, 200)
        expected = {'message': 'Store deleted'}
        self.assertDictEqual(json.loads(response.data), expected)

    def test_find_store(self):
        store = StoreModel('Test')
        store.save_to_db()
        response = self.client.get('/store/Test')
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(json.loads(response.data), store.json())

    def test_store_not_found(self):
        response = self.client.get('store/Test')
        self.assertEqual(response.status_code, 404)
        expected = {'message': 'Store not found'}
        self.assertDictEqual(expected, json.loads(response.data))

    def test_store_found_with_items(self):
        item = ItemModel('Test Item', 19.99,1 )
        store = StoreModel('Test')
        store.save_to_db()
        item.save_to_db()

        response = self.client.get('store/Test')

        self.assertEqual(response.status_code, 200)

        expected = {
            'name': 'Test',
            'items': [
                {'name': 'Test Item', 'price': 19.99}
            ]
        }
        self.assertDictEqual(json.loads(response.data), expected)

    def test_store_list(self):
        store1 = StoreModel('Test1')
        store2 = StoreModel('Test2')
        store1.save_to_db()
        store2.save_to_db()
        response = self.client.get('/stores')
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(json.loads(response.data),
                             {'stores': [store1.json(), store2.json()]})

    def test_store_list_with_items(self):
        store = StoreModel('Test')
        store.save_to_db()
        ItemModel('Test Item', 19.99, 1).save_to_db()

        response = self.client.get('/stores')
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(json.loads(response.data),
                             {'stores': [store.json()]})
