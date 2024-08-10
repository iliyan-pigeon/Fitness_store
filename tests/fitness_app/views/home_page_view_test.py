from django.test import TestCase, Client
from django.urls import reverse


class HomePageViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_page_view(self):
        response = self.client.get(reverse('homepage'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')
        self.assertTrue('best_selling_supplements' in response.context)
        self.assertTrue('best_selling_gym_equipment' in response.context)
        