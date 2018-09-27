from unittest import TestCase
from api.models.user import UserModel


class UserTest(TestCase):
    def test_create_user(self):
        user = UserModel('Test', 'password')

        self.assertIsNotNone(user)

        self.assertEqual(user.username, 'Test')

        self.assertEqual(user.password, 'password')
