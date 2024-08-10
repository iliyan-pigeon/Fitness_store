from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class ProfileDeleteViewTest(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(username='testuser', password='testpassword')
        self.delete_url = reverse('profile delete', kwargs={'pk': self.user.pk})

    def test_profile_delete_view_get(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.delete_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_delete.html')

    def test_profile_delete_view_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.delete_url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('homepage'))
        self.assertFalse(UserModel.objects.filter(username='testuser').exists())
