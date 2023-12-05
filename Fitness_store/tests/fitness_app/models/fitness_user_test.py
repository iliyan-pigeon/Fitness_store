from django.core.exceptions import ValidationError
from django.test import TestCase
from Fitness_store.fitness_app.models import FitnessUser
from django.core.files.uploadedfile import SimpleUploadedFile


class FitnessUserTest(TestCase):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    GENDER_MAX_LENGTH = 1

    def setUp(self):
        self.VALID_DATA = {
            'first_name': 'Test First Name',
            'last_name': 'Test Last Name',
            'email': 'test@email.com',
            'gender': 'Male',
            'profile_picture': SimpleUploadedFile('test_photo.jpg', b'content', content_type='image/jpeg')
        }
        self.fitness_user = FitnessUser.objects.create(**self.VALID_DATA)

    def test_valid_gym_equipment_creation(self):
        self.assertEqual(self.fitness_user.first_name, 'Test First Name')
        self.assertEqual(self.fitness_user.last_name, 'Test Last Name')
        self.assertEqual(self.fitness_user.email, 'test@email.com')
        self.assertEqual(self.fitness_user.gender, 'Male')
        self.assertTrue(self.fitness_user.profile_picture.name.endswith('.jpg'))

    def test_when_first_name_is_longer_than__max_length(self):
        self.fitness_user.first_name = 'a' * self.FIRST_NAME_MAX_LENGTH + 'a'

        with self.assertRaises(ValidationError) as ve:
            self.fitness_user.full_clean()

        expected_error_message = [f'Ensure this value has at most {self.FIRST_NAME_MAX_LENGTH} characters'
                                  f' (it has {self.FIRST_NAME_MAX_LENGTH + 1}).']
        self.assertEqual(expected_error_message, ve.exception.message_dict.get('first_name'))

    def test_when_first_name_is_shorter_than__MinLengthValidator(self):
        self.fitness_user.first_name = 'a' * (self.FIRST_NAME_MIN_LENGTH - 1)

        with self.assertRaises(ValidationError) as ve:
            self.fitness_user.full_clean()

        expected_error_message = [f'Ensure this value has at least {self.FIRST_NAME_MIN_LENGTH}'
                                  f' characters (it has {self.FIRST_NAME_MIN_LENGTH - 1}).']
        self.assertEqual(expected_error_message, ve.exception.message_dict.get('first_name'))

    def test_when_last_name_is_longer_than__max_length(self):
        self.fitness_user.last_name = 'a' * self.LAST_NAME_MAX_LENGTH + 'a'

        with self.assertRaises(ValidationError) as ve:
            self.fitness_user.full_clean()

        expected_error_message = [f'Ensure this value has at most {self.LAST_NAME_MAX_LENGTH} characters'
                                  f' (it has {self.LAST_NAME_MAX_LENGTH + 1}).']
        self.assertEqual(expected_error_message, ve.exception.message_dict.get('last_name'))

    def test_when_last_name_is_shorter_than__MinLengthValidator(self):
        self.fitness_user.last_name = 'a' * (self.LAST_NAME_MIN_LENGTH - 1)

        with self.assertRaises(ValidationError) as ve:
            self.fitness_user.full_clean()

        expected_error_message = [f'Ensure this value has at least {self.LAST_NAME_MIN_LENGTH}'
                                  f' characters (it has {self.LAST_NAME_MIN_LENGTH - 1}).']
        self.assertEqual(expected_error_message, ve.exception.message_dict.get('last_name'))

    def test_when_email_is_in_wrong_format(self):
        self.fitness_user.email = 'testemail.com'

        with self.assertRaises(ValidationError) as ve:
            self.fitness_user.full_clean()

        expected_error_message = ['Enter a valid email address.']
        self.assertEqual(expected_error_message, ve.exception.message_dict.get('email'))

        self.fitness_user.email = 'test@emailcom'

        with self.assertRaises(ValidationError) as ve:
            self.fitness_user.full_clean()

        expected_error_message = ['Enter a valid email address.']
        self.assertEqual(expected_error_message, ve.exception.message_dict.get('email'))

    def test_when_gender_is_not_a_valid_choice(self):
        self.fitness_user.gender = 'Male'

        with self.assertRaises(ValidationError) as ve:
            self.fitness_user.full_clean()

        expected_error_message = ["Value 'Male' is not a valid choice."]
        self.assertEqual(expected_error_message, ve.exception.message_dict.get('gender'))
