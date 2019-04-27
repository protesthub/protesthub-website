from django.test import TestCase

from main.users.models import User, UserBackend


class ProfileBackendTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='rick', email='rick@42.com', password='qwerty', terms_of_use=True,
                                             newsletter=False)

    def test_authenticate_user_using_email(self):
        actual_user = UserBackend.authenticate(None, username='rick@42.com', password='qwerty')
        self.assertEqual(actual_user, self.user)

    def test_authenticate_user_using_email_is_case_insensitive(self):
        actual_user = UserBackend.authenticate(None, username='RicK@42.COM', password='qwerty')
        self.assertEqual(actual_user, self.user)

    def test_authenticate_user_using_username(self):
        actual_user = UserBackend.authenticate(None, username='rick', password='qwerty')
        self.assertEqual(actual_user, self.user)

    def test_authenticate_user_using_username_is_case_insensitive(self):
        actual_user = UserBackend.authenticate(None, username='Rick', password='qwerty')
        self.assertEqual(actual_user, self.user)

    def test_authenticate_user_is_not_case_insensitive(self):
        actual_user = UserBackend.authenticate(None, username='rick', password='QwerTy')
        self.assertIsNone(actual_user)

    def test_do_not_authenticate_user_on_invalid_email_password(self):
        actual_user = UserBackend.authenticate(None, username='rick@42.com', password='1234567')
        self.assertEqual(actual_user, None)

    def test_do_not_authenticate_user_on_invalid_username_password(self):
        actual_user = UserBackend.authenticate(None, username='rick', password='1234567')
        self.assertEqual(actual_user, None)

    def test_get_user_by_id(self):
        actual_user = UserBackend.get_user(self.user.id)
        self.assertIsNotNone(actual_user)
        self.assertEqual(actual_user, self.user)
