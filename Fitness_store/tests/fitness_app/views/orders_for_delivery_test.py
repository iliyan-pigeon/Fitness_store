from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from Fitness_store.fitness_app.models import Order
from Fitness_store.fitness_app.views import orders_for_delivery

UserModel = get_user_model()


class OrdersForDeliveryViewTest(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create(username='testuser', email='test@example.com')
        self.order1 = Order.objects.create(user=self.user, address='Address 1', city='City 1', region='Region 1',
                                           zipcode='12345')
        self.order2 = Order.objects.create(user=self.user, address='Address 2', city='City 2', region='Region 2',
                                           zipcode='67890')

    def test_orders_for_delivery_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('orders for delivery'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders_for_delivery.html')
        self.assertInHTML(self.order1.address, 'Address 1')
        self.assertInHTML(self.order2.address, 'Address 2')
