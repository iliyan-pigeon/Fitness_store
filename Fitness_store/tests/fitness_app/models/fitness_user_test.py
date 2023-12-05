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

