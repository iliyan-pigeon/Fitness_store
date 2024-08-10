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
            'order': self.valid_order,
            'name': 'Test Product',
            'price': 10.50,
            'quantity': 2,
            'product_type': 'Type A'
        }
        self.order_item = OrderItem.objects.create(**self.VALID_DATA)

    def test_valid_order_item_creation(self):
        self.assertEqual(self.order_item.order, self.valid_order)
        self.assertEqual(self.order_item.name, 'Test Product')
        self.assertEqual(self.order_item.price, 10.50)
        self.assertEqual(self.order_item.quantity, 2)
        self.assertEqual(self.order_item.product_id, 1)
        self.assertEqual(self.order_item.product_type, 'Type A')

    def test_when_delete_order_if_also_deletes_order_items(self):
        self.assertEqual(OrderItem.objects.filter(order=self.valid_order).count(), 1)

        self.valid_order.delete()

        self.assertEqual(OrderItem.objects.filter(order=self.valid_order).count(), 0)

    def test_when_name_is_longer_than_the__max_length(self):
        self.order_item.name = 'a' * (self.MAX_LENGTH_NAME + 1)

        with self.assertRaises(ValidationError) as ve:
            self.order_item.full_clean()

        expected_error_message = {'name': [f'Ensure this value has at most {self.MAX_LENGTH_NAME} characters'
                                           f' (it has {self.MAX_LENGTH_NAME + 1}).']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_price_digits_are_more_than__max_digits(self):
        self.order_item.price = 123456789012

        with self.assertRaises(ValidationError) as ve:
            self.order_item.full_clean()

        expected_error_message = {'price': [f'Ensure that there are no more than {self.MAX_DIGITS_PRICE}'
                                            f' digits in total.']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_the_price_decimal_places(self):
        self.order_item.price = 10

        self.assertEqual(self.order_item.price, 10.00)

    def test_default_item_quantity(self):
        new_cart_item = OrderItem.objects.create(order=self.valid_order, name='Another Product', price=5.00)

        self.assertEqual(new_cart_item.quantity, self.DEFAULT_QUANTITY)

    def test_when_product_type_is_longer_than__max_length(self):
        self.order_item.product_type = 'a' * (self.MAX_LENGTH_NAME + 1)

        with self.assertRaises(ValidationError) as ve:
            self.order_item.full_clean()

        expected_error_message = {'product_type': [f'Ensure this value has at most {self.MAX_LENGTH_NAME} characters'
                                                   f' (it has {self.MAX_LENGTH_NAME + 1}).']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)