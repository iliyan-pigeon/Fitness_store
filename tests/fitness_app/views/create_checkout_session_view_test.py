from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from unittest.mock import patch
from django.http import JsonResponse
from Fitness_store.fitness_app.models import Cart, CartItem, Supplements, GymEquipment, Order
import stripe

UserModel = get_user_model()


class CreateCheckoutSessionViewTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(username='testuser', password='testpassword')
        self.cart = Cart.objects.create(user=self.user)

    def test_authenticated_user_with_cart_items(self):
        self.client.force_login(self.user)
        self.cart = Cart.objects.create(user=self.user)

        url = reverse('create-checkout-session')
        response = self.client.post(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)

#    def test_anonymous_user_with_cart_id_in_session(self):
#        # Create a cart with a specific session key
#        self.cart = Cart.objects.create(session_key='some_key')
#
#        # Store the cart ID in the session
#        self.client.session['cart_id'] = self.cart.id
#
#        # Verify that the cart is created and session key is set correctly
#        self.assertTrue(Cart.objects.filter(session_key='some_key').exists())
#        #self.assertEqual(self.client.session.get('cart_id'), self.cart.id)
#
#        #url = reverse('create-checkout-session')
#        #response = self.client.post(url)
#
#        #self.assertEqual(response.status_code, 200)
#        #self.assertIsInstance(response, JsonResponse)
#
#    def test_invalid_cart_id(self):
#        # Simulate an anonymous user with an invalid cart ID in the session
#        self.client.session['cart_id'] = 99999  # Use an invalid cart ID
#
#        url = reverse('create-checkout-session')
#        response = self.client.post(url)
#
#        self.assertEqual(response.status_code, 404)  # Change status code as needed
#
#    @patch('stripe.checkout.Session.create')
#    def test_checkout_session_creation(self, mock_checkout_session):
#        mock_checkout_session.return_value.id = 'fake_checkout_session_id'
#
#        # Set up cart items and call the view
#        # ...
#
#        url = reverse('create-checkout-session')
#        response = self.client.post(url)
#
#        self.assertEqual(response.status_code, 200)
#        self.assertTrue('id' in response.json())
#
#        # Verify Stripe Session.create was called with correct arguments
#        mock_checkout_session.assert_called_once()
#
#    # Add more tests for cart item reduction, order creation, success/cancel URLs, etc.