from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from Fitness_store.fitness_app.forms import CustomPasswordChangeForm

UserModel = get_user_model()


class PasswordChangeViewTest(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.url = reverse('password change')
        self.password_change_data = {
            'old_password': 'testpassword',
            'new_password1': 'newpassword123',
            'new_password2': 'newpassword123',
        }

    def test_password_change_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'password_change.html')

    def test_password_change_success(self):
        response = self.client.post(self.url, self.password_change_data, follow=True)
        self.assertRedirects(response, reverse('password change done'))
        self.assertTrue(response.context['user'].check_password('newpassword123'))

    def test_password_change_form(self):
        form = PasswordChangeForm(user=self.user, data=self.password_change_data)
        self.assertTrue(form.is_valid())

    def test_custom_password_change_form(self):
        form = CustomPasswordChangeForm(user=self.user, data=self.password_change_data)
        self.assertTrue(form.is_valid())
