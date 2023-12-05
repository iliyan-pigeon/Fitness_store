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
