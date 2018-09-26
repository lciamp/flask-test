from models.user import UserModel
from api.tests.base_test import BaseTest
import json
from flask import jsonify


class UserTest(BaseTest):
    def test_register_user(self):
        with self.app() as client:
            with self.app_context():
                response = client.post('/register', data={'username': 'test', 'password': 'password'})
                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('test'))
                expected = {"message": "User created successfully."}
                self.assertDictEqual(expected, json.loads(response.data))

    def test_register_and_login(self):
        with self.app() as client:
            with self.app_context():
                UserModel('test', 'password').save_to_db()
                auth_response = client.post('/auth',
                                            data=json.dumps({'username': 'test', 'password': 'password'}),
                                            headers={'Content-Type': 'application/json'})
                self.assertIn('access_token', json.loads(auth_response.data).keys())

    def test_register_duplicate_user(self):
        with self.app() as client:
            with self.app_context():
                user = UserModel('test', 'password')
                user.save_to_db()
                response = client.post('/register', data={'username': 'test', 'password': 'password'})
                self.assertEqual(response.status_code, 400)
                expected = {"message": "A user with that username already exists"}
                self.assertDictEqual(expected, json.loads(response.data))
