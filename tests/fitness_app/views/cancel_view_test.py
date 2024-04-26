from django.test import TestCase
from django.urls import reverse


class CancelViewTest(TestCase):
    
    def test_cancel_view(self):
        cancel_url = reverse('cancel')
        response = self.client.get(cancel_url)

        self.assertTemplateUsed(response, 'cancel.html')
