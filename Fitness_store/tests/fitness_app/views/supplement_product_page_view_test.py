from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse
from Fitness_store.fitness_app.models import Supplements


class SupplementProductPageViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.VALID_DATA = {
            'name': 'Test Supplement',
            'description': 'This is a test supplement description.',
            'amount': 100,
            'amount_type': 'mg',
            'price': 10.99,
            'amount_in_stock': 50,
            'photo': SimpleUploadedFile('test_photo.jpg', b'content', content_type='image/jpeg')
        }
        self.supplement_product = Supplements.objects.create(**self.VALID_DATA)

    def test_supplement_product_page_view(self):
        url = reverse('supplement product', kwargs={'pk': self.supplement_product.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'supplement_product.html')
        self.assertTrue('object' in response.context)
        self.assertEqual(response.context['object'], self.supplement_product)
        self.assertContains(response, self.supplement_product.name)
        self.assertNotContains(response, 'This text should not be in the equipment product page')
