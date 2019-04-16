import datetime

from django.test import TestCase
from django.utils import timezone

from main.models import Demo


class DemoTestCase(TestCase):
    def setUp(self):
        Demo.objects.create(title="Example Title",
                            starting_time=timezone.now(),
                            ending_time=timezone.now() + datetime.timedelta(days=1)).save()

    def test_smoke(self):
        """
        example smoke test
        """
        demo = Demo.objects.get(title="Example Title")
        self.assertEqual(demo.title, "Example Title")
