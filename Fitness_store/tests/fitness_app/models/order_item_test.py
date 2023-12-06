from django.core.exceptions import ValidationError
from django.test import TestCase
from Fitness_store.fitness_app.models import Order, OrderItem


class OrderItemTest(TestCase):
    MAX_LENGTH_NAME = 30
    MAX_DIGITS_PRICE = 10
    DECIMAL_PLACES = 2
    DEFAULT_QUANTITY = 1

    def setUp(self):
        self.valid_order = Order.objects.create(session_key='test_session')
        self.VALID_DATA = {
            'cart': self.valid_order,
            'name': 'Test Product',
            'price': 10.50,
            'quantity': 2,
            'product_type': 'Type A'
        }
        self.order_item = OrderItem.objects.create(**self.VALID_DATA)
