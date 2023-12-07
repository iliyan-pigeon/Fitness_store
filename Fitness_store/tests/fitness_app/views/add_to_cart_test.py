from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.sessions.middleware import SessionMiddleware
from django.test.client import RequestFactory
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from Fitness_store.fitness_app.views import add_to_cart
from Fitness_store.fitness_app.models import Supplements, GymEquipment, CartItem

UserModel = get_user_model()


class AddToCartViewTest(TestCase):
    def setUp(self):
        self.supplement_data = {
            'name': 'Test Supplement',
            'description': 'This is a test supplement description.',
            'amount': 100,
            'amount_type': 'mg',
            'price': 10.99,
            'amount_in_stock': 50,
            'photo': SimpleUploadedFile('test_photo.jpg', b'content', content_type='image/jpeg')
        }

        self.equipment_data = {
            'name': 'Test Gym Equipment',
            'description': 'This is a test gym equipment description.',
            'price': 10.99,
            'amount_in_stock': 50,
            'photo': SimpleUploadedFile('test_photo.jpg', b'content', content_type='image/jpeg')
        }

        self.factory = RequestFactory()
        self.user = UserModel.objects.create_user(username='testuser', password='testpassword')
        self.supplement_product = Supplements.objects.create(**self.supplement_data)
        self.equipment_product = GymEquipment.objects.create(**self.equipment_data)
        self.cart_url = reverse('homepage')

    def test_add_supplement_to_cart(self):
        request = self.factory.get(self.cart_url)
        request.user = self.user

        response = add_to_cart(request, 'supplement', self.supplement_product.id)
        self.assertEqual(response.status_code, 302)
        cart_item = CartItem.objects.filter(cart__user=self.user, product_type='supplement').first()
        self.assertIsNotNone(cart_item)
        self.assertEqual(cart_item.name, 'Test Supplement')

    def test_add_equipment_to_cart(self):
        request = self.factory.get(self.cart_url)
        request.user = self.user

        response = add_to_cart(request, 'gym_equipment', self.equipment_product.id)
        self.assertEqual(response.status_code, 302)
        cart_item = CartItem.objects.filter(cart__user=self.user, product_type='gym_equipment').first()
        self.assertIsNotNone(cart_item)
        self.assertEqual(cart_item.name, 'Test Gym Equipment')
