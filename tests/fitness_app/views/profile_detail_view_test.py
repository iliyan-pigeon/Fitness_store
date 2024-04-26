from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class ProfileDetailViewTest(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(username='testuser', password='testpassword')
        self.profile_url = reverse('profile detail', kwargs={'pk': self.user.pk})

    def test_profile_detail_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.profile_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_details.html')

    def test_profile_context_data(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(self.profile_url)

        self.assertTrue('object' in response.context)
