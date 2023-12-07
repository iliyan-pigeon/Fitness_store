from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse
from Fitness_store.fitness_app.models import GymEquipment


class EquipmentProductPageViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.VALID_DATA = {
            'name': 'Test Gym Equipment',
            'description': 'This is a test gym equipment description.',
            'price': 10.99,
            'amount_in_stock': 50,
            'photo': SimpleUploadedFile('test_photo.jpg', b'content', content_type='image/jpeg')
        }
        self.equipment_product = GymEquipment.objects.create(**self.VALID_DATA)

    def test_equipment_product_page_view(self):
        url = reverse('equipment product', kwargs={'pk': self.equipment_product.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'equipment_product.html')
        self.assertTrue('object' in response.context)
        self.assertEqual(response.context['object'], self.equipment_product)
        self.assertContains(response, self.equipment_product.name)
        self.assertNotContains(response, 'This text should not be in the equipment product page')
