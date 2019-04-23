from django.test import TestCase
from django.urls import reverse

from main.users.models import Profile


class ProfileViewTest(TestCase):
    """
    References:
        - https://docs.djangoproject.com/en/2.2/topics/forms/#building-a-form-in-django
        - https://test-driven-django-development.readthedocs.io/en/latest/05-forms.html
        - https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
    """
    def test_create_user(self):
        data = {'username': 'rick', 'email': 'rick@42.com', 'password': 'qwerty', 'terms_of_use': True}
        response = self.client.post(reverse('users:sign_up'), data)

        actual_user = Profile.objects.get_by_natural_key('rick')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(actual_user.username, 'rick')
        self.assertEqual(actual_user.email, 'rick@42.com')
        self.assertEqual(actual_user.terms_of_use, True)
        self.assertEqual(actual_user.newsletter, False)

    def test_accepted_newsletter(self):
        data = {'username': 'rick', 'email': 'rick@42.com', 'password': 'qwerty', 'terms_of_use': True,
                'newsletter': True}
        self.client.post(reverse('users:sign_up'), data)

        actual_user = Profile.objects.get_by_natural_key('rick')
        self.assertEqual(actual_user.newsletter, True)

    def test_duplicated_email_not_allowed(self):
        data = {'username': 'rick', 'email': 'rick@42.com', 'password': 'qwerty', 'terms_of_use': True,
                'newsletter': True}
        self.client.post(reverse('users:sign_up'), data)

        data = {'username': 'morty', 'email': 'rick@42.com', 'password': 'qwerty', 'terms_of_use': True,
                'newsletter': True}
        self.client.post(reverse('users:sign_up'), data)

        self.assertEqual(Profile.objects.filter(email='rick@42.com').count(), 1)

    def test_do_not_create_if_email_is_invalid(self):
        data = {'username': 'rick', 'email': 'invalid42.com', 'password': 'qwerty'}
        response = self.client.post(reverse('users:sign_up'), data)

        self.assertEqual(response.status_code, 200)
        self.assertRaises(Profile.DoesNotExist, Profile.objects.get_by_natural_key, 'rick')

    def test_do_not_create_if_no_email_given(self):
        data = {'username': 'rick', 'email': '', 'password': 'qwerty'}
        response = self.client.post(reverse('users:sign_up'), data)

        self.assertEqual(response.status_code, 200)
        self.assertRaises(Profile.DoesNotExist, Profile.objects.get_by_natural_key, 'rick')

    def test_do_not_create_if_terms_of_use_not_accepted(self):
        data = {'username': 'rick', 'email': '', 'password': 'qwerty', 'terms_of_use': False}
        response = self.client.post(reverse('users:sign_up'), data)

        self.assertEqual(response.status_code, 200)
        self.assertRaises(Profile.DoesNotExist, Profile.objects.get_by_natural_key, 'rick')
