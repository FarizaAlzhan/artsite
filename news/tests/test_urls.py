from django.test import SimpleTestCase
from django.urls import reverse, resolve
from news.views import *


class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')