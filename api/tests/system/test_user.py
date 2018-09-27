from api.models.user import UserModel
from api.tests.base_test import BaseTest
import json


class UserTest(BaseTest):
    def test_register_user(self):
        response = self.client.post('/register',
                               data={'username': 'test', 'password': 'password'})
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(UserModel.find_by_username('test'))
        expected = {"message": "User created successfully."}
        self.assertDictEqual(expected, json.loads(response.data))

    def test_register_and_login(self):
        UserModel('test', 'password').save_to_db()
        auth_response = self.client.post('/auth',
                                    data=json.dumps({'username': 'test', 'password': 'password'}),
                                    headers={'Content-Type': 'application/json'})
        self.assertIn('access_token', json.loads(auth_response.data).keys())

    def test_register_duplicate_user(self):
        user = UserModel('test', 'password')
        user.save_to_db()
        response = self.client.post('/register', data={'username': 'test', 'password': 'password'})
        self.assertEqual(response.status_code, 400)
        expected = {"message": "A user with that username already exists"}
        self.assertDictEqual(expected, json.loads(response.data))
