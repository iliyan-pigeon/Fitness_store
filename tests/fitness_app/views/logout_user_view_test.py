from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class LogoutUserViewTest(TestCase):

    def setUp(self):
        self.logout_url = reverse('logout')
        self.login_url = reverse('login')
        self.homepage_url = reverse('homepage')

        self.user = UserModel.objects.create_user(username='testuser', password='testpassword')

    def test_logout_user_view(self):
        self.client.login(username='testuser', password='testpassword')

        self.assertTrue(self.client.session['_auth_user_id'])

        response = self.client.get(self.logout_url)

        self.assertRedirects(response, self.homepage_url)
        self.assertFalse(self.client.session.get('_auth_user_id'))
