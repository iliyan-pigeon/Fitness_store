from django.test import TestCase, Client
from django.urls import reverse


class AboutUsPageViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_about_us_page_view(self):
        response = self.client.get(reverse('about us'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_us.html')
