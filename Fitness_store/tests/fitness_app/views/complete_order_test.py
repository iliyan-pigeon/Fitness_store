from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from Fitness_store.fitness_app.models import Cart, CartItem, Supplements, GymEquipment, Order, OrderItem
from Fitness_store.fitness_app.utils import get_or_create_cart
from Fitness_store.fitness_app.views import complete_order

UserModel = get_user_model()


class CompleteOrderViewTest(TestCase):

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

        self.user = UserModel.objects.create(username='testuser', email='test@example.com')
        self.supplement_product = Supplements.objects.create(**self.supplement_data)
        self.equipment_product = GymEquipment.objects.create(**self.equipment_data)
        self.cart_authenticated = Cart.objects.create(user=self.user)
        self.cart_guest = Cart.objects.create(session_key='test_session_key')
        self.cart_item_supplement_authenticated = CartItem.objects.create(cart=self.cart_authenticated,
                                                                          name=self.supplement_product.name,
                                                                          price=self.supplement_product.price,
                                                                          quantity=1,
                                                                          product_id=self.supplement_product.id,
                                                                          product_type='supplement')
        self.cart_item_equipment_authenticated = CartItem.objects.create(cart=self.cart_authenticated,
                                                                         name=self.equipment_product.name,
                                                                         price=self.equipment_product.price, quantity=3,
                                                                         product_id=self.equipment_product.id,
                                                                         product_type='gym_equipment')

    def test_complete_order_successful_redirect(self):

        response = self.client.post(reverse('complete order'), {
            'address': '123 Test Street',
            'city': 'Test City',
            'region': 'Test Region',
            'zipcode': '12345'
        })

        self.assertRedirects(response, reverse('payment'))

    def test_render_form_with_get_request(self):
        response = self.client.get(reverse('complete order'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'complete_order.html')

    def test_authenticated_user_order_creation(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('complete order'), {
            'address': '123 Test Street',
            'city': 'Test City',
            'region': 'Test Region',
            'zipcode': '12345'
        })

        order = Order.objects.filter(user=self.user).first()

        self.assertIsNotNone(order)
        self.assertEqual(order.user, self.user)

    def test_order_item_creation(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('complete order'), {
            'address': '123 Test Street',
            'city': 'Test City',
            'region': 'Test Region',
            'zipcode': '12345'
        })

        order = Order.objects.filter(user=self.user).first()
        order_items = OrderItem.objects.filter(order=order)

        self.assertEqual(order_items.count(), 2)
        self.assertTrue(order_items.filter(name=self.supplement_product.name).exists())
        self.assertTrue(order_items.filter(name=self.equipment_product.name).exists())
