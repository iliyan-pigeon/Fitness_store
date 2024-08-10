from django.test import TestCase
from django.urls import reverse
from Fitness_store.fitness_app.models import Order
from Fitness_store.fitness_app.views import order_details


class OrderDetailsViewTest(TestCase):

    def setUp(self):
        self.order = Order.objects.create(address='123 Main St', city='City', region='Region', zipcode='12345')
        self.order_id = self.order.pk

    def test_order_details_view(self):
        response = self.client.get(reverse('order details', kwargs={'pk': self.order_id}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_details.html')
        self.assertInHTML(self.order.address, '123 Main St')
