from api.tests.base_test import BaseTest
from api.models.user import UserModel


class UserTest(BaseTest):
    def test_crud(self):
        user = UserModel('Test', 'password')

        self.assertIsNone(user.find_by_username('Test'),
                          "Found a user with name '{}', but expected not to.".format(user.username))
        self.assertIsNone(user.find_by_id(1),
                          "Found a user with id: 1, but expected not to.")

        user.save_to_db()

        self.assertIsNotNone(user.find_by_username('Test'),
                             "Did not find a user with name '{}', but expected to.".format(user.username))
        self.assertIsNotNone(user.find_by_id(1),
                             "Did not find a user with id: 1, but expected to.")

        user.delete_from_db()

        self.assertIsNone(user.find_by_username('Test'),
                          "Found a user with name '{}', but expected not to.".format(user.username))
        self.assertIsNone(user.find_by_id(1),
                          "Found a user with id: 1, but expected not to.")


