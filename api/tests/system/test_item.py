from api.models.store import StoreModel
from api.models.item import ItemModel
from api.models.user import UserModel
from api.tests.base_test import BaseTest
import json


class ItemTest(BaseTest):
    def setUp(self):
        super(ItemTest, self).setUp()
        UserModel('test', 'password').save_to_db()
        auth_response = self.client.post('/auth',
                                    data=json.dumps({'username': 'test', 'password': 'password'}),
                                    headers={'Content-Type': 'application/json'})
        self.token = 'JWT {}'.format(json.loads(auth_response.data).get('access_token'))

    def test_get_item_with_auth(self):
        headers = {'Authorization': self.token}

        ItemModel('test', 19.99, 1).save_to_db()
        response = self.client.get('/item/test',
                              headers=headers)
        self.assertEqual(response.status_code, 200)
        expected = {'name': 'test', 'price': 19.99}

        self.assertDictEqual(json.loads(response.data),
                             expected)

    def test_get_item_no_auth(self):

        ItemModel('test', 19.99, 1).save_to_db()
        response = self.client.get('/item/test')
        self.assertEqual(response.status_code, 401)
        expected = {'message': 'Could not authorize. Did you include a valid Authorization header?'}
        self.assertDictEqual(json.loads(response.data), expected)

    def test_get_item_not_found(self):
        UserModel('test', 'password').save_to_db()
        auth_response = self.client.post('/auth',
                                    data=json.dumps({'username': 'test', 'password': 'password'}),
                                    headers={'Content-Type': 'application/json'})
        token = json.loads(auth_response.data).get('access_token')
        headers = {'Authorization': 'JWT {}'.format(token)}

        response = self.client.get('/item/test', headers=headers)

        self.assertEqual(response.status_code, 404)
        self.assertDictEqual(json.loads(response.data),
                             {'message': 'Item not found'})

    def test_delete_item(self):
        ItemModel('test', 19.99, 1).save_to_db()
        response = self.client.delete('/item/test')
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(json.loads(response.data),
                             {'message': 'Item deleted'})

    def test_create_item(self):
        response = self.client.post('/item/test',
                               data=json.dumps({'price': 19.99, 'store_id': 1}),
                               headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201)
        self.assertDictEqual(json.loads(response.data),
                             {'name': 'test', 'price': 19.99})

    def test_put_item(self):
        response = self.client.put('/item/test',
                              data=json.dumps({'price': 19.99, 'store_id': 1}),
                              headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(json.loads(response.data),
                             {'name': 'test', 'price': 19.99})

    def test_put_item_update(self):
        ItemModel('test', 19.99, 1).save_to_db()
        response = self.client.put('/item/test',
                              data=json.dumps({'price': 20.00, 'store_id': 1}),
                              headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(json.loads(response.data),
                             {'name': 'test', 'price': 20.00})

    def test_get_items(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(json.loads(response.data),
                             {'items': []})
