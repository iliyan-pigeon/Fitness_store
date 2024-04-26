from django.test import TestCase
from Fitness_store.fitness_app.forms import OrderAddressForm


class OrderAddressFormTest(TestCase):

    def test_valid_order_address(self):
        form_data = {
            'address': '123 Test St',
            'city': 'Test City',
            'region': 'Test Region',
            'zipcode': '12345'
        }
        form = OrderAddressForm(data=form_data)
        self.assertTrue(form.is_valid())
