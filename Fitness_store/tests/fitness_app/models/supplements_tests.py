from django.core.exceptions import ValidationError
from django.test import TestCase
from Fitness_store.fitness_app.models import Supplements
from django.core.files.uploadedfile import SimpleUploadedFile


class SupplementsTest(TestCase):
    NAME_MAX_LENGTH = 30
    NAME_MIN_LENGTH = 2
    DESCRIPTION_MAX_LENGTH = 300
    DESCRIPTION_MIN_LENGTH = 5

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

    def test_when_name_is_longer_than__max_length(self):
        self.supplement.name = 'a' * self.NAME_MAX_LENGTH + 'a'

        with self.assertRaises(ValidationError) as ve:
            self.supplement.full_clean()

        expected_error_message = {'name': [f'Ensure this value has at most '
                                           f'{self.NAME_MAX_LENGTH} characters (it has {self.NAME_MAX_LENGTH + 1}).']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_name_is_shorter_than__MinLengthValidator(self):
        self.supplement.name = 'a' * (self.NAME_MIN_LENGTH - 1)

        with self.assertRaises(ValidationError) as ve:
            self.supplement.full_clean()

        expected_error_message = {'name': [f'Ensure this value has at least {self.NAME_MIN_LENGTH}'
                                           f' characters (it has {self.NAME_MIN_LENGTH - 1}).']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_name_is_null(self):
        self.supplement.name = None

        with self.assertRaises(ValidationError) as ve:
            self.supplement.full_clean()

        expected_error_message = {'name': ['This field cannot be null.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_name_is_blank(self):
        self.supplement.name = ''

        with self.assertRaises(ValidationError) as ve:
            self.supplement.full_clean()

        expected_error_message = {'name': ['This field cannot be blank.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_description_is_longer_than__max_length(self):
        self.supplement.description = 'a' * self.DESCRIPTION_MAX_LENGTH + 'a'
        print(len(self.supplement.description))

        with self.assertRaises(ValidationError) as ve:
            self.supplement.full_clean()

        expected_error_message = {'description': [f'Ensure this value has at most {self.DESCRIPTION_MAX_LENGTH}'
                                                  f' characters (it has {self.DESCRIPTION_MAX_LENGTH + 1}).']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_description_is_shorter_than__MinLengthValidator(self):
        self.supplement.description = 'a' * (self.DESCRIPTION_MIN_LENGTH - 1)

        with self.assertRaises(ValidationError) as ve:
            self.supplement.full_clean()

        expected_error_message = {'description': [f'Ensure this value has at least {self.DESCRIPTION_MIN_LENGTH}'
                                                  f' characters (it has {self.DESCRIPTION_MIN_LENGTH - 1}).']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

#    def test_when_name_is_null(self):
#        self.supplement.name = None
#
#        with self.assertRaises(ValidationError) as ve:
#            self.supplement.full_clean()
#
#        expected_error_message = {'name': ['This field cannot be null.']}
#        self.assertEqual(expected_error_message, ve.exception.message_dict)
#
#    def test_when_name_is_blank(self):
#        self.supplement.name = ''
#
#        with self.assertRaises(ValidationError) as ve:
#            self.supplement.full_clean()
#
#        expected_error_message = {'name': ['This field cannot be blank.']}
#        self.assertEqual(expected_error_message, ve.exception.message_dict)
