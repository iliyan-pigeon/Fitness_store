from django.core.exceptions import ValidationError
from django.test import TestCase
from Fitness_store.fitness_app.models import Order, FitnessUser
from django.utils import timezone


class OrderTest(TestCase):
    ADDRESS_MAX_LENGTH = 200
    CITY_MAX_LENGTH = 200
    REGION_MAX_LENGTH = 200
    ZIPCODE_MAX_LENGTH = 200

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

    def test_valid_order_creation(self):
        self.assertEqual(self.order.user, self.valid_user)
        self.assertEqual(self.order.session_key, 'test_session_key')
        self.assertEqual(self.order.address, '123 Test St')
        self.assertEqual(self.order.city, 'Test City')
        self.assertEqual(self.order.region, 'Test Region')
        self.assertEqual(self.order.zipcode, '12345')
        self.assertIsNotNone(self.order.date_added)
        self.assertEqual(self.order.status, Order.PENDING)
        self.assertIsNone(self.order.payment)

    def test_order_str_representation(self):
        self.assertEqual(str(self.order), "123 Test St")

    def test_update_order_status(self):
        self.order.status = Order.DELIVERED
        self.order.save()
        updated_order = Order.objects.get(pk=self.order.pk)

        self.assertEqual(updated_order.status, Order.DELIVERED)

    def test_delete_order(self):
        order_id = self.order.id
        self.order.delete()
        with self.assertRaises(self.order.DoesNotExist):
            Order.objects.get(pk=order_id)

    def test_empty_user(self):
        order_empty_user = Order.objects.create(session_key='empty_user_order', address='Empty User Address')
        self.assertIsNone(order_empty_user.user)

    def test_empty_session_key(self):
        order_empty_user = Order.objects.create(user=self.valid_user, address='Test User Address')
        self.assertIsNone(order_empty_user.session_key)

    def test_when_address_is_longer_than__max_length(self):
        self.order.address = 'a' * (self.ADDRESS_MAX_LENGTH + 1)

        with self.assertRaises(ValidationError) as ve:
            self.order.full_clean()

        expected_error_message = {'address': [f'Ensure this value has at most {self.ADDRESS_MAX_LENGTH} characters'
                                              f' (it has {self.ADDRESS_MAX_LENGTH + 1}).']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_city_is_longer_than__max_length(self):
        self.order.city = 'a' * (self.CITY_MAX_LENGTH + 1)

        with self.assertRaises(ValidationError) as ve:
            self.order.full_clean()

        expected_error_message = {'city': [f'Ensure this value has at most {self.ADDRESS_MAX_LENGTH} characters'
                                           f' (it has {self.ADDRESS_MAX_LENGTH + 1}).']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_region_is_longer_than__max_length(self):
        self.order.region = 'a' * (self.REGION_MAX_LENGTH + 1)

        with self.assertRaises(ValidationError) as ve:
            self.order.full_clean()

        expected_error_message = {'region': [f'Ensure this value has at most {self.ADDRESS_MAX_LENGTH} characters'
                                             f' (it has {self.ADDRESS_MAX_LENGTH + 1}).']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_zipcode_is_longer_than__max_length(self):
        self.order.zipcode = 'a' * (self.ZIPCODE_MAX_LENGTH + 1)

        with self.assertRaises(ValidationError) as ve:
            self.order.full_clean()

        expected_error_message = {'zipcode': [f'Ensure this value has at most {self.ADDRESS_MAX_LENGTH} characters'
                                              f' (it has {self.ADDRESS_MAX_LENGTH + 1}).']}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_changing_valid_status(self):
        self.order.status = 'ORDERED'

        self.assertEqual(self.order.status, 'ORDERED')

    def test_when_changing_invalid_status(self):
        self.order.status = 'TEST'

        with self.assertRaises(ValidationError) as ve:
            self.order.full_clean()

        expected_error_message = {'status': [f"Value '{self.order.status}' is not a valid choice."]}
        self.assertEqual(expected_error_message, ve.exception.message_dict)

    def test_when_changing_payment_status(self):
        self.order.payment = 'card'

        self.assertEqual(self.order.payment, 'card')
