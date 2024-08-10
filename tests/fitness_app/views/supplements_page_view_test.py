from django.test import TestCase, Client
from django.urls import reverse
from Fitness_store.fitness_app.models import Supplements


class SupplementsPageViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_supplements_page_view(self):
        response = self.client.get(reverse('supplements'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'supplements.html')
        self.assertTrue('object_list' in response.context)
        self.assertTrue(all(isinstance(item, Supplements) for item in response.context['object_list']))
        for supplement in response.context['object_list']:
            self.assertContains(response, supplement.name)
        self.assertNotContains(response, 'This text should not be in the supplements page')
