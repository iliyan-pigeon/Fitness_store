from django.test import TestCase
from django.urls import reverse


class SuccessViewTest(TestCase):

    def test_success_view(self):
        success_url = reverse('success')
        response = self.client.get(success_url)

        self.assertTemplateUsed(response, 'success.html')

