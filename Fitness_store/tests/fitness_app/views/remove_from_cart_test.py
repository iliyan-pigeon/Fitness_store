from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test.client import RequestFactory
from Fitness_store.fitness_app.views import remove_from_cart, add_to_cart
from Fitness_store.fitness_app.models import Supplements, GymEquipment, CartItem

UserModel = get_user_model()


class RemoveFromCartViewTest(TestCase):

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

    def test_remove_supplement_from_cart(self):
        request = self.factory.get(self.cart_url)
        request.user = self.user

        add_response = add_to_cart(request, 'supplement', self.supplement_product.id)
        self.assertEqual(add_response.status_code, 302)

        remove_response = remove_from_cart(request, 'supplement', self.supplement_product.id)
        self.assertEqual(remove_response.status_code, 302)

        cart_item = CartItem.objects.filter(cart__user=self.user, product_type='supplement').first()
        self.assertIsNone(cart_item)

    def test_remove_equipment_from_cart(self):
        request = self.factory.get(self.cart_url)
        request.user = self.user

        add_response = add_to_cart(request, 'gym_equipment', self.equipment_product.id)
        self.assertEqual(add_response.status_code, 302)

        remove_response = remove_from_cart(request, 'gym_equipment', self.equipment_product.id)
        self.assertEqual(remove_response.status_code, 302)

        cart_item = CartItem.objects.filter(cart__user=self.user, product_type='gym_equipment').first()
        self.assertIsNone(cart_item)
