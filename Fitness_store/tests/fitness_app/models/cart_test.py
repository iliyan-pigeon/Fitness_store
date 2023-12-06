from django.test import TestCase
from Fitness_store.fitness_app.models import Cart, FitnessUser
from django.utils import timezone


class CartTest(TestCase):
    SESSION_KEY_MAX_LENGTH = 50

    def setUp(self):
        self.valid_user = FitnessUser.objects.create(username='testuser', email='test@example.com')
        self.VALID_DATA = {
            'user': self.valid_user,
            'created_at': timezone.now(),
            'session_key': 'test_session_key'
        }
        self.cart = Cart.objects.create(**self.VALID_DATA)
        