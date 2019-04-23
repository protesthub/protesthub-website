from django.test import TestCase

from main.users.models import Profile, ProfileBackend


class ProfileBackendTest(TestCase):
    def setUp(self):
        self.user = Profile.objects.create_user(username='rick', email='rick@42.com', password='qwerty', terms_of_use=True,
                                                newsletter=False)

    def test_authenticate_user_using_email(self):
        actual_user = ProfileBackend().authenticate(None, username='rick@42.com', password='qwerty')
        self.assertEqual(actual_user, self.user)

    def test_authenticate_user_using_username(self):
        actual_user = ProfileBackend().authenticate(None, username='rick', password='qwerty')
        self.assertEqual(actual_user, self.user)

    def test_do_not_authenticate_user_on_invalid_email_password(self):
        actual_user = ProfileBackend().authenticate(None, username='rick@42.com', password='1234567')
        self.assertEqual(actual_user, None)

    def test_do_not_authenticate_user_on_invalid_username_password(self):
        actual_user = ProfileBackend().authenticate(None, username='rick', password='1234567')
        self.assertEqual(actual_user, None)

    def test_get_user_by_id(self):
        actual_user = ProfileBackend().get_user(self.user.id)
        self.assertIsNotNone(actual_user)
        self.assertEqual(actual_user, self.user)
