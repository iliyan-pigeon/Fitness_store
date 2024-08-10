from django.core.exceptions import ValidationError
from django.test import TestCase
from Fitness_store.fitness_app.models import GymEquipment
from django.core.files.uploadedfile import SimpleUploadedFile


class GymEquipmentTest(TestCase):
    NAME_MAX_LENGTH = 30
    NAME_MIN_LENGTH = 2
    DESCRIPTION_MAX_LENGTH = 300
    DESCRIPTION_MIN_LENGTH = 5

    def setUp(self):
        self.VALID_DATA = {
            'name': 'Test Gym Equipment',
            'description': 'This is a test gym equipment description.',
            'price': 10.99,
            'amount_in_stock': 50,
            'photo': SimpleUploadedFile('test_photo.jpg', b'content', content_type='image/jpeg')
        }
        self.gym_equipment = GymEquipment.objects.create(**self.VALID_DATA)

    def test_valid_gym_equipment_creation(self):
        self.assertEqual(self.gym_equipment.name, 'Test Gym Equipment')
        self.assertEqual(self.gym_equipment.description, 'This is a test gym equipment description.')
        self.assertEqual(self.gym_equipment.best_selling, False)
        self.assertEqual(self.gym_equipment.price, 10.99)
        self.assertEqual(self.gym_equipment.amount_in_stock, 50)
        self.assertTrue(self.gym_equipment.photo.name.endswith('.jpg'))

    def test_when_name_is_longer_than__max_length(self):
        self.gym_equipment.name = 'a' * self.NAME_MAX_LENGTH + 'a'

        with self.assertRaises(ValidationError) as ve:
            self.gym_equipment.full_clean()

        expected_error_message = {'name': [f'Ensure this value has at most '
                                           f'{self.NAME_MAX_LENGTH} characters (it has {self.NAME_MAX_LENGTH + 1}).']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_name_is_shorter_than__MinLengthValidator(self):
        self.gym_equipment.name = 'a' * (self.NAME_MIN_LENGTH - 1)

        with self.assertRaises(ValidationError) as ve:
            self.gym_equipment.full_clean()

        expected_error_message = {'name': [f'Ensure this value has at least {self.NAME_MIN_LENGTH}'
                                           f' characters (it has {self.NAME_MIN_LENGTH - 1}).']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_name_is_null(self):
        self.gym_equipment.name = None

        with self.assertRaises(ValidationError) as ve:
            self.gym_equipment.full_clean()

        expected_error_message = {'name': ['This field cannot be null.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_name_is_blank(self):
        self.gym_equipment.name = ''

        with self.assertRaises(ValidationError) as ve:
            self.gym_equipment.full_clean()

        expected_error_message = {'name': ['This field cannot be blank.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_description_is_longer_than__max_length(self):
        self.gym_equipment.description = 'a' * self.DESCRIPTION_MAX_LENGTH + 'a'

        with self.assertRaises(ValidationError) as ve:
            self.gym_equipment.full_clean()

        expected_error_message = {'description': [f'Ensure this value has at most {self.DESCRIPTION_MAX_LENGTH}'
                                                  f' characters (it has {self.DESCRIPTION_MAX_LENGTH + 1}).']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_description_is_shorter_than__MinLengthValidator(self):
        self.gym_equipment.description = 'a' * (self.DESCRIPTION_MIN_LENGTH - 1)

        with self.assertRaises(ValidationError) as ve:
            self.gym_equipment.full_clean()

        expected_error_message = {'description': [f'Ensure this value has at least {self.DESCRIPTION_MIN_LENGTH}'
                                                  f' characters (it has {self.DESCRIPTION_MIN_LENGTH - 1}).']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_description_is_null(self):
        self.gym_equipment.description = None

        with self.assertRaises(ValidationError) as ve:
            self.gym_equipment.full_clean()

        expected_error_message = {'description': ['This field cannot be null.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_description_is_blank(self):
        self.gym_equipment.description = ''

        with self.assertRaises(ValidationError) as ve:
            self.gym_equipment.full_clean()

        expected_error_message = {'description': ['This field cannot be blank.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_best_selling_is_null(self):
        self.gym_equipment.best_selling = None

        with self.assertRaises(ValidationError) as ve:
            self.gym_equipment.full_clean()

        expected_error_message = {'best_selling': ['“None” value must be either True or False.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_best_selling_is_blank(self):
        self.gym_equipment.best_selling = ''

        with self.assertRaises(ValidationError) as ve:
            self.gym_equipment.full_clean()

        expected_error_message = {'best_selling': ['“” value must be either True or False.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_true_assigned_to_best_selling(self):
        self.gym_equipment.best_selling = True

        self.assertEqual(self.gym_equipment.best_selling, True)

    def test_when_price_is_null(self):
        self.gym_equipment.price = None

        with self.assertRaises(ValidationError) as ve:
            self.gym_equipment.full_clean()

        expected_error_message = {'price': ['This field cannot be null.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_price_is_blank(self):
        self.gym_equipment.price = ''

        with self.assertRaises(ValidationError) as ve:
            self.gym_equipment.full_clean()

        expected_error_message = {'price': ['“” value must be a float.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_amount_in_stock_is_null(self):
        self.gym_equipment.amount_in_stock = None

        with self.assertRaises(ValidationError) as ve:
            self.gym_equipment.full_clean()

        expected_error_message = {'amount_in_stock': ['This field cannot be null.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_amount_in_stock_is_blank(self):
        self.gym_equipment.amount_in_stock = ''

        with self.assertRaises(ValidationError) as ve:
            self.gym_equipment.full_clean()

        expected_error_message = {'amount_in_stock': ['“” value must be an integer.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_photo_is_null(self):
        self.gym_equipment.photo = None

        with self.assertRaises(ValidationError) as ve:
            self.gym_equipment.full_clean()

        expected_error_message = {'photo': ['This field cannot be blank.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_photo_is_blank(self):
        self.gym_equipment.photo = ''

        with self.assertRaises(ValidationError) as ve:
            self.gym_equipment.full_clean()

        expected_error_message = {'photo': ['This field cannot be blank.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)
        