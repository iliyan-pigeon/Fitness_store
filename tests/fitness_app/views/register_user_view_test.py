from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from Fitness_store.fitness_app.forms import RegisterUserForm

UserModel = get_user_model()


class RegisterUserViewTest(TestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.homepage_url = reverse('homepage')

    def test_register_user_view(self):
        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        self.assertIsInstance(response.context['form'], RegisterUserForm)

    def test_register_user_success(self):
        data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'gender': 'M',
        }
        response = self.client.post(self.register_url, data)
        user_count = UserModel.objects.filter(username='testuser').count()
        user = UserModel.objects.get(username='testuser')

        self.assertEqual(user_count, 1)
        self.assertRedirects(response, self.homepage_url)
        self.assertTrue(user.is_authenticated)
