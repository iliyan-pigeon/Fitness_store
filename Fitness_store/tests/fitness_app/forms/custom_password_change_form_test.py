from django.test import TestCase
from Fitness_store.fitness_app.forms import CustomPasswordChangeForm
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class CustomPasswordChangeFormTest(TestCase):

    def test_valid_password_change(self):
        user = UserModel.objects.create_user(username='testuser', password='testpassword123')
        form_data = {
            'old_password': 'testpassword123',
            'new_password1': 'newtestpassword123',
            'new_password2': 'newtestpassword123'
        }
        form = CustomPasswordChangeForm(user=user, data=form_data)
        self.assertTrue(form.is_valid())
