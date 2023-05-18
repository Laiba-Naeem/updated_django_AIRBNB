

from django.urls import reverse, resolve
from django.test import SimpleTestCase
from accounts.views import RegisterAPI
# from accounts.models import User


class ApiUrlTests(SimpleTestCase):

    def test_get_api_register(self):
        url = reverse('register')
        # print(url)
        print(resolve(url).func)
        self.assertEquals(resolve(url).func.view_class, RegisterAPI)
