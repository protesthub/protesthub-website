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
        data = {'username': 'rick', 'email': 'rick@42.com', 'password': 'qwerty'}
        response = self.client.post(reverse('users:sign_up'), data)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(User.objects.get_by_natural_key('rick'))
