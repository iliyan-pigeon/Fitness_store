from django.core.exceptions import ValidationError
from django.test import TestCase
from Fitness_store.fitness_app.models import Supplements
from django.core.files.uploadedfile import SimpleUploadedFile


class SupplementsTest(TestCase):

    def setUp(self):
        self.VALID_DATA = {
            'name': 'Test Supplement',
            'description': 'This is a test supplement description.',
            'best_selling': True,
            'amount': 100,
            'amount_type': 'mg',
            'price': 10.99,
            'amount_in_stock': 50,
            'photo': SimpleUploadedFile('test_photo.jpg', b'content', content_type='image/jpeg')
        }
        self.supplement = Supplements.objects.create(**self.VALID_DATA)

    def test_valid_supplement_creation(self):
        supplement = Supplements.objects.get(id=self.supplement.id)
        self.assertEqual(supplement.name, 'Test Supplement')
        self.assertEqual(supplement.description, 'This is a test supplement description.')
        self.assertEqual(supplement.best_selling, True)
        self.assertEqual(supplement.amount, 100)
        self.assertEqual(supplement.amount_type, 'mg')
        self.assertEqual(supplement.price, 10.99)
        self.assertEqual(supplement.amount_in_stock, 50)
        self.assertTrue(supplement.photo.name.endswith('.jpg'))
