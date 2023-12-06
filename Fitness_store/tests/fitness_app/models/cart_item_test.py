from django.test import TestCase
from Fitness_store.fitness_app.models import CartItem, Cart


class CartItemTest(TestCase):
    MAX_LENGTH_NAME = 30
    MAX_DIGITS_PRICE = 10
    DECIMAL_PLACES = 2
    DEFAULT_QUANTITY = 1

    def setUp(self):
        self.valid_cart = Cart.objects.create(session_key='test_session')
        self.VALID_DATA = {
            'cart': self.valid_cart,
            'name': 'Test Product',
            'price': 10.50,
            'quantity': 2,
            'product_id': 12345,
            'product_type': 'Type A'
        }
        self.cart_item = CartItem.objects.create(**self.VALID_DATA)
        