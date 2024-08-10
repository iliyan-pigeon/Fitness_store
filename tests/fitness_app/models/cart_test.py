from django.core.exceptions import ValidationError
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

    def test_valid_cart_creation(self):
        self.assertEqual(self.cart.user, self.valid_user)
        self.assertIsNotNone(self.cart.created_at)
        self.assertEqual(self.cart.session_key, 'test_session_key')

    def test_when_session_key_is_longer_than_max_length(self):
        self.cart.session_key = 'a' * (self.SESSION_KEY_MAX_LENGTH + 1)

        with self.assertRaises(ValidationError) as ve:
            self.cart.full_clean()

        expected_error_message = {'session_key': [f'Ensure this value has at most {self.SESSION_KEY_MAX_LENGTH}'
                                                  f' characters (it has {self.SESSION_KEY_MAX_LENGTH+1}).']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_str_representation_with_user(self):

        self.assertEqual(str(self.cart), f"Cart for testuser")

    def test_str_representation_without_user(self):
        self.cart.user = None
        self.assertEqual(str(self.cart), f"Guest Cart")
