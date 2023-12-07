from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from Fitness_store.fitness_app.forms import LoginForm
from Fitness_store.fitness_app.views import LoginUserView

UserModel = get_user_model()


class LoginUserViewTest(TestCase):

    def setUp(self):
        self.login_url = reverse('login')
        self.homepage_url = reverse('homepage')

        self.user = UserModel.objects.create_user(username='testuser', password='testpassword')

    def test_login_user_view(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertIsInstance(response.context['form'], LoginForm)

    def test_login_success(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(self.login_url, data, follow=True)

        self.assertRedirects(response, self.homepage_url)
        self.assertTrue(response.context['user'].is_authenticated)
