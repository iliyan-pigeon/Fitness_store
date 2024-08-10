from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from Fitness_store.fitness_app.models import Supplements, GymEquipment

UserModel = get_user_model()


class SearchProductViewTest(TestCase):

    def setUp(self):
        self.supplement1_data = {
            'name': 'Test Supplement',
            'description': 'This is a test supplement description.',
            'amount': 100,
            'amount_type': 'mg',
            'price': 10.99,
            'amount_in_stock': 50,
            'photo': SimpleUploadedFile('test_photo.jpg', b'content', content_type='image/jpeg')
        }

        self.equipment1_data = {
            'name': 'Test Gym Equipment',
            'description': 'This is a test gym equipment description.',
            'price': 10.99,
            'amount_in_stock': 50,
            'photo': SimpleUploadedFile('test_photo.jpg', b'content', content_type='image/jpeg')
        }
        self.supplement2_data = {
            'name': 'Test Supplement2',
            'description': 'This is a test supplement description2.',
            'amount': 200,
            'amount_type': 'mg',
            'price': 10.99,
            'amount_in_stock': 50,
            'photo': SimpleUploadedFile('test_photo.jpg', b'content', content_type='image/jpeg')
        }

        self.equipment2_data = {
            'name': 'Test Gym Equipment2',
            'description': 'This is a test gym equipment description2.',
            'price': 10.99,
            'amount_in_stock': 50,
            'photo': SimpleUploadedFile('test_photo.jpg', b'content', content_type='image/jpeg')
        }

        self.user = UserModel.objects.create_user(username='testuser', password='testpassword')
        self.supplement1 = Supplements.objects.create(**self.supplement1_data)
        self.supplement2 = Supplements.objects.create(**self.supplement2_data)
        self.gym_equipment1 = GymEquipment.objects.create(**self.equipment1_data)
        self.gym_equipment2 = GymEquipment.objects.create(**self.equipment2_data)

    def test_search_product_with_valid_query(self):
        query = 'Supplement'
        response = self.client.get(reverse('search product'), {'search_query': query})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_results.html')
        self.assertInHTML('Test Supplement', self.supplement1.name)
        self.assertInHTML('Test Supplement2', self.supplement2.name)

    def test_search_product_with_no_results(self):
        # Simulate a query with no matching results
        query = 'Nonexistent Product'
        response = self.client.get(reverse('search product'), {'search_query': query})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_results.html')
        self.assertQuerysetEqual(response.context['supplements'], [])
        self.assertQuerysetEqual(response.context['gym_equipment'], [])
