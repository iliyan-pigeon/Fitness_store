from django.test import TestCase
from Fitness_store.fitness_app.models import Order, FitnessUser
from django.utils import timezone


class OrderTest(TestCase):

    def setUp(self):
        self.valid_user = FitnessUser.objects.create(username='testuser', email='test@example.com')
        self.VALID_DATA = {
            'user': self.valid_user,
            'session_key': 'test_session_key',
            'address': '123 Test St',
            'city': 'Test City',
            'region': 'Test Region',
            'zipcode': '12345',
            'date_added': timezone.now(),
        }
        self.order = Order.objects.create(**self.VALID_DATA)
        