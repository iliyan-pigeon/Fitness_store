from django.test import TestCase
from django.urls import reverse

from Fitness_store.fitness_app.forms import CustomSetPasswordForm


class CustomPasswordResetConfirmViewTest(TestCase):

    def test_custom_password_reset_confirm_view(self):
        reset_confirm_url = reverse('password_reset_confirm', kwargs={'uidb64': 'someuid', 'token': 'sometoken'})
        response = self.client.get(reset_confirm_url)

        self.assertTemplateUsed(response, 'password_reset_confirm.html')

