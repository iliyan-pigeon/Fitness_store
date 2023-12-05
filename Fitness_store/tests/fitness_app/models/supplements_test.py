from django.core.exceptions import ValidationError
from django.test import TestCase
from Fitness_store.fitness_app.models import Supplements
from django.core.files.uploadedfile import SimpleUploadedFile


class SupplementsTest(TestCase):
    NAME_MAX_LENGTH = 30
    NAME_MIN_LENGTH = 2
    DESCRIPTION_MAX_LENGTH = 300
    DESCRIPTION_MIN_LENGTH = 5
    AMOUNT_TYPE_MAX_LENGTH = 30

    def setUp(self):
        self.VALID_DATA = {
            'name': 'Test Supplement',
            'description': 'This is a test supplement description.',
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
        self.assertEqual(self.supplement.best_selling, False)
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

    def test_when_description_is_null(self):
        self.supplement.description = None

        with self.assertRaises(ValidationError) as ve:
            self.supplement.full_clean()

        expected_error_message = {'description': ['This field cannot be null.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_description_is_blank(self):
        self.supplement.description = ''

        with self.assertRaises(ValidationError) as ve:
            self.supplement.full_clean()

        expected_error_message = {'description': ['This field cannot be blank.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_best_selling_is_null(self):
        self.supplement.best_selling = None

        with self.assertRaises(ValidationError) as ve:
            self.supplement.full_clean()

        expected_error_message = {'best_selling': ['“None” value must be either True or False.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_best_selling_is_blank(self):
        self.supplement.best_selling = ''

        with self.assertRaises(ValidationError) as ve:
            self.supplement.full_clean()

        expected_error_message = {'best_selling': ['“” value must be either True or False.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_true_assigned_to_best_selling(self):
        self.supplement.best_selling = True

        self.assertEqual(self.supplement.best_selling, True)

    def test_when_amount_is_null(self):
        self.supplement.amount = None

        with self.assertRaises(ValidationError) as ve:
            self.supplement.full_clean()

        expected_error_message = {'amount': ['This field cannot be null.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_amount_is_blank(self):
        self.supplement.amount = ''

        with self.assertRaises(ValidationError) as ve:
            self.supplement.full_clean()

        expected_error_message = {'amount': ['“” value must be an integer.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_amount_type_is_null(self):
        self.supplement.amount_type = None

        with self.assertRaises(ValidationError) as ve:
            self.supplement.full_clean()

        expected_error_message = {'amount_type': ['This field cannot be null.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_amount_type_is_blank(self):
        self.supplement.amount_type = ''

        with self.assertRaises(ValidationError) as ve:
            self.supplement.full_clean()

        expected_error_message = {'amount_type': ['This field cannot be blank.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_amount_type_is_longer_than__max_length(self):
        self.supplement.amount_type = 'a' * self.AMOUNT_TYPE_MAX_LENGTH + 'a'

        with self.assertRaises(ValidationError) as ve:
            self.supplement.full_clean()

        expected_error_message = {'amount_type': [f'Ensure this value has at most {self.NAME_MAX_LENGTH} characters'
                                                  f' (it has {self.NAME_MAX_LENGTH + 1}).']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_price_is_null(self):
        self.supplement.price = None

        with self.assertRaises(ValidationError) as ve:
            self.supplement.full_clean()

        expected_error_message = {'price': ['This field cannot be null.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_price_is_blank(self):
        self.supplement.price = ''

        with self.assertRaises(ValidationError) as ve:
            self.supplement.full_clean()

        expected_error_message = {'price': ['“” value must be a float.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_amount_in_stock_is_null(self):
        self.supplement.amount_in_stock = None

        with self.assertRaises(ValidationError) as ve:
            self.supplement.full_clean()

        expected_error_message = {'amount_in_stock': ['This field cannot be null.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_amount_in_stock_is_blank(self):
        self.supplement.amount_in_stock = ''

        with self.assertRaises(ValidationError) as ve:
            self.supplement.full_clean()

        expected_error_message = {'amount_in_stock': ['“” value must be an integer.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_photo_is_null(self):
        self.supplement.photo = None

        with self.assertRaises(ValidationError) as ve:
            self.supplement.full_clean()

        expected_error_message = {'photo': ['This field cannot be blank.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_photo_is_blank(self):
        self.supplement.photo = ''

        with self.assertRaises(ValidationError) as ve:
            self.supplement.full_clean()

        expected_error_message = {'photo': ['This field cannot be blank.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)
        