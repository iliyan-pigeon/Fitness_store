from django.test import TestCase, Client
from django.urls import reverse
from Fitness_store.fitness_app.models import GymEquipment


class GymEquipmentPageViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_gym_equipment_page_view(self):
        response = self.client.get(reverse('gym equipment'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gym_equipment.html')
        self.assertTrue('object_list' in response.context)
        self.assertTrue(all(isinstance(item, GymEquipment) for item in response.context['object_list']))
        for equipment in response.context['object_list']:
            self.assertContains(response, equipment.name)
        self.assertNotContains(response, 'This text should not be in the supplements page')
        