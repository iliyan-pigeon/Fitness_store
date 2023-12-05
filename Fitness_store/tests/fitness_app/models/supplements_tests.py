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
        self.assertEqual(self.supplement.name, 'Test Supplement')
        self.assertEqual(self.supplement.description, 'This is a test supplement description.')
        self.assertEqual(self.supplement.best_selling, True)
        self.assertEqual(self.supplement.amount, 100)
        self.assertEqual(self.supplement.amount_type, 'mg')
        self.assertEqual(self.supplement.price, 10.99)
        self.assertEqual(self.supplement.amount_in_stock, 50)
        self.assertTrue(self.supplement.photo.name.endswith('.jpg'))

#    def test_when_name_is_longer_than__max_length(self):
#        self.supplement += 'a' * 16
#
#        with self.assertRaises(ValueError) as ve:
#            self.assertEqual(supplement.name, 'Test Supplement')
