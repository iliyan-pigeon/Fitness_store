from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from Fitness_store.fitness_app.forms import ProfileEditForm

UserModel = get_user_model()


class ProfileEditViewTest(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(username='testuser', password='testpassword')
        self.edit_url = reverse('profile edit', kwargs={'pk': self.user.pk})

    def test_edit_view_access(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.edit_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_edit.html')

    def test_edit_view_redirect(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'username': 'testuser2'
        }

        response = self.client.post(self.edit_url, data)

        self.assertEqual(response.status_code, 200)

    def test_edit_view_context_data(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.edit_url)

        self.assertTrue('form' in response.context)

        form = response.context['form']

        self.assertIsInstance(form, ProfileEditForm)
