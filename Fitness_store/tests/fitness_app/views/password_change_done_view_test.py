from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

UserModel = get_user_model()


class PasswordChangeDoneViewTest(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.url = reverse('password change done')

    def test_password_change_done_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'password_change_done.html')