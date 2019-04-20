from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class UserViewTest(TestCase):
    """
    References:
        - https://docs.djangoproject.com/en/2.2/topics/forms/#building-a-form-in-django
        - https://test-driven-django-development.readthedocs.io/en/latest/05-forms.html
        - https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
    """
    def test_create_user(self):
        data = {'username': 'rick', 'email': 'rick@42.com', 'password': 'qwerty', 'terms_of_use': True}
        response = self.client.post(reverse('users:sign_up'), data)

        actual_user = User.objects.get_by_natural_key('rick')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(actual_user.username, 'rick')
        self.assertEqual(actual_user.email, 'rick@42.com')
        self.assertEqual(actual_user.profile.terms_of_use, True)
        self.assertEqual(actual_user.profile.newsletter, False)

    def test_accepted_newsletter(self):
        data = {'username': 'rick', 'email': 'rick@42.com', 'password': 'qwerty', 'terms_of_use': True,
                'newsletter': True}
        response = self.client.post(reverse('users:sign_up'), data)

        actual_user = User.objects.get_by_natural_key('rick')
        self.assertEqual(actual_user.profile.newsletter, True)

    def test_do_not_create_if_email_is_invalid(self):
        data = {'username': 'rick', 'email': 'invalid42.com', 'password': 'qwerty'}
        response = self.client.post(reverse('users:sign_up'), data)

        self.assertEqual(response.status_code, 200)
        self.assertRaises(User.DoesNotExist, User.objects.get_by_natural_key, 'rick')

    def test_do_not_create_if_no_email_given(self):
        data = {'username': 'rick', 'email': '', 'password': 'qwerty'}
        response = self.client.post(reverse('users:sign_up'), data)

        self.assertEqual(response.status_code, 200)
        self.assertRaises(User.DoesNotExist, User.objects.get_by_natural_key, 'rick')

    def test_do_not_create_if_terms_of_use_not_accepted(self):
        data = {'username': 'rick', 'email': '', 'password': 'qwerty', 'terms_of_use': False}
        response = self.client.post(reverse('users:sign_up'), data)

        self.assertEqual(response.status_code, 200)
        self.assertRaises(User.DoesNotExist, User.objects.get_by_natural_key, 'rick')
